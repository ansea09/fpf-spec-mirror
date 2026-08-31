---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:2"
section_title: "Kind and Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__003_kind-and-boundary.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:2 — Kind and Boundary"
line_start: 3797
line_end: 3853
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
  - "E.24.UK"
keywords:
  - "ability envelope"
  - "capability-fit condition"
  - "currentness"
  - "holder-dependent capability instance"
  - "measure set"
  - "qualification window"
---

### A.2.2:2 - Kind and Boundary

`U.Capability` is retained as a dependent durable U-kind name under `E.24.UK`. A concrete `U.Capability` instance is the holder-dependent capability instance of a named `U.System`; its identity is grounded by the holder, work family or result class, envelope, measure set, qualification window, and currentness condition. The statement that asserts the ability, the evidence that supports reliance, and the fit predicate that tests work admission are separately governed records or relations rather than the `U.Capability` instance.

```text
CapabilityUKindAdmissionDecision:
  CandidateSpelling: U.Capability
  Disposition: retained as dependent durable U-kind name
  E24Settlement: dependent capability instance under the named U.System holder settlement, governed here by A.2.2
  RootSubjectUKind: U.System holder whose ability is being stated
  DependentInstance: holder-dependent concrete U.Capability instance
  semanticArea: system ability, work admission, capability planning, and method threshold use
  ontologicalNeighborhood: U.System holder, U.SystemRoleAssignment, U.Method, U.MethodDescription, U.WorkPlan, U.Work, U.Characteristic, Q-Bundle, architecture-characteristic row, evidence relation, source-use relation, currentness assessment, and capability-fit predicate
  IdentityGroundingOrRecognitionRule: holder plus work family or result class plus envelope plus measure set plus qualification window plus currentness condition
  admissibleUse: state or test that a named holder can perform a Work family or produce a result class within declared bounds for planning, promise support, System, assignment, Method, and Work admission, or architecture-move feasibility
  nonUseBoundary: do not use U.Capability for statements, reports, evidence, source-use relations, currentness assessments, characteristics, Q-Bundles, architecture-characteristic rows, fit predicates, local system-role kinds, system-role assignments, MethodDescriptions, Work plans, or Work occurrences
  NonUSubstitutionBoundary: statements, evidence, source-use relations, currentness assessments, Q-Bundles, characteristics, architecture-characteristic rows, and fit predicates do not become U.Capability

ConcreteCapabilityInstance:
  CapabilityHolderRef: U.System
  WorkFamilyOrResultClassRef:
  CapabilityEnvelope:
  CapabilityMeasureSet:
  QualificationWindow:
  CapabilityCurrentnessCondition:
  DependentInstancePolicy: dependent on holder identity and declared envelope/measure/window boundary

SupportAndUseReferencesAroundCapability:
  CapabilityStatementRefs?: governed episteme or publication records that describe the instance
  EvidenceRelationRefs?: governed evidence relations that support reliance
  SourceUseRelationRefs?: governed source-use relations used to justify or constrain the statement
  CurrentnessAssessmentRefs?: dated assessment relations evaluating the currentness condition
  CapabilityFitConditionRefs?: admission predicates or gate relations that test this instance for a use
```

**CapabilityHolderRef.** The holder is an admitted `U.System`: a physical, cyber, socio-technical, organizational, team, composite-cell, deployed-software, or other System satisfying A.1 for this claim. A local system-role kind, assignment, Method, MethodDescription, Work record, episteme, publication, standard, or dashboard is not the capability holder merely because it appears in the sentence.

**WorkFamilyOrResultClassRef.** The ability is about a class of work the holder system can perform or a result class it can produce. The envelope may cite the exact `U.Method` that prospective Work occurrences would enact, or a separately identified `U.MethodDescription` whose claims constrain the capability use. Those references do not turn the Method or description into the holder, do not make the holder enact the Method, and do not establish that any candidate episteme is `U.MethodDescription`.

**CapabilityEnvelope.** The envelope states the bounded conditions under which the ability holds: input range, environment, resources, configuration, system version, calibration state, staffing composition, access constraints, safety limits, or other current conditions.

**CapabilityMeasureSet.** The measures state achieved or required bounds with units, scales, tolerances, success predicates, reliability, throughput, latency, precision, defect rate, or other declared characteristics. A measure may cite a `U.Characteristic`, Q-Bundle slot, or architecture-characteristic criteria row as an input for a capability-fit check, but that characteristic, Q-Bundle, or architecture row does not become the capability.

**QualificationWindow.** Capability is stable enough to plan with but not timeless. The instance may depend on software version, calibration horizon, team training state, wear, operating season, regulatory state, or other temporal currentness relation.

**CapabilityStatementRefs.** A `CapabilityStatement` is a governed episteme or publication-side record that says a capability instance exists, describes its holder, envelope, measures, and window, or cites it for planning. It is not `U.Capability`, but it is still a governed record under its own episteme or publication pattern.

**EvidenceRelationRefs and SourceUseRelationRefs.** Evidence, tests, certifications, prior work summaries, simulations, audit records, standards, and model results can justify a capability statement through direct evidence or source-use relations. These are governed relations or records. They do not become the capability and do not become its holder.

**CurrentnessAssessmentRefs.** A currentness assessment is a dated assessment relation saying whether the capability instance remains usable under its qualification window and current conditions. It is not the capability instance, but it is still a governed assessment relation. `CapabilityCurrentnessCondition` states what must remain true; an assessment evaluates that condition.

**CapabilityFitConditionRefs.** A capability-fit condition is an admission predicate, threshold, or gate relation that tests a holder capability and any declared characteristic, Q-Bundle, or architecture-characteristic inputs against a current local system-role-kind classification, exact assignment, Method step, WorkPlan, Work occurrence, ClaimScope, qualification window, or gate need. Unless a separate E.24.UK admission is written, it is not a `U.*` kind.

**Neighboring-term boundary.** When a neighboring pattern uses `U.WorkScope`, recover the set-valued condition part of `CapabilityEnvelope`: the inputs, environment, resources, configuration, and assumptions against which an intended work slice is checked. When it uses `U.WorkMeasures`, recover `CapabilityMeasureSet`. `JobSlice` names the intended work slice for a work-admission check. `QualificationWindow` names the temporal currentness relation for the capability instance. These are neighboring governed terms, not substitute names for `U.Capability`.



