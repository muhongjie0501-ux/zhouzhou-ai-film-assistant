# Cinema Studio 4.0 dated baseline

Maintainer historical UI observation: 2026-10-06 from a live account-page check; this does not guarantee every account has identical dynamic presets. Exact Cinema Studio 4.0 MCP `models_get` rechecked on 2026-10-07. The earlier CLI workflow list/get baseline is 2026-09-13 unless `platform-state.json` records a newer successful check. Movement prompt interaction was separately observed in the maintainer's account on 2026-09-28; it is not verification of the reader's current page.

Historically verified callable workflow ID: `cinematic_studio_video_4_0`; display name: Cinema Studio 4.0.

The 2026-10-06 page showed a 4–30-second slider, a References counter up to 50, audio, and Director Panel controls. The official version-specific [Help Center](https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-cinema-studio) explicitly says Cinema Studio 4.0 runs on Seedance 2.5. Report that as an official documentation attribution, not as an independently exposed engine field: neither the CLI workflow schema nor the exact MCP Studio model schema returns its underlying engine identity. Keep Studio web controls separate from Seedance model parameters.

## Best fit

Choose 4.0 for:

- a deliberate 16–30 second one-take or restrained performance;
- dialogue that needs room for pauses and reactions;
- a simple sustained action or gradual reveal;
- a small legible sequence of internal cuts;
- a control or mode visibly present on the current 4.0 page or verified by its exact workflow schema.

It may also be right for a short shot when a 4.0-only capability is decisive. It is not a cure for too many independent bodies, impacts, injuries, camera changes, or dialogue turns.

## Dated visible click hierarchy

1. References.
2. Film setup:
   - Genre.
   - Era.
   - Tempo.
3. Camera:
   - Setup: Camera, Lens, Aperture.
   - Movement: separate tab; the 2026-10-06 observed library is listed below as a dated snapshot, not a permanent menu.
4. Color palette.
5. Lighting.
6. Prompt and visible bottom bar: Studio, resolution, aspect ratio, duration, audio, output count.

The 2026-10-06 page showed a duration slider with 4–30-second bounds. The 2026-10-07 MCP schema independently states 4–30 seconds with default 5. Do not mistake the five-second default for a limit or invent a list of discrete duration buttons; select an exact slider value that the current page accepts.

An Emotion Wheel is documented by official 4.0 materials, but its exact placement and availability were not visible in the historical captures. Include it as an exact click only when the current page exposes it.

## Control names observed in the dated check

Film setup Genre visibly includes:

- General, Action, Epic, Drama, Comedy, Horror, Noir.

Film setup Era observed on 2026-10-06: Auto, 1960s, 1980s, 1990s, 2000s, 2020s. Tempo observed: Auto, Single shot, Calm, Dynamic, Chaotic. These are account-page observations, not a promise that the menu can never change. A tempo selection shapes editing rhythm, not the physical camera path.

Camera Setup:

- Camera: Auto, Modern, 35mm Film, 8mm Film, DV Camcorder.
- Lens: Auto, Clean Sharp, Anamorphic, Vintage Anamorphic, Warm Vintage, Halation Vintage.
- Aperture: Auto, f/1.4 Wide Open, f/4 Moderate, f/11 Deep Focus.

Lighting:

- New lighting preset, Auto, Silhouette, Practicals, Window, Overhead fall, Contre jour, Soft cross.

Color palette:

- Auto plus a dynamic named library. The historical capture showed names such as Static Noon, Industrial Fog, Field Post, Highway Standoff, and others.
- Do not hardcode those examples as universal choices. When the supplied references already establish the look, Auto is a valid precision choice. Select a named palette only for an intentional visible grade and only when that name is present.

Camera Movement:

- The 2026-10-06 account-page check observed these 33 names in the Movement tab (not an evergreen catalog): Snorricam, Robot arm, Tilt up, Rack focus, Tilt down, POV, Pan left, Crane up, Pan right, Crane down, Side tracking, Pedestal up, Pedestal down, Handheld, Tracking, Drone orbit, Dolly zoom, Aerial pullback, Static shot, Bullet time, Whip pan, Slow zoom in, Arc left, Slow zoom out, Arc right, Truck right, Dolly in, Truck left, Dolly out, Slider right, Crush zoom, Slider left, Helicopter shot. The MCP/CLI schema does not enumerate these human-readable choices.
- Choose zero, one, or several presets by the dramatic need and the clarity of the camera path. Multiple compatible movements can express an ordered move, but do not stack them merely because the UI allows it. Give an exact name only when verified on the current page; otherwise describe the movement in ordinary camera language and mark the preset choice unverified.
- When recommending a verified preset, place its exact `#English preset name` at the relevant beat inside the complete paste-ready English video prompt and keep that token unchanged in the Chinese translation. In the maintainer's dated test, pasted `#` strings remained plain text until each popup candidate was selected. The reader performs any such binding manually on the current page. Never describe the pasted text alone as an activated preset or claim automatic bulk binding.
- Keep the Studio control card's Camera → Movement row consistent with the prompt tags and their order. Do not give contradictory camera directions in prose. This convention does not apply automatically to image prompts, Cinema Studio 3.5, or another workflow.

## Cinematography effects

- Modern + Clean Sharp: contemporary precision; useful for equipment and readable blocking but may feel clinical.
- 35mm Film + moderate aperture: organic cinematic texture with practical focus tolerance.
- f/1.4: isolated face and intimate emotion; high focus risk for groups and fast action.
- f/4: balanced moving-subject coverage.
- f/11: deep geography and multiple planes; can demand more light and feel less intimate.
- Auto palette/light: lets approved references and prompt carry the visual baseline.
- Contre jour or Silhouette: strong outline and threat, weak facial information.
- Window, Practicals, or Soft cross: motivated, readable faces when their source makes sense in the location.
- Chaotic movement/tempo, when visible: intentional disorientation; compounds action continuity risk.

For a realistic multi-person action shot, favor readable geography, moderate depth, and one coherent camera path. Do not stack aggressive camera motion, extreme shallow focus, stylized backlight, and exact tactical blocking.

## Historical exact Studio schema fields and UI limits

The 2026-10-07 exact MCP Studio model schema reconfirmed the callable fields below; the reference-count and cross-field rules are separately dated 2026-09-13 CLI findings, not fresh MCP validations:

- `mode`: t2v, omni_reference, video_edit, video_extension;
- `extension_mode`: backward or forward;
- `bitrate_mode`: standard or high;
- `aspect_ratio`, integer `duration`, 480p/720p/1080p, and required prompt;
- `generate_audio`, start/end images, and image/video/audio references;
- `genre_id`, `era_id`, `pacing_id`;
- `camera_model_id`, `camera_lens_id`, `camera_aperture_id`;
- `color_palette`, `light`, `light_custom`, and `light_id`.
- The earlier CLI schema says t2v accepts no media, omni-reference requires media, total media is capped at 50, and images including start/end at 30. The current MCP response lists media roles but does not expose these counts or validation rules.
- The earlier CLI schema says video edit requires exactly one video, video extension requires at least one video plus forward/backward extension mode, and start/end images are omni-reference-only; the current MCP response does not validate those combinations.
- The earlier CLI schema says custom lighting requires `light_custom`, preset/user lighting requires a noncustom `light_id`, and custom data and preset/user IDs must not be mixed; the current MCP response exposes the fields but not these cross-field checks.

These are API fields and rules. They do not prove that every field is a visible website control, and opaque IDs do not reveal the current human-readable menu values. The current MCP schema directly states 4–30 seconds. Neither schema exposes the underlying engine/model identity; the official Help Center makes the separate Seedance 2.5 attribution above.

The current hosted MCP separately exposes `seedance_2_5` with mode, extension direction, duration, resolution, bitrate, audio, and media-reference roles. Those fields belong to that model and must not be relabeled as visible Cinema Studio 4.0 controls.

The current MCP model catalog directly exposes exact `cinematic_studio_video_4_0` and `cinematic_studio_video_3_5` entries, as well as older generic Cinema IDs. Never guess that `cinematic_studio_video_v2` means 4.0. Use an exact-ID MCP or CLI schema for callable fields and the current page for exact Director Panel labels.

## Structured internal cuts

Use time ranges only for a small readable sequence. Each internal shot receives:

- one framing and camera idea;
- one dominant subject action or speaking turn;
- a clear cause/effect;
- a clean end state.

Do not attach artificial start/end frames between internal cuts in one generation. Across separate generations, use the previous tail frame only for real continuation or match-on-action.
