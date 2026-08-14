---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:3"
section_title: "Problem (Informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__005_problem-informative.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:3 — Problem (Informative)"
line_start: 28398
line_end: 28406
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2.6"
  - "A.6.5"
  - "C.16"
  - "C.2.1"
  - "E.24"
  - "F.9"
  - "G.11"
  - "G.4"
  - "U.ClaimScope"
  - "U.ContextSlice"
keywords:
  - "CharacteristicSpace"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
  - "system-role–Method–Work assertions stay outside A.19"
---

### A.19:3 - Problem (Informative)

- **P1 - Feature-vector drift.** A list of values with implicit units, scales, missingness, or arity cannot support a sound state or comparison claim.
- **P2 - Lifecycle bias.** Without a declared space, system change is narrated as one-way stages instead of typed trajectories and separately governed state or classification claims.
- **P3 - Semantic-locality collapse.** Different claim scopes, context slices, reference schemes, or reference planes may use different coordinate sets or meanings. Treating one umbrella context label as their common identity makes projection and comparison unverifiable.
- **P4 - Relational characteristics.** A multi-entity characteristic loses arity and direction when flattened into an intrinsic scalar.
- **P5 - Hidden predicate semantics.** A threshold label or criterion-description edition can conceal the actual coordinate bindings, scale, comparator, cut, polarity, and normalization or Bridge basis.
- **P6 - Geometry by implication.** An undeclared order, topology, distance, scalarization, or aggregation can silently decide a comparison or selection.

