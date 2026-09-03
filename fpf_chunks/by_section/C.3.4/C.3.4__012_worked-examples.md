---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:10"
section_title: "Worked Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__012_worked-examples.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:10 — Worked Examples"
line_start: 46213
line_end: 46228
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

`VehicleABSUse-2026` designates `Vehicle`, pins its signature, and adds the governed candidate condition that the vehicle has ABS. A physical vehicle in the declared slice is admissible; missing ABS support yields `unknown`, while a non-vehicle input is `not-applicable`. Surface, rig, and time conditions used only to bound the claim remain Scope. If ABS becomes a stable classification distinction, recover another kind and test its subkind relation separately.

#### C.3.4:10.2 - `AuthenticatedRequest@Frontend` Vocabulary Use

`FrontendAuthHeaderUse-2026` binds `authHeader` to local spelling `X-Auth` and adds no candidate condition. Its judgment therefore equals the admissible base judgment. Moving the same exact request kind to another team requires a fresh receiving evaluation but no `KindBridge` merely because the team or spelling changed. If two independently identified request kinds differ, establish any bridge separately.

#### C.3.4:10.3 - `AdultPatient@Clinic` Composite Use

`ClinicAdultPatientUse-2026` pins the base adult-patient signature and adds the candidate condition `ageAt(patient, slice) >= 21`; the chosen clinic and claim window remain separately governed scope/applicability values. A person in the declared candidate domain is admissible; unavailable birth support yields `unknown`.

In Jurisdiction Y, first compare the exact patient-kind membership distinctions. If the same kind continues, use the Y declaration and evaluate afresh without a bridge. If the threshold or interpretation makes a distinct target kind and a directional correspondence is relied on, establish the `KindBridge`. A separate adaptation-correspondence declaration may then state how the two exact use declarations differ. Neither object transfers source truth.

