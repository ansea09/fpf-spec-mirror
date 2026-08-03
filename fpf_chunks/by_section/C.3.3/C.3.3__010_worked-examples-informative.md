---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:9"
section_title: "Worked Examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__010_worked-examples-informative.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:9 — Worked Examples (informative)"
line_start: 45297
line_end: 45310
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
  - "CL^k"
  - "KindBridge direct relation"
  - "R penalty"
  - "bridge assertion episteme"
  - "loss"
  - "target judgment"
---

### C.3.3:9 - Worked Examples (informative)

#### C.3.3:9.1 - Vehicle → TransportUnit (manufacturing)

Source kinds `Vehicle` and `PassengerCar`, target kinds `TransportUnit` and `PassengerTransportUnit`, and their exact declaration editions are independently identified. One KindBridge relation obtains from `Vehicle` to `TransportUnit` and another from `PassengerCar` to `PassengerTransportUnit` under the pinned scheme editions. The bridge assertion states that source fact `SubkindOfObtains(PassengerCar, Vehicle; sourceRS)` is preserved by target fact `SubkindOfObtains(PassengerTransportUnit, TransportUnit; targetRS)`, while the EV distinction is collapsed; it records `CL^k=2`, the lost battery-health invariants, and definedness limited to `registryAPI v1.4` in the selected time window. A candidate is classified only by `J(candidate, TransportUnit, transportUnitEdition, TargetSlice)` or the more specific target judgment when that receiving use is current. The independent scope-bridge and kind-bridge reliance penalties reduce R; F and G are unchanged.

#### C.3.3:9.2 - AuthenticatedRequest across services (software)

Source and target `AuthenticatedRequest` kinds and their exact declaration editions are independently identified. The bridge mapping predicate states the `authHeader` to `x-auth` correspondence and preservation of the signature-validity invariant; the bridge assertion gives `CL^k=3` and its definedness under `AuthStandard v2.3`. It does not construct the target declaration. The frontend evaluates each exact request with its target signature edition and slice; unavailable target dependencies yield `unknown`.

#### C.3.3:9.3 - AdultPatient across jurisdictions (clinical)

The obtaining bridge relates source kind `AdultPatient` to independently identified target kind `AdultPerson_Y`. Its assertion gives `CL^k=1`, states the 18-versus-21 boundary loss, and limits definedness to the declared jurisdictional editions. The target classification uses its own signature edition. Missing DOB support yields `unknown`; a mask adapter or narrower Scope may support a later use, while the guard's refusal and R penalty remain separate from target truth.

