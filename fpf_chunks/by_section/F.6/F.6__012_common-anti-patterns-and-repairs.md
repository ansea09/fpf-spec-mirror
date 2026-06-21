---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:10"
section_title: "Common Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__012_common-anti-patterns-and-repairs.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:10 — Common Anti-Patterns and Repairs"
line_start: 76132
line_end: 76144
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:10 - Common Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Role description as assignment | A role card or label is cited as proof that someone holds the role. | Recover `U.RoleAssignment` through `A.2.1`; keep the card as role-description episteme under `F.4`. |
| Assignment as work | "Assigned reviewer" is used as evidence that review happened. | Name the `U.Work` occurrence under `A.15.1` or lower the claim to assignment only. |
| Work without assignment | A work log names "reviewed" but gives no holder-role-context assignment. | Recover holder, role, context, and window; if missing, block performed-work attribution. |
| `U.RoleEnactment` revival | A log or pattern names a durable role-enactment object. | Use `Work.performedBy = RoleAssignment`; name `RoleEnactmentFact` only when a fact label is useful. |
| Evidence role | A report, dataset, model card, or standard is made a role holder. | Use evidence-use, source-use, standard-use, requirement-use, status-use, or publication-use relation. |
| Status branch | `Approved`, `Ready`, `Satisfied`, or `Valid` is handled as a role. | Use `F.10` or the direct status-use pattern. |
| Access role as work role | RBAC or permission label is used as proof of work-facing role assignment. | Recover the access or policy relation first; create a work-facing role assignment only if actual work attribution is current. |
| Cross-context role reuse | BPMN participant, RBAC role, PROV activity, or local team role are treated as one role. | Keep local assignment; use `F.9` for bridge or substitution claims. |

