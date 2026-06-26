---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__006_solution.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:4 — Solution"
line_start: 33627
line_end: 33688
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.M"
  - "B.1"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30.LCA"
  - "G.6"
keywords:
---

### B.2.5:4 - Solution

Model the current object as `SupervisorSubholonFeedbackRelation@Context`.

```text
SupervisorSubholonFeedbackRelation@Context:
  supervisedHolonRefs: FinSet(U.HolonRef)
  boundedContextRef:
  supervisorRoleRef:
  supervisingActingSystemRef:
  supervisedWorkOrTransformationRefs?
  observationOrReportRefs: FinSet(ObservationRef | ReportRef | PublicationUnitRef | SourceUseRef)
  influenceOrConstraintRefs: FinSet(InfluenceSignalRef | ConstraintRef | ObjectiveRef | ModeRef)
  sharedMediumOrPublicationRefs?
  holonBoundaryCrossingRelationRefs?
  feedbackClosureCondition:
  admissibleUse:
  nonAdmissibleUse:
  neighboringClaimOwnerRefs?
```

This relation is not a U-kind and not a mathematical loop lens. It is a relation record for the current bounded context.

#### B.2.5:4.1 - Two-Sided Feedback Relation

A one-way command, publication, or report relation is not yet a supervisor-subholon feedback relation. Name both:

- the observation, report, signal, source, or publication side; and
- the returned influence, constraint, objective, mode, or work-change side.

If only one side is current, record a one-sided relation and use the direct owner for that claim.

#### B.2.5:4.2 - Part-Whole Boundary

A supervised holon may be part of a larger holon, but supervision and parthood are different relations. An acting controller system, committee system, platform-governance system, review board, or tool-mediated group can hold the supervisor role without being a physical part of the supervised holon. A method, policy, or review practice can structure the supervision work; it does not supervise by itself.

Use `A.1`, `B.1`, `A.14`, and `C.13` for parthood. Use B.2.5 only for the supervisor-subholon feedback relation.

#### B.2.5:4.3 - Acting-System Boundary

The supervisor role is held by an acting system in a bounded context. Do not create `U.TransformerRef` or treat a publication, theory, dashboard, model, method description, or report as the acting system.

For acting-side externalization, use `A.12`. For transformation, use `A.3.4`. For work, use `A.15.1`. For role assignment, use `A.2.1`.

#### B.2.5:4.4 - Control-Structure View Boundary

When the relation is drawn as planner, controller, observer, plant, and supervisor structure, B.2.5 names the relation, while `C.30.LCA` owns the control-structure view. A diagram or view does not establish the relation by appearance; recover the in-life relation and the description relation separately.

#### B.2.5:4.5 - Neighboring Claim Boundary

B.2.5 does not certify stability, safety, assurance, evidence sufficiency, causal validity, gate passage, rate adequacy, or mathematical adequacy.

Use:

- `A.3.3` for reusable dynamics or state-evolution claims;
- `C.27` for temporal and rate adequacy;
- `C.28` for causal-use claims;
- `A.10` and `G.6` for evidence and provenance;
- `B.3` for assurance;
- `A.20` and `A.21` for constraint validity and gate decisions;
- `C.29` for mathematical-lens use.

