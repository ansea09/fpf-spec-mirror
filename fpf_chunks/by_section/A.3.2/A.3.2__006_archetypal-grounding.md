---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__006_archetypal-grounding.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:5 — Archetypal Grounding"
line_start: 6643
line_end: 6684
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

### A.3.2:5 - Archetypal Grounding

Across the slices below, `U.MethodDescription` is recognized by its relation to a method, not by its carrier or notation:

```text
In this bounded context, which representation describes which U.Method, for which later work, review, planning, audit, or enactment use?
```

#### A.3.2:5.1 - Industrial procedure

`SOP_Etch_v7.pdf` and a PLC ladder file describe `EtchAl2O3@FabA`.

The method description states gas-flow inputs, temperature bounds, chamber preconditions, expected etch profile, failure conditions, operator role kind, calibration capability threshold, and accepted parameter ranges.

The scheduled maintenance-window run is `U.WorkPlan`; tool run `W-143` is `U.Work`; metrology output becomes evidence only when an evidence pattern governs the relevant claim or use; gas-flow equations may require `C.29` or `A.6.0`.

#### A.3.2:5.2 - Optimization model

A MILP model and solver configuration describe `JSScheduleV4@Plant2026` when the current claim is the method for producing a production schedule.

The same files may also carry formal-substrate claims: variables, constraints, objective, admissible solution set, and invariants. A solver run with timestamps is work. A selector mechanism, if declared, lives under `A.6.1` and `E.20`.

Do not infer that solver search order is the project work sequence.

#### A.3.2:5.3 - Proof script

A proof-assistant script may describe the method for deriving a theorem, expose a formal substrate, or serve as evidence for a claim. The method-description claim is current only when the script is used as the representation of the reusable way of deriving or checking.

A concrete proof-checking session is work. A theorem publication or source citation is publication use or evidence use. The algebraic or type-theoretic structure may require a mathematical-lens or formal-substrate declaration.

#### A.3.2:5.4 - Clinical guideline

A clinical guideline describes `AcuteAppendicitisTriage@HospitalContext` when it states the triage method: inputs, exclusions, decision criteria, role kind, capability requirements, expected result, and failure response.

Regulatory acceptance, authorization to use, patient-specific dated enactment, and causal-use claims are separate. If the resulting work is used for a causal claim, apply `C.28`.

#### A.3.2:5.5 - Workflow diagram

A BPMN or object-centric process model can be a method description when it states the reusable method. It can also be a work-plan view, source data, event-log model, process-mining representation, or publication face.

If the diagram is being interpreted as a route that tokens or workers must follow, check whether that route claim is truly part of the method. If it is only a diagrammatic overread of constraints, objects, events, or graph structure, use `C.2.P.DR` and the direct governing pattern.

