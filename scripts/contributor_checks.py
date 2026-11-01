"""Checks for contributor profile links and avatars. Standard library only.

Links mirror the website's validator (grcskills-website src/lib/catalog/links.ts): the same
keys, hosts and limits. Where the two differ, this side is stricter, so a profile that passes
CI here never fails the site build. Hosts are compared on the parsed URL, never as a string
prefix, so https://www.linkedin.com.evil.example/ is not LinkedIn.

Avatars are personal data that the site serves byte for byte, so besides format and size we
reject embedded metadata: a phone photo's EXIF block can carry GPS coordinates.
"""
from __future__ import annotations

import re
import struct
from urllib.parse import urlsplit

# key -> (label, allowed hosts or None for any host, also allow *.<domain>, example)
# In the site's display order. GitHub is not here: it is derived from the handle.
LINK_PLATFORMS: dict[str, tuple[str, tuple[str, ...] | None, str | None, str]] = {
    "website": ("Website", None, None, "https://example.com"),
    "linkedin": ("LinkedIn", ("linkedin.com", "www.linkedin.com"), None,
                 "https://www.linkedin.com/in/<you>"),
    "x": ("X", ("x.com", "www.x.com", "twitter.com", "www.twitter.com"), None, "https://x.com/<you>"),
    "youtube": ("YouTube", ("youtube.com", "www.youtube.com"), None, "https://www.youtube.com/@<you>"),
    "medium": ("Medium", ("medium.com",), "medium.com", "https://medium.com/@<you>"),
    "tiktok": ("TikTok", ("tiktok.com", "www.tiktok.com"), None, "https://www.tiktok.com/@<you>"),
    "facebook": ("Facebook", ("facebook.com", "www.facebook.com"), None,
                 "https://www.facebook.com/<you>"),
}
LINK_MAX = 300
# Whitespace, control characters and backslashes, as on the site.
_BAD_CHARS = re.compile(r"[\s\x00-\x1f\x7f\\]")
# Stricter than the WHATWG URL parser, which fails on some characters Python accepts.
# Internationalised domains must be written in punycode (xn--...).
# The last label must start with a letter, which also rules out bare IP addresses.
_HOST = re.compile(r"^(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z](?:[a-z0-9-]*[a-z0-9])?$")


def link_problem(key: str, value: str) -> str | None:
    """Why `value` is not an acceptable `key` link, or None if it is."""
    label, hosts, subdomains_of, example = LINK_PLATFORMS[key]
    if len(value) > LINK_MAX:
        return f"must be at most {LINK_MAX} characters"
    if not value.startswith("https://") or _BAD_CHARS.search(value):
        return "must be an absolute https:// URL with no spaces or backslashes"
    parts = urlsplit(value)
    netloc = parts.netloc
    if "@" in netloc:
        return "must not contain credentials"
    if ":" in netloc:
        return "must not set a port"
    host = (parts.hostname or "").lower()
    if not _HOST.match(host):
        return "must have a plain domain name as its host (use punycode for non-ASCII domains)"
    if hosts is None:
        return None
    if host in hosts or (subdomains_of and host.endswith("." + subdomains_of)):
        return None
    allowed = ", ".join([*hosts, *([f"*.{subdomains_of}"] if subdomains_of else [])])
    return (f"must be a {label} URL on {allowed} (got {host}), e.g. {example}; "
            "put other links under 'website'")


# ---------------------------------------------------------------- avatars
AVATAR_MAX_BYTES = 500 * 1024  # same cap as the site
AVATAR_MIN_PX = 256
AVATAR_NAMES = ("avatar.png", "avatar.jpg", "avatar.jpeg")

PNG_SIG = b"\x89PNG\r\n\x1a\n"
# We reject the metadata that can carry location or personal details (EXIF, XMP, IPTC), not
# every comment: ffmpeg, GIMP and ImageMagick add harmless "Created with ..." or date text.
PNG_REJECT = {b"acTL": "is animated (APNG)", b"eXIf": "contains EXIF metadata"}
PNG_TEXT = {b"tEXt", b"zTXt", b"iTXt"}
# Text-chunk keywords that hold XMP, or EXIF/IPTC as ImageMagick stores them.
PNG_TEXT_REJECT = (b"XML:com.adobe.xmp", b"Raw profile type")
# JPEG segments: APP1 holds EXIF and XMP, APP13 holds IPTC.
JPEG_REJECT = {0xE1: "contains EXIF/XMP metadata (it can include GPS location)",
               0xED: "contains IPTC metadata"}
JPEG_SOF = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
STRIP_HINT = " Re-export it without metadata (see contributors/README.md)."


def _png_size(data: bytes) -> tuple[int, int]:
    """Width and height of a PNG; raises ValueError if it is malformed or not allowed."""
    pos, size, seen_end = len(PNG_SIG), None, False
    while pos < len(data):
        if pos + 12 > len(data):
            raise ValueError("is truncated")
        length, ctype = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + length]
        if len(body) != length:
            raise ValueError("is truncated")
        if size is None:
            if ctype != b"IHDR" or length != 13:
                raise ValueError("is not a valid PNG (no IHDR)")
            size = struct.unpack(">II", body[:8])
        if ctype in PNG_REJECT:
            raise ValueError(PNG_REJECT[ctype] + ("" if ctype == b"acTL" else "." + STRIP_HINT))
        if ctype in PNG_TEXT and body.split(b"\0", 1)[0].startswith(PNG_TEXT_REJECT):
            raise ValueError("contains EXIF/XMP/IPTC metadata (it can include GPS location)." + STRIP_HINT)
        pos += 12 + length
        if ctype == b"IEND":
            seen_end = True
            break
    if size is None or not seen_end:
        raise ValueError("is truncated")
    if pos != len(data):
        raise ValueError("has data after the end of the image")
    return size


def _jpeg_size(data: bytes) -> tuple[int, int]:
    """Width and height of a JPEG; raises ValueError if it is malformed or not allowed."""
    pos, size = 2, None
    while True:
        if pos + 4 > len(data) or data[pos] != 0xFF:
            raise ValueError("is not a valid JPEG")
        marker = data[pos + 1]
        if marker == 0xFF:  # fill byte
            pos += 1
            continue
        if marker == 0xDA:  # start of scan: headers are over
            break
        if marker in (0x01, *range(0xD0, 0xD8)):  # markers with no length
            pos += 2
            continue
        (length,) = struct.unpack(">H", data[pos + 2:pos + 4])
        if length < 2 or pos + 2 + length > len(data):
            raise ValueError("is truncated")
        if marker in JPEG_REJECT:
            raise ValueError(JPEG_REJECT[marker] + "." + STRIP_HINT)
        if marker in JPEG_SOF and length >= 7:
            h, w = struct.unpack(">HH", data[pos + 5:pos + 9])
            size = (w, h)
        pos += 2 + length
    if size is None:
        raise ValueError("is not a valid JPEG (no frame header)")
    return size


def avatar_problem(name: str, data: bytes) -> str | None:
    """Why the avatar file `name` with contents `data` is not acceptable, or None if it is."""
    if len(data) > AVATAR_MAX_BYTES:
        return f"is {len(data) // 1024} KB; must be at most {AVATAR_MAX_BYTES // 1024} KB"
    is_png = name.endswith(".png")
    if is_png and not data.startswith(PNG_SIG):
        return "is not a real PNG (check the file, not just its extension)"
    if not is_png and not data.startswith(b"\xff\xd8\xff"):
        return "is not a real JPEG (check the file, not just its extension)"
    try:
        w, h = _png_size(data) if is_png else _jpeg_size(data)
    except ValueError as e:
        return str(e)
    if w != h:
        return f"is {w}x{h}; it must be square"
    if w < AVATAR_MIN_PX:
        return f"is {w}x{h}; it must be at least {AVATAR_MIN_PX}x{AVATAR_MIN_PX}"
    return None
