---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__006_archetypal-grounding.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:5 — Archetypal grounding"
line_start: 15082
line_end: 15171
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.NAR"
  - "A.6.4"
  - "A.7"
  - "B.3"
  - "B.5.2"
  - "B.5.2.0"
  - "C.2.1"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "C.29"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18"
  - "E.24.PUB"
  - "F.9"
keywords:
---

### A.6.3.RT:5 - Archetypal grounding

#### A.6.3.RT:5.1 - Ordinary same-concern text-to-table move

**Source slice.** `Service S showed three recurring latency spikes in the evening batch window. Trace T-44 and dashboard pin D-17 concern the same service and time window.`

**Target table.**

| Service | Window | Spike count | Source pins |
| --- | --- | --- | --- |
| Service S | Evening batch | 3 | T-44, D-17 |

The first result needs no endpoint dossier. The note says comparison across rows becomes easier; the service/window claim, count, and pins survive; prose order is lost; no causal or severity claim is added; use is inspection; and any qualifier or causal question returns to the source note and traces.

If the table is independently cited or disputed, exact source episteme `LatencyFinding-X` and receiving episteme `LatencyTable-Y` concern `Service-S-during-W` under effective schemes `ServiceTelemetryScheme-4` and `TabularTelemetryScheme-2`. `TabulateLatency : LatencyFinding-X -> LatencyTable-Y` records the exact construction, scheme relation, preservation, omission, prohibited strengthening, and inspection-only use. The visible table form and file carrier are not `Y`.

#### A.6.3.RT:5.2 - Positive later-specific table-to-diagram occurrence

Exact source episteme `CoolingLoopRelationTable-X` and exact receiving episteme `CoolingLoopDependencyDiagram-Y` state the same two connection claims about `CoolingLoop-7` under effective schemes `TabularPlantScheme-5` and `DirectedDiagramPlantScheme-3`. `Y` is a candidate episteme, not automatically a `U.View`.

Scheme-description epistemes `TabularPlantSchemeDescription-5` and `DirectedDiagramPlantSchemeDescription-3` concern their respective schemes and state their interpretation rules. Independently selected `CoolingLoopReviewModelUseStructure` satisfies A.1.1 because its model-use organization changes this review. System `PlantModelingTool-2`, under an exact system-role assignment, performs dated `CoolingLoopDiagrammingWork-18`; its bindings use all six participants. `DiagramCoolingLoop : X -> Y` states the exact claim rule, scheme relation, preserved connection claims, omitted table qualifiers, prohibited strengthening, and applicability.

Only then does this occurrence obtain:

```text
RepresentationSchemeTransitionRelation@Context(
  CoolingLoopReviewModelUseStructure,
  CoolingLoop-7,
  CoolingLoopRelationTable-X,
  CoolingLoopDependencyDiagram-Y,
  TabularPlantSchemeDescription-5,
  DirectedDiagramPlantSchemeDescription-3)
```

Its transition-description episteme cites the Work, construction, exact source relations, omitted qualifiers, topology-inspection use, blocked control-timing/work-order inference, and return to `X`. Rows become directed edges; pairwise lookup becomes topology inspection; each edge links back to its source-table relation. Publication, diagram form, and SVG carrier remain separate. `Y` is a `U.View` only if E.17.0 conformance independently obtains.

#### A.6.3.RT:5.2.a - Correspondence-mediated text-to-table shift

**Source prose.** `In the safety view, CL-2 maintains the required temperature condition during standard operating demand.`

**Target row.** `| Safety | CL-2 | required temperature condition during standard operating demand | CM-12 |`

The case stays RT only when exact `X`, exact `Y`, and `v : X -> Y` are identified for reliance-facing use, their EntityOfConcern is the same, and every relied-on correspondence is an exact governed occurrence. The visible row and correspondence record are not that relation.

#### A.6.3.RT:5.2.b - Same-concern diagram-to-structured-notation shift

**Source diagram.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

**Target notation.** `dependsOn(CoolingLoop, SensorA)` and `dependsOn(CoolingLoop, ValveB)`

This remains RT when the notation carries the same relation line and adds no dependency theory. If `dependsOn` has stronger semantics than the source arrows, that added claim must be removed or separately established.

#### A.6.3.RT:5.2.c - Functional-description diagram, table, or screen shift

A source description says that a mixing cell transfers liquid from Tank A through heat exchanger H-2 to reactor R-4, while keeping instrumentation and control claims outside. A target table foregrounds the transfer path. This remains RT only while the same functional slice is represented without adding performed-work order, module structure, evidence, gate passage, or control architecture.

Explanatory diagram order is not physical time or Work order unless the source states that temporal claim. OCR or parsing that merely extracts pixels, text, or layout starts with A.7. If the target becomes honest only by omitting exceptions, confidence bands, or source distinctions under a narrower use, use A.6.3.CSC.

#### A.6.3.RT:5.3 - Boundary to textual rewrite

A prose note is shortened, reordered, or translated but remains in the same textual regime. Use A.6.3.CR rather than inventing RT.

#### A.6.3.RT:5.4 - Boundary to explanation-facing rendering

A representation is changed mainly to teach or explain an existing face. E.17.EFP is primary; RT remains only for a separately material scheme transition.

#### A.6.3.RT:5.4.a - Boundary to bridge-bearing comparison

A local reliability note about Pump P-2 becomes a comparison claiming operational equivalence with Unit U-7 in another plant. That is not merely representation change. Keep any local representation delta in RT and establish the cross-context equivalence or substitution under the applicable F.9 relation.

#### A.6.3.RT:5.4.b - Boundary to carrier work

A table is exported as CSV and dashboard PNG after its representation scheme was chosen. The later activity is carrier formatting, export, packaging, or rendering Work, not another RT merely because the visible form changed.

#### A.6.3.RT:5.4.c - Boundary to coarsened dashboard view

An incident worksheet carries three causal branches, two confidence bands, and an open ambiguity; a dashboard tile foregrounds only cache-failover evidence. If the tile needs a narrower-use card, non-admissible action line, and explicit return to the worksheet, A.6.3.CSC is primary. The tile is not causal proof, service-status verdict, or action cue.

#### A.6.3.RT:5.4.d - Boundary to structure-to-narrative rendering

**Source structure.** `Architecture candidate C-2 has module split M, data-custody constraint D, placement constraint P, and unresolved latency versus maintainability trade-off T.`

**Narrative.** `The team first tried to preserve M, then found that D forced P, so C-2 accepts latency residual T to preserve maintainability.`

The main move is ordering selected structures into a reader path. Apply A.6.3.NAR for ordering, connective account, preservation/loss, use, and source return. Use RT only for a remaining representation-scheme shift that does not depend on that narrative ordering.

#### A.6.3.RT:5.5 - Guarded decode-mediated rendering

Probe run P-8 is tied to model-state log M-12 and evaluation bundle EV-4. A decoded rendering suggests a cluster corresponding to the same failure episode. The result remains exploratory and report-only until the decoding/access relation and recoverability evidence support that use. A latent region, feature cluster, probe result, source publication, or readable output fills no episteme endpoint.

