---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:8"
section_title: "Gating Profiles (applied to E.18)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__011_gating-profiles-applied-to-e-18.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:8 — Gating Profiles (applied to E.18)"
line_start: 82865
line_end: 82876
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:8 - Gating Profiles (applied to E.18)

Profiles set strictness only through an exact current application to one gate, subject, action, scope, and window. A profile description or name does not by itself introduce a crossing, `LaunchGate`, publication face, comparator, selector, cycle, refresh, audit record, evidence lane, or Work occurrence. A.21 defines the profile-application, check-application, decision-result, and optional reuse-record boundaries.

| Profile | Effect inside an active branch | Boundary |
| --- | --- | --- |
| **Lean** | Use the least assurance needed for the active claims. For a current launch branch, keep only the freshness, design-run-tag, ingress, crossing, or other checks required by the exact current profile application and their own rules. For a current publication, keep its minimum pins. | The label activates no branch and supplies no fixed result mapping. |
| **Core** | Strengthen an active branch only as the exact current profile application says: retain independent A.20 and other check results for a current gate; use comparison pins, budget and refresh tests, guard aggregation, a governed SquareLaw check, or the UNM declaration-locus test only when its exact claim and rule are current. | The label activates no absent gate, crossing, publication, selector, cycle, refresh, guard, check, or assurance record. |
| **Safety-Critical or RegulatedX** | Add the applicable safety-envelope or regulator checks and use the stricter folds for the active gate, crossing, publication, or assurance branch. | The profile tightens an applicable check; it does not manufacture the subject of that check. |

**Profile selection and change.** Cite the exact current policy-application fact, including its rule and edition, applicability, gate and subject, scope, window, required set, mappings, and any separately required authority. A `PathSlice` only bounds changed data or currentness and may trigger reevaluation; it neither selects, inherits, overrides, nor weakens a profile. G.11 supplies refresh wiring only when refresh itself is current.

