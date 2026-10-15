# Higgsfield platform access protocol

Use this reference only when current platform capabilities, exact controls, costs, versions, or refresh status matter. Ordinary prompt writing should use the dated local snapshot and stay offline.

## Evidence order

When sources disagree, use this order:

1. the user's current visible Cinema Studio page or Appshot;
2. a live read-only CLI/MCP schema for the exact workflow or model;
3. the version-specific Help Center page;
4. the newest version-specific official prompt guide or Academy course;
5. the official GitHub Skills repository;
6. official case-study .skill attachments;
7. broad marketing copy.

Label the evidence honestly: current visible, live schema, dated official document, or inference. Never turn a lower-level example into a verified current button.

## Hosted MCP

- Endpoint: https://mcp.higgsfield.ai/mcp
- Transport: Streamable HTTP.
- Authentication: OAuth bearer through the client. Never store tokens, passwords, cookies, client secrets, or authorization headers in this Skill.
- Let the MCP client negotiate the protocol version. Do not hardcode it.
- Current Codex tool prefix may appear as mcp__codex_apps__higgsfield_*. Discover actual tool names instead of inventing them.

Allowed by this workflow:

- list, search, get, describe, recommend, schema and capability reads; cost-estimate calls only after their current schema confirms no upload, media import, library mutation, job or credit use. A price-only request must omit media that a tool would otherwise import.
- read-only Element or history inspection only when needed and already authorized by the user's scope.

Forbidden by default:

- generate, create, submit, upload, edit, delete, train, publish, workspace switching, authentication changes, billing changes, or any credit-consuming call.

In the maintainer's historical read-only check on 2026-10-07, the hosted MCP video catalog contains 55 entries, including exact `cinematic_studio_video_3_5` and `cinematic_studio_video_4_0` IDs. Read-only `models_get` for both IDs returns the callable Studio parameters. The 3.5 schema includes `multi_shots`, `multi_shot_mode`, and `multi_prompt` (maximum six shot prompts). The 4.0 schema includes 4–30 seconds, 480p/720p/1080p, four generation modes, audio, bitrate, and Director Panel ID fields for genre, era, pacing, camera, lighting, and color. These API fields do not enumerate all human-readable web choices or prove that a field is visible on the director's page. The catalog also has older generic Cinema IDs; never map those to 3.5 or 4.0 by guessing. Do not infer an underlying engine from overlapping fields.

## Inspect actual images without saving a second copy

Use current tool descriptions to find read-only Element/list/get or specific-media inspection. An Element result may provide only metadata and media URLs, not pixels. Follow an authorized preview/view route and actually inspect the relevant image before claiming it was seen. A browser image view may be used when the connector does not expose pixels; no page editing, asset binding or upload is implied.

Do not automatically download/save image files to the project or Skill as a fallback. If a direct view is unavailable or insufficient for a face/detail check, state what cannot be checked and request the minimum view or authorized alternative. Browser/tool internals may cache images; no zero-cache claim is justified. Record stable asset/media identifiers, image version and inspection scope in the film's asset index, not this Skill. Existence of an Element does not prove the current page selection, prompt text, slot availability or absence of stale references.

## Local CLI

Resolve `higgsfield` from the reader's environment only if it is already installed and the task calls for CLI use. This package does not install or authenticate it. A missing CLI does not block ordinary film advice or an available authorized read-only browser/MCP route.

The maintained historical CLI schema baseline is 2026-09-13. Updating a binary does not refresh schema evidence. Model and workflow catalogs are separate namespaces; discover the exact requested ID instead of assuming a catalog count or copying another machine's installation state.

Minimum read-only commands:

    higgsfield --version
    higgsfield workflow list --json
    higgsfield workflow get <exact-id-from-list> --json
    higgsfield model get <exact-job-type> --json
    higgsfield generate cost <exact-job-type> --prompt test --duration=<seconds> --json

Use model list/get for an underlying model question. Use workflow list/get for a Studio workflow only after the exact current ID has been discovered.

Both exact workflow schemas were read successfully on 2026-09-13. The 3.5 schema exposes genre, color grading, camera MoveSet style, lighting, multi-shot fields, prompt/audio/media fields, aspect ratio, resolution, and duration. The 4.0 schema exposes four generation modes, bitrate, extension direction, Director Panel ID/object fields, prompt/audio/media fields, aspect ratio, resolution, and duration. Exact `model get` calls for these job types additionally return validation rules even though the unfiltered model list omits both branded Studio entries. The schemas prove callable fields, not the complete human-readable website menus.

For these two Studio job types, the 2026-09-13 CLI cost validation used the direct job type, not `generate cost workflow ...`; the latter returned Unknown workflow. `generate cost` is documented as an estimate that creates no job. It confirmed 4.0 accepts 4–30 seconds and rejects values outside that range. For 3.5 it confirmed a four-second minimum but did not reveal a trustworthy maximum; it accepted 16 seconds even though the public/web route is up to 15. Do not recommend a 3.5 duration above the visible page limit without later non-credit evidence.

Neither schema returns an underlying engine or model identity. Shared mode or media-field names are not proof that Cinema Studio 4.0 equals Seedance 2.5. Never reverse-engineer an ID into a web label or claim the CLI mirrors the full page.

The exact 4.0 job schema and the independent `seedance_2_5` model schema each confirm the same reference-mode rules: t2v accepts no reference media; omni-reference requires at least one item; all reference media together are capped at 50; images including start/end are capped at 30; video edit requires exactly one video; video extension requires at least one video plus forward/backward extension mode; start/end images are omni-reference-only. This similarity still does not establish their engine relationship.

The 3.5 job schema separately caps all reference media at 15 and makes `style_prompt` mutually exclusive with inline `camera_style`, `light_scheme`, or `color_grading`. The 4.0 job schema also requires custom light data for custom lighting, a noncustom preset ID for preset/user lighting, and forbids mixing custom light data with preset/user IDs.

## Fallback route

1. Use cached cinematography guidance for ordinary shots.
2. For current Studio 3.5/4.0 or other model capability, use MCP read-only `models_list`/`models_get` with the exact ID when available. CLI `workflow get`/`model get` is a second exact-schema route if the MCP result is incomplete or unavailable.
3. For exact button names, palettes, movements, emotions, ordering, or account-specific availability, use the user's current screenshot/Appshot as final truth; a schema field alone is not a button.
4. If none can verify a value, say 当前无法核验 and omit the exact click instruction.

## Fifteen-day refresh

At invocation, run:

    python3 scripts/check_platform_freshness.py

This reads platform-state.json only. It does not use the network or change a file. The public snapshot is intentionally marked historical_reference, so it reports DUE until relevant evidence is independently checked. DUE does not mean the Skill is broken and does not block offline creative advice. A reader's current project check belongs in that project; do not change the shared Skill during film work.

When any relevant source reaches 15 days:

- a simple creative request still gets an immediate answer, followed by one concise refresh reminder;
- an exact current-control or availability request pauses for refresh authorization;
- a declined refresh uses the dated snapshot and labels it as cached;
- authorization covers read-only checking only; an explicit request to verify current facts already supplies that read scope. Do not repeat a permission question already resolved in the session.

After authorization, check the smallest relevant sources. A full refresh may compare CLI version and workflow schemas, MCP inventory/model discovery, official version pages, GitHub Skills version, and the current UI supplied by the user. If one source fails, mark the refresh partial. Show material differences before changing this Skill or upgrading the CLI.

The Skill cannot wake itself while unused. The fifteen-day mechanism is an invocation-time reminder, not a background scheduler. A recurring automation would require a separate user request.
