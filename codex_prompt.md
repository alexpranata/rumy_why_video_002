# CODEX TASK: Review and complete RUMY WHY Video 002 (Hoover Dam)

**Current state:** The project already includes a working offline video pipeline at `render.py`.
It has passed an end-to-end test using temporary synthetic inputs at reduced resolution and a 7-second test timeline. No synthetic test assets are included in this package or used as substitutes in final video creation.

Read `RUN.md`, `README.md`, `scenes.json`, `voiceover.txt`, `captions_rough.srt`, and `render.py` before changing any files.

## Your role
1. Confirm the project root and make sure command execution is working.
2. Run `python3 render.py --check`. Missing media is EXPECTED in the template ZIP.
3. Run `python3 -m unittest discover -s tests -v` to check deterministic helper functionality.
4. Improve the pipeline only where it benefits final export quality or resiliency. Prefer incremental edits over unnecessary rewrites. Read source media only from `assets/video` and `assets/audio`.
5. If supplied media is available, produce `output/revision_v2/rumy_why_002_v2.mp4` and inspect `output/revision_v2/render_report.json`.
6. If media is missing, do not fabricate, scrape, download, or generate substitute videos, speech, SFX, or music. Tell the user exactly what is missing.
7. Voiceover timing must be checked against SRT. Scene-timed captions are rough placeholders, not word-aligned transcripts.
8. Maintain early-1930s scene chronology and avoid representing AI reconstructions as authentic archive footage.
9. Preserve export defaults: portrait 1080x1920, 30fps, H.264 CRF ~20, AAC 192kbps, 14 scenes ~70s.

## Recovery for inaccessible workspace
If the command tool fails before executing **any** command, report the precise error and stop. Do not claim the project or media is damaged. Ask the user to restart/open a fresh Codex session with the extracted folder as workspace root.


## New: Adobe After Effects-inspired engineering motion graphics

The project now ships with editable `motion_graphics.py`, `motion_graphics.json`, and `MOTION_STYLE_GUIDE.md`. Keep the exact channel accent `#FFD400` across arrows, circles, highlight text and measurement lines. The renderer already composites the yellow vector ASS graphics.

Read these files, run unit tests, and inspect motion effects in the final exported footage. **Do not rebuild the motion system unnecessarily**; adjust per-scene positions to real subject areas once media exists. Do not assume overlays are tracked automatically. Keep captions above graphics and avoid lower UI-safe zone.


## REVISION v2: requested after first real render (priority)

The user says the first render felt stiff. Main title is satisfactory in style but should be **10–15% larger and placed upper-center**. The v2 config/renderer already implements `text_layout` with a centered x=0.5, y=0.125, headline size=64 px (was 56) and micro=30 px. Keep bottom narration subtitles separately positioned.

1. Audit pacing on actual user-provided Hoover Dam footage. Use expressive purposeful cuts, mild push-ins and occasional motion matches; avoid repetitive fixed-duration transitions or overbearing effects.
2. **Do not enable unverified shapes**. `motion_graphics.json` defaults all `geometry_verified=false`, hiding the previous floating arrows/rings/brackets. Inspect actual frames; add reliable motion keyframes / object tracking for each shape before enabling it. If real feature is unclear, retain title only.
3. For verified shape motion, modify drawing to follow **the footage object through time**, not just a fixed screen position; boolean `geometry_verified=true` alone does not implement tracking. Do not mark moving shots verified without keyframes/real tracking.
4. For real-photo overlays, inspect `REFERENCE_OVERLAY_SOURCES.md`. Suggest/download only images with usage rights checked and keep provenance; do not assume Library of Congress media are all public domain. When possible, add brief 1–3 s relevant archival inserts with small credits. If the user has not supplied approved photos and licensing is unresolved, leave them out and report missing images instead.
5. Run tests, create a lower-resolution preview and spot-check 4–5 representative frames before final rendering. Do not overwrite original source assets or confuse preview with final MP4.
