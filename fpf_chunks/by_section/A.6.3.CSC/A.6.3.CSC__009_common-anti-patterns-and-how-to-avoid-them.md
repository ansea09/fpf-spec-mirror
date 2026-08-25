---
chunk_kind: "child"
pattern_id: "A.6.3.CSC"
pattern_title: "Controlled Semantic Coarsening"
section_id: "A.6.3.CSC:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CSC/A.6.3.CSC__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.6.3.CSC — Controlled Semantic Coarsening"
  - "A.6.3.CSC:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 13944
line_end: 13956
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.NAR"
  - "A.6.3.RT"
  - "A.6.4"
  - "C.2.1"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "F.9"
  - "F.9.1"
keywords:
---

### A.6.3.CSC:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Avoid by |
| --- | --- | --- |
| Helpful summary becomes authority | The coarsened rendering starts deciding downstream questions that it does not carry. | Publish non-admissible downstream use and reopen trigger. |
| Citation laundering | A coarsened rendering is cited as if it were the source. | Keep the source-bearing side named and reopenable. |
| Label-as-evidence | A lookup handle carries a claim. | State retrieval-only use. |
| Redaction-as-closure | Withheld detail is treated as resolved detail. | State the sharing boundary and accountability reopen condition. |
| Stance cure | `projection` or `nonEquivalent` is used instead of the Bridge, bounded-use claim, loss account, or source return. | Recover the F.9 Bridge and bounded-use claim, keep the CSC source return, and add an F.9.1 stance note only as optional reader help. |
| Briefing-as-work | A summary becomes work plan, action cue, gate, or approval. | Use `A.15`, `A.20`, or `A.21` for the work, constraint, or gate claim. |
| Summary-chain source loss | A note summarizes an already coarsened note and loses the original source and loss envelope. | Keep the same source-bearing side and added loss delta visible, or reopen that source-bearing side. |
| Aggregation EntityOfConcern shift | A quotient or bundle turns several entities or alternatives into one new proxy EntityOfConcern. | Apply `A.6.4` rather than treating EntityOfConcern shift as a same-lineage source-to-rendering case. |

