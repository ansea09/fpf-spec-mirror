---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:12"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__014_worked-examples.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:12 — Worked examples"
line_start: 82753
line_end: 82807
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:12 - Worked examples

#### F.9:12.1 - Service acceptance, executions, and observations

A service team uses an SLO, runtime observations, and an automation-process model.

Bridge Cards:

```text
BridgeCard:
  CellA: ITIL4:SLO@service-design
  CellB: SOSA:Observation(availability)@monitoring-run
  senseFamilyA: Status
  senseFamilyB: Measurement
  BridgeKind: Measurement-evidence-for
  Direction: CellB evidences CellA
  CL: 2
  LossNotes: sampling window; clock skew; target definition
  CounterExampleOrInvariantEvidence: an observation can be true while the service status claim remains under review
  AdmittedUse: Explanation-only
  NonAdmittedUse: do not treat the observation as the SLO status itself
  DirectGoverningPatternIfNotF9: F.10 or B.3 for status or assurance use
  RevisionTrigger: monitoring window or SLO definition changes
```

The same team may publish a Naming-only row for "availability" if each participating Bridge reaches `CL >= 1`, but no observation becomes the status target and no process design becomes a performed work occurrence by that row.

#### F.9:12.2 - Behavioral role versus access role

A process model has `BPMN:Participant`; an access-control catalogue has `NIST-RBAC:Role`.

Bridge Card result:

* Bridge kind: Partial-overlap.
* `CL`: 2.
* Loss Notes: assignment moment, enforcement locus, multiplicity, accountability boundary.
* Admitted use: Naming-only label "actor" and, if a local `U.Role` is separately recovered, role-description naming.
* Non-admitted use: no `U.RoleAssignment`, no required-role satisfaction, no performed-work attribution.

If a project wants an RBAC role to count for a work step, it must open A.2.1 or F.6 and recover a local `U.RoleAssignment`; F.9 supplies only the cross-context sense relation and the stated losses.

#### F.9:12.3 - Equivalence of subtype notions for structural rows

`OWL2:SubClassOf` and a curated taxonomy `is-a` relation can admit a Type-structure row only when the curated taxonomy is acyclic, anti-symmetric, and uses class-level reasoning compatible with the OWL profile being cited. If those invariants are absent, the Bridge is demoted to `CL = 2` and the admitted use falls to Naming-only or explanation.

#### F.9:12.4 - Setpoint versus service target

`CTRL:setpoint` and `ITIL:target` may look close because both are called targets. F.9 keeps them apart:

* `CTRL:setpoint` is a physical reference value in a control context.
* `ITIL:target` is a service objective or requirement-like status claim.
* Bridge kind is usually Disjoint or Partial-overlap, not Equivalence.

The result is didactic contrast or Naming-only orientation, not substitution in control or service calculations.

