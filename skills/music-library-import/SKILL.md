---
name: music-library-import
description: Find and acquire a user-requested album from a supplied website or other legitimate source, compare available audio quality against the user's stated target, verify track completeness, organize files in iCloud Drive, and import them into Apple Music. Use when a user asks to download, organize, or import an album into their Music library.
metadata:
  short-description: 核对音质与曲目后归档并导入 Apple Music
---

# Music album acquisition and Apple Music import

## Required first decision

Before searching or downloading, ask which quality target the user wants: lossless (ALAC/FLAC/WAV), or a lossy format and minimum bitrate (AAC/MP3). Do not infer their preferred quality from a prior task. Explain that file extensions and advertised labels alone do not prove quality. If they have already stated the target in the current request, use it without asking again.

## Source and quality checks

1. Start with the website or album page the user supplied. Confirm the exact release, edition, artist, and album; distinguish standard, deluxe, remaster, and bonus-track editions.
2. Check that the source is authorized and actually offers a download to the user. Prefer official artist/label stores and reputable stores with explicit download rights. A streaming URL, cached CDN URL, or a site's assertion of consent does not by itself establish download authorization. Never rip streams, defeat DRM, evade password/paywall/CAPTCHA/access checks, or use another person's credentials. If access control blocks the download, stop and explain the exact user action needed through the site's normal process. A fresh private window may be used to diagnose an ordinary stale session or cache issue, but never to evade access controls.
3. Compare the supplied source against the user's target and any clearly higher-quality authorized sources. For lossless requests, verify lossless codec/container and inspect actual sample rate, bit depth, channel count, and (where feasible) lossless encoding or source evidence. Flag suspicious upsampling or unsupported “Hi-Res” claims; a larger sample rate does not by itself prove a better master. For lossy requests, record codec and bitrate and compare actual available options.
4. Apply the user's priority: obtain the requested lossless format if an authorized source offers it; otherwise identify the best legally available alternative, state its actual format/bitrate and limitation, then ask whether to proceed if that changes the requested outcome. Do not buy anything without explicit confirmation of the price and purchase.
5. Before downloading, confirm expected track count and sequence against a reliable release listing (label, distributor, or reputable catalog). Include bonus tracks only if the requested edition contains them.

## Download, organize, verify

1. Use the user's named destination. If they ask for iCloud and no album folder exists, create an album-named folder inside iCloud Drive. Do not overwrite existing files; inspect collisions and choose a safe new name or ask.
2. Download only the selected album audio from the authorized download flow. Keep source files unchanged. Do not download unrelated files bundled by a site.
3. Verify every file is present, readable, nonzero, and has the expected container/codec. Check track tags, track numbers, album, artist, and album artist; correct metadata only in a separate copy if needed. Compare the actual file count and ordering to the expected release tracklist and report any mismatch before import.
4. Apple Music may not import FLAC directly. If needed, make separate ALAC copies with Apple's supported conversion or a local system conversion tool; preserve the downloaded originals. Do not claim conversion improves source fidelity.
5. Import through the Music app's normal File > Import flow. Do not use scripts or private APIs to alter Music's database. Confirm the album appears in the library with the intended artist/album metadata and expected track count/order. If Music displays waiting/analyzing or cloud-sync status, report that the local library import is complete while sync or analysis is still pending.
6. Distinguish local presence in iCloud Drive from confirmed cloud synchronization. Verify only what the available status actually shows.

## Completion report

State the source and authorization evidence, exact audio format and measured properties, expected versus imported track count, iCloud destination, whether original files were preserved, and Apple Music import/sync status. Mark unknowns as unverified. Keep the report brief and do not claim audio quality beyond what the file metadata and source evidence establish.
