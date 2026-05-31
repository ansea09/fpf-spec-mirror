---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:9"
section_title: "Common anti-patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__012_common-anti-patterns.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:9 — Common anti-patterns"
line_start: 52126
line_end: 52136
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.8"
  - "J.4"
keywords:
---

### C.30.P:9 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Diagram-as-architecture | A diagram, graph, dashboard, ADR, or generated view is said to be the architecture. | Recover publication/carrier/view/source role and then apply `C.30` or `C.30.ASV` only if the architecture claim or structural view is live. |
| Architecture-as-proof | Architecture wording carries evidence, assurance, causal proof, gate passage, release permission, or decision authority. | Exit to `A.10`, `B.3`, `C.28`, `A.20`, `A.21`, `C.11`, release, or exact pattern. |
| Function-as-default-architecture | Any function, functional block, interface, or module behavior is treated as architecture. | Use `A.6.F` and `C.30.ASV` functional-structure, TGA-flow, `A.6.M` module/interface, or exact quality pattern. |
| Score-as-architecture | A score, metric, benchmark, or quality coordinate is used as architecture adequacy. | Apply `C.16.P` and the exact measurement, characteristic-space, Q-bundle, pattern-quality, gate, or benchmark pattern. |
| Viewpoint-as-structure-kind | A viewpoint label is used as if it selected structure kind. | Use `C.30.ASV`; recover structure kind and viewpoint separately. |
| Repair registry duplication | `A.22`, `C.30`, `C.30.ASV`, or an exact `C.30.*` host copies architecture/structure first-stage repair lists. | Keep the subject invariant there and use one thin pointer to `C.30.P`. |

