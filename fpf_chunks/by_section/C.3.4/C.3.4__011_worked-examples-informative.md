---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:10"
section_title: "Worked Examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__011_worked-examples-informative.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:10 — Worked Examples (informative)"
line_start: 45580
line_end: 45593
dependencies:
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
keywords:
  - "RoleMask declaration episteme"
  - "candidate-feature constraint"
  - "masked judgment"
  - "stable-refinement review"
  - "vocabulary binding"
---

### C.3.4:10 - Worked Examples (informative)

#### C.3.4:10.1 - `Vehicle@ABSOnly` constraint use

The `RoleMask` declaration episteme designates `Vehicle`, pins its `KindSignature` edition, and adds the direct candidate-feature predicate `hasABS(candidate)=true`. For an exact vehicle and TargetSlice, evaluate `J_mask(vehicle, Vehicle, vehicleEdition, absMaskEdition, TargetSlice)`. Surface, speed, rig, and time remain Scope predicates. Missing ABS evidence gives `unknown`; a guard may decline use. If ABS becomes a stable conceptual distinction, identify local kind `VehicleWithABS` and establish an obtaining `U.SubkindOf` relation separately.

#### C.3.4:10.2 - `AuthenticatedRequest@Frontend` vocabulary use

The RoleMask declaration binds `authHeader` to local spelling `X-Auth` and adds no candidate criterion. The masked judgment therefore equals the base `J(request, AuthenticatedRequest, authEdition, slice)`. Another spelling, row, or field does not classify the request. Cross-context kind use still requires the exact KindBridge relation; local aliases alone require no MaskAdapter unless their correspondence is relied on across contexts.

#### C.3.4:10.3 - `AdultPatient@Clinic` composite use

The declaration pins the base adult-patient signature edition and adds the direct candidate-feature criterion `ageAt(patient, slice) >= 21`; `EHR system = X` remains Scope. A date-of-birth record may support the age claim, but record availability is not the patient feature or the mask criterion. In Jurisdiction Y, establish the KindBridge relation to the target kind, use a target RoleMask edition, and use a MaskAdapter declaration only for a changed age threshold or interpretation. Evaluate the exact target `J_mask`. An unavailable date-of-birth dependency yields `unknown`; the guard declines use separately and R receives only the justified bridge penalties.

