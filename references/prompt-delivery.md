# Prompt compilation and delivery

Read for image/video prompt work in roles ② or ③. This file preserves the detailed prompt rules formerly in the main entrypoint. It does not grant platform operation or generation permission. Project storage and handoff are defined in [project-workflow.md](project-workflow.md); technical shot design remains in [prompt-and-shot-guide.md](prompt-and-shot-guide.md). Read only the sections relevant to this request.

## Make one firm production recommendation

Use three layers in order:

1. Hard capability facts: current duration limits and verified version-only features.
2. Director risk: independent trajectories, contacts, identities, blocking, camera changes, dialogue, performance, continuity, and expected usable seconds.
3. Stability and efficiency: prefer the adjacent shot's version when both can work; compare generated seconds, usable seconds, and paid attempts.

Current dated baseline:

- Cinema Studio 3.5: strongest candidate for a concentrated shot within 15 seconds with one dominant cause-and-effect chain.
- Cinema Studio 4.0: strongest candidate for a deliberate 16–30 second performance, restrained dialogue, simple sustained action, or a verified 4.0-only control/mode. Treat it as a Studio UI route; do not infer its underlying model from a marketing page, a generic model catalog, or the number 4.0.
- A 30-second allowance gives breathing room, not unlimited choreography. Split overloaded fights by dramatic objective.
- One failed generation does not justify switching versions. Switch only when evidence shows the required capability is missing from the chosen route.

Give one primary recommendation and its short reason. Mention an alternative only when a creative choice or new evidence could genuinely overturn it. Read prompt-and-shot-guide.md for complex routes and repair work.

## Choose references deliberately

- Use text alone when identity, anatomy, geography, or exact first-frame geometry does not need locking.
- Use the smallest useful reference set. Assign each reference one primary authority and record material exclusions in working notes; include an exclusion in the model-facing prompt only when needed to resolve a real conflict. These assignments guide attention, not hard isolation of image content. Inspect the actual asset and its temporal state; use the compatibility method in [performance-space-methods.md](performance-space-methods.md).
- For an exact group, a formation reference owns count, geometry, and the person-to-position mapping. An explicitly approved identity image may own that person’s face; a wardrobe-only sheet must not replace identity. Judge whether actual face detail is sufficient for the shot, rather than banning identity from all group images. A location image owns architecture/path; a creature sheet owns anatomy. Confirm the mapping when combining them.
- Name every new reference exactly as: Element名称（请按此保存）：short stable Chinese name **without `@`**. This is the value the director copies into the Higgsfield **Name** field; the shown interface displays a separate **Element ID** such as `@车站候车厅`.
- In every paste-ready **image prompt and video prompt**, as well as any 调用要素 line, prefix each mention of a named Element used as a reference with exactly one `@` before its saved name. Apply this to existing Elements and explicitly planned Elements that the director will create before running that prompt. Keep the same exact Chinese names and `@` prefixes in the English source prompt and Chinese translation; never translate, abbreviate, renumber, or double-prefix them. For example: `@晚班值守员 controls facial identity, hairstyle and clothing, not the background or expression.`
- Do not add `@` to the Element名称 line or reference a new Element as `@名称` inside the image prompt that creates that same Element. Do not prefix generic subjects or invent unnamed Elements. A written `@名称` does not by itself prove the webpage has bound the asset; check the UI after pasting. Dedicated uploaded start/end-frame slots remain separate and are not replaced by an `@` mention. If the current page has no such slot, call the image an opening-composition reference, never a bound/locked Start Frame, and do not instruct the user to use a nonexistent slot.
- Keep instructions to upload, select, or bind a Start/End frame outside the paste-ready prompt. Inside the prompt, describe what the opening frame visibly contains and how the camera and subjects move from it; an instruction to upload an image is not a visible scene action.
- For each needed reference, provide one complete English image prompt for direct copying and one faithful full Chinese translation for review. Do not include aspect ratio, resolution, Studio version, or other UI-owned basics.
- Only when a new reference image is actually needed and choosing its image generator would improve the result, offer one optional, currently checked model suggestion by asset purpose. Keep that suggestion outside the paste-ready prompt; do not impose a model, change the director's existing image workflow, or treat MCP catalog presence as proof that the model is visible in the reader's account. Use the conditional routing in prompt-and-shot-guide.md.
- Do not fabricate a separate Element ID or assume a planned Element already exists. The shown UI displays `@名称` as its Element ID; a planned `@名称` reference is usable only after the director creates that Element.

## Compile the prompt adaptively

For image prompts, use the relevant [image asset methods](image-asset-methods.md) branch: a new asset describes what its purpose requires; an edit identifies the source version, intended change, critical preservation scope and necessary consequences. These are internal decisions, not mandatory displayed forms. Keep reference names, bilingual output, UI separation and actual-image checks under this guide.

For video prompts, select the smallest prompt form that can carry the shot:

- Simple direct: first frame and subject, one chronological action or emotion, camera behavior, final state, essential sound.
- Continuous one-take: explicitly keep one shot, lock opening geometry, subject path, camera path, physical cause and effect, and a stable ending.
- Structured internal cuts: use only for a small legible sequence supported by the selected route; describe each cut or time range inside one self-contained prompt.
- High constraint: use high-constraint-dialogue-template.md only for exact dialogue turns, visibility/state gates, tightly timed reveals, complex performance rules, or exact sound landings.

Choose exactly one primary form. A high-constraint prompt may contain structured internal cuts, but it remains one self-contained prompt rather than a second template or duplicate deliverable.

Before writing, assign each important fact to one primary execution carrier (distinct from the role that approved its meaning): a Studio control, a reference asset, a static prompt invariant, a timed beat, or a post-generation acceptance check. Put stable facts before changing events. Avoid redundant or conflicting identity, space, style, or performance instructions. An approved requirement may pass from plan to asset to necessary visible prompt language without becoming three competing decisions. Follow the lighting baseline in [performance-space-methods.md](performance-space-methods.md); resolve incompatible inputs rather than adding louder prose.

Build the prompt for this generation's complete span, not just its first picture. Include an entrance, reveal or offscreen voice when it belongs to that span, and make its timing or sound role clear. Use earlier footage or decisions to establish the state at the opening; do not replay an earlier line merely because it explains the character's present reaction. Review each remaining piece of project history: if it changes nothing the model should show or sound in this shot, leave it in the project record. Use [actor performance](actor-performance-and-facial-actions.md) to select the relevant behavior and voice choices. A character's full biography and private reasoning are not a substitute for the required visible or audible performance.

Cinema Studio 4.0 Movement is a narrow UI exception: a verified `#English preset name` in the prompt is the user's entry point for binding that movement, not a second independent camera instruction. Its placement, any prose describing the visible camera path, and the control card must agree.

Read performance-space-methods.md when the current beat needs multi-person spatial control, lighting continuity or coordinated performance. Story revision and directing decisions remain with ① within the user's requested scope. Read the relevant sections of actor-performance-and-facial-actions.md for recurring behavior/voice continuity, a face-readable reaction, nuanced or heightened acting, emotional dialogue, subtext, listener performance, or a failed expression; continuity alone does not require every acting method. Read dialogue-coverage-grammar.md for dialogue, interrogation, confrontation, interview, or reaction coverage that needs shot/reverse-shot, over-the-shoulder framing, clean singles, internal/external reverse angles, eyeline, screen direction, or axis continuity. These are conditional directing tools, not extra sections that every answer must display.

Use seedance-2.5-vetted.md only when Seedance 2.5 itself is explicitly selected or a version-specific official Studio source explicitly attributes the selected Studio route to it. Current official Help Center calls Cinema Studio 4.0 Seedance 2.5-based; the live Studio schema does not independently expose its engine identity, so label this as an official documentation claim and keep Studio UI controls separate from Seedance model fields. A shared field or version number alone is not evidence. Use seedance-2.0-vetted.md only when Seedance 2.0 itself is explicitly selected or its transferable prompt language is being compared; never infer that Studio 3.5 equals Seedance 2.0.

For every reference-image prompt and every video prompt, output exactly one bilingual pair in this order:

1. **英文提示词（复制使用）** — the complete paste-ready source prompt.
2. **中文翻译（审阅使用）** — a faithful full translation of that English prompt.

The two versions must carry the same shot count, timecodes, subject count, Element names, spatial relations, action order, dialogue, camera behavior, sound, exclusions, and final state. The Chinese version must not add, remove, weaken, or reinterpret a production requirement. Keep Element names and quoted dialogue in their approved form when translating them is not intended. Control tables, route explanations, and pass/fail checks remain single-copy Chinese content; do not duplicate those sections in English.

Before delivering either an image or video prompt, check that every actual named Element reference in the paste-ready English and Chinese text has its single `@` prefix. Keep the separately displayed Element名称 plain so it can be copied into the Name field.

Every video prompt must:

- be self-contained and chronological;
- establish current count, placement, facing direction, active reference roles, action, camera, performance/physics when relevant, sound, and final state;
- separate subject motion from camera motion;
- use visible behavior instead of decorative mood words or fake numerical precision;
- contain no internal codes such as C1, P0, S1, A图, R1, FACS, AU plus a number, or A–E facial-intensity grades, and no relative phrase such as 沿用上一镜, 同上, or 见上文;
- omit UI-owned basics and selectable control labels unless a visible result is essential to the story, except for an intentionally selected Cinema Studio 4.0 Movement `#English preset name`;
- use compact exclusions only for proven, costly failure modes.

For Cinema Studio 4.0, decide from the shot whether Movement presets help at all. Use none when prose is enough; use one or several only when their verified functions form a clear, ordered camera path. If used, put each exact, currently verified `#English preset name` at its intended point in the complete paste-ready English video prompt and preserve the same token in the Chinese translation. Do not invent names, stack presets by default, or put 4.0 Movement tags in image prompts or a 3.5 prompt without separate UI evidence. Pasting all tags as plain text does not prove they are selected: the director clicks the matching popup candidate for each tag manually. Do not manipulate page selections or claim that a bulk paste binds all tags automatically; authorized read-only inspection remains allowed.

Put no more than three objective pass/fail checks outside the prompt under 生成后检查.

## Continuity and failed-result rules

- A previous last frame is not the default next reference. Use it only for actual extension, continuous action, match-on-action, or nearly identical camera geometry.
- For a new angle, reverse, insert, reaction, or clean reset, reuse approved Elements and describe a new self-contained opening; request a new composition image only when existing inputs are insufficient. When continuing accepted footage, use the actual edit out-point supplied by editing, not an imagined end state or automatically the source file’s last frame.
- In repair mode, inspect observable evidence before rewriting. Classify the main failure as count/blocking, identity, reference conflict, action overload, camera/control conflict, dialogue/time, contact/physics, or platform/model limitation.
- Repair one main cause and its necessary dependencies per retry. If the reference set is incompatible, repair the smallest dependent asset group first. When removing a reference, identify who now supplies its identity, pose, geography, and state. Keep the model/version unless evidence indicates a platform/model limitation.

## Manual Studio controls

Keep the control card separate from the prompt. Read studio-controls.md and only the selected version file:

- studio-3.5.md for 3.5;
- studio-4.0.md for 4.0.

Use one compact table in the exact current click order with columns 网页板块 | 子模块 | 选择 | 理由. Keep settings in the card; the verified 4.0 Movement `#` tokens are the sole prompt-side UI-binding exception, and the card should name those same chosen movements in order when used. A CLI/MCP field is not automatically a visible web control. Do not invent Multi-shot, interpret an unlabeled 1/4 selector, or turn dynamic palette/movement examples into a complete current menu.

## Adaptive prompt delivery

Use the delivery location chosen under [project-workflow.md](project-workflow.md): long project prompts belong once in the assigned project file, with a short chat summary/link; small requests may stay in chat. Return only what the current request needs:

- Simple prompt request: one firm route sentence, essential manual controls from the verified dated baseline, one bilingual prompt pair, and checks only if material.
- Standard/precision request: new Elements if needed, shared controls once, then one clearly labeled block per generation with exact Studio version, exact selectable duration, intended usable interval, exact Element names, one bilingual prompt pair, differing controls, and up to three checks. Default the usable interval to the full generation; do not invent routine trim waste.
- Failed result: observable diagnosis, whether the route stays or changes and why, then the smallest repair of the main cause and its necessary dependencies.
- If the user only wants advice, do not force executable prompt sections.

Do not repeat shared settings, duplicate control tables or checklists between languages, dump raw schema, or produce a fixed dossier. Per generation or reference, deliver only one English source prompt and its one faithful Chinese translation. Offer up to three filming approaches only when the director asks for ideas or has no decided approach.
