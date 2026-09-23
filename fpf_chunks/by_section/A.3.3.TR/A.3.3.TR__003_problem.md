---
chunk_kind: "child"
pattern_id: "A.3.3.TR"
pattern_title: "Construct a Rule for State Change"
section_id: "A.3.3.TR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.TR/A.3.3.TR__003_problem.md"
commit_sha: "4ddaf71557d4159e988cc61d2bd3088bfc1d2803"
heading_path:
  - "A.3.3.TR — Construct a Rule for State Change"
  - "A.3.3.TR:2 — Problem"
line_start: 9876
line_end: 9883
dependencies:
  - "A.22.CGUS"
  - "A.3.3"
  - "A.3.3.CC"
  - "B.5.FM"
  - "B.5.MPC"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.TR:2 - Problem

A state constraint and a transition rule answer different questions. Two connected carts may have to maintain a fixed separation; that condition permits many common accelerations. Forces and masses are needed to select one. Similarly, saying that a participant reads before it writes constrains local order but leaves several global execution orders possible.

A rule assembled from separately plausible statements can also be inconsistent or too permissive. An omitted unchanged value may become free to vary. Combining alternatives as if they had to occur together can eliminate legitimate behavior. Treating a desired invariant as an automatic filter can hide the very failure the model was meant to investigate.

The practical problem is to construct a connected account from which the needed changes follow, while keeping visible the choices and missing information that still affect the answer.

