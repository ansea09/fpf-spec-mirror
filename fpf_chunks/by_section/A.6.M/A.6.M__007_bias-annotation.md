---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__007_bias-annotation.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:6 — Bias-Annotation"
line_start: 18722
line_end: 18733
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.B"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.RSA"
  - "E.18"
  - "E.20"
  - "G.5"
keywords:
  - "are used only for pattern users"
  - "claims"
  - "component"
  - "conformance items"
  - "evidence records"
  - "interface"
  - "interface specification"
  - "layer"
  - "module relation"
  - "open architecture"
  - "or assurance records. Modeled modules and interfaces are not written as agents with duties"
  - "or publication records"
  - "platform"
  - "port"
  - "records"
  - "stack"
  - "substitutability"
---

### A.6.M:6 - Bias-Annotation

| Bias risk | A.6.M repair |
| --- | --- |
| Box bias | Do not treat a diagram box as a module. Recover holon, whole, boundary, and interface specification. |
| Open-label bias | Do not treat "open" as substitutability. Recover standards, conformance expectations, data or access constraints, and change policy when those conditions are part of the claim being made. |
| Component bias | Do not treat every part as a module. Apply A.14 to component wording unless a module-interface relation is being claimed. |
| Interface-label bias | Do not treat API, port, endpoint, or signature labels as implemented compatibility. Recover `InterfaceSpecificationRef`. |
| Team-boundary bias | Do not treat Conway-like mirroring, team responsibility, team communication boundary, or delivery-unit labels as module boundaries. Recover role-assignment, responsibility, work, and procedural relations first; add module-interface correspondence only when the boundary and interface specification are declared. |
| Parallelism bias | Do not treat decomposition into more modules, teams, services, or transformation-flow paths as performance or evolvability improvement. Recover serial work, synchronization, communication overhead, shared resources, and bottleneck claims through `E.18`, `C.30.TFS-REL`, C.29, C.31, or neighboring characteristic patterns when those claims are being made. |
| Platform bias | Do not treat a platform name as architecture quality. Recover platform grammar and the claim named by value it can substantiate. |

