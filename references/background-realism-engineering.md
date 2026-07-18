# Background Realism Engineering

Use this reference when an AIGC scene looks like a polished set, game environment, synthetic industrial corridor, or decorated AI background even when the prompt says realistic.

## First Principle

Background realism is not the amount of texture. It is the agreement of geometry, scale, construction, material response, lighting, wear history, optics, and time.

A generated wall with many cracks can still look fake. A plain real wall looks real because every mark has a physical cause, every edge belongs to a buildable structure, and every highlight can be traced to a light source.

Do not use `realistic`, `cinematic`, `gritty`, `industrial`, `rough concrete`, or a long camera-brand stack as proof of realism. Treat them as unverified requests.

## Root-Cause Model

Fake backgrounds usually come from one or more of these failures:

1. The model invents the location, character, lighting, styling, and composition in one pass. The fashion subject activates a fashion-set prior.
2. Decorative damage is distributed like a texture overlay instead of following water, gravity, traffic, fasteners, joints, and human contact.
3. Every surface shares the same roughness. Concrete, galvanized steel, paint, cloth, skin, and floor all become equally smooth or equally noisy.
4. The scene is too composed: centered vanishing point, balanced empty space, symmetrical lamps, convenient colored light, and no ordinary maintenance evidence.
5. The prompt removes all incidental reality by demanding perfectly dry, perfectly matte, perfectly clean air, one ideal lamp, and no functional clutter.
6. Independent first and end frames describe similar locations but not one physical location.
7. A large generative camera move exposes unseen pixels, forcing the video model to redesign walls, columns, floors, and fixtures during the shot.

## Evidence Hierarchy

Use the strongest available source in this order:

1. a real photo or extracted frame from the exact location
2. several real photos or a short phone video of one location from planned axes
3. a licensed real-location plate with controlled edits
4. one AI-generated empty environment master derived from real references, followed only by low-freedom edits
5. pure text-to-image scene generation, suitable for exploration but not the default final route

If the background is commercially important and no real plate or real reference exists, state the reliability limit. More prompting does not remove that limit.

## Separate-Pass Architecture

Build the shot in this order:

1. **Environment truth source**: approve an empty plate before adding characters.
2. **Anchor ledger**: record structural elements, normalized screen positions, dimensions, light sources, floor condition, and wear marks.
3. **Character composite**: add the supplied model using a low-freedom edit while freezing the plate.
4. **End-frame derivation**: edit the approved first frame; never regenerate the environment.
5. **Motion generation**: animate character action while minimizing background synthesis.
6. **Post camera move**: add a 2-4% crop, pan, push, or controlled shake in editing when generative movement is not necessary.

Do not ask a single generation to solve all six stages.

## Physical-Causality Checklist

### Geometry and scale

- doors, shutters, rails, stairs, columns, lamps, conduits, and drains have plausible dimensions and attachment points
- parallel edges converge consistently under one lens perspective
- rails terminate into a floor or column; lamps mount to a ceiling; shutter guides connect to jambs
- no impossible thin slabs, floating pipes, repeating bays, or changing ceiling height

### Material response

- unfinished concrete is mostly matte with subtle local variation, not plastic and not uniformly sandpaper-like
- traffic-polished floor zones may be slightly smoother than dusty edges
- galvanized shutter has a restrained broad sheen, not mirror reflections and not perfectly dead matte
- rust begins around exposed steel, fasteners, joints, or drainage paths
- different materials do not share one global gloss or one procedural noise pattern

### Wear history

- water marks run downward from a joint, penetration, pipe, or roof edge
- impact scars cluster at trolley, shoe, hand, or vehicle contact height
- dust accumulates at wall-floor junctions, corners, and unused edges
- tire and foot traffic follow believable routes
- damage is sparse and causal; it is not decorative grunge placed everywhere

### Lighting

- every bright region has a visible or inferable source
- shadow direction, softness, and color agree with those sources
- practical lamps may clip slightly while deep corners retain ordinary sensor noise
- mixed ambient spill is allowed when the opening that causes it exists
- no unexplained rim light, teal-orange split, glowing wall, or uniformly lifted shadow

### Optical capture

- use one coherent focal-length perspective and one horizon
- depth of field follows subject distance rather than blurring random background areas
- exposure and white balance may be imperfect but must remain stable
- avoid perfect symmetry, perfect edge-to-edge sharpness, excessive HDR, and showroom composition

## Camera-Motion Risk Rule

Every generative camera move creates an unseen-pixel budget. Larger lateral moves, arcs, and orbits require more architecture to be invented.

- lowest risk: locked camera, character moves within frame
- low risk: very small axial move with unchanged occlusion
- medium risk: short lateral move where all revealed surfaces already exist in both frames
- high risk: arc, orbit, passing a column, moving from one room into another, or changing the visible side of a structure

For identity-heavy multi-character shots, prefer a locked or nearly locked camera. Generate subject motion first and add small camera energy in post. A locked frame can still feel like a hiphop MV through blocking, foreground occlusion, cut timing, subject scale, and performance rhythm.

## Background Master Gate

Approve the empty plate only when all checks pass:

- crop the people out mentally: the image still reads as an ordinary shootable location
- count all doors, columns, rails, lamps, pipes, and drains; each has a plausible function
- trace every shadow and highlight to a source
- inspect wear at 200%; no repeated stamp, mirrored crack, melted edge, or identical stain cluster
- inspect straight lines and attachment points; no breathing geometry
- grayscale the image; it still has believable exposure without relying on color styling
- reject any image that looks attractive because of perfect symmetry, theatrical haze, colored rim light, or decorative destruction

An attractive failed plate remains a failed plate.

## First/End-Frame Background Gate

Align the first and end frames on fixed architecture and compare them before video generation:

- fixed anchors should remain within roughly 0.4% of frame width for a locked shot
- lamp, door, column, rail, conduit, crack, and drain counts must not change
- material roughness and damage patterns must not pulse or migrate
- only planned parallax may move; unexplained deformation is a hard rejection
- a camera move that cannot be explained by both keyframes must be removed or moved to post

## Adversarial Preflight

Before approval, try to prove the background is fake:

1. View the background without the characters.
2. Compare first, middle, and end frames side by side.
3. Play the clip backward to expose geometry breathing.
4. Track one lamp edge, one column edge, one floor crack, and one shutter groove.
5. Inspect 200% crops for repeating texture, edge halos, and melted fasteners.
6. Check whether removing color grade destroys the illusion.
7. Ask whether a construction worker could explain how every visible object is installed.

If any test fails, repair the plate or reduce camera motion. Do not add more mood adjectives or negative-prompt terms.
