---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:12.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__015_sota-echoing.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:12.1 — SoTA-Echoing"
line_start: 62211
line_end: 62221
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:12.1 - SoTA-Echoing

Wolpert and Macready's ["No Free Lunch Theorems for Optimization"](https://doi.org/10.1109/4235.585893), 1997, remains historical lineage for the warning that method superiority is distribution-dependent. It does not by itself supply the current C.22 field set, a selector policy, or evidence that one TaskSignature is adequate. The following sources inform different parts of this task-typing use.

| Source and scope | Contribution | Use boundary |
| --- | --- | --- |
| Roger Jiao, ["Towards rigorous problem formulation for engineering design research: from motivations to measurable claims via metric-measure-method"](https://doi.org/10.1080/09544828.2026.2633289), *Journal of Engineering Design* 37, 2026; Szajnfarber, Lifshitz and Tushman, ["Beyond translation: how context work during problem formulation enables effective solving by outsiders"](https://doi.org/10.1080/09544828.2026.2633491), 2026. | Formulate the problem before selecting a method; connect operational characteristics and measures to the decision or action that will use them. In C.22 this supports the task/work target, declaration content and distinct problem-side and receiving-use participants. | Engineering research formulation and outsider problem solving do not establish FPF kinds or a universal signature schema. An available method or dataset does not determine the task declaration. |
| Cenikj, Kudela, Tuba and Eftimov, ["Evaluating Real-World Generalizability of Algorithm Selection Models"](https://arxiv.org/abs/2606.02016), June 2026. | Problem characteristics inform selection, while transfer from benchmark to real-world landscapes may fail. Preserve scope, unknowns and the evidence or currentness basis consumed by the use; reopen a prior selector result only when its dependency changed. | The optimization-landscape study supplies neither a universal transfer-failure claim nor a complete TaskSignature field list for every sector. |
| Qin et al., ["A survey on Quality-Diversity optimization: Approaches, applications, and challenges"](https://doi.org/10.1016/j.swevo.2025.102240), *Swarm and Evolutionary Computation* 100, 2026; Lin et al., ["Quality-Diversity Optimization as Multi-Objective Optimization"](https://arxiv.org/abs/2602.00478), 2026 preprint. | QD uses collection-valued results, declared behavior/characteristic spaces, containers and policies. Its optional signature fields preserve the declared dominance rule, archive basis and separate telemetry; the MOO treatment is one approach. | The sources do not define all QD through MOO or authorize every diversity measure to enter dominance. A different container, metric or scalarization needs its own applicable comparison and policy basis. |
| SciML, ["Problem Interface"](https://docs.sciml.ai/DiffEqDocs/stable/basics/problem/) and ["Common Solver Options"](https://docs.sciml.ai/DiffEqDocs/stable/basics/common_solver_opts/). | Separate the constructed problem value from solver dispatch and explicitly remake it when fields change. For C.22, apply identity/membership/continuity checks to semantic declaration changes and recheck an assignment whose participant changed. | This software interface supplies no transdomain ontology and does not require every project to use an immutable software record. A material interface change reopens only the adaptation that relies on it. |

