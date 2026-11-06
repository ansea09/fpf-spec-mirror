---
chunk_kind: "child"
pattern_id: "C.27.TA"
pattern_title: "Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
section_id: "C.27.TA:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27.TA/C.27.TA__002_use-this-when.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "C.27.TA — Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
  - "C.27.TA:0 — Use This When"
line_start: 67448
line_end: 67482
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.18"
  - "E.24"
  - "G.11"
  - "G.9"
keywords:
  - "cadence"
  - "currentness"
  - "freshness"
  - "recovery timing"
  - "rhythm"
  - "temporal aspect"
  - "time window"
  - "validity window"
---

### C.27.TA:0 - Use This When

Use this pattern when a project needs to state a positive temporal-aspect claim about one exact object or exact claim—for example, its time window, cadence, freshness, recovery timing, or currentness.

Use it when the working question is:

- which time window, interval, duration, latency, cadence, rhythm, synchronization, currentness, freshness, validity window, recovery timing, stabilization timing, trajectory, effort over time, inertia, or refresh condition matters;
- which bearer has that temporal property: system, episteme, work plan, work occurrence, claim, source, benchmark, architecture-selected structure, method description, publication, or project-world object;
- which temporal reference makes the statement reviewable: calendar time, clock time, event order, cycle, sprint, epoch, release train, sampling interval, follow-up interval, or domain-local timing reference; and
- whether the property is merely stated, measured, used in a temporal claim, used in a transformation claim, or used in a work, evidence, or decision relation.

**Primary EntityOfConcern.** The `EntityOfConcern` is the independently identified bearer or exact claim being qualified. A temporal label such as *cadence*, *freshness*, or *recovery timing* is a predicate or qualifier in the ClaimGraph; it is not a second entity.

**C.2.1 and publication boundary.** A materialized temporal-aspect statement is ClaimGraph content in one `C.2.1` episteme whose effective ReferenceScheme makes the temporal terms interpretable. Changing that claim content identifies another episteme. A changed layout, publication occurrence, form, or carrier can leave the episteme unchanged; those publication objects remain separate under `E.24.PUB` when availability matters. When the claim depends on another direct relation, cite that relation's exact declaration or independently established occurrence. A PatternID remains an ordinary rule citation and is never a relation reference.

**First useful move.** Identify the bearer or claim, state its temporal property, and supply the reference and extent needed to interpret it. An observed cadence needs the period observed; a general ordering rule can instead name the event types and their relative order.

**First result.** `CheckoutSystem-1 had a weekly release cadence during release train R14.` This is enough when the receiving action needs no further distinction. Stop there.

Open the fuller statement only when the receiving use also depends on measurement, an exact scheme or scope, a selected Structure, a source or use boundary, currentness, reopen conditions, coupling, another direct relation, or an explicit rule citation or blocked overread.

**What goes wrong if missed.** A cadence has no bearer, a currentness claim has no reference date, or a recovery estimate omits its starting event. Readers then cannot tell which temporal claim could support the receiving action.

**What this buys.** A practitioner can state one positive temporal-aspect claim before selecting `C.27`, `A.3.4`, `A.3.3`, `A.15.2`, `A.15.1`, `C.16`, `C.28`, `G.9`, or the relevant evidence, source, gate, or assurance pattern for the receiving use.

**Not this pattern when.**

- If the question is adequacy or supported use of an authored temporal claim, use `C.27`.
- If the question is bounded transformation under conditions, use `A.3.4`.
- If the question is a state-space and transition-law episteme, use `A.3.3`.
- If the question is work planning or dated work, use `A.15.2` or `A.15.1`.
- If the question is measurement construction, rate construction, scale, score, or metric comparability, use `C.16` and related characterization patterns.
- If the question is causal use of an intervention or policy, use `C.28`.
- If the temporal phrase is ordinary prose and no practical use changes, do not introduce a C.27.TA statement.

