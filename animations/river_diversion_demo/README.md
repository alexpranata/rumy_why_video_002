# Original river diversion 3D prototype

This eight-second visual demo was created from procedural Blender geometry and local Pillow typography. No reference footage, downloaded models, textures, stock photos or paid generation APIs are used. It is a schematic cutaway, not a surveyed model of Black Canyon or a historical recreation.

The four exposed conduits represent four diversion tunnels, two on each bank. Flow markers indicate the bypass direction. Temporary barriers isolate a central work zone, which drains after the bypass is established. This is a deliberately simplified explanation, not a hydraulic simulation. Route geometry, elevations, timing and dimensions are illustrative, not to scale.

## Reproduce

From `/workspace/rumy_why_video_002`:

```bash
XDG_CACHE_HOME=/workspace/.cache blender --background --factory-startup --threads 3 --python animations/river_diversion_demo/build_scene.py
python3 animations/river_diversion_demo/compose_clip.py
```

Blender 4.3.2 Workbench renders 240 original 540x960 RGBA frames. Pillow composites them into a 1080x1920 layout with crisp, export-resolution system DejaVu Sans typography; FFmpeg encodes H.264 at 30 fps. It is an upscaled 3D prototype, not a native 1080 3D production render. The saved `.blend` can be rerendered at higher resolution for a final insertion. No audio or narration is included in this demonstration.

## Deliverables

- `output/animation_demo/river_diversion_original_3d_demo.mp4`
- `animations/river_diversion_demo/river_diversion.blend`
- Editable scene builder and composition script in this directory.
- Representative stills and validation record in `output/animation_demo/`.

The prototype is separate from the original 14 clips, narration, v1 final and v2 final. None of those is overwritten, and the demo is not yet inserted into the episode. Possible next original visual modules are interlocking concrete blocks, heat buildup/cooling pipes, and a simple construction sequence.
