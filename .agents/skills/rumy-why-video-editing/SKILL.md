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
- Work only with supplied/licensed media. **Do not call billable video-generation APIs**; the user generates Google Flow footage manually and places it in `assets/`. Never silently invent an asset, synthesize fake source footage, or claim a completed render if mandatory files are missing.

## 3. Upper-center typography and safe-zone rules

- Default main text is **upper-center**, not floating per object: horizontally centered at x=0.50 and positioned around y=0.125 of a 1080×1920 frame (roughly 240 px from top). Check against the actual YouTube Shorts top UI; adjust 180–250 px as needed.
- Make the main technical title **10–15% larger** than the prior version; the Hoover Dam implementation increases 56 px to 64 px. Set secondary micro labels around 30 px, below the title, centered on the same x-axis.
- Preserve the proven font, yellow `#FFD400` headline, and white supporting text. Break overlong headings into 2 lines or reduce size slightly; do not overfill the upper 88% content width.
- Use a restrained 0.2–0.35 s fade and ~18 px vertical rise for title entrance, avoid jittery sideways movements.
- Narration captions/subtitles remain near the **bottom**, separate from the engineering title. Avoid text overlap with moving subjects and platform UI. Inspect phone-sized preview for readability.

## 4. Engineering motion-graphics grammar

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
- **Never misrepresent tracking**: fixed coordinates are not automatic object tracking. **Disable all unverified object geometry by default** (`geometry_verified: false`). Inspect real frames and align arrow endpoints/rings to objects actually visible; use time-varying keyframes or track targets when they move, then mark each scene verified. If a target is not visible, remove the shape entirely. No floating leader lines.
- Stay out of the bottom approximately 20–22% UI/caption conflict zone where practical; check actual subtitle positions and YouTube overlays on phone. Keep key details, faces, machinery, and text from colliding.
- Layering order: source footage → color/contrast → technical annotations → readable voice captions → platform-safe framing.

## 5. Pacing and storytelling

1. **Hook (0–3 s):** immediately show an extraordinary construction visual and a concrete engineering mystery, preferably anchored by a real measurement.
2. **Identify (3–12 s):** name the structure and location; establish scale and why construction was difficult.
3. **Build sequence (main body):** show how the engineers solved the problem, in chronological or causal order. Include tools, sequence, obstacles, and specific measurements when supported.
4. **Payoff (last 5–8 s):** show result, reveal scale and deliver one memorable verified fact. End decisively; no filler outro.

Prefer visible cause-and-effect over generic atmospheric montage. Translate each narration beat into a specific shot, annotation type, and timing. Use crisp cuts; transitions should have purpose.

## 6. Codex execution workflow

1. Inspect the repository (`README.md`, `RUN.md`, `scenes.json`, existing renderer/tests and available media); use the current project's files as source of truth for episode details.
2. Build or extend a **repeatable data-driven** render pipeline rather than hardcoding each episode. Keep visual tokens in a single config, prefer editable scene annotations (e.g. `motion_graphics.json`), and keep overlays separate from historical facts.
3. Validate footage exists, duration/resolution and codec are readable, narration duration fits, and subtitle timestamps are aligned. Report missing assets specifically and stop before an impossible final render.
4. Generate a low-resolution preview/contact sheet when assets exist. Position arrows, rings, and lines against **actual** footage frames; adjust and review overlaps at scene transitions.
5. Render H.264/AAC MP4, preserve 9:16 framing, and run tests plus `ffprobe` sanity checks (resolution, fps, video/audio streams, duration). Where possible inspect representative frames and audio.
6. Report exactly what was generated, what was tested, and what still requires human review. Do not confuse a synthetic-input smoke test with completion of the real video.

If the episode already has `render.py`/`motion_graphics.py`/`motion_graphics.json`, **reuse and improve them** rather than replacing them unnecessarily. Do not mutate or overwrite the original assets. If Codex's command tool is unavailable, report that environment limitation explicitly; do not claim a successful build or test.

## 7. Real photo overlays (optional, source-aware)

- Use historical photos or engineering diagrams as **brief factual visual inserts**, not as decoration or fake footage. A tasteful photo overlay can appear as a short 1–3 second overlay with Ken Burns motion, subtle frame, and small readable source credit. Match historic context and chronology of the current scene.
- For Hoover Dam, possible official starting points are the U.S. Bureau of Reclamation's historic photo gallery (https://www.usbr.gov/lc/hooverdam/gallery/historicviews.html) and modern photo collections (https://www.usbr.gov/lc/hooverdam/gallery/damviews.html). For other episodes, prefer corresponding government archives, museums, institutions or project operators.
- **Inspect image-specific licensing/rights and attribute sources**. A government-hosted photo is not automatically safe for every use, and Library of Congress records can have undecided rights status. Do not assume blanket permission from being publicly viewable.
- Do **not** scrape the web or use third-party rights-unclear photos silently. If source rights are unverified, provide a suggested source list instead and request locally supplied approved images. Keep existing user footage unchanged.
- If the renderer does not support photo inserts yet, make that an explicit pipeline enhancement rather than pretending the images are in the export. Narration text and subtitles must remain legible above overlays.

## 8. Historical accuracy, copyright and final QA

- Verify names, dates, engineering methods, dimensions and numerical callouts from reputable sources; when uncertain, omit or qualify claims. Do not fabricate precise measurements for dramatic effect.
- For historical reconstructions generated by AI, label/discuss them as illustrative when necessary; never falsely present them as authenticated historical footage.
- Confirm all footage, audio and fonts are properly usable; avoid copyrighted music without rights.
- Check: hook strength; clear structure/location; construction sequence; every arrow/ring targets the correct feature; `#FFD400` consistency; readable digits and captions on a phone; synced voice; no unintended black frames, cropping, cut-off words, or conflicting UI overlays.
- Deliver the MP4 when actual inputs permit, plus editable configuration / project files and a concise QA summary.
