---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__002_intent.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:1 — Intent"
line_start: 45229
line_end: 45243
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:1 - Intent

*Keep **Working-Model** relations readable and, when this profile is elected, connect each covered assertion to inspectable grounding and a declared validation posture.*

**What you get (manager/engineer view).**
 The same relations you already know (e.g., **ComponentOf**) remain the **public relation vocabulary**.

**What changes when the profile is elected (auditor/ontologist view).**
* Each covered published edge carries two additional commitments:

  1. **`tv:groundedBy`** → points to the support required by the relation's branch: the applicable `sum` or `slice` trace for structural parthood, one current `C.13 set` trace for the collection's belongs-to relation, or an admissible argument or evidence object for another permitted claim.
  2. **`validationMode ∈ {axiomatic, inferential, postulate}`** → declares how the author justifies the assertion.

The pattern that defines the relation still decides when it obtains. CT2R-LOG records the branch-specific support link and declared assurance posture. An optional `tv:AliasOf` declaration resolves a local relation label to its accepted Tech designation under E.10 and Lang-CHR.

