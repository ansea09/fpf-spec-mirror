---
chunk_kind: "child"
pattern_id: "C.16.RM"
pattern_title: "Repair a Measurement Model or Arrangement"
section_id: "C.16.RM:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.RM/C.16.RM__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "acc387fc7a206495eabe07f1953849217f291715"
heading_path:
  - "C.16.RM — Repair a Measurement Model or Arrangement"
  - "C.16.RM:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 53867
line_end: 53877
dependencies:
  - "B.5.MPC.R"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.16"
  - "C.16.IR"
  - "C.16.MR"
  - "C.28"
  - "C.29.2"
keywords:
---

### C.16.RM:8 - Common Anti-Patterns and How to Avoid Them

| Failure in these situations | Consequence | Repair |
| --- | --- | --- |
| Repeat a mixed signal and average it | The stable background remains in the result. | Cancel, estimate or control the consequential contribution through a justified relation. |
| Add an unknown correction without a way to bound or determine it | The formula changes while the target stays unresolved. | Obtain the missing relation or choose an arrangement that limits the influence. |
| Improve agreement by changing the wanted subject condition | The new reading answers a different question. | Preserve the target or derive the relation connecting the changed condition to it. |
| Treat an implementation test as confirmation of the physical model | Correct arithmetic is used to support an untested subject premise. | Match the comparison to the contribution whose adequacy is in question. |
| Continue fault diagnosis after a sufficient repair | The present result is delayed for an unrelated explanation. | Return the adequate result and pursue the remaining cause only for a question that needs it. |
| Apply a new correction to an old result without checking its conditions | The revised value can misrepresent the earlier measurement. | Reuse the retained observations through a relation supported for that situation. |

