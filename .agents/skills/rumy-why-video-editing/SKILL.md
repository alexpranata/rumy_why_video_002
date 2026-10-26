---
name: rumy-why-video-editing
description: Create, edit, and quality-check RUMY WHY engineering, megastructure, ancient engineering, and extraordinary-construction YouTube Shorts in Codex. Use when planning shots, building or modifying FFmpeg editing pipelines, rendering Google Flow and ElevenLabs assets, adding animated yellow technical annotations, captions, cinematic camera moves, or reviewing finished RUMY WHY videos. Do not apply to unrelated channels without an explicit request.
---

# RUMY WHY — Video Editing & Motion Graphics

Make every RUMY WHY engineering Short feel like a fast, premium documentary with clean Adobe After Effects–style motion design. Treat these as **channel-wide defaults**, not footage-specific instructions. Adapt shot timing, visual positions and technical labels to each video. Implement the design with tools available in the actual workspace (FFmpeg/libass, Python, After Effects, etc.); do **not** require Adobe After Effects unless a native `.aep` deliverable is requested.

## 1. Brand identity (non-negotiable unless user changes it)

- Accent: **Engineering Yellow `#FFD400`** — the *only* saturated accent on arrows, animated rings/reticles, measurement lines, numeric highlights, callout underlines, and technical indicators.
- Supporting text: **Off-white `#F7F9FD`**; dark outline/shadow: **`#0B1523`**. Keep technical graphics minimal and legible on bright or dark footage.
- Color grading: cinematic yet realistic; consistent contrast and white balance across clips. Avoid random green/red/blue neon annotations and cluttered effects. Natural colors in footage are fine.
- Typeface: a bold modern sans-serif with clear digits. Use a licensed/system font and deterministic fallbacks; never assume a proprietary font is installed.
- Identity: clean 2D technical annotations **on top of** cinematic construction footage; graphics explain real engineering, not merely decorate.

## 2. Default format and source media

- Platform: vertical YouTube Shorts **9:16, 1080×1920, 30 fps, H.264/AAC MP4**; aim for approximately 60–70 seconds *when the project's approved script supports it*. Follow the specific episode's requested length if different.
- Narration: English **ElevenLabs** documentary voice, aimed at US/global audiences. Preserve intelligibility; music and sound effects must never compete with the voice.
- Video sources: **Google Flow 8-second generated clips**, select engaging **3–5 second portions** for most shots. Do not impose a rigid five seconds where narration or action requires something else.
- Apply varied purposeful camera movement: selective fast push-in/pull-out, smooth digital pans, tracking, crane/aerial motion, match cuts, and rare speed ramps. Avoid zooming *every* scene or visible artifacts from over-cropping.
- Work only with supplied/licensed media. Never silently invent an asset, synthesize fake source footage, or claim a completed render if mandatory files are missing.

## 3. Engineering motion-graphics grammar

Choose an annotation only when it helps explain the **specific visible object** or quantifiable fact in the scene:

| Feature | What it communicates | Recommended behavior |
|---|---|---|
| Animated arrow / leader line | Engineering feature or direction of water, material, force | Yellow line draws toward a verified target; hold briefly, then exit |
| Yellow ring / reticle | Identify a turbine, tunnel, machine, formwork, wall, pipe or other physical detail | Pop/scale in gently with short opacity fade; align around the target |
| Dimension line / bracket | Height, width, depth, volume or scale | Animate line draw with endpoints; label with accurate units |
| Underline / highlight | Place name, date, method, and key facts | Slide or draw on a short, readable phrase |
| Large number + micro-label | One striking engineering measurement at a time | Bold yellow digits plus small white unit/context label |

- One primary callout at a time; at most two overlapping annotations when composition requires it.
- Typical graphic entry: 0.2–0.5 s after a shot cut; entry animation around 0.2–0.35 s; keep long enough to read; exit before the next conflicting shot.
- Use vector-quality 4–6 px equivalent strokes at 1080 px output, with restrained easing and minimal shadow. Tune thickness to actual footage.
- Use **normalized screen coordinates (0–1)** in data templates where practical. Numbers and measurements must be sourced to a trustworthy reference and use correct units.
- **Never misrepresent tracking**: fixed coordinates are not automatic object tracking. Inspect real frames and align arrow endpoints/rings to objects actually visible; keyframe motion or track targets when they move. If a target is not visible, remove or redesign the graphic instead of falsely pointing to empty space.
- Stay out of the bottom approximately 20–22% UI/caption conflict zone where practical; check actual subtitle positions and YouTube overlays on phone. Keep key details, faces, machinery, and text from colliding.
- Layering order: source footage → color/contrast → technical annotations → readable voice captions → platform-safe framing.

## 4. Pacing and storytelling

1. **Hook (0–3 s):** immediately show an extraordinary construction visual and a concrete engineering mystery, preferably anchored by a real measurement.
2. **Identify (3–12 s):** name the structure and location; establish scale and why construction was difficult.
3. **Build sequence (main body):** show how the engineers solved the problem, in chronological or causal order. Include tools, sequence, obstacles, and specific measurements when supported.
4. **Payoff (last 5–8 s):** show result, reveal scale and deliver one memorable verified fact. End decisively; no filler outro.

Prefer visible cause-and-effect over generic atmospheric montage. Translate each narration beat into a specific shot, annotation type, and timing. Use crisp cuts; transitions should have purpose.

## 5. Codex execution workflow

1. Inspect the repository (`README.md`, `RUN.md`, `scenes.json`, existing renderer/tests and available media); use the current project's files as source of truth for episode details.
2. Build or extend a **repeatable data-driven** render pipeline rather than hardcoding each episode. Keep visual tokens in a single config, prefer editable scene annotations (e.g. `motion_graphics.json`), and keep overlays separate from historical facts.
3. Validate footage exists, duration/resolution and codec are readable, narration duration fits, and subtitle timestamps are aligned. Report missing assets specifically and stop before an impossible final render.
4. Generate a low-resolution preview/contact sheet when assets exist. Position arrows, rings, and lines against **actual** footage frames; adjust and review overlaps at scene transitions.
5. Render H.264/AAC MP4, preserve 9:16 framing, and run tests plus `ffprobe` sanity checks (resolution, fps, video/audio streams, duration). Where possible inspect representative frames and audio.
6. Report exactly what was generated, what was tested, and what still requires human review. Do not confuse a synthetic-input smoke test with completion of the real video.

If the episode already has `render.py`/`motion_graphics.py`/`motion_graphics.json`, **reuse and improve them** rather than replacing them unnecessarily. Do not mutate or overwrite the original assets. If Codex's command tool is unavailable, report that environment limitation explicitly; do not claim a successful build or test.

## 6. Historical accuracy, copyright and final QA

- Verify names, dates, engineering methods, dimensions and numerical callouts from reputable sources; when uncertain, omit or qualify claims. Do not fabricate precise measurements for dramatic effect.
- For historical reconstructions generated by AI, label/discuss them as illustrative when necessary; never falsely present them as authenticated historical footage.
- Confirm all footage, audio and fonts are properly usable; avoid copyrighted music without rights.
- Check: hook strength; clear structure/location; construction sequence; every arrow/ring targets the correct feature; `#FFD400` consistency; readable digits and captions on a phone; synced voice; no unintended black frames, cropping, cut-off words, or conflicting UI overlays.
- Deliver the MP4 when actual inputs permit, plus editable configuration / project files and a concise QA summary.
