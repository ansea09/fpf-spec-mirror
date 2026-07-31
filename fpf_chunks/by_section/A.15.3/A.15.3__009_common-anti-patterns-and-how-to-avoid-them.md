---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 25364
line_end: 25380
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
| Generic slot-bearing description | Any description with fields is treated as a reusable declaration. | Point to a declared `RelationSignature` SlotSpec, A.6.1 argument or result, or another member whose pattern defines its meaning and actual use. |
| Dependent PlanItem U-kind | A ClaimGraph component receives a rival identity and ontic settlement. | Keep `SlotFillingsPlanItem` as declaration-local WorkPlan content. |
| Planned SlotRelation | The plan claim is reified as an obtaining world-side relation. | Keep planned filling as positive claim content; open an actual relation only under its direct predicate. |
| Declaration/plan responsibility blur | The declaration pattern is said to make the planning intention, or A.15.3 is said to define actual use. | Let the declaration pattern define member meaning and actual-use predicate; let A.15.2 and A.15.3 state the intention. |
| Method-description slot | Generic method wording is mistaken for a declaration member. | Keep it as ordinary plan content or return `missing-governor` when typed reuse is required. |
| Relation/operation collapse | A.6.1 arguments and results are written as A.6.5 SlotSpecs. | Dispatch by target family and keep each declaration vocabulary local. |
| Row-count cardinality | Row count or order silently defines multiplicity, alternatives, or sequence. | Use the declaration's cardinality; for alternatives, state conditions and a resolution rule. |
| Empty filler as prohibition | Omission, null, or a negated reference is read as *must not use*. | State prohibition, exclusion, required absence, or completeness as a separate plan claim. |
| Plan-as-actual | A planned value is treated as actual participation or a returned result. | Identify work and actual relation or application bindings independently. |
| Generic reference or policy | `Ref`, `SpecRef`, `PolicyRef`, or a shared label is treated as sufficient. | Use the concrete RefKind and identify the policy's kind, defining pattern, edition, applicability, and reference scheme. |
| Latest-as-baseline | A mutable label stands for a declaration or value edition. | Pin the edition when choosing another one could change the planned or comparison result. |
| Backfilled plan | Actual values replace planned rows after work. | Preserve the cited plan edition and state a neighboring substitution or variance claim. |

