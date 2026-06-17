---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__013_relations.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:12 — Relations"
line_start: 15777
line_end: 15794
dependencies:
  - "A.1"
  - "A.6.0"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "B.5"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.17.0"
  - "E.8"
  - "U.EpistemeSlotRelation"
  - "U.MultiViewDescribing"
  - "U.Signature"
keywords:
  - "argument position"
  - "pass-by-reference"
  - "pass-by-value"
  - "reference"
  - "signature"
  - "slot"
  - "substitution"
  - "value"
---

### A.6.5:12 - Relations

`A.6.0` governs `U.Signature`; `A.6.5` supplies SlotSpec discipline for n-ary vocabulary items inside signatures.

`A.6.P` governs qualified relation precision restoration; `A.6.5` supplies the slot discipline consumed by relation-restoration patterns.

`E.24` governs ontic introduction. `A.6.5` is one reusable discipline used by ontic introductions, but it does not create a new ontic every time a slot label appears.

`C.2.1` is the mature precedent for slot relation discipline in epistemes. `A.6.5` keeps its `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, and `ReferenceSchemeSlot` usable across morphisms and publication patterns.

`A.2`, `A.2.1`, `A.2.5`, `A.2.7`, and `A.15` govern role values, role assignments, role-state checks, role relation structure, and role-method-work alignment. `A.6.5` only expresses the SlotSpecs of relations that include role values or role assignments.

`A.10`, `B.3`, `G.6`, `C.28`, and `F.10` govern evidence-use, assurance, causal-use, provenance, and status-use relations. Old evidence-role and status-role source wording is governed through typed evidence-use, assurance, causal-use, provenance, or status-use relations, not through work-role assignment.

`A.6.M`, `A.6.F`, `E.18`, `C.30.TFS-REL`, and architecture patterns govern interface, port, functional, and transformation-flow cases. `A.6.5` applies only after the governing EntityOfConcern has been recovered.

`E.10`, `E.10.ARCH`, `F.18`, and `A.6.RSIR` govern wording-use triage and naming. They require each relation, signature, interface, role, slot, capability, method, function, concern, or interest word to be resolved under its direct governing pattern, using `A.6.5` when relation-position discipline is the current issue.

