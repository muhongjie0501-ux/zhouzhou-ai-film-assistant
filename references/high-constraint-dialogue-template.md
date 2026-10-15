# High-constraint dialogue and multi-beat template

Read this only after the generation has passed the normal feasibility and split check. Use it for exact multi-speaker dialogue, delayed reveals, metaphysical visibility rules, tightly timed comic/dramatic turns, several planned beats inside one generation, or a precise sound ending. It is an execution mode, not the default prompt shape.

## Activation gate

Use this template when at least one requirement is genuinely decisive:

- exact spoken wording, order, or turn-taking;
- speaking/silence rights or director-specified overlapping dialogue must be controlled while listeners visibly react;
- a subject or detail must stay hidden until a visible trigger;
- a world rule controls shadows, reflections, physical contact, or who can perceive something;
- a punchline, reveal, door close, impact, or sound cue must land at a particular beat;
- the user explicitly requests a high-control, timecoded execution document.

Do not activate it merely because the user supplied many details. If independent subjects, physical contacts, camera changes, or speech already exceed one generation, split first and write one self-contained template per generation.

For a 30-second action generation, treat roughly three or four readable internal shots and one or two major physical interactions as a practical planning ceiling, not a promise of deterministic control. Split before compiling when the scene exceeds it.

## Preflight

Before writing the final prompt:

1. Lock the exact generation duration and intended edit duration.
2. Estimate or measure every line's spoken length in the requested performance style.
3. Add pauses, speaker handoffs, reactions, transitions, and actions that cannot happen during speech.
4. Check that each planned camera angle preserves any hidden reveal.
5. Confirm that the chosen Studio route can handle the requested multi-shot/audio behavior; otherwise recommend separate generations or post-production.
6. Separate UI-owned settings from model-facing narrative instructions.

If the budget fails, say so. Never solve it by silently making restrained dialogue unnaturally fast.

## Internal compiler structure

Use the following sections internally to verify a difficult generation. Do not return a 12-section dossier by default. After the checks pass, merge the necessary model-facing instructions into one complete English paste-ready prompt followed by one faithful full Chinese translation, then the compact single-copy controls and at most three `生成后检查` items. Follow [prompt-delivery.md](prompt-delivery.md) and the project delivery location; do not repeat the long file in chat.

### 1. Fixed invariants

List only facts that must remain true throughout the entire generation:

- identities, body/creature structure, wardrobe, props, and scale;
- location and world state;
- reference assignments and what each reference must not control;
- perception and physical-interaction rules;
- persistent absences that are genuinely story-critical.

### 2. One dramatic objective

State the single change the generation must communicate. Several shots may support one objective, but they must not introduce several competing story turns.

### 3. Delivery specification

Record generation duration, intended trim point, audio strategy, and visible style result outside the paste-ready prompt. Put selectable aspect ratio, resolution, frame rate, Studio version, camera, lens, aperture, movement, lighting/color presets, tempo, and emotion values in the separate Studio control card. Necessary visible light relationships belong to the approved scene baseline and may be expressed in the narrative; follow performance-space-methods. The sole exception is an intentionally chosen, currently verified Cinema Studio 4.0 Movement `#English preset name`: keep its token at the intended beat in the paste-ready video prompt for the director's manual candidate selection, and list the same choice in the card. Do not make the user copy other UI-owned basics into Higgsfield's prompt field.

### 4. Dialogue ledger

For each turn, record:

| Speaker | Exact line | Delivery | Listeners / intended interjections | Handoff cue |
|---|---|---|---|---|
| Character | Locked wording | pace, volume, emotional pressure | one or two visible micro-actions | line end, gaze, movement, or sound |

State outside the prompt whether exact wording and lip synchronization are pass/fail requirements. Default to distinct turns unless overlap is intended. When the director requests interruption, laughter or natural overlap, preserve it: record the entry cue/word, continuing speaker, must-hear line, and listener/interjector behavior. Do not apply all-others-silent constraints to the same interval.

### 5. Time budget

Show the planned duration of dialogue, pauses, reactions, camera transitions, and physical actions. Use ranges that reflect real uncertainty. Do not use 0.1-second precision unless the workflow has demonstrated that level of timing control and the beat genuinely requires it.

### 6. Timecoded execution

For every beat, write:

- time range;
- start state and current framing;
- one dominant camera action;
- one dominant subject action or speaking turn;
- listener reactions and any explicitly intended interjections/overlap;
- any state-gate transition;
- end state that cleanly hands off to the next beat.

Prefer a small number of legible beats. Treat many cuts, different lens languages, or several independent actions as a split signal.

When these beats are internal shots within one 4.0 generation, describe the cuts in the prompt itself. Do not invent separate start/end reference images between those internal shots. Across separate generations, choose a previous-tail-frame handoff only for genuine continuous action or match-on-action; a deliberate new angle should use shared Elements and a self-contained new first-frame description.

### 7. Performance rules

Translate tone into visible and audible behavior: gaze, blink, breath, jaw, lips, hands, shoulders, posture, hesitation, vocal pressure, and interaction with the environment. Use only cues that support the one dramatic objective.

When close acting, subtext, listener behavior, or a strong emotional turn is decisive, use `actor-performance-and-facial-actions.md` internally. Strip every FACS/AU code, intensity letter, and temporary character/priority label before delivery; the model-facing prompt receives only visible and audible natural-language direction.

### 8. Sound progression and ending

Separate dialogue, ambience, effects, and music policy. When useful, designate one final visual-and-sound landing point such as a latch, impact, breath, silence, or door close.

### 9. State gates

For every delayed reveal, write:

- **Before:** target is outside the visible composition or physically occluded;
- **Trigger:** one observable action completes;
- **After:** target becomes clearly visible and remains consistent.

Also state who can perceive supernatural subjects and whether shadows, reflections, contact, or environmental responses exist.

### 10. Post-generation acceptance checks

List no more than three objectively testable requirements whose failure prevents the intended use of the shot or selected interval; assess other usable portions separately. Examples include exact line presence, fixed subject count, reveal order, intended silence or overlap, absence of an established world-state violation, and the required final frame. Present these outside the paste-ready prompt under `生成后检查`; never expose the internal term `P0`.

### 11. Compact exclusions

Use only critical recurring exclusions. Group them by identity, world state, performance, audio, or output hygiene. Prefer positive targets in the main prompt and avoid repeating the same forbidden item in several sections without a demonstrated reason.

### 12. Separate Studio control card

Keep the standard manual control card outside the narrative prompt. Check it for conflicts with framing, focus depth, planned cuts, state gates, tempo, lighting, and emotional performance.

## Final conflict check

Before delivery, reject or repair these combinations:

- speech plus pauses exceeds the assigned beat;
- a camera angle reveals a locked detail before its trigger;
- a character assigned silence for that interval is given conflicting dialogue, or a competing action breaks feasibility; intended overlap is not a conflict by itself;
- several characters require different complex emotions under one global emotion control;
- the prompt requests a camera behavior that conflicts with its `#` Movement tag or the Studio control card;
- the shot asks for deep group focus while the control card selects very shallow focus;
- acceptance checks contain broad aesthetic preferences rather than pass/fail requirements.
- any internal identifier such as S1–S6 is used as model-facing direction; readable project tracking IDs may remain outside the prompt;
- any FACS label, AU number, C1/P0-style code, or A–E expression grade appears in the delivered image or video prompt;
- a paste-ready prompt depends on relative wording such as `沿用上一镜`, `同上`, or `见上文`;
- a CLI-only schema field is presented as a visible web control without current page evidence.
