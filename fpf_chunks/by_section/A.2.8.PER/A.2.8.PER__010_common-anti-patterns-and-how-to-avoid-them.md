---
chunk_kind: "child"
pattern_id: "A.2.8.PER"
pattern_title: "Granted Permission, Exercise, and Non-Prohibition"
section_id: "A.2.8.PER:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8.PER/A.2.8.PER__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.2.8.PER — Granted Permission, Exercise, and Non-Prohibition"
  - "A.2.8.PER:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 9139
line_end: 9152
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8"
  - "A.2.9"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "F.6"
  - "U.Work"
keywords:
  - "checked non-violation"
  - "exact policy rule or decision result"
  - "matching dated-work exercise"
  - "permission or prohibition conflict"
  - "policy-valid strong grant"
  - "weak non-prohibition finding"
---

### A.2.8.PER:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| `MAY` stored as a `U.Commitment` modality | Recover whether the claim is a strong grant, weak finding, entry predicate, or ordinary prose; use the applicable subject pattern. |
| No prohibition found, therefore permission | Return `nonProhibited` only for a current frame sufficiently complete for the use; otherwise return `unresolved`. Neither result establishes a grant. |
| Permit document as permission | Establish what the operative rule makes sufficient. A permit can evidence an existing grant. Check its applicability, current scope and window, and the instituting act or combination when the question depends on that history. |
| Gate pass as authorization | Keep `GateDecisionResult` in `A.21`; cite a separate grant/conflict result when the gate consumes one. |
| Permission as readiness or capability | Keep readiness in `A.15.5` and capability in `A.2.2`; permission supplies neither. |
| Work “violates permission” | Test exercise coverage and any separately governed prohibition; uncovered work is not a permission violation by default. |
| Unnecessary evaluation records for action match or beneficiary eligibility | Test the Work against the action specification and the performer against the beneficiary branch; cite the already obtaining assignment or on-behalf-of relation and add separate evaluation evidence only when a receiving use needs it. |
| Precedence “owner” as resolution | Apply the rule when it selects the outcome. When a decision is needed, establish the authorised decision or combination of decisions and the result for this conflict. |
| Hidden generic beneficiary kind | Keep the closed reference union and branch-specific eligibility checks. |

