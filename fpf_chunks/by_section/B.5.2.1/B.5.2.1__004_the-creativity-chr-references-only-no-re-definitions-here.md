---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Creative Abduction with NQD"
section_id: "B.5.2.1:3"
section_title: "The Creativity‑CHR (references only; no re‑definitions here)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__004_the-creativity-chr-references-only-no-re-definitions-here.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "B.5.2.1 — Creative Abduction with NQD"
  - "B.5.2.1:3 — The Creativity‑CHR (references only; no re‑definitions here)"
line_start: 33053
line_end: 33066
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
  - "Creativity-CHR"
  - "DecisionSubject note"
  - "E/E-LOG"
  - "NQD binding"
  - "Novelty@context"
  - "Q-front"
  - "creative abduction"
  - "declared Q components"
  - "retained exploration/archive evidence"
  - "Γ_nqd.generate"
  - "ΔDiversity_P"
---

### B.5.2.1:3 - The **Creativity‑CHR** (references only; no re‑definitions here)

This binding **references** the context‑local **Creativity‑CHR** (see **C.17**) and **does not** restate measurement templates. The primary coordinates are:
• **`Novelty@context`** (C.17 §5.1), • **`ΔDiversity_P`** (marginal; C.17 §5.5), and • **`Q` components** (per A.18).
**`Surprise`** and **`Illumination`** are **secondary**: Illumination is **report‑only telemetry** (published as **`IlluminationSummary`** over `Diversity_P`); both act as **tie‑breakers** unless explicitly promoted by policy (C.19).
**`Use‑Value`** (*alias:* `ValueGain`) is **informative for decision lenses** (Decsn‑CAL) and **MUST NOT** enter NQD dominance by default (see C.17 §5.2).

All listed **Characteristics** are **context‑local** with explicit units/ranges and **polarity↑**. They are *measurements*, not eligibility conditions; eligibility conditions are supplied by **USM/RSG**. (Complies with **A.18** measurement discipline; does not overload assurance semantics.)

> **Lexical discipline.** The items above are **Characteristics** in the sense of **A.17/A.18**; avoid reserved names such as “validity” or “operation.”
> **Normalization note.** If a **QualityVector** has heterogeneous units, Contexts SHALL normalize or nondimensionalize each component before Pareto analysis (see CC‑B.5.2.1‑7).
> **D vs I (normative).** **D = ΔDiversity_P** (marginal gain) is measured for archive quality, tie-breaking, and policy-promoted dominance only. By default it is **not** in the primary `DominanceSet`. **I** is _portfolio illumination_ (report/visual); it **SHALL NOT** be part of the primary dominance test and is usable **only** as an explicit tie-break per policy.
> **Measurement invariants.** Distances, grids, and transforms MUST be declared once per run, versioned, and referenced from provenance (§3, §5).

