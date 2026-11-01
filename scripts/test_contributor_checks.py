"""Tests for contributor link and avatar checks. Run: python3 -m unittest discover -s scripts"""
from __future__ import annotations

import struct
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_catalog  # noqa: E402
from contributor_checks import avatar_problem, link_problem  # noqa: E402


def png(w: int, h: int, extra: list[bytes] = (), tail: bytes = b"", text: list[bytes] = ()) -> bytes:
    def chunk(t: bytes, body: bytes) -> bytes:
        return struct.pack(">I", len(body)) + t + body + struct.pack(">I", zlib.crc32(t + body))
    ihdr = chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
    others = b"".join(chunk(t, b"x") for t in extra) + b"".join(chunk(b"tEXt", k + b"\0value") for k in text)
    return b"\x89PNG\r\n\x1a\n" + ihdr + others + chunk(b"IDAT", zlib.compress(b"\0")) + chunk(b"IEND", b"") + tail


def jpeg(w: int, h: int, segments: list[int] = ()) -> bytes:
    def seg(marker: int, body: bytes) -> bytes:
        return bytes([0xFF, marker]) + struct.pack(">H", len(body) + 2) + body
    app0 = seg(0xE0, b"JFIF\0\x01\x01\0\0\x01\0\x01\0\0")
    extra = b"".join(seg(m, b"Exif\0\0data") for m in segments)
    sof = seg(0xC0, struct.pack(">BHHB", 8, h, w, 1) + b"\x01\x11\x00")
    sos = seg(0xDA, b"\x01\x01\x00\x00\x3f\x00")
    return b"\xff\xd8" + app0 + extra + sof + sos + b"\x00" + b"\xff\xd9"


class Links(unittest.TestCase):
    def ok(self, key, url):
        self.assertIsNone(link_problem(key, url), url)

    def bad(self, key, url):
        self.assertIsNotNone(link_problem(key, url), url)

    def test_accepts(self):
        self.ok("website", "https://grcmana.com/about?x=1#y")
        self.ok("linkedin", "https://www.linkedin.com/in/someone")
        self.ok("linkedin", "https://linkedin.com/in/someone")
        self.ok("x", "https://twitter.com/someone")
        self.ok("youtube", "https://www.youtube.com/@someone")
        self.ok("medium", "https://medium.com/@someone")
        self.ok("medium", "https://someone.medium.com/")
        self.ok("tiktok", "https://www.tiktok.com/@someone")
        self.ok("facebook", "https://www.facebook.com/someone")

    def test_rejects_lookalike_hosts(self):
        self.bad("linkedin", "https://www.linkedin.com.evil.example/in/x")
        self.bad("linkedin", "https://uk.linkedin.com/in/x")
        self.bad("youtube", "https://youtu.be/abc")
        self.bad("facebook", "https://fb.com/x")
        self.bad("medium", "https://evilmedium.com/@x")
        self.bad("x", "https://x.com.evil.example/")

    def test_rejects_unsafe_shapes(self):
        self.bad("website", "http://grcmana.com")
        self.bad("website", "javascript:alert(1)")
        self.bad("website", "https://user:pw@grcmana.com/")
        self.bad("website", "https://evil.example@grcmana.com/")
        self.bad("website", "https://grcmana.com:8443/")
        self.bad("website", "https://grcmana.com/a b")
        self.bad("website", "https://grcmana.com/\\x")
        self.bad("website", "https://grcmana.com/\x07")
        self.bad("website", "https://localhost/")
        self.bad("website", "https://127.0.0.1/")
        self.ok("website", "https://xn--bcher-kva.de/")
        self.bad("website", "https://foo<bar>.com/")
        self.bad("website", "https://")
        self.bad("website", "https://grcmana.com/" + "a" * 300)


class Avatars(unittest.TestCase):
    def test_accepts_clean_images(self):
        self.assertIsNone(avatar_problem("avatar.png", png(256, 256, [b"sRGB", b"pHYs"])))
        self.assertIsNone(avatar_problem("avatar.png", png(256, 256, text=[b"date:create", b"Software"])))
        self.assertIsNone(avatar_problem("avatar.jpg", jpeg(256, 256, [0xFE])))  # "Created with GIMP"
        self.assertIsNone(avatar_problem("avatar.jpg", jpeg(512, 512, [0xE2])))  # ICC profile is fine
        self.assertIsNone(avatar_problem("avatar.jpeg", jpeg(400, 400)))

    def test_rejects(self):
        cases = {
            "not square": ("avatar.png", png(300, 256)),
            "too small": ("avatar.jpg", jpeg(128, 128)),
            "animated": ("avatar.png", png(256, 256, [b"acTL"])),
            "png xmp": ("avatar.png", png(256, 256, text=[b"XML:com.adobe.xmp"])),
            "png raw exif": ("avatar.png", png(256, 256, text=[b"Raw profile type exif"])),
            "png exif": ("avatar.png", png(256, 256, [b"eXIf"])),
            "trailing data": ("avatar.png", png(256, 256, tail=b"hidden")),
            "jpeg exif": ("avatar.jpg", jpeg(256, 256, [0xE1])),
            "jpeg iptc": ("avatar.jpg", jpeg(256, 256, [0xED])),
            "jpeg named png": ("avatar.png", jpeg(256, 256)),
            "svg": ("avatar.png", b"<svg xmlns='http://www.w3.org/2000/svg'/>"),
            "truncated header": ("avatar.png", png(256, 256)[:20]),
            "truncated body": ("avatar.png", png(256, 256)[:-6]),
            "truncated jpeg": ("avatar.jpg", jpeg(256, 256)[:12]),
            "too large": ("avatar.png", png(256, 256) + b"\0" * 600_000),
        }
        for label, (name, data) in cases.items():
            self.assertIsNotNone(avatar_problem(name, data), label)


class Folders(unittest.TestCase):
    BIO = "word " * 25

    def build(self, files: dict[str, bytes | str]) -> tuple[dict, list[str]]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "contributors").mkdir()
            (root / "contributors" / "README.md").write_text("guide")
            for rel, content in files.items():
                p = root / "contributors" / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(content if isinstance(content, bytes) else content.encode())
            old, build_catalog.ROOT = build_catalog.ROOT, root
            try:
                errors: list[str] = []
                return build_catalog.load_contributors(errors), errors
            finally:
                build_catalog.ROOT = old

    def profile(self, handle: str, extra: str = "") -> str:
        return f"---\nname: Someone\ngithub: {handle}\n{extra}---\n{self.BIO}\n"

    def test_valid_profile_with_avatar(self):
        people, errors = self.build({
            "someone/README.md": self.profile("someone", "x: https://x.com/someone\n"),
            "someone/avatar.png": png(256, 256),
        })
        self.assertEqual(errors, [])
        self.assertEqual(people["someone"]["avatar_file"], "contributors/someone/avatar.png")
        self.assertEqual(people["someone"]["avatar"], "https://github.com/someone.png")
        self.assertEqual(people["someone"]["links"], {"x": "https://x.com/someone"})

    def test_no_avatar_is_null(self):
        people, errors = self.build({"someone/README.md": self.profile("someone")})
        self.assertEqual(errors, [])
        self.assertIsNone(people["someone"]["avatar_file"])

    def test_layout_errors(self):
        cases = {
            "old flat file": {"someone.md": self.profile("someone")},
            "two avatars": {"someone/README.md": self.profile("someone"),
                            "someone/avatar.png": png(256, 256), "someone/avatar.jpg": jpeg(256, 256)},
            "stray file": {"someone/README.md": self.profile("someone"), "someone/photo.png": png(256, 256)},
            "missing profile": {"someone/avatar.png": png(256, 256)},
            "handle mismatch": {"someone/README.md": self.profile("other")},
            "bad folder name": {"Some_One/README.md": self.profile("some_one")},
            "old avatar key": {"someone/README.md": self.profile("someone", "avatar: avatar.png\n")},
            "bad link": {"someone/README.md": self.profile("someone", "linkedin: https://evil.example/\n")},
        }
        for label, files in cases.items():
            _, errors = self.build(files)
            self.assertTrue(errors, label)


if __name__ == "__main__":
    unittest.main()
