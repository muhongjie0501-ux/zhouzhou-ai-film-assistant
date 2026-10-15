# Studio control router

Cinema Studio 3.5 UI baseline: 2026-09-10. Cinema Studio 4.0 UI baseline: 2026-10-06. Live hosted MCP exact 3.5/4.0 model-schema refresh: 2026-10-07. The earlier CLI workflow-schema baseline is 2026-09-13 unless `platform-state.json` records a newer successful check. Read that file for freshness and `platform-access.md` before any live check.

## Keep four layers separate

- Cinema Studio 3.5 or 4.0 is the workbench/workflow.
- Seedance 2.0 or 2.5 is an underlying video model family.
- A preset is a reusable motion or style recipe.
- A Skill is guidance and orchestration for an AI agent.

Do not rename one layer as another. A generic model-catalog entry is not automatically the workflow behind the current Studio page. The current MCP exposes exact 3.5 and 4.0 callable model IDs; the earlier CLI confirms branded workflows. Neither exact schema exposes an underlying engine identity. The version-specific official Help Center explicitly says 4.0 runs on Seedance 2.5, so this may be reported as an official documentation claim, not as an independently exposed backend field. Overlapping mode or reference fields alone are not enough.

## Select the generation unit before the version

Choose one generation when there is one dominant cause-and-effect chain, one readable camera idea, one major spatial change, and one emotional turn.

Split when independent trajectories, contacts, identities, camera axes, dialogue turns, reveals, injuries, or outcomes compete. Preserve the user's event order; each generation carries one dramatic objective and a stable end state.

Then select:

- 3.5: concentrated beat within 15 seconds whose needed controls exist in 3.5.
- 4.0: deliberate 16–30 second performance, restrained dialogue, simple sustained action, a small structured sequence, or a verified 4.0-only mode/control.

Prefer the neighboring shot's version when both can work. Compare generated seconds, expected usable seconds, and number of paid attempts. Do not create six half-used 15-second generations when one or two coherent 30-second generations are genuinely readable. Do not place a whole dense fight into 30 seconds merely because the option exists.

One failed generation keeps the same version unless observable evidence shows that version lacks the necessary capability.

After splitting an overloaded scene, re-evaluate the new units but keep one Studio version across the scene when practical. Do not assume 3.5 is inherently better for action. If the scene deliberately occupies 16–30 seconds, benefits from the current 4.0 reference/director controls, and has no verified 3.5-only advantage, prefer 4.0; isolate only the fragile contact as a shorter insert. Prefer 3.5 when the complete beat truly fits within 15 seconds and its existing scene continuity or control grammar is the clearer advantage.

## Evidence levels for controls

1. Current visible page/Appshot: exact click instruction is allowed.
2. Live MCP/CLI exact schema: proves a field or model capability, not necessarily a visible web button.
3. Dated official help/tutorial: reliable version guidance, but may lag the account UI.
4. Cached example: useful cinematography language, not a complete menu.

Never promote levels 2–4 into a level-1 label. Do not expose an opaque ID. Do not infer Multi-shot from a CLI field. Do not interpret the unlabeled 1/4 selector.

## Prompt versus control ownership

The prompt owns:

- visible subjects and reference roles;
- first-frame geometry and screen direction;
- chronological action and cause/effect;
- performance and physical response;
- dialogue, ambience, effects, and final visible state.

The control card owns:

- Studio route, duration, resolution, aspect ratio, audio;
- genre, era, tempo;
- camera body, lens, focal length, aperture, movement;
- selectable palette/lighting presets and a global emotion control when visible. These choices implement the approved look; they do not independently redefine scene time, physical sources, light direction or performance.

Cinema Studio 4.0 Movement has one narrow exception: when a specific verified preset is useful, its exact `#English preset name` may appear at the intended beat in the complete video prompt so the director can manually select the matching popup candidate after pasting. The card records the same movement choices in the same order; the tag is a UI-binding entry point, not a competing camera owner. A pasted plain-text tag alone is not evidence of binding. Do not assume bulk paste selects multiple tags, and do not use this convention for image prompts or another Studio route without current UI evidence.

For light and spatial authority, follow [performance-space-methods.md](performance-space-methods.md). Preserve the approved scene baseline across actual references, prose and controls. Describe a control's visible result in the prompt only when needed for story clarity. The described camera path and any `#` Movement tags must support one another. Reject camera, depth-of-field, light, tempo, or movement contradictions between the two layers.

## Manual click order

Cinema Studio 3.5:

1. Genre.
2. Style: Color Palette, Lighting, Camera MoveSet Style.
3. Camera: Camera, Lens, Focal Length, Aperture.
4. Relevant visible bottom-bar settings.

Cinema Studio 4.0:

1. References.
2. Film setup: Genre, Era, Tempo.
3. Camera: Setup, then Movement when needed. Setup contains Camera, Lens, Aperture.
4. Color palette.
5. Lighting.
6. Relevant visible bottom-bar settings and any separately visible emotion control.

Output one table with 网页板块 | 子模块 | 选择 | 理由. Finish one panel before moving to the next. Omit unchanged Auto values when a very simple prompt does not need a full card.

## Exact-duration discipline

State the generation duration separately from the intended edit interval. Use an exact visible/selectable value. Default to using the complete generated duration. Pace a simple action with a meaningful lead-in, reaction, and stable dramatic ending when that serves the director's intent; do not pad with meaningless stillness.

A label such as 生成15秒｜计划使用0–8秒 means the user receives and pays for 15 seconds but plans to keep only the first 8. Use partial trim only for an explicitly short edit requirement or one critical insert after more efficient routes have been rejected; never make it the routine solution.

If an exact duration choice is not visible and current accuracy matters, follow the refresh protocol or ask for the opened duration menu. Do not turn an estimated beat length into a claimed UI option.
