# RUMY WHY Video #002 — edit and QA

## Edit decisions

- Existing 14 clips remain in their original storytelling order. All 15 media-file SHA-256 checksums match the pre-edit inventory in `qa/source_inventory.json`.
- Original voiceover retained in full, without time stretching: container duration 69.250612 seconds; decoded speech reaches approximately 69.2 seconds. Timeline remains 70 seconds, with a short ending hold.
- Local PocketSphinx 5.0.4 forced alignment against the supplied script produced the word estimates in `qa/narration_alignment.json`. This constrains alignment to the approved wording; it is not an independent transcript or listening review. Numeric phrases were expanded for alignment and kept as digits in captions.
- Scene cuts follow phrase pauses, quantized to 30 fps. `scenes.json` contains editable `trim_start_sec` values, cuts, and durations. All selections fit actual source durations, including the four approximately six-second clips.
- Captions now use 42 short phrases instead of 14 fixed five-second blocks. No words were removed. Subtitle timing remains an automatic estimate needing final listening confirmation.
- Native clip camera motion is retained; additional digital zooms were removed to reduce target drift. The renderer bounds each scene by frame count to prevent cumulative frame rounding drift.
- All new technical annotations use #FFD400. Labels occupy the upper safe area; captions remain lower in the frame. Drilling and excavation rings identify visible work rather than claiming an invisible bedrock boundary. The four-tunnel fact uses an underline rather than a misleading calibrated span across the river. The 1936 label enters during that part of the narration.
- Per-scene `enter_sec` and `hold_sec` control brief fixed overlays. These are manually positioned screen annotations, not automatic tracking. Supporting measurement brackets are illustrative rather than calibrated surveys.
- No replacement/generated footage, voice, music, or paid generation APIs. No optional licensed music was supplied; the mix uses the narration only, not original clip audio.

## Validation

- `python3 render.py --check`: all required media and libass available.
- `python3 -m unittest discover -s tests -v`: 10 tests passed, including late annotation entry/hold timing and ordered non-overlapping captions.
- 360x640 preview rendered and all 14 annotated scene samples visually reviewed before the master export.
- Final export checks and representative final frames are recorded in `qa/export_validation.json` and `qa/final_contact_*.jpg`.
- `render_report.json` records the actual final render, source selections, narration length, and renderer warnings.

## Remaining review

- Listen to the final export at normal speed to confirm pronunciation, the automatically estimated caption boundaries, and the transition around “not as one giant slab, but in hundreds…”. No human listening sign-off is claimed.
- Scene 2 contains a baked-in split-view inset and structures that should not be treated as an authenticated pre-construction view. Scene 3 contains baked-in colored route markings. Several construction clips have internal transitions and illustrative geometry. These are supplied-media limitations; no asset was altered to disguise them.
- The original 720x1280 clips are upscaled to the requested 1080x1920 export; annotations render at export resolution. AI reconstructions are illustrative, not archival footage or engineering diagrams. MP4 metadata retains that disclosure.
- Short fixed rings/arrows are reviewed at representative times, not frame-by-frame tracked. Check target drift on a phone before publication, especially drilling, excavation, and cooling-pipe shots. Keep platform UI overlays in mind.
- Numeric facts are carried over from the supplied narration/configuration. The checkout contains no cited README or source dossier; independent historical fact verification was not performed in this local-only edit.

Final checks completed: exactly 2,100 video frames / 70.000 seconds; H.264 1080x1920 at 30 fps, AAC at 48 kHz; full decode passed; no black intervals detected at the documented threshold; decoded peak -2.8 dBFS. All 14 representative final annotated frames were inspected with clear caption/callout separation. All 15 source hashes remain unchanged.
