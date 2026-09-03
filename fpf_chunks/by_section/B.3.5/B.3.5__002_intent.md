---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__002_intent.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:1 — Intent"
line_start: 40081
line_end: 40095
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:1 - Intent

*Provide a single, human-facing family of **Working-Model** relations as the **public relation layer**, with explicit hooks for (G) grounding and (R) reliability, without exposing constructor jargon or overloading day-to-day authors.*

**What you get (manager/engineer view).**
 The same relations you already know (e.g., **ComponentOf**) remain the **public relation vocabulary**.

**What changes when the profile is elected (auditor/ontologist view).**
* Each covered published edge carries two additional commitments:

  1. **`tv:groundedBy`** → points to the support required by the relation's branch: the applicable `sum` or `slice` trace for structural parthood, one current `C.13 set` trace for the collection's belongs-to relation, or an admissible argument or evidence object for another permitted claim.
  2. **`validationMode ∈ {axiomatic, inferential, postulate}`** → declares how the author justifies the assertion.

The pattern that defines the relation still decides when it obtains. CT2R-LOG records the public alias, the branch-specific support link, and the declared assurance posture; Lang-CHR supplies the labels.

