---
chunk_kind: "child"
pattern_id: "C.27.TA"
pattern_title: "Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
section_id: "C.27.TA:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27.TA/C.27.TA__002_use-this-when.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.27.TA — Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
  - "C.27.TA:0 — Use This When"
line_start: 55797
line_end: 55827
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

Use this pattern when a project needs to name a positive temporal aspect of a governed object, claim, transformation, work plan, evidence relation, architecture move, benchmark, source use, or publication use.

Use it when the working question is:

- which time window, interval, duration, latency, cadence, rhythm, synchronization, currentness, freshness, validity window, recovery timing, stabilization timing, trajectory, effort over time, inertia, or refresh condition matters;
- which bearer has that temporal aspect: system, episteme, work plan, work occurrence, claim, source, benchmark, architecture-selected structure, method description, publication, or project-world object;
- which temporal reference makes the statement reviewable: calendar time, clock time, event order, cycle, sprint, epoch, release train, sampling interval, follow-up interval, or domain-local timing reference;
- whether the temporal aspect is merely named, measured, used in a temporal claim, used in a transformation claim, or used in a work, evidence, or decision relation.

**Primary EntityOfConcern.** The `EntityOfConcern` is a temporal aspect of a governed object or claim. `C.27.TA` introduces no new `U.TemporalAspect` kind; it supplies slot discipline for temporal aspects that fill relations in other patterns.

**E.24 ontic boundary.** C.27.TA follows `E.24` by refusing a new ontic root here. A temporal aspect is identified by its bearer, aspect kind, temporal reference, window or interval, relation to the governed object or claim, and governing use relation. Those slots make the aspect reviewable without claiming that `timeWindow`, `cadence`, `freshness`, `trajectory`, or `recoveryTiming` are standalone `U.*` kinds. If an authored temporal claim uses the aspect as sufficient for action, C.27 carries adequacy; if a transformation, dynamics model, work plan, evidence use, benchmark, or assurance claim is being made, the governing pattern for that use carries it.

**First useful move.** Write a `TemporalAspectStatement`: bearer, aspect kind, bounded context, temporal reference, interval or window, relation to the governed object or claim, and the governing FPF pattern relation that carries the use.

**What goes wrong if missed.** Temporal words become vibe labels. A cadence is named without bearer, a freshness claim has no validity window, a rhythm has no timing reference, a recovery claim has no interval, an architecture trajectory has no changed structure, and a transformation claim smuggles timing into method, mechanism, or evidence.

**What this buys.** A practitioner can name the temporal aspect as a positive subject before deciding whether `C.27`, `A.3.4`, `A.3.3`, `A.15.2`, `A.15.1`, `C.16`, `C.28`, `G.9`, evidence, source, gate, or assurance patterns carry the actual use.

**Not this pattern when.**

- If the question is adequacy or supported use of an authored temporal claim, use `C.27`.
- If the question is bounded transformation under conditions, use `A.3.4`.
- If the question is a state-space and transition-law episteme, use `A.3.3`.
- If the question is work planning or dated work, use `A.15.2` or `A.15.1`.
- If the question is measurement construction, rate construction, scale, score, or metric comparability, use `C.16` and related characterization patterns.
- If the question is causal use of an intervention or policy, use `C.28`.
- If the temporal phrase is ordinary prose and no practical use changes, do not introduce a C.27.TA statement.

