---
chunk_kind: "child"
pattern_id: "A.4"
pattern_title: "Compare a System's Intended Design with Its Operating Conditions"
section_id: "A.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.4/A.4__006_archetypal-grounding.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.4 — Compare a System's Intended Design with Its Operating Conditions"
  - "A.4:5 — Archetypal Grounding"
line_start: 10988
line_end: 11011
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.3.4"
  - "B.4"
  - "C.2.1"
  - "C.27"
keywords:
  - "comparison criterion"
  - "conformance"
  - "design account"
  - "discrepancy"
  - "missing basis"
  - "operating facts"
---

### A.4:5 - Archetypal Grounding

#### A.4:5.1 - One continuing pump, two selected design accounts

In this constructed case, `Pump37` operates under condition set C. A justified domain comparison uses exact flow values in L/min under those matched conditions. The available observation is 105. Account D1 requires at least 100; account D2 requires at least 110.

| Selected basis | Comparison | Bounded result |
|---|---|---|
| D1, C, minimum 100 L/min | 105 ≥ 100 | This flow requirement is met. |
| D2, C, minimum 110 L/min | 105 < 110 | Flow misses this requirement by 5 L/min. |
| D2 under C, observation under C′, with no justified translation | The comparison premise is missing. | Unresolved comparison, not a failed pump or a false design. |

Selecting D2 changes the comparison basis; it does not physically change Pump37. Editing D1 into D2 changes the account's claim content. Its historical edition relation, if claimed, must independently obtain. The discrepancy against D2 may justify a later response question, but supplies neither change authority nor a requirement to revise the design.

#### A.4:5.2 - Distinguish the actual event and its next use

| Working situation | Correct exit |
|---|---|
| A pump circulates coolant while its CAD account is edited. | Use the continuing pump and the selected CAD account claim in the comparison. Operating Work and editing Work concern different subjects; the edit establishes no physical pump change. |
| An author cites an unchanged theorem. | Use the direct episteme-use rule. The theorem executes no OperationalMethod; any reasoning Work has its own performer and Method. |
| An unused pump weathers. | A.3.4 can qualify the actual material change without invented Work. If later design conformance matters, compare the resulting condition with the selected criterion. |
| A sensor measurement produces a new observation record. | Use the observation as warranted input to the comparison. Measurement and result do not by themselves establish target change. |
| A pump's internal control System performs maintenance. | A.12 distinguishes acting and changed participants. The System's identity rule can preserve the same pump; compare its relevant resulting facts if the intended use requires it. |

