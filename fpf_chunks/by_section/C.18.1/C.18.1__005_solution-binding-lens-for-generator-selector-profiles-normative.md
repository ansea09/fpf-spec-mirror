---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:4"
section_title: "Solution — binding lens for generator/selector profiles (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__005_solution-binding-lens-for-generator-selector-profiles-normative.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:4 — Solution — binding lens for generator/selector profiles (normative)"
line_start: 45782
line_end: 45811
dependencies:
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

### C.18.1:4 - Solution — *binding lens for generator/selector profiles* (normative)

#### C.18.1:4.1 - Types (aliases; ΔKernel = 0).
`SLL.Profile` is an **annotation** on a `MethodFamily/Generator` or a `Selector` profile; no durable U-kinds are minted (LEX discipline).

#### C.18.1:4.2 - Fields (conceptual descriptors).

* **S — Scale Variables.** Minimal set of **monotone knobs** for the Context: `compute` (steps/tokens/FLOPs/time/energy), `data` (size/quality), `model capacity` (params/branches), `iteration budget`, **`freedom‑of‑action (FoA)`**/**environment richness**, etc. Declare **units** via **Resrc‑CAL** and bind to a **ScaleWindow**. Where training/inference trade, **name the phase** the claim concerns.
* **ScaleWindow.** Declared range of `S` values for which behaviour claims hold (editioned). This is **distinct from** **FreshnessWindow** used by parity.
* **Scale‑Probe.** At least **two** (preferably **≥ 3**) **parity‑respecting** points in `S` within the ScaleWindow, recorded with **replicates/seeds** and **CI/error bars** to support elasticity classification. Pick points via a **small factorial or Latin‑hypercube** when multiple knobs vary.
* **ElasticityClass** `χ ∈ {rising, knee, flat, declining}` — a **qualitative** class; numeric exponents/fits live in domain annexes, not Core.
* **ParityNotes.** `iso‑scale parity?` flag and **loss notes** if not achieved, plus **Bridge**, **Φ**, and **Ψ** IDs when crossing contexts; penalties affect `R` only.

#### C.18.1:4.3 - Norms (SLL).

* **SLL‑1 (Declaration).** Any profile **claiming scale behaviour SHALL** declare `S` and a **ScaleWindow** for the Context.
* **SLL‑2 (Probe).** Early investigation **SHALL** include a **scale‑probe** (≥ 2 points in `S`, with replicates/CI) and record **χ**. Multi‑knob probes **SHALL** hold unspecified knobs fixed or pinned, and disclose invariants.
* **SLL‑3 (Parity).** Where `S` is declared, comparisons **SHALL** ensure **iso‑scale parity** and lawful **UNM/NormalizationMethod‑based mapping** across heterogeneous knobs (e.g., FLOPs↔tokens) **before** comparing outcomes; **FreshnessWindows/editions** must be equal/pinned per **G.9**. Record **seeds/replicates**, ComparatorSet, and policy‑ids in telemetry/SCR.
* **SLL‑4 (Selection lens).** Within the **same Context and ScaleWindow**, if other heads (N/U/C) are tied, selectors **MAY** use illumination as a tie‑breaker, but it **SHALL NOT** change default dominance; illumination remains **report‑only telemetry** unless a CAL policy promotes it.
* **SLL‑5 (Knee test).** A **knee** is **claimed** only where a monotone rise is followed by a **statistically significant** slope drop across adjacent probe points within the ScaleWindow; thresholds (e.g., Δslope & CI level) are **policy‑defined** (E/E‑LOG) and must be cited. Absent such evidence, classify as **rising**.
* **SLL‑6 (Telemetry invariants).** Probes **SHALL** export seeds/replicates, edition pins, policy‑ids, and Resrc‑CAL units to **G.11**.

#### C.18.1:4.4 - Method — minimal SoTA probe recipe (notation‑agnostic; informative).
1) **Choose knobs** `S` that are plausibly monotone in the Context (compute/data/capacity/FoA).
2) **Pick 3–5 probe points** per active knob (edge/mid/edge) under iso‑scale parity; use a **fractional factorial** if >2 knobs.
3) **Run replicates** (≥ 3 preferred) and **bootstrap** 95% CI on the primary objective(s); log seeds.
4) **Estimate local slopes** on a log‑log grid; apply **piecewise/segmented regression** or a **knee detector** (e.g., L‑curve/Kneedle) to support `χ`.
5) **Record invariants** (pinned knobs, safety envelope) and publish **SLL.Card@Context**.
6) **If χ changes** across the window, split the ScaleWindow and re‑classify per segment.

