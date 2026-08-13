---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:11"
section_title: "Anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__012_anti-patterns-and-repairs.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:11 — Anti-patterns and repairs"
line_start: 95718
line_end: 95732
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.24.PUB"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
  - "NameCard"
  - "assignment"
  - "designation"
  - "evidence use"
  - "permission"
  - "reuse"
  - "status names"
  - "system-role names"
  - "term row"
  - "vocabulary explosion"
---

### F.14:11 - Anti-patterns and repairs

| ID | Anti-pattern | Symptom | Repair |
| --- | --- | --- | --- |
| AP-1 | Hybrid-system-role minting | `RequestApproverSystemRole` becomes one kind. | Use exact A.2.7 relations; admit a new kind only under A.2 with C.3 and later naming gates. |
| AP-2 | Modifier-as-system-role | Every circumstance yields `NightOperatorSystemRole` or `RemoteOperatorSystemRole`. | Recover schedule, location, state, plan, or policy qualifier. |
| AP-3 | Status or evidence role | `ReadyReviewerSystemRole` or `EvidenceRole` becomes a system-role family. | Use F.10 for status, A.10 or B.3 for evidence use, E.10.D2 for description use, or the pattern that defines, constrains, or tests the recovered claim. |
| AP-4 | Prestige bypass | `SeniorReviewer` substitutes for assurance or separation. | Keep the system-role kind fixed and recover capability, state, assurance, policy, or assignment checks. |
| AP-5 | Row duplication | Another row is added for an already admitted name and use. | Reuse the exact row within its admitted use; retain old wording as lineage when useful. |
| AP-6 | Assignment hidden in a name | `AliceReviewerSystemRole` looks like a kind but encodes one assigned system. | Use A.2.1 to recover the exact assignment occurrence. Use F.6 only when a separate claim attributes dated Work to that assignment; keep the local system-role kind separate. |
| AP-7 | Method hidden in a system-role name | `PressureTestReviewerSystemRole` fuses a Method and a kind. | Keep the Method and system-role kind under their direct patterns; name either only after recovery. |
| AP-8 | Presentation as status family | Red, amber, or green becomes status ontology. | Recover the exact status criterion and keep display form separate. |
| AP-9 | Naming-object cascade | A word automatically gets a cell, card, row, id, and publication. | Apply each gate separately and stop at the lightest useful disposition. |
| AP-10 | Spelling-based cross-local identity | Same label merges values or automatically creates a Bridge. | Resolve exact local senses; test F.9 only for a named use and keep governed values distinct. |

