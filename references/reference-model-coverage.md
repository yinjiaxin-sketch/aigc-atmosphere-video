# Reference Model Coverage

Use this reference when the user provides photos of specific models, especially front and back clothing references.

## Core Rule

Provided models are core characters, not optional background extras. If the user provides four models, all four must appear in the main visual world.

Do not make the film a product catalog unless requested. The clothing can be visible without being emphasized.

## How To Use Front And Back References

- Four models with one front and one back image each means eight source images organized as four identity pairs.
- Use front photos to preserve face, hair, posture, body shape, outfit silhouette, jewelry, pants, shoes, and emotional temperature.
- Use back photos to preserve hairstyle from behind, T-shirt back graphic position, shoulder shape, garment length, pants silhouette, stance, and back-turn identity.
- Use both angles as natural moments inside the atmosphere: standing, walking away, turning, leaning, group blocking, or final silhouette.
- Label the references before prompting, for example `A-front/A-back`, `B-front/B-back`, `C-front/C-back`, and `D-front/D-back`.
- Use only the matching viewpoint in a clear front or back shot. For a three-quarter view, assign explicit roles to the same character's pair instead of blending them equally.
- Never treat all eight files as equal visual references in one generation. That encourages identity averaging, face swaps, garment exchange, and missing characters.
- For four-person group frames, create fixed character slots and preferably composite one character at a time while freezing the approved environment and previously placed characters.

## Required Shot Coverage

For four provided models:

1. Each model must appear in at least one main shot.
2. At least one group shot should include all four or clearly imply the four-person tribe.
3. Back views should appear as atmosphere/identity reveals, not as catalog display.
4. Front views should show attitude and presence, not just clothing.
5. Clothing prints should remain readable enough to feel present, but should not dominate every frame.

## Good Integration

- A model faces away under a bridge while smoke and light make the back graphic part of the world.
- A model slowly turns from side/back to three-quarter view while the camera stays atmospheric.
- A four-person crew stands in a loose triangle with different poses but the same emotional temperature.
- Front-facing models use restrained hiphop gestures while clothing stays naturally visible.
- Back-facing models become silhouettes, with the garment graphic treated as a visual symbol.

## Bad Integration

- Treating the models as replaceable background people.
- Showing only one or two models when four were required.
- Turning every shot into front/back product display.
- Cropping out the provided outfit without a reason.
- Changing hair, body, ethnicity, outfit silhouette, pants, shoes, or jewelry so much that the reference identity is lost.
- Overemphasizing the T-shirt print until the atmosphere becomes a normal clothing advertisement.

## Prompt Rule

When generating prompts, explicitly state:

> All four reference models must appear as core characters in the main visual world. Use their front and back photos to preserve identity, hairstyle, outfit silhouette, and styling. Show front and back angles naturally through poses, walking, leaning, and group blocking. Do not make the video a product catalog or clothing close-up ad.
