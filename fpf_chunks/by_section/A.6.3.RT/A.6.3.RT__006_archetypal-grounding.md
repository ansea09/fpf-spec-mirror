---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__006_archetypal-grounding.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:5 — Archetypal grounding"
line_start: 12578
line_end: 12660
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.4"
  - "A.7"
  - "B.3"
  - "B.5.2"
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

#### A.6.3.RT:5.1 - Same-entity text-to-table shift
**Source slice.** `Service S showed three recurring latency spikes in the evening batch window. Trace T-44 and dashboard pin D-17 identify the same service and time window.`

**Published table slice.** `| Service | Window | Spike count | Source pins |
| Service S | Evening batch | 3 | T-44, D-17 |`

This is an admissible direct `RepresentationSchemeTransition` if no new claims are introduced, the same EntityOfConcern stays explicit, and the representation-factor delta is declared. In ordinary engineering use, this usually needs a visible source-relation chain, explicit loss notes if anything was omitted, and a clear statement that the table is still about the same service occurrence rather than a new EntityOfConcern.

#### A.6.3.RT:5.2 - Same-entity table-to-diagram shift
**Source table slice.** `| Node | Depends on |
| CoolingLoop | Sensor A |
| CoolingLoop | Valve B |`

**Published diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

The move stays in this pattern only if the EntityOfConcern is preserved, the diagram does not silently add new semantic commitments, and reasoning-medium change is declared. If the diagram starts asserting dependency theory not actually stated by the source table, the case must reopen and another governing pattern may apply.

#### A.6.3.RT:5.2.a - Correspondence-mediated text-to-table shift
**Source prose slice.** `In the safety view, CL-2 maintains the required temperature condition during standard operating demand.`

**Published table slice.** `| View | Entity | Condition | Correspondence model |
| Safety | CL-2 | required temperature condition during standard operating demand | CM-12 |`

The move stays in this pattern only if the correspondence remains explicit, the EntityOfConcern stays preserved, and the resulting table does not quietly import bridge semantics or a changed EntityOfConcern. Because the required correspondence witness is doing real work here, a source-bearing continuity note is often warranted instead of relying only on the rendered table.

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

If the published screen becomes honest only by omitting exceptions, confidence bands, or source distinctions and by carrying a narrower admissible use with source-bearing return, apply A.6.3.CSC Controlled Semantic Coarsening rather than keeping the case here as ordinary representation-scheme transition.

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

This does **not** remain ordinary RepresentationSchemeTransition if the tile is treated as more than a narrow report view. The tile foregrounds one causal branch and suppresses uncertainty and alternative branches, so it stays honest only with source-bearing return to the source-bearing worksheet and a non-admissible downstream-use line. It is not a causal proof, service status verdict, or action cue. Once that narrower-use card becomes primary, ordinary entityOfConcernRef-preserving representation-scheme transition no longer governs; apply A.6.3.CSC Controlled Semantic Coarsening rather than treating it as a normal scheme shift.

#### A.6.3.RT:5.5 - Boundary to decode-mediated latent cases
A user or decoding relation tries to restate a latent region or distributed feature cluster as explicit entity content or relation content. This stays outside the admissible entityOfConcernRef-preserving case under `A.6.3.RT` unless the pinned source claim or publication, decoding relation or access relation, recoverability evidence, admissible-use value, and remaining user action are already present. Readable decoded output alone is not enough.

#### A.6.3.RT:5.5.a - Guarded decode-mediated rendering
**Pinned source cluster.** `Probe run P-8 is tied to model-state log M-12 and evaluation bundle EV-4 for the same diagnostic case.`

**Published exploratory slice.** `A decoded rendering suggests a cluster that may correspond to the same failure episode already pinned in P-8, M-12, and EV-4. This rendering stays exploratory and report-only until the required recoverability evidence is published.`

This example remains guarded-open rather than green. The didactic point is that a decode-mediated rendering may still be useful, but it does not become a normal same-entity publication merely because the result looks readable.

