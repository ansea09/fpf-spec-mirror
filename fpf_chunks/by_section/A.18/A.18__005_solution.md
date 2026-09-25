---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__005_solution.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.18 — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:4 — Solution"
line_start: 31582
line_end: 31620
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CN"
  - "B.3"
  - "C.16"
  - "G.0"
keywords:
  - "CSLC"
  - "Characteristic"
  - "Coordinate"
  - "Level"
  - "Scale"
  - "lawful comparability"
  - "measurement interpretability"
  - "no illegal averaging"
  - "one-characteristic-one-scale rule"
  - "ordinal vs cardinal scale"
  - "scale order"
  - "use-dependent preference"
---

### A.18:4 - Solution

**Bind each measurement template to one Characteristic and one Scale.** A Coordinate is one value on that Scale; a named Level is optional when the Scale supplies discrete categories or tiers. A performed measurement may attribute one value or a set of values, with uncertainty and measurement conditions under C.16. CSLC types those values; it does not require every observation to determine one exact Coordinate.

> **Exactly one Characteristic + exactly one Scale; each reported Coordinate belongs to that Scale, with an optional named Level.**

Concretely, the parts of this clause are defined as follows:

-   **Characteristic:** the aspect or feature being measured (the “CG‑frame” along which comparison is made). It answers “_What are we measuring?_” – e.g. _Distance, Temperature, Quality, Reliability_.

-   **Scale:** the organized set of possible values that the Characteristic can take, including the type of scale (_nominal_, _ordinal_, _interval_, or _ratio_), the measurement **Unit** (if applicable), and any bounds or structure. The Scale defines “_How are values represented, and which operations does the Scale permit?_” – e.g. “meters on a linear scale from 0 up to 1000” or “ratings 1 through 5 with ordering only”.

- **Coordinate:** one value in the declared Scale's value domain, numeric or categorical. A measurement result may attribute one Coordinate or a set of admissible Coordinates to its subject; C.16 supplies the model, uncertainty and conditions for that attribution. Examples of individual Coordinates are 7.4 on a meter Scale or Expert on the declared expertise Scale.

-   **Level (optional):** a named **tier or category** on the scale, used only if the scale is tiered or discretized. For example, an ordinal scale might have Levels _Low, Medium, High_. A Level is essentially a human-friendly label for certain coordinates or ranges. On purely continuous scales, **Level** is not used.

This CSLC structure makes the measured Characteristic and the Scale of each value recoverable, with an optional Level label. Interpreting an actual measurement additionally uses its C.16 model, conditions and uncertainty. Notably, this pattern _forbids bundling multiple characteristics into one metric_ – each metric template is one-characteristic-per-template to keep semantics crisp. If something needs to assess multiple factors, it should be modeled as multiple CSLC metrics or an explicit composite over several CSLC metrics (see §8 below). This one-aspect-one-scale rule makes the value meaning recoverable; comparison additionally requires compatible measurement conditions.

Finally, the solution ensures **tier optionality**: If a domain uses named Levels, we include them; if not, we don’t force it. For example, one can have a _Bug Severity_ Characteristic with Levels {Minor, Major, Critical} on an ordinal scale, whereas a _Length_ Characteristic would have a continuous scale (no predefined levels, just units). Both fit the pattern.

#### A.18:4.1 - Characteristic-space support must stay declared

- When one front, archive, shortlist, or derived tradition view is discussed in one space, declare the object kind and the relevant characteristic space explicitly.
- Use one `SpaceRef` only when the text truly needs to recover which space or typed feature family is carrying the comparison.
- One declared space does not imply that every neighboring line must use the same space.
- Different declared spaces may coexist for the same family when they answer different comparison questions, but the active one must stay recoverable.
- If one atlas-like reading uses several declared spaces over the same palette, front, archive, or shortlist family, say which `SpaceRef` is active in the current reading rather than letting the atlas label hide that choice.
- If one outcome-side declared space/ref is materially different from one representation-side or search-side declared space/ref, keep that difference explicit rather than calling both simply `space`.
- `OutcomeMapRef` is warranted only when the text needs one declared map from the current set result into one outcome-side or effect-side declared space/ref.
- When `OutcomeMapRef` is cited for one atlas-like or cross-scale reading, keep the source set result and the projected outcome-side declared space/ref visible together so the map stays support for the view rather than a replacement default.

#### A.18:4.2 - Scale order, preference and calculation

For a magnitude comparison, interpret values under the Characteristic and Scale, including the meaning of their order and units. For a judgement about which value is better, state the preference for that use: higher, lower, a target or range, or another declared rule. A nominal Scale supplies labels without an intrinsic order; a receiving use can still express a preference among them. A descriptive measurement needs no preferred direction.

A mathematical relation can combine quantities into another quantity, as a measurement model does in C.16. Identify that relation, its conditions and the Scale of the resulting quantity. A unit conversion expresses the same quantity on another compatible Scale. A ScoringMethod instead supplies a Score for a declared evaluation and follows A.17-R7's preference rule. For example, multiplying resistance by current gives voltage; ranking designs by cost and reliability requires a choice of preference.

For evaluative comparison or combination across different CSLC templates, the ScoringMethod must declare a bounded output range for its Score.

