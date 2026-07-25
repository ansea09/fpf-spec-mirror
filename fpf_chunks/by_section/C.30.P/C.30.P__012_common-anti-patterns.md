---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:9"
section_title: "Common anti-patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__012_common-anti-patterns.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:9 — Common anti-patterns"
line_start: 59848
line_end: 59858
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.8"
  - "G.5"
keywords:
---

### C.30.P:9 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Diagram-as-architecture | A diagram, graph, dashboard, ADR, or generated view is said to be the architecture. | Recover publication, carrier, view, or source-use relation and then apply `C.30` or `C.30.ASV` only if the architecture claim or structural-view claim is being made. |
| Architecture-as-proof | Architecture wording carries evidence, assurance, causal proof, gate passage, release permission, or decision authority. | Apply `A.10`, `B.3`, `C.28`, `A.20`, `A.21`, `C.11`, release, or the pattern governing the claim being made. |
| Function-as-default-architecture | Any function, interface, module behavior, or source label such as block is treated as architecture. | Use `C.30.STRAT` for source-label recovery where needed, then `A.6.F`, `C.30.ASV` functional-structure, `C.30.TFS-REL` transformation-flow structure relation, `A.6.M` module-relation repair, or quality pattern governing the claim. |
| Score-as-architecture | A score, metric, benchmark, or quality coordinate is used as architecture adequacy. | Apply `C.16.P` and the measurement named by value, characteristic-space, Q-bundle, pattern-quality, gate, or benchmark pattern. |
| Viewpoint-as-structure-kind | A viewpoint label is used as if it selected structure kind. | Use `C.30.ASV`; recover structure kind and viewpoint separately. |
| Repair registry duplication | `A.22`, `C.30`, `C.30.ASV`, or a named `C.30.*` host copies architecture or structure first-stage repair lists. | Keep the subject invariant there and use one thin pointer to `C.30.P`. |

