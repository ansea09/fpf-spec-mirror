---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 25256
line_end: 25272
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "U.WorkPlan"
keywords:
  - "WorkPlan claim content"
  - "actual-use predicate"
  - "baseline replay"
  - "concrete RefKind and policy"
  - "direct owner"
  - "edition pin"
  - "exact declaration member"
  - "intended-performance designator"
  - "no actuality by plan"
  - "open-world omission"
  - "participant/argument/result meaning"
  - "positive planned designation"
  - "semantic cardinality"
---

### A.15.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Generic slot-bearing description | Any description with fields becomes a reusable declaration. | Resolve one exact RelationSignature SlotSpec, A.6.1 argument/result declaration, or other directly governed declaration member. |
| Dependent PlanItem U-kind | A ClaimGraph component receives a rival identity and ontic settlement. | Keep `SlotFillingsPlanItem` as declaration-local WorkPlan content. |
| Planned SlotRelation | The plan claim is reified as an obtaining world-side relation. | Keep planned filling as positive claim content; open an actual relation only under its direct predicate. |
| Planned-meaning owner blur | The target's direct pattern is said to own the planning intention. | Let the target owner govern reusable member meaning and corresponding actual-use predicate; let A.15.2/A.15.3 govern intended-use content. |
| Method-description slot | Generic method semantics are mistaken for declaration members. | Cite the method description as ordinary plan content or return a missing declaration governor for typed reuse. |
| Relation/operation collapse | A.6.1 arguments and results are written as A.6.5 SlotSpecs. | Dispatch by target family and keep each declaration vocabulary local. |
| Row-count cardinality | Repeated rows or their order silently define multiplicity, alternatives, or sequence. | Apply the target declaration's semantic cardinality and an exact policy whose conditions and resolution rule determine the effective planned value. |
| Empty filler as prohibition | Omission, null, or a negated reference is treated as “must not use.” | State prohibition, exclusion, required absence, or completeness as a separate governed plan claim. |
| Plan-as-actual | A planned value is treated as actual participation or a returned result. | Identify work and actual relation or application bindings independently. |
| Generic reference or policy | `Ref`, `SpecRef`, `PolicyRef`, or a shared label is treated as sufficient. | Use the concrete governed RefKind and exact policy kind, owner, edition, applicability, and reference scheme. |
| Latest-as-baseline | A mutable label stands for the declaration or value edition. | Pin the exact edition when the receiving use depends on it. |
| Backfilled plan | Actual values replace planned rows after work. | Preserve the cited plan edition and state a neighboring substitution or variance claim. |

