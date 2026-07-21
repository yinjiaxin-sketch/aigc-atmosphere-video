# Prompt Cinematography Control

Use this reference when a prompt needs to control premium AIGC video texture instead of relying on vague words.

## Garment Fit Lock

If clothing reference images are provided, do not over-describe every visible item in every shot. Lock each garment according to its actual reference image. Do not force all outfits into one fit category.

- preserve the actual reference length: short boxy, regular length, or longer loose fit depending on that specific model
- preserve the actual hem position seen in the reference; do not let the hem drift upward or downward
- preserve the actual body proportion: boxy, square, regular, cropped, or loose depending on the reference
- preserve dropped shoulders, relaxed sleeve opening, and sleeve length as seen in the reference
- sleeves end near mid upper-arm to elbow, not tight
- thick washed cotton with natural drape, not thin stretchy fabric
- preserve reference pants, shoes, jewelry, hairstyle, and body proportion

Avoid saying only "oversized T-shirt" because many models may make it too long, too soft, too cropped, or dress-like. The correct instruction is: "match the reference garment length and hem position."

## Lighting Control

Replace generic "heavy shadows" with visible and physically motivated consequences. For realism-first industrial scenes, start with the fewest possible light sources:

- one existing overhead fluorescent or one believable off-screen practical source
- natural falloff, uneven illumination, and locally dark corners
- shadow separation created by subject position, not a glowing rim outline
- no flat beauty light, no glossy commercial studio fill
- no decorative wall lamps or colored accent lights unless they are already part of the approved environment master

## Film And Lens Texture

Use film texture as a controlled consequence, not a stack of prestige camera terms:

- prefer a plain real-location capture description before naming a camera, stock, filter, LUT, or emulsion
- if a camera or stock is named, state only the visible consequence needed: highlight rolloff, shadow noise, motion blur, or color response
- do not stack ARRI, Vision3, CineStill, Pro-Mist, halation, bloom, grain, wet reflections, and teal-orange color in one prompt; many models convert this stack into polished synthetic imagery
- when output looks glossy, remove diffusion, halation, wet reflections, colored rim light, and decorative haze before adding more negative terms
- use no diffusion filter by default for this user's rough underground MV direction
- 28mm to 40mm lens feeling for MV presence; use 50mm only for calmer close medium shots
- describe the exact camera path and endpoint instead of writing only "subtle handheld"
- keep skin natural and textured; avoid plastic smoothing
- lock facial texture and volume explicitly: `Skin texture is visible but natural, showing slight pores and subtle surface variation, NOT smoothed or airbrushed, NOT plastic or wax-like, NOT overly sharp or grain-heavy. Face maintains volume in shadow, eye socket and jawline never collapse or flatten. High-key areas transition smoothly without harsh highlight blooming or HDR appearance.`
- treat visible pores as low-amplitude surface variation, not a sharpening effect or grain overlay; preserve cheek, eye-socket, nose, lip, and jaw volume in shadow

## Face Identity Lock

When reference models are provided, treat face identity as a primary success condition:

- preserve facial structure, ethnicity, skin tone, hairline, hair length/style, age, body proportion, and expression temperature
- use "same person as reference, not a similar model" for front-view shots
- avoid beautified replacement faces, generic fashion faces, face averaging, race drift, age drift, and hairstyle drift
- keep front-facing shots medium or medium-wide if the tool struggles with exact likeness; do not force extreme close-ups
- for back-view shots, preserve hairstyle from behind, neck/shoulder shape, stance, outfit proportion, and body silhouette

## Haze, Smoke, And Atmosphere

Atmospheric haze is optional, not a default quality marker:

- begin with clean air or barely visible dust for realism-first tests
- use thin suspended haze only when a visible practical light needs depth
- low drifting smoke only near floor or background corners
- no opaque smoke cloud covering clothes, hands, faces, or body edges
- smoke should move slowly across the background, not erupt from the T-shirt

## Wet Ground And Reflections

Wet ground is optional and high-risk. Start dry when the model already produces glossy imagery:

- mostly dry dusty concrete with small darker damp patches
- if water is needed, confine it to one or two shallow depressions visible in both first and end frames
- do not use blue-orange floor reflections as a default atmosphere device
- keep shoe contact with ground clear

## Wall And Location Texture

Texture must follow construction and use history rather than decorate the frame:

- establish buildable geometry, attachment points, scale, drainage, traffic routes, and light sources before describing surface wear
- place water streaks below joints or penetrations, impact marks at contact height, dust at edges, rust near exposed steel or fasteners, and wear along real foot or trolley paths
- give concrete, galvanized steel, painted metal, floor, cloth, and skin different reflectance; do not apply one global roughness or noise texture
- preserve small ordinary functional evidence such as conduit, a junction box, shutter guide, drain, fastener, or patched fixing point when it has a structural reason
- avoid random pores, cracks, tape, stains, and peeling paint across every surface; decorative grunge is an AI-set signal
- approve an empty location plate before adding the model; character prompts must not redesign the background

## Color Palette

For the user's hiphop atmosphere films:

- base colors: charcoal, washed navy, deep indigo denim, dirty concrete gray, muted cream, worn tan boots
- accents: controlled ember orange and electric blue from the garment graphic language
- do not let neon green, magenta, purple, or saturated cyberpunk colors dominate unless requested

## Negative Prompt Areas

Write negatives as a stable system and repeat the relevant full categories in the master prompt and every shot prompt. Do not scatter a few negatives at random. Use this order:

1. Character identity and face: face replacement, averaged face, identity merge, copied person, age/ethnicity/skin-tone change, hair swap, beauty repaint, airbrushed skin, plastic or wax skin, collapsed eye sockets, flattened jawline, harsh HDR highlight bloom.
2. Anatomy: extra/missing/fused fingers, hand penetration, reversed joints, fused legs, sliding feet, floating soles, stretched body proportions.
3. Garment and styling: hem drift, wrong garment length, tucked shirt, dress-like T-shirt, tightened fit, thinner fabric, changed neckline/sleeve, graphic/text drift, front/back graphic swap, swapped pants/shoes/accessories.
4. Action and choreography: repeated dance loop, synchronized group choreography, complex finger signs, fast floorwork, impossible weight transfer, reversed motion, slow motion, speed ramp.
5. Scene and material: new people/vehicles/props/text, glossy concrete, mirror-wet floor, neon color wash, thick smoke, volumetric beams, HDR, CGI surfaces, breathing architecture, changing openings or fixtures.
6. Camera and edit: floating gimbal, drone motion, random shake, uncontrolled orbit, fast zoom, focus breathing, impossible parallax, invented transition, morph, dissolve, flash wipe, or any extra shot not specified by the timecode.

## Prompt Rule

For final prompts, write in layers:

1. model/reference lock
2. garment fit lock
3. pose/gesture
4. location texture
5. lighting design
6. film/lens texture
7. movement
8. negative prompt

When realism fails, simplify the positive prompt first. Repeating technical film terms and long anti-gloss negatives cannot override a glossy first frame.
