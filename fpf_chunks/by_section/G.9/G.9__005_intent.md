---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__005_intent.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:1 — Intent"
line_start: 105447
line_end: 105454
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.21"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.22.1"
  - "C.23"
  - "C.27"
  - "C.28"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
  - "U.ClaimScope"
keywords:
  - "adaptation parity"
  - "benchmark plan"
  - "comparator pins"
  - "freshness windows"
  - "parity harness"
  - "selected-set outcomes"
---

### G.9:1 — Intent

Provide a **notation‑independent** harness that:

* plans parity runs for one explicit subject—either one `EntityOfConcernRef` or target refs under their existing subject patterns—with a `ReferencePlane`, scope, window, applicable rules, CSLC comparability and admissibility references, comparator references (`CNSpecRef`, `CGSpecRef`, `ComparatorSpecRef`), and reproducibility pins for editions and policy ids;
* executes parity in a way that **G.5** can consume, with selected-set outcomes and a DRR and SCR evidence trace;
* publishes an edition-pinned **ParityReport** suitable for downstream consumption, shipping, refresh wiring, and RSCR.

