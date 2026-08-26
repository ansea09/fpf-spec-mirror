---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge and CL^k — Cross-local Correspondence between Distinct Kinds"
section_id: "C.3.3:9"
section_title: "Worked Examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__010_worked-examples-informative.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "C.3.3 — KindBridge and CL^k — Cross-local Correspondence between Distinct Kinds"
  - "C.3.3:9 — Worked Examples (informative)"
line_start: 44509
line_end: 44522
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
---

### C.3.3:9 - Worked Examples (informative)

#### C.3.3:9.1 - Vehicle → TransportUnit (manufacturing)

Source kinds `Vehicle` and `PassengerCar`, target kinds `TransportUnit` and `PassengerTransportUnit`, and their exact declaration editions are independently identified. One KindBridge relation obtains from `Vehicle` to `TransportUnit` and another from `PassengerCar` to `PassengerTransportUnit` under the pinned scheme editions. The bridge assertion states that source fact `SubkindOfObtains(PassengerCar, Vehicle; sourceRS)` is preserved by target fact `SubkindOfObtains(PassengerTransportUnit, TransportUnit; targetRS)`, while the EV distinction is collapsed; it records `CL^k=2`, the lost battery-health invariants, and definedness limited to `registryAPI v1.4` in the selected time window. A candidate is first checked for admissibility and then classified by the exact receiving declaration; source classification is not copied. If the receiving claim also relies on an independently established scope translation, that relation's consequence remains separate from the kind-bridge consequence; F and G are unchanged.

#### C.3.3:9.2 - Same AuthenticatedRequest kind across services — no bridge

Frontend and gateway services use the same `AuthenticatedRequest` kind: the candidate request domain, signature-validity condition, and intended member/non-member distinction are aligned. Each service uses its selected declaration edition and evaluates the request afresh. The gateway spelling `x-auth` may require an F.9 sense relation or a C.3.4 vocabulary binding when that wording use is relied on, but the service boundary and spelling alone create neither another kind nor a `KindBridge`.

#### C.3.3:9.3 - AdultPatient across jurisdictions (clinical)

The obtaining bridge relates source kind `AdultPatient` to independently identified target kind `AdultPerson_Y`. Its assertion gives `CL^k=1`, states the 18-versus-21 boundary loss, and limits definedness to the declared jurisdictional editions. The target classification uses its own signature edition. Missing DOB support yields `unknown`; a mask adapter or narrower Scope may support a later use, while the guard's refusal and R penalty remain separate from target truth.

