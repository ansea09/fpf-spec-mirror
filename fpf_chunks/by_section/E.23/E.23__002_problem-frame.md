---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__002_problem-frame.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:1 — Problem frame"
line_start: 84640
line_end: 84654
dependencies:
  - "A.19.ECS"
  - "A.22.CGUS"
  - "C.17-C.19"
  - "C.32.P2S"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:1 - Problem frame
When the entry phrase is "loop engineering", "agent loop", "harness loop", or "improve this with an agent", treat the phrase as a recognition cue, not as an FPF kind. First recover the object version under improvement and the evaluation that can be rerun. If those cannot be named, this is not yet an `E.23` use; name the live claim and send it to its direct governing pattern. Common exits are work, transformation-flow structure, evolutionary retention and publication, source use, refresh, gate-decision publication, and DPF framework authoring.

Use `E.23` when an object version will be improved through repeated passes under a declared object-under-improvement evaluation. The object can be a pattern, `DRR`, FPF corpus object, engineering quality object, naming candidate, OEE and NQD candidate, archive or front member, selected set, parity report, refresh report, or declared transformation result, if an exact evaluation supplies values and stop meanings for that object kind.

Not this pattern when one direct quality evaluation is enough. Use `E.22` to frame one evaluation and then run the named object-under-improvement evaluation. Use `A.19.ECS` first if the needed evaluation characteristic space does not exist.

First useful move: name the object version under improvement, the exact evaluation that will re-evaluate it, the improvement aim, protected trade-offs, cost and risk account, and local stop condition.

What goes wrong if missed: teams close discharge rows instead of improving quality, retry blindly, optimize visible values while damaging protected qualities, stop forever after a local all-`5` result, or let a review recommendation become decision, work, evidence, selected-set publication, parity, or refresh by stealth.

What this buys in practice: each pass has a declared object version, an intended evaluation-result change, a rerunnable evaluation, protected trade-offs, and a stop or switch condition. Effort can then change substantive quality and stop when no non-dominated change is worth its cost, instead of merely producing more review state.

Primary EntityOfConcern in plain terms: the repeated quality-improvement method for one object version under one declared evaluation.

