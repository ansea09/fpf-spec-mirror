---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:4"
section_title: "Solution — binding lens for generator/selector profiles (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__005_solution-binding-lens-for-generator-selector-profiles-normative.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:4 — Solution — binding lens for generator/selector profiles (normative)"
line_start: 64162
line_end: 64191
dependencies:
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
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
* **ScaleWindow.** The declared range of resource settings under investigation. Identify the settings actually tested and the response, statistic, task family and conditions to which the result applies. To extend a conclusion to untested settings, state the model, bound or other grounds for that extension. `FreshnessWindow` governs the age of the evidence.
* **Scale‑Probe.** At least **two** (preferably **≥ 3**) **parity-respecting** points in `S` within the ScaleWindow, with uncertainty appropriate to the empirical claim. Use replicates, seeds and confidence intervals when the trial design and variability require them; deterministic results retain their conditions and any applicable measurement or numerical error. Pick points via a **small factorial or Latin-hypercube** when that design answers the multi-knob question.
* **ElasticityClass** `χ ∈ {rising, knee, flat, declining}` — a **qualitative** class supported by the probe at the settings supported within the declared ScaleWindow. Leave `χ` unassigned when the observations and their uncertainty do not support a class, and state what remains unresolved. Numeric exponents/fits live in domain annexes, not Core.
* **ParityNotes.** `iso‑scale parity?` flag and **loss notes** if not achieved, plus applicable **Bridge**, **Φ**, and **Ψ** IDs for actual crossings under **G.9**; any numerical assurance penalty follows its applicable B.3 model.

#### C.18.1:4.3 - Norms (SLL).

* **SLL‑1 (Declaration).** Any profile **claiming scale behaviour SHALL** declare `S` and a **ScaleWindow** for the Context.
* **SLL‑2 (Probe).** An empirical conclusion about a change with scale **SHALL** use an applicable **scale‑probe** (≥ 2 points in `S`, with the applicable uncertainty treatment in §4.2) and record the supported **χ**, or the unresolved classification. An existing probe may supply this basis while its window, definitions and conditions remain applicable. Multi‑knob probes **SHALL** hold unspecified knobs fixed or pinned, and disclose invariants. A result at one setting can establish what happened there. Repeat trials at that setting can improve the estimate for that setting. A change with scale remains open until the evidence covers distinct settings.
* **SLL‑3 (Parity).** A comparison claiming matched scale **SHALL** establish **iso‑scale parity**. When heterogeneous knobs such as FLOPs and tokens require a mapping, apply a justified **UNM/NormalizationMethod** mapping **before** comparing outcomes under **G.9**; their names alone supply no conversion. Keep **FreshnessWindows/editions** equal/pinned as required by G.9. If iso-scale parity cannot be established, state the loss and restrict the comparison to what its applicable rule admits. Loss notes alone do not make an otherwise unsupported comparison admissible. Record any **seeds/replicates** used, the uncertainty basis, ComparatorSet and applicable policy ids in telemetry/SCR.
* **SLL‑4 (Selection lens).** Within the **same Context and ScaleWindow**, if novelty, use value and constraint fit are tied, selectors **MAY** use illumination as a tie-breaker when an applicable pinned policy admits that bounded use. This **SHALL NOT** change default dominance. Promotion into dominance needs its own explicit CAL policy; otherwise illumination remains report-only telemetry.
* **SLL‑5 (Knee test).** A **knee** is claimed only when a monotone rise is followed by a slope drop across adjacent intervals formed by at least three distinct probe points within the ScaleWindow. Compare slopes along one ordered resource coordinate with other influential conditions held comparable. If several resources change together, define the path and its unit of advance, and attribute the knee to that path. The slope comparison must be admissible for the declared Scales and establish a drop exceeding the **policy-defined threshold** under the uncertainty or error treatment appropriate to the probe. For stochastic probes, assess the slope drop under the governing uncertainty rule using a method whose assumptions fit the trial design. If that rule requires a significance test, report its result and significance level. If it specifies a probability or bound on the drop, give the probability or bound and its supporting assumptions. Report the level of any interval used. For deterministic probes, establish the threshold exceedance throughout the applicable error bounds. Cite the threshold policy (E/E-LOG), comparison method and uncertainty basis. Failure to establish a knee leaves that claim unsupported. Report **rising**, **flat** or **declining** only when the probe supports that class; otherwise leave **χ** unassigned. Absence of a confirmed knee is not evidence of rising performance.
* **SLL‑6 (Telemetry invariants).** Probes **SHALL** export the uncertainty basis, any seeds/replicates used, edition pins, applicable policy ids and resource-account units governed by **C.16** and **B.1.6**, with dated-work and provenance links under **A.15.1** and **A.10**, to **G.11**.

#### C.18.1:4.4 - Method — minimal SoTA probe recipe (notation‑agnostic; informative).
1) **Choose ordered scale variables** `S` from the decision the result will inform. Identify whose resource is varied, which system or work produces the response, and the range of settings the decision must cover. When using component readings to judge a whole service, establish how their allocation, timing and interaction determine the service result. A direct service measurement or sufficient bound can settle the question. Declare the measurement basis for the selected variables.
2) Choose attainable settings that can distinguish the effects in question. Three to five settings can reveal curvature along a single ordered resource. A two-state variable permits a two-state comparison. For several resources, choose a design that can distinguish the relevant main effects and interactions.
3) For stochastic trials, choose replication and an uncertainty method adequate to the claimed trend; bootstrap intervals are one option when their assumptions fit the data. Retain the seeds used. For deterministic trials, retain the conditions and applicable error bounds.
4) Estimate the contrast needed for the claim. For a knee, use the adjacent slopes in SLL‑5. Logarithmic slopes require positive values and operations admitted by the Scales under `A.18`. A segmented fit or a knee detector can assist that comparison.
5) Record the response and statistic, task family, settings tested and conditions held fixed. Make the evidence available through the profile or `SLL.Card@Context`. An observed run demonstrates that its outcome occurred under those conditions. A feasible solution with a verified objective value supplies a lower bound when maximizing that objective. Meeting a target with a verified amount of an ordered resource supplies an upper bound on the minimum needed under the same conditions. If several resources are tracked separately, report the feasible combination. A claim about expected performance, population coverage or a required success probability needs evidence for that statistic.
6) **If χ changes** across the window, split the ScaleWindow and re‑classify per segment.

