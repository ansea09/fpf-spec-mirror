---
chunk_kind: "child"
pattern_id: "C.27"
pattern_title: "Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Change"
section_id: "C.27:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27/C.27__002_use-this-when.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.27 — Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Change"
  - "C.27:0 — Use This When"
line_start: 70019
line_end: 70055
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

### C.27:0 - Use This When

Use this pattern when a claim about speed, rhythm, throughput, recovery, convergence, rollout, adoption, braking, coasting, redirection, or stabilization is being used to change action.

The practical question is:

> Are we only reading a state, only reading a rate, or claiming that an intervention changes a rate, rhythm, recovery, or regime?

If the claim is only a state or rate reading and that answers the receiving question, stop. For an intervention-sensitive claim, recover the proposed input, relevant time, resistance or cost, and grounds for the predicted change. Return the supported use and any material limitation; add a reopening condition when later reliance needs it.

**What this buys.** The practitioner distinguishes a trend from an intervention model. Braking, pausing, stabilizing, redirecting, coasting, widening, narrowing, or slowing rollout remain available when acceleration would be the wrong move.

**Primary working object.** The temporal claim whose adequacy matters to the receiving action. Recover its content and subject from the available plan, report, model, observation or other account. An exact C.2.1 episteme or `ClaimAddress` is needed when the receiving use relies on that independently referable identity. Here `ClaimAddress` means exact edition plus intrinsic claim identity declared by that edition's ClaimGraph.

When an adequacy assertion is independently identified under C.2.1, its EntityOfConcern is the source episteme or addressed claim, not the reference used to designate it. An ordinary assessment can state its conclusion directly. Publication under E.24.PUB is separate from that claim and identity.

**First useful move.** Recover what is claimed to change over time, for which subject and conditions. Use `C.27.TA` when its temporal meaning needs clarification, then classify the claim:

| Reading | What the claim treats as sufficient | Normal result |
| --- | --- | --- |
| Dyn0 | a state or snapshot | ordinary prose; C.16 only when measurement construction matters |
| Dyn1 | a rate, trend, trajectory, flow, throughput, tempo, or cadence | ordinary prose or a C.16 result |
| Dyn2 | effort, input, policy, timing, resistance, feedback, or constraint is claimed to change a rate, rhythm, recovery, or regime | one small C.27 account, in ordinary prose or the card below |

Dyn0, Dyn1, and Dyn2 classify authored claims. They do not classify Systems, teams, services, Methods, or practices as kinds of things.

**Not this pattern when.**

- The temporal wording is ordinary explanation and changes no practical use.
- The result needed is only a positive temporal-aspect claim. Use C.27.TA.
- The question is measurement construction or comparability. Use C.16.
- The question is a transition law, simulation, prediction, or control model. Use A.3.3.
- The question is a bounded transformation. Use A.3.4.
- The question is planned or performed Work. Use A.15.2, A.15.1, and F.6 as applicable.
- The question is causal use, benchmark parity, a promise, assurance, value, harm, viability, scaling, adaptation, search health, publication, or residual QL. Use the direct pattern for that question; keep C.27 only if a separate temporal-claim adequacy question remains.
- The reader has only a cue such as braking difficulty, rhythm mismatch, demand accumulation, divergent event traces, or more activity without better results. Keep the cue through A.16, A.16.1, B.4.1, or B.5.2.0 until a temporal claim can be stated.

