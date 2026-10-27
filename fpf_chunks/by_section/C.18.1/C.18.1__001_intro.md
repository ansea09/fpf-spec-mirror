---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__001_intro.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:intro — Intro"
line_start: 60507
line_end: 60522
dependencies:
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "G.10"
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
  - "elasticity class"
  - "iso‑scale parity"
  - "knee"
  - "knee detection"
  - "probe uncertainty"
  - "resolution‑elasticity"
  - "scale variables (S)"
  - "scale‑probe"
  - "scaling law"
  - "segmented regression"
---

## C.18.1 - Scaling‑Law Lens Binding (SLL)

> **Status:** Stable
> **Type:** Pattern

**Use this pattern when.** Use C.18.1 when a generator, selector, method family, benchmark, or comparison claims that behavior changes with scale—for example, with resource budget, data, model capacity, iteration budget or freedom of action. First name what is scaled, the window and the outcome being compared. Reuse an applicable probe account; new probing is needed only when the required scale claim remains unsupported. If no scale claim is needed, use the ordinary comparison directly.

**What goes wrong if missed.** Teams compare unequal budgets, call coverage telemetry an objective, claim a knee without probe evidence, or assume more scale means linear improvement across a window where the behavior has already changed.

**What this buys.** A compact scale-law lens: declare the scale variables, ScaleWindow, probe points, elasticity class, parity notes, and policy thresholds before treating a scale claim as usable in selection, parity, refresh, shipping, or mathematical-lens work.

**Purpose.** Declare which scale variables change, the ScaleWindow and the supported behavior class. Numeric fits remain domain work. G.9 governs parity, and a selector policy must admit any decision use of illumination.


**Keywords.** scaling law; **Scale Variables (S)**; ScaleWindow; knee; diminishing returns; **iso‑scale parity**; **UNM/NormalizationMethod‑based mapping**; **scale‑probe**; **DoE** (design‑of‑experiments); segmented regression; knee detection.

