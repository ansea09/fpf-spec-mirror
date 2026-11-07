---
chunk_kind: "child"
pattern_id: "C.27"
pattern_title: "Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Change"
section_id: "C.27:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27/C.27__005_solution.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "C.27 — Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Change"
  - "C.27:3 — Solution"
line_start: 67034
line_end: 67121
dependencies:
  - "A.10"
  - "A.3.3"
  - "A.3.4"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.18.1"
  - "C.19"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.26"
  - "C.26.3"
  - "C.27.TA"
  - "G.9"
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

### C.27:3 - Solution

Use the least-committing result that changes the receiving action.

1. Recover the temporal claim from the available account, keeping its subject, quantity or condition and relevant time explicit. Cite an exact episteme or ClaimAddress when that identity is consumed by the use.
2. Resolve what the timing means: a dated observation, elapsed duration, order, recurring cadence, validity condition or another temporal property. Use `C.27.TA` if this is unclear; a separate temporal-aspect artifact is unnecessary when the claim already states it adequately.
3. Classify the claim as Dyn0, Dyn1 or Dyn2.
4. If it is Dyn0 or Dyn1 and no intervention-sensitive question remains, stop or use C.16 for the unresolved measurement question.
5. For Dyn2, connect the proposed input to the claimed temporal effect. Recover the baseline, relevant window and resistance or cost; identify whether the basis is observation, a planning assumption, a model consequence or a causal result. Reuse adequate grounds. When the effect is the unresolved causal question, use C.28 and its construction or mechanism-replacement method as needed.
6. Return the supported conclusion and only the neighboring result on which it depends. Unknown resistance or another missing premise can justify a narrower or unresolved result.
7. Add more detail only when it can resolve a remaining receiving question; an incomplete form is not itself a reason to open a larger profile.

#### C.27:3.1 - A Sufficient Dyn2 Account

A compact account states the input, proposed temporal change, relevant window, resistance or cost and grounds. Its length follows the explanation needed by the receiving use.

For example: "Adding two reviewers is expected to increase completed reviews during the next two weeks. That forecast assumes sufficient independent review capacity; the shared approval bottleneck remains unmeasured, so doubling throughput is not yet supported."

The optional record below is useful when separately identified claims must be referenced or reviewed:

~~~text
Dyn2TemporalClaimAdequacyCardClaimContent
sourceTemporalClaimRef:
positiveTemporalAspectClaimRef:
move:
claimedInterventionOrInput:
interventionWindow?:
resistanceOrCost:
reasonForReading:
supportedUse:
unsupportedUse?:
reopenTrigger?:
~~~

When an independently identified C.27 adequacy episteme uses this record, its EntityOfConcern is the source episteme or addressed claim denoted by `sourceTemporalClaimRef`.

- `positiveTemporalAspectClaimRef` identifies the temporal claim used by that reference-bearing account. Ordinary prose may instead state the temporal aspect directly, keeping its meaning under C.27.TA.
- move names the claimed temporal change, for example accelerate, brake, coast, recover, stabilize, widen, narrow, or a domain-local move.
- claimedInterventionOrInput says what is claimed to affect the temporal behavior. It does not assert performed Work, authority, capability, or causal effect.
- interventionWindow is omitted when the C.27.TA window is enough. Add it only when the input occurs over a different interval.
- resistanceOrCost names the relevant lag, constraint, stored work, queue pressure, coordination cost, residue, or another domain-local obstacle. Unknown is an acceptable local answer.
- reasonForReading names one exact evidence relation, measurement result, model assumption, planning assumption, diagnostic judgement, or direct neighboring result. These alternatives do not become one generic evidence kind.
- supportedUse states the result's practical reach; unsupportedUse names a live overreach only when it needs to be excluded explicitly.
- reopenTrigger is included when continued reliance needs a condition for revision, new evidence or another direct result.

One local window may stand for claim, sampling, intervention, rhythm, and validity when the difference changes neither the claim nor the receiving action. Split them when, for example, evidence is sampled over a different interval, input precedes the observed outcome, comparison needs a baseline, follow-up occurs later, or validity expires sooner than the trace.

Unknown resistance can support a local diagnosis or planning discussion. It cannot support durable acceleration, causal, benchmark, promise-like, gate, or assurance use without the direct evidence or assumption boundary required for that use.

#### C.27:3.2 - Readable Actor and Intervention Boundary

Ordinary practitioner prose may say, for example, “the engineer slowed the rollout” when it recognizably names the System acting in the situation.

If the receiving claim relies on performed Work, identify the actual System actor, recover its A.13 core, and independently admit the dated Work under A.15.1. Add F.6 afterward only when the temporal claim also needs precise assignment-bound attribution. If the claim relies on a local system-role kind, System classification, or assignment, add each distinction separately. An assignment does not act and does not supply authority; cite its directly declared relation species and exact obtaining occurrence while still naming the holder System.

For a non-system input, name its actual direct relation to the temporal behavior, or keep it as an unresolved or source-side intervention claim. Keep authority, WorkPlan, capability, performed Work, and claimed effect separate.

#### C.27:3.3 - Rhythm, Coasting, and Reversibility

Observed cadence can remain Dyn1. A rhythm claim becomes Dyn2 only when effort pattern, coordination, recovery, stabilization, or another intervention-sensitive use changes the supported action.

For coasting, ask what continues after effort changes or stops, why it may continue, over which window, what use that reading supports, and what change reopens it. Possible bases include habit, automation, stored work, queue pressure, learned capability, commitment momentum, social norm, physical inertia, or unknown; these are examples, not proof.

Keep coasting and debt distinct. Coasting describes continued movement or stability. Debt or hysteresis describes what remains and how costly reversal or recovery is. A claim may need both. Rework, service demand, quality loss, burnout, hidden queues, risk, or coordination cost can appear after acceleration. Reversibility may be unknown; that bounds use instead of forcing a theory.

#### C.27:3.4 - Boundary-Crossing Header

An adequate compact account can finish the work. When the receiving use depends on another pattern's result, include its contribution and an exact reference where that identity is required. This optional header can organize separately referable results:

~~~text
Dyn2TemporalClaimProfileClaimContent

sourceTemporalClaimRef:
positiveTemporalAspectClaimRef:
dynOrder: Dyn2
boundaryCrossingUse:
supportedUse:
unsupportedUse?:
validityOrReopenCondition?:
activeNeighborResults:
  - exact result kind and reference supplied by its direct pattern
    contributionToThisUse:
~~~

When the profile is used to identify an adequacy episteme, its EntityOfConcern is the source episteme or addressed claim denoted by `sourceTemporalClaimRef`. The profile's references preserve the direct results it consumes; they are not substituted for those results.

Each activeNeighborResults entry names the actual result kind supplied by its direct pattern. Do not replace a C.16 measurement result, C.28 causal-use result, G.9 parity result, C.26.3 envelope-regulation claim, Work occurrence, evidence relation, or assurance claim with a generic C.27 field.

