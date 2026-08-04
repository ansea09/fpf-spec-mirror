---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:2"
section_title: "Thin First Use and Output Kind"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__003_thin-first-use-and-output-kind.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:2 — Thin First Use and Output Kind"
line_start: 51829
line_end: 51992
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
---

### C.22.2:2 - Thin First Use and Output Kind

#### C.22.2:2.1 - Thin First-Use Form

The first substantive use is the Thin form. It is a practitioner-facing prompt for the smallest reviewable card, not a demand to complete a schema.

A `ProblemCard` is complete for its current use when it states:

1. what signal or cue made the practitioner stop;
2. the one exact joint `EntityOfConcern`, effective `U.ReferenceScheme`, and `U.ClaimScope` for the claims being carried;
3. which claim family is current: actual-PFR assertion, anticipated-condition claim, method-availability or solvability claim, or another directly governed problem-side claim;
4. why this is not merely a wish, ticket, slogan, label, or preselected Work request;
5. what would count as improvement or as an acceptance probe; and
6. one honest next use.

The next use may be `P2W-ready`, characterize, compare, search, refresh, retire, archive, `abstainOrNoChange`, or apply the direct pattern governing the named claim, relation, or boundary. If an improvement check or acceptance probe is absent, the card may preserve the signal and choose one of the other uses but cannot claim `P2W-ready`.

`C.22.2 - ProblemCard` is the pattern heading. A `ProblemCard` instance is the C.2.1 episteme described above. `ProblemCardRef` is only a reference value designating one such episteme; it is not another durable kind. Plain-register glosses and local labels do not replace the Tech name.

Local labels include `problem-formulation follow-up reason`, `validation boundary`, `risk condition`, `solvability band`, `P2W-ready`, `reviewable`, `stale`, `refreshed`, `retired`, `archived`, `abstainOrNoChange`, and `firstPrinciplesCue`. They describe claim content or a local disposition; they create no FPF kind, state-machine kind, gate result, relation occurrence, or mathematical-lens object.

Use `E.10.MOVE` only when move-like wording no longer denotes one of these local dispositions and instead hides a pattern-use recommendation, Work-entry readiness, performed Work, gate, transformation, source relation, architecture move, call-planning move, or another directly governed value.


Reference labels ending in `Ref` are reference roles, not kind names. This includes `ProblemCardRef`, `sourceSetRef`, `rivalProblemFormulationRef`, and `representationOrWordingUseRelationRef`.

Semantic locality comes from the exact EntityOfConcern, effective ReferenceScheme, ClaimScope, declared assumptions or window, and receiving use carried by the relevant claims. A broad domain, organization, practice, or location label is only recognition material until those exact values are recoverable. None becomes a container participant or establishes global Problem identity.

Plain gloss for `P2W-ready`: *problem-side input ready*. It means ready as input to downstream P2W or selector reasoning, not ready for Work execution, gate passage, method selection, evidence reliance, or autonomy.

When a downstream reader asks whether intended Work can enter a work boundary, the card may supply problem-side cues, acceptance probes, constraints, and freshness conditions, but A.15.5 governs the readiness relation. C.22.2 decides no full-kit preparation, commitment, launch gate, or performed Work.

#### C.22.2:2.2 - Required Solution Use

The Solution turns observed signal material into one C.2.1 episteme and one governed next use, not a completed form.

1. Capture the symptom, anomaly, risk, stakeholder cue, drift, hypothesis, or other observed signal before naming an actual Problem.
2. Recover the one joint EntityOfConcern, effective ReferenceScheme, ClaimScope, and claim family. If the claims concern unrelated entities, split the ClaimGraph and card.
3. Separate the signal detector, actual-PFR assertion if independently grounded, anticipated-condition claim, improvement check, candidate acceptance criterion, method-availability claim, monitored risk signal, and proxy-distortion risk. These are not one card status or one PFR participant set.
4. Pay only for current complexity. Add conditional content only when it changes the current next use; otherwise stop at the lighter card or name the direct pattern for the claim now current.
5. If the formulation changes EntityOfConcern, effective scheme, ClaimScope, diagram, functional description, or transformation-flow interpretation, name the representation-transition, retargeting, Bridge, structural-reinterpretation, or wording-use relation before inheriting an earlier card disposition.
6. Close by the honest next use. A filled card without a truthful next use is not a successful result.

**Cheap stop.** The smallest card that gives a truthful next use is sufficient. A conforming use does not require heavier fields merely because the full inventory exists.

**First practitioner use.** State the signal, joint EntityOfConcern, scheme, scope, claim family, not-wish reason, improvement check or acceptance probe, and honest next use. Open the relation-boundary aid only when another claim or relation changes that move.

#### C.22.2:2.3 - Relation Boundary Aid

Use this aid only after the Thin `ProblemCard` is legible: signal, joint EntityOfConcern, effective ReferenceScheme, ClaimScope, not-wish reason, improvement check or acceptance probe, and honest next use. It is not a second writing order and not a catalogue of other patterns. It answers one question:

> Which claim being made, relation, or boundary changes the problem-card use, and which FPF pattern governs that claim, relation, or boundary?

If the claim, relation, or boundary does not change the current problem-card use, leave it out of the card. If it does change the move, keep only the local cue or reference that makes the card reviewable, then apply the governing pattern for that claim, relation, or boundary.

| Current claim, relation, or boundary that changes the card use | Local `ProblemCard` content | Governing pattern |
|---|---|---|
| Characterization, measurement, indicator, Q-bundle, comparison, acceptance, or parity | Characterization cue, acceptance probe, candidate criterion, comparator cue or window cue, and the current reason the relation changes the problem formulation. | `C.16`, `A.19`, `C.25`, `G.0`, `G.4`, or `G.9` according to the relation named by value. |
| Archive, pool, front, shortlist, selected set, retained candidate, or set-return source | `sourceSetRef`, source-set kind, selection or retention criterion, budget or window when current, and non-scalar next use. | `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, `A.6.P:7a`, or `C.16.Q` according to the relation named by value. |
| Method family, work planning, work-entry readiness, performed work, result record, evidence, provenance, assurance, gate, or autonomy | Problem-side cue, source reference when it changes formulation, and stop condition before that outside use. | `G.5`, `A.15`, `A.15.5`, `A.10`, `G.6`, `B.3`, `A.21`, or `E.16` according to the claim named by value. |
| Temporal, causal-use, representation-transition, retargeting, bridge, structural-reinterpretation, or wording-use relation | Relation reference plus the inheritance boundary: what can be reused from the old card and what relation is reopened. | `C.27`, `C.28`, `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, `E.18`, or `E.10` according to the relation named by value. |
| First-principles or mathematical structure cue | Candidate structure, preserved and lost structure when current, practical payoff for problem formulation, problem-formulation follow-up reason, and stop condition. | `C.29` for mathematical-lens use; `A.6.0` for a `FormalSubstrate` `U.Signature` declaration when that signature declaration is current. |
| Agentic safe probe or world-affecting next action | Probe need, risk condition, bounded next action, and the safety named by value, autonomy, gate, work, evidence, or assurance claim kind that blocks local action. | `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` according to the relation named by value. |

Over-capture symptom: the practitioner spends the pattern use classifying FPF patterns while the signal, joint EntityOfConcern, effective ReferenceScheme, ClaimScope, improvement check, acceptance probe, and next use remain unstable.

Repair: return to the Thin problem-side action. State the signal, joint EntityOfConcern, effective ReferenceScheme, ClaimScope, why this is not merely a wish, ticket, slogan, or preselected work request, the improvement check or acceptance probe, and the honest next use. Reopen this aid only for the claim, relation, or boundary that changes that move.

#### C.22.2:2.4 - Use Boundaries and Record Budgets

Use `C.22.2` when a signal is not yet a problem-side record and downstream task typing, P2W, method-family selection, work planning, evidence use, gate passage, autonomy control, or selected-set use depends on such a record. A known method does not close this pattern when the problem signal, scope, acceptance probe, or EntityOfConcern remains unstable.

Use another pattern directly when the question under repair is already that pattern's `EntityOfConcern` or governed relation: `A.15` for work planning or performed work; `A.10`, `G.6`, or `B.3` for evidence, provenance, or assurance; `A.21` for gate decision; `E.16` for autonomy; `C.11` for a local choice among explicit options; and `C.18`, `C.19`, or `G.5` for archive, pool, front, or selected-set governance. `C.22.2` may still preserve the problem-side cue or reference that explains why that pattern is now current.

Use record budgets:

- Thin record budget: signal, joint EntityOfConcern, effective ReferenceScheme, ClaimScope, not-wish, not-slogan, not-ticket, or not-preselected-work reason, provisional improvement check or acceptance probe, and one honest next use.
- Standard record budget: Thin fields plus the current comparison, acceptance, risk, validation, freshness, unknown-handling, or P2W-readiness fields needed for downstream use.
- High-relation record budget: Standard fields plus only the relation references needed when public, disputed, high-risk, set-derived, cross-scheme, cross-use-boundary, evidence-adjacent, autonomy-adjacent, gate-adjacent, agentic, temporal, causal, representation, or Part-G relations are current.

Stop at Thin when it gives a truthful next use. Stop at Standard when it is enough to emit or bind a minimal `TaskSignature`, `TaskKind`, or `ProblemProfile`. Apply the governing FPF pattern for the claim being made, relation, or boundary instead of enlarging the card when the issue under repair is no longer the problem-side record itself.

#### C.22.2:2.5 - Field Labels and Current-Use Conditions

Use these readable labels only when current for the case:

- problem signal and exact signal reference;
- one exact ClaimGraph, joint EntityOfConcern, effective ReferenceScheme, and ClaimScope;
- actual-PFR assertion with exact polarity and PFR reference only when C.22.PFR independently establishes the occurrence;
- anticipated-condition, forecast, scenario, or counterfactual claim with assumptions and horizon;
- method-availability or solvability claim with admitted method set, evidence qualification, constraints, and intended use;
- primary viewpoint or role concern as claim qualification, never as card or PFR identity;
- symptom detector, problem hypothesis or cause-theory cue, and rival formulation when current;
- improvement check, acceptance probe, characterization relation, characteristic or Q-bundle relation, indicator selection, and parity or comparison relation when current;
- mandatory constraints, risk condition, validation boundary, freshness or expiry condition, and unknown handling;
- problem-formulation follow-up reason when it changes review, discrimination, or receiving use;
- representation-transition, retargeting, Bridge, structural-reinterpretation, or wording-use reference when an earlier disposition may no longer transfer;

- `sourceSetRef`, source-set kind, selection or retention criterion, budget or window, and non-scalar next use when the signal comes from a set, pool, front, archive, shortlist, or selected set;
- `firstPrinciplesCue` when a mathematical structure changes the formulation; and
- governing-pattern cue naming the direct pattern, claim kind, exact receiving-use reference, and stop condition when an outside claim changes the card use.

| Field current-use class | Required treatment |
|---|---|
| C.2.1 constitution | State the exact ClaimGraph, one joint EntityOfConcern, and effective ReferenceScheme. These constitute the card episteme; ClaimScope, viewpoint, assumptions, windows, and receiving use qualify the relevant claims and relations, while id, carrier, and publication remain outside constitution. |
| Core problem-side claims | State the signal, ClaimScope, claim family, not-wish reason, improvement check or acceptance probe, and honest next use. |
| Conditional claims and references | Add only the exact characterization, comparison, risk, validation, freshness, set-source, representation, forecast, solvability, PFR, or other direct relation content that changes the move. |
| Governing-pattern cue | Keep only the local cue or reference needed by the card, then name the direct pattern and claim kind that govern the outside use. |

If a conditional value is not current, omit it rather than writing `unknown`. Use `unknown` only where a current direct pattern admits that result or value. If a required current value is unavailable, state whether the next use is blocked, degraded, sandboxed, or must return to its governor. A stale value receives the G.11/currentness disposition; an intentionally omitted value states the record-budget reason without implying it was checked.

When the card compares options, retained candidates, or rival formulations, it states the exact comparison or parity relation or why comparison is not current. Absence is a disposition, not an automatic defect; any positive parity or selected-set result remains outside C.22.2.

`problemCardWitnessRefs` may be used as a local recoverability group, not as a new kind or evidence graph:

```text
problemCardWitnessRefs:
  problemSignalRef?
  sourceSetRef?
  selectionOrRetentionCriterion?
  characterizationRelationRef?
  parityRelationRef?
  freshnessRef?
  representationOrWordingUseRelationRef?
```

Generated variants, evaluator feedback, and open-ended mutation remain signal or source-set cues. They do not constitute the card, supply evidence sufficiency, make PFR obtain, or authorize action.

#### C.22.2:2.6 - Anti-Pattern Checks and Worked Slices

Anti-pattern checks start from the local card use:

- card-as-executable-work request: the card is treated as executable work while method, plan, and work occurrence remain undecided;
- form-completion: every field is filled because the template exists, even though the Thin next use would be truthful;
- readiness shortcut: `P2W-ready` is declared from signal and scope alone, without improvement check or acceptance probe;
- source-claim shortcut: a preselected solution, work request, proof-looking reference, gate-looking cue, or authority-looking cue replaces the problem-side signal, joint EntityOfConcern, effective ReferenceScheme, ClaimScope, acceptance probe, and next use;
- scalar shortcut: archive, set-return, Goldilocks, NQD, OEE, partial-order, stepping-stone, or indicator material collapses into one readiness score;
- prestige shortcut: first-principles or mathematical wording is kept without practical payoff, preserved and lost structure when current, problem-formulation follow-up reason, and stop condition.

Local stop rule: if the encountered material tries to carry a claim outside `C.22.2`, the card keeps only the cue or reference that changes problem formulation or the next use, then names the governing FPF pattern and claim kind named by value to use before that claim is relied on.

A conforming `C.22.2` use is testable against at least one Thin worked slice, such as repeated task rework or another compact problem signal, showing signal, EntityOfConcern, ReferenceScheme, ClaimScope, not-preselected-work reason, improvement check, and next use. It is also testable against at least one High-relation worked slice from a set, archive, pool, front, shortlist, selected set, or portfolio source, showing `sourceSetRef`, candidate acceptance criterion, risk condition, and the claim, relation, or boundary without creating a local portfolio or archive kind.

#### C.22.2:2.7 - Conformance Checklist Requirements

The checklist protects a completed or reviewed card from overread; the writing order remains the Thin form and honest next use.

| Check | Required test |
|---|---|
| C.2.1 identity | The card has one exact ClaimGraph, one independently identified joint EntityOfConcern, and one effective ReferenceScheme. Unrelated PFRs or other concerns force ClaimGraph/card split. |
| Claim-family separation | Actual-PFR assertion polarity, reliance result, anticipated-condition claim, and method-availability or solvability claim remain distinct. |
| PFR boundary | Any affirmative actual-PFR assertion names an occurrence independently established by C.22.PFR. A card, signal, label, viewpoint, evidence item, method, or negative assertion creates or ends none. |
| Core usability | The card states signal, ClaimScope, claim family, not-wish reason, improvement check or acceptance probe, and honest next use. |
| `P2W-ready` reason | `P2W-ready` appears only with an improvement check or acceptance probe and one named downstream use; it is problem-side readiness only. |
| Field budget | Conditional content appears only when current; absence and admitted `unknown` remain distinct. |
| Exact source and set | A set-derived card preserves exact `sourceSetRef`, set kind, retention or selection criterion, and non-scalar next use without becoming an archive or portfolio object. |
| Direct-governor cue | Claims outside C.22.2 remain local cues or references and name the exact pattern and claim kind used next. |
| Constitution stays exact | Only ClaimGraph, one joint EntityOfConcern, and effective ReferenceScheme constitute the card. Scheme, ClaimScope, assumptions, windows, viewpoint, receiving use, and any exact A.15.6 Work reference stay in their claims and direct relations; no setting, carrier, or organization is added as a participant. |
| Currentness and change | Freshness, changed representation, retargeting, or unknown-blocked use states refresh, retirement, bounded use, `abstainOrNoChange`, or the exact relation reopened. |
| Scalar and proxy guard | Goldilocks, NQD, OEE, set-return, priority, indicator, or stepping-stone wording does not become one readiness score or substitute for value. |
| First-principles payoff | A mathematical cue states practical payoff, preserved and lost structure when current, follow-up reason, and stop; C.29 governs the lens use. |
| External wording recovery | Passport, rule-of-choice card, evidence pack, autonomy budget, logs, gates, portfolio, factory, and similar source terms enter only as exact signal, set, characterization, comparison, or follow-up material under their direct governors. |
| Record-budget invariant | The card is as small as the current next use permits; a template, relation aid, or worked example is not another FPF kind. |

