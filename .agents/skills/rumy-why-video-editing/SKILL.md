---
name: rumy-why-video-editing
description: Plan, edit, animate, validate, and version RUMY WHY engineering, megastructure, ancient-engineering, and extraordinary-construction Shorts. Use for Google Flow footage, ElevenLabs narration, editorial camera moves, verified yellow engineering overlays, source-aware measurements, offline FFmpeg rendering, and production QA. Not a generic channel template.
---

# RUMY WHY — Engineering Video Editing

## Mission and boundaries

Produce a dynamic, concise engineering documentary, not a generic motion-graphics slideshow. **The current episode workspace and approved sources are the source of truth.** Preserve working code and approved edits; prefer small reversible patches to replacing the renderer. A verified past implementation is a useful example, not proof that a feature works in another shot.

**Channel-wide rules:** purposeful engineering storytelling, accurate facts, restrained high-contrast brand graphics, faithful footage, synchronized narration, reproducible exports, and explicit human review of uncertain geometry.

**Never:** silently replace supplied media; call paid video-generation APIs; claim fixed coordinates are tracking; present AI reconstruction as authentic archive footage; imply an illustrative bracket measures a hidden physical foundation; publish rights-uncleared material; or overwrite an approved export without explicit direction.

The user manually generates Google Flow footage and places it in assets. ElevenLabs voice recordings are provided or created through an expressly authorized workflow. Use local/offline editing tools and available assets only. Do not spend additional API credits unless explicitly authorized.

## 1. Decide which motion is requested

"Make it move" has **three distinct meanings**. Identify the requested outcome before implementing; if materially ambiguous, clarify which type is desired. When context is sufficiently clear, proceed and state which types will be changed.

1. **Source-footage action** — water visibly flows, cranes lift, concrete pours, workers act. This must come from actually depicted source frames. A yellow arrow moving over static water is *not* evidence that the water itself moves. If missing, flag the shot for manual replacement/re-generation; do not fabricate moving historical action.
2. **Editorial camera movement** — crop, dolly/push, pan, zoom, speed changes, shot selection, match cuts. Ensure movement supports the explanation and remains smooth after output cropping. Avoid constant zooms, distorted source reconstruction, and transitions unrelated to narration.
3. **Explanatory graphical animation** — curved directional flow arrows, verified reticles, dimension drawing, counters, leader lines, headings, timelines, and diagrams. Graphics must relate to visible geometry or clearly identified illustrative concepts; their movement is distinct from motion in the source footage.

Make changes measurable in a short visual demonstration. A request for animated graphics is not satisfied by writing config that leaves them invisible because every target remains unverified.

## 2. Visual identity and legibility

- **Engineering Yellow:** `#FFD400` for annotations and numeric highlights. Supporting text `#F7F9FD`; contrast/shadow `#0B1523`. Maintain consistent grading but do not recolor the natural world neon yellow.
- Adobe After Effects–inspired motion design is a **style target**, not a required .aep file. Implement using the tools available in the workspace (e.g. Python/FFmpeg/libass).
- Typography: bold readable sans-serif with license-safe system fallbacks. Main explanatory headings **upper-center**, approximately x=0.5, y=0.125 in normalized output coordinates, adjustable for footage and Shorts UI. The established Hoover Dam title style uses ~64 px at 1080x1920; treat it as a tested reference, not a universal pixel requirement.
- Entrance/exit: restrained fades and short positional easing; preserve a phone-readable hold. Avoid overly stiff full-screen line templates.
- Captions are visually above technical graphics and must remain legible over real imagery. Lower caption safe zones, main title, and interactive platform UI must not overlap. Actual footage and platform-safe framing decide the final positions.
- For each annotation, prioritize purpose, correct target, legibility, and the moment it is narrated. Use a small number of overlays rather than leaving moving decoration onscreen continuously.

## 3. Story structure and editorial selection

Hook with the engineering mystery or surprising grounded measurement; establish **what / where / why difficult**; show **how it was built** in causal or chronological steps; reveal the result. Include dimensions, techniques, tools, obstacles, and numbers only when sourced and relevant.

Select actual footage based on **both** visual attractiveness and action correctness. Favor shots demonstrating the narrated mechanical or physical process. Faster, newer, prettier, or AI-regenerated footage is not automatically better. Example: an alleged wet-concrete pouring shot depicting dry aggregate must be rejected for narration about a concrete pour.

Use flexible shot lengths based on voice and action; 8-second Google Flow clips can supply shorter edited segments. Keep narration untruncated. Match cuts, restrained punch-ins/outs, and camera movement should serve the explanation rather than enforce identical five-second beats.

## 4. Separate reusable policy from episode configuration

**This SKILL.md holds channel policy and QA rules only.** Each episode owns its own configuration: subject and verified facts, script, target duration, number of scenes, source paths and selections, trim windows, crop/zoom, shot motion, overlay timing, annotations, measurement data, music, and output paths.

Do **not** require exactly fourteen scenes, a seventy-second timeline, a specific dam measurement, or Hoover Dam animation windows in a general renderer or the channel skill. The v4 Hoover Dam `scenes.json` and `motion_graphics.json` are episode-specific examples, not portable defaults.

For every selected shot record, where feasible:
- source path, original SHA-256, provenance/source type, license or authorization status;
- selected time span and effective editorial transform (trim, crop, zoom, pan, resize, speed);
- narration beat and intended physical action;
- whether overlay geometry or measurement values have been approved for **this exact source and transform**.

Keep scene selections data-driven; do not implicitly substitute a different clip when an input is missing.

## 5. Verified motion-graphic geometry

Permitted explanatory treatments include manually fitted **curved flow-path keyframes**, camera-fit dimensions, animated endpoint caps, counters, short heading reveals, underlines, and object callouts. Select the type that matches the scene.

**Fail closed on object geometry:** unreviewed targets must not draw physical-object arrows, rings, leader lines, or brackets. A constant screen point is not motion tracking. Optical-flow analysis can help manual inspection; it does not prove 3D tracking, physical action, flow speed, or a true measurement.

A geometry review must record:
- the source file identity **and source hash**;
- exact selected source time, effective trim, crop, zoom, speed and output mapping (or a canonical transform hash);
- the target identity, direction and what is visibly depicted, with reviewed timestamp/frame evidence;
- coordinates and camera-fit keyframes in the final output coordinate system;
- reviewer, status, and the difference between illustration, manual fitting, and calibration.

**Source-change invalidation:** replacing footage, switching supplemental clips, changing trim, crop, zoom, pan, speed, aspect transform, or output framing invalidates geometry verification. Disable affected geometric overlays until reviewed again and update the review record. Inactive or obsolete notes from a prior shot do not count as approval. Do not mark verified based on labels alone.

Where the required graphic is blocked by unverified geometry: show the cause, produce a screenshot/short inspection preview, request or perform manual coordinate alignment, and render a **visible demonstration** once verified. Do not silently omit the feature and call the task finished.

Reference from verified Hoover Dam v4: moving curved river arrows were keyed against viewed river/camera frames; a dam-height bracket used manual camera-fit keys. Neither constitutes automatic object tracking.

## 6. Measurements, numeric counters and provenance

Every displayed quantitative fact must include, in editable project data:
- numerical source value and source reference/URL or citation;
- display unit and conversion basis if converted;
- intended rounding and precision; avoid implying false precision;
- a clear measurement status: **published fact**, **illustrative overlay**, or **calibrated image/world measurement**;
- for calibrated values: calibration method, reference baseline, error/uncertainty and review evidence.

A counter may animate **to a sourced published value** without becoming a computed measurement. Do not map pixels to feet/meters unless genuinely calibrated. For illustrative dimensions, position a helpful line against a visible structure but disclose the visual bracket is illustrative if the published measurement includes invisible portions (e.g. a buried foundation). Never label movement speed as measured flow velocity without an actual measurement.

Keep formulae, rounding rules and sourced values out of renderer constants where possible. Check all displayed conversions, label timing, unit consistency and fact provenance during QA.

## 7. Supplemental footage and archival overlays

Accept new material only after checking **subject match, construction stage, actual depicted physical action, time/chronology, orientation, image quality, and rights**. A replacement should improve factual fidelity, not merely look more cinematic. Keep original and candidate sources separately for comparison.

For still photos, diagrams or historical archives, check **rights for each item** and record source URL, creator/owner, permission/license terms and required credit. A government website, image search hit, or historic appearance is not automatically a reuse license. A rights-cleared still can be inserted briefly with mild parallax/Ken Burns if appropriate, never as counterfeit moving historical footage. Prefer explicitly labeled archive imagery versus AI reconstructions.

If external media is unapproved or licensing is unclear: leave it out, cite/source it as a candidate, and continue using the approved footage. Do not scrape and silently insert unlicensed photos.

## 8. Review-to-export workflow (mandatory)

1. **Inventory and inspection:** read actual skill, active episode files, renderer and tests; inspect assets and scene selections. Record source hashes. Check media decode, frame rate, duration and narration. **Inspection is not a strict pass.** If a CLI `--check` exits 0 with missing prerequisites, do an independent mandatory-input check and block master rendering until satisfied.
2. **Short feature showcase:** render a compact demonstration of each newly requested feature (e.g. moving flow arrow and a drawing bracket/counter). Inspect entry, middle, exit and target adherence at frame-level or short playback. Iterate until the animation is visibly present and correctly placed.
3. **Full-timeline preview:** render in a **versioned, isolated** preview output and staging directory; inspect all cuts, shots, graphic collisions, captions, audio transitions and motion continuity. No unreviewed factual geometry.
4. **Master render:** export to a new version-specific destination and staging directory. Never rely on FFmpeg `-y` to protect existing files. Refuse an existing output unless the user has explicitly authorized overwriting that particular version.
5. **Verify and derive:** full decode, FFprobe streams/duration/resolution/fps, black/silent interval checks where appropriate, subtitle/voice timing, audio clipping and end-of-narration. Record source and export SHA-256 hashes. When making a downloadable preview/showcase from the verified master, record its exact source master hash and derivation command.
6. **Three explicit sign-offs:** (a) technical tests + media validity; (b) visual/engineering accuracy, overlays, safe zones and storytelling; (c) listening review at normal speed for voice, music and caption alignment. Do not treat test-count success as visual or listening approval.

**Concurrent rendering:** jobs must use unique temporary/caption/motion/intermediate paths per job. If the implementation shares staging files, do not launch preview and master concurrently. Serial rendering alone is a workaround, not a concurrency fix.

**Reproducibility manifest:** capture version/commit, renderer/config hashes, source hashes, trim/transforms, FFmpeg version, invoked command, output path/hash, test results, manual geometry review and QA sign-offs. Preserve previous source files and approved masters as immutable baselines.

## 9. Renderer compatibility and honesty

Never infer that a CLI flag removes all visible graphics without inspecting the real output. Check each layer independently (headline text, caption-borne numeric callouts, vector geometry, advanced geometry and counters). Document the effective behavior and offer a known-safe layer combination or a tested fix.

For the **Hoover Dam v4 adapter**, consult `production/V4_TECHNICAL_DEBT.md` and `output/revision_v4/final/QA_v4.md`. At the time of its v4 review, the renderer still has: a non-strict `--check`, layer-disable flag inconsistencies, overwrite-prone FFmpeg output, shared staging files, fourteen-scene assumptions and geometry notes not bound to source/crop hashes. **These are known defects or limitations, not desired channel standards.** Do not represent them as solved until code and tests demonstrate the fixes.

Implement and validate behavior changes in the episode-specific renderer before promoting them to reusable automation. Make changes in a branch or reversible patch; preserve current v4 visual outcomes unless a deliberate change is requested.

## 10. Handoff

Provide a concise production report: exact inputs used, source-selection rationale, types of motion delivered, verified versus illustrative graphics, measurement references, rights status, generated previews/master paths, commands, hashes, checks and remaining issues. Explain any human QA still outstanding. Never report a real-media render or human sign-off that did not happen.
