---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:10"
section_title: "Anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__012_anti-patterns-and-repairs.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:10 — Anti-patterns and repairs"
line_start: 74745
line_end: 74757
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
  - "U.EpistemeSlotRelation"
keywords:
  - "Description episteme"
  - "DescriptionContext"
  - "EntityOfConcern"
  - "specification use"
  - "testable"
  - "verifiable"
---

### E.10.D2:10 - Anti-patterns and repairs


| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Entity-description collapse** | "The method is the document"; "the architecture is the diagram"; "the role contains the checklist". | Name the EntityOfConcern, then name the Description episteme or publication relation separately. |
| **Spec by name** | Any detailed write-up is called `...Spec`. | Use `...Description` unless specification-use admission conditions are present. |
| **Publication as authority** | A card, dashboard, schema, generated view, or file is treated as permission, evidence, gate, assurance, decision, or work. | Apply the neighboring pattern that governs the exact claim being made; keep the publication relation separate. |
| **Carrier identity** | The file path or repository entry is treated as the episteme or EntityOfConcern. | Say the `U.PresentationCarrier` or carrier relation bears, encodes, transports, or renders the publication, and keep the episteme and EntityOfConcern separate. |
| **Context erasure** | A context-local Description episteme is read as a global definition. | Restore `BoundedContextRef` and `ViewpointRef`, or use F.9, A.6.3, or A.6.4 for cross-context relations. |
| **Status-state leakage** | Evidence, requirement, approval, or standard status becomes a role-state value. | Keep statuses over epistemes distinct from role-state relations and runtime state attestations. |
| **Episteme-role shortcut** | "The standard plays the compliance role"; "the evidence has the approval role"; "the source authorizes work". | Recover the typed relation: standard-use, evidence-use, status-use, source-use, assurance-use, gate-use, publication-use, or work-relevance relation. Use `U.RoleAssignment` only for work-facing holder-role claims. |

