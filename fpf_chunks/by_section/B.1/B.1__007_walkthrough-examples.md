---
chunk_kind: "child"
pattern_id: "B.1"
pattern_title: "Universal Algebra of Aggregation (Γ)"
section_id: "B.1:6"
section_title: "Walkthrough Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1/B.1__007_walkthrough-examples.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "B.1 — Universal Algebra of Aggregation (Γ)"
  - "B.1:6 — Walkthrough Examples"
line_start: 29957
line_end: 29982
dependencies:
  - "A.1"
  - "A.9"
  - "B.1.x"
  - "B.2"
keywords:
  - "COMM"
  - "IDEM"
  - "LOC"
  - "MONO"
  - "WLNK"
  - "aggregation"
  - "composition"
  - "gamma operator"
  - "holon"
  - "invariants"
---

### B.1:6 - Walkthrough Examples

#### B.1:6.1 - `Γ\_sys` — Offshore Wind Farm (2025 build)

1. **Parts**: 72 nacelles, 72 towers, 1 export cable set.
2. **Graph**: acyclic; each nacelle depends on its own tower, all depend on cable.
3. **Fold**: Any parallel assembly order is legal → COMM, LOC.
4. **WLNK check**: weakest nacelle (load factor = 0.91) bounds farm output ≤ 0.91 × rated.
5. **Upgrade test**: swapping one nacelle to 0.95 raises farm bound — satisfies MONO.

*Result*: farm holon inherits predictable capacity curve; financiers can quote risk‑adjusted yield without bespoke simulation.

#### B.1:6.2 - `Γ_epist` — Living Systematic Review on mRNA Therapies (2024–2025)

1. **Parts**: 38 peer‑reviewed trials, 12 preprints.
2. **Graph**: dependency edges encode shared cohorts; no cycles.
3. **Fold**: trials merged irrespective of ingestion order → COMM; distributed evaluators may differ, but provenance hashes equalise weighting → LOC.
4. **WLNK**: overall certainty cannot exceed the lowest GRADE score among included trials.
5. **Emergence**: discovery of a consistent age‑interaction effect violates WLNK; reviewers declare **MHT**, elevating the combined dataset to a new holon “Evidence v2” with age‑stratified potency as a *novel attribute*.

*Result*: regulators see a transparent promotion of evidence-support status rather than a hidden statistical artefact.

#### B.1:6.3 - `Γ\_time` — National Grid Frequency Forecast (2025‑2030)

*COMM* holds only across non‑overlapping windows; *LOC* is waived because regional sensors differ in latency.  Additional TS‑1/TS‑2 rules ensure gaps are filled before aggregation.  Engineers iterate locally yet obtain one coherent five‑year projection.

