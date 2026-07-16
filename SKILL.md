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

7. AI realism:
   - Check hands, faces, eyes, clothing text, signage, logos, reflections, fabric movement, product geometry, scale, and architecture consistency.
   - Advanced AIGC should feel controlled, not over-generated.

8. Brand memory:
   - For atmosphere-led films, memory can come from world, color, material, posture, sound, camera rhythm, or recurring symbol.
   - Do not force logo shots unless the brief requires commercial clarity.

9. Provided model coverage:
   - If the user provides front and back photos for multiple models, preserve each model as a distinct character type and make all provided models appear in the main shots.
   - Front and back references are used to preserve identity, hair, body shape, outfit silhouette, garment fit, and overall styling.
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
   - For a full film, declare total duration, working BPM, frame rate, beat length, shot boundaries, and total frame count before writing individual prompts.
   - Give every short clip a beat-by-beat local timeline and a whole-film global time range. State the body action, camera travel, accent, deceleration, landing, and cut point on exact beats or frame ranges.
   - Track each shot's entry state, exit state, screen direction, subject scale, camera axis, and visual handoff to the next shot. A detailed clip that does not connect to the next clip still fails the whole-film edit.

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

Read `references/blogger-reference.md` when comparing against the reference creators Suwen, Yang Peilin yppl, Lishen, and related Douyin AIGC accounts.
