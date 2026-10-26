# Hoover Dam Revision v2 — edit and QA

Revision files applied from GitHub main at fd53fb58d7c75ff4e4aef509b191caae05c1e488. The prior locally synced narration and phrase captions are retained. Previous edit files are archived at `/workspace/video-review/revision-v2-backup/previous-edit-files.zip`.

## Preserved material

- All 14 original video assets and the original voiceover remain unchanged. Their SHA-256 values are recorded in `qa/preservation.json`.
- The previous final remains at `output/rumy_why_002.mp4`, SHA-256 `a3d723c3ad2071d4d23f856fa4df0d30231ab843f9967e55936b934e279a3d02`. Its report and QA files are preserved.
- New preview, final and reports live under `output/revision_v2/`. The renderer now defaults to the v2 destination.

## Picture and text changes

- v2 top-center headline at x=0.50, y=0.125: 64 px yellow #FFD400, 14.3% larger than the 56 px original. Centered 30 px off-white micro labels sit below. Entrance is a slight vertical rise and fade. Narration captions remain separate near the bottom.
- Original 70-second narration-paced cuts and 42 short phrase captions are retained. Cut timing is quantized to 30 fps; no narration is shortened or stretched.
- Opening selection starts at source 0.8 seconds to reveal the dam face earlier. Selective opening push-in and closing pull-back use the existing renderer; other shots retain native camera motion. Hard cuts preserve construction chronology and avoid transition padding.
- No decorative measurement lines, floating rings, or unsupported bedrock identification. The foundation heading now says FOUNDATION WORK.
- All geometry is disabled by default. Only scene 11 has `geometry_verified: true`: a two-second arrow to the visible upper cooling-pipe bend, with five manually reviewed screen-space keyframes. It is interpolated at 30 fps, with a short fade in/out. This is manual editorial keyframing, not automatic feature tracking. The other 13 scene geometries remain off.

## Preview review

A 360x640, 30 fps preview was rendered before the master. All 14 title/caption scene samples were visually reviewed; the top-center text is readable with no caption overlap. Five additional samples during the scene 11 arrow show its endpoint following the visible pipe bend. Review sheets are in `qa/v2_preview_contact_*.jpg` and `qa/v2_pipe_overlay.jpg`.

## Optional archival photographs

No external photo is included. The supplied source manifest and rights caveats were reviewed. Live requests to Bureau of Reclamation and Library of Congress were blocked by this environment's proxy (CONNECT 403), preventing independent image/rights confirmation. Government hosting is not blanket image clearance. The LOC 1933 candidate remains excluded because its supplied advisory says rights status not evaluated; the 2018 image is modern, not 1930s archival evidence. See `REFERENCE_OVERLAY_SOURCES.md` for the detailed review. Future inserts need both rights verification and an explicit overlay implementation.

## Validation and limits

- Initial check found all required media, FFmpeg and libass. All 13 unit tests passed, including geometry suppression, keyframe interpolation, invalid key order, and late title timing.
- Master validation is recorded in `qa/export_validation.json` and `qa/decode.log` after rendering.
- Original sources are 720x1280, upscaled to 1080x1920; titles and vector graphics render at export resolution.
- Caption boundaries are local forced-alignment estimates from the previous edit; a final listening review is still needed. No human listening sign-off is claimed.
- Baked-in reconstruction issues remain, including the scene 2 split-view inset, scene 3 colored markings, internal source edits, and illustrative rather than historically authenticated geometry. No original asset was altered to conceal these. These visuals are not archival footage.
- No paid APIs, replacement footage, synthesized voice, or unlicensed music. Narration-only mix.

Master verification completed: 2,100 frames, exactly 70.000 seconds, H.264 1080x1920 at 30 fps and AAC at 48 kHz. Full decode passed; no black intervals detected at the documented threshold. Original media and previous final hashes still match.

All 14 representative final master frames were also reviewed after export, confirming upper-center title placement and caption separation at full export resolution. Decoded peak is -2.8 dBFS.
