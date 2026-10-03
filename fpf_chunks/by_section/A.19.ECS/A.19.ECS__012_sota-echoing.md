---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction: Define What Counts as Better"
section_id: "A.19.ECS:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__012_sota-echoing.md"
commit_sha: "51fc062ab576f61d48174286011e2aa4c2dd4f54"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction: Define What Counts as Better"
  - "A.19.ECS:10 — SoTA-Echoing"
line_start: 32665
line_end: 32675
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
| Improvement concern can damage the intended value when the evaluation is a weak proxy. | Current proxy-risk anchors: `Goodhart's Law in Reinforcement Learning` (ICLR 2024) and current catastrophic-Goodhart reward-misspecification work (NeurIPS 2024); retained lineage: Goodhart taxonomy. | `A.19.ECS` requires evidence rules, missingness rules, protected trade-offs, and lowering/reopen conditions before a loop can treat a value as improved. | It is not an anti-measurement rule; it makes the measurement or ordinal evaluation explicit enough to be challenged. |
| OEE and NQD work keeps the quality side distinct from novelty, diversity, archive, pool, and selected-set semantics. | Current QD, OEE, and NQD neighbour basis: quality-diversity work evaluates quality together with novelty and diversity, while archive and front are separate relations. Use `C.17` for novelty and diversity retention, `C.18` for archive and front relations, `C.19` for pool treatment, `G.5` for selected-set result declaration, `G.9` for parity, and `G.11` for currentness and refresh. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. | An evaluation may supply `Q` values. It does not thereby establish neighboring search, selection, retention, currentness, or publication claims. Examples include novelty, diversity, archive, front, pool, selected-set, parity, refresh, and publication claims; apply the named definitions and tests only when the corresponding claim is current. | `A.19.ECS` constructs an evaluation `U.CharacteristicSpace`; using it neither performs nor establishes OEE or NQD generation, selection, archive, publication, parity, or refresh. |
| Evaluator quality must be connected to the decisions it improves. | Kim et al., [*Rethinking Reward Model Evaluation Through the Lens of Reward Overoptimization*](https://arxiv.org/abs/2505.12763v1) (2025), studies reward-model evaluation in bounded mathematical tasks. HCD.18/.19 and ME.14 supply developed FPF domain treatments of criterion error, support conditions and comparative practical worth. | **Adapt:** §4.5 compares missed defects, admissible difficult cases, proposed repairs and cost. This cross-domain construction requires its own subject grounds; the domain methods remain examples, not Core authority. | Reward-model correlation, evaluator agreement and a better specification do not establish general decision usefulness. Reopen when a target use cannot obtain the independent basis the comparison needs. |
| Adaptive reuse can turn adoption cases into tuning material. | Dwork et al., [*Generalization in Adaptive Data Analysis and Holdout Reuse*](https://arxiv.org/abs/1506.02629) (2015), is statistical lineage; Iacob et al., [*The Red Queen Gödel Machine*](https://arxiv.org/abs/2606.26294v2) (2026), is current bounded research on evolving evaluation. | **Adapt:** separate known-case development from independent adoption, preserve scope and expose cost in §4.5. | Neither statistical holdout guarantees nor benchmark improvement transfers automatically to qualitative framework evaluation. Reopen if leakage, a new population or comparison burden defeats the intended use. |

