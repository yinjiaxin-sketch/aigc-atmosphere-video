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

Replace generic "heavy shadows" with:

- low-key lighting with high contrast, around 8:1 key-to-fill feeling
- hard side key from 45 degrees, slightly above head height
- weak cool top light from industrial fluorescent tubes
- narrow rim/back light to separate shoulders and hair from the dark background
- strong negative fill on the shadow side, keeping one side of the face/body near black while retaining slight detail
- no flat beauty light, no glossy commercial studio fill

## Film And Lens Texture

Use film texture as a controlled look, not random noise:

- 35mm night color negative feeling, Kodak Vision3 500T / CineStill 800T inspired color response
- fine-to-medium organic grain, visible mostly in shadows and midtones
- subtle halation/bloom only around practical lights and wet reflections
- Black Pro-Mist 1/8 or 1/4 style diffusion: softened highlights, retained garment edge detail
- anamorphic-like vertical depth and slight falloff, but avoid fake streak flares unless needed
- keep skin natural and textured; avoid plastic smoothing

## Haze, Smoke, And Atmosphere

Use haze more than thick smoke:

- thin suspended haze to reveal light beams and give depth
- low drifting smoke only near floor or background corners
- no opaque smoke cloud covering clothes, hands, faces, or body edges
- smoke should move slowly across the background, not erupt from the T-shirt

## Wet Ground And Reflections

Make wet ground believable:

- uneven wet asphalt or sealed concrete, not mirror glass
- shallow puddles in cracks and surface low points
- broken blue-orange reflections from off-screen practical lights
- reflections should be dim and fragmented, not neon cyberpunk
- keep shoe contact with ground clear

## Wall And Location Texture

Use tactile, imperfect surfaces:

- raw concrete with pores, chipped paint, water stains, scratches, old tape marks, scuffed metal shutter, oxidized steel railings
- avoid clean 3D-rendered walls, smooth plastic concrete, generic futuristic corridor, or empty gray studio

## Color Palette

For the user's hiphop atmosphere films:

- base colors: charcoal, washed navy, deep indigo denim, dirty concrete gray, muted cream, worn tan boots
- accents: controlled ember orange and electric blue from the garment graphic language
- do not let neon green, magenta, purple, or saturated cyberpunk colors dominate unless requested

## Negative Prompt Areas

Include negatives for:

- anatomy: extra fingers, missing fingers, fused fingers, broken wrists, twisted elbows, impossible knees, bent ankles, floating feet, wrong shoulder width, stretched neck, warped spine, duplicated limbs
- face/identity: face swap, changed ethnicity, changed age, changed hairstyle, merged models, generic AI people, missing required model
- garment: wrong garment length, wrong hem position, cropped when the reference is longer, longline when the reference is shorter, dress-like T-shirt, tucked-in shirt, tight fitted shirt, stretched print, melted print, warped text, changing pants, changing shoes, changing jewelry, plastic fabric
- scene: glossy 3D render, smooth AI wall, cheap neon, fake cyberpunk, dense smoke covering subject, mirror-like wet floor, flat studio light
- motion: exaggerated dance, chaotic hand signs, gang signs, weapon gesture, fast hand motion, jitter, flicker, morphing body, teleporting limbs

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
