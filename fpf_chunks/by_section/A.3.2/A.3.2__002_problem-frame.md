---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__002_problem-frame.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:1 — Problem frame"
line_start: 6742
line_end: 6763
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "A.3.1"
  - "B.3"
  - "C.2.P.DR"
  - "C.28"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "U.BoundedContext"
  - "U.Method"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "SOP"
  - "U.Episteme"
  - "code"
  - "method description"
  - "method vs description vs work"
  - "model"
  - "recipe"
  - "source"
---

### A.3.2:1 - Problem frame

Use this pattern when a project needs to say what text, code, diagram, rule set, solver formulation, proof script, SOP, protocol, or process model **describes a method**.

Use it when the working question is:

* which `U.Method` is being described;
* which representation states the fields needed for reuse, review, planning, audit, or enactment;
* whether two descriptions preserve the same method identity in one bounded context;
* which parameters, preconditions, effects, admissible outcomes, and acceptance criteria are stated by the description;
* whether an executable file, proof script, workflow diagram, or optimization model is only a method description, or whether a different FPF claim is current.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.MethodDescription`: an `U.Episteme` that describes a `U.Method` in some representation.

**First useful move.** Name the method being described, the bounded context in which its identity is judged, the representation form, and the fields by which work can later cite or enact the described method.

**What goes wrong if missed.** Code becomes "the method", a workflow diagram becomes work, an approved protocol becomes evidence of safe execution, a proof script becomes mechanism law, or a declarative representation becomes an ordered work-control claim.

**What this buys.** The project can improve, compare, version, audit, and reuse method descriptions without collapsing them into method semantics, work plans, dated work, mechanisms, mathematical substrates, gates, authority claims, or evidence relations.

**Not this pattern when.** Do not use this pattern merely because the source says `algorithm`, `program`, `proof`, `workflow`, `process`, `procedure`, `recipe`, or `model`. First recover the slot. The current claim may instead be `A.3.1 U.Method`, `A.6.0` formal-substrate declaration, `C.29` mathematical-lens use, `A.6.1` or `E.20` mechanism meaning, `A.15.2 U.WorkPlan`, `A.15.1 U.Work`, an evidence relation, a publication-use relation, or quote-only source wording.

