---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "U.Flow.ConstraintValidity — Eulerian"
section_id: "A.20:0"
section_title: "Intention"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__002_intention.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.20 — U.Flow.ConstraintValidity — Eulerian"
  - "A.20:0 — Intention"
line_start: 27832
line_end: 27880
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransductionFlow"
  - "flow"
---

### A.20:0 - Intention

**One‑liner** Defines cross‑cutting **ConstraintValidity** rules for all `U.Flow` instances. `U.TransductionFlow` inherits these rules and may refine **CV class specializations** for transduction‑specific semantics (species‑binding only; genus rules remain unchanged). The CV core is **kind‑agnostic** and assumes an **open‑world** catalogue of node **species**; the enumeration of node **kinds** in E.TGA is a **minimal kind baseline**.
**Operational interpretation.** **Eulerian** stance: **flow = valuation** over `U.Transfer`; **CV is attached to transformations (steps)** and evaluated **before any GateFit**; edges carry **assurance‑only operations**; no token‑passing semantics are assumed.

**Use this when.** Use A.20 when the question under repair is whether one transformation step internally satisfies its declared constraints before any gate-profile fit is evaluated.

**First useful move.** Name the step, the CV class being checked, the `CV.Status`, and the witness or missing witness. Stop there unless a gate, comparator, bridge, freshness, or work-boundary question is actually being made.

**Smallest sufficient CV guidance.** Use the lightest CV guidance that preserves the next admissible reader move. Add publication lexemes, witnesses, `DecisionLog` detail, `CrossingBundle`, `PQG`/`RSCR`, or MIP-run material only when the live CV claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient next move.** For ordinary CV, `step + CV class + CV.Status + witness or refusal` is enough. Per-check publication lexemes are needed only when the CV result is carried into a publication face, gate relation, or assurance material.

**Do not escalate when.** Do not create `GateDecision`, `GateDecisionExplanation`, GateFit narrative, comparator law, bridge law, freshness claim, release-confidence claim, or work-boundary authority from `CV.Status`. Open those neighboring pattern relations only when their own claim being made is present.

**Conformance-marker overread note.** Use this note when a conformance label, `CV.Status=pass`, release-screen status, dashboard cue, or CV-looking publication is being read as gate passage, release confidence, safety acceptance, assurance, work occurrence, work authorization, or performed work. The first A.20 move is to return to the local step, CV class, `CV.Status`, witness or refusal, and window governed here; then state the unsupported attempted use and open the receiving relation only if its claim being made is present: `A.21` for gate decision, `B.3` for assurance, `A.10` for evidence/currentness, `A.15` for work, or the neighboring pattern governing that claim that carries the claim being made. Write `CV.Status=pass` when CV is meant; do not write plain `pass` near gate, release, safety, or work use. Plain wording remains ordinary unless it changes admissible use, source relation, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

**Common wrong first reading.** `CV.Status=pass` means release, safety acceptance, or gate passage. First honest entry: `CV.Status` is local step constraint validity with witness or refusal; release, safety, gate, assurance, or work use exits to the governing pattern only when that claim being made is present.

Repaired anti-case: a manufacturing conformance label near release may carry only the local CV or conformance relation it actually records. If release permission, safety acceptance, or work authorization is attempted, state that unsupported use and open the receiving relation rather than treating the label as release authority.

**Same problem, different question under repair.** For a TGA-looking problem, use `E.18` for graph/flow/crossing, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is live.

**Semantic repair return.** When A.20 blocks a misleading word, face, alias, or source label, the repair must return to the enabled CV action: name `CV.Status`, the applicable CV class, and the witness or refusal that remains admissible. Do not stop at a classification of vocabulary or publication faces.

**Locus and relation separation.** Keep the graph object and path or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-governing definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence carrier, MIP manifest, or work witness does not carry another pattern's project-side value unless that governing pattern consumes it for that relation.

**Smallest affected locus.** Localize the change to the smallest live locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated flow, path-slice, CV, gate, or mechanism-definition locus when the smaller locus is enough.

**Ordinary success.** For ordinary A.20 use, success is that the live CV class, `CV.Status`, and witness or refusal are placed for the step without implying gate passage, comparator admissibility, freshness, or launch readiness. A full conformance review is needed only when the downstream claim consumes expanded assurance or conformance material.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, TGA `Check` distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field liveness.** Always core for A.20: step, applicable CV class, `CV.Status`, and witness or refusal. Conditional-live: `GateCheckRef(aspect=ConstraintValidity)`, MVPK face pins, bridge/UTS refs, comparator/set-return refs, refresh refs, and SquareLaw or retargeting witnesses; open them only when the corresponding publication, gate, bridge, comparator, refresh, or `StructuralReinterpretation` claim is live.

**Retrieval trap guard.** When excerpted alone, A.20 must not be read as requiring every CV class or a Lipschitz certificate for every step. CV classes are applicability-triggered, and `CV.Status` does not create gate passage, launch readiness, comparator admissibility, or a reusable `GateDecision`.

**Anti-Goodhart guard.** CV completeness is not a substitute for the governed step result: the step must still satisfy the applicable internal constraint, and CV conformance does not create gate fit, freshness, comparator admissibility, or launch readiness.

**Generative side.** A.20 preserves open-ended action by letting internally valid steps, set publications, and archives remain usable without premature gate, ranking, or launch claims; CV supplies a local admissibility relation for future moves, not only an assurance stop.

**What goes wrong if missed.** Readers may treat internal constraint satisfaction as gate passage, launch readiness, freshness, comparator admissibility, or decision reuse. That collapses CV into GateFit and hides the `A.21` gate decision relation.

**What this buys.** A.20 lets a reader keep mechanism constraint status local to the step and move to `A.21` only when gate fit or gate decision aggregation is really the question under repair.

**Not this pattern when.** If the question is profile fit, gate decision, gate-decision reuse, gate explanation, or pass/fail gate publication, use `A.21`. If the question is graph crossing or flow valuation, use `E.18`. If the question is comparator admissibility, set-return, archive, or refresh policy, use the current neighboring loci named in Relations.

