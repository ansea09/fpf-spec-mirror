---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__008_conformance-checklist.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:7 — Conformance Checklist"
line_start: 6567
line_end: 6598
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

### A.3.2:7 - Conformance Checklist

**CC-A3.2-1 (Episteme).** `U.MethodDescription` is an `U.Episteme` describing a `U.Method`. It may be expressed in text, code, diagram, model, rule set, or executable form, but the publication form or representation form does not determine the current FPF claim.

**CC-A3.2-2 (Method linkage).** A method description must name or recover the `U.Method` it describes and the bounded context where the method identity is judged.

**CC-A3.2-3 (No automatic trigger repair).** `Algorithm`, `program`, `proof`, `solver`, `workflow`, `process`, `procedure`, `recipe`, and `model` wording must not be repaired to `U.MethodDescription` until the current slot is recovered.

**CC-A3.2-4 (Description not work).** A method description is not a work occurrence. Executability does not change this: program runs, proof-checking sessions, solver runs, lab runs, and clinical applications are `U.Work` when dated occurrence fields are current.

**CC-A3.2-5 (Description not plan or authority).** A method description is not a work plan, gate decision, permission, approval, external-rule authorization, or evidence relation. Those claims may cite the description but require their own governing patterns.

**CC-A3.2-6 (Description not mechanism).** A method description does not close a mechanism claim. If operation algebra, law set, admissibility predicates, applicability, transport, audit, or realization relation is current, use `A.6.1` and `E.20` as needed.

**CC-A3.2-7 (Description not formal substrate).** A method description does not close a formal-substrate or mathematical-lens claim. If variables, equations, invariants, structure, substrate, or mathematical payoff are current, use `A.6.0`, `C.29`, or the direct mathematical pattern.

**CC-A3.2-8 (No people or calendars inside the description claim).** A method description may state role kinds and capability thresholds required for enactment. Named people, dates, schedules, launch values, and work witnesses belong to work planning, role assignment, or work occurrence claims.

**CC-A3.2-9 (Parameters and binding time).** Parameters may be declared in the method or method description. Concrete run values are bound in `U.WorkPlan` or `U.Work` according to the current claim.

**CC-A3.2-10 (Equivalence).** Two method descriptions describe the same `U.Method` in a bounded context only when they preserve the same method identity: accepted inputs, preconditions, effects, bounds, and acceptance criteria. Different notation, control structure, or representation style is not enough to split or merge method identity.

**CC-A3.2-11 (Refinement).** A refinement claim must state what is preserved and what is strengthened: interface, preconditions, postconditions, effects, bounds, or accepted outcomes. Refinement is not implied by a new file version.

**CC-A3.2-12 (Nondeterminism).** If the method description permits search, optimization, sampling, nondeterministic choice, or learned behavior, it must state the admissible outcome set and acceptance criteria needed to judge work results.

**CC-A3.2-13 (Context bridge).** Cross-context reuse requires an explicit bridge or alignment relation for terms, units, roles, assumptions, and acceptance criteria. Name identity alone is insufficient.

**CC-A3.2-14 (Declarative representation).** If a method description contains declarative representations, do not overread them as ordered work-control claims. Use `C.2.P.DR` when route, path, call, dispatch, work-control sequence, workflow, or lifecycle language hides the represented object or direct governing pattern.

**CC-A3.2-15 (Causal-use boundary).** A method description may describe intervention assignment, target-trial emulation, realized-counterfactual sampling, simulation, or causal-evidence collection. It does not by itself establish causal use. If causal effect, intervention success, counterfactual comparison, causal fairness, or policy effect is claimed, use `C.28`.

