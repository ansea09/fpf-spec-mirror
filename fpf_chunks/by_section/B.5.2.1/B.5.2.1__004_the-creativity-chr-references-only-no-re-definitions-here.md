---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:3"
section_title: "The Creativity‑CHR (references only; no re‑definitions here)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__004_the-creativity-chr-references-only-no-re-definitions-here.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:3 — The Creativity‑CHR (references only; no re‑definitions here)"
line_start: 46588
line_end: 46601
dependencies:
  - "A.17"
  - "A.18"
  - "B.4"
  - "B.5"
  - "B.5.2"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.5"
keywords:
---

### B.5.2.1:3 - The **Creativity‑CHR** (references only; no re‑definitions here)

This binding **references** the context‑local **Creativity‑CHR** (see **C.17**) and **does not** restate measurement templates. The primary coordinates are:
- **`Novelty@context`** (C.17 §4.1), • **`ΔDiversity_P`** (marginal; C.17 §5.1), and • **`Q` components** (per A.18).
Surprise is an optional coordinate; IlluminationSummary is a retained-set telemetry report under C.17. Use either in comparison only when the C.19 policy names that use and its constituted basis; promotion into dominance requires an explicit policy.
**`Use‑Value`** (*alias:* `ValueGain`) is **informative for decision lenses** (Decsn‑CAL) and **MUST NOT** enter NQD dominance by default (see C.17 §4.2).

For each coordinate actually used, declare its bearer, Characteristic, Scale, polarity, admissible operations, scope, window and evidence basis under C.17. Cite a constituted C.16 measurement result when the coordinate was measured, or a C.2.1 ascription under its declared rule. Candidate must-constraint eligibility and the conditions for performing generation are separate questions.

> **Lexical discipline.** The items above are **Characteristics** in the sense of **A.17/A.18**; avoid reserved names such as “validity” or “operation.”
> **Comparison basis.** Compare each Q coordinate under its declared Scale, polarity and admissible order. Different units across coordinates do not by themselves require normalization for componentwise Pareto comparison. If the chosen comparator requires a transformation, declare it and preserve the order distinctions on which dominance depends (see CC-B.5.2.1-6).
> **D and I.** D = ΔDiversity_P(h | Pool) is a marginal retained-set reading under the same declared measurement policy. It is outside primary dominance unless explicitly promoted. IlluminationSummary reports the retained set; it is not a per-hypothesis primitive coordinate. A C.19 policy may name a tie-break or promoted use with the corresponding report and basis.
> **Measurement invariants.** Distances, grids, and transforms MUST be declared once per run, versioned, and referenced from provenance (§3, §5).

