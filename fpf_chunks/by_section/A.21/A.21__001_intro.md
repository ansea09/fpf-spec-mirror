---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__001_intro.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:intro — Intro"
line_start: 34118
line_end: 34172
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.7"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
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

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative for gate-decision publication by `OperationalGate(profile)` under `E.18` `TransformationFlowStructure`, A.20 constraint-validity input, and the A.21 CV=>GF activation boundary.

**One-liner.** A single microkernel-style gate aggregates **GateChecks (CV + GF)** into an **order-independent** `GateDecision` via the `GateDecision` join-semilattice `abstain <= pass <= degrade <= block`, uses the **CV=>GF activation predicate** and the LaunchGate pre-run barrier, applies `GateProfile`-bound folds for `error|timeout|unknown`, and publishes replay-grade traces through MVPK faces, `DecisionLog`, and `EquivalenceWitnessRef`.

**Use this when.** Use A.21 when the current question is whether a gate-decision relation publishes a `GateProfile`-bound `GateDecision` from declared GateChecks, folds, pins, and rationale.

**First useful gate use.** Name the `OperationalGate(profile)`, the current declared `GateProfile`, the effective `GateCheckRef` set, the aggregated CV status, and the `DecisionLogRef` that carries the decision rationale.

**Smallest sufficient gate-publication guidance.** Use the lightest gate-publication guidance that preserves the current bounded gate use. Add crossing fields, launch fields, regulated fields, safety-critical fields, replay witnesses, `CrossingBundle`, `PQG` or `RSCR`, or MIP-run material only when the present gate-decision claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient gate use.** If there is only a guard, dashboard cue, explanation, full-kit-looking label, or readiness-looking label and no `A.21` gate-decision relation, A.21 has no gate-decision relation to publish. Once the gate-decision relation is present, the low-risk publication minimum is `GateId + GateProfile + GateCheckRef set + CV aggregate + GateDecision + DecisionLogRef`; crossing, launch, regulated, and safety-critical fields appear only when those claims are being made. If the current question is whether intended work has full-kit or work-entry readiness without a gate-decision relation, use `A.15.5`.

**Do not escalate when.** Do not turn cues, guards, narrative explanations, dashboard states, CV results, or readiness-looking labels into a `GateDecision`. Use A.21 only when a present gate-decision relation consumes check refs under a current declared `GateProfile`.

**Gate-looking display and conformance-label disposition.** A green tile, readiness badge, release screen, full-kit label, conformance label, `CV.Status`, safety-envelope note, or regulated-conformance phrase is not gate passage by resemblance. If the attempted use is gate passage, recover the current `OperationalGate(profile)`, `GateProfile`, effective `GateCheckRef` set, CV aggregate, `GateDecision`, `DecisionLogRef`, scope, currentness, and effective window. If those fields are not recoverable, keep the display as a cue, source pointer, CV result, evidence question, or work-entry-readiness question; the evidence claim is governed by `A.10`, the CV result by `A.20`, the work-entry-readiness relation by `A.15.5`, the assurance claim by `B.3`, the language-quality question by `E.19`, or the recovered neighboring claim by its own governing pattern. Safety-envelope, work-entry-readiness, and assurance claims do not belong to A.21 unless they are declared gate checks consumed under the current `GateProfile`; their evidence, readiness, and assurance relations remain with `A.10`, `A.15.5`, and `B.3`. Plain wording remains ordinary unless it changes bounded use, source relation, evidence, gate, readiness, assurance, work, decision, or neighboring-pattern relation.

**Common wrong interpretation.** A green tile, readiness display, or release screen means `GateDecision=pass` exists. First honest entry: A.21 applies only when a current `OperationalGate(profile)` consumes declared checks and publishes a `GateDecision` with `DecisionLogRef`; otherwise the display remains a cue or source question.

Repaired anti-case: a release screen says all checks are green but no current `OperationalGate(profile)`, effective `GateCheckRef` set, `GateDecision`, or `DecisionLogRef` is recoverable. The display remains a cue or evidence question; the attempted gate-passage use has no bounded current gate use until the A.21 gate-decision relation is recoverable.

Agent-loop anti-case: a monitor retries twice, escalates to a supervisor, and the harness dashboard turns green. That sequence may be performed work, telemetry, a transformation-flow path, or evidence for a later check, but it is not `GateDecision=pass` unless a current `OperationalGate(profile)` consumes declared `GateCheckRef`s and publishes `GateDecision` plus `DecisionLogRef`. If the gate-decision relation is intended but missing, repair it by recovering the A.21 gate-decision relation; otherwise the result remains a cue for A.15, E.18, G.9, or evidence work, not an A.21 gate passage.

**Same problem, different current question.** For a gate-bearing transformation-flow problem, use `E.18` for transformation-flow structure, graph value, path relation, valuation, or crossing claims, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not use the other three until their own claim is present.

**Semantic repair target.** When A.21 blocks a misleading word, face, alias, or source label, the repair must restore the gate-decision claim: name the current gate-decision relation, current `GateProfile`, consumed `GateCheckRef` set, aggregate, `GateDecision`, and `DecisionLogRef` that remain available under A.21. Do not stop at a classification of vocabulary or publication faces.

**EntityOfConcern and relation separation.** Keep the graph value, path relation or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10` and `G.6`), work plan or work occurrence (`A.15`), and mechanism-governing definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence value, MIP manifest, or work witness does not stand in for another pattern's project-side value unless that governing pattern consumes it for that relation.

**Smallest affected locus.** Localize the change to the smallest affected locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated EntityOfConcern when that locus is enough.


**Ordinary success.** For ordinary A.21 use, success is that the current gate-decision relation, current `GateProfile`, check set, aggregated decision, and `DecisionLogRef` are placed without implying performed work or mechanism-definition truth. A full conformance review is needed only when crossing, launch, regulated, safety-critical, or replay claims consume expanded assurance or conformance material.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, `E.18` `Check` locus distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a performed work occurrence, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field applicability.** Always core for A.21 once the gate-decision relation is present: `GateId`, `GateProfile`, effective `GateCheckRef` set, CV aggregate, `GateDecision`, and `DecisionLogRef`. Conditional fields are crossing pins, LaunchGate pre-run barrier fields, regulated or safety-critical evidence refs, equivalence witnesses, and replay or currentness fields; include a conditional field only when the corresponding crossing, launch, regulated, safety-critical, replay, or reuse claim is present.

**Retrieval trap guard.** When excerpted alone, A.21 DecisionLog fields must not be interpreted as requiring a full regulated log for every cue, guard, or low-risk gate. The `DecisionLog` content follows the current `GateDecision`, current `GateProfile`, and field-applicability rules.

**Anti-Goodhart guard.** A complete gate record is not a substitute for the governed gate result: the gate must still publish the correct `GateDecision` under the current `GateProfile`, and that decision does not prove performed work or mechanism-definition truth. `DecisionLog` completeness does not make an invalid check true; check truth remains with the governing patterns.

**Generative side.** A.21 preserves open-ended action by publishing explicit `GateDecision=pass`, `GateDecision=degrade`, `GateDecision=block`, or `GateDecision=abstain` decisions with rationale, so downstream work can continue, narrow, retry, or stop under declared conditions instead of being hidden behind an unreviewable cue.

**What goes wrong if missed.** A guard can be mistaken for a GateCheck, a human-readable explanation can be mistaken for the decision or decision record, and a dashboard-like pass-or-fail cue can be treated as gate passage without the `A.21` decision relation.

**What this buys.** A.21 gives the practitioner one place to separate `GateProfile` fit, decision aggregation, rationale, optional explanation, and decision-record reuse while keeping gate logic out of CV and planning.

**Not this pattern when.** If the question is internal step constraint satisfaction, use `A.20`. If the question is graph crossing or valuation, use `E.18`. If the question is performed work or work planning, use the work occurrence or work-planning loci. If the question is full-kit condition or work-entry readiness before work entry, use `A.15.5` unless an actual gate-decision relation is current. If the text only contains a guard, cue, explanation, dashboard state, lexical pseudo-gate, or readiness-looking label without an `A.21` gate-decision relation, do not infer gate passage.

