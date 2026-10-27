---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__006_archetypal-grounding.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:5 — Archetypal Grounding"
line_start: 128503
line_end: 128534
dependencies:
  - "A.10"
  - "A.10.1"
  - "A.13"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.2.4"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.24.PUB"
  - "F.10"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.9"
keywords:
  - "EvidenceGraph"
  - "NotCarried"
  - "PathCitationRecord"
  - "PathId"
  - "PathSliceId"
  - "actual-use relation"
  - "direct governors"
  - "downstream work"
  - "exact direct relations"
  - "exact represented objects"
  - "local refresh"
  - "obtaining claims"
  - "provenance ledger"
  - "representation correspondence"
  - "source/currentness"
  - "unresolved gaps"
---

### G.6:5 - Archetypal Grounding

#### G.6:5.1 - Measurement, acceptance, and decision

In this constructed case, a measurement team performs dated C.16 measurement Work with bindings for the pressure measurand, detector, calibration, model, input quantities and uncertainty propagation. Its pressure measurement result is stated in a distinct C.2.1 episteme. An evaluation team later performs G.4 `EvaluationWork`, applying one declared acceptance clause through exact A.6.1 bindings and obtaining `unknown`; another C.2.1 episteme states that verdict. A decision maker then performs C.11 decision Work, uses the verdict episteme through an exact premise relation and defers. The performer and Work references are independently established under §4.1.

G.6 may give this chain one `PathId` only after the measurement, work, binding, result, episteme, clause-application, premise, and decision relations are independently established. Its nodes keep raw detector output, indication, actual pressure, measurement result, verdict, and decision distinct. Its edges cite the exact relations; none produces the work, verdict, or decision.

#### G.6:5.2 - Resource aggregation

An engine programme has several C.16 resource measurements, dated test-run Work occurrences, exact phase and overlap relations, and a shared warm-up allocation rule. An aggregation team performs dated B.1.6 aggregation Work, applies `ProgrammeResourcePolicy-v3` and obtains a typed resource vector with propagated uncertainty; a distinct C.2.1 episteme states it. The path uses the independently established performer and Work refs.

The G.6 path cites every measurement result and episteme, the work-set and overlap relations, the edition-pinned policy, aggregation work, aggregation result, sources, and representation refs. Epoch labels alone do not establish work-part relations. Warm-up energy allocation and uncertainty propagation are performed in the aggregation work; an emissions verdict remains a separate result.

#### G.6:5.3 - Produced model and benchmark use

A training team performs dated training Work with exact actual bindings and, when an inception or completion claim is current, one local A.15.PROD claim. An evaluation team separately performs benchmark-evaluation Work, applies its declared method and dataset edition and obtains a result under the benchmark's direct governor; a C.2.1 episteme states that result. Both Work occurrences use their independently established performer refs. E.17 governs the model card's source-backed face and return to the selected claims, E.24.PUB their actual audience availability, and C.29 any consumed representation correspondence. G.11 supplies currentness when later use depends on edition or freshness.

A G.6 `PathSliceId` may cite that dependency chain for replication. The graph does not infer training from the model's presence, participation from a roster, evaluation from the protocol, superiority from the score, or deployment permission from the model card.

#### G.6:5.4 - Dashboard status cue

A dashboard cell shows `Ready`. F.10 governs the status-use classification; A.10 recovers the source and provenance for bounded reliance, with query Work, currentness, and a live rival explanation when those facts affect the claim. G.6 is entered only when a downstream audit or release package needs a stable path through those already established relations. The visible cue, graph path, and ledger row establish neither gate passage nor release.

#### G.6:5.5 - One calibration basis, several receiving paths

In a constructed inspection account, `Path-P1` connects measurement result M1 to acceptance result V1, and `Path-P2` connects M2 to V2. Both measurements use the same calibration qualification K through independently established relations. A later selection S uses both acceptance results. `Path-P3`, stored in the same publication, uses a different calibration and supports an unrelated result.

A correction to K first appears in P1's projection. The ledger's indexes also locate P2, and the receiving-use relations lead from V1 and V2 to S. Reconsider both branches and S under their subject patterns. P3 stays outside this reach because it does not consume the changed qualification. Two paths citing K still cite one common basis; their count supplies no independent corroboration. If the index cannot cover another receiving store, state that discovery limit and use A.10.1 when the receiving question needs that search.

The resulting G.6 account identifies the affected paths and their exact dependencies. G.11:5 continues this case through different branch outcomes and selection of the needed work.

