# Prompt and shot decisions

Use this reference for the requested shot/coverage plan or current clip, reading only the relevant sections. Detailed prompt assembly and bilingual delivery live in [prompt-delivery.md](prompt-delivery.md). These are production heuristics, not creative rules.

## Preserve the director's idea

Extract these facts before rewriting:

- active subjects and independently controlled groups;
- first-frame positions, facing directions, screen direction, and scale;
- one dominant action, sustained state or emotional change;
- camera behavior, separate from subject behavior;
- final visible state for the edit;
- required sound and dialogue, including approved offscreen sources;
- director locks versus negotiable technical choices.

Translate emotion into visible performance: gaze target, eyelids, brow, jaw, lips, breath, swallow, fingers, shoulders, posture, hesitation, vocal pressure, and interaction with props. Use only the cues that matter; a face overloaded with simultaneous expressions becomes unreadable.

## Choose a camera from the information the scene needs

First identify the relationship the audience must be able to read during this shot. That may be a person and an exit, the distance between two speakers, a concealed observer, a small expression or a decisive contact. Decide which part can remain hidden and which part must stay visible. A camera choice succeeds when it communicates that relationship with the intended feeling; a lens label by itself does not do so.

Place the camera relative to the action before choosing an optical description. Moving nearer, farther, higher or to the other side changes the view of the set and the relative size of near and distant objects. A nearby camera can connect the viewer to a character's movement; a distant viewpoint can make observation feel detached. These are options to test against the scene, not universal emotional meanings assigned to lens lengths.

Next choose the needed framing and readable depth. A reaction might require the whole upper body or only the eyes; a close shot need not discard all background information. A geography shot must reveal the relevant paths and landmarks; a wide-angle label alone cannot guarantee that. Use occlusion deliberately, so a foreground object does not accidentally hide the gesture or contact that makes the beat understandable.

Perspective depends on viewpoint and the relative distances of objects from the camera. With viewpoint unchanged, focal length and image format change the field of view and framing, not the underlying perspective. Moving back to maintain subject size while using a longer focal length changes perspective because the camera moved. Distinguish this from merely cropping a view.

Depth of field depends jointly on aperture, focus distance, focal length and imaging format. Choose what needs to remain readable instead of assuming that a long lens always blurs the background or a wide lens keeps everything sharp. A focus change can be intentional storytelling; do not impose constant sharpness when the director has approved a transfer of attention.

Describe the visible effect needed for the shot, using numerical settings only when the selected controls and the creative purpose support them. Avoid a preset quota of camera distances, FOV values, blur levels or concealment percentages.

### Camera support and motion

A locked viewpoint, a moving support and an operator-carried camera produce different relationships between the camera and the action. Select the behavior that serves the approved beat. For handheld work, describe the relevant adjustment: the operator catches up after a subject changes direction, settles into the framing, or absorbs a stop. Keep the essential action readable. Do not add continual jitter simply to signify documentary realism, or remove an approved deliberate instability as if it were always a defect.

### Lighting in the selected view

Use the responsibility chain in [performance-space-methods.md](performance-space-methods.md): ① approves the lighting baseline, ② supplies compatible assets, and ③ writes the shot from its chosen camera position. The side of a face that appears bright can change when the camera moves while the light source remains in the same world position. Preserve that distinction across coverage.

Determine which story information must be exposed clearly and which may be lost in intentional shadow or brightness. Highlights in eyes, reflections and cast shadows need to agree with the established sources. Do not replace these relationships with a generic beauty-light request or allow a new angle to imply an unapproved time of day.

Selectable lens, aperture, lighting, palette and movement settings belong in the control card under [studio-controls.md](studio-controls.md). Describe a necessary visible result in the prompt only when it supports the approved shot and agrees with those controls. The Cinema Studio 4.0 Movement `#` exception remains governed by [prompt-delivery.md](prompt-delivery.md). When controls, references and the plan cannot agree, resolve the affected input with its owner before proceeding.

## Decide one generation or several

Count independent trajectories, not headcount. A six-person squad can act as one unit if all members receive one cue, perform the same action, and hold the same end pose. They become separate control burdens when they need different timing, targets, directions, reactions, injuries, dialogue, or end states.

Prefer one generation when all are true:

- one dominant cause-and-effect chain;
- one readable camera idea;
- at most one major spatial reconfiguration;
- at most one emotional turn;
- the final state follows naturally from the opening geometry.

Recommend a split when several of these compete:

- more than three independently tracked people or two opposing groups;
- reveal, impact, injury, counterattack, retreat, and dialogue in one prompt;
- exact tactical blocking plus fast camera travel;
- two or more creatures or vehicles with separate paths;
- identity-sensitive close acting mixed with large-scale physics;
- several impacts, location changes, or emotional turns;
- a requested cut, angle change, or lens-language change hidden inside one long prompt.

Do not delete events. Preserve the user's order and make one generation carry one dominant beat with one readable end state. For every split, add a continuity handoff: subject positions, screen direction, wardrobe/prop state, damage, light direction, and the exact first-frame condition of the next generation.

Prefer the same Studio version across adjacent generations for visual continuity. Mix versions only when a verified capability creates a clear benefit, and warn about possible texture, motion, color, or identity drift.

## Choose 15 seconds or 30 seconds

- **3–6 seconds:** impact, glance, turn, reveal, insert, reaction, entrance, or explosion beat.
- **6–10 seconds:** one complete action or one short emotional response with a simple move.
- **10–15 seconds:** one small dramatic beat with beginning, development, and end.
- **16–30 seconds:** a deliberately continuous one-take, slow reveal, restrained dialogue/performance, or simple sustained action that benefits from natural time.

A 30-second route provides breathing room, not unlimited event capacity. Dense combat, many independent bodies, exact causal timing, and changing camera axes still need a complexity check. However, do not automatically convert them into many fixed 15-second jobs whose useful action ends halfway through. Compare generated seconds with usable seconds first. When the scene has two coherent dramatic halves, two structured 30-second 4.0 generations may be more efficient than six half-used 15-second 3.5 generations.

For a 30-second action generation, aim for about three or four readable internal shots and no more than one or two major physical interactions. Each internal shot needs one camera idea, one dominant action, and a clear end state. If identity, contact physics, or screen direction still compete, split again or isolate the critical interaction as a short insert. Conversely, 4.0 may still be the right choice for a short shot when a capability shown on the current 4.0 page or verified by its exact workflow schema is essential; do not borrow Seedance model modes and call them Studio controls.

If the UI offers only fixed durations, choose the nearest longer duration, finish the intended beat on time, hold a stable end state, and tell the user where to trim. Never silently stretch the narrative.

Treat large trim waste as a route penalty. Default the planned usable interval to the entire selected duration. Let a simple beat breathe through purposeful setup, observation, reaction, and a usable ending when that preserves the director's intention; never add empty padding just to fill time. 生成15秒｜计划使用0–8秒 means exactly that the user pays for and receives 15 seconds but expects to keep only the first 8 seconds. It is acceptable only for an explicitly short edit or a single hard insert after more efficient routes have been rejected, never as the repeated default.

## Budget dialogue before promising the duration

Dialogue time is part of shot capacity. Prefer an actual read-through or supplied voice track. When neither exists, use a conservative planning estimate rather than pretending exact timing:

- restrained or emotional Mandarin: roughly 3–4.2 spoken syllables per second;
- ordinary clear Mandarin: roughly 4–5 spoken syllables per second;
- urgent Mandarin: roughly 5–6 spoken syllables per second only when faster delivery is creatively acceptable.

Add deliberate pauses, speaker handoffs, breaths, non-speaker reactions, and actions that cannot occur naturally during the line. Preserve headroom for transitions. If the budget does not fit, offer explicit choices: shorten dialogue with director approval, move to a longer verified route when the physical action is simple, split the generation, or use approved post-dubbing. Never silently drop words, overlap speakers, or make a calm character speak unnaturally fast.

For multiple speakers, define a speaking protocol:

- one active speaker per turn unless overlap is intentional;
- the speaker's delivery and exact stop point;
- what each listener visibly does; silence applies only where the director has not requested an interjection or overlap;
- the cue that transfers speaking rights;
- whether lip synchronization or exact words are pass/fail requirements.

For director-requested natural overlap, retain the interruption entry cue/word, whether the first speaker continues, the essential audible words, and reactions. Account for overlapping time rather than serializing every line; do not erase the approved ensemble energy. Audio must actually be heard to confirm this outcome.

## Use state gates for timed reveals

When an object, costume detail, character, expression, injury, transformation, or location must appear only after a specific event, describe three states:

1. **Before:** what the camera can see while the reveal remains hidden.
2. **Trigger:** one visible, unambiguous action that changes the state.
3. **After:** what must now be visible and how the camera confirms it.

Keep camera framing consistent with the gate. A wide or overhead angle that reveals the target early conflicts with a later delayed reveal. For supernatural visibility rules, separately lock who can perceive the entity and whether it creates shadows, reflections, contact, or environmental reactions.

A reference that visibly shows the hidden state can compete with the gate. First prefer a start/composition reference that physically occludes the hidden detail. If the hidden design must also be exact, assign that design reference only to appearance, keep the opening frame incapable of showing it, and disclose the risk. When the reveal is a pass/fail story condition and the two authorities still conflict, split before and after the reveal instead of pretending prose can guarantee both.

## Keep acceptance checks small and outside the prompt

Use a short post-generation checklist only for conditions whose failure prevents the intended use of the shot or selected interval: an exact line, identity, count, reveal order, screen direction, world-state rule, or final edit frame. Assess other usable portions separately. Make every check objectively observable. Present it to the user as `生成后检查`, outside the paste-ready prompt, with no more than three items. Do not use internal labels such as `P0` in the delivered answer. Keep broad taste discussions separate from these compact checks, but include a director-locked dramatic/aesthetic requirement when it determines whether the intended use succeeds. Technical stability must not silently flatten approved performance, comedy or spectacle.

Use a compact negative list only for recurring, high-cost failure modes or a verified negative-prompt field. Prefer positive visible target states in the main prompt; repeatedly naming every forbidden object can dilute attention or reintroduce it.

## Decide whether a reference image is needed

Recommend a reference when one or more must be exact:

- recurring face, costume, creature anatomy, vehicle, prop, or scale;
- location geography, architecture, light direction, or production design;
- first-frame group count, formation, rear/front orientation, eyelines, or camera height;
- a close-up facial configuration or body pose that prose is unlikely to anchor;
- an end-state composition, transition boundary, or match-cut frame supported by the selected mode.

Use text alone for generic establishing shots, simple atmosphere, one-off background figures, abstract motion, or a single subject whose exact geometry and identity do not matter.

Use the smallest useful reference set. Record each primary role and material exclusion in working notes, such as `身份与服装；忽略背景和光线`; put only necessary conflict-resolving exclusions into the prompt. Actual image content still influences generation, so inspect its moment and compatibility under [performance-space-methods.md](performance-space-methods.md). Do not pretend a general reference is a pinned start/end frame. Identify whether the current slot is a start frame, end frame, Element, identity reference, composition reference, or general style reference.

For an exact synchronized group viewed from one direction, prefer one formation image showing the entire geometry over several competing portrait references. Put the desired aspect ratio in the UI settings line, not inside the paste-ready image prompt. A separately approved identity image may supply face detail when the formation image is insufficient. A wardrobe-only sheet must not override identity; check the person-to-position mapping and actual face resolution.

## Write every requested reference-image prompt

For each missing still, return compactly:

1. **Element名称（请按此保存）** — choose a short, unique Chinese name suitable for the Higgsfield Element picker. Prefer `地点或项目 + 主体 + 用途`, such as `雨后车站双人候车构图` or `黄铜门锁结构参考`. Give only the plain name to copy into the **Name** field, without `@`; in the recorded Higgsfield interface the separate **Element ID** displays `@` plus that name. Once assigned, reuse the exact spelling later.
2. **用途** — one sentence stating what the video model should learn and what it must ignore.
3. **图片提示词** — one concrete still-image prompt that depicts a stable moment, not a sequence of actions. Include important composition in natural visual language, but omit UI-owned basics such as aspect ratio, resolution, frame rate, model name, and style-control labels.

Do not generate the image. The user prepares and approves it before using the video prompt.

When the user needs a **new** reference still and model choice materially affects it, optionally name one candidate **outside** the copy-ready image prompt, using the dated candidates below only as a starting point and checking the current image-model catalog and the user's visible options when needed under [platform-access.md](platform-access.md):

- Photoreal character turnaround or reference-face edit: Seedream 5.0 Pro is a candidate because the recorded model schema accepts image references. Keep a stable identity and wardrobe across views; a model name cannot guarantee that consistency.
- Pure empty location made from text: Soul Location is a candidate. Its recorded schema accepts no input images, so do not recommend it for editing an approved location or assembling an existing set and character.
- Cinematic shot-opening still made from scratch: Soul Cinema is a candidate for the film look. If the first frame must combine existing character, location, and prop references in exact positions, choose a currently verified image-reference-capable route instead; do not mistake an identity Element or empty-location Element for an exact Start frame.
- Stylized/cartoon character: consider the current Nano Banana option only when that visual style fits the film, and verify its displayed model and exact ID at use time. The recorded official CLI Skill and hosted MCP disagree on a Nano Banana ID mapping.

These are conditional candidates, not fixed defaults, quality guarantees, or authorization to generate. Do not put a model name, resolution, or aspect ratio inside the paste-ready prompt; leave actual model selection to the director.

For every reference prompt, give one complete English paste-ready prompt followed by one faithful full Chinese translation for review. Preserve the same subject count, Element names, composition, exclusions, and intended authority in both versions; the translation must not add or remove requirements. Keep UI settings such as aspect ratio out of both prompts. Do not duplicate the reference purpose, control table, or checklist in English.

When composing **any image or video prompt** or 调用要素 line, prefix every mention of a named Element used as a reference with exactly one `@`: `@晚班值守员`, `@车站候车厅`, `@失物领取单`, and `@候车厅双人开场`. This includes an explicitly planned Element that the director will create before using that prompt; state the creation order when it matters. Keep these Chinese names and `@` prefixes unchanged in the English prompt and Chinese translation. Do not put `@` in the separately supplied Element名称, and do not make the image prompt for a new Element refer to that same not-yet-created Element. The last example applies when the first-frame asset is saved as an Element; a dedicated uploaded start/end-frame slot is a separate attachment, not something an `@` mention can create. Do not prefix generic nouns or invent unnamed assets, and do not equate pasted `@` text with a confirmed webpage asset binding.

## Choose continuity references intelligently

Do not automatically feed the previous generation's last frame into the next generation. Use the actually selected edit out-point and its observed picture/sound state when known; a planned end state is not evidence. If selection is provisional, say so. A continuous match, time ellipsis, and new scene have different continuity needs.

Use the previous end frame as the next start frame only when the edit requires actual pixel-level continuity, such as:

- continuous action or video extension;
- match-on-action across a generation boundary;
- the same camera axis and nearly the same composition;
- exact pose, contact point, or prop position continuing without a deliberate cut.

Do not use it when the director intends:

- a new angle, reverse angle, different shot size, insert, or reaction close-up;
- a new establishing composition;
- a clean reset after the previous result acquired bad anatomy, clutter, smoke, damage, or incorrect geometry.

For a deliberate cut, maintain continuity with the same approved Elements and a new shot-specific composition/start reference only when needed. Restate identities, costume, subject count, damage state, light direction, and screen direction; preserve those facts rather than the previous frame's pixels. For several timecoded shots inside one 4.0 generation, describe the cuts inside the prompt—no artificial tail-frame/start-frame chain is needed between them.

## Keep internal continuity labels internal

Temporary labels such as S1–S6, A/B images, R1 references, or priority levels can help internal reasoning, but a video model cannot infer them reliably across independent generations. Project indexes and handoffs may use readable shot/asset IDs for traceability, but these are not instructions the video model understands. Never put internal codes in a paste-ready prompt; in user-facing continuity descriptions pair tracking IDs with readable names rather than substituting unexplained codes for visible relationships. Translate every identifier into a visually recoverable description based on the current first frame, such as `靠近售票窗口的值守员`, `长椅左端的旅客`, or `站在出口旁的工作人员`. When exact identity across clips matters, use an approved frame or Element rather than relying on a code. Never write `沿用上一段`, `同上`, or `见上文` inside a paste-ready prompt; restate the necessary visible first-frame condition.

Every generation header shown to the user must distinguish two values:

- **实际生成秒数** — the duration selected on the current Studio page;
- **计划使用秒数** — the useful portion expected to survive the edit.

Normal example: `片段1｜窗口交接与听者反应｜Cinema Studio 3.5｜生成15秒｜计划使用0–15秒`. The actual generation duration is always one exact verified UI value, never a range such as `8–9秒`. Never invent a 6-second Studio option merely because an action should last 6 seconds. A partial-use plan such as `生成15秒｜计划使用0–6秒` is an exception for one critical insert after the more efficient routes have been rejected, not a default scene-building method. If available values are unknown, label the generation duration as awaiting current-page confirmation. Duration may stay outside the paste-ready prompt unless the prompt contains a timed reveal or other beat that requires explicit timing.

Label Cinema Studio 3.5 or 4.0 as the `Studio版本`, never as the video model. Include a separate `引擎/模型` only when a distinct model selector is visible and the chosen name is verified; otherwise omit it rather than inferring that Studio 3.5 equals Seedance 2.0 or any other model.

## Compose action and emotion safely

For synchronized groups, use: shared visible/audible cue → same-beat reaction → identical body action → held readable end pose. Lock exact count, keep every member visible when composition allows, maintain screen direction, and state facing direction positively.

For fights, separate attacker path, defender response, contact point, weight transfer, environmental reaction, and end positions. Avoid asking the model to resolve several simultaneous contacts and camera changes in one beat.

For emotional acting, specify a simple arc such as neutral restraint → recognition → suppressed fear. Anchor it in face, breath, hands, and posture. When several faces need different arcs, use separate close shots or simplify the group performance.

For intended absence, describe the visible target positively: `屋顶线空无一物，只有碎瓦和尘土滑落`. Keep exclusions in the reference note or risk section rather than repeating the unwanted object throughout the prompt.

## Retry by diagnosis

Repair the smallest main cause and its necessary dependencies. Before another prompt retry, check that the reference set itself is compatible and that removed assets leave no missing identity, pose, light or state authority. Typical starting points:

- wrong count or placement → improve the first-frame composition reference;
- broken identity → reduce competing references and strengthen role assignment;
- skipped action → shorten the causal chain or split it;
- weak emotion → simplify to one arc and add visible micro-actions;
- confused camera → remove competing movement instructions and use the smallest coherent set of available controls: none, one, or several in an explicit order as the intended movement requires;
- bad contact/physics → for a contact failure, isolate the important interaction and state start/contact/end geometry; for other motion or material failures, use the relevant diagnostic below;
- style conflict → reconcile the scene lighting baseline, reference content and verified controls; remove redundant prose without discarding required visible light relationships.

Do not rerun an overloaded prompt unchanged. More generations of the same unresolved design usually waste credits.

### Investigate a physical failure at the affected moment

Use this during shot design when an interaction is important, or when reviewing an actual failure. Begin with what is visible before, during and after that interaction. Identify the bodies or objects involved, their supports, direction of travel and the cause of any change. This provides a small testable explanation; it is not a requirement to describe all physical phenomena in every prompt.

For an unintended slide or pass-through, inspect the contact rather than diagnosing from one frame. A foot's support interval, a hand's grip or an object's resting surface must remain consistent with the body's movement. Check whether the apparent slide is instead camera movement or an intended action. Clarify the relevant support and release; do not prescribe heel-first contact for all walking, running or stylized motion.

When a moving load changes speed implausibly, locate the missing cause. A person may brace, another object may collide, or a grip may fail; the required response depends on the approved action. Relate the object's motion to the support and the body carrying it. Weight does not mean that every movement must be slow, and a stop needs an intelligible force rather than a heavy-sounding adjective.

For a secondary movement, consider what is attached to what and how flexible it is. A loose hem can continue moving briefly after a turn; rigid armor may not. Add follow-through or settling only when it would be visible and appropriate to the actual material. Do not animate every surface merely to fill a quiet beat.

For a contact that should change a surface, check the material and the available view. Liquid can transfer, bead, spread or be absorbed differently on different surfaces; what remains must follow the established interaction. Request only the trace needed to make this action coherent. Do not add debris, dirt, blood, snow or other effects absent from the scene.

Treat these as competing explanations to inspect. Choose the smallest correction supported by the evidence, keep related reference and contact geometry consistent, then review the repaired interval. If the inputs cannot support the action, return the affected asset or plan to its owner instead of repeatedly elaborating the same prompt. This method is available from ordinary shot work and repair, without selecting a particular model.

### Check a change in camera appearance against the plan

Compare the approved purpose with the actual take at the point where useful information disappears or an unwanted look begins. Separate an intended cut, zoom, camera move or focus pull from an unplanned change. A different appearance is not automatically a defect.

Suppose the scene requires the viewer to watch a hand reach for a key while the listener's response remains visible, but the result shows only the reaching hand. First locate when the listener is lost. Determine whether the frame tightened, a person or camera moved, an object blocked the view, or focus made the listener unreadable. Check the active references and controls for instructions that compete with the plan. Do not infer a precise focal length from the look alone.

Restore the particular relationship that the shot needs through the relevant asset, framing, focus or movement instruction. Keep the existing distinction between viewpoint, focal length and depth of field. A proposed new coverage choice belongs with ①; a correction of the agreed shot belongs with ③ and is checked by ④ against the actual result. Reinspect the affected interval before calling it resolved, without imposing universal FOV, distance or blur settings.
