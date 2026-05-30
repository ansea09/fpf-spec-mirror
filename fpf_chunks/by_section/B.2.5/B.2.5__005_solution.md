---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__005_solution.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:4 — Solution"
line_start: 31429
line_end: 31465
dependencies:
  - "A.1"
  - "A.12"
  - "A.15"
  - "A.2"
  - "A.3"
  - "A.7"
  - "B.2"
  - "C.30.LCA"
keywords:
  - "control architecture"
  - "feedback loop"
  - "layered control"
  - "stability"
  - "supervisor"
---

### B.2.5:4 - Solution

Model a supervisor-subholon feedback loop as a relation among holons, roles, transformers, media, and returned influence. A conforming loop identifies:

```text
SupervisorSubholonFeedbackLoop@Context ::= {
  supervisedHolonRefs      : FinSet(U.HolonRef),
  supervisorRoleRef        : U.RoleRef,
  supervisorTransformerRef : U.TransformerRef | TransformerBearingSystemRef,
  sharedMediumRefs         : FinSet(U.InteractionRef | PublicationChannelRef),
  observationOrReportRefs  : FinSet(ObservationRef | ReportRef | PublicationUnitRef),
  influenceOrConstraintRefs: FinSet(InfluenceSignalRef | ConstraintRef | ObjectiveRef),
  feedbackRelationRefs     : FinSet(QualifiedRelationRecordRef),
  objectiveOrConstraintRef?,
  loopClosureCondition,
  admissibleUse,
  nonAdmissibleUse,
  governingClaimPatternRefs?
}
```

**Loop reading.** The loop has an observation/report side and an influence/constraint side. A one-way command relation is not yet a closed supervisor-subholon feedback loop unless the return observation, report, or state relation is also declared.

**Structural-composition boundary.** A supervised holon may be part of a larger holon, but supervision is not the same relation as part-whole composition. A controller, committee, method, or review practice can supervise a subholon without being a physical component of that subholon.

**Control-structure view boundary.** When the loop appears in an architecture description as planner/controller/observer/plant/supervisor structure, use `C.30.LCA` to record the control-structure view. `B.2.5` supplies the supervisor-subholon relation; `C.30.LCA` records the broader control-structure view.

**Proof boundary.** A conforming `B.2.5` loop is a relation, not proof. Stability and reusable state-evolution claims use `A.3.3`; rate and timing claims use `C.27`; causal-use claims use `C.28`; evidence claims use `A.10` or `G.6`; assurance claims use `B.3`; gate and constraint-validity claims use `A.20`/`A.21`; mathematical-lens transfer uses `C.29`.

**Episteme case boundary.** In an episteme case, the acting and revising work is performed by systems or practices bearing `Transformer` roles. The `U.Episteme` is the knowledge-bearing object being reviewed, revised, stabilized, cited, or published. It does not itself sense, judge, plan, or act.

**Worked slice A - robotic swarm.** A drone fleet has individual drones, a shared communication medium, and a fleet-scope controller or distributed consensus method. `B.2.5` records each drone as supervised holon, the controller or consensus system as supervisor transformer, telemetry as observation side, and waypoint or mode commands as influence side. Claims about exponential convergence, delay tolerance, or disturbance damping use `A.3.3`, `C.27`, and evidence/assurance claim as live.

**Worked slice B - scientific theory.** A scientific theory is revised when labs publish findings and a research community reviews anomalies and accepted revisions. `B.2.5` records the theory or its constituent epistemes as supervised objects and the community/review practice as transformer-bearing supervisor. Journals, conferences, datasets, and review records are publication or interaction channels. The theory does not perform the sensing or judging; the acting systems and practices do.

**Worked slice C - product supervisor loop.** A product platform constrains component teams through published interface rules and release gates. `B.2.5` records the supervising platform policy role, component/subproduct holons, report channels, and constraint returns. Work authority uses `A.15`; gate passage uses `A.21`; interface commitments use module/interface patterns.

