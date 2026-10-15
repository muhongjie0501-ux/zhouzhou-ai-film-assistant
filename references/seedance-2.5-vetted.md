# Seedance 2.5: recorded schema and route boundary

Read this when Seedance 2.5 itself is selected or when a version-specific official Studio source attributes the selected route to it. A documentation attribution can justify considering shared shot methods; it does not independently verify the backend or make model API parameters into Studio buttons. The recorded Help Center description attributes Cinema Studio 4.0 to Seedance 2.5, while the inspected Studio schema does not identify its engine. Keep those two evidence types separate; see [sources.md](sources.md).

This adapter contains dated technical facts and directs execution to the film's common guides. It does not reproduce a downloadable vendor prompt template. Use [platform-access.md](platform-access.md) when the task needs a current read-only verification; do not silently treat this snapshot as a live result.

## Recorded model schema, 2026-09-13

- Recorded model ID: `seedance_2_5`.
- Duration: 4–30 seconds; resolution: 480p, 720p, or 1080p.
- Modes: `t2v`, `omni_reference`, `video_edit`, and `video_extension`.
- `t2v` is prompt-only. Use `omni_reference` for image, video, or audio references.
- Supported media roles in this dated schema: start image, end image, image references, video references, and audio references.
- `video_edit` edits one source video; its duration and aspect ratio follow the source rules rather than the ordinary output controls.
- `video_extension` requires `extension_mode` set to forward or backward; its aspect ratio follows the source video.
- `generate_audio` controls output audio and is separate from an audio reference. `bitrate_mode` is standard or high.
- `t2v` accepts no reference media; `omni_reference` requires at least one reference item.
- The total reference-media limit is 50. Image references plus start/end images may total at most 30.
- `video_edit` requires exactly one video reference. `video_extension` requires at least one video reference and an extension mode.
- Start and end images are accepted only in `omni_reference` mode.

These are underlying-model invocation facts, not proof of visible Cinema Studio 4.0 buttons. The official Help Center's 4.0-to-Seedance-2.5 attribution is a separate documentation claim, not a field in this schema. The recorded schema does not enumerate reference weighting or separate video/audio quantity ceilings beyond the total-media rule; never invent them.

## Use the common filming workflow

The approved shot determines prompt structure. Start with [prompt-and-shot-guide.md](prompt-and-shot-guide.md) for feasibility, timing, camera intention and reference needs. Then use [prompt-delivery.md](prompt-delivery.md) for assembly, Element names, a complete English/Chinese pair and separation of prose from controls. Include only the sections needed to express the approved shot.

Inspect the active assets before making their contents a premise of the shot. The set must support the intended route, people must begin where the action requires them, and a later state must not accidentally be supplied as the opening. Resolve conflicts using [performance-space-methods.md](performance-space-methods.md); a generous reference limit is not a reason to include more images.

When adapting a shot to this route, preserve the scene's dramatic and edit requirements. Add detail to the specific performance, interaction or transition that would otherwise be ambiguous; do not expand every prompt into a technical catalogue. Physical diagnosis and camera-drift checks remain available from the common shot guide even when a different model is selected.

Select only fields actually offered by the chosen route. Output audio and an input audio reference serve different purposes; neither proves that a particular voice or lip-sync control is present. Keep route facts, official documentation claims and untested expectations distinct. No field or prompt guarantees exact identity, timing or visual matching, and no adapter grants permission to generate.
