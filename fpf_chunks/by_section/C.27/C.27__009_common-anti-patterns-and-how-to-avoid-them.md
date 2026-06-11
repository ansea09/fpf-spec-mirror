---
chunk_kind: "child"
pattern_id: "C.27"
pattern_title: "Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change"
section_id: "C.27:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27/C.27__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "C.27 — Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change"
  - "C.27:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 49079
line_end: 49126
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

### C.27:8 - Common Anti-Patterns and How to Avoid Them

C.27 starts with the anti-patterns most likely to make a working reader misuse a
state/rate reading as a Dyn2 temporal claim. Less frequent traps belong in the
extended bank and should not become a first-screen checklist.

| Core anti-pattern | What it looks like | Repair |
| --- | --- | --- |
| Rate -> intervention laundering | "We measured throughput, therefore we know how to accelerate it." | Ask whether the claim is Dyn0 state, Dyn1 rate, or Dyn2 rate-change under effort/resistance/window; add only the least-committing C.27 record that changes admissible use. |
| Effort-free acceleration | "Velocity will double" with no effort, input, intervention actor/role, resistance proxy, window, evidence, or supported use. | Add a `Dyn2TemporalClaimAdequacyCard` or downgrade to Dyn1 measurement. |
| Past slope as control model | A historical trend is treated as a future intervention law. | Separate observed Dyn1 trend from Dyn2 intervention claim and formal-model relation. |
| C.27 as `C.28`-governed causal-use claim | Rate changed after effort, therefore effort caused it. | Keep it as a planning assumption or diagnostic reading, or include `dyn2CausalUseRoute?` with `causalInterventionSpecRef`, contrast/counterfactual, timing, outcome, assumptions, rival causes, supported causal use and unsupported causal use, and `C.28` causal-use relation. |
| Rhythm as decoration | Rhythm names vibe/cadence with no bearer, timing reference, window, proxy, evidence, or supported use. | Name bearer, timing reference, window, instrument/evidence proxy, and supported use; add coupling/phase/entrainment only when the claim depends on a cross-bearer relation. |
| Metric-accelerated theater | The measured rate improves after becoming a target while hidden work worsens. | Separate real work-rate change, measurement/probe effect, gaming risk, and temporal intervention effect. |
| Aggregate acceleration laundering | Local speed or aggregate speed is laundered across levels. | Separate local bearer, aggregate bearer, mix shift, aggregation relation, and `crossScaleTransferUseBoundary`. |
| Acceleration bias | Faster is treated as better by default. | Make braking, pause, stabilization, redirection, coasting, and slower rollout legitimate outcomes. |

Use the negative cases to make non-use easy. They are not profile triggers.

| Negative case | Correct C.27 outcome |
| --- | --- |
| "This section accelerates orientation." | No C.27 record unless the `PublicationUnit` carries that acceleration claim as the basis for a decision, promise, intervention, or comparison. |
| "The chart shows throughput rising." | Dyn1; C.16 only if the measurement construction is FPF-governed. No C.27 record unless a rate-change intervention claim appears. |
| "The team has a strong rhythm." | No C.27 record unless rhythm carries a decision-use; then name bearer, timing reference, window, evidence proxy, and admissible use. |
| "We use a dashboard of velocity." | C.16/E.13/C.26.1 when the issue under repair is measurement, proxy distortion, or probe/publication effect; C.27 only when the dashboard is claimed to change a temporal outcome. |
| "The model is dynamic." | `U.Dynamics` when a state-space or transition law is being described; no C.27 record unless authored prose makes a rate-change adequacy claim. |
| "The agent used more calls." | C.24/work-trace relation; C.27 only when more calls are claimed to change debugging, search, learning, recovery, or stabilization rate. |
| "The process is agile." | A.6.P/local-head restoration first when "agile" is overloaded; C.27 only when braking, redirection, or rate-change question is live. |

Use the extended anti-patterns only when the live temporal claim actually raises
that trap.

| Extended anti-pattern | What it looks like | Repair |
| --- | --- | --- |
| Keyword-triggered bureaucracy | Any speed, rhythm, agility, throughput, velocity, accelerate, or slow-down word forces a profile. | Use supported-use relevance, not keyword matching. |
| Derivative label without template | Acceleration, velocity, momentum, or cadence number lacks base characteristic, unit, scale, sampling window, method, and evidence. | Use C.16 measurement construction. |
| Rhythm bearer mismatch | Evidence from one bearer/window is applied to another. | Add bridge/evidence relation or mark transfer unsupported. |
| Effort window hidden in plan prose | Plan says "push harder" without WorkPlan, method, resource envelope, or actual burn evidence relation. | Attach planned effort to planning patterns and actual burn to work patterns. |
| Dynamics law as work log | Work trace or telemetry is treated as the law of change. | Keep `U.Dynamics` separate from `U.Work` evidence. |
| Agility as cornering speed | "Change direction fast" hides braking and redirection cost. | Name braking, redirection cost, intervention constraints, evidence, and admissible use. |
| Premature convergence by acceleration | Faster narrowing collapses diversity, novelty, or frontier coverage. | Use C.17, C.18, and C.19 as applicable and distinguish exploitation speed from healthy search. |
| Dyn2 profile as hidden promise | A planning note becomes a service guarantee, SLA-like statement, or public commitment. | Separate planning basis from promise content and boundary obligation. |
| Noisy acceleration worship | Small variation is overread as meaningful rate-change. | Widen sampling, add uncertainty, downgrade, or collect higher-quality or more directly relevant evidence. |
| Tool-call acceleration theater | More calls or more context are treated as faster reasoning. | Name the target rate-change and stop/replan trigger. |
| Harmful acceleration | Work is accelerated while safety, ethics, legality, operational-support load, or human wellbeing becomes worse. | Use pattern-reference-only `dyn2HighStakesTemporalMoveRoute?` to name the high-stakes temporal move, window, and unsupported use and cite the assurance, ethics, legal, safety, quality, or wellbeing pattern that governs the other question. |
| Coasting claim without basis | Continued motion after effort stops is treated as free evidence of success. | Name coasting basis: habit, automation, stored work, learned capability, social norm, commitment momentum, physical inertia, queue pressure, or unknown. |
| Reversibility fantasy | Effort is removed and the system is assumed to return cleanly. | Include `dyn2DebtHysteresisBlock?` only when supported use depends on residue/reversibility; record `unknown` if needed and bound supported use, with brake/recovery relation when FPF-governed. |

