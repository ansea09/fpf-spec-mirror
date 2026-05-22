---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:2"
section_title: "Thin First Use and Output Kind"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__003_thin-first-use-and-output-kind.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:2 — Thin First Use and Output Kind"
line_start: 41725
line_end: 41948
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "A.6.Q"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.SEMIO"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
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
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:2 - Thin First Use and Output Kind

#### C.22.2:2.1 - Thin First-Use Form


The first substantive use of this pattern is the Thin form. It is a practitioner-facing prompt for writing the smallest reviewable problem card, not a demand to complete a field list.

A `ProblemCard@Context` is complete for its current use when it states:

1. why this signal matters now;
2. what problem representation is being carried under which context and scope;
3. why this is not merely a wish, ticket, slogan, or preselected work item;
4. what would count as improvement or an acceptance probe;
5. what the honest next move is.

The Thin form asks for:

- the problem signal or selected-problem cue: what made the practitioner stop before downstream task typing or work selection;
- context grounding and scope cut, including what is outside the current problem;
- the reason this is not merely a wish, slogan, ticket, or preselected work item;
- a provisional improvement check or acceptance probe;
- one honest next move: `P2W-ready`, characterize, compare, search, refresh, retire, archive, `abstain/no-change`, or a named neighboring-pattern exit.

If the Thin form lacks an improvement check or acceptance probe, it may preserve the signal or exit to characterization, comparison, search, refresh, retirement, archive, `abstain/no-change`, or a neighboring pattern, but it must not declare `P2W-ready`.

Only after the Thin pass is legible, recover the output-kind boundary:

`C.22.2 - ProblemCard@Context` is the compact problem-side output under current `C.22`.

`C.22.2 - ProblemCard@Context` is the pattern heading. `ProblemCard@Context` is the `C.22.2`-governed problem-side record shape; an instance is a reviewable problem-side record before P2W. `ProblemCard@ContextRef` may be used as a reference form when downstream text cites such an instance, but it is not a separate durable kind unless a separate naming or kind decision approves one under `F.18` and `A.6.P`. The Tech heading remains `C.22.2 - ProblemCard@Context`. Plain-register glosses or section-local practitioner labels may appear in this pattern, but those labels do not replace the Tech heading.

Local labels in this pattern are local to the `C.22.2` record shape unless a separate accepted FPF naming or kind decision assigns them a broader FPF kind or authority. This includes `support posture`, `validation boundary`, `risk posture`, `solvability band`, `P2W-ready`, `reviewable`, `sentToNeighbor`, `stale`, `refreshed`, `retired`, `archived`, `abstain/no-change`, and `firstPrinciplesCue`; they do not create FPF kinds, gate statuses, state-machine kinds, or local mathematical-lens objects. When a mathematical or first-principles cue is live, cite `C.29`; local `support posture` names only why the problem formulation or structure cue is worth reviewing or moving onward from `C.22.2`; `C.29` carries mathematical-lens adequacy and the support posture for that lens.

Reference labels ending in `Ref` are reference roles, not object names. This includes `ProblemCard@ContextRef`, `setContextRef`, `rivalProblemFormulationRef`, and `semioRelationRef`; do not shorten or promote them into local object kinds such as `ProblemCardRef`, `SetContext`, `RivalFrame`, or `SemioRelation`.



`@Context` means that the card is bound to declared context grounding: a named `U.BoundedContext`, a project-side context reference, or an explicitly bounded practice situation with recoverable local meaning. Domain or practice wording may identify the informative locus of the problem, but it does not replace context grounding. A broad label such as healthcare, education, engineering, research, or operations is not context grounding by itself. When domain or practice wording carries semantic load, recover the named bounded context, project-side context reference, or explicit bounded practice situation and state what local meaning or rule is being used. The card does not assert global problem identity outside that declared context grounding.

Plain gloss for `P2W-ready`: problem-side input ready. It means ready as input to downstream P2W or selector reasoning, not ready to execute work, pass a gate, or select a method.

#### C.22.2:2.2 - Required Solution Moves

The `C.22.2` Solution is organized around practitioner moves from signal to reviewable problem to one admissible next move, not around schema completion.

1. Capture the symptom, anomaly, risk, stakeholder cue, drift, hypothesis, or other source signal before naming the problem.
2. Stabilize the cheap problem-side record: context grounding, scope cut, described entity when load-bearing, primary viewpoint or role concern, and provisional problem framing.
3. Make action possible by separating the symptom detector, improvement check, candidate acceptance basis, optimization target when live, monitored risk signal when live, and proxy-distortion risk when an indicator can be gamed or substitute for value; then state mandatory constraints, risk posture when live, and intended next move before downstream selection.
4. Pay only for live complexity: add conditional fields only when their relation is live, and otherwise name the neighboring-pattern exit or stop at the lighter card.
5. Run the representation-continuity check: if the problem formulation changes the described entity, representation scheme, diagram, functional description, or TGA path reading, name the SEMIO exit before using inherited support.
6. Close by the honest next move rather than by a completed form. A filled card without a truthful next move is not a successful `C.22.2` result.

Cheap-stop rule: the smallest card that gives a truthful next move is sufficient. A conforming `C.22.2` use must not require heavier fields merely because the full field list exists.

First practitioner pass before neighboring exits:

1. Capture the problem signal or selected-problem cue, context grounding, and scope cut.
2. State why it is not merely a wish, slogan, ticket, or preselected work item.
3. State the provisional improvement check or acceptance probe.
4. Choose the honest next move.
Use the neighboring-exit aid only when a conditional relation is live.

This is the Thin-form writing order, not a completion sequence for the whole pattern. It adds no fields; it keeps the practitioner on the smallest truthful card before Standard or High-load relations are paid for.

#### C.22.2:2.3 - Neighboring-Exit Aid


Use this exit aid when a live relation appears while writing or reviewing a `ProblemCard@Context`.

Neighboring exits are authority boundaries, not orchestration steps. The aid names the receiving pattern where authority already lives; it does not give `C.22.2` authority over that pattern or make the neighboring relation local to the card.

Cue and abductive-entry boundary: use `C.22.2` only when the cue can be scoped as a problem-side representation with an improvement check, acceptance probe, or honest next move. If the material is still only a partly stated cue, several candidate meanings, or an explanation-ready prompt without problem-side scope, preserve it under `A.16.1`, `B.4.1`, or `B.5.2.0` before forcing `ProblemCard@Context`.

When `A.16.1`, `B.4.1`, or `B.5.2.0` has preserved or typed the cue, `C.22.2` may receive that cue only to stabilize one problem-side record with context, scope, improvement check or acceptance probe, and honest next move. It does not replace cue preservation, entry-load typing, or abductive prompt handling.
Failure mode: receiving-table over-capture. The practitioner spends the pattern use classifying neighboring patterns, or trying to fill every receiving-pattern column, while the problem signal, context grounding, scope cut, not-wish reason, improvement or acceptance probe, and honest next move remain unstable.

Repair: return to the Thin problem-side action. State the signal, context and scope, why this is not merely a wish, ticket, slogan, or preselected work item, the improvement check or acceptance probe, and the honest next move. Use the exit aid only after that Thin record exposes a live relation that needs a receiving pattern.

| Live relation | Receiving pattern | Permitted local cue or reference | Forbidden local decision |
|---|---|---|---|
| Characterization or measurement basis | `C.16` | Characterization basis, measurement cue, or current reason characterization is not live. | Measurement admission, full characterization protocol, or comparison authority. |
| Characteristics, indicators, scale, unit, or polarity | `A.19` | Characteristic or indicator cue, indicator role, and needed scale or polarity reference. | Indicator admission, scale repair, unit discipline, or characteristic ontology. |
| Q-bundle or multi-characteristic acceptance basis | `C.25` | Q-bundle cue, acceptance-basis cue, or need for multi-characteristic treatment. | Local Q-bundle definition, acceptance settlement, or quality scalarization. |
| Parity, comparability, comparator, budget, or window | `G.9` | Parity basis reference, comparator or window cue, or explicit reason parity is not live. | Fair-comparison claim or parity result. |
| Selected set, shortlist, archive, pool, front, or set-return | `G.5`, `C.18`, `C.19`, `G.11`, `A.6.P:7a`, `A.6.Q` | `setContextRef`, source set kind, selection or retention basis, and non-scalar next move. | Portfolio or archive governance, selected-set authority, single winner, or one readiness score. |
| Local choice among explicit options | `C.11` | Local choice cue and option-set reference when the live issue is choice rather than problem-card completion. | Choice record, chooser authority, or option evaluation. |
| Method-family selection or method cue | `G.5`, `E.18`, `A.15` | Method-family cue and reason method selection is not yet local work. | Method selection, method description, or selected method authority. |
| Work planning, performed work, or result record | `A.15`, `A.10`, `G.6`, `B.3` | Work need, performed-work cue, result-record cue, or work-authority exit. | Work plan, work authorization, performed-work record, or result certification. |
| Evidence need or evidence-looking source | `A.10` | Evidence cue, support posture, source reference, or evidence exit. | Evidence proof, evidence sufficiency, or self-evidence. |
| Provenance or source lineage | `G.6` | Provenance cue, source reference, or relation to a provenance record. | Provenance claim or lineage certification. |
| Assurance, safety reliance, or confidence | `B.3`, with `A.10` or `G.6` when support is live | Validation boundary, support posture, and assurance exit. | Assurance claim, safety-case acceptance, confidence marker, or proof. |
| Gate passage or gate decision | `A.21` | Gate cue, gate need, or relation to a gate record. | Gate passage, gate decision, release permission, or work authorization. |
| Autonomy permission or autonomy budget | `E.16` | Autonomy cue, autonomy risk, or need for autonomy governance. | Autonomy permission, autonomy budget, or delegated authority. |
| Refresh, expiry, stale signal, or unknown handling | `G.11` plus the affected receiving pattern | Freshness or expiry disposition, unknown handling, refresh, retire, bounded-use, or `abstain/no-change` cue. | Silent current validity after expiry or unknown-blocked P2W readiness. |
| Temporal claim: speed, cadence, recovery, adoption, lead time, rhythm, or learning rate | `C.27` | Temporal cue and reason it changes the next move. | Intervention model, trend-as-proof, or effort or rhythm doctrine. |
| Cause-theory, intervention, counterfactual, responsibility, or expected effect | `C.28` plus support or evidence patterns when live | Cause-theory cue that focuses formulation. | Causal-use claim, causal evidence, or transfer license. |
| Agentic call planning or safe probe | `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, `B.3` as applicable | Probe need, call-planning cue, risk posture, and authority exit. | Tool-call permission, delegation authority, world-affecting action, or safety reliance. |
| Representation transition or changed described entity | `A.6.3.RT`, `A.6.4`, `E.17`, `E.18` | `semioRelationRef`, representation-change cue, and support-inheritance boundary. | Same-entity proof or inherited support by wording continuity. |
| Retargeting | `A.6.4`, `E.18` | Retargeting cue and current described-entity boundary. | Claim that the old and new target are interchangeable. |
| Bridge, cross-context reuse, same, equivalent, or aligned wording | `F.9`, `E.17`, `E.18` | Bridge cue, context grounding, loss or congruence need. | Equivalence, alignment, or reuse authority by label alone. |
| Structural reinterpretation | `E.18`, with `C.29` when mathematical structure is live | Structural-reinterpretation cue and receiving-pattern exit. | Local proof that the reinterpretation preserves the problem. |
| Structure cue that improves formulation, including first-principles or mathematical structure when live | `C.29` | `firstPrinciplesCue`, candidate structure, practical formulation payoff, preserved and lost structure when live, support posture, and stop condition. | Mathematical adequacy proof, formalism choice, method selection, or decorative mathematics. |

#### C.22.2:2.4 - Use Boundaries and Profiles

Use this pattern when a signal, anomaly, drift, risk, hypothesis, or stakeholder pressure has appeared and the team must decide whether a problem-side record is needed before downstream task typing. Also use it when P2W would otherwise receive a slogan, wish, ticket-shaped task, preselected work item, or solution-shaped task; when the method is unknown, contested, or not specific enough for task typing, method-family selection, or work planning; or when the problem must become reviewable before method selection or P2W can honestly receive it.

Do not use this pattern as a work-planning record. If the method is already accepted and only work planning is live, use `A.15`. If evidence, proof, provenance, or assurance is central, use `A.10`, `G.6`, or `B.3`; `C.22.2` may name only a support cue or support posture. If gate passage or a gate decision is central, use `A.21`; `C.22.2` may name only a gate cue or neighboring exit. If the live issue is a local choice among explicit options, use `C.11` rather than treating the choice as problem-card completion. If archive, front, pool, selected-set, or portfolio governance is central, use `C.18`, `C.19`, or `G.5`; `C.22.2` may only preserve the `setContextRef` or set-source cue needed for the singleton problem-side record. If the conversation is only ordinary discussion with no downstream project-side move, do not use `C.22.2`.

Use profiles:

- Thin profile: signal, context grounding and scope cut, not-wish, not-slogan, not-ticket, or not-preselected-work reason, provisional improvement check or acceptance probe, and one honest next move.
- Standard profile: the Thin profile plus live fields needed when P2W or selector-facing use is likely: comparison-and-acceptance cue or acceptance-basis reference, mandatory constraints, risk posture, support posture, validation boundary, freshness or expiry, unknown handling, and named neighboring exits.
- High-load profile: conditional for public, disputed, high-risk, set-derived, cross-context, semio-transformed, evidence-adjacent, autonomy-adjacent, gate-adjacent, agentic, or Part-G-facing cases. It adds references and exits such as `setContextRef`, characterization, parity, support, evidence, gate, autonomy, work, temporal, causal, agentic call-planning, semio relation, and refresh references; it does not locally certify those relations.

Thin is not an immature profile. When it gives the honest next move, Thin is a final conforming result for the current use. High-load is not a higher maturity claim; it is a conditional profile required when public, disputed, high-risk, set-derived, cross-context, semio-transformed, evidence-adjacent, autonomy-adjacent, gate-adjacent, agentic, or Part-G-facing relations are live in the case.

The profile order is a reading aid, not a required transition sequence. Thin is the default entry; Standard and High-load add only liveness-triggered fields; neighboring exits are consulted after the Thin next move exposes a live relation.


Stop at Thin when the honest next move is local stabilization, local characterization, source reread, or another early problem-side clarification before P2W readiness is claimed. Stop at Standard when it is sufficient to emit or bind a minimal `TaskSignature`, `TaskKind`, or `ProblemProfile` for downstream selector-facing use without carrying high-load relations locally. Exit immediately instead of continuing the card when the live issue is work, evidence, provenance, assurance, gate, autonomy, bridge, representation transition, retargeting, structural reinterpretation, causal-use claim, temporal claim, agentic call planning, or refresh.


#### C.22.2:2.5 - Field Labels and Liveness

The governed move is to make one problem usable before P2W by stating these field labels when they are live for the case:

- problem signal;
- source signal basis: prior solution-use evidence, environmental drift observation, new constraint, new environment, underused capability, opportunity-like cue, risk signal, anomaly, hypothesis, stakeholder signal, accepted local theory, or safe-probe or environment cue;
- domain or practice locus when helpful, plus the context grounding that carries local meaning;
- described entity or exact project-side FPF kind or reference when load-bearing;
- context grounding;
- primary viewpoint or role concern;
- scope cut;
- symptom detection;
- problem hypothesis or cause-theory cue;
- rival-frame reference when multiple plausible problem frames remain live;
- improvement check;
- comparison-and-acceptance cue or acceptance-basis reference;
- characterization basis;
- characteristic or Q-bundle basis;
- indicator selection;
- comparability or parity basis, or explicit current reason it is not needed;
- mandatory constraints;
- risk posture;
- support posture;
- validation boundary;
- freshness or expiry condition;
- unknown handling;
- `setContextRef` when a set, pool, front, archive, shortlist, selected set, or portfolio context is live;
- `firstPrinciplesCue` for a first-principles or mathematical structure cue that changes problem formulation;
- neighboring-pattern exit.

Field liveness for `C.22.2` is determined as follows:

| Field liveness class | Required treatment |
|---|---|
| Always-core problem-card identity fields | State the problem signal or selected problem cue, context grounding, described entity when load-bearing, scope cut, and the current reason this is not just a wish, slogan, ticket, or preselected task. |
| Conditional-live fields | State source signal basis, domain or practice locus when helpful plus the context grounding that carries local meaning, viewpoint or role concern, symptom detection, problem hypothesis or cause cue, rival-frame reference when multiple plausible frames remain live, improvement check, comparison-and-acceptance cue or acceptance-basis reference, characterization or comparability basis, characteristic or Q-bundle basis, indicator selection and indicator role, mandatory constraints, risk posture, support posture, validation boundary, freshness or expiry, unknown handling, `setContextRef` or set-source cue, first-principles cue, and accepted `SEMIO-03` relation exit when that relation affects reviewability. |
| Exit-only fields | Evidence proof, gate passage, autonomy control, method selection, work planning, performed work, result record, and result measurement are not problem-card fields. `C.22.2` may carry only the cue or exit that sends the practitioner to the receiving pattern. |

Field absence rule: if a conditional relation is not live, the field is absent, not `unknown`. Use `unknown` only for a live relation whose value is currently unknown. If a live value is unavailable, state whether the next move is blocked, degraded, sandboxed, or sent to the receiving pattern. If a value is stale, use the freshness or expiry disposition in `C.22.2:12` and `G.11`. If a field is intentionally omitted, state the record-budget reason and do not imply that the omitted relation has been checked. Exit-only material is never completed locally; it is named as cue, reference, or exit. This split is part of the local answer. A minimal `ProblemCard@Context` contains the always-core fields; conditional fields are added when live; exit-only material is named as a neighboring-pattern exit instead of being absorbed into the card.

When the card compares options, selected-set members, retained candidates, or rival problem formulations, it must state the live comparison or parity basis, or state why comparison is not live for the current move. Absence of a parity basis is not automatically a defect; it is a disposition. The admissible result is either parity not live for the current card, or exit to `G.9` before `P2W-ready` is claimed. A local fair-comparison result or selected-set result is not admissible inside `C.22.2`.


A conforming `C.22.2` use includes minimal source and context witness material when source, set, selection, characterization, parity, freshness, or semio relation is live. Otherwise a Thin card may cite the observed signal in plain form. The field-group label `problemCardSource` may be used inside the pattern, but it is not a new FPF object and not an evidence graph. It is a recoverability field group for the source and neighboring references that make the problem-side record reviewable:


```text
problemCardSource:
  sourceSignalRef?
  setContextRef?
  selectionOrRetentionBasis?
  characterizationBasisRef?
  parityBasisRef?
  freshnessRef?
  semioRelationRef?
```

Generated problem variants, evaluator feedback, and open-ended problem mutation may be recorded only as `sourceSignalRef`, `selectionOrRetentionBasis`, or `setContextRef` when they make the problem-side record reviewable. They do not provide problem authority, evidence sufficiency, or permission to probe or act.


#### C.22.2:2.6 - Anti-Pattern Checks and Worked Slices

Anti-pattern checks begin with card-as-work-item: treating the card as work to execute while the method remains unselected is non-conformant. Filling every field merely to satisfy the form is also non-conformant; fields are required only by liveness, profile, and next-move need. Declaring `P2W-ready` from signal and scope alone is non-conformant when no improvement check or acceptance probe is present.

A preselected solution or work item such as "implement X" is non-conformant as a problem card unless a problem-side signal, context, scope, and candidate acceptance basis are recovered. Evidence, provenance, assurance, gate, and autonomy references inside the card are non-conformant if they are read as proof, gate passage, safety acceptance, or permission instead of a cue, reference, or exit to the receiving pattern.

Treating a problem portfolio, archive, pool, front, shortlist, or selected set as a task queue inside `C.22.2` is non-conformant; the card may only preserve `setContextRef` or a set-source cue and exit. Replacing Goldilocks, NQD, OEE, set-return, partial-order, or stepping-stone reasoning with one readiness score is non-conformant. A first-principles or mathematical cue without practical payoff, preserved and lost structure when live, support posture, and stop condition is non-conformant.

A conforming `C.22.2` use is testable against at least one Thin worked slice, such as repeated task rework or another compact source signal, showing signal, context, not-preselected-work reason, improvement check, and next move. It is also testable against at least one High-load worked slice from a set, archive, pool, front, shortlist, selected set, or portfolio context, showing `setContextRef`, candidate acceptance basis, risk posture, and neighboring exits without creating a local portfolio or archive kind.

#### C.22.2:2.7 - Conformance Checklist Requirements

Checklist role boundary: this checklist protects against overread after the practitioner has written or reviewed the card. It is not the writing order, not a mandatory field-completion sequence, and not a gate. The writing order remains Thin form, honest next move, and live exits only when their relation is live.

| Check | Required test |
|---|---|
| Name and kind identity | A conforming `C.22.2` use keeps the pattern heading as `C.22.2 - ProblemCard@Context` and treats the governed output as a problem-side record shape, not `U.Problem`, `TaskSignature`, `U.WorkPlan`, an evidence object, a gate object, or an autonomy object. |
| Pattern scope boundary | A conforming `C.22.2` use does not present a complete problematization methodology, process model, method model, or work model. It governs the problem-side record before P2W; method, work, evidence, gate, autonomy, organization-capability, and other heavier concerns exit to the receiving patterns named for this pattern. |
| No new `U.` kind | A conforming `C.22.2` use does not introduce `U.ProblemCard@Context`, `U.ProblemCard`, or another `U.`-prefixed problem-card kind. `ProblemCard@Context` remains the `C.22.2`-governed problem-side record shape used by this pattern. |
| Core card identity | A conforming `ProblemCard@Context` states the problem signal or selected-problem cue, context grounding, scope cut including outside scope, described entity when that entity is load-bearing, and the current reason the record is not merely a wish, slogan, ticket, or preselected work item. |
| Cue, reference, and exit discipline | A conforming `C.22.2` use marks heavy neighboring relations as cue, reference, or exit rather than local governing content. Support posture, validation boundary, gate need, evidence need, `setContextRef` or set-source cue, work need, autonomy cue, refresh need, and semio relation may be named only in the role that sends the practitioner to the receiving pattern or preserves the needed reference. |
| No pre-binding by card | A conforming `ProblemCard@Context` does not by itself select a method, plan work, record performed work, pass a gate, prove evidence, grant autonomy, or select a solution. It may mention a work need, but it does not create a WorkPlan-shaped `PlanItem`. It may name only the problem-side cue, reference, or neighboring-pattern exit needed before those relations are handled elsewhere. |
| `P2W-ready` basis | A conforming `ProblemCard@Context` marked `P2W-ready` states an improvement check or acceptance probe and the intended downstream move. `P2W-ready` means sufficient problem-side record for downstream P2W or selector-facing use; it is not work-authorized, not gate-passed, and not method-selected. If that basis is absent, the card may remain reviewable or exit elsewhere, but it must not claim `P2W-ready`. |
| Readiness disposition | A conforming `ProblemCard@Context` states whether it is reviewable-only, `P2W-ready`, or sent to a neighboring pattern. A reviewable-only card must not bind `TaskSignature`. |
| Minimal downstream anchor | When `ProblemCard@Context` emits or binds `ProblemProfile`, `TaskKind`, or `TaskSignature`, a conforming result keeps the downstream `C.22` object minimal and selector-facing. It must not copy the full card fields into `TaskSignature` or make the downstream anchor a work plan. |
| Source-local term recovery | A conforming `C.22.2` use treats source-local terms such as problem factory, solution factory, passport, rule-of-choice card, evidence pack, autonomy budget, logs, gates, and portfolio wording as ordinary source wording or maps them to named receiving patterns. It must not mint them as `C.22.2` subkinds. |
| Acceptance and comparability exits | A conforming `ProblemCard@Context` may state an acceptance probe, candidate acceptance basis, comparison-and-acceptance cue, or acceptance-basis reference, but it does not create local acceptance authority. It sends comparison-frame or CG-Spec governance to `G.0`, acceptance clauses and threshold predicates to `G.4`, parity or comparability questions to `G.9`, and characterization, characteristic, indicator-admissibility, or Q-bundle basis to `C.16`, `A.19`, or `C.25` when those relations are live, instead of settling that basis locally. |
| Detector, check, criterion, and optimization-target distinction | A conforming `ProblemCard@Context` distinguishes symptom detector, improvement check, candidate acceptance basis, optimization target, monitored risk signal, and proxy-distortion risk when those relations are live. A measured value or observed improvement is not by itself an acceptance result for P2W. |
| Set-source reference preservation | When a `ProblemCard@Context` comes from an archive, pool, front, shortlist, selected set, or portfolio, a conforming card cites the existing receiving pattern such as `C.18`, `C.19`, or `G.5` when the set relation is live, preserves `setContextRef` and the selection or retention basis, and does not turn that reference into a new `C.22.2` portfolio or archive kind or task queue. |
| Causal cue boundary | A conforming `ProblemCard@Context` treats local cause-theory wording as a formulation cue unless a causal-use claim is explicitly made. Any causal-use claim exits to `C.28` and the needed support or evidence pattern when live; a local cause-theory cue is not evidence of cause and does not license causal transfer by itself. |
| Temporal claim exit | If speed, cadence, throughput, recovery, adoption, learning rate, review rhythm, lead time, freshness window, or expiry wording changes the next move, a conforming `ProblemCard@Context` names the temporal claim and exits to `C.27`. The card may preserve the cue; it does not turn a trend, cadence note, or freshness field into an intervention model. |
| Representation-relation exit | When representation transition, retargeting, bridge, structural reinterpretation, or changed described entity is live, a conforming `ProblemCard@Context` names the receiving relation in `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, or `E.18` as appropriate. Wording continuity is not same-entity proof, and the card must not inherit support across the changed representation by wording continuity alone. |
| Posture and authority boundary | A conforming `ProblemCard@Context` keeps support posture, validation boundary, risk posture, and next move as problem-side fields or neighboring exits. Support posture means the current reason the problem formulation is worth reviewing or moving onward. It is not a confidence marker, evidence sufficiency, evidence proof, provenance, assurance claim, engineering justification, gate passage, safety-case acceptance, release permission, autonomy permission, or work authority. Validation boundary is not an assurance claim or safety-case acceptance; risk posture is not autonomy permission; next move is not work authority. |
| Support-posture citation boundary | A `ProblemCard@Context` citation is non-conformant if it is used as evidence, gate passage, safety acceptance, assurance, release permission, autonomy permission, or work authorization without naming the receiving pattern record that carries that relation. |
| Freshness and unknown disposition | A conforming `ProblemCard@Context` states whether freshness and unknown handling permit the intended use, require bounded or degraded use, require `abstain/no-change`, require sandbox treatment, require refresh, or block P2W. Expiry or unknowns may not remain as passive notes. |
| Record-budget invariant | A conforming `ProblemCard@Context` is as small as the next move permits. A Thin card is valid when it prevents wish, ticket, or solution-shaped-task collapse and names the next move honestly. The full field set is used only when the corresponding relation is live. |
| No scalar readiness shortcut | A conforming `ProblemCard@Context` does not turn Goldilocks, NQD, OEE, set-return, partial-order, or stepping-stone wording into one local readiness score or a local QD or OEE vocabulary. Those terms may appear only as cue or exit to the current receiving patterns when their relation is live. |
| First-principles and mathematical cue payoff | A conforming first-principles or mathematical cue states the practical payoff for problem formulation, the preserved and lost structure when live, the support posture, and the stop condition or `C.29` exit. A cue without those recoverable elements is not load-bearing action guidance. |

Do not treat a compact card template or worked example as a separate FPF object or pattern.

