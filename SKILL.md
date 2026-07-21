---
name: aigc-atmosphere-video
description: Analyze, critique, and plan atmosphere-first AIGC fashion, lifestyle, hiphop, and product videos where the goal is selling style, mood, music-video energy, brand world, pose language, reference-model presence, and visual consistency rather than obvious product closeups. Use when reviewing AI-generated video sequences, Douyin AIGC references, provided model photos, front/back outfit references, character motion, expressions, hiphop gestures, classic poses, camera movement, motion continuity, architecture, scene logic, atmosphere unity, visual aesthetics, storyboards, shot plans, production workflows, risk control, or prompts for mood-led hiphop music-video films.
---

# AIGC Atmosphere Video

Use this skill for the user's AIGC fashion/lifestyle/product films when the creative goal is not a traditional product ad. The product can stay subtle. The main product is the atmosphere: style, world, taste, emotional state, and visual identity.

## Core Rule

Do not judge the work by "product exposure is not enough" unless the user explicitly asks for a hard-selling ad. For this user's direction, low product prominence is acceptable when the film still has a strong hidden anchor: repeated silhouette, material, gesture, face type, posture, space, color, rhythm, prop, or emotional state.

The central question is:

> After watching, does the viewer remember a distinct world and want to belong to it?

## Evaluation Axes

1. Style anchor:
   - Identify the exact style being sold: cold urban, retro street, industrial loneliness, future nomad, quiet luxury, dark fashion, ritual space, coastal freedom, or another clear world.
   - Criticize the film when the style changes without purpose or becomes a random moodboard.

2. Character system:
   - Characters may change, but they must feel like one tribe.
   - Check face type, hair, clothing silhouette, posture, walking rhythm, gaze, attitude, and emotional temperature.
   - If one protagonist is intended, identity continuity must stay stable.
   - When the user provides specific model photos, those models are not optional background extras. They must appear in the main visual world as core characters.

3. Emotion line:
   - A mood film does not need a conventional plot, but it needs emotional progression.
   - Look for movement such as isolation to control, pressure to release, distance to intimacy, chaos to order, or numbness to awakening.

4. Visual world unity:
   - Locations, architecture, color, lighting, props, wardrobe, typography, and camera language must belong to one world.
   - Multiple locations are acceptable only when they share the same visual grammar.

5. Motion principle:
   - Choose one main movement language: breathing stillness, street fashion walk, cinematic music-video drift, ritual object movement, or fast editorial impact.
   - Repeated walking, standing, turning, and looking become weak when they do not build identity or emotion.

6. Hiphop pose and gesture language:
   - For hiphop-led films, use classic gestures and body attitudes as style anchors: head nods, shoulder bounce, hand-to-chest emphasis, open-palm rap gestures, two-finger point, arms crossed, hands in pockets, chain touch, hood/cap adjustment, wall lean, low squat, sneaker tap, back-turn reveal, and crew formation.
   - Keep gestures controlled and intentional. Use 1-2 clear gestures per shot rather than constant hand motion.
   - Avoid accidental gang signs, weapon gestures, offensive gestures, fake bravado, or exaggerated dancing unless the brief explicitly calls for them.
   - Unless the user explicitly requests a dance film, treat classic dance vocabulary as beat punctuation rather than the main action. Default to roughly 70% spatial action and attitude, 20% restrained groove, and 10% recognizable dance accent.
   - In a 20-25 second film, use only 2-3 explicit upright accents such as one two-step, one shallow top-rock cross-step, or one heel-toe/chest-hit punctuation. Keep floorwork and fast choreography out of identity-critical generations.

7. AI realism:
   - Check hands, faces, eyes, clothing text, signage, logos, reflections, fabric movement, product geometry, scale, and architecture consistency.
   - Advanced AIGC should feel controlled, not over-generated.

8. Brand memory:
   - For atmosphere-led films, memory can come from world, color, material, posture, sound, camera rhythm, or recurring symbol.
   - Do not force logo shots unless the brief requires commercial clarity.

9. Provided model coverage:
   - If the user provides front and back photos for multiple models, count the files and register them as identity pairs. Four models with front and back references means eight source images but four characters, not eight characters.
   - Preserve each model as a distinct character type and make all provided models appear in the main shots.
   - Front and back references are used to preserve identity, hair, body shape, outfit silhouette, garment fit, and overall styling.
   - Use viewpoint-matched sources: front source for front shots, back source for back shots. For a three-quarter view, assign the front image to face/front identity and the back image to rear hair/shoulder/graphic structure; never average all references together.
   - In four-person shots, map one source to one fixed character slot and preferably composite characters sequentially. Do not feed all eight images as equal references in one uncontrolled generation.
   - Do not turn the film into a catalog, lookbook, or product close-up sequence unless requested.
   - Make clothing visible naturally through movement, group blocking, back-turn reveals, walking, leaning, and environmental framing rather than forced display.

10. Production path:
   - For final-quality work with multiple required reference models, prefer storyboard-first production.
   - Do not rely on one whole-video generation from several reference images plus a long text prompt, except for rough mood exploration.
   - Generate or define keyframes per shot, then create short video clips shot by shot. This reduces identity drift, missing models, clothing drift, gesture chaos, and inconsistent atmosphere.

11. Prompt precision:
   - Avoid vague style-only prompts such as "cinematic", "film grain", "heavy shadows", or "smoke" without specifying the intended optical effect.
   - When reference clothing is provided, lock the garment fit per model according to the actual reference: hem position, body length, boxy or regular proportion, dropped shoulder, sleeve length, body width, fabric weight, and natural drape. Do not force every garment into the same short-boxy fit.
   - Treat atmosphere as cinematography: define key light, negative fill, rim/back light, haze density, wet-ground reflectivity, wall texture, lens/filter feel, color palette, and shadow detail.
   - Add detailed negative prompts for body anatomy, garment deformation, model merging, warped graphics, bad hands, distorted limbs, plastic skin, and cheap AI smoothness.
   - Preserve natural skin as slight pores and low-amplitude surface variation, never as sharpening or heavy grain. Face volume must survive in shadow: eye sockets and jawline cannot collapse or flatten, and bright skin must roll smoothly without highlight bloom or HDR appearance.
   - Organize negatives in a fixed order: character/face, anatomy, garment, action, scene/material, then camera/edit. Repeat the relevant complete categories in the master prompt and each shot prompt.

12. Hiphop MV priority:
   - When the user asks for hiphop, prioritize music-video energy over brand campaign stillness.
   - Build each shot around a beat-driven micro-action: walk-in, lean-in, head nod, shoulder bounce, chain touch, low squat, turn-back, step-through, crew reveal, or camera orbit.
   - Define how every shot enters and exits so the edit flows. Avoid independent stand-still portraits that do not connect.
   - Preserve the provided faces and hairstyles aggressively. If a face changes, the shot fails even if the atmosphere is strong.

13. First/end-frame continuity:
   - Reject a first/end-frame pair before video generation when the architecture, camera axis, lens perspective, light positions, exposure, color temperature, or surface layout changes beyond the planned camera move.
   - The end frame must be an edit or controlled continuation of the approved first frame, not a second independent scene generation.
   - A location change disguised as a camera move is a failed frame pair. Do not try to repair it in the video prompt.

14. Action and camera direction:
   - Do not use breathing, a small head nod, a shoulder drop, or a short push-in as the only event of a normal MV shot. That produces a standing portrait.
   - Give each shot one visible primary action with spatial or posture change, one restrained beat accent, and one readable landing pose.
   - Write an explicit timeline, camera path, start framing, end framing, entry state, and exit state. Camera movement must express reveal, pressure, connection, pursuit, or departure rather than decorate the shot.

15. Master time grid and shot handoffs:
   - Keep this user's atmosphere-led short films within 15-30 seconds unless the brief explicitly needs another length. Prefer the shortest duration that can preserve all required characters, viewpoints, relationships, and the ending image; do not stretch actions to fill 30 seconds.
   - For a full film, declare total duration, working BPM, frame rate, beat length, shot boundaries, and total frame count before writing individual prompts.
   - Give every short clip a beat-by-beat local timeline and a whole-film global time range. State the body action, camera travel, accent, deceleration, landing, and cut point on exact beats or frame ranges.
   - Track each shot's entry state, exit state, screen direction, subject scale, camera axis, and visual handoff to the next shot. A detailed clip that does not connect to the next clip still fails the whole-film edit.

16. Background realism engineering:
   - Judge background realism by physical causality: buildable geometry, plausible scale, material-specific reflectance, source-consistent light, causal wear, coherent optics, and temporal stability. More cracks and texture do not create realism.
   - Approve an empty environment plate before adding models. Prefer a real location photo or video frame; pure text-to-image backgrounds are exploratory unless they pass a strict environment gate.
   - Separate background, character composite, end-frame derivation, motion generation, and post camera movement. Do not ask one generation to invent all of them.
   - Treat generative camera movement as an unseen-pixel risk. Prefer locked or nearly locked shots when character identity, clothing, architecture, and multi-person consistency are all critical; add small camera energy in post.
   - Adversarially inspect the background without people, at 200% crop, in grayscale, across first/middle/end frames, and in reverse playback. Reject attractive images with impossible construction or breathing geometry.

17. Visual authorship beyond realism:
   - Treat realism as a pass/fail gate, not as the creative concept. A believable but generic loading bay still fails when its silhouette, architecture, blocking, and camera attitude are forgettable.
   - Build atmosphere in this order: dominant silhouette, spatial motif, character hierarchy, light logic, color hierarchy, then surface detail.
   - Reject the generic AI-industrial package of roll-up shutters, random cracks, mirror-wet floors, blue-orange light, thick smoke, glossy skin, and centered fashion-campaign posing.
   - For hiphop, prioritize low camera height, foreground occlusion, asymmetrical negative space, depth-plane crossings, body-led cuts, and crew relationships.

18. Kling 3.0 Omni mode:
   - When the user selects Kling 3.0 Omni without first/end frames, do not apply first/end-frame interpolation rules to the generation plan.
   - Build one Element per real character using that character's matched front/back references, plus one approved environment-world Element from 2-4 continuous location views.
   - Prefer two 10-12 second custom multi-shot sequences for a 20-25 second film. Use 3-4 storyboard shots per sequence and replace only failed shots with separate single-shot Omni generations.
   - Specify duration, visible Elements, environment zone, body route, beat accent, landing, shot size, camera path, light continuity, handoff, and negatives for every custom shot.
   - When several approved plates represent one location, state in the master prompt and every shot that they are continuous zones of the same site, time, weather, light direction, practical-light color, construction system, and material response.
   - Give every shot a hard start and hard end time. Explicitly prohibit Omni from adding transitions, establishing inserts, reaction shots, or any unrequested intermediate shot.
   - For manual production or when an external image API is unavailable, prefer three or four independent 4-6 second single-take clips for a 15-25 second film. A four-by-five-second structure is the default for this user's four-model hiphop work because each clip can be approved or replaced independently.
   - Do not ask Omni to edit these independent clips internally. Assemble them with hard cuts in post at the declared boundaries.

19. Production control and measurable acceptance:
   - Treat reference files, Element definitions, environment plates, prompts, generations, and accepted clips as versioned production assets rather than loose files.
   - Fingerprint every front/back reference pair and refresh the Element version whenever either source changes.
   - Do not claim centimeter-level garment tolerances from uncalibrated reference images. Without physical measurements, lock hem, shoulder, sleeve, width, and drape using body landmarks and normalized visual proportions.
   - Gate production in order: references, empty environment, prompts, solo shots, multi-character shots, shot QC, then final edit.
   - Log every generation attempt with stable failure codes and a repair decision. Notes such as "bad" or "no feeling" are not sufficient failure records.
   - Never invent an API endpoint. Export generation queues without sending until official API documentation and credentials are available.

## Review Workflow

When analyzing a full video:

1. State the film's likely intention in one sentence.
2. Separate single-frame beauty from whole-film success.
3. List strengths first: atmosphere, composition, styling, lighting, spatial taste, character attitude, motion restraint, or cinematic feeling.
4. List failures by severity: style drift, character inconsistency, weak emotional line, scene logic break, repetitive actions, AI artifacts, poor ending, or weak rhythm.
5. Explain whether each failure hurts atmosphere, character, world, or commercial memory.
6. Give concrete repairs: what to delete, what to repeat, what to unify, what to reshoot/regenerate, and what anchor to add.

Do not over-focus on product closeups. Instead ask: "What is the invisible brand anchor?"

## Creation Workflow

Before writing prompts or shot lists:

1. Define one atmosphere sentence:
   - Example: "A cold industrial city tribe moving through metal, fog, and late-night light."

2. Define the tribe:
   - Who belongs in this world?
   - What faces, postures, clothes, gestures, and emotional states repeat?
   - Which provided models must appear as core characters?

3. Define hidden anchors:
   - Choose 3-5 recurring anchors, such as black nylon texture, silver metal, wet pavement, side-profile faces, slow walking, cold white light, narrow corridors, or wind on fabric.

4. Define reference-model coverage:
   - Map each provided model to at least one main shot.
   - Use front and back angles as natural character presence, not as product catalog views.
   - Avoid making the clothing print the only reason the shot exists.

5. Define location logic:
   - Every location must feel like the same world, even if it changes.
   - Avoid random location jumps unless they mark a clear emotional chapter.

6. Define motion logic:
   - Pick one movement style and keep it consistent.
   - Use fewer movements with clearer intention.

7. Define gesture logic:
   - Choose 3-5 repeated hiphop pose/gesture anchors when the style calls for them.
   - Make gestures support the world: confidence, pressure, coldness, defiance, ritual, or crew identity.
   - Decide whether dance is primary or auxiliary. When auxiliary, embed a maximum of one classic dance accent inside an existing walk, crossing, rise, or cypher shot; do not create isolated dance-demonstration shots.

8. Define ending memory:
   - End on the strongest brand-world image, not a blurry or generic scene.

9. Define production workflow:
   - Choose storyboard-first for final deliverables.
   - Use direct reference-image plus text-to-video only for fast style tests, not final presentation.
   - Build the final film from short controlled clips, then assemble rhythm, color, and sound.

## Repair Principles

- If a shot is beautiful but does not strengthen the world, cut it.
- If a character changes but does not feel like the same tribe, redesign the identity system.
- If provided models disappear or become generic extras, rebuild the shot list around them as core characters.
- If the video has many scenes, reduce them into fewer families of space.
- If the product is subtle, make the style symbols stronger.
- If the emotion is flat, reorder shots into a visible emotional arc.
- If the hiphop mood feels static, add restrained gesture anchors instead of random dancing.
- If direct whole-video generation creates unstable results, switch to storyboard-first and generate each shot separately.
- If AI artifacts appear, simplify text, signage, hands, reflective surfaces, and complex fabric details.

## References

Read `references/creative-principles.md` when creating, rewriting, or repairing an AIGC video concept.

Read `references/hiphop-gesture-system.md` when creating hiphop, rap, streetwear, underground street, or music-video style prompts.

Read `references/reference-model-coverage.md` when the user provides model photos, front/back outfit images, or says specific people must appear in the main video.

Read `references/production-workflow.md` when deciding whether to generate the whole video directly or build it from storyboards/keyframes and shot-level clips.

Read `references/prompt-cinematography-control.md` when prompts need professional control over clothing fit, lighting, film texture, haze, wet reflections, color palette, and negative prompts.

Read `references/hiphop-mv-continuity.md` when creating hiphop music-video style shot plans, camera movement, performance actions, face-identity locks, and edit continuity.

Read `references/kling-first-last-frame-direction.md` when using Kling first/end-frame generation, designing timed movement, checking frame-pair continuity, preventing standing-portrait motion, or locking one environment across several clips.

Read `references/background-realism-engineering.md` when a background looks synthetic, over-designed, glossy, game-like, structurally inconsistent, or unstable during camera motion.

Read `references/hiphop-visual-authorship.md` when a scene is technically realistic but still has no feeling, visual authorship, spatial tension, or memorable hiphop image grammar.

Read `references/hiphop-nightclub-world.md` when the chosen setting is a bar, nightclub, basement venue, DJ room, dance floor, backstage corridor, or after-hours club and the result must feel hiphop without generic neon-club AI imagery.

Read `references/kling-3-omni-workflow.md` when the user is working with Kling 3.0 Omni, Element references, custom multi-shot generation, or a no-first/end-frame workflow.

Read `references/production-control-system.md` when the user needs Element versioning, preflight gates, parameter tables, generation queues, failure tracking, automatic shot checklists, or repeatable production records. Use `scripts/omni_production.py` for deterministic refresh, queue export, checklist generation, and failure logging.

Read `references/blogger-reference.md` when comparing against the reference creators Suwen, Yang Peilin yppl, Lishen, and related Douyin AIGC accounts.
