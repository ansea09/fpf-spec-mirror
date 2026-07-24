---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:2"
section_title: "Thin First Use and Output Kind"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__003_thin-first-use-and-output-kind.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:2 — Thin First Use and Output Kind"
line_start: 51107
line_end: 51295
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
  - "P2W-ready"
  - "Thin problem card"
  - "actual PFR versus non-actual or solvability claim"
  - "assertion polarity"
  - "current reliance"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card episteme"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "validation boundary"
---

### C.22.2:2 - Thin First Use and Output Kind

#### C.22.2:2.1 - Thin First-Use Form

The first substantive use of this pattern is the Thin form. It is a practitioner-facing prompt for writing the smallest reviewable problem card, not a demand to complete a field list.

A `ProblemCard@Context` is complete for its current use when it states:

1. why this signal matters now;
2. what problem representation is being carried under which context and scope;
3. why this is not merely a wish, ticket, slogan, or preselected work request;
4. what would count as improvement or an acceptance probe;
5. what the honest next use is.

The Thin form asks for:

- the problem signal or selected-problem cue: what made the practitioner stop before downstream task typing or work selection;
- context grounding and scope cut, including what is outside the current problem;
- the reason this is not merely a wish, slogan, ticket, or preselected work request;
- a provisional improvement check or acceptance probe;
- one honest next use: `P2W-ready`, characterize, compare, search, refresh, retire, archive, `abstainOrNoChange`, or apply the FPF pattern governing the named claim kind, relation kind, or boundary that changes the problem-card use.

If the Thin form lacks an improvement check or acceptance probe, it may preserve the signal and choose characterization, comparison, search, refresh, retirement, archive, `abstainOrNoChange`, or governing-pattern application for the claim being made; the Thin form does not declare `P2W-ready`.

Only after the Thin form is legible, recover the output-kind boundary:

`C.22.2 - ProblemCard@Context` is the compact problem-side output under current `C.22`.

`C.22.2 - ProblemCard@Context` is the pattern heading. `ProblemCard@Context` is the `C.22.2` problem-side record shape; an instance is a reviewable problem-side record before P2W. `ProblemCard@ContextRef` may be used as a reference form when downstream text cites such an instance, but it is not a separate durable kind unless a separate naming or kind decision approves one under `F.18` and `A.6.P`. The Tech heading remains `C.22.2 - ProblemCard@Context`. Plain-register glosses or section-local practitioner labels may appear in this pattern, but those labels do not replace the Tech heading.

Local labels in this pattern are local to the `C.22.2` record shape unless a separate accepted FPF naming or kind decision assigns them a broader FPF kind. This includes `problem-formulation follow-up reason`, `validation boundary`, `risk condition`, `solvability band`, `P2W-ready`, `reviewable`, `stale`, `refreshed`, `retired`, `archived`, `abstainOrNoChange`, and `firstPrinciplesCue`; they do not create FPF kinds, gate statuses, state-machine kinds, or local mathematical-lens kinds or relations. When a claim outside `C.22.2` is current, do not mint a local reference field for it; name the governing FPF pattern, claim kind named by value, project-side reference when known, and stop condition in the next use or local cue. When a mathematical or first-principles cue is current, cite `C.29`; local `problem-formulation follow-up reason` names only why the problem formulation or structure cue is worth reviewing or moving onward from `C.22.2`; `C.29` carries mathematical-lens use and the problem-formulation follow-up reason for that lens.

Use `E.10.MOVE` only when move-like wording is no longer recoverable as this local problem-card disposition and begins to hide pattern-use recommendation, work-entry readiness, performed work, gate, transformation, source relation, architecture, call-planning, or another directly governed value.

Reference labels ending in `Ref` are reference roles, not kind names. This includes `ProblemCard@ContextRef`, `setContextRef`, `rivalProblemFormulationRef`, and `representationOrWordingUseRelationRef`; do not shorten or promote them into local kind names such as `ProblemCardRef`, `SetContext`, `RivalFrame`, or `RepresentationRelation`.

`@Context` means that the card is bound to declared context grounding: a named `U.BoundedContext`, a project-side context reference, or an explicitly bounded practice situation with recoverable local meaning. Domain or practice wording may identify the informative locus of the problem, but it does not replace context grounding. A broad label such as healthcare, education, engineering, research, or operations is not context grounding by itself. When domain or practice wording is used for context grounding, recover the named bounded context, project-side context reference, or explicit bounded practice situation and state what local meaning or rule is being used. The card does not assert global problem identity outside that declared context grounding.

Plain gloss for `P2W-ready`: problem-side input ready. It means ready as input to downstream P2W or selector reasoning, not ready for work execution, gate passage, or method selection.

When a downstream reader asks whether intended work can enter a work boundary, the problem card may supply problem-side cues, acceptance probes, constraints, and freshness conditions, but the readiness relation itself is `WorkEntryReadiness@Context` under `A.15.5`. `C.22.2` does not decide full-kit preparation, commitment disposition, launch gate, or performed work.

#### C.22.2:2.2 - Required Solution Use

The `C.22.2` Solution is organized around turning observed problem-side signal material into a reviewable problem-side record and one governed next use, not around schema completion.

1. Capture the symptom, anomaly, risk, stakeholder cue, drift, hypothesis, or other observed signal before naming the problem.
2. Stabilize the cheap problem-side record: context grounding, scope cut, EntityOfConcern when it changes the problem-side use, primary viewpoint or role concern, and provisional problem framing.
3. Make action possible by separating the symptom detector, improvement check, candidate acceptance criterion, optimization objective when current, monitored risk signal when current, and proxy-distortion risk when an indicator can be gamed or substitute for value; then state mandatory constraints, risk condition when current, and intended downstream use before downstream selection.
4. Pay only for current complexity: add conditional fields only when their kind is current for the problem-card use; otherwise stop at the lighter card or name the governing FPF pattern to use next and the claim kind named by value.
5. Run the representation-continuity check: if the problem formulation changes the EntityOfConcern, representation scheme, diagram, functional description, or transformation-flow path interpretation, name the representation-transition, retargeting, bridge, structural-reinterpretation, or wording-use relation before reusing an inherited local cue or readiness disposition.
6. Close by the honest next use rather than by a completed form. A filled card without a truthful next use is not a successful `C.22.2` result.

Cheap-stop rule: the smallest card that gives a truthful next use is sufficient. A conforming `C.22.2` use does not require heavier fields merely because the full field list exists.

First practitioner use before governing-pattern cues:

1. Capture the problem signal or selected-problem cue, context grounding, and scope cut.
2. State why it is not merely a wish, slogan, ticket, or preselected work request.
3. State the provisional improvement check or acceptance probe.
4. Choose the honest next use.
Use the relation boundary aid only when a conditional relation is current.

This is the Thin-form writing order, not a completion sequence for the whole pattern. It adds no fields; it keeps the practitioner on the smallest truthful card before Standard or High-relation material is paid for.

#### C.22.2:2.3 - Relation Boundary Aid

Use this aid only after the Thin `ProblemCard@Context` is legible: signal, context grounding, scope cut, not-wish reason, improvement check or acceptance probe, and honest next use. It is not a second writing order and not a catalogue of other patterns. It answers one question:

> Which claim being made, relation, or boundary changes the problem-card use, and which FPF pattern governs that claim, relation, or boundary?

If the claim, relation, or boundary does not change the current problem-card use, leave it out of the card. If it does change the move, keep only the local cue or reference that makes the card reviewable, then apply the governing pattern for that claim, relation, or boundary.

| Current claim, relation, or boundary that changes the card use | Local `ProblemCard@Context` content | Governing pattern |
|---|---|---|
| Characterization, measurement, indicator, Q-bundle, comparison, acceptance, or parity | Characterization cue, acceptance probe, candidate criterion, comparator cue or window cue, and the current reason the relation changes the problem formulation. | `C.16`, `A.19`, `C.25`, `G.0`, `G.4`, or `G.9` according to the relation named by value. |
| Archive, pool, front, shortlist, selected set, retained candidate, or set-return source | `setContextRef`, source-set kind, selection or retention criterion, budget or window when current, and non-scalar next use. | `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, `A.6.P:7a`, or `C.16.Q` according to the relation named by value. |
| Method family, work planning, work-entry readiness, performed work, result record, evidence, provenance, assurance, gate, or autonomy | Problem-side cue, source reference when it changes formulation, and stop condition before that outside use. | `G.5`, `A.15`, `A.15.5`, `A.10`, `G.6`, `B.3`, `A.21`, or `E.16` according to the claim named by value. |
| Temporal, causal-use, representation-transition, retargeting, bridge, structural-reinterpretation, or wording-use relation | Relation reference plus the inheritance boundary: what can be reused from the old card and what relation is reopened. | `C.27`, `C.28`, `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, `E.18`, or `E.10` according to the relation named by value. |
| First-principles or mathematical structure cue | Candidate structure, preserved and lost structure when current, practical payoff for problem formulation, problem-formulation follow-up reason, and stop condition. | `C.29` for mathematical-lens use; `A.6.0` for a `FormalSubstrate` `U.Signature` declaration when that signature declaration is current. |
| Agentic safe probe or world-affecting next action | Probe need, risk condition, bounded next action, and the safety named by value, autonomy, gate, work, evidence, or assurance claim kind that blocks local action. | `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` according to the relation named by value. |

Over-capture symptom: the practitioner spends the pattern use classifying FPF patterns while the problem signal, context, scope, improvement check, acceptance probe, and next use remain unstable.

Repair: return to the Thin problem-side action. State the signal, context, scope, why this is not merely a wish, ticket, slogan, or preselected work request, the improvement check or acceptance probe, and the honest next use. Reopen this aid only for the claim, relation, or boundary that changes that move.

#### C.22.2:2.4 - Use Boundaries and Record Budgets

Use `C.22.2` when a signal is not yet a problem-side record and downstream task typing, P2W, method-family selection, work planning, evidence use, gate passage, autonomy control, or selected-set use depends on such a record. A known method does not close this pattern when the problem signal, scope, acceptance probe, or EntityOfConcern remains unstable.

Use another pattern directly when the question under repair is already that pattern's `EntityOfConcern` or governed relation: `A.15` for work planning or performed work; `A.10`, `G.6`, or `B.3` for evidence, provenance, or assurance; `A.21` for gate decision; `E.16` for autonomy; `C.11` for a local choice among explicit options; and `C.18`, `C.19`, or `G.5` for archive, pool, front, or selected-set governance. `C.22.2` may still preserve the problem-side cue or reference that explains why that pattern is now current.

Use record budgets:

- Thin record budget: signal, context grounding, scope cut, not-wish, not-slogan, not-ticket, or not-preselected-work reason, provisional improvement check or acceptance probe, and one honest next use.
- Standard record budget: Thin fields plus the current comparison, acceptance, risk, validation, freshness, unknown-handling, or P2W-readiness fields needed for downstream use.
- High-relation record budget: Standard fields plus only the relation references needed when public, disputed, high-risk, set-derived, cross-context, evidence-adjacent, autonomy-adjacent, gate-adjacent, agentic, temporal, causal, representation, or Part-G relations are current.

Stop at Thin when it gives a truthful next use. Stop at Standard when it is enough to emit or bind a minimal `TaskSignature`, `TaskKind`, or `ProblemProfile`. Apply the governing FPF pattern for the claim being made, relation, or boundary instead of enlarging the card when the issue under repair is no longer the problem-side record itself.

#### C.22.2:2.5 - Field Labels and Current-Use Conditions

The first problem-side use is to make one problem usable before P2W by stating these field labels when they are current for the case:

- problem signal;
- problem signal reference: prior solution-use evidence, environmental drift observation, new constraint, new environment, underused capability, opportunity-like cue, risk signal, anomaly, hypothesis, stakeholder signal, accepted local theory, or safe-probe or environment cue;
- domain or practice locus when helpful, plus the context grounding that carries local meaning;
- EntityOfConcern or project-side FPF kind or reference named by value when it changes the problem-side use;
- context grounding;
- primary viewpoint or role concern;
- scope cut;
- symptom detection;
- problem hypothesis or cause-theory cue;
- rival-frame reference when multiple plausible problem frames remain current;
- improvement check;
- comparison-and-acceptance cue or acceptance-criterion reference;
- characterization relation;
- characteristic or Q-bundle relation;
- indicator selection;
- comparability or parity relation, or explicit current reason it is not needed;
- mandatory constraints;
- risk condition;
- problem-formulation follow-up reason;
- validation boundary;
- freshness or expiry condition;
- unknown handling;
- `setContextRef` when a set, pool, front, archive, shortlist, selected set, or portfolio context is current;
- `firstPrinciplesCue` for a first-principles or mathematical structure cue that changes problem formulation;
- governing-pattern cue when a claim outside `C.22.2` changes the problem-card use: governing pattern for that claim, relation, or boundary; claim kind named by value; project-side reference when known; and stop condition;

Field current-use conditions for `C.22.2` are determined as follows:

| Field current-use class | Required treatment |
|---|---|
| Always-core problem-card identity fields | State the problem signal or selected problem cue, context grounding, EntityOfConcern when it changes the problem-side use, scope cut, and the current reason this is not just a wish, slogan, ticket, or preselected task. |
| Conditional fields | State problem signal reference, domain or practice locus when helpful plus the context grounding that carries local meaning, viewpoint or role concern, symptom detection, problem hypothesis or cause cue, rival-frame reference when multiple plausible frames remain current, improvement check, comparison-and-acceptance cue or acceptance-criterion reference, characterization or comparability relation, characteristic or Q-bundle relation, indicator selection and indicator role, mandatory constraints, risk condition, problem-formulation follow-up reason, validation boundary, freshness or expiry, unknown handling, `setContextRef` or set-finding cue, first-principles cue, and representation-transition, retargeting, bridge, structural-reinterpretation, or wording-use relation reference when that relation affects reviewability. |
| Governing-pattern cue | When a claim, relation, or boundary outside `C.22.2` changes the card's next use, state only the local cue or reference needed by the problem card, plus the governing pattern and claim kind named by value to use next. The named pattern carries the outside use. |

Field absence rule: if a conditional field kind is not current, the field is absent, not `unknown`. Use `unknown` only for a current field whose value is currently unknown. If a current value is unavailable, state whether the next use is blocked, degraded, sandboxed, or requires the FPF pattern governing the named claim kind before that use. If a value is stale, use the freshness or expiry disposition in `C.22.2:12` and `G.11`. If a field is intentionally omitted, state the record-budget reason and do not imply that the omitted kind has been checked. A minimal `ProblemCard@Context` contains the always-core fields; conditional fields are added only when current for the problem-card use.

When the card compares options, selected-set members, retained candidates, or rival problem formulations, it states the current comparison or parity relation, or state why comparison is not current for the current move. Absence of a parity relation is not automatically a defect; it is a disposition. The governed result is either parity not current for the current card, or a `G.9`-governed parity relation before `P2W-ready` is claimed. A local fair-comparison result or selected-set result stays outside `C.22.2`.

A conforming `C.22.2` use includes minimal witness material and context witness material when source material, source relation, set, selection, characterization, parity, freshness, representation relation, or wording-use relation is current. Otherwise a Thin card may cite the observed signal in plain form. The field-group label `problemCardWitnessRefs` may be used inside the pattern, but it is not a new FPF kind and not an evidence graph. It is a recoverability field group for problem signal references and project-side references that make the problem-side record reviewable:

```text
problemCardWitnessRefs:
  problemSignalRef?
  setContextRef?
  selectionOrRetentionCriterion?
  characterizationRelationRef?
  parityRelationRef?
  freshnessRef?
  representationOrWordingUseRelationRef?
```

Generated problem variants, evaluator feedback, and open-ended problem mutation may be recorded only as `problemSignalRef`, `selectionOrRetentionCriterion`, or `setContextRef` when they make the problem-side record reviewable. They do not make the problem-side record usable, do not supply evidence sufficiency, and do not justify probe or action.

#### C.22.2:2.6 - Anti-Pattern Checks and Worked Slices

Anti-pattern checks start from the local card use:

- card-as-executable-work request: the card is treated as executable work while method, plan, and work occurrence remain undecided;
- form-completion: every field is filled because the template exists, even though the Thin next use would be truthful;
- readiness shortcut: `P2W-ready` is declared from signal and scope alone, without improvement check or acceptance probe;
- source-claim shortcut: a preselected solution, work request, proof-looking reference, gate-looking cue, or authority-looking cue replaces the problem-side signal, context, scope, acceptance probe, and next use;
- scalar shortcut: archive, set-return, Goldilocks, NQD, OEE, partial-order, stepping-stone, or indicator material collapses into one readiness score;
- prestige shortcut: first-principles or mathematical wording is kept without practical payoff, preserved and lost structure when current, problem-formulation follow-up reason, and stop condition.

Local stop rule: if the encountered material tries to carry a claim outside `C.22.2`, the card keeps only the cue or reference that changes problem formulation or the next use, then names the governing FPF pattern and claim kind named by value to use before that claim is relied on.

A conforming `C.22.2` use is testable against at least one Thin worked slice, such as repeated task rework or another compact problem signal, showing signal, context, not-preselected-work reason, improvement check, and next use. It is also testable against at least one High-relation worked slice from a set, archive, pool, front, shortlist, selected set, or portfolio context, showing `setContextRef`, candidate acceptance criterion, risk condition, and the claim being made, relation, or boundary without creating a local portfolio or archive kind.

#### C.22.2:2.7 - Conformance Checklist Requirements

The checklist protects a completed or reviewed card from overread. It is not the writing order and not a gate. The writing order remains Thin form, honest next use, and relation references only when they change the move.

| Check | Required test |
|---|---|
| Name and kind identity | The pattern output is `ProblemCard@Context`: a compact problem-side record shape under `C.22`; it is not a downstream selector record, work record, evidence record, gate record, or autonomy record. |
| Core card identity | The card states signal, context grounding, scope cut, EntityOfConcern when it changes the action, and the reason the record is not merely a wish, slogan, ticket, or preselected work request. |
| `P2W-ready` reason | `P2W-ready` appears only with an improvement check or acceptance probe and a downstream P2W or selector-facing use. It means problem-side input ready, not downstream readiness. |
| Field-budget discipline | Conditional fields appear only when current. A missing relation is absent, not `unknown`; `unknown` is used only for a current value whose absence changes the next use. |
| Governing-pattern cue | Claims outside `C.22.2` are recorded only as local cues or references when they change the card. The next use names the governing pattern and claim kind named by value for that use. |
| External or local wording | External terms such as passport, rule-of-choice card, evidence pack, autonomy budget, logs, gates, portfolio, or factory wording are recovered by use. They become problem-card content only when they supply problem-side signal, set, characterization, comparison, or follow-up material. |
| Scalarization and proxy guard | Goldilocks, NQD, OEE, set-return, partial-order, stepping-stone, priority, or visible indicator wording does not become one local readiness score or value proxy. |
| Currentness and lowering | Freshness, expiry, changed representation, retargeting, evidence change, redress, or unknown-blocked use states refresh, retirement, bounded use, `abstainOrNoChange`, or the relation named by value that is reopened. |
| First-principles and mathematical cue payoff | A first-principles or mathematical cue states practical payoff, preserved and lost structure when current, problem-formulation follow-up reason, and stop condition; `C.29` governs mathematical-lens use. |
| Record-budget invariant | The card is as small as the next use permits. A compact card template, relation aid, or worked example is not a separate FPF kind. |

