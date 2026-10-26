# RUMY WHY — Video 002: Run the edit pipeline

The **editing pipeline is implemented** in `render.py`. You do not need Codex just to start it.
It uses Python 3 standard library and a local FFmpeg build with FFprobe and libass.

## 1) Extract the whole project

Keep the `rumy_why_video_002` folder and its subdirectories intact.

## 2) Prepare only your own existing media

Save the 14 Google Flow clips as:

```text
assets/video/scene_01.mp4
assets/video/scene_02.mp4
...
assets/video/scene_14.mp4
```

Each source clip needs at least 5 seconds (plus any `trim_start_sec` you configure in `scenes.json`).
Create the ElevenLabs voiceover from `voiceover.txt`, save it as:

```text
assets/audio/voiceover.wav
```

Optional, properly licensed background audio: `assets/audio/music.mp3`.
The current ZIP intentionally includes **no** Google Flow footage, voiceover WAV, or music files.

## 3) Validate your environment and inputs

From a terminal inside the extracted project directory:

```bash
python3 render.py --check
```

This reports which of the 15 mandatory media files are missing and checks FFmpeg, but does not render or produce substitute footage. A check with missing files exits successfully for inspection.

If FFmpeg / FFprobe is missing, install an FFmpeg version that includes the `ass` subtitle filter. Check it with `ffmpeg -filters | grep ass` on Linux/macOS.

## 4) Render the Short

```bash
python3 render.py --output output/rumy_why_002.mp4
```

Output: H.264, AAC, portrait 1080x1920, 30fps, ~70 seconds, hard cuts, editorial zooms, burnt-in captions, plus consistent animated engineering-yellow shapes (arrows, reticles, rulers, underlines) and fact labels.
A sidecar report is written to `output/render_report.json`.

## 5) Adjust timings

Edit `scenes.json`: use `target_duration_sec` per scene (default 5s) and add `trim_start_sec` (optional, default 0) to choose the best seconds of each Flow clip. Keep scene order and video filenames unchanged.

**Important:** `captions_rough.srt` has scene-based timestamps, not accurate word-level voice alignment. Listen to the generated ElevenLabs narration and correct the subtitle timings before publishing. If you change scene durations, you must adjust the SRT timings too.

If the voiceover is longer than the combined scene durations, rendering stops to avoid cutting the last words. Either adjust the video timing or re-export voiceover.

## New: animated engineering annotations

The default render uses `motion_graphics.json` and `motion_graphics.py` to add a **consistent `#FFD400` annotation system**. This is rendered offline with FFmpeg libass. Arrows and reticles are not automatically tracked: before publishing, adjust their normalized coordinate positions in `motion_graphics.json` to point at real relevant parts of each shot. See `MOTION_STYLE_GUIDE.md`.

For a shape-only edit use `python3 render.py --no-callouts`; for no graphic overlay use `python3 render.py --no-graphics`; for graphic overlay with no subtitles use `python3 render.py --no-captions`.

## Extra flags

```bash
python3 render.py --help
python3 render.py --no-captions
python3 render.py --no-callouts
python3 render.py --crf 18 --preset slow
```

`--check` is also a smoke/validation mode that works before the media is available.
The visual media should be understood as AI-based **historical reconstruction**, not authentic archival footage.

## Codex recovery prompt

If Codex previously reported that command execution was unavailable, start a fresh Codex workspace with this **extracted folder as its workspace root**. Confirm its command execution tool is working, then paste:

> Inspect RUN.md, README.md, scenes.json, and render.py. The offline FFmpeg editing pipeline is already implemented and verified with temporary synthetic test inputs. Run `python3 render.py --check` and `python3 -m unittest discover -s tests -v`. Do not replace existing media or generate fake clips. When 14 user-provided Google Flow clips and the user-provided ElevenLabs WAV are available, run the real render and inspect render_report.json. If commands remain unavailable, report the exact workspace tool error rather than claiming the project files are corrupt.

If the command tool fails **before any command starts**, troubleshoot or restart the Codex workspace/session: that problem is independent of the files in this ZIP.

## Reuse the channel-wide editing Skill

This project now includes `.agents/skills/rumy-why-video-editing/SKILL.md`. When working with Codex in this extracted project, you can explicitly invoke `$rumy-why-video-editing` or ask it to edit RUMY WHY Shorts. To reuse in other projects, copy the *directory* `rumy-why-video-editing` (not just its contents) into `~/.agents/skills/` on the machine where Codex runs. Restart Codex if it does not discover a new skill.


### Motion graphics revision v2
Titles are 10–15% larger and placed at top-center. Unverified arrows, circles and measurement lines are disabled by default; add them back only after alignment/tracking review against actual footage. See `REFERENCE_OVERLAY_SOURCES.md` for possible authentic photo inserts and their rights caveats.
