---
chunk_kind: "child"
pattern_id: "A.6.3.CSC"
pattern_title: "Controlled Semantic Coarsening"
section_id: "A.6.3.CSC:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CSC/A.6.3.CSC__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.6.3.CSC — Controlled Semantic Coarsening"
  - "A.6.3.CSC:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 14595
line_end: 14607
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
| Helpful summary becomes authority | A reader relies on the coarsened rendering for a downstream decision that its claims do not support. | State the unsupported downstream use and reopen trigger. |
| Citation laundering | A coarsened rendering is cited as if it were the source. | Keep the source-bearing side named and reopenable. |
| Label-as-evidence | A reader treats a lookup handle as evidence for a claim in the source. | State retrieval-only use. |
| Redaction-as-closure | Withheld detail is treated as resolved detail. | State the sharing boundary and accountability reopen condition. |
| Stance cure | `projection` or `nonEquivalent` is used instead of establishing the operative relation, supporting its bounded use, or stating loss and source return. | Recover the operative relation under its governing pattern, support its bounded use, and keep the CSC loss account and source return. For a Bridge between exact local senses with different interpretation bases, use F.9 with a separate bounded-use claim; an F.9.1 stance note remains optional reader help. |
| Briefing-as-work | A reader treats a summary as sufficient basis for a work plan, execution cue, gate decision, or approval. | Use the applicable `A.15` pattern for the Work plan or actual Work. For an authority-looking claim, select the matching `A.6` `A6-AW-*` row by the assertion and follow its direct subject pattern; use `A.20` or `A.21` for the actual constraint or gate claim. |
| Summary-chain source loss | A note summarizes an already coarsened note and loses the original source and loss envelope. | Keep the same source-bearing side and added loss delta visible, or reopen that source-bearing side. |
| Aggregation EntityOfConcern shift | A quotient or bundle turns several entities or alternatives into one new proxy EntityOfConcern. | Apply `A.6.4` rather than treating EntityOfConcern shift as a same-lineage source-to-rendering case. |

