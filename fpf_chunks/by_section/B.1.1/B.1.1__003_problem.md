---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Graph & Proofs"
section_id: "B.1.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__003_problem.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "B.1.1 — Dependency Graph & Proofs"
  - "B.1.1:2 — Problem"
line_start: 30048
line_end: 30056
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
keywords:
  - "dependency graph"
  - "proofs"
  - "set"
  - "slice"
  - "structural aggregators"
  - "sum"
---

### B.1.1:2 - Problem

Without a disciplined `DependencyGraph`, four pathologies recur:

1. **Relation drift:** Edges blur composition with mapping (e.g., “represents”), or confuse collections with parts. Aggregations then mix algebraic regimes (sums where mins are required, etc.).
2. **Boundary blindness:** Cross‑holon influences are drawn as parts, bypassing explicit `U.Boundary` and `U.Interaction`. This corrupts locality (LOC) and defeats reproducible folding.
3. **Temporal conflation:** `design‑time` and `run‑time` holons appear in one graph; simulations then “prove” facts about a blueprint using live telemetry.
4. **Hidden cycles:** Self‑dependence enters through aliasing (e.g., a team is a member of itself via “units of units”). Γ cannot topologically fold such graphs.

