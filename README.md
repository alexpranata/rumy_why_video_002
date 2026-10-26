# RUMY WHY | VIDEO 002 — HOOVER DAM

## Production target
- 14 clips generated in Google Flow at 8 seconds each; select best 5 seconds per clip in edit.
- Target output: 1080x1920, 30fps, MP4 H.264, AAC, ~70s.
- English narration by ElevenLabs, US-audience documentary tone. Output audio file to `assets/audio/voiceover.wav`.
- Google Flow-generated clips must be manually downloaded to `assets/video/scene_01.mp4` ... `scene_14.mp4`.
- `scenes.json` is the authoritative scene script, visual prompts, captions, and editing intent.
- Scene SRT is rough timing only; re-sync to actual ElevenLabs voice track prior to release.

## Story structure
1. Reveal monumental 726-foot height and problem of running river (0–10s).
2. Engineers divert Colorado River through four tunnels nearly three miles total (10–25s).
3. Cofferdams, bedrock excavation, and high scalers (25–40s).
4. Concrete block construction and embedded chilled water cooling pipes (40–60s).
5. 1935 concrete completion, all project features finished in 1936; reveal Hoover Dam (60–70s).

## Historical accuracy notes
- The four diversion tunnels were EXCAVATED to 56 ft diameter and finished at 50 ft after lining.
- Four tunnels collectively measured 15,946 feet, about 3 miles; they are not each three miles long.
- Dam itself contains ~3.25 million cubic yards concrete, different from ~4.36 million for full works.
- Concrete placed June 6, 1933 to May 29, 1935; full works completed by March 1, 1936.
- Dam height is 726.4 ft from foundation rock to roadway; round to 726 feet.
- Vertical interlocking blocks with ~215 blocks, not a single poured slab.
- Model scenes in early 1930s without modern bypass bridge, modern excavators, or modern protective gear.
- AI generated video is illustrative reconstruction, not historical source footage. Do not label it as archival video.

## Authentic sources
- U.S. Bureau of Reclamation dam FAQ: https://www.usbr.gov/lc/hooverdam/faqs/damfaqs.html
- U.S. Bureau of Reclamation tunnels FAQ: https://www.usbr.gov/lc/hooverdam/faqs/tunlfaqs.html
- U.S. Bureau of Reclamation tunnels narrative: https://www.usbr.gov/lc/hooverdam/history/essays/tunnels.html
- National Park Service engineering history: https://www.nps.gov/articles/4-bureau-of-reclamation-engineering-achievements.htm

## Folder structure
```
assets/video/scene_01.mp4 ... scene_14.mp4
assets/audio/voiceover.wav
assets/audio/music.mp3  # optional, properly licensed
scenes.json
voiceover.txt
captions_rough.srt
codex_prompt.md
output/
```

## Ready-to-run editing pipeline (updated package)

This version includes `render.py`, a functioning Python + FFmpeg video renderer, and `RUN.md` with setup commands. The renderer was exercised in a separate temporary end-to-end test and generated valid video and audio streams. Use `python3 render.py --check` to inspect source media requirements, then `python3 render.py` once clips and narration exist. Tests are in `tests/`.

## Motion graphics brand system — new
- `motion_graphics.json`: 14 editable scene-specific annotation presets; engineering yellow `#FFD400` for arrows, target rings, lines and highlight numbers.
- `motion_graphics.py`: uses vector ASS overlays with fade and slide animations; no After Effects installation or Python third-party dependencies needed.
- `MOTION_STYLE_GUIDE.md`: full brand guide, overlay timeline, constraints, review checklist.
- `render.py` composites motion graphics **below** burned-in voice captions.
- **Important:** positions are placeholders to be adjusted to real footage. These effects are not object-tracking.

## Codex reusable channel skill
- This project includes `.agents/skills/rumy-why-video-editing/SKILL.md`. Codex can discover and apply this skill to video editing and motion graphics work in this repository.
- For **all future RUMY WHY repositories**, install the same `rumy-why-video-editing/` folder into `~/.agents/skills/` on your Codex machine (user-level skills).
- The skill is a channel-wide editing policy, whereas `motion_graphics.json` and `scenes.json` are per-video data. The reusable skill does not generate missing Google Flow or ElevenLabs source assets.


### Motion graphics revision v2
Titles are 10–15% larger and placed at top-center. Unverified arrows, circles and measurement lines are disabled by default; add them back only after alignment/tracking review against actual footage. See `REFERENCE_OVERLAY_SOURCES.md` for possible authentic photo inserts and their rights caveats.
