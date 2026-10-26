# RUMY WHY — Engineering Yellow Motion Graphics System (Video 002)

## Visual identity

**Visual reference:** Adobe After Effects-style engineering explainers: purposeful motion, animated callouts, vector technical annotations, clean dark shadows, editorial highlights. The renderer achieves this look using **FFmpeg + libass**, not Adobe After Effects itself.

| Use | Color | Hex |
|---|---|---|
| Single brand accent (all arrows, rings, measurement lines, highlighted numeric text) | Engineering yellow | `#FFD400` |
| Supporting micro-labels | Clean white | `#F7F9FD` |
| Text contrast outlines | Midnight charcoal | `#0B1523` |

Typeface: DejaVu Sans Bold with crisp outline. Portrait 9:16 master: 1080×1920, 30 FPS. Reticle stroke ~5 px, ring radius ~90–118 px, graphic entry at ~0.42 s, fade in/out ~200–300 ms; label slides 22 px in. Yellow annotation layer is **above video but below subtitles**.

## Purposeful effects (not decoration)

- **Arrow:** directs attention to a visible construction step (cofferdams, diversion, cooling pipes).
- **Reticle / ring:** identifies a visible detail (excavation, bedrock, concrete pour).
- **Measurement bracket:** dramatizes engineering scale (726 ft, tunnel span, cliffside work).
- **Underline:** anchors facts and dates (Black Canyon, 3.25 million yd³, 1936).
- **Number + micro-caption:** key facts remain readable; the source footage carries the story.

Don't use arrows to point at an *invisible or incorrect* location. Our scene placements are **starting coordinates only**, not footage-aware tracking. Once you provide each actual Flow shot, review frames and edit `motion_graphics.json` `x`, `y`, `target_x`, `target_y`, `label_x`, `label_y` to match the footage. All positions are 0..1 relative coordinates, so `0.5` means center. Keep text clear of lower caption zone (roughly bottom 22%), faces, machinery interfaces, and key engineering details.

## Per-scene overlays

| Scene | Overlay style | Primary English label |
|---:|---|---|
| 01 | Vertical scale bracket | 726 FEET |
| 02 | Underline | BLACK CANYON |
| 03 | Arrow | DIVERT THE RIVER |
| 04 | Reticle | TUNNEL EXCAVATION |
| 05 | Horizontal bracket | 4 TUNNELS |
| 06 | Arrow | COFFERDAMS |
| 07 | Reticle | SOLID BEDROCK |
| 08 | Vertical bracket | HIGH SCALERS |
| 09 | Reticle | CONCRETE POUR |
| 10 | Horizontal bracket | BLOCK BY BLOCK |
| 11 | Arrow | COOLING PIPES |
| 12 | Underline | 3.25 MILLION YD³ |
| 13 | Underline | 1936 |
| 14 | Reticle | HOOVER DAM |

## How to change the look

Edit `motion_graphics.json` and re-render. Edit per-scene `type`, `label`, `micro`, positions, `radius`, or `span`. The accent color is intentionally **locked** at `#FFD400` to prevent accidental color changes. If you need to change the entire channel color brand later, update the constant in `motion_graphics.py` and the matching value in the JSON together.

To turn off vector motion graphics:

```bash
python3 render.py --no-graphics
```

To show only shapes without labels:

```bash
python3 render.py --no-callouts
```

To keep graphics but hide subtitles:

```bash
python3 render.py --no-captions
```

## Export & quality control

1. Render actual user-owned Google Flow 8-second clips trimmed per `scenes.json` and recorded ElevenLabs narration.
2. Verify overlays point to visible relevant features; use the timeline for visual context rather than pretending graphics auto-track targets.
3. Verify fact labels against source references in README.md.
4. Inspect on a phone at normal Shorts viewing size. Ensure on-screen text is legible and not cut by YouTube interface.
5. Listen through audio and correct `captions_rough.srt` timestamps against the final narration before publishing.
6. Export MP4 H.264, 1080×1920. The project does not contain generative clips or voiceover; no replacement footage is created.
