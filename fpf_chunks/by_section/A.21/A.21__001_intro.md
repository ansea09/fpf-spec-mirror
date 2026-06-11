---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__001_intro.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:intro — Intro"
line_start: 28172
line_end: 28222
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.7"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "CV⇒GF"
  - "DecisionLog"
  - "EquivalenceWitness"
  - "GateChecks"
  - "GateDecision"
  - "GateFit"
  - "GateProfile"
  - "LaunchGate"
  - "OperationalGate"
  - "join-semilattice"
---

## A.21 — GateProfilization: `OperationalGate(profile)` (GateFit core)

**ID:** A.21
**Type:** Architectural pattern

**One-liner.** A single microkernel-style gate aggregates **GateChecks (CV + GF)** into an **order-independent** `GateDecision` via the `GateDecision` join-semilattice `abstain <= pass <= degrade <= block`, uses the **CV=>GF activation predicate** (and the LaunchGate pre-run barrier), applies profile-bound folds for `error|timeout|unknown`, and publishes replay-grade traces (MVPK + `DecisionLog` + `EquivalenceWitnessRef`).

**Use this when.** Use A.21 when the question under repair is whether a gate may publish a profile-bound `GateDecision` from declared GateChecks, folds, pins, and rationale.

**First useful move.** Name the `OperationalGate(profile)`, the active `GateProfile`, the effective `GateCheckRef` set, the aggregated CV status, and the `DecisionLogRef` that will carry the decision rationale.

**Smallest sufficient gate-publication guidance.** Use the lightest gate-publication guidance that preserves the next admissible reader move. Add crossing fields, launch fields, regulated fields, safety-critical fields, replay witnesses, `CrossingBundle`, `PQG`/`RSCR`, or MIP-run material only when the live gate-decision claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient next move.** If there is only a guard, dashboard cue, explanation, or readiness-looking label and no `A.21` gate-decision relation, no gate is opened here. Once a gate is live, the low-risk publication minimum is `GateId + GateProfile + GateCheckRef set + CV aggregate + GateDecision + DecisionLogRef`; crossing, launch, regulated, and safety-critical fields appear only when those claims are being made.

**Do not escalate when.** Do not turn cues, guards, narrative explanations, dashboard states, CV results, or readiness-looking labels into a `GateDecision`. Open A.21 only when a live gate-decision relation consumes check refs under an active `GateProfile`.

**Gate-looking display and conformance-label disposition.** A green tile, readiness badge, release screen, conformance label, `CV.Status`, safety-envelope note, or regulated-conformance phrase is not gate passage by resemblance. If the attempted use is gate passage, recover the active `OperationalGate(profile)`, `GateProfile`, effective `GateCheckRef` set, CV aggregate, `GateDecision`, `DecisionLogRef`, scope, and currentness/window. If those fields are not recoverable, keep the item as a display cue, source pointer, CV result, or evidence question and return to `A.10`, `A.20`, `B.3`, `E.19`, or the pattern governing the recovered claim that carries the claim being made. Safety envelope and assurance claims do not live in A.21 unless they are declared gate checks consumed under the active profile; their evidence and assurance support remain with `A.10` and `B.3`. Plain wording remains ordinary unless it changes admissible use, source relation, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

**Common wrong first reading.** A green tile, readiness display, or release screen means `GateDecision=pass` exists. First honest entry: A.21 is live only when an active `OperationalGate(profile)` consumes declared checks and publishes a `GateDecision` with `DecisionLogRef`; otherwise the item remains a cue or source question.

Repaired anti-case: a release screen says all checks are green but no active `OperationalGate(profile)`, effective `GateCheckRef` set, `GateDecision`, or `DecisionLogRef` is recoverable. The display remains a cue or evidence question; the attempted gate-passage use has no admissible current use until the A.21 gate-decision relation is recoverable.

**Same problem, different question under repair.** For a TGA-looking problem, use `E.18` for graph/flow/crossing, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is live.

**Semantic repair return.** When A.21 blocks a misleading word, face, alias, or source label, the repair must return to the enabled gate action: name the live gate-decision relation, active `GateProfile`, consumed `GateCheckRef` set, aggregate, `GateDecision`, and `DecisionLogRef` that remain admissible. Do not stop at a classification of vocabulary or publication faces.

**EntityOfConcern and relation separation.** Keep the graph object and path or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-governing definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence carrier, MIP manifest, or work witness does not carry another pattern's project-side value unless that governing pattern consumes it for that relation.

**Smallest affected locus.** Localize the change to the smallest live locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated EntityOfConcern when that locus is enough.

**Ordinary success.** For ordinary A.21 use, success is that the live gate-decision relation, active profile, check set, aggregated decision, and `DecisionLogRef` are placed without implying performed work or mechanism-definition truth. A full conformance review is needed only when crossing, launch, regulated, safety-critical, or replay claims consume expanded assurance or conformance material.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, TGA `Check` distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field liveness.** Always core for A.21 once a gate is live: `GateId`, `GateProfile`, effective `GateCheckRef` set, CV aggregate, `GateDecision`, and `DecisionLogRef`. Conditional-live: crossing pins, LaunchGate pre-run barrier fields, regulated or safety-critical evidence refs, equivalence witnesses, and replay/currentness fields; open them only when the corresponding crossing, launch, regulated, safety-critical, replay, or reuse claim is live.

**Retrieval trap guard.** When excerpted alone, A.21 DecisionLog fields must not be read as requiring a full regulated log for every cue, guard, or low-risk gate. The `DecisionLog` content follows the live `GateDecision`, active profile, and conditional field-liveness rules.

**Anti-Goodhart guard.** A complete gate record is not a substitute for the governed gate result: the gate must still publish the correct `GateDecision` under the active profile, and that decision does not prove performed work or mechanism-definition truth. `DecisionLog` completeness does not make an invalid check true; check truth remains with the governing patterns.

**Generative side.** A.21 preserves open-ended action by publishing explicit `GateDecision=pass`, `GateDecision=degrade`, `GateDecision=block`, or `GateDecision=abstain` decisions with rationale, so downstream work can continue, narrow, retry, or stop under declared conditions instead of being hidden behind an unreviewable cue.

**What goes wrong if missed.** A guard can be mistaken for a GateCheck, a human-readable explanation can be mistaken for the decision or decision record, and a dashboard-like pass/fail cue can be treated as gate passage without the `A.21` decision relation.

**What this buys.** A.21 gives the reader one place to separate profile fit, decision aggregation, rationale, optional explanation, and decision-record reuse while keeping gate logic out of CV and planning.

**Not this pattern when.** If the question is internal step constraint satisfaction, use `A.20`. If the question is graph crossing or valuation, use `E.18`. If the question is performed work or work planning, use the work/enactment or planning loci. If the text only contains a guard, cue, explanation, dashboard state, lexical pseudo-gate, or readiness-looking label without an `A.21` gate-decision relation, do not infer gate passage.

