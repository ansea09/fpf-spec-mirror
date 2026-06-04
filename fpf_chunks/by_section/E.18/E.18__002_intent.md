---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__002_intent.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:1 — Intent"
line_start: 65945
line_end: 65987
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:1 - Intent

Provide a **notation‑independent** architecture for graphs whose vertices are **morphisms (transductions)** and whose edges are **typed transfers**. The architecture is **agnostic to the concrete morphism set** and equips the graph with **publication, comparability, crossing, and budget** disciplines so that **flows** are **valuations over paths** within the same graph object. Faces appear via **MVPK**; numeric/comparable publication carries **pins** with **Bridge/CL** notes; Φ/CL^plane penalties remain in **R**.
**Admissibility wording.** E.TGA criteria are model conditions: if the declared graph, path, crossing, or publication conditions hold, the E.TGA explanation applies; otherwise it does not apply. Duty verbs appear only in named conformance minima.

**Use this when.** Use E.TGA when the live question is whether a project description needs one transduction graph relation, one graph crossing, or one flow valuation over `U.Transfer` rather than an ordered work and method narrative.

**First useful move.** Name the graph object, the node kinds, the single `U.Transfer` edge kind, and the exact crossing or path slice whose pins are required.

**Smallest sufficient graph and path guidance.** Use the lightest graph and path guidance that preserves the next admissible practitioner move. Add extra pins, witnesses, `DecisionLog` detail, `CrossingBundle`, `PQG`/`RSCR`, or MIP-run material only when the live claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient next move.** For the ordinary case, name `TransductionGraph`, the active `PathId` or `PathSliceId` when a path or slice is live, the node kinds, one `U.Transfer`, and only the crossings or pins that are live. If there is no crossing, comparison, launch, or refresh claim, do not open `CrossingBundle`, `GateProfile`, or `DecisionLog`.

**Do not escalate when.** Do not create a graph kind from semio wording, lineage metadata, tool-pipeline order, or reference-flow prose. Keep those as source wording or neighboring-pattern relation prose unless a live `TransductionGraph`, path, flow valuation, or crossing relation is being governed here.

**Same problem, different live question.** For a TGA-looking problem, use `E.18` for graph/flow/crossing, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is live.

**Semantic repair return.** When E.TGA blocks a misleading word, face, alias, or source label, the repair returns to the enabled graph, path, or crossing action: name the graph relation, path or flow valuation, or crossing boundary that remains admissible. Do not stop at a classification of vocabulary or publication faces.

**Governed-object and relation separation.** Keep the graph object and path or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-governing definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence carrier, MIP manifest, or work witness does not carry another pattern's project-side value unless that exact governing pattern consumes it for that relation.

**Smallest affected locus.** Localize the change to the smallest live locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated smallest affected locus when that locus is enough.

**Ordinary success.** For ordinary E.TGA use, success is that the graph object, path or slice, single `U.Transfer` edge kind, and any live crossing boundary are placed without hidden work and method order or hidden scalarization. A full conformance pass is needed only when the downstream claim consumes expanded assurance or conformance material.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, TGA `Check` distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field liveness.** Always core for E.TGA: graph object, node kinds, one `U.Transfer`, and the path or slice being governed. Conditional-live: `CrossingBundle`, `GateProfile`, `DecisionLog`, `ViewpointMap`, evidence carriers, refresh pins, and launch/work-boundary fields; open them only when the corresponding crossing, publication, evidence, refresh, gate, or work-boundary claim is live.

**Retrieval trap guard.** When excerpted alone, E.TGA vocabulary is not read as governing `GateCheckRef`, full viewpoint taxonomy, or gate publication semantics. `A.21` governs gate publication, `E.17` governs MVPK faces, and S12-style viewpoint material is conditional viewpoint-mapping input, not the graph architecture itself.

**Anti-Goodhart guard.** Passing E.TGA conformance is not a substitute for the governed graph result: the graph still avoids hidden work and method order, hidden crossings, hidden scalarization, and unsupported path/slice currentness.

**Generative side.** E.TGA preserves open-ended action by keeping set-return, archive preservation, admissible loops, and budgeted refresh visible; these are not merely assurance checks, but the reason the graph can carry multiple future paths without collapsing them into one score or one pipeline.

**What goes wrong if missed.** A practitioner may treat a reference flow, a semio word such as `transition`, or a tool pipeline as a new graph kind or a second work and method order, then lose comparability, crossing evidence, and slice-local refresh boundaries.

**What this buys.** E.TGA lets the practitioner keep graph structure, publication pins, crossings, CV/GF separation, and refresh locality in one current architecture without turning every domain path into its own flow doctrine.

**Not this pattern when.** If the problem is only internal step constraint satisfaction, use `A.20`. If it is gate profile fit or gate decision aggregation, use `A.21`. If it is mechanism-governing-definition meaning, citeable-token denotation, suite membership, planned-baseline pins, or wiring semantics, use `E.20`. If the text asserts that work occurred or should occur, use the work and enactment loci; `E.18` can locate entry to `U.WorkEnactment` as a crossing, but it does not assert work occurrence. If the text only uses semio wording such as `transition` without a live transduction relation and governed graph, path, or crossing locus, do not mint a graph kind; keep the phrase in the semio pattern or source-local wording that carries it.

