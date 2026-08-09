---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:11"
section_title: "Anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__012_anti-patterns-and-repairs.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:11 — Anti-patterns and repairs"
line_start: 94942
line_end: 94956
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
  - "F.8"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:11 - Anti-patterns and repairs

| ID | Anti-pattern | Symptom | Repair |
| --- | --- | --- | --- |
| AP-1 | Hybrid-role minting | `RequestApproverRole` becomes one role. | Use exact A.2.7 relations; admit a new role only under the direct role owner and later naming gates. |
| AP-2 | Modifier-as-role | Every circumstance yields `NightOperatorRole` or `RemoteOperatorRole`. | Recover schedule, location, state, plan, or policy qualifier. |
| AP-3 | Status or evidence role | `ReadyReviewerRole` or `EvidenceRole` becomes a role family. | Return status/evidence use to F.10, A.10, B.3, E.10.D2, or its direct owner. |
| AP-4 | Prestige bypass | `SeniorReviewer` substitutes for assurance or separation. | Keep the role fixed and recover capability, state, assurance, policy, or assignment checks. |
| AP-5 | Row duplication | Another row is added for an already admitted name and use. | Reuse the exact row within its admitted use; retain old wording as lineage when useful. |
| AP-6 | Assignment hidden in a name | `AliceReviewerRole` looks like a role value. | Use A.2.1/F.6 and keep the role value separate. |
| AP-7 | Method hidden in a role name | `PressureTestReviewerRole` fuses method and role. | Keep method and role under their direct owners; name either only after recovery. |
| AP-8 | Presentation as status family | Red/amber/green becomes status ontology. | Recover the exact status criterion and keep display form separate. |
| AP-9 | Naming-object cascade | A word automatically gets a cell, card, row, id, and publication. | Apply each gate separately and stop at the lightest useful disposition. |
| AP-10 | Spelling-based cross-local identity | Same label merges values or automatically creates a Bridge. | Resolve exact local senses; test F.9 only for a named use and keep governed values distinct. |

