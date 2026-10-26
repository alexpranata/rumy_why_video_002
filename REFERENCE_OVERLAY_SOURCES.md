# Hoover Dam — Real-photo overlay candidates (external sources; NOT auto-included)

The supplied 14 Google Flow clips are illustrative 3D/video re-creations. Do not mislabel them as authentic archive footage.

## Verified source pages

1. **U.S. Bureau of Reclamation – Historic Views**: https://www.usbr.gov/lc/hooverdam/gallery/historicviews.html
   - Best for: early Black Canyon (scene 02), high scalers (scene 08), Jumbo Rig and tunneling (scenes 04–05), cofferdams and excavation (scenes 06–07), nearly completed dam (scene 13).
   - Caption as `ARCHIVAL PHOTO — U.S. BUREAU OF RECLAMATION`, only if actual source/rights corroborate.
2. **U.S. Bureau of Reclamation – Dam Views**: https://www.usbr.gov/lc/hooverdam/gallery/damviews.html
   - Best for: real current dam photos for end reveal (scene 14), if a suitable image is used and permitted.
3. **Library of Congress – 2018 Hoover Dam Photograph**: https://www.loc.gov/item/2018702437/
   - Listed as `No known restrictions on publication`; modern genuine image candidate.
4. **Library of Congress – 1933 Dam Construction Photograph**: https://www.loc.gov/item/2004680467/
   - Rights advisory is **`Rights status not evaluated`**. Do **not** use without clearing rights.

## Editing implementation

- Download and incorporate **only rights-cleared** chosen images manually into `assets/references/`.
- Add a data-driven `reference_overlay` manifest or adapt `render.py` to show the optional still in 1–3 second overlays. Use 9:16 friendly placement, mild Ken Burns movement, subtle border, and short `SOURCE: ...` credit. Keep captions unobstructed.
- Do not fabricate the existence of downloaded photos or claim they have been included when only links are provided. No paid image/video generation APIs.
- Verify that archival photos match the narrated construction step, and distinguish them visually from AI video reconstructions.

## Revision v2 review in this environment

The two official source families were reviewed from this supplied manifest. Live requests to the Bureau of Reclamation gallery and Library of Congress were rejected by the environment proxy (CONNECT 403), so image-specific content, creator, download files and current rights statements could not be independently verified. No photos were downloaded or added to the render.

- Historic Views: promising for scenes 02, 04–08 and 13, subject to checking each photograph’s creator, date, described construction step and rights. Federal hosting alone does not clear all images.
- Dam Views: suitable only for a modern reveal, not evidence of 1930s construction; verify the individual creator and terms.
- LOC 2018702437: a modern 2018 image candidate; the supplied “No known restrictions on publication” advisory is not a blanket warranty or evidence that this is a 1930s archival photograph. Confirm the live item and credit before use.
- LOC 2004680467: excluded while rights status remains unevaluated.

Optional photo inserts are not enabled in this revision. Any future image insert needs a rights record and a separate data-driven overlay implementation with visible source credit.
