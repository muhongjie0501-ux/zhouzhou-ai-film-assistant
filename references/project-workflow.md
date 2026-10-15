# Film project files and role handoffs

Read this for an ongoing film, work shared across chats, project-state maintenance, or a substantial Markdown deliverable. Use only the parts needed for the current assignment. A small question can still be answered in chat.

## One film, the director's existing directory

The director specifies the existing directory for each film. Use that exact project root; do not infer it from a chat's working directory, another film, or the last project used. If it has not been supplied, continue useful discussion or a clearly labeled chat draft and ask for the path before writing project files. Do not invent a path or create a film project on the director's behalf.

The installed Skill holds reusable instructions and blank templates only. Never write film state, actor or scene assets, prompts, review logs, temporary files, or caches anywhere inside the Skill directory. Do not keep a global "current film" pointer there. Project records belong in the specified film directory. Existing media can stay in their existing locations and be linked without moving or copying them.

A Skill is a role's instructions; a Codex chat is an executor; project files are shared records. File changes do not automatically update another chat's already-read context, start an idle chat, or schedule downstream work. Do not promise automatic synchronization or dispatch. A single chat may perform several roles when appropriate; five roles do not require five chats or five approvals for every shot.

## File ownership by responsibility

Use the existing project organization where it works. The following are responsibilities, not a mandatory folder tree or a demand to create every file at startup.

| Role | Owns the authoritative record | Reads as needed |
|---|---|---|
| ① Director planning and coordination | Director decisions, scene/shot-plan versions, and the short project entry/index linking the approved screenplay | Current project constraints and relevant production feedback |
| ② Reference assets | Image prompts and asset index, including actual image versions and checked roles | Current recognized shot plan and existing assets |
| ③ Shot execution | Video prompts and generated-media records | Recognized shot plan, relevant asset versions, and adjacent actual media state |
| ④ Review | Review findings, inspected evidence, scope, limitations, and unresolved defects | The submitted prompt, actual inputs, and result under review |
| ⑤ Post-production | Proposed or actual selected source intervals, edit points, transitions, sound tails, and net runtime | Available takes, director choices, reviews, and the actual edit when accessible |

Assign one writer to each authoritative file. Other roles read it and put suggestions in their own deliverable; they do not silently rewrite another role's source of truth. Role ① maintains the shared entry/index from the available role records. When one chat covers several roles, keep these ownership boundaries clear. If a writer changes, record the handoff rather than letting two chats overwrite the same file. This is a coordination rule, not a claim of an automatic file lock.

When recurring-character consistency needs a behavior/voice baseline, ① owns the director-recognized version and story-driven changes within its project plan or a linked character record. Keep it short and conditional; do not require a new file for every character. The [actor performance methods](actor-performance-and-facial-actions.md) govern its content. ③ records actual take states in the media record; ⑤ owns the observed states at selected edit boundaries; ④ records discrepancies. These observations do not silently rewrite the creative baseline. Pass the relevant baseline version and current shot/selected-state dependencies, not the full character history. No character profile or project state belongs in the Skill directory.

## Keep the entry short and retrieve selectively

The project entry should identify the film and current assignment, current recognized screenplay/shot-plan version, essential director locks, and links to the relevant role records. Distinguish the newest draft from the version currently recognized for production. Link to detail instead of duplicating asset tables, complete prompts, reviews, or the entire conversation in this entry.

At task start:

1. Confirm the specified project root, assigned role, and requested scope from the existing conversation or project entry.
2. Read the short entry, then only the current scene/shot, its actual asset records, and the adjacent continuity evidence needed for this task.
3. Record the versions on which the work depends. If a required source is missing, say what is unknown; do not reconstruct a supposedly approved fact from a filename or an old draft.

Before delivery or an authoritative update, compare those dependency versions with the current records. Check relevant content changes as well when a file was modified without updating its version label. If a relevant source changed, reconcile the affected work first. An unrelated change does not require rereading the whole film. Do not routinely load every old prompt, full screenplay, historical chat, audit report, and Skill reference into each turn.

This task-start and pre-delivery reading is what "automatic reading" means here: the active executor follows the instructions without asking the user to recopy known material. It does not imply background monitoring. Markdown supports persistence and traceability; it does not itself remove content from the model's context. Avoid writing a long file and then repeating it in full in chat.

## Evidence, versions, and decisions

For an important record, retain a compact version/date, owner, source dependencies, current conclusion, and evidence link or identifier. Use readable scene/shot names; keep tracking labels outside model-facing prompts. Preserve enough history to identify which prompt and asset versions produced a particular take, without copying all conversations into a log.

Keep these distinctions explicit where applicable:

- a proposed creative change versus the director's recognized decision;
- a planned asset versus an existing image, a saved Element, and a checked page binding;
- a prompt delivered versus actually used for a generation;
- media generated versus inspected, director-accepted, or selected in the edit;
- a planned end state versus the visible and audible state of the actual selected take;
- a planned usable interval versus the interval actually present in an inspected timeline or export.

These are not one universal status ladder. A take may be accepted with known defects, and a visually checked take may still have unreviewed sound. Record the director's acceptance separately from the reviewer's findings. A newer draft does not silently replace a recognized version. Do not infer acceptance from silence, the existence of a file, or the user's move to another topic. Do not ask again about a decision already clearly confirmed.

When a source changes, identify only the affected downstream records as needing review, with the changed dependency and reason. Preserve previously accepted media and its acceptance history. If applicability changed, say "accepted under the earlier version; continued use needs review" rather than deleting the take, erasing approval, or ordering a reshoot. Creative changes and final selection remain the director's choices.

## Platform image index, without local duplication

Film reference images remain on the platform. Record the exact saved name, displayed Element identifier when available, stable platform media/asset ID or page locator when exposed, image revision or replacement date, assigned purpose, and what was actually inspected. Do not invent an ID that the interface or tool has not returned. A temporary signed image URL alone is not a durable asset record.

Record whether the image was directly viewed, which angle/state it actually shows, and whether Element existence or page binding was checked, by whom or from what evidence, and when. A name can remain unchanged after replacement; the latest recognized actual image and director decision take precedence over obsolete details embedded in its name. Link the replacement to the earlier revision so old generations remain traceable.

Inspect relevant images directly through an available permitted platform preview or user-supplied view when needed. Do not save another local copy, automatically download an image as a fallback, or treat an index description as proof of unseen details. If direct inspection is unavailable, report the limitation and request the minimum missing view or authorized access. Existing reliable evidence may be reused while the asset and relevant conditions are unchanged; do not demand a new screenshot for every prompt.

## Scope from screenplay discussion to production

When the director requests whole-film story discussion, read the supplied screenplay and discuss the requested structure, characters, scene progression, and runtime. At scene/shot-planning stage, use the selected screenplay version and preserve relevant adjacent transitions. At production stage, prepare only the authorized scene or shot while reading the minimum global and adjacent constraints needed for continuity.

Do not use "current beat only" to refuse an explicitly requested screenplay discussion. Conversely, reading whole-film constraints does not authorize writing the next scene, preparing all its assets, or starting its production. "One image at a time" and similar current working choices remain binding. A recognized screenplay is a production baseline, not a ban on later director changes.

## Deliver once, then hand off briefly

For substantial image/video prompt work in a specified project, save one Markdown deliverable containing the complete English copy-ready prompt followed by its faithful full Chinese translation. Keep the exact Element names and required `@` prefixes in both. Put the compact Chinese control card, reference responsibilities, and material checks outside the copy-ready prompt. Reuse the current role's existing file organization rather than making a second dossier. In chat, give the useful conclusion, material change or unresolved issue, and a link to the file; do not duplicate the long bilingual text.

Small wording changes, brief advice, and short questions may stay in chat. A user request for a different delivery format takes precedence. If no project root is known, deliver a useful chat draft and resolve the path before persisting it.

At a role or chat handoff, provide only: the version and scope handed over; actual asset/media evidence; the current conclusion and director decisions; unresolved or unverified items; and the next concrete task. Link the authoritative records instead of repasting them. Review findings are recommendations, not automatic creative approval. Reading a handoff does not itself authorize platform generation, downloading, editing a timeline, or messaging/starting another chat.

For selected intervals, editing, sound, finishing, or delivery, use [post-production-guide.md](post-production-guide.md). The project entry points to those records; it does not duplicate their full contents.
