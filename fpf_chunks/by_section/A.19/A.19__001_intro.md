---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__001_intro.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:intro — Intro"
line_start: 28649
line_end: 28659
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

## A.19 - CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)

> **Type:** Kernel characteristic-space and dynamics-typing pattern
> **Status:** Stable

**Use this when.** Use this pattern when the current object is either a declared `CharacteristicSpace` or a reusable by-value `CharacteristicSpacePredicate` over that space: characteristics, scales, value sets, coordinate bindings, optional overlays, predicate operators and cuts, comparability boundaries, normalization boundaries, missingness, and the `U.Dynamics.stateSpace` hook.

**What goes wrong if missed.** Teams compare raw numbers from different scales, treat dashboards or scores as the space, hide thresholds inside state labels, silently change a predicate use's scope or evaluation window, smuggle method sequences into checklists, or give consumer patterns private space and predicate kinds.

**What this buys.** One declared space and one recoverable predicate form that make state, threshold, comparability, normalization, and dynamics-typing claims inspectable while leaving each evaluation, result, evidence use, gate, and selection occurrence with its subject pattern.

