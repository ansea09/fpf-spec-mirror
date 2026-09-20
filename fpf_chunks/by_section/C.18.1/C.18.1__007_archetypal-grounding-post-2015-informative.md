---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:9"
section_title: "Archetypal Grounding (post-2015; informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__007_archetypal-grounding-post-2015-informative.md"
commit_sha: "1fa007d1110d961d54ced2fa58e08177663c401f"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:9 — Archetypal Grounding (post-2015; informative)"
line_start: 55583
line_end: 55590
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

### C.18.1:9 - Archetypal Grounding (post-2015; informative)

* **LLM scaling.** Kaplan-style & **Chinchilla-optimal** regimes; **Mixture-of-Experts** and **retrieval-augmented** families shift effective capacity with different inference budgets; prompt-policies often transfer better than narrow pipelines.
* **RL/Planning.** Model-based optimization & general agents vs hand-tuned controllers; slopes reported wrt budget/FoA under safety envelopes.
* **QD/OEE.** MAP-Elites, **CMA-ME**, **DQD**, **QDax**; **POET/Enhanced-POET** families: coverage/illumination as telemetry metrics; parity uses fixed grids/spaces and edition pins.

**Constructed classification case.** A matched-probe account supports unchanged performance across the declared resource window, with uncertainty small enough for the comparison's stated tolerance. Report `flat`; the absence of a knee does not turn it into `rising`. In a second account, the uncertainty still permits both an increase and a decrease that would matter to the choice. Leave `χ` unassigned and retain that limitation. A supported monotone increase without a confirmed slope drop can instead support `rising`. These supplied accounts illustrate classification and its limit; they are not empirical scaling results.

