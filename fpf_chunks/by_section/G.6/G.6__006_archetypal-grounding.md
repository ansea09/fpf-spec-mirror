---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__006_archetypal-grounding.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:5 — Archetypal Grounding"
line_start: 103722
line_end: 103745
dependencies:
  - "A.10"
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

C.16 dated measurement work binds the pressure measurand, detector, calibration, model, input quantities, and uncertainty propagation and obtains a pressure measurement result. A distinct C.2.1 episteme states that result. Later G.4 `EvaluationWork` applies one declared acceptance clause through exact A.6.1 bindings and obtains `unknown`; another C.2.1 episteme states that verdict. Later C.11 decision work uses the verdict episteme through an exact premise relation and defers.

G.6 may give this chain one `PathId` only after the measurement, work, binding, result, episteme, clause-application, premise, and decision relations are independently established. Its nodes keep raw detector output, indication, actual pressure, measurement result, verdict, and decision distinct. Its edges cite the exact relations; none produces the work, verdict, or decision.

#### G.6:5.2 - Resource aggregation

An engine programme has several C.16 resource measurements, dated test-run work occurrences, exact phase and overlap relations, and a shared warm-up allocation rule. B.1.6 dated aggregation work applies `ProgrammeResourcePolicy-v3` and obtains a typed resource vector with propagated uncertainty; a distinct C.2.1 episteme states it.

The G.6 path cites every measurement result and episteme, the work-set and overlap relations, the edition-pinned policy, aggregation work, aggregation result, sources, and representation refs. The ledger does not make epoch labels into work parts, allocate the warm-up energy, perform uncertainty propagation, or turn the aggregate into an emissions verdict.

#### G.6:5.3 - Produced model and benchmark use

Dated training work has exact actual bindings and, when an inception or completion claim is current, one local A.15.PROD claim. Separate benchmark-evaluation work applies its declared method and dataset edition and obtains a result under the benchmark's direct governor; a C.2.1 episteme states that result. A source publication and model card expose selected claims under E.17/C.29 relations. G.11 supplies currentness when later use depends on edition or freshness.

A G.6 `PathSliceId` may cite that dependency chain for replication. The graph does not infer training from the model's presence, participation from a roster, evaluation from the protocol, superiority from the score, or deployment permission from the model card.

#### G.6:5.4 - Dashboard status cue

A dashboard cell shows `Ready`. F.10 governs the status-use classification; A.10 recovers the source, query work, provenance, currentness, bounded reliance, and rival explanation. G.6 is entered only when a downstream audit or release package needs a stable path through those already established relations. The visible cue, graph path, and ledger row establish neither gate passage nor release.

