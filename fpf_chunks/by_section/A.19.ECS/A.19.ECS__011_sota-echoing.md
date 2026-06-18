---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction"
section_id: "A.19.ECS:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__011_sota-echoing.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction"
  - "A.19.ECS:10 — SoTA-Echoing"
line_start: 24163
line_end: 24171
dependencies:
  - "A.17-A.19"
  - "C.16"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8.ECSPF"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### A.19.ECS:10 - SoTA-Echoing

| Claim | Current practice line | Adoption in A.19.ECS | Boundary |
|---|---|---|---|
| Evaluation artifacts must declare intended use, object, criteria, and missingness before their values are useful. | Current reporting anchors: BenchmarkCards/EvalCards practice for evaluation-card structure, model-card lineage for intended-use and performance-characteristic reporting, and HELM/VHELM/AHELM-style evaluation suites for scenario, metric, raw-result, and modality-extension transparency. | `A.19.ECS` starts from evaluated object kind, use scope, contrast cases, coordinate meanings, evidence rule, and missingness rule. | It is not a benchmark harness, automated judge, or publication format by itself. |
| Multicriteria evaluation needs preserved dimensions and protected trade-offs. | Current QD overview: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026); retained design lineage: MCDA and value-focused thinking for criterion separation and trade-off visibility. | The pattern requires coordinate values, polarity or no-simple-direction value rule, protected trade-offs, status meanings, and stop or reopen conditions. | Scalarization belongs only to an neighboring pattern governing the claim or explicitly declared local method. |
| Improvement pressure can damage the intended value when the evaluation is a weak proxy. | Current proxy-risk anchors: `Goodhart's Law in Reinforcement Learning` (ICLR 2024) and current catastrophic-Goodhart reward-misspecification work (NeurIPS 2024); retained lineage: Goodhart taxonomy. | `A.19.ECS` requires evidence rules, missingness rules, protected trade-offs, and lowering/reopen conditions before a loop can treat a value as improved. | It is not an anti-measurement rule; it makes the measurement or ordinal evaluation explicit enough to be challenged. |
| OEE/NQD separates the quality side from novelty, diversity, archive, pool, and selected-set semantics. | Current QD and OEE/NQD neighbour basis: QD uses quality pressure with novelty/diversity and archive/front practice, while current FPF `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep archive, pool, selected-set, parity, and refresh semantics named by value. | The evaluation may supply `Q` values, while novelty, diversity, archive, front, pool, selected-set publication, parity, and refresh remain with neighboring pattern governing the claims. | `A.19.ECS` does not govern OEE/NQD generation, selection, archive, parity, or refresh. |

