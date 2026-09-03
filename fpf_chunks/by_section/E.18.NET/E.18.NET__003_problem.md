---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__003_problem.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:2 — Problem"
line_start: 87475
line_end: 87488
dependencies:
  - "A.1.STM"
  - "A.12"
  - "A.15"
  - "A.15.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "E.11"
  - "E.11.PUA"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "F.18"
  - "U.Transfer"
keywords:
---

### E.18.NET:2 - Problem

Teams routinely connect flows that concern different objects, Work occurrences, architecture boundaries, valuation state, and change cadence. A development flow produces or changes a tool; another flow uses the tool; another evaluates the use; feedback returns to development. A manufacturing system is changed through one flow while products are made through another. A compiler is built by one toolchain and then participates in a later build.

A single picture can hide three different ontic answers:

| Working situation | What is actually selected | What to do |
| --- | --- | --- |
| Several valuations, paths, or slices share one exact TFS identity | one `TransformationFlowStructure` | stay in E.18; do not mint another structure |
| A detailed portion resolves through positions and internal `U.Transfer` occurrences of one exact parent TFS | one parent-relative `SubflowRef` | stay in E.18; return through the parent's boundary positions |
| Independently identified TFS or nested-network values are connected by exact obtaining relations across their boundaries | one `TransformationFlowStructureNetwork` | apply this pattern |

When the third case is treated as one giant TFS, local state appears global, an internal `U.Transfer` is asked to mean production, use, evaluation, feedback, correspondence, and dependency, and a change in one member appears to reidentify everything. When the first or second case is over-split into a network, the model invents members and relations that the engineering situation does not need.

