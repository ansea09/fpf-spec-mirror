---
chunk_kind: "child"
pattern_id: "A.19.CHR"
pattern_title: "CHRMechanismSuite: Shared Rules for Characterization and Selection"
section_id: "A.19.CHR:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CHR/A.19.CHR__004_forces.md"
commit_sha: "d5df418106507cff0972788834c0bf8825597de0"
heading_path:
  - "A.19.CHR — CHRMechanismSuite: Shared Rules for Characterization and Selection"
  - "A.19.CHR:3 — Forces"
line_start: 36865
line_end: 36873
dependencies:
  - "A.15.2"
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.21"
  - "A.6.1"
  - "A.6.7"
  - "A.6.RCD"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.19"
  - "G.0"
  - "G.10"
  - "G.5"
keywords:
  - "CG-Spec"
  - "CHR suite"
  - "CN-Spec"
  - "P2W seam"
  - "SlotFillingsPlanItem"
  - "admissibility conditions"
  - "applicable correspondence and crossing conditions"
  - "characterization core"
  - "crossing visibility"
  - "model-bound assurance penalties"
  - "no hidden scalarization"
  - "no hidden thresholds"
  - "planned baseline"
  - "set-return selection"
  - "suite obligations"
  - "tri-state guard decision"
---

### A.19.CHR:3 - Forces

* **No implicit crossings.** Identify the relations actually claimed or consumed: F.9 semantic correspondence, C.3.3 kind correspondence, or a separately governed plane relation. Use E.18/A.21 visibility and gate anchors when their actual crossing or gate is present. Context, entity, plane and edition changes alone create none of those relations.
* **CN‑Spec and CG‑Spec must remain the governing spec refs.** Mechanisms cite them; mechanisms do not duplicate them.
* **Strict separation of layers.** Universal CHR core vs discipline/method specializations vs generators vs packaging.
* **SlotKind invariance.** Specialisation chains must preserve SlotKind meaning and only refine ValueKind / strengthen guards/laws.
* **No silent scalarization / totalization.** CPM comparison results preserve the declared partial-order distinctions, and selection remains set-returning; any numeric summary is report‑only unless explicitly declared as a lawful comparator/policy.
* **P2W split.** Planned slot filling belongs to WorkPlanning; launch values belong to WorkEnactment.

