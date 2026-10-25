# Music album acquisition and Apple Music import

[English](README.md) · [简体中文](README.zh-CN.md)

This skill guides album acquisition from a user-supplied site or another legitimate download source, compares the actual available audio format with the user's stated quality target, checks the edition and tracklist, organizes files in iCloud Drive, and imports them through Apple Music.

It requires asking the user for a quality target before searching unless they already specified one. It prioritizes authorized lossless downloads, verifies actual file properties rather than trusting labels, and preserves downloaded originals when ALAC copies are needed for Music. It never bypasses DRM, passwords, CAPTCHA, paywalls, or other access controls, and it never rips streaming audio. A private window may diagnose ordinary session or cache problems only. Purchases require explicit price confirmation.

The final check confirms the album, artist, track count and order in the Music library. Local iCloud placement is reported separately from cloud synchronization, and pending analysis or sync is not described as complete.
