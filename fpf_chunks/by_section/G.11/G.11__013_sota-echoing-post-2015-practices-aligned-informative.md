---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:11"
section_title: "SoTA-Echoing — Post‑2015 practices aligned (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__013_sota-echoing-post-2015-practices-aligned-informative.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:11 — SoTA-Echoing — Post‑2015 practices aligned (informative)"
line_start: 93323
line_end: 93368
dependencies:
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "C.32.P2S"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.12"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G11"
keywords:
  - "Bridge Sentinels"
  - "PathSlice"
  - "RSCR"
  - "decay"
  - "deprecation"
  - "edition bumps"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
---

### G.11:11 - SoTA-Echoing — Post‑2015 practices aligned (informative)

Each entry follows: **claim → practice → source → alignment → adoption status**.

0. **Queue-7 QD currentness requires visible survey support.**
   Practice: current QD work is surveyed as approaches, applications, and challenges, with archive, diversity, descriptor, and evaluator-currentness concerns still live.
   Source: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 2026, DOI `10.1016/j.swevo.2025.102240`.
   Alignment: `RefreshCurrentnessLine@Context` may name selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, portfolio lineage, descriptor or distance edition, and path-slice scope, while `C.18`, `C.19`, and `G.5` keep archive, pool, and selected-set meanings.
   Adoption: **Adopt and bound** (survey support changes refresh currentness fields and boundaries; it is not the governing ontology source).

0a. **Open-ended engineering outputs need source and evaluator currentness.**
   Practice: self-improving-agent, AlphaEvolve-style, and DeepEvolve-style lines use generated variants, external knowledge, evaluators, tests, archives, and empirical validation.
   Source: Darwin Godel Machine `arXiv:2505.22954`, AlphaEvolve `arXiv:2506.13131`, and DeepEvolve-style deep-research augmentation `arXiv:2510.06056`.
   Alignment: G.11 refresh records carry source, evaluator, descriptor, policy, edition, lineage, and report refs; generated method text, evaluator success, and archive update keep their governing patterns.
   Adoption: **Adopt and adapt** (refresh tracks currentness and smallest affected scope; it does not accept generated text as proof, gate passage, or performed work).

1. **Continuous refresh is necessary in deployed evaluation pipelines.**
   Practice: production ML systems use monitoring, retraining, and reevaluation triggers and insist on reproducibility hooks.
   Source: Breck et al., *The ML Test Score* (`arXiv:1706.04599`, 2017); Amershi et al., *Software Engineering for Machine Learning* (ICSE-SEIP 2019).
   Alignment: `G.11` formalizes triggers as typed causes and forces edition and policy pins for replay.
   Adoption: **Adopt and adapt** (adapted to id-based, PathSlice-scoped refresh rather than “retrain everything”).

2. **Non-stationarity requires explicit drift and decay handling, not ad-hoc updates.**
   Practice: continual learning emphasizes non-stationarity as a first-class maintenance condition.
   Source: Parisi et al., *Continual Lifelong Learning with Neural Networks* (`arXiv:1802.07569`, 2019); De Lange et al., *A Continual Learning Survey* (`arXiv:1909.08383`, 2021).
   Alignment: `B.3.4` supplies decay semantics; `G.11` wires decay events into refresh planning and controlled deprecation.
   Adoption: **Adapt** (refresh of conceptual artefacts and evidence closures, not untracked model mutation).

3. **Quality-Diversity requires archive semantics and comparability under descriptor and distance evolution.**
   Practice: QD methods treat the archive as the primary result and track changes under policy and edition conditions.
   Source: contemporary QD families such as CMA-MAE (`arXiv:2205.10752`) and differentiable QD (`arXiv:2106.03894`).
   Alignment: QD-specific meaning lives with the governing patterns; `G.11:Ext.QDRefreshWiring` ensures edition pins and scope pins exist so targeted archive refresh is admissible.
   Adoption: **Adopt** (set and archive preservation; no covert scalarization).

4. **Open-endedness co-evolves environments and agents; transfer rules must be versioned.**
   Practice: POET-class open-ended systems require explicit transfer rules and environment validity constraints.
   Source: Wang et al., POET (`arXiv:1901.01753`, 2019); later generator-family claims require a named `G.2` SoTA pack or exact current source.
   Alignment: `G.11:Ext.OEERefreshWiring` requires `TransferRulesRef.edition` and scope pins so refresh reruns remain comparable and auditable.
   Adoption: **Adopt and adapt** (adapted to Part G pin and UTS publication discipline).

5. **Efficient orchestration benefits from bandit and early-stopping scheduling, but it must not become semantics.**
   Practice: modern hyperparameter and experiment scheduling uses bandit-style resource allocation and asynchronous early stopping.
   Source: ASHA (`arXiv:1810.05934`) and BOHB (`arXiv:1807.01774`) as representative post-2015 scheduling practice.
   Alignment: scheduling is expressed as `RefreshQueue` and `RefreshPlan@Context` policy pins (`RefreshPriorityPolicyIdRef`, `BudgetDeclRef`) so core semantics remain stable and WorkPlanning stays separate from executed Work.
   Adoption: **Adapt** (useful practice, but quarantined outside core norms).

