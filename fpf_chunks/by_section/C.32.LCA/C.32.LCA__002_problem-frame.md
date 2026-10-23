---
chunk_kind: "child"
pattern_id: "C.32.LCA"
pattern_title: "Construct and Compare a Control Architecture"
section_id: "C.32.LCA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.LCA/C.32.LCA__002_problem-frame.md"
commit_sha: "a5ac87ac15e78517d12bc66155b9da3ca254b643"
heading_path:
  - "C.32.LCA — Construct and Compare a Control Architecture"
  - "C.32.LCA:1 — Problem frame"
line_start: 76662
line_end: 76685
dependencies:
  - "A.3.3.PI"
  - "B.2.5"
  - "C.30.LCA"
  - "C.32"
  - "C.32.MWA.PP"
keywords:
---

### C.32.LCA:1 - Problem frame

Use this pattern when a result depends on decisions and actions that use different information, take different amounts of time, or belong to participants with different authority, and you need to construct or change how those contributions work together.

A robot can follow a target accurately and still receive a target that exceeds its actuator limit. A production team can respond quickly and still wait for a decision that nobody present may make. In both situations, improving one participant is insufficient: the arrangement must connect what can be observed, decided and done in time.

**First useful move.** Choose one consequential demand or disturbance. Follow it from the information available at the time, through the decision and permitted action, to the receiving result. Check whether the arrangement supplies the conditions along that path. A missing condition directs construction of an alternative; an adequate path can be retained while examining another consequential case or a justified improvement. Follow each proposed change through the same whole.

**What this buys.** The reader obtains comparable control arrangements, the mechanism by which each could obtain the intended result, their conditions and costs, and a reason to retain, select or revise an arrangement. A useful result can be a simpler incumbent, a bounded proposal, a qualified technical construction, or a precise finding that the requested outcome is unavailable under the supplied conditions.

The broad subject is functional organization: how contributions combine to obtain a whole result. This pattern develops its **control-architecture branch**. It constructs the organization of observation, decision and intervention, including coordination needed between controllers or participants. It does not presume a hierarchy, three layers, different update rates, or a correspondence between one function and one physical part. Layered and multirate control are important alternatives within this question.

The primary working reader is an architect, engineer or operations practitioner who can explain the relevant work and obtain the subject knowledge needed for its consequential claims. The common method requires reasoning about dependencies, time and conditions. A numerical stability or safety claim additionally requires the appropriate control-engineering competence and model.

**Ordinary boundaries.**

- If an available controller or working arrangement already answers the question, use it. A new architecture exercise needs a consequential reason.
- If the question is what control structure a description actually represents, use **C.30.LCA**. Its result can supply the present arrangement here.
- If the difficulty is functional construction without a control dependence, use **C.32** for the candidate-configuration question or **C.39** for a missing way to obtain the required contribution. Return here when the observation, decision and intervention dependence is the unresolved part.
- If the task is to establish the purpose or legitimate priority itself, obtain that decision from its governing practice and participants. Here the question is how that decision affects feasible control and when feedback requires its reconsideration.
- If a project needs a particular controller, estimator or safety proof, construct or obtain that technical result. The common architecture method below identifies and uses its necessary contribution; it does not replace the subject mathematics.

A proposed arrangement and an operating arrangement have different evidence. The explanation can justify a candidate before implementation. Claims about its actual effectiveness require observations of its use under the conditions that matter.

