---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:10"
section_title: "Worked Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__012_worked-examples.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:10 — Worked Examples"
line_start: 45432
line_end: 45447
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
---

### C.3.4:10 - Worked Examples

#### C.3.4:10.1 - `Vehicle@ABSOnly` Constraint Use

`VehicleABSUse-2026 : KindUseAdaptationDeclaration` designates `Vehicle`, pins its `KindSignature` edition, and adds the direct candidate-feature predicate `hasABS(candidate)=true`. For one vehicle and `TargetSlice`, evaluate `J_kindUse(vehicle, Vehicle, vehicleEdition, absUseEdition, TargetSlice)`. Surface, speed, rig, and time remain Scope predicates. Missing ABS evidence gives `unknown`; a guard may decline use. If ABS becomes a stable conceptual distinction, identify local kind `VehicleWithABS` and establish an obtaining `U.SubkindOf` relation separately.

#### C.3.4:10.2 - `AuthenticatedRequest@Frontend` Vocabulary Use

`FrontendAuthHeaderUse-2026 : KindUseAdaptationDeclaration` binds `authHeader` to local spelling `X-Auth` and adds no candidate criterion. Its judgment therefore equals the base `J(request, AuthenticatedRequest, authEdition, slice)`. Another spelling, row, or field does not classify the request. Cross-context kind use still requires the exact `KindBridge`; local aliases need no correspondence declaration unless their correspondence is relied on across contexts.

#### C.3.4:10.3 - `AdultPatient@Clinic` Composite Use

`ClinicAdultPatientUse-2026 : KindUseAdaptationDeclaration` pins the base adult-patient signature edition and adds the direct candidate-feature criterion `ageAt(patient, slice) >= 21`; `EHR system = X` remains Scope. A date-of-birth record may support the age claim, but record availability is not the patient feature or adaptation criterion.

In Jurisdiction Y, establish the `KindBridge` to the independently identified target kind and use a target adaptation declaration. If the age threshold or interpretation differs, add a `KindUseAdaptationCorrespondenceDeclaration` whose endpoints are the two exact adaptation declarations and whose content states direction, rule, loss, and definedness. That declaration creates no Bridge or target truth. Evaluate the target `J_kindUse`; an unavailable date-of-birth dependency yields `unknown`, the guard declines use separately, and R receives only justified Bridge penalties.

