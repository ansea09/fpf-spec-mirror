---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:10"
section_title: "Anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__012_anti-patterns-and-repairs.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:10 — Anti-patterns and repairs"
line_start: 76503
line_end: 76517
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.3.2"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "E.10"
  - "E.10.D1"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.11"
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
| **Entity-description collapse** | “The method is the document”; “the architecture is the diagram”; “the role contains the checklist.” | Recover the exact EntityOfConcern and C.2.1 description episteme; route every subject-side claim to its direct owner. |
| **Filled-card ontology** | A completed tuple, record, table, or schema is treated as what makes the episteme or relation exist. | Recover the governed object and obtaining relation first; treat the record as an episteme, form, carrier, or representation only when its own recognition conditions hold. |
| **Spec by name** | Any detailed, approved, or formal-looking write-up is called `...Spec`. | Use `...Description` until checkable claims, the describing-use qualification, and an exact harness or validation relation are all recoverable. |
| **Context as identity** | A project, viewpoint selection, or model-use setting is copied into episteme identity. | Keep the C.2.1 identity triple fixed; state only the exact use qualification or neighboring relation the receiver needs. |
| **Describing-use erasure** | A description is read as globally viewpoint-free, or a prior use's selected viewpoint is silently reused. | Name the current receiving use and its exact E.17.0 DescriptionContext; changing that selection does not by itself reidentify the episteme. |
| **View by appearance or construction** | A generated table, diagram, query result, or published face is called a `U.View`. | Apply E.17.0 conformance for view membership; use A.6.3 only for actual source-to-receiving construction and E.24.PUB/C.29 for form or representation uses. |
| **Publication as authority** | Availability, an approval mark, card, dashboard, or file is treated as permission, evidence, assurance, gate result, decision, or work. | Recover the exact publication occurrence, then apply the direct governor for the stronger claim. |
| **Carrier identity** | A file path, screen, sheet, or repository entry is treated as the episteme or EntityOfConcern. | Identify the exact carrier and bearing relation while keeping form, publication occurrence, episteme, and EntityOfConcern separate. |
| **Status-state leakage** | Evidence, requirement, approval, or standard status becomes a role-state or runtime value. | Keep status claims on their exact epistemic or deontic subject; use the direct state or attestation pattern for system-side facts. |
| **Episteme-role shortcut** | “The standard plays the compliance role”; “the evidence has the approval role”; “the source authorizes work.” | Recover the exact standard-use, evidence-use, source-use, assurance-use, gate-use, or publication-use relation. For a claimed Work use, name the exact premise, governed reference, decision-use relation, or A.6.1 operation-argument binding and its actual participants; if no direct governor supplies the needed predicate and participants, return the exact `missing-governor` result. Reserve `U.RoleAssignment` for work-facing holder-role claims. |

