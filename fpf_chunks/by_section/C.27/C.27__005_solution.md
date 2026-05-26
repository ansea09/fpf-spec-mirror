---
chunk_kind: "child"
pattern_id: "C.27"
pattern_title: "Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change"
section_id: "C.27:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27/C.27__005_solution.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.27 — Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change"
  - "C.27:4 — Solution"
line_start: 46286
line_end: 47126
dependencies:
  - "A.3.3"
  - "B.1.4"
  - "B.1.6"
  - "C.16"
  - "C.18.1"
  - "C.19"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.26"
  - "C.26.3"
  - "C.27"
  - "C.28"
  - "G.9"
  - "U.Rhythm"
keywords:
  - "braking"
  - "coasting"
  - "dynamic benchmark"
  - "effort window"
  - "intervention-sensitive temporal change"
  - "rate reading"
  - "rate-change"
  - "recovery"
  - "resistance/inertia"
  - "rhythm/cadence"
  - "stabilization"
  - "state reading"
  - "temporal claim"
  - "temporal claim adequacy"
  - "temporal trend"
  - "throughput"
---

### C.27:4 - Solution


Use the least-committing dynamic-order output that changes the admissible use. Dyn0 and Dyn1 are readings in ordinary prose, not C.27 record classes; C.27 records start only when a `Dyn2TemporalClaimAdequacyCard` or `Dyn2TemporalClaimProfile` for boundary-crossing claim use is needed.

| Level | User-visible move | Stop condition |
| --- | --- | --- |
| **Skip** | Leave as ordinary prose | temporal wording does not change claim/use |
| **Dyn0 reading** | state reading or snapshot only | snapshot is enough |
| **Dyn1 reading** | rate, trend, or trajectory only, or C.16-compatible measure when load-bearing | no intervention-sensitive claim |
| **Dyn2TemporalClaimAdequacyCard** | one-screen `Dyn2TemporalClaimAdequacyCard` | local plan, diagnostic, rhythm, effort, or intervention clarity is enough |
| **Dyn2TemporalClaimProfile** | `Dyn2TemporalClaimProfile` with active profile blocks only | the authored temporal claim is used beyond the local working context, is published, benchmarked, promised, assured, made durable rationale, repeated in a reusable method description, used in a gate/public dashboard/Part G pack, or carried across context/scale |
| **Formal-model relation** | C.27 states the temporal-claim question and cites the pattern that carries the formal claim | reusable law, simulation, prediction, control, calibrated model, or assurance-bearing comparison is claimed |

A Dyn2 classification is not evidence that a `U.Dynamics` model exists. It is
only evidence that the authored claim is using temporal change in a way that may
need a dynamics pattern relation if a downstream claim, effect, or use is claimed.

Normativity follows boundary-crossing use:

- normative when the claim carries decision, gate, budget, benchmark,
  publication, assurance, public promise, or reusable method;
- advisory when the claim is exploratory, abductive, or early planning;
- informative when the pattern teaches examples, vocabulary, or anti-patterns.

This is the ordinary first-minute reader-facing form and the main visible C.27 record
for ordinary C.27 use. It remains anchored to an authored claim rather than
becoming a free-standing consulting card.

```text
Dyn2TemporalClaimAdequacyCard

claimText / claimRef:
  What sentence, claim, plan line, benchmark line, or promise-like wording is being read?

target:
  What rate, rhythm, regime, recovery, trajectory, or stability reading is being changed?

move:
  accelerate | decelerate | brake | redirect | coast | pause |
  stabilize | recover | sustain | widen | narrow | domain-local

intervention:
  What effort, input, policy, method, resource, tool-use change, or action is supposed to change it?

window:
  Over what claim, sampling, effort, rhythm, or validity window?

resistanceOrCost:
  What resists, delays, stores momentum, creates residue, or makes the change costly?

basis:
  What evidence, trace, model, assumption, or diagnostic judgement supplies the basis for this reading?

basisPosture?:
  assumption | observedTrace | measured | modelled | diagnostic |
  planning | benchmark-referenced | causal-use-referenced |
  promise/assurance-referenced | unknown

supportedUse:
  What decision, plan, diagnosis, comparison, or pattern relation can this record carry?

unsupportedUse / reopen:
  What downstream claim, effect, or use is unsupported, and what would reopen, downgrade, or add a pattern reference to this claim?
```

Window default: for a local card, one `window` line may stand for claim, sampling,
effort, rhythm, and validity when the distinction does not change admissible use.
Split windows only when evidence is sampled over a different interval than the
claim, effort or intervention occurs over a different interval than the outcome,
benchmark baseline/adaptation/follow-up windows differ, the rhythm anchor/window
differs from the measurement window, or validity/refresh depends on a separate
freshness window.

Optional `basisPosture?` is the card-level bridge to profile posture. It names the
local evidence-support or source-support posture without making the card a full
profile. When the claim later crosses a boundary, `basisPosture?` helps choose
the matching `dynClaimPosture`; it does not strengthen the claim by itself.

`claimText` and `claimRef` keep C.27 tethered to the `PublicationUnit` or claim-bearing `U.EpistemePublication` that carries the temporal claim. `target`
separates the bearer/reading from the intervention, so "we accelerate the team"
gets repaired into a rate/rhythm/trajectory question. `move` protects against
acceleration bias: braking, pausing, stabilization, recovery, coasting,
widening, and narrowing are also Dyn2 moves when they change admissible use.

If the author cannot answer these in short lines, the correct repair is usually
to clarify the claim, not to escalate immediately to a full `Dyn2TemporalClaimProfile`.

Compact C.27 rhythm-claim discipline:

```text
dyn2RhythmClaimBlock? / Dyn2TemporalClaimAdequacyCard fields:
  rhythmBearerRef : whose or what rhythm?
  rhythmAnchor : beat | cadence | cycle | sprint | epoch | release train | attention window | domain-local anchor
  rhythmWindowRef : over what interval?
  instrumentProxyOrEvidenceRef? : trace | proxy | observation | measurement reference
  supportedUse : what decision or reading this record can carry
  couplingMode? : only when cross-bearer synchronization, phase relation, dependency, coordination, or entrainment-like practice relation is claimed
  validityWindowRef? : only when the rhythm reading is used beyond the immediate working window
```

Cadence as observed interval rate may be Dyn1. Rhythm becomes Dyn2 only when
interval structure, effort pattern, coordination, recovery, stabilization, or
intervention-sensitive use changes admissible use.

This discipline keeps rhythm connected to a dynamic claim. A plain "release cadence" or "workshop rhythm" does not need phase or entrainment language unless the admissible use depends on a relation between bearers. If the rhythm wording does not change a rate, intervention, recovery, coordination, or admissible-use reading, it should remain ordinary prose rather than make C.27 relevant.

Compact C.27 coasting-claim discipline:

```text
dyn2CoastingClaimBlock? / Dyn2TemporalClaimAdequacyCard fields:
  coastingClaim : movement, stability, adoption, quality change, queue drain, operational-support load, or practice persistence continues after effort changes or stops
  coastingBasis : habit | automation | stored work | queue pressure | learned capability | commitment momentum | social norm | physical inertia | unknown
  coastingWindowRef : over what interval after effort changes or stops?
  supportedUse : what decision, plan, diagnosis, comparison, or local practice reading this record can carry
  unsupportedUse : what downstream claim, effect, or use this coasting reading does not support
  reopenTrigger : what change, decay, stall, reversal, hidden cost, or new evidence reopens the claim
```

Coasting becomes a full `Dyn2TemporalClaimProfile` block only when a promise,
gate, assurance, benchmark, cross-scale transfer, or public comparison depends
on continued movement or stability after effort changes or stops. Local cases
such as adoption continuing after incentives stop, quality degrading after
acceleration stops, operational-support load continuing after rollout, a trained practice
persisting after training, or a queue draining after intervention ends usually
need only the card fields above.

Coasting/debt fork:

- Use `dyn2CoastingClaimBlock?` when supported use depends on continued
  movement, stability, adoption, queue drain, practice persistence, or
  operational-support load after effort changes or stops.
- Use `dyn2DebtHysteresisBlock?` when supported use depends on residue,
  reversibility, hidden cost, delayed damage, repayment, braking, or recovery
  plan.
- If both are live, coasting describes continued motion or stability; debt and
  hysteresis describe what remains and how costly reversal or recovery is.

**Rare boundary-crossing escalation.** Use the `Dyn2TemporalClaimProfile` only for authored temporal claims used beyond the local working context. It is a pattern-local authored temporal-claim adequacy record, not a model of the dynamic system itself, not a publication role, not a Part G record, not an MVPK face, and not the default C.27 record.

Read the profile-block menu only when boundary-crossing use is already live. The list below is a pattern-relation menu, not a form. The absence of an inactive block is normal; it is not a missing field.

The shape is a header plus present profile blocks. The header carries the minimum boundary-crossing claim-use posture. Each block should be read from its applicability sentence first, and a block appears only when `supportedUse` relies on that claim relation. These blocks are not fields of one universal dynamic object; they are different evidence descriptions and pattern relations made relevant by supported use.

Profile-block closure rule: every present block is either defined by C.27,
a pattern-reference-only block that cites the existing FPF pattern carrying the
other question and adds no new C.27 object, or absent from `activeBlocks`.
A block name is not a new governed object.

Active-block naming rule: read each `activeBlocks` name by one of three statuses.
`localAdequacyBlock` means C.27 states local adequacy fields for an authored
temporal claim. `patternReferenceOnly` means C.27 states only the temporal
move/window/supported-use boundary and cites the FPF pattern that carries the
other question. `relationOnly` means the concern appears in relations or
examples but not as an active block. `dyn2PromiseBoundaryRoute?`,
`dyn2HighStakesTemporalMoveRoute?`, and `dyn2PolicyTransferRoute?` are
pattern-reference-only by default; `dyn2PolicyTransferRoute?` is folded into
`dyn2ControlPolicyRoute?` when behavior-policy/evaluation-policy transfer is
load-bearing.


```text
Dyn2TemporalClaimProfile {
  header:
    claimRef
    describedEntityRef
    temporalBearerRef?
    profileCarrierRef?
    dynClaimPosture
    dynOrder
    baseCharacteristicRef?
    claimWindowRef
    supportedUse
    unsupportedUse
    reopenTrigger

  activeBlocks:
    c16RateMeasurementRouteRef? // if rate/rate-change measurement evidence is load-bearing
    dyn2EffortWorkBlock? // if effort, resource, work, intervention actor, or authority basis is load-bearing
    dyn2ResistanceInertiaBlock? // if resistance, delay, residue, reversibility, or cost is load-bearing
    dyn2RhythmClaimBlock? // if rhythm or cadence changes admissible use
    dyn2CoastingClaimBlock? // if boundary-crossing use depends on continued movement or stability after effort changes or stops
    dyn2CausalUseRoute? // if rate-change or intervention is used as a causal-use basis
    dyn2BenchmarkParityBlock? // if comparison/benchmark depends on rate, rate-change, rhythm, recovery, or intervention effect
    dyn2MetricTargetEffectBlock? // if metric publication or target use changes temporal behavior or admissible use
    dyn2ObjectCentricTraceBlock? // if work-cycle or service-process evidence depends on object-centric or multi-bearer traces
    dyn2ScaleVariableClaimBlock? // if changing a resource or scale variable is claimed to change rate, learning, recovery, or throughput
    dyn2TaskFamilyAdaptationRoute? // if learning/adaptation-rate claim depends on a declared task-family specialization signature
    dyn2ControlPolicyRoute? // if control, feedback, policy update, adaptive regime, or MPC/RL-style evaluation basis is load-bearing
    dyn2PolicyTransferRoute? // pattern-reference-only alias inside dyn2ControlPolicyRoute? when behavior-policy/evaluation-policy transfer is load-bearing
    dyn2CrossScaleTransferBlock? // if dynamic claim transfers across bearer, level, scale, or aggregate
    dyn2ViabilityEnvelopeRoute? // if rate-change, braking, rhythm, or stabilization is used to keep a viability envelope inside usable bounds
    dyn2DebtHysteresisBlock? // if admissible use relies on sustained acceleration, braking, recovery, stabilization, or residue after effort changes
    dyn2PromiseBoundaryRoute? // pattern-reference-only when promise, SLA/SLO, gate, assurance, or public commitment is live
    dyn2HighStakesTemporalMoveRoute? // pattern-reference-only when high-stakes acceleration, braking, redirection, or rollout is live
    dyn2QLResidualRoute? // if residual probe, frame, order, export, or coarsening cue remains after ordinary FPF pattern relations
}
```

Absence of an inactive block is normal. It is not a missing field. A block
becomes active only when the admissible use relies on it; otherwise the `Dyn2TemporalClaimProfile`
should stay smaller or downgrade to a `Dyn2TemporalClaimAdequacyCard`, Dyn1 reading, or ordinary prose.

Pattern-reference-only blocks:

- `dyn2PolicyTransferRoute?` is handled inside `dyn2ControlPolicyRoute?` when
  behavior-policy/evaluation-policy or off-policy transfer is load-bearing. C.27
  names `behaviorPolicyRef`, `proposedPolicyRef`, `offPolicyRisk`, and the
  evaluation/control pattern relation; it does not create a separate policy-transfer
  pattern.
- `dyn2PromiseBoundaryRoute?` states only the temporal move, window,
  supported use, unsupported downstream claim, effect, or use, and references to the patterns that
  carry promise, commitment, instituting speech act, service acceptance,
  contract unpacking, and assurance: `A.2.3`, `A.2.8`, `A.2.9`, `A.6.C`,
  `F.12`, and assurance patterns.
- `dyn2HighStakesTemporalMoveRoute?` states only the high-stakes temporal move, window,
  unsupported downstream claim, effect, or use, and reference to the pattern that carries the harm,
  quality, safety, ethics, legal, financial, operational-support, or
  human-wellbeing question.

Header discipline: for a `Dyn2TemporalClaimProfile` for boundary-crossing claim use, `claimRef`,
`describedEntityRef`, `dynClaimPosture`, `dynOrder`, `claimWindowRef`,
`supportedUse`, `unsupportedUse`, and `reopenTrigger` are mandatory.
`temporalBearerRef` is present when the temporal bearer differs from the
described entity or is otherwise load-bearing. `profileCarrierRef` is present
when publication or evidence needs the authored carrier named. `baseCharacteristicRef`
is mandatory only when measurement, comparison, or C.16 relation is load-bearing; for a Plain diagnostic claim it may remain a local phrase in the `target` line.

Window split rule: one local window is enough only when the claim window,
sampling window, effort/intervention window, validity window, baseline window,
and follow-up window are the same for the admissible use. Split them when the
evidence is sampled over a different interval than the claim, effort is applied
before or after the measured change, a comparison needs a baseline, an outcome is
observed after exposure, or the claim remains valid only for a shorter period
than the historical trace. If the split is unknown and the admissible use depends
on it, downgrade the use or add the relevant window reference before relying on
the temporal claim.

C.16 rate-measurement relation: when rate or rate-change is load-bearing, C.27
cites the C.16 measurement relation. C.27 does not define measurement
legality.

```text
c16RateMeasurementRouteRef? {
  baseCharacteristicRef
  stateMeasureRef?
  rateMeasureRef?
  rateChangeReadingMeasureRef?
  DHCMethodRef?
  samplingWindowRef
  scaleUnitPolarityRef?
  evidenceStubRefs?
  stabilityOrNoisePosture?
  C16RouteRef
}
```

C.27 effort/work block: when a rate-change claim depends on effort, resource,
method, intervention actor, or role-assignment capacity, C.27 separates planned
effort, method description, resource envelope, actual work trace, and
authority/capability posture. It does not turn work evidence into a dynamics law.

```text
dyn2EffortWorkBlock? {
  causalInterventionSpecRef?
  plannedEffortRef?        // WorkPlan / MethodDescription / resource envelope
  actualEffortTraceRef?    // U.Work / Gamma_work evidence
  effortWindowRef?
  interventionActorRef? {
    actorOrRoleAssignmentRef
    authorityPosture: authorized | proposed | hypothetical | unknown
    capabilityOrScopeRef?
  }
  resourceEnvelopeRef?
  A15RouteRef?
}
```

`interventionActorRef` means the actor, role assignment, tool, system, policy
rule, or human/work arrangement claimed to apply the intervention, plus an
authority/capability posture. If a planning claim says "add review capacity", C.27
should make it visible whether that capacity is assigned, capable, available,
authorized, proposed, hypothetical, or unknown, while leaving role, method, work-plan, and work-occurrence
alignment to A.15 and work patterns.

C.27 resistance/inertia block: `dyn2ResistanceInertiaBlock?` is present when admissible use depends on what resists, delays, stores momentum, creates residue, or makes the change costly. This is core C.27 content because it prevents effort-free acceleration claims. The `Dyn2TemporalClaimAdequacyCard` asks the question locally; the `Dyn2TemporalClaimProfile` uses a separate active profile block only when that answer matters beyond the local working context.

```text
dyn2ResistanceInertiaBlock? {
  resistanceOrInertiaProxy
  resistanceProxyFamily
  resistanceProxyBasisPosture: qualitative | measured | modelled | assumed | unknown
  evidenceRef?
  unsupportedUse?
}
```

`resistanceProxyBasisPosture = unknown` is an acceptable C.27 result. Unknown resistance need not
block a local diagnostic `Dyn2TemporalClaimAdequacyCard`, but it should block durable
acceleration, causal, benchmark, promise-like, or assurance use until a higher evidence-support class
or carrying pattern reference is supplied.

C.27 control/policy relation: `dyn2ControlPolicyRoute?` is present only when `dynClaimPosture` is `controlModel`, `policyRule`, `adaptive`, a feedback-bearing `planningModel`, or an explicit C.24/C.19/evaluation relation. This relation says that the authored temporal claim has crossed into control/policy model or policy-evaluation use. It does not make C.27 an MPC, reinforcement-learning, or policy-evaluation pattern.

```text
dyn2ControlPolicyRoute? {
  interventionRegime
  controlHorizon?
  closedLoopUpdate?
  behaviorPolicyRef?
  proposedPolicyRef?
  offPolicyRisk?
  stopRule?
  controlPolicyRouteRef -> U.Dynamics / C.19 / C.24 / evaluation pattern
}
```

C.27 causal-use relation: `dyn2CausalUseRoute?` is present only when the authored temporal claim uses a rate-change, intervention, effort, workshop, policy, or practice change as a causal-use basis. Core rule: C.27 can say a claim is Dyn2 and intervention-sensitive; C.27 cannot turn that basis into a `C.28`-governed causal-use claim. The fields below are `C.28` refs consumed by C.27, not `C.27`-defined causal aliases.

```text
dyn2CausalUseRoute? {
  causalInterventionSpecRef
  comparatorOrCounterfactualRef
  timeZeroOrAssignmentWindow
  followUpWindowRef
  outcomeMeasureRef
  estimandRef?
  causalAssumptionSetRef?
  rivalCauseSetRef?
  causalIdentificationProfileRef?
  causalUseEvidenceDesignRef?
  offPolicyCausalEvaluationProfileRef?
  supportedCausalUse
  unsupportedCausalUse
}
```

C.27 dynamic benchmark requirement: `dyn2BenchmarkParityBlock?` is present only when a comparison or benchmark depends on rate, rate-change, recovery speed, rhythm improvement, intervention effect, effort budget, or dynamic outcome. Content rule: C.27 declares the dynamic claim question of the benchmark; `G.9` carries parity.

```text
dyn2BenchmarkParityBlock? {
  comparedClaimRefs
  dynOrderCompared: Dyn1 | Dyn2
  baselineWindowRef
  adaptationOrInterventionWindowRef?
  budgetOrEffortParityRef?
  rateOrRateChangeReadingMeasureRef?
  G9ParityPlanRef
  G9ParityReportRef?
}
```

C.27 metric-target effect block: `dyn2MetricTargetEffectBlock?` is present only
when metric publication, target use, incentive use, dashboard use, gate use, or
public comparison changes temporal behavior or admissible use. C.16 carries the
measure; E.13, assurance, or governance patterns carry proxy/utility distortion;
C.26 is relevant only if residual probe, frame, order, or export cue remains.

```text
dyn2MetricTargetEffectBlock? {
  publishedOrTargetedMeasureRef
  targetOrIncentiveUse
  dashboardGatePromiseOrBudgetUse?
  behaviorChangeRisk
  temporalWorkChangeVsMeasurementChangeNote
  C16RouteRef?
  E13ProxyAuditRef?
  C26RouteRef? // only if residual probe, frame, order, or export cue remains
}
```

C.27 object-centric trace block: `dyn2ObjectCentricTraceBlock?` is present only
when a work-cycle/process rate claim depends on several object bearers, event
traces, interactions, or aggregation basis rather than one scalar speed label.
C.27 records why scalar throughput is insufficient; object-centric process
mining or local process evidence carries the detailed log discipline.

```text
dyn2ObjectCentricTraceBlock? {
  bearerKind: single-object | multi-object | aggregate | proxy
  objectTypeRefs
  eventTraceRef
  interactionOrCouplingNote?
  convergenceDivergenceRisk?
  aggregationRoute?
  supportedUse
  unsupportedUse
}
```

C.27 cross-scale transfer field: `dyn2CrossScaleTransferBlock?` is present only when a dynamic claim transfers rate, rate-change, rhythm, recovery, acceleration, braking, or agility from one bearer/level/aggregate to another. Aggregate rate-change and local rate-change are different readings unless aggregation basis and bearer continuity are declared.

```text
dyn2CrossScaleTransferBlock? {
  sourceBearerRef
  targetBearerRef
  aggregationRoute?
  mixShiftRisk?
  dynamicTransferPosture
}
```

C.27 scale-variable claim block: `dyn2ScaleVariableClaimBlock?` is present only when the
authored temporal claim says that changing a resource or scale variable changes
rate, improvement, learning, recovery, throughput, or stabilization. This is
not the same as cross-scale transfer: scale-variable claim asks which variable is
changed and over what scale window; cross-scale transfer asks whether a dynamic
reading is carried across bearer, level, or aggregate. C.18.1 carries scale
variables, scale windows, scale probes, and elasticity posture; C.27 records
only that the scale change is being used as the basis for a temporal-claim reading.

```text
dyn2ScaleVariableClaimBlock? {
  scaleVariableRef
  scaleWindowRef?
  scaleElasticityPosture: rising | knee | flat | declining | unknown
  C18_1RouteRef?
  G9ParityPlanRef?
}
```

C.27 task-family adaptation relation: `dyn2TaskFamilyAdaptationRoute?` is present
only when the temporal claim says that a holder, dyad, team, specialist
portfolio, method, or agent reaches usable specialization faster on one declared
`TaskFamilyRef` or `TaskSignature`. C.22.1 carries the task-family adaptation
signature. C.27 records only the learning/adaptation-rate question and the
admissible use that made it relevant.

```text
dyn2TaskFamilyAdaptationRoute? {
  TaskFamilyRef?
  TaskSignature?
  thresholdOrUsableSpecializationRef?
  timeToThresholdRef?
  budgetToThresholdRef?
  C22_1RouteRef
}
```

C.27 viability-envelope relation: `dyn2ViabilityEnvelopeRoute?` is present only when
a temporal claim says braking, slowing rollout, throttling, cadence change,
recovery timing, adaptation cost, operational-support load, or stabilization keeps a
viability bearer inside usable bounds. C.27 may type the temporal move and its
window. C.26.3 carries the viability-envelope claim: protected promise or
function, viable bounds, disturbance, sensor/probe/action split, adaptation
cost, and failure mode. Do not make C.27 the pattern for all "stability through
change" claims.

```text
dyn2ViabilityEnvelopeRoute? {
  viabilityBearerRef?
  protectedPromiseOrFunctionRef?
  temporalMoveRef?
  C26_3RouteRef
}
```

C.27 residual QL relation: `dyn2QLResidualRoute?` is present only when ordinary FPF
patterns have already carried the temporal-claim, measurement, work, benchmark,
value/proxy, scale, adaptation, viability, promise, or evidence basis and a
residual probe, frame, order, export, or coarsening cue still changes the admissible
reading. C.26 carries the residual QL reading. C.27 only records that the authored
temporal claim has a residual QL relation; this block stays hidden by default when
no such residue exists.

```text
dyn2QLResidualRoute? {
  residualQLCue?
  residualQLRouteRef?
  ordinaryRouteBasisRef?
  C26RouteRef
}
```

C.27 debt/hysteresis block: `dyn2DebtHysteresisBlock?` is present only when admissible use depends on sustained acceleration, braking, recovery, stabilization, domain residue after effort changes, or a public promise/gate/assurance/high-stakes decision about rate-change. Unknown reversibility is allowed, but it bounds supported use.

```text
dyn2DebtHysteresisBlock? {
  debtKind?
  debtWindowRef?
  evidenceRef?
  reversibilityPosture: reversible | costlyToReverse | irreversibleWithinWindow | unknown
  hysteresisOrResidue?
  repaymentOrBrakePlan?
  debtHysteresisRouteRef -> planning / assurance / quality / wellbeing / safety pattern
}
```

These C.27 dynamic-claim profile-block field definitions are boundary-crossing
material for `Dyn2TemporalClaimProfile` and for higher-stakes authored temporal
claims used beyond the local working context. They are not the default C.27 user
interface, not a data model, and not a universal C.27 dynamic-claim field list
that every user must fill.


C.27 uses physical words only as Plain analogies. Tech prose uses effort,
input, and work references rather than force; resistance/inertia proxies rather
than mass; rate-change readings rather than acceleration as a new kind; and
rhythm bearer/anchor/window rather than `U.Rhythm`.

Each field-definition item either carries a small local C.27 temporal-claim adequacy value or points
back to the existing FPF pattern that governs the referenced object. A field name
is not a pattern.
Metric, process, service, practice, policy, harm, operational-support, and envelope wording
does not create a free C.27 slot. It must resolve to a local C.27 value, an
existing FPF kind and reference, or a governing-pattern relation; otherwise it remains
Plain example language.

| Field/question | Definition | Kind discipline |
| --- | --- | --- |
| claimText / claimRef | The sentence, claim, plan line, benchmark line, or promise-like wording being read. | Anchors C.27 to an authored claim/source; not a free-standing consulting card. |
| target | The temporal reading whose adequacy is in question: rate, cadence, flow, convergence, recovery, narrowing, widening, stabilization, regime, or trajectory. | Local description plus `baseCharacteristicRef` or measurement relation when load-bearing. |
| move | The temporal move: accelerate, decelerate, brake, redirect, coast, pause, stabilize, recover, sustain, widen, narrow, or domain-local. | Prevents acceleration-only bias; braking, pausing, recovery, and coasting can be positive Dyn2 moves. |
| effort, input, policy, method, or intervention | The planned or claimed source of rate-change. It may be work, method change, policy rule, resource input, tool-use change, or control action. | References planning, work, method, policy, or control patterns; it is not stored as a new force object. |
| window | The time interval over which the claim is made, effort is applied, rate is sampled, rhythm is observed, or validity is asserted. | Use a time/window reference appropriate to the pattern; do not collapse all windows into `U.Dynamics.timeBase`. |
| resistance, delay, momentum, or cost | The reason rate-change is not free or immediate: constraint, lag, habit, queue pressure, coordination cost, technical debt, operational-support load, friction, or domain-local resistance proxy. | Domain-local proxy, not literal mass; evidence or assumption should be named when the authored temporal claim is used beyond the local working context. |
| evidence or assumption | The basis that makes the `Dyn2TemporalClaimAdequacyCard` more than a slogan: observed trace, measurement, work evidence, model assumption, planning assumption, or diagnostic judgement. | Cites C.16, work/evidence, causal, benchmark, or assurance patterns when a downstream claim, effect, or use is claimed. |
| basisPosture? | Optional compact basis kind: assumption, observed trace, measured, modelled, diagnostic, planning, benchmark-referenced, causal-use-referenced, promise/assurance-referenced, or unknown. | Bridges a local card to `dynClaimPosture` if the claim later becomes boundary-crossing; it does not strengthen the claim by itself. |
| supported decision or use | The practical use that this `Dyn2TemporalClaimAdequacyCard` can carry: orientation, plan choice, budget, benchmark, gate, replan, publication, or local diagnosis. | Must stay within the evidence basis and `dynClaimPosture`. |
| unsupported downstream claim, effect, or use | A nearby use that this `Dyn2TemporalClaimAdequacyCard` cannot carry, such as `C.28`-governed causal-use claim, release approval, public promise, cross-context transfer, benchmark superiority, or service guarantee. | Prevents laundering a light `Dyn2TemporalClaimAdequacyCard` into a heavier temporal-claim record. |
| reopen, downgrade, or pattern-reference condition | A condition that requires revisiting the `Dyn2TemporalClaimAdequacyCard`, downgrading to Dyn0 or Dyn1, escalating to a profile or formal pattern, or citing another pattern. | This is an evolvability trigger, not a status note. |
| rhythmBearerRef | The entity, practice, work cycle, service, learner, body part, system component, or other named bearer whose rhythm is described. | Must resolve to a named FPF kind and reference or explicitly remain Plain example language; C.27 does not mint a new rhythm kind. |
| rhythmAnchor | The temporal reference for a rhythm claim: beat, cadence, cycle, sprint, epoch, release train, attention window, or domain-local anchor. | It is an anchor for interpretation, not `U.Rhythm`. |
| rhythmWindowRef | The time window across which rhythm is asserted or measured. | Separate from claim, sampling, effort, and validity windows when they differ. |
| instrumentProxyOrEvidenceRef | The measurement or observation proxy used for rhythm, such as tapping task, cadence log, work trace, event sequence, survey, sensor, or domain evidence reference. | Uses C.16 and evidence discipline when load-bearing. |
| couplingMode | How rhythm in one bearer or signal is related to another: synchronization, phase relation, dependency, coordination, entrainment-like practice relation, or domain-local coupling. | Active only when cross-bearer relation is claimed; otherwise ordinary cadence does not need coupling language. |
| validityWindowRef | The period or condition under which the rhythm reading is valid. | Prevents stale rhythm claims from boundary-crossing indefinitely. |

Claim posture discipline: in `Dyn2TemporalClaimProfile`, `dynClaimPosture` is a
pattern-relation declaration, not a maturity scale. A `diagnosticReading` does not mature
into a `causalClaim` by adding fields; `C.28` carries causal-use
claim posture. A `planningModel` does not become `promiseBoundaryUse` by
publication; promise, boundary, commitment, service, or assurance patterns carry
promise-like posture. Changing posture may change the governing relation, pattern,
evidence basis, or assurance-facing relation.
No C.27 field completion upgrades the posture; a higher-stakes posture is a
relation change.


| Field | Definition | Kind discipline |
| --- | --- | --- |
| claimRef | The authored claim, sentence, plan line, benchmark line, or promise-like wording that the profile for boundary-crossing claim use describes. | Mandatory; anchors the profile to authored temporal-claim content. |
| describedEntityRef | The entity, work object, system, practice, service, method, or other governed described entity whose temporal claim is being described. | Reference to the described entity through its named FPF kind and reference; not the `Dyn2TemporalClaimProfile` itself. |
| temporalBearerRef | The object that bears the rate, rhythm, regime, trajectory, or rate-change. It may differ from the described entity in aggregate or proxy cases. | Use only when bearer distinction matters; avoid loose `carrierOrSubject`. |
| profileCarrierRef | The document, card, profile, report, benchmark record, or other authored carrier that contains the Dyn2 claim record. | Carrier of the description, not the dynamic system. |
| dynClaimPosture | The kind and support posture of the dynamic temporal claim: assumption, conjecture, observed trace, diagnostic reading, planning model, control model, calibrated model, causal claim, benchmark claim, assurance claim, or promise-like claim. This is not a maturity sequence: a causal claim is differently governed from a diagnostic reading, and a promise-like claim is differently governed from a benchmark. Changing posture may change the governing relation, pattern, evidence basis, or assurance pattern. | Reading a dynamic temporal claim as carrying a different claim posture is a relation change; use the FPF pattern that governs the target claim, effect, or use. |
| dynOrder | Pattern-local classification: `Dyn0`, `Dyn1`, or `Dyn2`. | Classification of a claim, not a Kernel kind. |
| baseCharacteristicRef | The characteristic whose state/rate/rate-change is being discussed. | Mandatory only when measurement, comparison, or C.16 relation is load-bearing; otherwise the `target` line may carry a local Plain phrase. |
| stateMeasureRef | Measurement reference for a state reading or snapshot. | C.16-compatible when used as evidence or comparison. |
| rateMeasureRef | Measurement reference for rate, tempo, throughput, cadence, flow, trend, or trajectory. | C.16-compatible and separate from state measure when load-bearing. |
| rateChangeReadingMeasureRef | Measurement reference used as evidence for an acceleration, deceleration, braking, redirection, stabilization, hazard-change, queue-pressure-change, or other rate-change reading. | C.16-compatible; this is evidence for a reading, not a new primitive acceleration measure. |
| publishedOrTargetedMeasureRef | The measure being used as reading, dashboard signal, target, gate, incentive, budget input, or public comparison. | C.16 carries measurement legality and comparability; target/proxy use belongs outside C.27 when load-bearing. |
| targetOrIncentiveUse | How the metric is used as a target, incentive, optimization proxy, management signal, or behavior-shaping prompt. | E.13, assurance, or governance patterns carry proxy/utility distortion. |
| dashboardGatePromiseOrBudgetUse | Whether the metric appears in a dashboard, gate, promise, budget, review, or public comparison. | Names boundary/assurance pattern relations when those uses are live. |
| behaviorChangeRisk | How publication, target pressure, incentive, or gate use may change behavior. | C.27 records temporal intervention risk; causal-use claim still needs `C.28` causal-use relation. |
| temporalWorkChangeVsMeasurementChangeNote | Split between real work/process rate change, measurement/probe effect, gaming/selection effect, and causal effect if claimed. | Prevents metric improvement from being read as system improvement. |
| C16RouteRef | Route/reference for admissible measurement construction, comparability, and evidence. | C.27 cites it; C.27 does not define metric legality. |
| E13ProxyAuditRef | Route/reference for proxy-metric distortion, pragmatic utility, or value/proxy divergence. | Keeps metric-as-target work out of C.27 when the dynamic temporal claim is not live. |
| C26RouteRef | Reference for residual probe, frame, order, export, or coarsening cue. | Only present after ordinary C.27, C.16, and E.13 pattern relations leave a residual quantum-like cue. |
| residualQLCue | The cue that a remaining probe, frame, order, export, coarsening, or similar representational condition may change the admissible reading after ordinary FPF patterns have carried their parts. | Plain cue; vocabulary alone does not make QL relevant. |
| residualQLRouteRef | The specific residual QL cue, if any, that still matters to supported use after ordinary temporal, measurement, work, benchmark, value/proxy, scale, adaptation, viability, promise, or evidence pattern relations are named. | C.26 carries the QL discipline; C.27 only records the pattern-reference need. |
| ordinaryRouteBasisRef | Reference or short basis showing which ordinary FPF pattern relation already carries the non-QL relation. | Prevents QL from stealing measurement, work, value, benchmark, scale, adaptation, viability, or promise work. |
| DHCMethodRef | Reference to the declared method for constructing or interpreting the characteristic/measure. | Existing C.16 relation; not a new measurement primitive. |
| scaleVariableRef | The resource or scale variable whose change is claimed to change rate, improvement, learning, recovery, throughput, or stabilization: review capacity, tool-call budget, token budget, sprint count, data volume, model capacity, parallelism, freedom of action, or domain-local scale variable. | Resolves through `C.18.1` or through the named FPF kind and reference that carries the resource or scale variable; not a new force or effort kind. |
| scaleWindowRef | The scale range or window over which the scale-variable claim is asserted. | C.18.1 carries scale-window discipline; G.9 carries parity when compared. |
| scaleElasticityPosture | Qualitative C.18.1 posture for the scale claim: rising, knee, flat, declining, or unknown. | Not a numeric scaling law and not proof that more scale is better. |
| C18_1RouteRef | Route/reference for C.18.1 scaling-law lens adequacy when a scale-variable or elasticity claim is live. | C.27 cites it; C.27 does not define scaling-law discipline. |
| TaskFamilyRef | The declared task family whose time-to-usable-specialization or adaptation speed is being discussed. | C.22.1 carries the task-family adaptation signature; C.27 only states the temporal-claim question. |
| TaskSignature | The declared task signature or specialization signature used by C.22.1. | Not a C.27 kind; used only to prevent generic learning-speed talk. |
| thresholdOrUsableSpecializationRef | The threshold, criterion, or usable-specialization target that makes "adapted faster" inspectable. | Keeps adaptation-speed claims from becoming vague improvement claims. |
| timeToThresholdRef | The time window or time-to-threshold reference for reaching the declared adaptation target. | C.27 may type the temporal-claim question; C.22.1 carries adaptation-signature meaning. |
| budgetToThresholdRef | The effort, resource, exposure, or budget reference needed to reach the declared adaptation target. | Routes budget/exposure detail through C.22.1 and work/resource patterns when load-bearing. |
| C22_1RouteRef | Route/reference for C.22.1 task-family adaptation signature reference. | Mandatory when `dyn2TaskFamilyAdaptationRoute?` is active. |
| viabilityBearerRef | The system, collective system, delivery system, role configuration, organism-as-system, service situation, or declared bearer whose viability is being discussed. | C.26.3 carries viability-envelope discipline; C.27 only names the temporal move when live. |
| protectedPromiseOrFunctionRef | The promise, function, or operating regime that the viability envelope is meant to preserve. | Uses C.26.3 and promise, boundary, or service patterns when load-bearing. |
| C26_3RouteRef | Route/reference for C.26.3 viability-envelope boundary regulation when temporal change is used to preserve viable bounds. | Mandatory when `dyn2ViabilityEnvelopeRoute?` is active; C.27 does not define viability envelopes. |
| timeBase | Time basis of an underlying dynamics model, if a model is live. | Do not use it as a catch-all for every claim/sampling/effort/rhythm window. |
| claimWindowRef | The time window over which the Dyn2 claim is asserted. | Separate from evidence and effort windows when needed. |
| samplingWindowRef | The time window over which state/rate/rate-change evidence is sampled. | Required for noisy derivative-like readings used in claims requiring additional evidence. |
| effortWindowRef | The time window over which planned or actual effort or input is applied. | Applies planning and work patterns. |
| rhythmWindowRef | The window over which rhythm/cadence/phase relation is asserted. | Uses rhythm-bearing note discipline; not `U.Rhythm`. |
| temporalScalePosture | Optional declaration of the time scale that carries the authored temporal claim used beyond the local working context: spot, episode, sprint, lifecycle, learning-cycle, technoevolution, lifetime, or domain-local. | Use only when scale changes the claim's admissible use, bearer, evidence, or reopen condition; it is not a new temporal kind. |
| validityWindowRef | The period or condition over which the `Dyn2TemporalClaimProfile` remains valid. | Carries the refresh/reopen basis. |
| rateChangeIntent | The intended temporal move: accelerate, decelerate, brake, redirect, coast, pause, stabilize, widen, narrow, recover, sustain, or domain-local move. | Avoids acceleration-only bias. |
| interventionRegime | The intervention pattern: impulse, scheduled, feedback, adaptive, exploratory, or policy rule. | Uses planning, control, or policy patterns when formal. |
| controlHorizon | The horizon over which a control-style intervention is evaluated or adjusted. | Only live for `dyn2ControlPolicyRoute?` claims. |
| closedLoopUpdate | The feedback/update rule by which later observations change the intervention. | Uses control or model patterns when reusable or formal. |
| behaviorPolicyRef | The source policy, regime, or practice that produced the evidence being reused. | Only live when policy/regime evidence is used as the basis for another policy or adaptive claim. |
| proposedPolicyRef | The proposed or evaluation policy, regime, rollout, or intervention rule being argued for. | Separate from `behaviorPolicyRef`; otherwise off-policy transfer is hidden. |
| offPolicyRisk | Risk that evidence from one policy/regime does not carry another policy/regime use. | Uses sequential decision or evaluation discipline. |
| stopRule | Condition for stopping, braking, pausing, replanning, or exiting the intervention. | Carries affordability and harm-control basis. |
| controlPolicyRouteRef | The FPF pattern relation used when the claim needs formal dynamics, search/policy health, agentic action, or evaluation basis: `U.Dynamics`, C.19, C.24, or an evaluation pattern. | C.27 records the crossing; the referenced pattern carries the required control or policy discipline. |
| plannedEffortRef | Reference to planned effort in WorkPlan, MethodDescription, resource envelope, or planning pattern. | Ex ante plan, not actual burn. |
| actualEffortTraceRef | Reference to observed work/resource/time burn or trace. | Cites `U.Work` / `Gamma_work`, not `U.Dynamics`. |
| inputCharacteristicRefs | Characteristics treated as inputs to a dynamics or intervention claim. | Existing characteristic/model discipline. |
| effortProfile | Mapping from time window to effort or input posture. | Pattern-local description of effort timing; not a new law. |
| interventionActorRef | The actor, role assignment, tool, system, policy rule, or work arrangement claimed to apply the intervention. | Resolves through A.15, planning, role, method, work, or agentic-action patterns; not a new physical-mechanism kind. |
| interventionAuthorityPosture | Whether the intervention actor/role is authorized, proposed, hypothetical, unknown, assigned, available, or otherwise scoped. | Missing authority or capability bounds admissible use rather than creating proof of executable work. |
| capabilityOrScopeRef | Reference to the scope, capability, assignment, or availability basis for the intervention actor/role. | Requires A.15 or a work pattern for role, method, work-plan, or work-occurrence alignment; C.27 only makes the supported-use limit visible. |
| resistanceOrInertiaProxy | Domain-local reason that changing the rate is hard, delayed, sticky, or costly. | Proxy with `resistanceProxyBasisPosture` and evidence; not literal mass. |
| resistanceProxyFamily | Pattern-local grouping of resistance/inertia proxy: lag, queue, habit, constraint, coordination cost, technical debt, operational-support load, physical inertia, or domain-local family. | Not a `U.Kind`; Plain/Tech mapping must stay explicit. |
| resistanceProxyBasisPosture | Whether a resistance/inertia proxy is qualitative, measured, modelled, assumed, unknown, or otherwise declared. | Prevents unsupported assumptions from being treated as evidence support. |
| evidenceRef | Evidence reference that supplies the basis for a field. | Uses evidence patterns. |
| interventionConstraintRefs | Resource, safety, service, legal, ethical, quality, or domain constraints that bound the intervention. | These constraints are not governed by C.27; C.27 records that they are active. |
| resourceEnvelopeRef | Resource boundary for the intervention. | Planning/resource pattern. |
| safetyEnvelopeRef | Safety boundary for the intervention. | Assurance/safety pattern. |
| serviceEnvelopeRef | Service boundary or operational envelope. | Service/promise/boundary pattern. |
| legalOrEthicalEnvelopeRef | Legal, ethical, or compliance boundary. | Legal/ethics/assurance pattern. |
| qualityEnvelopeRef | Quality boundary affected by acceleration, braking, or rate-change. | Quality pattern such as C.25 where applicable. |
| uncertaintyPosture | Declared uncertainty around model, measurement, evidence basis, stability, or transfer. | May force downgrade or a higher evidence-support relation. |
| dyn2CausalUsePosture | Declared causal-use posture and its details for a Dyn2 temporal claim. | C.27 does not supply a `C.28`-governed causal-use claim by itself; use `dyn2CausalUseRoute?` only when causal use is live. |
| causalInterventionSpecRef | The intervention, effort, workshop, policy, regime, practice change, or other action being treated as causal. | C.27 may name it; `C.28` carries the causal intervention spec, estimand, assumptions, identification, realizability, and evidence design, and supported causal-use judgement. |
| comparatorOrCounterfactualRef | Comparator, contrast case, counterfactual, control group, prior regime, or declared absence of one. | Required when causal reading is live; otherwise the claim remains planning/diagnostic. |
| timeZeroOrAssignmentWindow | The start, assignment, exposure, or intervention window for the causal reading. | Keeps before/after slope claims from hiding timing ambiguity. |
| followUpWindowRef | The outcome observation window after intervention/exposure. | Separate from claim, sampling, effort, rhythm, and validity windows when they differ. |
| outcomeMeasureRef | The measured outcome whose change is being causally read. | Uses C.16 and evidence discipline when load-bearing. |
| estimandRef | The `U.CausalEstimand` being estimated when causal-use basis is claimed. | Defined by `C.28`; C.27 only cites it when a temporal claim is used causally. |
| causalAssumptionSetRef | Assumptions under which the causal/model/evaluation claim holds. | Uses `C.28`; not hidden inside C.27 shorthand. |
| rivalCauseSetRef | Alternative causes that could explain observed rate-change. | Uses `C.28`; required when causal reading is live. |
| causalIdentificationProfileRef | Identification strategy, graph proof, calculus proof, data-regime basis, or bound used for the causal claim. | Delegates to `C.28`; absent identification limits supported causal use. |
| causalUseEvidenceDesignRef | Experiment, quasi-experiment, target-trial emulation, counterfactual sampling, simulation validation, or other causal evidence-design reference. | Uses `C.28`; absent design limits supported causal use. |
| offPolicyCausalEvaluationProfileRef | Off-policy/sequential/adaptive policy evaluation route when rate-change or policy-improvement wording depends on logged behavior or replay. | Uses `C.28`; C.27 does not own off-policy causal evaluation. |
| supportedCausalUse | The causal conclusion or decision use carried by the `C.28` causal-use relation. | Must stay within the declared design, assumptions, outcome evidence, and uncertainty. |
| unsupportedCausalUse | Causal conclusion, action, or assurance claim not carried by the `C.28` causal-use relation. | Prevents C.27 temporal adequacy from laundering into causal-use claim. |
| comparedClaimRefs | Claims, methods, variants, practices, agents, or regimes being compared by dynamic outcome. | `G.9` carries parity; C.27 names the dynamic claim question of the comparison. |
| dynOrderCompared | Whether the comparison is Dyn1 rate or trend comparison, or Dyn2 intervention-sensitive rate-change comparison. | Prevents rate comparison from being laundered into intervention superiority. |
| baselineWindowRef | Baseline or starting window used by the comparison. | Must not be mixed silently across compared claims. |
| adaptationOrInterventionWindowRef | Window in which adaptation, effort, intervention, rollout, training, or practice change occurs. | Optional; required when Dyn2 comparison depends on intervention timing. |
| budgetOrEffortParityRef | Budget, effort, resource, or work-parity reference needed for fair dynamic comparison. | Uses `G.9`, work, and resource patterns when load-bearing. |
| rateOrRateChangeReadingMeasureRef | Measurement reference used as evidence for compared rate, recovery, rhythm, throughput, or rate-change reading. | Uses C.16 measurement discipline. |
| G9ParityPlanRef | `G.9` parity plan reference for baseline, freshness, comparator, bridge, and evidence pins. | Mandatory when benchmark parity is load-bearing. |
| G9ParityReportRef | Optional `G.9` parity report reference carrying outcomes/evidence. | Needed for published or benchmark used beyond the local working context result. |
| evidenceBranches | Decomposition of evidence by state, rate, rate-change, effort, resistance, rhythm, or causal effect. | Shows which branches are evidence and which remain assumptions. |
| stateEvidenceRefs | Evidence for state reading or snapshot. | Evidence relation or C.16 relation. |
| rateEvidenceRefs | Evidence for rate, trend, or trajectory reading. | Evidence relation or C.16 relation. |
| rateChangeEvidenceRefs | Evidence for rate-change/intervention-sensitive reading. | Evidence/C.16 relation. |
| effortEvidenceRefs | Evidence for planned or actual effort. | Planning/work relation. |
| resistanceEvidenceRefs | Evidence for resistance/inertia proxy. | Domain evidence relation. |
| rhythmEvidenceRefs | Evidence for rhythm/cadence/coupling. | Rhythm proxy/evidence relation. |
| causalEvidenceRefs | Evidence for causal attribution. | `C.28` causal-use relation. |
| dyn2CrossScaleTransferBlock | Declared relation when a Dyn2 temporal claim moves across levels, bearers, or aggregation. | Unsupported unless aggregation basis, bearer continuity, and mix-shift risk are addressed. |
| sourceBearerRef | Bearer where evidence or claim originates. | Existing object reference. |
| targetBearerRef | Target bearer for boundary-crossing use. | Existing object reference. |
| aggregationRoute | Rule or evidence path by which local/aggregate readings are related. | Uses aggregation, model, or evidence pattern. |
| mixShiftRisk | Risk that composition changes explain the apparent rate-change. | Must be named before cross-scale transfer. |
| dynamicTransferPosture | Whether cross-scale transfer is carried by declared bearer continuity and aggregation basis, remains unsupported, or is unknown. | Prevents aggregate acceleration laundering. |
| accelerationDebt | Consequence or residue created by sustained acceleration, braking, recovery, stabilization, or redirection: rework, operational-support load, quality loss, burnout, risk, hidden queue, or coordination cost. | Use only when admissible use relies on sustained acceleration/braking/recovery/stabilization or when the domain can retain residue after effort changes or stops. |
| debtKind | Kind of debt or residue. | Domain-local, with evidence if load-bearing. |
| debtWindowRef | Window over which debt appears or must be repaid. | Separate from effort and claim windows when needed. |
| reversibilityPosture | Whether the dynamic change is reversible, costly to reverse, irreversible within window, or unknown. | `unknown` is allowed; it bounds supported use instead of forcing theory-building. |
| reversibilityNote | Short explanation of why reversibility has that posture. | Captures hysteresis and residue only when load-bearing. |
| hysteresisOrResidue | What remains after effort changes or stops. | Domain-local description requiring evidence when load-bearing. |
| repaymentOrBrakePlan | Plan to repay debt, brake, recover, or stabilize. | Planning/assurance pattern if load-bearing. |
| debtHysteresisRouteRef | Route/reference for planning, assurance, quality, wellbeing, or safety relation when debt/hysteresis is load-bearing. | C.27 records the temporal-claim question; referenced patterns carry the required discipline. |

| brakeOrRecoveryPlan | Plan for braking, recovery, stabilization, or rollback. | Planning/assurance pattern when load-bearing. |
| supportedUse | The uses this C.27 temporal-claim record can carry. | Must match `dynClaimPosture` and evidence. |
| unsupportedUse | Nearby uses this note/profile does not support. | Prevents hidden escalation. |
| reopenTrigger | Condition that requires refresh, downgrade, a higher evidence-support relation, or reference to another pattern. | Evolvability trigger for the claim. |

C.27 has a small core. Specialized cases are C.27 dynamic-claim relations
or optional profile blocks for authored temporal claims used beyond the local working context; they are not mandatory rules
for every C.27 use.

These entries are not a general relation list. They apply only after an
authored temporal claim already has C.27 relevance because it changes admissible use.
Each entry names the neighbouring FPF pattern to inspect when that C.27-typed
dynamic claim also depends on one non-C.27 question. If the text has no state,
rate, rate-change, rhythm, regime, recovery, stabilization, transfer, or
intervention relation that changes admissible use, no entry here applies.

| Dynamic-claim relation | C.27 relation and next FPF pattern |
| --- | --- |
| Formal dynamics | Reusable law, simulation, prediction, control, or calibrated dynamics is carried by `A.3.3 U.Dynamics`, `C.16`, work evidence, `G.9`, and assurance patterns. |
| C.16 rate measurement relation | Rate and rate-change readings used as evidence, benchmark, gate, control, or C.27 profile use include `c16RateMeasurementRouteRef?`; C.27 cites `C16RouteRef` and does not define measurement legality. |
| C.27 effort/work block | `dyn2EffortWorkBlock?` separates planned effort, method description, resource envelope, actual `U.Work` trace or `Gamma_work` aggregation trace, effort window, intervention actor/role assignment, and authority/capability posture; A.15 and work patterns carry role, method, work-plan, and work-occurrence alignment. |
| C.27 resistance/inertia block | `dyn2ResistanceInertiaBlock?` names resistance proxy family, resistance proxy basis posture, evidence, and unsupported downstream claim, effect, or use; `resistanceProxyBasisPosture = unknown` may carry local diagnostic use but blocks durable acceleration, causal, benchmark, promise-like, or assurance use. |
| C.27 rhythm claim block | `dyn2RhythmClaimBlock?` names bearer, anchor, window, proxy/evidence, and admissible use; coupling, phase, synchronization, or entrainment-like details appear only when the supported use depends on a relation between bearers. |
| C.27 causal-use relation | `dyn2CausalUseRoute?` is present only when a rate-change/intervention claim is used as a causal-use basis; it requires `causalInterventionSpecRef`, contrast/counterfactual, timing, outcome, assumptions, rival causes, supported causal use, unsupported causal use, and `C.28` causal-use relation. |
| C.27 dynamic benchmark requirement | `dyn2BenchmarkParityBlock?` declares the rate/rate-change/rhythm/recovery/intervention-effect requirement of a comparison; it is a benchmark input declaration, not a benchmark harness. `G.9` carries baseline, freshness, comparator, bridge, parity plan, and parity report discipline. |
| C.27 metric-as-target block | `dyn2MetricTargetEffectBlock?` splits metric-as-measure, metric-as-target or incentive, metric publication as temporal intervention, and residual probe, frame, or export cue; C.16 carries measurement, E.13 or an assurance pattern carries proxy distortion, and C.26 applies only after ordinary FPF pattern relations leave residual QL cue. |
| C.27 cross-scale transfer field | `dyn2CrossScaleTransferBlock?` keeps local and aggregate dynamic readings separate; cross-scale use needs source bearer, target bearer, aggregation basis, bearer continuity, mix-shift risk, and explicit `dynamicTransferPosture`. |
| Object-centric dynamic trace | Workflow/process rate claims need bearer, object/event trace, interaction, and convergence/divergence discipline rather than one generic process-speed label. |
| Method composition or emergent work cycle | If the live claim is about how method parts compose, how an adaptive work cycle becomes a capability, or how repeated practice changes shape, C.27 handles only the temporal adequacy of the rate, rhythm, recovery, stabilization, or rate-change claim. `B.1.5` carries order-sensitive method composition and work enactment; `B.2.4` carries meta-functional transition and capability-emergence questions. |
| State-change or evolution loop and language-state movement | If the live claim is that a system, episteme, method, cue, branch, or language-state relation evolved, reopened, stabilized, operationalized, retired, or moved through a named state-change sequence, C.27 handles only the temporal adequacy of any speed/rhythm/recovery/stabilization claim. `A.4` / `B.4` carry temporal duality and canonical evolution loops; `A.16` / `B.4.1` carry language-state move and cue-stabilization discipline. |
| C.27 scale-variable claim block | `dyn2ScaleVariableClaimBlock?` is present only when changing review capacity, tool calls, tokens, sprints, data, model capacity, parallelism, freedom of action, or another declared scale variable is used as the basis for a rate-change, learning, recovery, throughput, or stabilization claim; C.18.1 carries scale variables, scale windows, scale probes, and elasticity posture. |
| Autonomy-budget or freedom-of-action claim | If freedom of action, action tokens, decision tokens, guard cadence, depletion, pause/resume, or autonomy-gated work is used as the basis for a rate-change or stabilization claim, C.27 states the temporal claim only. `E.16` carries autonomy budgets, guard checks, ledger evidence, depletion behavior, and override speech acts. |
| C.27 viability-envelope relation | `dyn2ViabilityEnvelopeRoute?` is present only when braking, throttling, rollout speed, cadence change, recovery timing, adaptation cost, or stabilization is used to keep a declared viability bearer inside usable bounds; C.26.3 carries viability-envelope boundary regulation. |
| Publication-unit stability around temporal wording | When a paragraph, note, working section, comparison, explanation, or decision-facing text mixes method-description, repeated-practice, service-boundary, rhythm, capability-claim, improvement, benchmark, and promise wording so that the primary described entity or active claim question is unstable, use E.17.AUD, E.17.ID.CR, or the relevant publication-unit pattern first. C.27 is active only when a temporal-claim adequacy question remains after that stabilization. |
| C.27 control/policy relation | `dyn2ControlPolicyRoute?` is present only for `controlModel`, `policyRule`, `adaptive`, feedback-bearing `planningModel`, or explicit C.24/C.19/evaluation relations; C.27 records the crossing and names the pattern that carries formal control/MPC/RL/policy evaluation. |
| Dynamic policy transfer | Pattern-reference-only inside `dyn2ControlPolicyRoute?`: sequential decision/evaluation discipline carries behavior-policy/evaluation-policy and off-policy transfer claims rather than default C.27 fields. |
| Explore/exploit | C.19 carries policy health for search, convergence, narrowing, widening, and switching-rate claims. |
| Creative or open-ended search speed | Claims about faster novelty, illumination, archive growth, frontier coverage, candidate generation, or candidate-set improvement use C.17 for novelty/value measures, C.18 for open-ended search calculus, and C.19 for pool policy; C.27 only names the temporal adequacy question when speed or change affects admissible use. |
| Task-family adaptation speed | If the claim concerns acquiring usable specialization on one declared `TaskFamilyRef` or `TaskSignature`, C.27 types the learning/adaptation-rate question and C.22.1 carries threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, and corridor-entry evidence. |
| C.27 debt/hysteresis block | `dyn2DebtHysteresisBlock?` is present only when admissible use depends on sustained acceleration, braking, recovery, stabilization, residue after effort changes, or high-stakes/promise/gate use; `unknown` reversibility is allowed but bounds supported use. |
| Promise / boundary / service acceptance | `A.2.3`, `A.2.8`, `A.2.9`, `A.6.C`, `F.12`, and assurance patterns carry service promises, SLA-like statements, agreement-language expectations, release gates, public commitments, boundary obligations, and service-acceptance bindings. |
| Evidence/provenance path | If a C.27 card/profile cites traces, assumptions, work evidence, evidence carriers, `PathId`, `PathSlice`, validity window, or evidence decay, C.27 states the temporal reading that needs an evidence basis. `A.10` / `G.6` carry evidence graph referring, provenance anchors, citable path/slice discipline, and SCR/RSCR-visible evidence bindings; `B.3` / `B.3.4` carry assurance posture and evidence decay / epistemic debt. |
| Dashboard telemetry, pack shipping, or refresh use | If a dashboard, time-series, telemetry pin, RSCR trigger, shipped pack, discipline-health slot, or dashboard slice is used as evidence for improvement, decay, recovery, stabilization, or rate-change, C.27 names the temporal-claim adequacy question. `C.21` carries discipline-health slot meaning; `G.12` carries DHC series/row/slice and telemetry-pin publication; `G.10` carries pack shipping; `G.11` carries refresh/decay orchestration; `G.6` carries path/slice evidence visibility. |
| Transduction gate or flow use | If a C.27-typed temporal claim is used as a `GateCheckRef` input, `GateDecisionRationale`, `LaunchGate` condition, `PathSlice` refresh trigger, crossing condition, or published flow condition, C.27 states only the temporal-claim adequacy question. `E.18` / `A.20` / `A.21` carry the transduction graph, `OperationalGate(profile)`, `ConstraintValidity`, `GateFit`, `DecisionLog`, `PathSlice`, `SquareLaw`, `Gamma_time`, and crossing pins. |
| Derivative noise | Noisy rate-change readings used for comparison, benchmark, gate, or control need sampling-window and stability posture, or downgrade. |
| Coasting | Coasting needs a basis when continued movement or stability after effort changes or stops carries the claim. |
| High-stakes temporal move | Pattern-reference-only relation: high-stakes acceleration, braking, or redirection claims name the temporal move, window, and unsupported use and cite the harm, resource, quality envelope, assurance, ethics, legal, safety, financial, or human-wellbeing pattern that governs the other question. |
| C.26 residual relation | C.27 does not add QL relation. If a Dyn2 claim also depends on probe, frame, order, export, or coarsening residue that ordinary FPF patterns cannot carry, C.26 carries the residue after ordinary C.27, C.24, C.16, G.9, and E.13 pattern relations are named. |
| No new publication object | `Dyn2TemporalClaimAdequacyCard` and `Dyn2TemporalClaimProfile` are pattern-local records/cards, not new Part G publication roles, MVPK faces, governed objects of related FPF patterns, or Kernel types. |
| Use-triggered lint | Useful lint requires temporal-improvement wording plus decision, comparison, budget, benchmark, gate, promise, publication, assurance, or intervention-plan use. |

Plain words may remain didactic. Tech prose must name the FPF pattern that carries the load-bearing question.
Problem frames, Forces, and worked examples may use speed, force, inertia,
acceleration, rhythm, cadence, agility, or process-speed language when it helps
recognition. Field definitions, conformance requirements, and governing-pattern
relations should use the Tech readings below.
Minted C.27-local labels must carry the dynamic claim question in the label: use
`Dyn2`, `Temporal`, `RateChange`, `Rhythm`, `Inertia`,
`CrossScale`, `MetricTarget`, `ControlPolicy`, or another explicit dynamic
qualifier. A generic head such as `Profile`, `Card`, `Process`, `Service`,
`Practice`, `Policy`, `Harm`, `OperationalSupport`, or `Envelope` is not enough by itself.
Ordinary prose may use those words only as Plain examples or after resolving the
actual FPF kind and reference or governing pattern.

| Plain wording | FPF-safe Tech reading |
| --- | --- |
| speed | rate, throughput, tempo, or trajectory reading with C.16 basis when load-bearing |
| acceleration | rate-change, regime transition, policy effect, or finite-difference reading |
| effort / force | planned effort, input characteristic, intervention actor/role assignment, actual work/resource trace, or resource envelope |
| mass / inertia | domain-local resistance or inertia proxy: lag, switching cost, coordination cost, queue pressure, habit persistence, physical inertia, or constraint |
| rhythm / cadence | interval-structured bearer/anchor/window/evidence relation; coupling only for cross-bearer claims |
| agility | braking, redirection, acceleration, stabilization, recovery, and constraint handling |
| process sped up | first resolve the bearer as system, work, method description, service promise/boundary, or event-log view; then add the C.27 temporal-claim question only if rate-change use is live |
| more calls / more context | agentic action whose target rate must be named, not automatic acceleration |

Avoid as Tech tokens unless already governed by the named pattern:
`carrierOrSubject`, `D2DynamicsProfile`, `Metric`, `Axis`, `Dimension`,
`Process`, `Practice`, `Service`, generic card names, `Profile`, `ProcessBearer`,
`PolicyEvaluation`, `HarmEnvelope`, `force`, `mass`, `acceleration`, and
`rhythm`.

Prefer: `DynOrder`, `Dyn2TemporalClaimAdequacyCard`, `Dyn2TemporalClaimProfile`,
`describedEntityRef`, `temporalBearerRef`, `profileCarrierRef`,
`baseCharacteristicRef`, `MeasureRef`, `DHCMethodRef`, `claimWindowRef`,
`samplingWindowRef`, `effortWindowRef`, `rhythmWindowRef`,
`plannedEffortRef`, `actualEffortTraceRef`, `inputCharacteristicRefs`,
`interventionActorRef`, `interventionAuthorityPosture`, `capabilityOrScopeRef`,
`resistanceOrInertiaProxy`, `resistanceProxyBasisPosture`,
`dyn2MetricTargetEffectBlock?`, `dyn2ObjectCentricTraceBlock?`,
`dyn2CrossScaleTransferBlock?`, `dyn2HighStakesTemporalMoveRoute?`,
`supportedUse`, `unsupportedUse`, and `reopenTrigger`.

The dynamic-order labels are values of a claim classification, not kinds of
things. Dyn0, Dyn1, and Dyn2 classify what a temporal claim treats as sufficient
for its use. They do not become `U.Dyn0`, `U.Dyn1`, `U.Dyn2`,
`U.Acceleration`, `U.Rhythm`, `U.Practice`, `U.Force`, or
`U.SecondOrderProcess`.

Kind-locality rule: `DynOrder`, `Dyn0`, `Dyn1`, `Dyn2`,
`Dyn2TemporalClaimAdequacyCard`, and `Dyn2TemporalClaimProfile` name readings
or records of authored temporal claims. They do not classify the governed object
itself unless an existing FPF pattern separately types that object. "Team
throughput accelerated" may receive a Dyn2 claim reading; the team does not
become a `Dyn2System`, throughput does not become `U.Acceleration`, and the
card/profile does not become a dynamics law.

`Dyn2TemporalClaimProfile` is a pattern-local episteme record about the adequacy of
a temporal claim. It is not `U.Dynamics`, `U.Work`, `U.WorkPlan`,
`U.MethodDescription`, `U.Measure`, or `CharacteristicSpace`. If materialized
as a document, card, table, or file, that material is a carrier of the `Dyn2TemporalClaimProfile`
content, not the actual work, process, law, practice, or system being discussed.

A.7 object/description/carrier split: `Dyn2TemporalClaimAdequacyCard` and
`Dyn2TemporalClaimProfile` are authored descriptions of temporal-claim adequacy.
They are not the dynamic system, not the work trace, not the measure, not the
service promise, not the intervention actor/role, not the dynamics law, and not identical to the
document/card/page that carries them.

The object split is:

| Object | Meaning |
| --- | --- |
| `describedEntityRef` | the entity/work/method/system/practice-like object the claim discusses, resolved through existing FPF kinds where load-bearing |
| `temporalBearerRef` | the object whose state, rate, rhythm, or regime is being read |
| `profileCarrierRef` | optional card/file/page carrier of the `Dyn2TemporalClaimProfile` content, only when publication/evidence needs it |
| `plannedEffortRef` | plan/method/resource-envelope basis for intended effort |
| `actualEffortTraceRef` | `U.Work` or `Gamma_work` basis for actual burn |
| `dynamicsModelRef` | `U.Dynamics` basis when a law/model of change is claimed |

Loose words require resolution in Tech prose. A process may be a method recipe,
dated work run, transition law, event-log view, or service situation. A practice
may be method description plus work traces. A service claim may involve system,
promise content, delivery work, boundary semantics, or assurance. C.27 should
not use these as untyped substitutes for named FPF kinds/references.


**Copy-paste authoring forms (informative).** These forms make C.27 cheap enough
to use without jumping straight to a full profile.

Dyn0 or Dyn1 exit:

```text
C.27 exit: this is a Dyn1 rate reading only.
No intervention-sensitive temporal claim is used here.
Measurement relation: <C16RouteRef or N/A>.
```

Local Dyn2 card:

```text
C.27 card:
claim:
target:
move:
intervention:
window:
resistance/cost:
basis:
supportedUse:
unsupportedUse/reopen:
```

Boundary-crossing profile header:

```text
C.27 profile header:
claimRef:
describedEntityRef:
temporalBearerRef?:
dynClaimPosture:
dynOrder:
claimWindowRef:
supportedUse:
unsupportedUse:
reopenTrigger:
activeBlocks:
```

**AI-assisted drafting posture (informative).** An AI-assisted draft may propose
that C.27 is relevant, but a profile appears only after the admissible use and the
boundary-crossing reason are named. First classify the prose as ordinary prose,
Dyn0, Dyn1, Dyn2 card, or profile/pattern relation. The draft does not infer:
more tool calls means better reasoning; faster narrowing means better search;
higher throughput means better quality; metric improvement means system
improvement; or trend means intervention model.

