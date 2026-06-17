---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__006_archetypal-grounding.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:5 — Archetypal Grounding"
line_start: 6142
line_end: 6181
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "B.1.5"
  - "C.2.P.DR"
  - "C.29"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
  - "abstract process"
  - "how-to"
  - "procedure"
  - "recipe"
---

### A.3.1:5 - Archetypal Grounding

Across the slices below, a `U.Method` is not recognized by source wording, notation, or publication form. It is recognized by a stable project answer to this question:

```text
In this bounded context, what way of doing changes, produces, derives, selects, controls, or preserves the EntityOfConcern under these conditions?
```

Manufacturing, optimization, proof, graph or query overread, and clinical triage differ in material, representation, and assurance needs, but they share the same method slot. The archetypal failure is also shared: a nearby description, plan, run, mechanism, formalism, or evidence relation takes the method name and silently changes what the project can rely on.

#### A.3.1:5.1 - Manufacturing recipe

`Etch_Al2O3` is the method when the bounded context uses that name for the way of transforming a wafer surface under specified conditions.

The SOP, PLC program, calibration recipe, and supplier note are method descriptions when they describe that method. A planned maintenance-window run is a `U.WorkPlan`. Tool run `W-143` with timestamps and logs is `U.Work`. Gas-flow equations may be a formal substrate or mathematical lens input. Evidence for whether the run met a safety or quality claim is governed separately by `A.10`, `B.3`, `C.27`, or a gate pattern.

#### A.3.1:5.2 - Optimization model

`JS_Schedule_v4` may be the method when it names the project-accepted way of producing a job-shop schedule.

The MILP formulation, solver configuration, and acceptance tests are method descriptions or formal-substrate declarations depending on the current claim. The solver's internal search is not automatically the project work sequence. A scheduled production plan is `U.WorkPlan`; the actual scheduling run and resulting dated decision record may be `U.Work` and evidence for separate claims.

#### A.3.1:5.3 - Proof or derivation

`Gauss_Elimination` can be a method for deriving a result under a mathematical context.

A textbook explanation, proof-assistant script, and formal rule set are method descriptions. A proof run in a concrete assistant session is work. The algebraic structure may be a formal substrate. The claim that this proof is used as evidence for a project decision is an evidence or assurance claim, not part of the method merely because the method produced a derivation.

#### A.3.1:5.4 - Graph or query overread

A graph path, SQL-like query, checklist predicate, or dashboard table may represent a relation, state, evidence structure, provenance structure, or publication face. It becomes a method claim only if the text recovers a semantic way of doing and its work-facing relation.

If the wording says the graph "routes" a project to a pattern, the query "calls" a work sequence, or the table "authorizes" action without a recovered method kind, work kind, gate claim, or authority claim, apply `C.2.P.DR` first.

#### A.3.1:5.5 - Clinical triage protocol

`SepsisTriage_v3` may be the method when the hospital context uses that name for the way of classifying a patient state and selecting the next clinical response.

The protocol PDF, order-set screen, and decision-support rule are method descriptions or publication faces. The clinician's dated assessment is `U.Work`. The physiological model or score formula may be a formal substrate or mathematical lens. An admission policy, a treatment-release gate, and evidence that the triage reduced harm are neighboring claims. Keeping those claims separate prevents a document from becoming authorization, proof, and performed work merely because it describes the method.

