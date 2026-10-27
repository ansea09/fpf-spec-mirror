---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:4"
section_title: "Solution — binding lens for generator/selector profiles (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__005_solution-binding-lens-for-generator-selector-profiles-normative.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:4 — Solution — binding lens for generator/selector profiles (normative)"
line_start: 60373
line_end: 60402
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

### C.18.1:4 - Solution — *binding lens for generator/selector profiles* (normative)

#### C.18.1:4.1 - Profile annotation
`SLL.Profile` annotates a `MethodFamily/Generator` or `Selector` profile with the scale claim and its basis.

#### C.18.1:4.2 - Fields (conceptual descriptors).

* **S — Scale Variables.** Minimal set of adjustable variables with a declared order for the Context: `compute` (steps/tokens/FLOPs/time/energy), `data` (size/quality), `model capacity` (params/branches), `iteration budget`, **`freedom‑of‑action (FoA)`**/**environment richness**, etc. Declare each variable’s Characteristic and Scale, with a unit when applicable under **C.16**, and bind `S` to a **ScaleWindow**. Ordering the input does not assume a monotone improvement in the outcome; do not treat qualitative data quality or freedom of action as a ratio quantity without that measurement basis. Keep planned budget values with **A.15.2**; bind dated resource-use accounts to **A.15.1**, **B.1.6**, and **A.10**. Where training/inference trade, **name the phase** the claim concerns.
* **ScaleWindow.** Declared range of `S` values for which behaviour claims hold (editioned). This is **distinct from** **FreshnessWindow** used by parity.
* **Scale‑Probe.** At least **two** (preferably **≥ 3**) **parity‑respecting** points in `S` within the ScaleWindow, recorded with **replicates/seeds** and **CI/error bars** to support elasticity classification. Pick points via a **small factorial or Latin‑hypercube** when multiple knobs vary.
* **ElasticityClass** `χ ∈ {rising, knee, flat, declining}` — a **qualitative** class supported by the probe over the declared ScaleWindow. Leave `χ` unassigned when the observations and their uncertainty do not support a class, and state what remains unresolved. Numeric exponents/fits live in domain annexes, not Core.
* **ParityNotes.** `iso‑scale parity?` flag and **loss notes** if not achieved, plus applicable **Bridge**, **Φ**, and **Ψ** IDs for actual crossings under **G.9**; penalties affect `R` only.

#### C.18.1:4.3 - Norms (SLL).

* **SLL‑1 (Declaration).** Any profile **claiming scale behaviour SHALL** declare `S` and a **ScaleWindow** for the Context.
* **SLL‑2 (Probe).** A scale-behavior investigation **SHALL** use an applicable **scale‑probe** (≥ 2 points in `S`, with replicates/CI) and record the supported **χ**, or the unresolved classification. An existing probe may supply this basis while its window, definitions and conditions remain applicable. Multi‑knob probes **SHALL** hold unspecified knobs fixed or pinned, and disclose invariants.
* **SLL‑3 (Parity).** A comparison claiming matched scale **SHALL** establish **iso‑scale parity**. When heterogeneous knobs such as FLOPs and tokens require a mapping, apply a justified **UNM/NormalizationMethod** mapping **before** comparing outcomes under **G.9**; their names alone supply no conversion. Keep **FreshnessWindows/editions** equal/pinned as required by G.9. If iso-scale parity cannot be established, state the loss and restrict the comparison to what its applicable rule admits. Loss notes alone do not make an otherwise unsupported comparison admissible. Record **seeds/replicates**, ComparatorSet and applicable policy ids in telemetry/SCR.
* **SLL‑4 (Selection lens).** Within the **same Context and ScaleWindow**, if novelty, use value and constraint fit are tied, selectors **MAY** use illumination as a tie-breaker when an applicable pinned policy admits that bounded use. This **SHALL NOT** change default dominance. Promotion into dominance needs its own explicit CAL policy; otherwise illumination remains report-only telemetry.
* **SLL‑5 (Knee test).** A **knee** is **claimed** only where a monotone rise is followed by a **statistically significant** slope drop across adjacent intervals formed by at least three distinct probe points within the ScaleWindow; thresholds (e.g., Δslope & CI level) are **policy‑defined** (E/E‑LOG) and must be cited. Failure to establish a knee leaves that claim unsupported. Report **rising**, **flat** or **declining** only when the probe supports that class; otherwise leave **χ** unassigned. Absence of a confirmed knee is not evidence of rising performance.
* **SLL‑6 (Telemetry invariants).** Probes **SHALL** export seeds/replicates, edition pins, policy‑ids, and resource-account units governed by **C.16** and **B.1.6**, with dated-work and provenance links under **A.15.1** and **A.10**, to **G.11**.

#### C.18.1:4.4 - Method — minimal SoTA probe recipe (notation‑agnostic; informative).
1) **Choose ordered scale variables** `S` for the Context, such as compute, data, capacity or FoA, under their declared measurement basis.
2) **Pick 3–5 probe points** per active knob (edge/mid/edge) under iso‑scale parity; use a **fractional factorial** if >2 knobs.
3) **Run replicates** (≥ 3 preferred) and **bootstrap** 95% CI on the primary objective(s); log seeds.
4) **Estimate local slopes** on a log‑log grid only where the declared Scale operations are admissible under **A.18** and the logged values are positive; apply **piecewise/segmented regression** or a **knee detector** (e.g., L‑curve/Kneedle) to support `χ`.
5) **Record invariants** (pinned knobs, safety envelope). Use **SLL.Card@Context** to keep the account reusable; an adequate existing account need not be recopied.
6) **If χ changes** across the window, split the ScaleWindow and re‑classify per segment.

