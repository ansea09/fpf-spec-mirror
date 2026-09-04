---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "SystemRoleKindDescription — Describing an Exact System-Role Kind"
section_id: "F.4:8"
section_title: "Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__010_anti-patterns-and-repairs.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "F.4 — SystemRoleKindDescription — Describing an Exact System-Role Kind"
  - "F.4:8 — Anti-Patterns and Repairs"
line_start: 94136
line_end: 94150
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "C.3.2"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.5"
  - "F.9"
keywords:
  - "classification criterion"
  - "description episteme"
  - "effective scheme"
  - "local kind"
  - "non-inference boundary"
  - "system-role-kind description"
---

### F.4:8 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Description as kind admission | A card is treated as if it constituted the local kind. | Establish the kind under A.2 with C.3; keep F.4 for its description. |
| Description as classification | “The card lists Alice, so Alice is a reviewer.” | Evaluate the exact candidate under the current `KindSignature`. |
| Description as assignment | “The inspector is assigned” appears without an exact holder, kind, direct species, and assignment occurrence. | Use A.2.1; keep F.4 for description of the kind. |
| Description as capability proof | “ReviewerSystemRole can verify formal models.” | Put capability under A.2.2; F.4 may cite the requirement. |
| Description as Method | The description contains a procedure. | Move the procedure to Method or MethodDescription patterns. |
| Description as Work evidence | A card is cited as proof that review occurred. | Recover the exact `U.Work` occurrence and evidence relation. |
| Episteme as system-role holder | A report, standard, dataset, theorem, dashboard, or publication is said to hold a role. | Recover the exact evidence, source, standard, requirement, publication, status, or assurance relation. |
| Status-template fusion | A status, permission, or evidence standing becomes another kind-description branch. | Use the direct status, policy, permission, or evidence relation. |
| Relation position as system role | “The subject role in this relation …” | Recover participant meaning, `SlotKind`, `ValueKind`, and `RefKind` under A.6.RSIR and A.6.5. |
| Bridge by label | Shared spelling, or a changed practice or source, is treated as proof of kind sameness or difference. | Compare the exact C.3 definitions first. Reuse one kind when its candidate domain and operative distinction continue; identify two only when those distinctions differ. Use C.3.3 only when an actual relation between two exact kinds obtains. Use F.9 only for an actual relation between distinct F.17 local-sense cells. |

