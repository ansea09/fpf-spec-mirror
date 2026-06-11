---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh & Decay Orchestrator"
section_id: "G.11:11"
section_title: "SoTA-Echoing — Post‑2015 practices aligned (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__012_sota-echoing-post-2015-practices-aligned-informative.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "G.11 — Telemetry-Driven Refresh & Decay Orchestrator"
  - "G.11:11 — SoTA-Echoing — Post‑2015 practices aligned (informative)"
line_start: 81936
line_end: 81969
dependencies:
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
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

1. **Continuous refresh is necessary in deployed evaluation pipelines.**
   Practice: production ML systems use monitoring + retraining / reevaluation triggers and insist on reproducibility hooks.
   Source: Breck et al., *The ML Test Score* (2017); Amershi et al., *Software Engineering for Machine Learning* (2019).
   Alignment: `G.11` formalizes triggers as typed causes and forces edition/policy pins for replay.
   Adoption: **Adopt/Adapt** (adapted to id-based, PathSlice-scoped refresh rather than “retrain everything”).

2. **Non-stationarity requires explicit drift/decay handling, not ad-hoc updates.**
   Practice: continual learning emphasizes non-stationarity as a first-class maintenance condition.
   Source: Parisi et al., *Continual Lifelong Learning with Neural Networks* (2019); De Lange et al., *A Continual Learning Survey* (2021).
   Alignment: `B.3.4` supplies decay semantics; `G.11` wires decay events into refresh planning and controlled deprecation.
   Adoption: **Adapt** (refresh of conceptual artefacts and evidence closures, not untracked model mutation).

3. **Quality-Diversity requires archive semantics and comparability under descriptor/distance evolution.**
   Practice: QD methods treat the archive as the primary result and track changes under policy/edition conditions.
   Source: contemporary QD families such as CMA‑ME (post‑2018) and differentiable QD lines (post‑2019).
   Alignment: QD-specific meaning lives with the governing patterns; `G.11:Ext.QDRefreshWiring` ensures edition pins and scope pins exist so targeted archive refresh is admissible.
   Adoption: **Adopt** (set/archive preservation; no covert scalarization).

4. **Open-endedness co-evolves environments and agents; transfer rules must be versioned.**
   Practice: POET-class open-ended systems require explicit transfer rules and environment validity constraints.
   Source: Wang et al., POET (2019) and subsequent POET extensions (2020+).
   Alignment: `G.11:Ext.OEERefreshWiring` requires `TransferRulesRef.edition` and scope pins so refresh reruns remain comparable and auditable.
   Adoption: **Adopt/Adapt** (adapted to Part‑G pin/UTS publication discipline).

5. **Efficient orchestration benefits from bandit/early-stopping scheduling—but it must not become semantics.**
   Practice: modern hyperparameter/experiment scheduling uses bandit-style resource allocation and asynchronous early stopping.
   Source: Async Hyperband / BOHB-style work (2018+) as representative post‑2015 scheduling practice.
   Alignment: scheduling is expressed as `G.11` queue/plan policy pins (`RefreshPriorityPolicyIdRef`, `BudgetDeclRef`) so core semantics remain stable and WorkPlanning stays separate from executed Work.
   Adoption: **Adapt** (useful practice, but quarantined outside core norms).

