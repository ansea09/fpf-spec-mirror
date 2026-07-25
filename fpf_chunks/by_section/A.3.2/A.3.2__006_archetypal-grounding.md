---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__006_archetypal-grounding.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:5 — Archetypal Grounding"
line_start: 7221
line_end: 7259
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.1"
  - "A.6.1"
  - "A.6.5"
  - "B.1.5"
  - "B.3"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "F.9"
  - "U.Method"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "claim-bearing episteme"
  - "exact U.Method EntityOfConcern"
  - "method-description membership"
  - "representation versus publication versus plan versus Work"
  - "same method versus equivalent descriptions"
  - "substantive way-of-doing claim"
---

### A.3.2:5 - Archetypal Grounding

Across the slices below, recognize the claim-bearing episteme before examining how it is represented or published. Ask in this order:

1. Which admitted `U.Method` is its exact `EntityOfConcern`?
2. Which claim says something substantive about that method as a way of doing?
3. Which work or decision will rely on the claim, and is the episteme adequate for that receiving use?
4. When expression or availability matters, which `C.29` representation corresponds to the claims, which publication occurrence makes the selected edition available, which publication form expresses it, and which `U.PresentationCarrier` bears that form?

#### A.3.2:5.1 - Industrial procedure

A procedure episteme about `EtchAl2O3@FabA` qualifies when its claims state how the etching method is done: gas-feed participant meanings, temperature bounds, chamber preconditions, intended etch profile, failure conditions, operator role kind, calibration capability threshold, or admitted parameter ranges.

A PDF publication form may express one edition of those claims, and a PLC ladder representation may correspond to some of them. Their visible forms do not establish membership. The scheduled maintenance-window preparation is `U.WorkPlan`; tool run `W-143` is a Work individual admitted under `U.Work`; an exact metrology measurement result can support another claim only through the governing evidence relation.

#### A.3.2:5.2 - Optimization model

A scheduling-method episteme qualifies when its exact `EntityOfConcern` is `JSScheduleV4@Plant2026` and its claims state how a production schedule is produced or evaluated. A MILP representation and an explicitly recovered solver-configuration representation can stand in declared correspondence to those claims.

A separate formal-substrate episteme can make claims about variables, constraints, objective, admissible solution set, or invariants. A publication form expressing that episteme may be borne by the same presentation carrier, but the carrier does not make the claims or establish their truth. A timestamped solver run is work. A selector mechanism, if declared, is governed by `A.6.1` and `E.20`. Solver search order does not by itself state the project work sequence.

#### A.3.2:5.3 - Proof script

An episteme about a reusable derivation or checking method qualifies when it identifies that `U.Method` exactly and makes a substantive claim about how the derivation or check is done. A proof-assistant script may represent those claims. The script's notation does not establish membership.

A concrete proof-checking session is work. Claims about a formal substrate, a theorem, or evidence for the theorem remain separately governed even when publication forms expressing those epistemes are borne by the same carrier. A publication occurrence, not the form or carrier, makes a selected edition available to an audience for a bounded use.

#### A.3.2:5.4 - Clinical guideline

A guideline episteme qualifies when its exact `EntityOfConcern` is `AcuteAppendicitisTriage@HospitalContext` and its claims state the triage method through patient-information and resource participant meanings, exclusions, decision criteria, relevant role kinds and capabilities, intended effects, or failure response. A publication form expresses one selected edition, and a publication occurrence can make that edition available; approval status remains a separate claim.

Patient-specific dated enactment is a Work individual admitted under `U.Work`. If a separately governed triage disposition, diagnostic finding, measurement result, or other exact effect is used for a causal claim, apply `C.28`; neither enactment nor causal use changes method-description membership.

#### A.3.2:5.5 - Workflow diagram

An episteme whose claims state one reusable method may qualify as `U.MethodDescription`; a BPMN or object-centric process model may represent those claims. A diagram can also represent a work plan, event-log model, or independently selected structure, so its notation does not settle the exact `EntityOfConcern`.

If the diagram is read as a route that tokens or workers must follow, check whether ordered enactment is genuinely claimed by the method. If a graph, constraint, object, or event structure has merely been turned into a route by wording, use `C.2.P.DR` and recover the direct governing pattern.

