---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Transformer and Transformed Architecture Correspondence"
section_id: "C.32.CONWAY:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__003_problem.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.32.CONWAY — Transformer and Transformed Architecture Correspondence"
  - "C.32.CONWAY:2 — Problem"
line_start: 59995
line_end: 60004
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "G.5"
keywords:
  - "Conway correspondence"
  - "changing relation"
  - "coordination cost"
  - "inverse Conway maneuver"
  - "selected-structure correspondence"
  - "transformed holon"
  - "transformer holon"
---

### C.32.CONWAY:2 - Problem

Architecture synthesis often crosses a changing relation. A manufacturing system changes a product. A design organization changes a system design. A method family changes documents and work products. An AI-agent toolchain changes project work. A school changes student capabilities. A hospital triage organization changes patient-flow states. In each case, the architecture of the changing holon can make some transformed-holon architectures cheap, slow, brittle, feasible, infeasible, evolvable, or hard to certify.

Conway's law and the mirroring hypothesis make this pressure visible, but they do not replace architecture synthesis. The recurring engineering failure is that a desired transformed-holon architecture is synthesized without recovering whether the changing holon's work, communication, toolchain, manufacturing, certification, operational, or evidence structures can produce and evolve it. The result is predictable: the candidate looks architecturally clean, then independent change, deployability, testability, certification, or maintenance collapses into cross-team and cross-structure coordination work.

The inverse Conway maneuver is also an architecture candidate change, not a slogan. It means deliberately changing selected structures of the changing holon so that the desired changed-holon architecture becomes feasible and maintainable. Sometimes the stronger candidate changes the transformed-holon architecture instead. Often the honest candidate changes both and records the new burden.

C.32.CONWAY makes the correspondence explicit enough to prepare comparison inputs without collapsing the two sides.

