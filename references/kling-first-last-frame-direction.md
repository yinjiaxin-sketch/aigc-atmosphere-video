# Kling First/End-Frame Direction

Use this reference for Kling first/end-frame video prompts and any workflow where two stills define one continuous shot.

## Hard Frame-Pair Gate

Treat the first and end frames as two moments from one physical camera take, not two attractive images.

Reject the pair before video generation if any of these change without a planned physical explanation:

- location architecture, shutter or door design, column spacing, ceiling height, railing, wall damage, or floor cracks
- number, type, screen position, direction, or color of light sources
- camera side, axis, height, horizon, focal-length perspective, or subject scale
- exposure, white balance, color palette, air density, or surface wetness
- character identity, garment fit, hem position, pants, shoes, jewelry, or hairstyle

The end frame must be derived from the approved first frame through editing, pose transfer, controlled outpainting, 3D layout, or another continuity-preserving method. A second independent text-to-image generation is not an acceptable final end frame.

Use a difference budget:

- freeze environment identity and layout
- change only the body action, physically valid fabric response, camera parallax caused by the stated path, and small exposure variation caused by movement under the same lights
- keep scene geometry at least visually 95% consistent
- keep added or removed lights, doors, windows, wall fixtures, puddles, and damage at zero

## Avoid Standing-Portrait Motion

A normal 3-5 second MV clip needs:

1. one primary action with visible travel or posture transformation
2. one restrained beat accent
3. one clear landing pose that matches the end frame

Breathing, a tiny head nod, a shoulder drop, or a 20-30 cm push-in may support the action but may not be the entire shot. Use an action-ready first frame rather than a neutral standing pose.

Useful primary actions include:

- take two deliberate steps across or toward frame
- push off a wall and cross a pool of light
- pass behind or emerge from a column
- turn the torso 60-90 degrees while stepping
- drop into or rise from a low squat
- cross another character and exchange foreground/background priority
- move aside to reveal the crew

## Timed Prompt Contract

Write all visible movement on a timeline. For a 4-second clip, use this default structure unless the action needs another rhythm:

- `0.0-0.4`: anticipation; define weight, lead foot, hand, gaze, and camera start
- `0.4-1.5`: initiation; the lead body part starts and the camera accelerates
- `1.5-2.8`: primary travel or posture change
- `2.8-3.5`: beat accent and camera deceleration
- `3.5-4.0`: landing; exact foot, hand, gaze, torso, and final framing

Do not describe an invisible past event in a still prompt, such as "after completing a nod." Describe only the visible end-state pose.

When no final track is supplied, declare a working BPM and frame grid instead of using arbitrary decimal timing. A useful hiphop planning grid is `96 BPM at 24fps`: one beat is `0.625 seconds / 15 frames`; a six-beat shot is `3.75 seconds / 90 frames`; eight six-beat shots equal `30 seconds / 48 beats / 720 frames`. Put anticipation, initiation, travel, accent, landing, and cut on named beats. Remap the grid when the final track BPM changes.

For a six-beat, 90-frame clip, use this local grid as a starting point:

- beat 1, frames 0-14: action-ready hold, weight commitment, camera start and acceleration
- beat 2, frames 15-29: primary action initiation and first camera travel segment
- beat 3, frames 30-44: first landing or mid-action weight transfer; preserve screen direction
- beat 4, frames 45-59: second travel or posture change; camera reaches peak speed
- beat 5, frames 60-74: one restrained performance accent; camera completes travel and decelerates
- beat 6, frames 75-89: exact foot, hand, gaze, torso, subject scale, and cut-ready landing

For a 30-second film on this working grid, use eight continuous global ranges: `0.000-3.750`, `3.750-7.500`, `7.500-11.250`, `11.250-15.000`, `15.000-18.750`, `18.750-22.500`, `22.500-26.250`, and `26.250-30.000`. Do not leave gaps or overlaps. For every range, record the shot's entry state, main action, camera function, exit state, and next-shot handoff. The local six-beat plan controls generation; the global 48-beat plan controls the edit.

## Camera Direction Contract

For every shot, specify:

- lens family
- start height and side of subject
- dominant movement type
- approximate travel distance or arc
- acceleration and deceleration
- whether the camera leads, follows, crosses, reveals, or resists the subject
- end height, subject scale, screen position, and look room
- the emotional function: reveal, pressure, connection, pursuit, isolation, or departure

Use one dominant camera move per short clip. Do not combine push, orbit, zoom, tilt, and shake. A short axial push toward a stationary person is not enough for a normal performance shot.

## Environment And Character Continuity

Create an environment master before the shot list:

- set ID, master plate, shutter and column geometry, fixed lamp positions, floor condition, and color temperature
- a no-invention list for doors, wall lamps, puddles, graffiti, pipes, rails, and damaged areas
- one lighting map reused across connected shots

Create a character ledger:

- character ID, front/back reference, face and hairstyle, body proportion, garment fit and hem, pants, shoes, jewelry
- entry state, primary action, accent, exit state, screen direction, and next-shot match point

If one keyframe introduces a new wall, two new wall lamps, another shutter, a new floor treatment, or a new color grade, reject it even if it is visually attractive.

## Realism-First Prompt Repair

When the image becomes glossy or synthetic:

1. regenerate the keyframe; do not expect the video prompt to repair it
2. remove decorative haze, wet reflections, colored rim lights, wall lamps, bloom, halation, diffusion filters, and prestige camera-stock stacks
3. use mostly dry surfaces, one believable available light source, clean air, ordinary location wear, and local non-uniform shadows
4. describe visible material behavior instead of repeating "cinematic" or long camera-brand lists
5. keep negative prompts concise and failure-specific

## Prompt Output Order

For each shot, provide:

1. shot intent and edit connection
2. first-frame prompt with an action-ready pose
3. end-frame edit prompt with allowed differences and frozen elements
4. first/end-frame continuity checklist
5. video timeline
6. camera path and final composition
7. character, garment, environment, and anatomy locks
8. concise failure-specific negatives
