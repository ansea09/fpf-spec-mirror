---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge and CL^k — Correspondence between Distinct Kinds"
section_id: "C.3.3:9"
section_title: "Worked Examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__010_worked-examples-informative.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "C.3.3 — KindBridge and CL^k — Correspondence between Distinct Kinds"
  - "C.3.3:9 — Worked Examples (informative)"
line_start: 58460
line_end: 58477
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

Source kinds `Vehicle` and `PassengerCar`, target kinds `TransportUnit` and `PassengerTransportUnit`, and their declaration editions are independently identified. One KindBridge relation obtains from `Vehicle` to `TransportUnit` and another from `PassengerCar` to `PassengerTransportUnit` under the pinned scheme editions.

The bridge assertion states that source fact `SubkindOfObtains(PassengerCar, Vehicle; sourceRS)` is preserved by target fact `SubkindOfObtains(PassengerTransportUnit, TransportUnit; targetRS)`, while the EV distinction is collapsed; it records `CL^k=2`, the lost battery-health invariants, and definedness limited to `registryAPI v1.4` in the selected time window.

A candidate is first checked for admissibility and, if admissible, then classified by the receiving declaration; source classification is not copied. If the receiving claim also relies on an independently established scope translation, that relation's consequence remains separate from the kind-bridge consequence; the kind-bridge consequence leaves F and G unchanged.

#### C.3.3:9.2 - Same AuthenticatedRequest kind across services — no bridge

Frontend and gateway services use the same `AuthenticatedRequest` kind: the candidate request domain, signature-validity condition, and intended member/non-member distinction are aligned. Each service uses the declaration edition and conditions that apply at its boundary. A trusted earlier judgment can settle the gateway’s question when it concerns the same request and covers the gateway’s criterion and validity window. A rule requiring the gateway to run its own check still calls for that check. The gateway spelling `x-auth` may require a C.3.4 vocabulary binding when that wording use is relied on; an F.9 sense relation is added only if that use also needs a relation between distinct local senses. The service boundary and spelling alone create neither another kind nor a `KindBridge`.

#### C.3.3:9.3 - AdultPatient across jurisdictions (clinical)

The obtaining bridge relates source kind `AdultPatient` to independently identified target kind `AdultPerson_Y`. In this example the source age threshold is 18 and the target threshold is 21. The assertion gives `CL^k=1` and states the jurisdictional editions and the age distinction lost in the correspondence. For an admissible candidate who meets the other target conditions, a verified source classification at 18 or older leaves the target age condition open if both 20 and 22 are possible. A verified lower age bound of 22 on the target date settles it without an exact date of birth. The receiving guard can refuse a use that requires positive classification while the age condition is unresolved. A later request for classification can use any evidence admitted by the target rule that settles the threshold. A separately required birth-date record remains a distinct deliverable.

