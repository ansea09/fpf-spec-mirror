---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__002_problem-frame.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:1 — Problem frame"
line_start: 69171
line_end: 69182
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.24"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.9.DA"
  - "F.19"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:1 - Problem frame

Use `E.23` when an object version will be improved through repeated passes under a declared object-under-improvement evaluation. The object can be a pattern, `DRR`, FPF corpus object, engineering quality object, naming candidate, OEE/NQD candidate, archive/front member, selected set, parity report, refresh report, or declared transduction result, if an exact evaluation supplies values and stop meanings for that object kind.

Not this pattern when one direct quality evaluation is enough. Use `E.22` to frame one evaluation and then run the named object-under-improvement evaluation. Use `A.19.ECS` first if the needed evaluation characteristic space does not exist.

First useful move: name the object version under improvement, the exact evaluation that will re-evaluate it, the improvement aim, protected trade-offs, cost and risk account, and local stop condition.

What goes wrong if missed: teams close discharge rows instead of improving quality, retry blindly, optimize visible values while damaging protected qualities, stop forever after a local all-`5` result, or let a review recommendation become decision, work, evidence, selected-set publication, parity, or refresh by stealth.

Primary EntityOfConcern in plain terms: the repeated quality-improvement method for one object version under one declared evaluation.

