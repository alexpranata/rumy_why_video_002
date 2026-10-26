# CODEX TASK: Review and complete RUMY WHY Video 002 (Hoover Dam)

**Current state:** The project already includes a working offline video pipeline at `render.py`.
It has passed an end-to-end test using temporary synthetic inputs at reduced resolution and a 7-second test timeline. No synthetic test assets are included in this package or used as substitutes in final video creation.

Read `RUN.md`, `README.md`, `scenes.json`, `voiceover.txt`, `captions_rough.srt`, and `render.py` before changing any files.

## Your role
1. Confirm the project root and make sure command execution is working.
2. Run `python3 render.py --check`. Missing media is EXPECTED in the template ZIP.
3. Run `python3 -m unittest discover -s tests -v` to check deterministic helper functionality.
4. Improve the pipeline only where it benefits final export quality or resiliency. Prefer incremental edits over unnecessary rewrites. Read source media only from `assets/video` and `assets/audio`.
5. If supplied media is available, produce `output/rumy_why_002.mp4` and inspect `output/render_report.json`.
6. If media is missing, do not fabricate, scrape, download, or generate substitute videos, speech, SFX, or music. Tell the user exactly what is missing.
7. Voiceover timing must be checked against SRT. Scene-timed captions are rough placeholders, not word-aligned transcripts.
8. Maintain early-1930s scene chronology and avoid representing AI reconstructions as authentic archive footage.
9. Preserve export defaults: portrait 1080x1920, 30fps, H.264 CRF ~20, AAC 192kbps, 14 scenes ~70s.

## Recovery for inaccessible workspace
If the command tool fails before executing **any** command, report the precise error and stop. Do not claim the project or media is damaged. Ask the user to restart/open a fresh Codex session with the extracted folder as workspace root.


## New: Adobe After Effects-inspired engineering motion graphics

The project now ships with editable `motion_graphics.py`, `motion_graphics.json`, and `MOTION_STYLE_GUIDE.md`. Keep the exact channel accent `#FFD400` across arrows, circles, highlight text and measurement lines. The renderer already composites the yellow vector ASS graphics.

Read these files, run unit tests, and inspect motion effects in the final exported footage. **Do not rebuild the motion system unnecessarily**; adjust per-scene positions to real subject areas once media exists. Do not assume overlays are tracked automatically. Keep captions above graphics and avoid lower UI-safe zone.
