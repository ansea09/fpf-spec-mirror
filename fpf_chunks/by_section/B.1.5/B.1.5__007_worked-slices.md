---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:5"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__007_worked-slices.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:5 — Worked Slices"
line_start: 32548
line_end: 32573
dependencies:
  - "A.1"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "E.10"
  - "E.20"
  - "G.5"
  - "U.Method"
  - "U.MethodDescription"
keywords:
  - "MIC"
  - "assurance hooks"
  - "capability continuity"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "order-sensitive method"
  - "submethod"
  - "typed join"
  - "work enactment"
---

### B.1.5:5 - Worked Slices

#### B.1.5:5.1 - Manufacturing Recipe

`AssembleFrame`, `InstallMotor`, and `RunFunctionalTest` are recovered as `U.Method` values in a bounded manufacturing context. `InstallMotor` must precede `RunFunctionalTest`; the test accepts the installed harness as input; an adapter method is needed when a supplier motor uses a different connector.

The composite `BuildAndVerifyPumpUnit` is admitted as a `U.Method` only after the whole states its preconditions, accepted inputs, final effect, exposed start and abort interactions, encapsulated internal calibration interactions, and failure conditions. The actual Tuesday build is `U.Work`; resource burn and test telemetry are not method parts.

#### B.1.5:5.2 - Emergency Intake

`RegisterPatient`, `AssessVitals`, `ClassifyUrgency`, and `RouteToCare` may compose into `EmergencyIntake@Hospital`. The guarded choice is driven by declared vital-sign and symptom predicates. A role assignment and capability check determine who may enact the work, but they are not parts of the method.

If the source only provides a wall poster with boxes and arrows, the current object is first `U.MethodDescription`. The composite `U.Method` is admitted only when the hospital context recovers the methods, guards, typed joins, failure response, and interface exposure.

#### B.1.5:5.3 - Learned Model Pipeline

A neural-network pipeline may describe feature extraction, embedding, attention, retrieval, ranking, and explanation generation. Some blocks may be formal substrate or mechanism material, some may be `U.MethodDescription`, and some may be recovered as `U.Method` values.

The pipeline is one composite `U.Method` only when it has accepted inputs, outputs, invariants or admissibility conditions, typed joins, fallback behavior, failure conditions, and work-facing acceptance criteria. Otherwise keep the graph as a method description, mathematical lens, mechanism material, or `MethodRelationStructure@BoundedContext`.

#### B.1.5:5.4 - Evidence Synthesis And Publication

`CollectDatasets`, `NormalizeSchemas`, `EstimateModel`, `CrossValidate`, and `DraftManuscript` can compose into `EvidenceSynthesisPublish@ResearchContext` only when each candidate is recovered as a `U.Method` and the typed joins are explicit. `NormalizeSchemas` must produce a feature or evidence space acceptable to `EstimateModel`; legacy datasets may need adapter methods; `CrossValidate` may be a critical cutset for later assurance; `DraftManuscript` may require a provenance or SCR condition before publication work is admitted.

A paper draft, workflow diagram, repository, or notebook is first a `U.MethodDescription` or another episteme. The publication work is `U.Work`. Compute, storage, reviewer time, and artifact-release resource costs belong to `U.Work` and `Gamma_work`. The MIC may expose `Submit()` and `ReleaseArtifacts()`, forward a parameterized `CrossValidate.Folds(k)` interaction, and encapsulate ad hoc scrubbing utilities.

