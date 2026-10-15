# Professional shot/reverse-shot and dialogue coverage grammar

Read this reference for dialogue, interrogation, confrontation, interview, reaction, or action/reaction coverage that needs matched angles, over-the-shoulder framing, clean singles, internal/external reverse angles, eyeline, screen direction, or axis continuity.

The terms are internal directing language. In the final model-facing prompt, expand them into visible framing, foreground, gaze, screen side, spatial anchors, and light direction. Never rely on `inner reverse`, `outer reverse`, or `reverse angle` alone.

## Distinguish the terms

- **Shot/reverse-shot:** an editing and coverage pattern that alternates two related viewing directions. It is not literally a front shot followed by a back shot.
- **Master/two-shot:** establishes both people, geography, distance, axis, height relationship, and the scene's dominant light/background anchors.
- **Over-the-shoulder (OTS):** one person is sharp while part of the partner's shoulder, head, or body remains soft in the foreground.
- **Dirty single:** primarily one person, with a small part of the partner intruding at the frame edge.
- **Clean single:** only the current person is visible; the partner remains offscreen.
- **External reverse angles / 外反拍:** camera positions stay outside the two-person relationship and look inward, commonly producing matched OTS or dirty singles that preserve the relationship.
- **Internal reverse angles / 内反拍:** camera positions move inside the two-person relationship and look outward at each person, commonly producing clean singles that isolate performance.
- **POV:** camera adopts what a character sees. An internal clean single can approach the partner's viewpoint but is not automatically a strict POV.
- **Reaction shot:** shows what an event or line does to a character; it may be silent and may interrupt normal dialogue coverage.

Chinese usage of 内反拍/外反拍 is not perfectly standardized internationally. Always use the mechanical definitions above and describe the final composition explicitly.

## Decide coverage by dramatic purpose

1. Establish the current relationship axis, dominant screen direction, character heights, and background/light anchors.
2. If audience must continuously read distance, hierarchy, obstruction, or who confronts whom, prefer a master or matched external OTS pair.
3. If a face, subtext, lie, realization, or emotional isolation is primary, prefer internal clean singles or a reaction close-up.
4. A scene may move from master/external OTS toward internal clean singles as emotional pressure increases, but this is a creative option, never a fixed formula.
5. Return to a wider master when new people enter, positions change materially, the axis changes, or the audience needs to understand the aftermath.

## Build and protect the axis

For a two-person scene, the relationship axis is the imaginary line through their eye contact. Keep paired camera positions on one side by default. This preserves opposite screen directions: if A is established screen-left looking screen-right, B remains screen-right looking screen-left.

For movement or combat, also identify the movement axis. When relationship and movement axes compete, choose the axis that currently carries the story action and re-establish the new one visibly.

For three or more people:

- establish the group geography first;
- treat each active exchange as a current pair or small subgroup with its own readable axis;
- when attention moves to a new pair, use a master, neutral-on-axis shot, visible camera move, or visible character move to establish the new screen relationship;
- do not let several invisible pair axes fight inside one prompt.

## Matched external OTS pair

For each direction, specify:

- whose shoulder/head occupies the foreground;
- which frame edge it occupies and how much of it remains visible;
- who is sharp and where that person's eyes sit;
- the sharp person's off-lens gaze target and screen direction;
- matching shot size, camera height, perspective, depth, background geography, and world light direction.

Example pattern for the first direction:

`Medium close-up over [A]'s right shoulder. Only a soft edge of A's shoulder and side of the head remains at the left edge without covering [B]'s eyes, mouth, or jaw. [B] is sharp, looking just off lens screen-left toward [A]. Preserve the established eye height, room geography, and key-light direction.`

Reverse it by independently describing the real opposite camera position:

`Matching medium close-up over [B]'s left shoulder. A soft edge of [B] remains at the right edge; [A] is sharp, looking just off lens screen-right toward [B]. Keep the same axis side, perspective, background anchors, and world light direction.`

Do not request a mirrored or flipped version of the first image. The room, wardrobe asymmetry, props, injuries, and light source must remain physically consistent.

## Matched internal clean-single pair

For each clean single, state:

- `no part of the partner is visible in frame`;
- the subject's exact off-lens gaze target and opposing screen direction;
- eye height relative to the partner;
- matched shot size and emotional distance;
- real background position and world light direction.

Example:

`Clean medium close-up of [A] from inside the conversational space; no part of [B] is visible. [A] looks just off lens screen-right toward [B], slightly downward because [B] is seated. Preserve the established background position and key-light direction.`

The reverse gives B the opposite eyeline. Do not let either person look directly into the camera unless deliberate direct address is story-locked.

## Continuity matching checklist

Match or deliberately motivate changes in:

- eye direction and eye height;
- character screen side and look room;
- shot size and face scale;
- camera height and angle to the relationship axis;
- perspective and depth of field;
- foreground shoulder size for OTS pairs;
- background landmarks and prop geography;
- world key-light direction and exposure logic;
- wardrobe, injury, hand, prop, and body position;
- speaking/listening state at the cut.

Matching does not require mechanically identical focal lengths. Describe the visible result—matching perspective, face scale, eye height, and depth—and let verified Studio controls own selectable lens/aperture settings.

## Eyeline rules

- Name the person or object being watched; screen-left/right alone is insufficient when the angle changes.
- In a matched pair, A and B normally look in opposite screen directions.
- Respect height: a standing person looks down toward a seated partner; the seated partner looks up.
- Use `just off lens toward [name]` for intimate singles without accidental camera address.
- For a glance to a prop or doorway, show the look, then the object/space or a reaction that confirms the target.
- Keep the listener's eyes alive; a frozen stare often reads as an unresponsive duplicate.

## Deliberate axis crossing

Cross the axis only through a legible device:

1. a continuous visible camera move that travels across the line;
2. a visible character move that creates a new relationship axis, followed by a re-establishing shot;
3. a neutral/on-axis shot, then a master or spatial anchor that establishes the new side;
4. an explicitly directed discontinuity used to create confusion, rupture, reversal, or threat.

A random close-up does not automatically repair an axis break. Never reinterpret an accidental left/right swap as creative intent.

## Performance progression through coverage

- Master/two-shot: behavior, distance, power balance, interruption, and who owns the space.
- External OTS/dirty single: relationship pressure plus readable face.
- Internal clean single: isolated face, subtext, reaction, and emotional shift.
- Close reaction insert: one decisive trigger and its physical consequence.
- Return master: changed positions, silence, damage, entrance, exit, or end-state geography.

Do not force all five into every scene. Choose the smallest coverage set that communicates the dramatic change.

## Action and confrontation coverage

For a fight, threat, or creature confrontation:

- establish attacker/defender positions and the dominant action axis;
- pair the attack direction with the defender's opposing eyeline and body orientation;
- separate the attack path, reaction/contact, and aftermath when exact physics matters;
- use a reaction insert only if it does not erase the contact geometry;
- re-establish positions after a fall, crossing, vehicle move, or new attacker changes the axis.

## When to split into separate generations

Prefer separate self-contained generations for master, A-side, B-side, or key reaction when any of these apply:

- more than two important camera positions, or both OTS and clean singles are required;
- exact dialogue, interruption, silence, lip sync, or reaction timing is pass/fail;
- facial identity/performance is the scene's value;
- three or more people change the attention center;
- strict background, prop, wound, screen-direction, or light continuity is required;
- camera changes occur during walking, contact, combat, or prop exchange;
- the selected generation route has not demonstrated reliable internal cuts.

For a simple two-person exchange with only two readable directions and a verified internal-cut route, one structured prompt may work. Across separate generations, do not automatically use the previous tail frame for a deliberate new angle; reuse approved Elements and write a new first-frame composition.

## Failure diagnosis

- Both people look the same way or into camera → eyeline/off-lens target failed.
- People swap screen sides → relationship axis or world topology failed.
- Reverse looks like a mirror image → the prompt asked for `opposite/mirror` instead of describing a real camera position.
- Foreground shoulder covers the face → edge occupancy and facial clearance were not specified.
- Background or light flips → world geography/light source was not independently preserved.
- Face duplicates or identity swaps → Element/reference authority conflict, not a need for more camera jargon.
- Emotional continuity resets after the cut → end state/start state and listener reaction were not handed off.

## Post-generation checks

Use at most three checks:

1. Opposing eyelines, heights, and screen sides form a believable exchange.
2. Foreground shoulder, background geography, props, wardrobe/injury, and light direction remain physically consistent rather than mirrored.
3. Speaker/listener performance continues through the cut; nobody looks into camera, duplicates, or changes identity.
