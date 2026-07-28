---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:8"
section_title: "Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__010_anti-patterns-and-repairs.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:8 — Anti-Patterns and Repairs"
line_start: 88386
line_end: 88398
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
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.3"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:8 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Role-description as assignment | A card says "the inspector is assigned" without holder, context, and window. | Use `A.2.1`; keep F.4 for description of the role value. |
| Role-description as capability proof | "ReviewerRole can verify formal models." | Put capability under `A.2.2`; F.4 may reference the requirement. |
| Role-description as method | A role description contains a procedure. | Move the procedure to method or method-description patterns. |
| Role-description as work evidence | A role card is cited as proof that review occurred. | Use `U.Work` and evidence-use patterns. |
| Episteme as role holder | A report, standard, dataset, theorem, dashboard, or publication is said to hold a role. | Recover evidence-use, source-use, standard-use, requirement-use, publication-use, status-use, or assurance-use relation. |
| Status-template fusion | A status, permission, or evidence standing is made a second kind of role description. | Use direct status-use, policy, or evidence patterns. |
| Slot position as role | "The subject role in this relation..." | Use `A.6.5` SlotKind and ValueKind wording. |
| Bridge by label | Same role-like label in two contexts is treated as one role. | Use `F.9` Bridge and `F.18` naming discipline. |

