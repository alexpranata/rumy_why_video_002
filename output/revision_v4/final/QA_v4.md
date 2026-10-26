# Hoover Dam v4 — animated graphics on footage

This revision addresses the requested graphical animation: moving river arrows and an animated dam-height dimension on the existing scene footage. It does not add a standalone Blender segment or generate new source video.

## Visible graphics

- **River arrows, approximately 5.37–7.97 s:** three yellow arrowheads travel along a curved guide fitted to the visible river centerline. The centerline changes with manually reviewed camera keyframes rather than remaining fixed on the screen. Source/timeline samples and optional optical-flow checks are in `../qa/`. Water texture tracking was compared with bank motion to avoid treating camera movement alone as water motion. The arrow speed is illustrative and does not encode a measured flow rate.
- **Dam height, approximately 63.20–65.60 s:** a yellow dimension line draws from crest-level to lower-face-level, with end caps. The number counts up to **726 FT**, then displays **221 m** and **TOTAL HEIGHT**. Line endpoints and label position follow manually fitted camera keys. Published total height includes foundation rock; the on-screen bracket is an illustrative callout, not a survey or a pixel-calibrated measurement of the exposed face.
- Both features use #FFD400, dark outlines, short fades and export-frame-cadence vector geometry. Caption and top-title layouts remain separate. Height numeral size was increased after preview review for phone readability.
- All other unreviewed object geometry remains disabled. The five supplemental selections, original pouring fallback, full narration and 70-second timeline from v3 remain unchanged.

## Review and reproduction

The first full preview was rendered before the master. Frame samples across four phases of each animation were inspected, showing moving arrow positions, line reveal, numeric progression and camera alignment. The final downloadable preview and short silent graphics showcase are generated from the verified master so their graphical appearance matches it.

```bash
python3 render.py --output output/revision_v4/final/rumy_why_002_v4.mp4
```

The default output now uses the v4 destination. Render dependencies remain Python standard library and FFmpeg with libass. OpenCV was used only as an optional local analysis tool for motion clues, not as a rendering dependency. No paid generation APIs were called.

## Checks and remaining limits

- All 21 tests passed, including changing flow geometry, geometry verification gating, dimension labels reaching the published height, matched keyframe structure, and interpolation endpoints.
- Full master decode, stream/duration/frame checks and file-preservation checks are recorded in `qa/export_validation.json` after rendering.
- Original 14 videos, narration, all supplemental sources and earlier masters are preserved. The graphic model is stored separately from source media in `motion_graphics.json`.
- These source images remain illustrative AI reconstructions. Manual camera-fit keys and optical-flow clues are not automatic 3D tracking or hydraulic verification. The measurement uses the published height; hidden foundations cannot be measured visually from the footage.
- Caption timing remains the prior local forced-alignment estimate and still merits normal-speed listening confirmation. Source geometry and reconstruction limitations from the v3 QA remain.

Master checks completed: 70.000 seconds / 2,100 frames, 1080x1920 at 30 fps, H.264/AAC. Full decode passed; no black intervals at the recorded detector threshold. Audio peak -2.8 dBFS. All 21 source files and three earlier masters match their hashes. Eight final animation-phase samples were inspected after export. The silent graphics showcase is 5.6 seconds / 168 frames.
