---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:8"
section_title: "Anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__009_anti-patterns-and-repairs.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:8 — Anti-patterns and repairs"
line_start: 60053
line_end: 60063
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.12"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "Description episteme"
  - "DescriptionContext"
  - "EntityOfConcern"
  - "specification use"
  - "testable"
  - "verifiable"
---

### E.10.D2:8 - Anti-patterns and repairs

| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Entity-description collapse** | "The method is the document"; "the architecture is the diagram"; "the role contains the checklist". | Name the EntityOfConcern, then name the Description episteme or publication relation separately. |
| **Spec by name** | Any detailed write-up is called `...Spec`. | Use `...Description` unless specification-use admission conditions are present. |
| **Publication as authority** | A card, dashboard, schema, generated view, or file is treated as permission, evidence, gate, assurance, decision, or work. | Send that live claim to the exact neighboring pattern; keep the publication relation separate. |
| **Carrier identity** | The file path or repository entry is treated as the episteme or EntityOfConcern. | Say the carrier encodes or renders the episteme. |
| **Context erasure** | A context-local Description episteme is read as a global definition. | Restore `BoundedContextRef` and `ViewpointRef`, or use F.9/A.6.3/A.6.4 for cross-context relations. |
| **Status-state leakage** | Evidence, requirement, approval, or standard status becomes a role-state node. | Keep statuses over epistemes distinct from state graphs and runtime state attestations. |

