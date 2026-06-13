---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 6489
line_end: 6501
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
  - "model"
  - "recipe"
  - "specification"
---

### A.3.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The code is the method." | If the claim is about the repository or executable form, use `U.MethodDescription`; if it is about the semantic way of doing, name the `U.Method`; if it is about a run, use `U.Work`. |
| "Yesterday's log is our procedure." | The log is work evidence or a work record. Write or cite the method description separately. |
| "The approved protocol proves safe use." | Separate method description, approval or gate claim, safety evidence, work plan, and work occurrence. |
| "The optimization model is the process." | Recover whether the current claim is method description, formal substrate, method, mechanism, work plan, work, or evidence. |
| "The query plan calls the next step." | Check whether this is a database plan, method description, formal representation, or metaphorical overread; use `C.2.P.DR` when needed. |
| "The diagram's route is the workflow." | Recover whether the route is graph path, method sequence, work plan, event trace, or diagram convention. |
| "The new version refines the old one." | State the preserved interface and strengthened preconditions, effects, outcomes, or bounds. |
| "SOPs are notes, code is the real spec." | Treat both as possible method descriptions; judge by recoverable method fields, not representation prestige. |

