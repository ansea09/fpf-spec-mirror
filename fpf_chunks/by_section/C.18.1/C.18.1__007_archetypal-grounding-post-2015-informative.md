---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:9"
section_title: "Archetypal Grounding (post-2015; informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__007_archetypal-grounding-post-2015-informative.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:9 — Archetypal Grounding (post-2015; informative)"
line_start: 61382
line_end: 61391
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

### C.18.1:9 - Archetypal Grounding (post-2015; informative)

* **LLM scaling.** Historical Kaplan-style and **Chinchilla-optimal** regimes illustrate different compute/data allocations. **Mixture-of-Experts** and **retrieval-augmented** families require their own capacity and inference-budget account.
* **RL/Planning.** Model-based optimization & general agents vs hand-tuned controllers; slopes reported wrt budget/FoA under safety envelopes.
* **QD/OEE.** MAP-Elites, **CMA-ME**, **DQD**, **QDax**; **POET/Enhanced-POET** families: coverage/illumination as telemetry metrics; parity uses fixed grids/spaces and edition pins.

**Constructed classification case.** A matched-probe account supports unchanged performance across the declared resource window, with uncertainty small enough for the comparison's stated tolerance. Report `flat`; the absence of a knee does not turn it into `rising`. In a second account, the uncertainty still permits both an increase and a decrease that would matter to the choice. Leave `χ` unassigned and retain that limitation. A supported monotone increase without a confirmed slope drop can instead support `rising`. These supplied accounts illustrate classification and its limit; they are not empirical scaling results.

**Constructed bounded-error knee.** At resource counts `1, 2, 3`, deterministic throughputs are `10, 18, 19`, each with absolute error at most `0.1`, under the same tested conditions and admissible linear scales. The first adjacent slope is in `[7.8, 8.2]`; the second is in `[0.8, 1.2]`. Both rises are positive and the slope drop is in `[6.6, 7.4]`. A declared drop threshold of `5` is therefore exceeded throughout these bounds, supporting a knee over these three probe counts. No interpolation beyond the admitted counts is claimed. If wider error bounds admit a drop of `5` or less, this knee conclusion is no longer established; use only the behavior class still supported by those observations and bounds.

