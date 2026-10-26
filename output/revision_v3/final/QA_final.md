# Hoover Dam v3 final — supplemental footage integration

Six user-provided Flow clips were received from GitHub main commit `32600f8`. All are eight seconds, 1080x1920, 24 fps with readable video streams. Full hashes are in `qa/supplemental_inventory.json`. This review used start/middle/end samples across each clip and a timeline preview.

## Selection

| Scene | Source | Trim start | Timeline duration | Decision |
|---|---|---:|---:|---|
| 02 | `scene_02_black_canyon_v3.mp4` | 1.0 s | 4.5667 s | Clean canyon context; replaces the old inset/finished-structure shot. |
| 03 | `scene_03_diversion_action_v3.mp4` | 2.2 s | 4.2333 s | River/current and visible tunnel portal, with camera moving toward it. |
| 06 | `scene_06_dry_worksite_v3.mp4` | 2.7 s | 5.0333 s | Water level lowers in the protected worksite. Monochrome reconstruction is explicitly labeled AI reconstruction. |
| 09 | Original `scene_09.mp4` | 0.15 s | 5.4333 s | New candidate retained but not selected: it pours visibly dry rocks/aggregate rather than wet concrete. |
| 10 | `scene_10_block_growth_v3.mp4` | 1.2 s | 4.4333 s | Timelapse construction/formwork action within the scene. |
| 11 | `scene_11_cooling_action_v3.mp4` | 0.8 s | 4.7667 s | Pipe surface gives way to a cutaway showing internal water movement during the narration. |

The other nine scene selections use the preserved original video files. Source overrides are explicit in `scenes.json` via `source_path`; original clip filenames remain intact. Old detail crops are removed for replaced shots so they do not inherit an unsuitable framing. The original pouring shot keeps its previously reviewed detail crop.

## Edit treatment

- All 14 scenes remain in the same storytelling sequence. Cuts retain the full, original narration alignment and 70-second timeline.
- Five new source selections are integrated; no Blender demo, generated local substitute or reference-video footage appears.
- 42 phrase captions retain yellow keyword emphasis and off-white supporting text. These are phrase-timed forced-alignment estimates, not word-by-word listening sign-off.
- Top-center headlines remain selective. All object geometry stays disabled so new footage is not overlaid with old coordinate keys.
- Original clip audio and generated audio from supplemental clips are not mixed in. The original narration is retained in full; optional music is absent.
- Supplemental preview rendered and inspected before the master. All 14 representative preview scenes showed clear text/subject separation. See `../supplemental_review/preview_contact_*.jpg` and `source_contact_*.jpg`.

## Remaining visual limits

These are illustrative AI reconstructions, not authenticated historical footage. The new block shot uses simplified regular geometry and time-compressed growth. The cofferdam shot has a stylized drainage progression and monochrome grading; it is labeled accordingly. The portal shot shows moving water near an opening, but exact hydraulic inlet/outlet behavior was not established by frame sampling; no directional arrow or calibrated flow claim is added. Some original shots still contain baked-in reconstruction artifacts and internal source edits. Final normal-speed listening and phone-size visual review remain advisable before publication.

The unselected pour candidate is preserved at `assets/supplemental/scene_09_concrete_pour_v3.mp4`. A future improved candidate should show cohesive wet concrete flowing under gravity and accumulating in the receiving form, without loose boulders.

## Validation and preservation

- All 17 unit tests passed, including project-relative supplemental source selection with original fallback, caption emphasis, crop bounds and safe geometry gating.
- Export target: H.264/AAC, 1080x1920, 30 fps, 70 seconds. Final checks are in `qa/export_validation.json` after full decode.
- Original 14 clips and voiceover, all six supplemental clips, v1 master, v2 master and the earlier v3 preview are checksum-checked for preservation.
- Original footage is 720x1280; the five new clips are native 1080x1920. The output uses both resolutions at the requested 1080x1920 canvas.
- No paid generation APIs or new archival photos are used.

Final verification completed: exactly 2,100 frames / 70.000 seconds, H.264 1080x1920 at 30 fps and AAC at 48 kHz. Full decode passed; no black intervals detected at the recorded threshold. Audio peak -2.8 dBFS. All 14 representative master frames were inspected. Five supplemental paths are confirmed in the actual render report; all 21 source files and three prior exports match their recorded hashes.
