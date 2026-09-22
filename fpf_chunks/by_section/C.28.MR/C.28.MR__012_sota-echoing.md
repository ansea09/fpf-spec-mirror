---
chunk_kind: "child"
pattern_id: "C.28.MR"
pattern_title: "Derive an Intervention Consequence by Mechanism Replacement"
section_id: "C.28.MR:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.MR/C.28.MR__012_sota-echoing.md"
commit_sha: "3e9ea496420256ac09257c024b3120fcbc762b81"
heading_path:
  - "C.28.MR — Derive an Intervention Consequence by Mechanism Replacement"
  - "C.28.MR:11 — SoTA-Echoing"
line_start: 62843
line_end: 62852
dependencies:
  - "A.3.3.TR"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.28"
  - "C.29.1"
keywords:
---

### C.28.MR:11 - SoTA-Echoing

The [corrected Pearl, Glymour and Jewell primer, p.55](https://bayes.cs.ucla.edu/PRIMER/mueller-edits-questions-pearl-etal-2016-primer-errata-pages-august2019.pdf) provides the classical mechanism-replacement account and explains why an intervention with additional direct effects needs a richer model. It supports the ordinary constant-intervention construction here.

[Bongers, Forré, Peters and Mooij (2021), *Foundations of Structural Causal Models with Cycles and Latent Variables*](https://arxiv.org/html/1611.06221v6), particularly :2.4 and :3.4, shows that solvability can change under intervention. The model transformation and its induced distribution therefore need separate consideration. Its perfect-intervention results do not automatically establish the properties of every replacement policy.

[Zane et al. (2025), *A Counterfactual Semantics for Hybrid Dynamical Systems*](https://proceedings.neurips.cc/paper_files/paper/2025/file/21e7127fed68ca30862a008d6b50718d-Paper-Conference.pdf), :3-4, treats instantaneous, state-triggered interventions as transformations of flow and jump constraints. Under stated assumptions it preserves existence, uniqueness and measurability over the modeled horizon. This informs the event and solvability boundary; it does not impose one hybrid-system formalism on every causal query.

The synthesis retains ordinary substitution as the small executable case, adds the solution question where it matters, and connects the result to the subject interpretation. Domain-specific causal discovery, identification and estimator choices remain governed by their methods and evidence through C.28.

