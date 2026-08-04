---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__004_problem.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:2 — Problem"
line_start: 33615
line_end: 33625
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransformationFlowStructure"
  - "flow"
---

### A.20:2 - Problem

Without a clear CV core:

* internal step laws (declared domains and ranges, invariants, units coherence, and Lipschitz-bound or stability claims) are mistaken for `GateProfile` fit;
* plane or comparator declarations sneak into mechanisms;
* freshness and DesignRunTag concerns appear inside mechanisms;
* reproducibility suffers because transfers start carrying hidden semantics beyond `⟨L,P,E⃗,D⟩`.

Under this pattern, CV is evaluated **inside** transformations. **If** a check declares planes, units, or comparators or depends on a declared `GateProfile`, **then** it is treated as **GateFit at gates** and the CV explanation **does not apply**.

