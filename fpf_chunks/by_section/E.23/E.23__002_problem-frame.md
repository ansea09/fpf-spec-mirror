---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__002_problem-frame.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:1 — Problem frame"
line_start: 67776
line_end: 67804
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
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:1 - Problem frame

Use `E.23` when the working question is: "how do we improve this?" The object under improvement can be a chair, component, subsystem, nuclear-plant safety case, policy, method, architecture description, benchmark result, declared transduction result, FPF pattern, `DRR`, corpus slice, or another exact object. `E.23` is the entry pattern for repeated improvement, but it does not say what "better" means by itself: the loop starts only after the object version and the object-under-improvement evaluation for that object are declared. If the object has no adequate object-under-improvement evaluation yet, construct or repair the object-under-improvement evaluation `CharacteristicSpace` through `A.19.ECS` before opening the loop.

The governed object is the repeated quality-improvement method parameterized by `<ObjectVersionUnderImprovement, ObjectUnderImprovementEvaluationRef>`. The loop does not supply quality values or construct coordinate sets. It changes the object under improvement, asks the object-under-improvement evaluation to re-read the changed object version, and decides whether to stop, narrow, continue, switch method, or hold for more exact information.

Use it especially when the work is more than a cheap admissibility read:

- an already admissible object under improvement is being improved toward exceptional expression;
- returned findings must be absorbed row by row and then re-read for actual quality movement;
- one `E.22` read returns a bounded portfolio of candidate improvement proposals, and the loop must choose, apply, re-read, or hand off those proposals without pretending the read already selected a winner;
- a proposed improvement may raise visible coordinates while damaging usability, affordability, repair locality, corpus ecology, neighbour fit, source-content preservation, or another protected quality;
- an agentic or tool-using loop is being considered and its cost, supervision, retry, memory, verification, or stop posture matters;
- a specialized improvement cycle, such as throughput, variation, learning, stabilization, or orientation under uncertainty, is being selected for one declared characteristic space.

**Not this pattern when.** Use `E.22` alone for one framed `floorRead` or other single quality review when no repeated improvement method is needed. Use the object-under-improvement evaluation itself when the question is already scoped and the work is a direct value read. Use `A.19.ECS` when the live problem is constructing or repairing the object-under-improvement evaluation `CharacteristicSpace` for the object under improvement. Use `C.16.Q` when the live problem is overloaded `quality` wording. Use `C.25` when the live problem is a composite engineering quality-family endpoint. Use project-side evidence, assurance, gate, work, release, safety, or compliance patterns when the result is being reused for those exact claims.

**First useful move.** Name the exact object version under improvement and the object-under-improvement evaluation before changing anything. If the evaluation is missing or not adequate for the object kind and use, construct or repair it through `A.19.ECS` first. Then state the improvement aim, floor, protected trade-offs, selected quality-read purpose, and the condition under which the next pass would stop, narrow, continue, switch method, or hold.

**Cheap stop.** If one `E.22` short-form `floorRead` under the object-under-improvement evaluation gives an admissible stop and no repeated improvement aim is live, do not open `E.23`.

**What goes wrong if missed.** A team counts closed checklist rows as quality improvement. An agent retries because it can, not because the object-under-improvement evaluation moved. A `DRR` becomes longer but not more decision-bearing. A pattern gets more machinery while first use becomes harder. A specialized cycle is used because it is familiar, even though the declared characteristic space does not fit it. An OEE/NQD run changes candidates without saying which `Q` movement it seeks relative to the current comparison set or front.

**What this buys.** `E.23` gives any improvement effort a disciplined shape: choose the object, declare the object-under-improvement evaluation that says what improvement means, change the object, re-read it, inspect trade-offs, justify added operation families, and stop or switch when the declared values, trade-offs, and costs no longer make another pass admissible.

**Governed object in plain terms.** The governed object is a repeated method for improving one exact object under improvement under the object-under-improvement evaluation that supplies values for that object under improvement.

**Primary working reader.** The first reader is the person running or supervising a repeated improvement pass. The downstream reader is the reviewer, steward, engineer, author, or maintainer who must judge whether the changed object version actually improved under the declared evaluation.

