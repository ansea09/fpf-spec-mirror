---
chunk_kind: "child"
pattern_id: "C.29.1"
pattern_title: "Mathematical Result Transfer"
section_id: "C.29.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.1/C.29.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.1 — Mathematical Result Transfer"
  - "C.29.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 60059
line_end: 60071
dependencies:
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "C.29"
keywords:
---

### C.29.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | How it changes the answer | Repair |
|---|---|---|
| “The numbers match in both formulas.” | Matching sampled values can conceal different domains or operations. | Derive the comparison for the claimed domain, or limit the conclusion to the cases established. |
| Naming an on-hand total “available” | The name conceals reserved stock; the same display permits and forbids a reservation. | Construct n − r and compare the update and its condition. |
| Choosing a convenient representative | The chosen route's cost is assigned to a summary that also represents other costs. | Establish independence or define the intended class operation, such as minimum over compatible routes. |
| Transferring arithmetic while dropping availability | The cost 1 + 2 is correct for a route composition that is unavailable. | Restore the permission or history needed for composition; otherwise use the relaxed minimum only as a bound. |
| Reversing a many-to-one map without justification | Equal receiving values are treated as identical source states or as a unique source action. | Retain a distinguishing quantity or construct an allowed source witness for the specific result. |
| Treating one preserved quantity as a complete state | Correct mean evolution is used to infer an unresolved maximum. | Express the query in retained variables and bound or restore the missing contrast. |
| Rejecting every inexact transfer | A sufficient threshold bound is discarded because it is not a reconstructed value. | Compare the justified bound with the actual decision. |
| Treating physical interpretation as another algebraic equality | A correct thermal derivation is taken to validate its exchange law for actual bodies. | State the model's physical premises and establish their application through physical and measurement work. |

