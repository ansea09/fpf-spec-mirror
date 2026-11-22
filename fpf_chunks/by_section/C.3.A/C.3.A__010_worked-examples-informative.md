---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:9"
section_title: "Worked examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__010_worked-examples-informative.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:9 — Worked examples (informative)"
line_start: 59098
line_end: 59111
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

**E1 — Same-context braking claim.** A policy quantified over `Vehicle` pins `VehicleSignature@v4`; the receiver pins `PassengerCarSignature@v3`. Declaration admission establishes `SubkindOfObtains(PassengerCar, Vehicle; plantVehicleScheme)`.

Applying the policy to VIN-17 evaluates `J(VIN-17, PassengerCar, v3, S-plant)`; on `true`, C.3.1 monotonicity supplies the Vehicle-side consequence needed by the universal claim. If axle data are missing and the remaining facts do not settle this VIN’s classification, the judgement is `unknown` and the guard separately refuses the use.

**E2 — Cross-plant reuse.** An obtaining KindBridge relates source `Vehicle` to target `TransportUnit`; its assertion records a collapsed EV/ICE distinction and `CL^k=2`. The target signature is independently authored.

Plant B evaluates the candidate under its target edition. Suppose the source rule requires every mapped vehicle to carry the same identifier. It can apply where the mapping covers the target units and preserves that identifier requirement. A source rule specific to battery-electric vehicles needs to distinguish those vehicles. If Plant B's classification combines them with vehicles powered only by combustion, establish the propulsion type from another admissible source or restrict the rule to a supported subset. The `CL^k` rating alone supplies neither this distinction nor a numerical R decrement.

**E3 — API adapter.** A producer declares `Request`; a consumer expects `AuthenticatedRequest`. Declaration compatibility fails until an adapter and target declaration are recovered. For request `req-884`, suppose the other grounds establish neither the required condition nor its failure. If key-validation support is unavailable, the target judgement is `unknown` and the consumer refuses. An established failure of another necessary condition would already settle the target judgement as `false`.

**E4 — Masked clinic use.** The guard designates the exact `AdultPatient@Clinic` RoleMask declaration, base signature edition, candidate and slice. The mask label and a record entry can identify them. Age classification requires evidence for the applicable criterion. Suppose age of at least 21 is required. A verified age of at least 22 at that time satisfies the age condition. If the available record establishes only age of at least 18 and both 20 and 22 remain possible, the age condition is `unknown`.

