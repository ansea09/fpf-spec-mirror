---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:10"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__014_relations.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:10 — Relations"
line_start: 90656
line_end: 90676
dependencies:
  - "A.19"
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
keywords:
  - "adaptation parity"
  - "benchmark plan"
  - "comparator pins"
  - "freshness windows"
  - "parity harness"
  - "selected-set outcomes"
---

### G.9:10 — Relations

**C.27 temporal-claim relation.**

- C.27 may flag: dynamic parity when a benchmark actually compares rate-change, rhythm change, recovery speed, intervention effect, effort budget, or dynamic outcome.
- This pattern keeps: baseline, freshness, comparator edition, effort/budget parity, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: faster improvement is not benchmark superiority, and `dyn2BenchmarkParityBlock?` is a benchmark input declaration, not a benchmark harness.
- Exit: when live, recover `dynOrderCompared`, baseline window, adaptation/intervention window, effort or budget parity reference, rate/rate-change measure, `G9ParityPlanRef`, and optional `G9ParityReportRef`; G.5 is relevant only if selector publication consumes such a benchmark result.

**C.29 mathematical-lens use relation.**

- C.29 may flag: parity or benchmark input whose comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, parity measure, model-family label, or model-selection basis depends on a mathematical lens that changes the parity claim and is missing, under-specified, or overread.
- This pattern keeps: baseline set, freshness, comparator edition, normalization ids, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: a `C.29` output does not publish a benchmark report, create benchmark superiority, supply selector output, or supply parity-measure admissibility by itself.
- C.29 application: for an under-lensed or overread parity input, cite the applicable `C.29` output for the stated use: `NoMathLensUseNeeded`, `MathLensUse.LensCandidateNote`, `MathLensUse.OneLine`, `MathLensUse.MiniCard`, `MathLensUse.FullCard`, or `NeighborGoverningPatternNote`. Use the cheap output that changes the next admissible parity use; full-card work is only required when the live parity or benchmark claim needs it.

**Builds on:** `G.Core`, `G.5`, `G.6`, `G.4`, `F.15`, `E.17`, `E.18`, `A.21`, `F.17`, `E.5.2`, `E.10`.
**Publishes to:** **UTS** (plan/report ids), **G.11** (refresh wiring), **G.10** (shipping publication form; parity records are cited records).
**Uses:** **G.0**, **A.19**, **F.9**, and `C.28` when parity compares causal methods or causal-use claims.
**Uses (optional, via Extensions):** **G.7**, **C.18 and C.19** (QD/OEE wiring), **C.23** (SoS‑LOG narration and failure‑policy pins).

