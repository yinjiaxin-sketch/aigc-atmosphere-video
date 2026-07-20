# Production Control System

Use this reference when a prompt package must become a repeatable production workflow with versioning, generation records, failure tracking, and shot-level acceptance gates.

## Source Of Truth

Maintain one project configuration containing:

- project, model, mode, duration, resolution, frame rate, and prompt-source version;
- one Element record per real character;
- matched front/back reference paths per Element;
- file fingerprints, Element version, refresh time, and lock status;
- one environment Element with named zones and acceptance status;
- one row per shot with timing, visible Elements, risk, lens, camera height, camera move, action, and handoff.

If a source image changes, refresh its fingerprint and Element version before generation. Never reuse a stale version label after changing a reference.

## Measurement Integrity

Do not claim centimeter-level garment tolerance from uncalibrated model images.

- If physical garment measurements and a calibrated body or scale reference exist, centimeter constraints may be recorded.
- Otherwise lock the fit by visual landmarks and normalized proportions: hem relative to waistband/upper hip/hip/crotch, shoulder-seam position, sleeve endpoint, body width, torso-length ratio, fabric weight, and drape.
- A numeric tolerance without a measurable reference is false precision and must not be used as an acceptance gate.

## Gates

Use this order:

1. Reference gate: every required file exists and every Element version is frozen.
2. Environment gate: all empty-plate checks pass before adding characters.
3. Prompt gate: every shot has timing, action, camera, environment, identity, garment, and negative constraints.
4. Low-risk generation gate: generate solo shots before multi-character shots to validate the world.
5. High-risk generation gate: dual and four-person shots require expanded independence checks.
6. Shot acceptance gate: identity, garment, environment, light, movement, camera, texture, and handoff must pass before editing.
7. Final-film gate: reject any hard failure even when grading or editing can hide it temporarily.

## Failure Tracking

Record every generation attempt with:

- generation ID and timestamp;
- shot and sequence;
- model, duration, resolution, and output path;
- status: pass, partial pass, or fail;
- one or more stable failure codes;
- severity, notes, repair strategy, and regenerate decision.

Use stable codes such as `ID`, `GAR`, `ENV`, `LGT`, `ACT`, `CAM`, `TEX`, `MUL`, and `CUT`. Do not record only subjective notes such as "bad" or "no feeling".

## Automation

Use `scripts/omni_production.py` for deterministic project operations:

```powershell
python scripts/omni_production.py refresh --config project_config.json
python scripts/omni_production.py export-queue --config project_config.json --output-dir queue
python scripts/omni_production.py checklists --config project_config.json --output-dir checklists
python scripts/omni_production.py log --config project_config.json --output-file failure_log.csv --generation-id GEN-001 --shot 7 --status 失败 --codes ID-01,MUL-02 --notes "..." --strategy "..."
```

The queue exporter must not submit to an undocumented API. Keep transport disabled until official API documentation, authentication, request schemas, rate limits, and retry behavior are available. Export auditable JSON/CSV job manifests in the meantime.

