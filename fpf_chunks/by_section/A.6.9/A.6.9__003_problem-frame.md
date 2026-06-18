---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "Cross-Context Sameness Disambiguation - Repairing cross-context \"same / equivalent / align\" via explicit Bridges (RPR-XCTX)"
section_id: "A.6.9:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__003_problem-frame.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.6.9 — Cross-Context Sameness Disambiguation - Repairing cross-context \"same / equivalent / align\" via explicit Bridges (RPR-XCTX)"
  - "A.6.9:1 — Problem frame"
line_start: 17441
line_end: 17457
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

### A.6.9:1 - Problem frame

Cross‑Context prose routinely uses umbrella predicates (“same”, “equivalent”, “align”, “map”, “matches”, “corresponds”) to compress a multi‑dimensional claim into a single adjective.

In FPF terms, this is almost never a single claim. It is a *Bridge situation* that typically contains, at minimum:

* two (or more) **Contexts** (`U.BoundedContext`; each with its own idiom);
* a potentially hidden **direction** (A→B is not B→A);
* a hidden **degree of fit** (≈ vs ⊑/⊒ vs ⋂ vs ⊥, or interpretation‑only);
* near‑inevitable **loss/distortion** on transfer;
* a (usually implicit) **edition / time‑slice basis** for both endpoints and the correspondence judgement (`Γ_time`);
* a usually implicit **facet span** (`facetSpan`; “which aspects are being aligned?”) — the correspondence is often a *partial lens*, not whole‑cell sameness;
* a critical ambiguity between **lexical synonymy / translation** (“same word/label”), **shared EntityOfConcern reference** (“same EntityOfConcern under different IDs”), and **value‑level normalization** (“equivalent after φ‑normalization / unit conversion”).
* a critical ambiguity between **explaining** a correspondence and **licensing substitution**.

A.6.9 is the RPR specialisation that makes this structure explicit and prevents accidental “global identity” claims when the author’s intent is merely naming convenience or interpretive help.

