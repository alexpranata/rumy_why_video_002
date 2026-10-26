# Hoover Dam v3 — in-scene action direction preview

This is a 70-second **preview using the existing footage**, not an export containing newly generated Flow shots. No Blender prototype or reference-video frames are in the timeline.

## What changed

- Source action audit reviewed scenes 06, 09, 10 and 11 at five source times each: the cofferdam/worksite sequence, bucket pour, growing block structure and cooling-pipe cutaway. The sampled audit is in `qa/action_audit.jpg`.
- Retained the narration-aligned cuts and all 42 phrase captions. No narration is cut or time stretched.
- Added bounded detail crops for pouring, block construction and cooling pipes (scenes 09–11), bringing the action/objects forward within the original scenes.
- Headlines appear selectively on eight scenes. Other shots let footage and captions carry the explanation. Key technical terms in captions use #FFD400, including after an ASS line break. These highlights persist for a caption phrase; they are not word-by-word karaoke alignment.
- All object geometry is off. The earlier pipe arrow was disabled because the new crop changes its screen coordinates. There are no free-floating decorative rings or measurements.
- All original source videos, narration and previous v1/v2 masters remain untouched. New outputs stay in `output/revision_v3/`.

## What still needs new footage

The cooling-pipe source shows the network but does not clearly demonstrate internal water transport. River diversion can be clearer in an integrated portal/current shot. Optional new block-growth, pouring and clean canyon clips may improve physical continuity.

`production/FLOW_SHOT_REQUESTS_V3.md` contains six ready-to-use English prompts, Indonesian production/acceptance notes, scene/time mappings, proposed filenames and original-project reference frames. All requested supplemental clips remain **not generated and not included**. The JSON shot registry carries that status explicitly. The user generates these manually in Flow; no paid generation API is called.

## Validation and review limits

- All 16 unit tests passed, including caption highlighting after line breaks, selective headline suppression, and source crop bounds.
- Preview export: 540x960, 30 fps, H.264/AAC, 70 seconds. Full decode and frame-count results are recorded in `qa/preview_validation.json`.
- Representative frames from all 14 preview scenes were inspected. A final listening review is still needed for forced-aligned caption boundaries.
- Baked-in source limitations remain, including scene 02's inset/finished structures, scene 03's colored paths, internal transitions, and imperfect historical geometry. The new shot requests call these out where relevant.
- No archival photo or externally sourced overlay is used. Prior archival rights review remains unresolved for optional candidates.

A new master should be chosen after the supplemental Flow clips have been inspected and selected. This iteration delivers the editable preview and manual production pack, without claiming those requested new actions have been synthesized locally.
