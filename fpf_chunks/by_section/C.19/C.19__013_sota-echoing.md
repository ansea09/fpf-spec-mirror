---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__013_sota-echoing.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:11 — SoTA-Echoing"
line_start: 60867
line_end: 60876
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "E.10.LRN"
  - "E.17"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "audience availability"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "publication face"
  - "publication occurrence"
  - "selector-facing declaration"
  - "sunset line"
  - "widen"
---

### C.19:11 - SoTA-Echoing

The cited editions inform different policy pressures; none supplies a default algorithm, quota or sampler. If a changed source premise affects a pool-policy claim, reopen that dependent use through G.11 while retaining unaffected results.

| Source or source family | Adopted FPF move | Rejected overread | Practitioner implication |
|---|---|---|---|
| Russo et al., `A Tutorial on Thompson Sampling`, arXiv:1707.02038v3 (2020-07-14). | Treat explore/exploit balancing as an explicit sequential policy pressure rather than one hidden winner-selection aftereffect. | Thompson sampling or any bandit algorithm becomes the default C.19 method. | A pool-policy result names the policy or lens and the change trigger; local option choice still requires `C.11`. |
| Frazier, `A Tutorial on Bayesian Optimization`, arXiv:1807.02811v1 (2018-07-08), and Yu et al., `Efficient and Principled Scientific Discovery through Bayesian Optimization: A Tutorial`, arXiv:2604.01328v3 (2026-04-07). | Keep acquisition, cost, uncertainty, and experiment-selection pressure visible when pool policy is used for expensive probing. | Bayesian optimization vocabulary locally redefines FPF choice, work, or evidence kinds. | Use BO-style source pressure to require policy ids, evidence/cost boundaries, and stop or change triggers, while comparison and enactment stay with their subject patterns. |
| Qin et al., `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI `10.1016/j.swevo.2025.102240`, `https://www.sciencedirect.com/science/article/pii/S2210650225003979`. | Preserve live front, archive, coverage, and diversity pressure without collapsing them to one scalarized winner. | QD taxonomy redefines the archive and front relations stated through C.18, redefines the G.5 selected-set result, or authorizes a default family quota, DPP sampler, or max-min rule. | Keep `keep_frontier`, `narrow_to_subset`, and `sunset_line` distinct; use `C.18` for archive and front meaning, `G.5` for result declaration, and a profile admitted by the applicable policy for any heterogeneity rule. |

