---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 16077
line_end: 16087
dependencies:
  - "A.1"
  - "A.2.1"
  - "A.6.0"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.17.0"
  - "E.8"
  - "F.6"
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

### A.6.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
|---|---|---|
| `RoleSlot` as a generic relation position | It can hide whether `role` means `U.Role`, argument position, provider relation, evidence use, or ordinary prose. | Name the actual SlotKind, such as `RoleValueSlot`, `RoleHolderSlot`, or a domain slot, and name the ValueKind separately. |
| Source label `EvidenceRole` for an episteme | It gives an episteme a work-facing role assignment it does not have. | Use an evidence-use relation with `EvidenceEpistemeSlot`, `EvidenceTargetClaimSlot`, and related slots. |
| "The API role is provider" | API, provider, role, promise, service, and interface may be different values. | Recover API description, provider role assignment, service promise relation, or interface specification under direct patterns. |
| `EntityOfConcernRef` used as a value kind | A reference field is treated as the described object. | Split `EntityOfConcernSlot`, ValueKind, and `entityOfConcernRef` or equivalent RefKind field. |
| "Late binding" without the affected link | The reader cannot tell whether name binding, slot filling, resolution, or method dispatch is late. | Rewrite as late name binding, late slot filling, lazy resolution, or dynamic dispatch with the governing relation named. |
| `interface` repaired by deleting the word | The useful engineering recognition cue is lost. | Keep interface as ordinary cue, then recover the governing EntityOfConcern and its SlotSpecs. |

