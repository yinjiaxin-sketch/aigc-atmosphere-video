# Kling 3.0 Omni Workflow

Use this reference when generating with Kling Video 3.0 Omni without a first/end-frame pair.

## Model Strategy

Kling 3.0 Omni supports reference-based generation and custom multi-shot control. Use those capabilities directly. Do not inherit first/end-frame restrictions from a different workflow.

For this user's four-model project:

- Build four fixed character Elements: `@A`, `@B`, `@C`, and `@D`.
- Each Element receives that model's matched front and back references. Do not create eight independent characters.
- Build one environment world Element, `@ENV-CYPHER`, from 2-4 approved views of the same real or visually continuous location.
- Keep garment fit, face, hair, body proportion, shoes, accessories, and front/back print behavior inside each character Element definition.
- In each storyboard shot, call only the characters visible in that shot.

## Recommended 20-25 Second Architecture

Do not ask one maximum-length generation to solve the whole film. Generate two custom multi-shot sequences and edit them together:

1. Sequence A, approximately 10-12 seconds: solo introductions and spatial ownership.
2. Sequence B, approximately 10-12 seconds: character interactions, crew convergence, and exit image.

Each sequence should contain 3-4 custom shots. This gives the model enough context to keep a world and rhythm while keeping failures replaceable.

If one shot fails, regenerate that shot as a separate single-shot Omni clip using the same Elements, action, camera path, environment zone, entry pose, and exit pose. Replace only that section in the edit.

For manual production, identity-critical multi-character work, or a temporarily unavailable external image API, prefer independent 4-6 second single-take clips. Use 3-6 clips according to the number of required characters, viewpoints, and group states; do not force four clips when four solo identity checks plus front/back group coverage require six. Give every clip one physical camera take, one main spatial action, at most one explicit dance accent, and no internal edit. Join the approved clips with hard cuts in post. This costs more separate submissions but sharply limits identity drift, environment redesign, and automatic transitions.

For a solo-first workflow, understand the actual limitation: accepting a solo clip does not train or update its Character Element. Extract one clean approved frame from each solo clip and use it as a secondary lighting and continuity reference during sequential group-anchor compositing. The original front/back source images remain authoritative for identity, anatomy, garment fit, hem, graphics, trousers, shoes, and accessories.

## Custom Multi-Shot Prompt Contract

For every shot specify:

1. Duration and shot number.
2. Visible Elements and fixed character slots.
3. Exact environment zone from `@ENV-CYPHER`.
4. Opening body position and screen direction.
5. One primary action with real spatial displacement.
6. One beat accent and one landing state.
7. Shot size, lens behavior, camera height, camera side, path, distance, and speed curve.
8. Light continuity and surface response.
9. Transition motivation into the next shot.
10. Shot-specific negatives.

Do not write a long paragraph that mixes all shots. Use separate storyboard blocks.

## Camera Diagram Reconciliation

When camera diagrams, storyboard HTML, and written camera instructions are supplied together, reconcile them before writing generation prompts. Create one source of truth per shot with:

1. environment anchors and navigable route;
2. subject start point, end point, facing, screen direction, and displacement;
3. camera start point, viewing direction, lens, height, path, travel distance, acceleration, deceleration, and stop point;
4. the shot's entry state, action completion, landing window, and hard-cut state;
5. the spatial and motion handoff into the next shot.

Do not preserve contradictions. If prose describes a full walking step while a diagram labels only 3-4 cm of movement, select the physically meaningful displacement and update both artifacts. If a shot is declared solo, remove any instruction that requires another named character to cross, brush past, or remain visible.

Floor plans must include real anchors, not only zone labels. For a nightclub world, draw the entrance door, bar, curtain opening, main floor, DJ booth, PA speakers, and exit. A camera icon placed in a different zone from the written camera position is a hard failure.

## Movement Freedom

Omni permits more camera and performance freedom than first/end-frame interpolation, but control one dominant move per shot:

- low lateral track;
- short shoulder-mounted push;
- low follow that stops while the subject continues;
- 25-40 degree half-orbit around two characters;
- locked low-angle crew frame.

Avoid combining orbit, push, zoom, tilt, rack focus, whip pan, and shake in one 3-second shot. More motion does not equal more MV energy.

## Environment Consistency

Reference the same environment Element in both sequences. Divide it into named zones instead of generating unrelated locations:

- `ZONE-RAMP`: sweeping concrete ramp and narrow daylight slit;
- `ZONE-PIERS`: repeated bridge ribs and circular support pier;
- `ZONE-YARD`: chain-link boundary, galvanized crash barrier, and service curb.

Keep structural anchors, ambient weather, time of day, surface dryness, practical-light family, and color response fixed across all zones.

## Audio

For a music-led final edit, generate without native dialogue and preferably without native music. Use a fixed editorial guide track and replace generated sound in post. Native ambient sound can be retained only when it is stable and supports footsteps, fabric, and location tone.

## Failure Gates

Regenerate a shot when any of these occurs:

- face or hairstyle replacement;
- front/back outfit details migrate between characters;
- the environment changes architectural family;
- the camera invents a new corridor or opening;
- gestures become random signs or hands dominate the lens;
- all characters move in identical synchronized steps;
- skin, concrete, or fabric becomes glossy;
- the scene reads as a fashion campaign lineup instead of a music-video moment;
- the model inserts a cut, extra person, text, prop, or light not specified in the storyboard.
