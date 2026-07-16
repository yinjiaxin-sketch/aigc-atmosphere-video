# Production Workflow

Use this reference when planning an AIGC video with multiple required reference models, specific outfits, or a final deliverable that must feel stable.

## Core Decision

For final-quality work, use storyboard-first production.

Do not generate the whole film from several reference images plus one long text prompt unless the goal is only a fast mood test. This method is unstable when the film must preserve four models, front/back outfit cues, gestures, atmosphere, and group blocking.

## Why Direct Whole-Video Generation Is Risky

- Reference models may disappear or merge.
- Faces, hair, body shape, pants, shoes, and jewelry may drift.
- The model may over-focus on one person and ignore the others.
- Back and front references may be confused.
- Clothing prints may become too prominent or distorted.
- Hiphop gestures may become random, exaggerated, or anatomically wrong.
- Scene changes may feel like unrelated AI clips.
- Final output may look impressive but fail the required character coverage.

## Recommended Final Workflow

1. Build a character bible:
   - Assign a short ID to each model.
   - Record each model's face, hair, outfit silhouette, pants, shoes, jewelry, and front/back references.

2. Build a shot map:
   - Decide which model appears in each shot.
   - Include at least one main shot for every required model.
   - Include at least one full-crew or near-full-crew shot.

3. Create storyboard/keyframes:
   - Generate or design a still frame for each shot first.
   - Lock atmosphere, location, pose, and model coverage before video generation.
   - Approve one environment master plate or a tightly matched environment reference set before generating character keyframes.
   - Derive the end frame from the approved first frame. Do not independently text-generate both ends of one shot.

4. Validate the frame pair:
   - Check the same architecture, column and shutter layout, light count and positions, floor cracks, camera axis, lens perspective, exposure, and color temperature.
   - Reject the pair if any difference cannot be explained by the planned subject or camera movement.

5. Generate shot-level clips:
   - Create 3-5 second clips per shot.
   - Keep each prompt focused on one primary action, one beat accent, one landing pose, one dominant camera movement, and one emotional purpose.
   - Write a timed action and camera path instead of letting the model invent pacing.

6. Select and assemble:
   - Choose the most stable clip for each shot.
   - Assemble in edit with consistent color, grain, sound, and rhythm.

7. Repair only weak shots:
   - Regenerate the unstable shot, not the whole video.

## When Direct Generation Is Acceptable

Use direct reference-image plus text-to-video only for:

- quick atmosphere testing
- motion style tests
- lighting tests
- checking whether a location concept works
- rough internal exploration

Do not use it as the final method when specific models must appear.

## Recommended Four-Model Appearance Structure

For a 30-45 second hiphop atmosphere film:

1. Opening: one back-view model, mysterious entry into the world.
2. Solo appearances: each model gets one controlled main shot.
3. Pair or trio transition: two or three models share a frame to build tribe connection.
4. Full crew: all four appear together in a loose formation.
5. Gesture passage: restrained hiphop gestures repeat across the models.
6. Ending: back-view or full-crew silhouette as the memory image.

## Shot Order Rule

Do not show all four models together too early unless the hook requires immediate crew impact. A stronger structure is:

- first: one iconic back-view silhouette
- second: one front-facing attitude shot
- middle: rotate through the remaining models
- late middle: bring them together as a tribe
- ending: return to the strongest back-view or group image

This makes the film feel designed, not like a random model collage.

## Whole-Film Continuity Ledger

Before generation, record for every shot:

- set ID and approved environment plate
- character IDs and reference viewpoints
- entry body state and exit body state
- primary action and beat accent
- lens, camera height, camera side, path, distance, and end framing
- light sources and their fixed screen positions
- the previous shot's exit direction and the next shot's entry direction

Do not approve a clip because it is attractive in isolation. Approve it only when it fits this ledger.
