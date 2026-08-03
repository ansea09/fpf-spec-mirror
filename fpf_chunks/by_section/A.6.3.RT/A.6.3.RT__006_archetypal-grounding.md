---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__006_archetypal-grounding.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:5 — Archetypal grounding"
line_start: 14658
line_end: 14757
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
  - "C.2.1"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### A.6.3.RT:5 - Archetypal grounding

#### A.6.3.RT:5.1 - Same-entity text-to-table construction

Exact source episteme `LatencyFinding-X` has claim content stating three evening-batch latency spikes with trace and dashboard support, exact EntityOfConcern `Service-S-during-W`, and effective reference scheme `ServiceTelemetryScheme-4`. Exact receiving episteme `LatencyTable-Y` has table-structured claim content about the same exact EntityOfConcern under effective reference scheme `TabularTelemetryScheme-2`; it preserves the spike-count claim and source designations and omits the prose ordering.

`TabulateLatency : LatencyFinding-X -> LatencyTable-Y` states that exact construction, the relation between the schemes, the omission, prohibited strengthening, and inspection-only use. The visible table form and its file carrier are not `Y`. Unless an exact bounded model-use structure and actual representation-transformation Work also satisfy section 4.1.a.1, this example asserts the A.6.3 construction but not `RepresentationSchemeTransitionRelation@Context`.

#### A.6.3.RT:5.2 - Positive six-participant table-to-diagram occurrence

Exact source episteme `CoolingLoopRelationTable-X` states two already governed connection claims about exact EntityOfConcern `CoolingLoop-7` under effective reference scheme `TabularPlantScheme-5`. Exact receiving episteme `CoolingLoopDependencyDiagram-Y` states the same two claims in diagrammatic claim content about `CoolingLoop-7` under effective reference scheme `DirectedDiagramPlantScheme-3`; it is a candidate episteme, not automatically a `U.View`.

Exact scheme-description epistemes `TabularPlantSchemeDescription-5` and `DirectedDiagramPlantSchemeDescription-3` concern their respective schemes and state their interpretation rules. Independently selected `CoolingLoopReviewModelUseStructure` satisfies A.1.1 because its exact model-use organization changes this review use. System `PlantModelingTool-2`, under exact role assignment, performs dated Work `CoolingLoopDiagrammingWork-18`; its governed bindings use the selected structure, `CoolingLoop-7`, `X`, `Y`, and both scheme descriptions. Exact construction `DiagramCoolingLoop : X -> Y` states the source-to-receiving claim rule, scheme relation, preserved connection claims, omitted table-cell qualifiers, prohibited strengthening, and applicability.

Only with all those facts does this occurrence obtain:

```text
RepresentationSchemeTransitionRelation@Context(
  CoolingLoopReviewModelUseStructure,
  CoolingLoop-7,
  CoolingLoopRelationTable-X,
  CoolingLoopDependencyDiagram-Y,
  TabularPlantSchemeDescription-5,
  DirectedDiagramPlantSchemeDescription-3)
```

The transition-description episteme has this exact occurrence as EntityOfConcern. Its claim content cites `CoolingLoopDiagrammingWork-18`, `DiagramCoolingLoop`, the exact source connection relations, the omitted qualifier, topology-inspection use, the blocked control-timing/work-order inference, and return to `X` when qualifiers matter. It also states the example-level representation and reasoning-medium deltas—rows become directed diagram edges and pairwise lookup becomes topology inspection—and the recoverability mechanism that each edge links to its exact source-table relation in `X`. A later publication occurrence, diagram form, or SVG carrier remains separate. `Y` is a `U.View` only if an exact E.17.0 conformance occurrence independently obtains.

#### A.6.3.RT:5.2.a - Correspondence-mediated text-to-table shift
**Source prose slice.** `In the safety view, CL-2 maintains the required temperature condition during standard operating demand.`

**Published table slice.** `| View | Entity | Condition | Correspondence model |
| Safety | CL-2 | required temperature condition during standard operating demand | CM-12 |`

This case stays only if exact text-source episteme `X`, exact table episteme `Y`, and `v : X -> Y` are identified, their EntityOfConcern is the same, and every relied-on correspondence is an exact governed occurrence. The source prose form and table form are not endpoints; the correspondence record or visible row is not the relation.

#### A.6.3.RT:5.2.b - Same-entity diagram-to-structured-notation shift
**Source diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

**Published notation slice.** `dependsOn(CoolingLoop, SensorA)`
`dependsOn(CoolingLoop, ValveB)`

This remains under `RepresentationSchemeTransition` when the notation states the same relation line already visible in the diagram, the EntityOfConcern remains preserved, and no additional dependency theory is silently imported by the notational rendering.

#### A.6.3.RT:5.2.c - Functional-description diagram, table, or screen shift

**Source slice.** `The mixing cell transfers liquid from Tank A through heat exchanger H-2 to reactor R-4; the source description is about the same declared functional slice and keeps instrumentation claims and control claims outside this relation.`

**Published table or screen slice.** `| Function relation | Source | Target | Limit |`
`| transfer and heat before reaction | Tank A | R-4 via H-2 | no control-loop claim |`

This remains `RepresentationSchemeTransition` only when the same EntityOfConcern is preserved and the table or screen changes representation scheme or reasoning medium without adding performed-work order, module structure, evidence, gate passage, or control architecture. If the diagram, table, or screen turns the receiving representation into a functional, control, or flow architecture claim rather than re-rendering the already declared functional slice, apply `A.6.4`, `OntologicalReframing`, or `E.18` as applicable. If the diagram order is explanatory, causal, dependency-like, or didactic, do not treat it as physical time order or performed-work sequence unless that temporal claim is present in the source episteme and separately admissible. If a parser step or OCR step only extracts pixels, text, or carrier layout from a scanned diagram or screen, start with `A.7`; apply this pattern only when the extracted structure is being treated as an entityOfConcernRef-preserving representation of source `U.Episteme` claims with source-relation chain and loss notes visible.

If exact receiving episteme `Y`, exposed through the screen, remains honest only by omitting exceptions, confidence bands, or source distinctions and carrying a narrower use plus return to exact `X`, apply CSC. The screen form or carrier alone is neither `Y` nor a controlled-coarsening construction.

#### A.6.3.RT:5.3 - Boundary to textual rewrite
A source prose note is shortened, reordered, or translated but remains essentially textual. That case stays with `ConservativeRetextualization`, not this pattern.

#### A.6.3.RT:5.4 - Boundary to explanation-facing renderings
A representation shift is performed mainly to teach or narrate rather than to publish another same-entity representation regime. That case leaves this pattern and is reviewed under explanation governance.

#### A.6.3.RT:5.4.a - Boundary to bridge-bearing comparison
**Source slice.** `Local reliability note: Pump P-2 remained within operating range during test window W-3.`

**Published comparative slice.** `Pump P-2 in W-3 behaves like Unit U-7 in Plant B and can therefore be treated as operationally equivalent for this comparison.`

This does **not** stay in RepresentationSchemeTransition. The rendering has changed from an entityOfConcernRef-preserving representation shift to comparative or bridge-bearing interpretation across contexts. Once the publication starts asserting cross-context equivalence, substitution, or comparative licence, the case is governed by explicit bridge-governed review.

#### A.6.3.RT:5.4.b - Boundary to carrier work and export work
**Source rendering slice.** `| Service | Window | Spike count | Source pins |`

**Published export slice.** `latency-report.csv` and dashboard PNG generated from the same table.

This also stays outside `RepresentationSchemeTransition`. The representation scheme was already chosen; what follows is carrier formatting, export, packaging, or rendering work on that representation. The didactic point is that not every change in visible form is a new entityOfConcernRef-preserving representation transition.

#### A.6.3.RT:5.4.c - Boundary to coarsened dashboard view
**Source slice.** `The incident worksheet tracks three causal branches, two confidence bands, and one still-open ambiguity note for Service S.`

**Published dashboard tile.** `Service S: current dashboard view foregrounds cache-failover evidence; alternative branches and confidence bands remain in the incident worksheet.`

This does **not** remain ordinary RepresentationSchemeTransition if the tile is treated as more than a narrow report view. The tile foregrounds one causal branch and suppresses uncertainty and alternative branches, so it stays honest only with an explicit return to the exact incident worksheet and its source relations, plus a non-admissible downstream-use line. It is not a causal proof, service status verdict, or action cue. Once that narrower-use card becomes primary, ordinary entityOfConcernRef-preserving representation-scheme transition no longer governs; apply A.6.3.CSC Controlled Semantic Coarsening rather than treating it as a normal scheme shift.

#### A.6.3.RT:5.4.d - Boundary to structure-to-narrative rendering

**Source structure slice.** `Architecture candidate C-2 has module split M, data-custody constraint D, placement constraint P, and unresolved latency versus maintainability trade-off T.`

**Published narrative slice.** `The team first tried to preserve module split M, then discovered that data custody D forced placement P, so candidate C-2 accepts latency residual T to keep maintainability within the selected range.`

This does not stay ordinary `RepresentationSchemeTransition` merely because prose is one representation of architecture. The receiving rendering orders selected source structures into a narrative path for a reader. Apply `A.6.3.NAR` for ordering rationale, preserved and lost structure, admissible use, and source return. Use RT only for any remaining representation-scheme shift that does not depend on narrative ordering.

#### A.6.3.RT:5.5 - Boundary to decode-mediated latent cases
A decode-mediated case stays outside RT until exact `X`, exact `Y`, `v`, the decoding/access relation, recoverability evidence, admissible use, and remaining user action are present. A latent region, feature cluster, probe result, source publication occurrence, or readable decoded output cannot fill an episteme endpoint.

#### A.6.3.RT:5.5.a - Guarded decode-mediated rendering
**Pinned source cluster.** `Probe run P-8 is tied to model-state log M-12 and evaluation bundle EV-4 for the same diagnostic case.`

**Published exploratory slice.** `A decoded rendering suggests a cluster that may correspond to the same failure episode already pinned in P-8, M-12, and EV-4. This rendering stays exploratory and report-only until recoverability evidence sufficient for that use is published.`

This example remains guarded-open rather than green. The didactic point is that a decode-mediated rendering may still be useful, but it does not become a normal same-entity publication merely because the result looks readable.

