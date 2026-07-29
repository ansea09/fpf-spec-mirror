---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__004_forces.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:3 — Forces"
line_start: 18063
line_end: 18075
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

### A.6.M:3 - Forces

| Force | Tension |
| --- | --- |
| Engineering convenience vs relation precision | Practitioners need short words such as module and interface, but claim-bearing use must recover relation kind, slots, boundary, and admissible use. |
| Module relation position vs root kind | A module is often a holon in a module-interface relation position; minting `U.Module` would hide context, viewpoint, and relation conditions. |
| Interface label vs interface specification | An API name, port label, connector label, or signature may substantiate an interface claim, but it is not by itself substitutability or conformance. |
| Function-flow-module proximity vs false identity | Functions, E.18 flow relations, control relations, mechanisms, and module interfaces often meet at the same artifact, but each has a different governing pattern. |
| Open architecture payoff vs open label overread | MOSA and open-system practice make open interfaces useful only with standards, conformance expectations, replacement or change policy, and data or access constraints when those conditions are part of the claim being made. |
| Team boundary vs module boundary | Conway's law and mirroring practice make team communication boundaries and delivery-responsibility scopes architecture-relevant, but they do not turn a team boundary, delivery unit, role assignment, or responsibility relation into a module interface by identity. |
| Parallel decomposition vs serial bottleneck | Amdahl-style reasoning makes serial work, synchronization, communication overhead, and shared resource limits visible; more modules, teams, or parallel transformation-flow paths do not automatically improve throughput or evolvability. |
| Cheap repair vs full evidence pack | Most cases need a relation repair note, not a full conformance, evidence, assurance, gate, or mechanism-suite record. |

