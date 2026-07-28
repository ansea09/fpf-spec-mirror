---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__010_consequences.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:9 — Consequences"
line_start: 64612
line_end: 64620
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.32"
  - "C.32.ACS"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "architecture-characteristic eval program"
  - "comparison input"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Evals are typed evaluations over declared criteria. | Variant comparison can proceed without collapsing criteria, readings, and decisions. | The team must write the parity frame before using the result in a receiving pattern. |
| Expectation-failure tests remain one eval operation when their expectation is declared. | Error prevention remains available without replacing optimization. | Some pass-fail dashboards can no longer drive decisions by themselves. |
| Losing variants remain useful. | Architecture exploration keeps stepping stones and source-space learning. | The variant archive needs deliberate upkeep. |
| Proxy and counter-characteristic risks are explicit. | Goodhart pressure is visible before eval results drive work. | More rows may remain monitored as guardrails rather than optimized. |

