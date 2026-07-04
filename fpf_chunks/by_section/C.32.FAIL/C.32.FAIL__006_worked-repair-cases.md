---
chunk_kind: "child"
pattern_id: "C.32.FAIL"
pattern_title: "Architecture Failure Recognition and Repair"
section_id: "C.32.FAIL:5"
section_title: "Worked Repair Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.FAIL/C.32.FAIL__006_worked-repair-cases.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.32.FAIL — Architecture Failure Recognition and Repair"
  - "C.32.FAIL:5 — Worked Repair Cases"
line_start: 61048
line_end: 61063
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.P"
  - "C.31"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.24.PUB"
  - "G.5"
keywords:
  - "architecture failure cue"
  - "architecture repair cue"
  - "candidate repair"
  - "repair-entry family"
  - "selected-structure relation"
  - "source overread"
  - "stressed architecture object"
---

### C.32.FAIL:5 - Worked Repair Cases

**Tell.** C.32.FAIL is a repair-entry pattern. It takes a recognizable warning cue and returns one typed repair action over a selected architecture object. It is useful only when the repair action changes architecture handling.

**Show-A - Safety-relevant model-as-module.** A model file is being treated as a module in a product architecture. The repair cue names the candidate module-interface relation, blocks the file-equals-module overread, and recovers interface behavior, admissible-use conditions, change policy, and evidence-decay boundary. Safety assurance follows only through its governing pattern.

**Show-B - Product-family platform with exception growth.** A platform promise reduces local delivery effort but grows evidence exceptions at the product-family scope. The repair cue names variation structure, substitution policy, and evidence scope as the architecture objects under stress. The first repair action is not to declare the platform adequate; it is to repair variation slots and bounded-exception rules, then open `C.32.MLAO` residual comparison if cross-scope burden is current.

**Show-C - Responsibility change shifts coordination cost.** A stream-aligned team improves local delivery flow, but release testing and evidence responsibility remain shared. The repair cue names the shifted coordination cost, keeps role-enactor and work structures distinct from module-interface and evidence structures, and asks whether the candidate should change transformer-side work, transformed-side module interfaces, evidence scope, or all three.

**Show-D - Generated architecture candidate.** An agent system produces a high-scoring blueprint. The repair cue treats the blueprint as a source cue, recovers the selected-structure changes encoded in it, names preserved and lost structure, and rebuilds the candidate palette before G.5 publication of a selected set or decision.

**Show-E - Built-asset maintenance dashboard.** A facility maintenance dashboard shows a dependency graph and freshness scores. The repair cue keeps the graph as a lens output, recovers the actual selected structures under stress in maintenance work and asset interfaces, and keeps timing or evidence claims with their governing patterns.

**Show-F - Function with no feasible bearer.** A searched AI workflow adds a verification function after model output, but the edge device has no resource margin and the cloud placement violates latency. The repair cue names the function-bearing gap, then returns to C.32: add a local bearer, split verification into local and cloud steps, change deployment placement, reduce the demand, or reject the candidate for the current evolution window.

