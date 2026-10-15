# Post-production: selection, assembly, finishing, and delivery

Read this when the director requests take selection, editing guidance, sound, color, subtitles, or delivery. This is a practical directing and review method, not evidence that a particular editor or automation interface is connected. Read [project-workflow.md](project-workflow.md) for the project root, file ownership, evidence, and version rules.

## Establish what can actually be inspected or changed

Use available tools to inspect the specific user-provided media, authorized platform preview, timeline, or export relevant to the request. Verify access and tool capability before promising operations in DaVinci Resolve or another editor. A media file on disk does not prove that the timeline is accessible; a proposed edit list does not prove that an edit has been applied.

Distinguish advice, file analysis, making an approved new edit, modifying an existing timeline, and exporting. This guide does not authorize modifying the director's timeline or overwriting an accepted master. Execute those actions only when the user has authorized the corresponding work; reuse existing clear authorization without asking again. Preserve unrelated tracks, timing, and creative decisions in a narrow revision. Keep project records and any authorized outputs in the specified project locations, never in the installed Skill.

Inspect what matters with the tools actually available. Report visual inspection, audio listening, metadata measurement, timeline inspection, and full playback separately. If the tool cannot play or analyze sound, do not certify dialogue, overlap, accent, music clearance, or lip sync from silent frames. Do not automatically download platform reference images to enable review.

## Choose usable intervals, not merely the prettiest take

Start from the director's intended change in the scene and the latest accepted decisions. Compare available takes for usable performance, readable action and reactions, identity, geography, continuity, and sound. One defect may affect only part of a take. Identify that interval and whether an already available insert, reaction, or audio edit can preserve the intended scene; do not label an entire take unusable from one isolated frame.

For a proposed selection, give the source file or stable media identifier, take/version, source in/out interval, why it serves the scene, and any defect or unreviewed sound. For an actual selection, also identify the inspected timeline or export revision. Keep "recommended," "director accepted," and "actually used" distinct. Leave all final take choices with the director.

Read or measure source duration, frame rate, and audio presence when they affect an edit. State whether positions are source-relative seconds, source timecode, or timeline timecode; do not interchange them. Use frame-accurate boundaries only when the timebase and inspected frames support them. When calculating an interval, use a clear start-inclusive/end-exclusive convention or the editor's documented convention consistently.

## Build the scene and check the joins

Establish the scene's action and performance with the smallest useful coverage. Let a cut follow a change in attention, action, knowledge, or emotion; do not add cuts just to hide every generated movement. For a deliberate angle change, preserve shared world state rather than requiring identical pixels. Use [dialogue-coverage-grammar.md](dialogue-coverage-grammar.md) when eyelines, screen direction, or reverse angles are decisive.

At each important join, inspect the outgoing and incoming media together, in motion when possible:

- action phase, contact, hands, props, body position, and movement direction;
- face identity, wardrobe, screen relationship, background geography, and lighting continuity;
- breath, emotional residue, listener reaction, dialogue onset, and the sound carried across the cut.

Match-on-action needs a compatible phase of the same action, not a generic instruction to use the previous last frame. A cutaway can bridge time or focus attention, but cannot by itself repair contradictory geography or remove a story-required action. If an intentional discontinuity serves the director's choice, describe it as intentional rather than pretending a seamless match.

## Out points, handles, and sound tails

Choose the picture out point after the required action or reaction is readable and before an unusable drift, unless the director wants the lingering performance. Inspect nearby frames and listen around the candidate cut; a still image alone cannot establish a good exit. Preserve useful handles when present, but do not invent a fixed amount of unused footage for every shot.

Treat picture and sound boundaries separately. A breath, final syllable, laugh, ambience, or musical decay may need to continue after the picture cuts. A J-cut introduces the next sound before its picture; an L-cut lets the previous sound continue over the next picture. Use them only when they support the scene, preserve who is speaking and where, and do not erase an intended silence or surprise.

Record picture in/out, any separate sound in/out or tail, and the intended join when necessary. If only a mixed soundtrack is available, acknowledge that dialogue, ambience, and music may not be independently adjustable. Do not promise clean separation, recovered clipped speech, or exact lip sync without checking the available media and tools.

## Net runtime and revision

Use the actual adopted picture intervals and timeline arrangement to determine film length. Sequential selected durations add together; simultaneous picture overlap counts once, while real gaps, title cards, pauses, and tails extending the timeline count where they occur. Audio overlap inside the existing picture span does not add a second copy of that time. A transition consuming existing overlap is not automatically extra duration.

Label the result as an estimate until the actual timeline or export has been inspected. After a change, update only the affected source intervals, joins, and net duration in role ⑤'s record. Keep generated source duration, proposed usable duration, actual selected duration, and measured export duration distinct. Respect a supplied duration target without silently speeding dialogue, cutting required reactions, or removing story events.

## Request only the pickup the edit actually needs

First identify the precise missing editorial function: an unreadable contact, absent listener reaction, missing spatial bridge, unusable ending, or insufficient audio tail. Check whether existing footage already covers it. If new material is needed, specify the smallest useful pickup with its entry state, action/performance, exit state, eyeline/geography, and audio relationship to adjacent selected takes.

Send that concrete need to the appropriate planning or execution role through the agreed handoff process. Do not silently change the story, reorder recognized events, or initiate generation. If a proposed pickup requires a creative change, state the tradeoff for the director's decision. A new prompt is a proposal, not proof that replacement footage exists or has been accepted.

## Sound pass

Listen to the actual cut or relevant source audio when capability permits. Check line presence, speaker assignment, intelligibility, intended interruption/overlap, breaths and reactions, abrupt edits, ambience continuity, and the dialogue's relationship to effects and music. Preserve deliberately chaotic or comic interaction; clarity does not require turning every exchange into orderly isolated lines.

Use available separate tracks or stems when they genuinely exist. Where needed, suggest local level changes, fades, room tone, or a motivated sound bridge, then listen to the result. Keep important dialogue intelligible without flattening the director's intended music and dynamics. Do not claim noise removal or source separation will be artifact-free. Dubbing requires its own timing, performance, and visible-mouth check.

Respect confirmed music and dialogue landmarks in a score or voice-only revision. Choose loudness and peak targets from the actual requested delivery specification, not a universal number. Measure them with a capable tool when compliance is required; listening alone does not prove numerical compliance.

## Color and image finishing

Compare adjacent selected shots in motion before choosing corrections. Distinguish exposure or white-balance mismatch from a different physical light source, time of day, or wrong location. Match the intended scene continuity while preserving deliberate contrast. A grading adjustment cannot reliably repair missing light direction, incompatible shadows, or changed architecture.

Use scopes and known color-management settings when the editor exposes them. Check skin, highlights, shadows, saturation, and visible artifacts at relevant playback size. Do not apply an arbitrary LUT to every clip or promise that one preset produces a cinema-ready master. Preserve the intended look and make reversible adjustments within the authorized edit.

## Subtitles and text

Use the recognized dialogue as a starting point, then check against the actual audio; a script alone does not prove that a line was spoken exactly. Flag unheard or unclear words rather than inventing a transcript. Time captions to speech and readable phrases, identify speakers only when needed, and check that intentional overlaps remain understandable.

Distinguish a review transcript, sidecar subtitles, and burned-in text. Use the requested language, spelling, and delivery format. Check timing, line breaks, clipping, safe placement, and interference with faces or important action at the final aspect ratio. Do not burn in captions, translate dialogue, or add titles merely because a subtitle tool is available.

## Delivery and acceptance

Confirm the actual requested destination and format before an authorized export. Use its required dimensions, frame rate, codec/container, audio layout, subtitles, and other delivery properties where specified; otherwise state the chosen practical settings. Do not invent a broadcaster, competition, or theatrical specification or guarantee acceptance by one.

Preserve the current accepted master; use a distinct output version unless overwriting was explicitly requested. After export, verify the file exists at the intended location, probe relevant technical properties with a capable tool, and play the result through when feasible. Check opening, ending, important joins, captions, sound tails, and the absence of missing media, unexpected black/frozen frames, or silence. Partial inspection must be labeled partial, not "fully passed."

Return the deliverable link, the measured or explicitly estimated runtime, what was actually checked, and any material unresolved issue. Update the project's selected-interval and delivery record with the export version and evidence. Export completion is not the director's final acceptance; retain that distinction until the director makes the decision.
