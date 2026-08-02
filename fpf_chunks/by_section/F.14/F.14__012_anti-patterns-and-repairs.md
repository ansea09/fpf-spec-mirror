---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:11"
section_title: "Anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__012_anti-patterns-and-repairs.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:11 — Anti-patterns and repairs"
line_start: 93705
line_end: 93718
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
  - "E.17"
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


| ID | Anti-pattern | Symptom | Why it breaks thinking | Repair |
| --- | --- | --- | --- | --- |
| AP-1 | Hybrid role minting | `RequestApproverRole` becomes one role. | Erases role relation structure and separation checks. | Use A.2.7 bundle or incompatibility relation; create a role only after F.8 and F.18 admission. |
| AP-2 | Modifier-as-role | `NightOperatorRole` or `RemoteOperatorRole` appears for every circumstance. | Circumstances become kinds. | Recover schedule, location, role state, work-plan, or policy qualifier. |
| AP-3 | Status role | `ReadyReviewerRole` or `EvidenceRole` becomes a role-name family. | Status or evidence use becomes role ontology. | Use F.10, A.10, B.3, E.10.D2, or direct status and evidence patterns. |
| AP-4 | Prestige bypass | `SeniorReviewer` bypasses incompatibility or assignment checks. | Trust label substitutes for assurance or separation. | Keep role relation; use B.3, capability, role state, or assignment checks. |
| AP-5 | Row duplication | New row or public term for a name already admitted by a bridge and row. | Concept-Set table widens without new meaning. | Reuse the row; record the old term as lineage or source wording when needed. |
| AP-6 | Assignment hidden in role name | `AliceReviewerRole` looks like a role value. | Holder assignment is hidden in a name. | Use A.2.1 and F.6; keep the role value separate. |
| AP-7 | Method hidden in role name | `PressureTestReviewerRole` mixes method requirement and role. | Method and role become one ontology. | Use A.3.1 and A.3.2 for method, A.2 for role, F.18 only after recovery. |
| AP-8 | Presentation as status family | Red, amber, and green become status types. | Display colors substitute for status values and criteria. | Use direct status or presentation pattern; keep status family explicit. |

