---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__017_sota-echoing.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:11 — SoTA-Echoing"
line_start: 49753
line_end: 49760
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
  - "sunset line"
  - "widen"
---

### C.19:11 - SoTA-Echoing

| Source or source family | Adopted FPF move | Rejected overread | Practitioner implication |
|---|---|---|---|
| Russo et al., `A Tutorial on Thompson Sampling`, arXiv:1707.02038. | Treat explore/exploit balancing as an explicit sequential policy pressure rather than one hidden winner-selection aftereffect. | Thompson sampling or any bandit algorithm becomes the default C.19 method. | A pool-policy result names the policy or lens and the change trigger; local option choice still exits to `C.11`. |
| Frazier, `A Tutorial on Bayesian Optimization`, arXiv:1807.02811, and Yu et al., `Efficient and Principled Scientific Discovery through Bayesian Optimization`, arXiv:2604.01328. | Keep acquisition, cost, uncertainty, and experiment-selection pressure visible when pool policy is used for expensive probing. | Bayesian optimization vocabulary locally redefines FPF choice, work, or evidence kinds. | Use BO-style source pressure to require policy ids, evidence/cost boundaries, and stop or change triggers, while comparison and enactment stay with their owners. |
| Qin et al., `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI `10.1016/j.swevo.2025.102240`, `https://www.sciencedirect.com/science/article/pii/S2210650225003979`. | Preserve live front, archive, coverage, and diversity pressure without collapsing them to one scalarized winner. | QD taxonomy replaces C.18 archive/front ownership or G.5 selected-set publication. | Keep `keep frontier`, `narrow to subset`, and `sunset line` distinct; archive/front meaning stays with `C.18`, publication with `G.5`. |

