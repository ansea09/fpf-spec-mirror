---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:9"
section_title: "Worked examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__010_worked-examples-informative.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:9 — Worked examples (informative)"
line_start: 45168
line_end: 45177
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1-C.3.5"
keywords:
  - "ESG"
  - "Method-Work"
  - "assurance"
  - "declaration compatibility"
  - "exact candidate judgment"
  - "guard refusal"
  - "regulatory"
  - "true/false/unknown"
---

### C.3.A:9 - Worked examples (informative)

**E1 — Same-context braking claim.** A policy quantified over `Vehicle` pins `VehicleSignature@v4`; the receiver pins `PassengerCarSignature@v3`. Declaration admission establishes `SubkindOfObtains(PassengerCar, Vehicle; plantVehicleScheme)`. Applying the policy to VIN-17 evaluates `J(VIN-17, PassengerCar, v3, S-plant)`; on `true`, C.3.1 monotonicity supplies the Vehicle-side consequence needed by the universal claim. A missing axle dependency yields `unknown` and a separate refusal.

**E2 — Cross-plant reuse.** An obtaining KindBridge relates source `Vehicle` to target `TransportUnit`; its assertion records a collapsed EV/ICE distinction and `CL^k=2`. The target signature is independently authored. Plant-B evaluates its exact vehicle candidate under that target edition; the source result is only support, and bridge consequences lower R.

**E3 — API adapter.** A producer declares `Request`; a consumer expects `AuthenticatedRequest`. Declaration compatibility fails until an adapter and target declaration are recovered. For request `req-884`, unavailable key-validation support yields target `unknown`; the consumer refuses without asserting that the request is known unauthenticated.

**E4 — Masked clinic use.** The guard designates the exact `AdultPatient@Clinic` RoleMask declaration, base signature edition, patient candidate, and slice. Unavailable date-of-birth support yields `unknown`; the mask label and EHR row do not classify the patient.

