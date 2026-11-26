---
chunk_kind: "child"
pattern_id: "B.5.MR"
pattern_title: "Compare Models by Refinement and Abstraction"
section_id: "B.5.MR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MR/B.5.MR__002_problem-frame.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "B.5.MR — Compare Models by Refinement and Abstraction"
  - "B.5.MR:1 — Problem frame"
line_start: 50992
line_end: 50997
dependencies:
  - "B.1"
  - "B.5.FM"
  - "B.5.TC"
  - "C.2.1"
  - "C.37.MM"
keywords:
---

### B.5.MR:1 - Problem frame

**Use this when** you need a model to determine something left open by another model, or need an abstraction that leaves some determinations open while retaining a useful conclusion. The practical question is which answers remain admissible and which conclusions can still be used. Two specifications of a design, two accounts of a method or two editions of the rules for constructing a model can each raise that question.

A useful first result identifies the inquiry, the assertions preserved and the answers admitted by each model. A strict refinement excludes an earlier admissible answer. A strict abstraction admits an answer excluded before, so a conclusion that depended on that exclusion needs reconsideration. When deciding between theories that answer different questions, B.5.TC helps identify a comparable use. When the change is in the actual system, examine the changed system directly.

