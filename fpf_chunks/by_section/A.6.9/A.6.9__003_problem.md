---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "U.CrossContextSamenessDisambiguation - Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR‑XCTX)"
section_id: "A.6.9:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__003_problem.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.6.9 — U.CrossContextSamenessDisambiguation - Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR‑XCTX)"
  - "A.6.9:2 — Problem"
line_start: 16755
line_end: 16768
dependencies:
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.3.3"
  - "E.10"
  - "E.10.D1"
  - "E.10.U9"
  - "E.17"
  - "E.19"
  - "F.0.1"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "CL"
  - "SenseCells"
  - "alignment"
  - "bridge"
  - "cross-context sameness"
  - "direction"
  - "loss notes"
  - "mapping"
  - "substitution licence"
  - "weakest-link"
---

### A.6.9:2 - Problem

When an umbrella predicate is used as if it were a single relation, readers (and downstream editors) silently choose defaults:

* **Symmetry hallucination:** “equivalent” is read as symmetric even when the intended relation is ⊑/⊒ (directional).
* **Scope creep:** “align/map” is read as substitution‑eligible, leaking into Role Assignment & Enactment or Concept‑Set row scopes.
* **Loss erasure:** “same” implies lossless transfer even when units, granularity, preconditions, or stance differ.
* **License confusion:** “explain X using Y” is mistaken for “Y can stand in for X”.
* **Implicit inversion:** later prose uses the inverse direction without an explicit redeclaration, breaking the “no silent inversion” rule.

The result is not merely imprecise wording: it changes what inferences are considered safe, and it pollutes Concept‑Set row scopes via unnoticed weakest‑link violations.

It also breaks **temporal coherence**: if the underlying canons (glossaries, schemas, code lists, ontologies) evolve, an un‑pinned “equivalent” claim silently becomes a claim about *two different editions at once*.

