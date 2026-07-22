---
chunk_kind: "child"
pattern_id: "C.33"
pattern_title: "Structural Information Adequacy for Architecture Capture and Missing-Structure Return"
section_id: "C.33:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.33/C.33__007_bias-annotation.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.33 — Structural Information Adequacy for Architecture Capture and Missing-Structure Return"
  - "C.33:6 — Bias-Annotation"
line_start: 65627
line_end: 65636
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
  - "G.5"
keywords:
  - "captured selected structure"
  - "carrier"
  - "lost structure"
  - "missing structure"
  - "missing-structure return"
  - "observer boundary"
  - "selected structure"
  - "structural information adequacy"
---

### C.33:6 - Bias-Annotation

| Bias | How C.33 counters it |
| --- | --- |
| Carrier completeness bias | Require captured selected structure, expected but uncaptured structure, lost or hidden structure, admissible use, and non-admissible use before relying on the carrier. |
| Metric bias | Treat entropy, epiplexity estimate, benchmark score, dashboard value, dependency F1, and invariant F1 as readings only when `C.16` or `C.32.ACE` has opened that claim. |
| Source-label ontology bias | Keep source labels such as layer, router, cache, expert, pruning, distillation, block, DSM cluster, and architecture-search result as labels until `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `C.31`, `C.32`, or another governing pattern recovers the selected structure and relation. |
| Observer-belief bias | Record observation class, confidence, active-passive gap, budget boundary, and unexplored regions for agent-produced or probe-produced carriers. Do not infer internal belief, safe change, or assurance from a map. |
| Decision-memory bias | Treat ADR-like records as decision descriptions and method expectations. Use `C.32.PAD` or `C.32.ADR` for decision and projection claims, and use C.33 only for what structural content the record carries or loses. |

