---
chunk_kind: "child"
pattern_id: "C.33"
pattern_title: "Assess Structural Information for Architecture Use"
section_id: "C.33:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.33/C.33__007_bias-annotation.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.33 — Assess Structural Information for Architecture Use"
  - "C.33:6 — Bias-Annotation"
line_start: 80381
line_end: 80390
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.8"
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
  - "ADR"
  - "captured structure"
  - "diagram"
  - "missing structure"
  - "observer boundary"
  - "partial description"
  - "relation graph"
  - "source return"
  - "structural information adequacy"
---

### C.33:6 - Bias-Annotation

| Bias | How C.33 counters it |
| --- | --- |
| Carrier completeness bias | Explain captured structure and the use it supports. State lost, hidden or uncaptured structure and excluded uses where they affect reliance. |
| Metric bias | Treat entropy, epiplexity estimate, benchmark score, dashboard value, dependency F1, and invariant F1 as readings only when `C.16` or `C.32.ACE` has opened that claim. |
| Source-label ontology bias | Keep source labels such as layer, router, cache, expert, pruning, distillation, block, DSM cluster, and architecture-search result as source wording. When a label carries an unresolved FPF structure or relation claim, use `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `C.31`, `C.32`, or another direct subject pattern to recover the object and predicate for that claim. |
| Observer-belief bias | State observation class, confidence, active-passive gap, budget boundary and unexplored regions where they qualify the use of an agent-produced or probe-produced carrier. A map alone does not establish internal belief, safe change or assurance. |
| Decision-memory bias | Treat ADR-like records as decision descriptions and method expectations. Use `C.32.PAD` or `C.32.ADR` for decision and projection claims, and use C.33 only for what structural content the record carries or loses. |

