---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__001_intro.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:intro — Intro"
line_start: 49476
line_end: 49493
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "G.10"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "DoE (design‑of‑experiments)"
  - "Scale Variables (S)"
  - "ScaleWindow"
  - "UNM/NormalizationMethod‑based mapping"
  - "compute‑elasticity"
  - "data‑elasticity"
  - "diminishing returns"
  - "exponent class"
  - "iso‑scale parity"
  - "knee"
  - "knee detection"
  - "resolution‑elasticity"
  - "scale variables (S)"
  - "scale‑probe"
  - "scaling law"
  - "segmented regression"
---

## C.18.1 - Scaling‑Law Lens Binding (SLL)

> **Status:** Stable
> **Type:** Pattern

**Use this pattern when.** Use C.18.1 when a generator, selector, method family, benchmark, or comparison claims that behavior changes with scale, budget, data, model capacity, iteration budget, freedom of action, or another monotone scale variable.

**What goes wrong if missed.** Teams compare unequal budgets, call coverage telemetry an objective, claim a knee without probe evidence, or assume more scale means linear improvement across a window where the behavior has already changed.

**What this buys.** A compact scale-law lens: declare the scale variables, ScaleWindow, probe points, elasticity class, parity notes, and policy thresholds before treating a scale claim as usable in selection, parity, refresh, shipping, or mathematical-lens work.

**One‑screen purpose (manager‑first).**
Make **generation/selection** scale‑savvy: at the level of **conceptual descriptors**, declare (a) **which monotone knobs** we would scale, (b) the **ScaleWindow** over which we claim behaviour, and (c) the **elasticity class** we observed—**without** imposing numeric fits or vendor tools at Core level. This surfaces knees early and keeps comparisons lawful and fair across families. (Parity is handled by **G.9**; illumination remains a **report-only telemetry** unless a CAL policy promotes it.)

**Builds on.** C.16 (MM‑CHR), C.17 (Creativity‑CHR), and C.18 (NQD‑CAL); resource-use and work-cost claims use A.15.1, A.15.2, B.1.6, C.16, and A.10 as applicable. Planned C.5 (Resrc-CAL) may later consolidate that guidance but supplies no current governing semantics.
**Coordinates with.** C.19 (E/E‑LOG), G.5 (Selector & Registry), G.9 (Parity Harness), G.10 (Shipping), G.11 (Refresh‑Telemetry), C.24 (Agent‑Tools‑CAL).
**Keywords.** scaling law; **Scale Variables (S)**; ScaleWindow; knee; diminishing returns; **iso‑scale parity**; **UNM/NormalizationMethod‑based mapping**; **scale‑probe**; **DoE** (design‑of‑experiments); segmented regression; knee detection.

