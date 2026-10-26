# Hoover Dam v4 — renderer technical debt (not channel standards)

Baseline audited: v4 commit `1ed781bdd62618e5a41eaf39f8ded73bb0ba8b4f`. These are observed or reported limitations to verify and fix; do not describe them as working guarantees in SKILL.md.

| Priority | Behavior / risk | Required acceptance test |
|---|---|---|
| P0 | `--check` exits successfully even with missing media or FFmpeg prerequisites | Keep inspection available but add an explicit strict readiness mode with nonzero exit for missing mandatory inputs; run negative tests |
| P0 | FFmpeg `-y` and unchanged output path can overwrite approved masters | Refuse existing output unless explicit overwrite flag and save hashes before/after; versioned output directories |
| P0 | Preview and master share `_build/captions.ass` and `_build/motion.ass` | Unique build directory per invocation; test concurrent renders and verify no intermediate cross-contamination |
| P1 | `--no-callouts` still emits advanced geometry height numeral/unit | Explicitly define headline/callout/advanced-number/geometry layers; test combinations with frame inspection |
| P1 | `--no-graphics` may retain legacy numeric callouts via caption renderer | Align CLI layer semantics with actual visible output; verify zero graphic layers for defined disable mode |
| P1 | Exactly fourteen scenes/annotations required | Parameterize episode count; verify a different count and flexible durations on synthetic source samples |
| P1 | Geometry verification notes are not bound to source SHA-256 or effective trim/crop/zoom | Record canonical clip+transform fingerprint, invalidate approvals on edit/replacement and test |
| P1 | Inactive scene 11 retains geometry review of an older source | Clear or explicitly archive obsolete evidence; no automatic reactivation |
| P2 | Published number versus screen-space bracket may imply a physical measurement | Add structured provenance/value/unit/rounding/illustrative-or-calibrated mode; QA checks |
| P2 | Fixed subtitle alignment still needs listening | Preserve QA listening sign-off as manual, never auto-mark signed off |

## Engineering constraints

- Keep v4 existing working river arrows, height bracket/counter, fourteen original source files, supplemental approved selections, master and QA record unchanged while hardening.
- Use reversible patches and tests; no paid APIs or automatic media replacement.
- Stage separate preview, showcase and master outputs; if derived from master, record command and master SHA-256.
- Keep this episode's exact fourteen-scene model, 70s timing, and 726ft text **in the episode config**, not in the channel-wide skill.
- Fixes above are **not implemented by this documentation change**.

## Existing acceptance evidence

See [QA_v4.md](../output/revision_v4/final/QA_v4.md) for manually fitted graphic windows, test counts, source limitations and listening caveat. Re-run tests against the target commit when validating future changes. `--check` success alone does not establish readiness.
