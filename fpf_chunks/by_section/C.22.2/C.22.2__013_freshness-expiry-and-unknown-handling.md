---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:12"
section_title: "Freshness, Expiry, and Unknown Handling"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__013_freshness-expiry-and-unknown-handling.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:12 — Freshness, Expiry, and Unknown Handling"
line_start: 52136
line_end: 52165
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

### C.22.2:12 - Freshness, Expiry, and Unknown Handling

`C.22.2` includes a section-local state and disposition vocabulary for `ProblemCard`; this vocabulary is not a new FPF kind. These labels describe the card's current governed use; they are not required states in a transition sequence, event kinds, or gate records. The local labels are:

| State or disposition label | Required interpretation |
|---|---|
| `draftSignal` | A problem signal has been captured, but the card is not yet reviewable. |
| `reviewable` | The problem-side record can be inspected, challenged, sent onward, or refined, but it is not necessarily P2W-ready. |
| `P2W-ready` | Local disposition label with plain gloss: problem-side input ready. The problem-side record is sufficient for downstream P2W or selector-facing use; it is not `ReadyForWork`, `GateReady`, `MethodReady`, `AutonomyReady`, or work authorization. |
| governing-pattern cue | A claim, relation, or boundary outside `C.22.2` changes the current problem-card use; the card names the governing FPF pattern and claim kind named by value to use next without claiming that use inside `C.22.2`. |
| `stale` | Freshness or expiry blocks the intended downstream use until refreshed, retired, or otherwise disposed. |
| `refreshed` | The relevant signal, source material, source relation, ReferenceScheme, ClaimScope, characterization, parity, evidence, provenance, assurance, representation relation, or wording-use relation has been updated enough for the named use. |
| `retired` | The problem-side record is no longer used as a current problem for downstream work. |
| `archived` | The record is retained under the relevant archive, pool, front, or selected-set pattern without being current for P2W. |
| `abstainOrNoChange` | No downstream receiving use is selected because the signal is stale, duplicate, already solved, already absorbed, unnecessary, or not worth current downstream Work. |

Freshness names the exact affected locus: problem signal, effective ReferenceScheme, ClaimScope, characterization or parity relation, problem-formulation reason, source material, source relation, source-set reference, representation relation, or wording-use relation. For the problem signal, ask whether it is still present, recurring, solved, absorbed, duplicate, unnecessary, or no longer worth downstream work. For ReferenceScheme or ClaimScope, ask whether the applicable meaning, cut, assumptions, window, or receiving use changed enough to alter the formulation. For characterization or parity, ask whether measurement, comparison, and parity relations are current enough for the intended use. For the formulation reason, source material, or source relation, ask whether cited sources, provenance, reason references, and source references remain current. For a source set, ask whether archive, front, pool, shortlist, or selected-set membership and its selection or retention criterion remain current. For a representation or wording-use relation, ask whether wording, diagram, functional description, transformation-flow path, Bridge, retargeting, or other representation change alters the EntityOfConcern, effective ReferenceScheme, ClaimScope, viewpoint qualification, comparison relation, governed next use, or relation needed for inheritance.

A stale source material, source relation, or evidence reference does not always retire the problem; it may require refresh while the problem remains reviewable. A stale problem signal may lead to refresh, retire, archive, abstain or no-change, or a governing-pattern cue for the claim, relation, or boundary that is checked.

Freshness or expiry failure is a current disposition. A stale or unknown-bearing problem card may remain reviewable as a problem-side record, but it does not become P2W-ready unless freshness and unknown handling permit the intended downstream use. A stale problem card does not silently remain usable as P2W input.

When freshness, expiry, or unknown handling fails, choose one of these current dispositions:

- refresh the problem card or its characterization or comparison relation under `G.11`, `C.16`, `A.19`, `C.25`, or `G.9`;
- retire or deprecate the problem-side record under the relevant archive, pool, selected-set, or refresh pattern;
- continue only as explicitly governed bounded-risk use under the governing pattern for the claim being made, relation, or boundary.

Unknown-handling fields state whether they permit use, require degraded use, abstention, or sandbox treatment, or make the current problem formulation blocked. No P2W, no change, or abstain-for-now may be a successful next use when the signal is stale, duplicate, already solved, already absorbed, unnecessary, or not currently worth downstream work. Before `ProblemCard` emits or binds `TaskSignature`, it checks whether the problem signal is still present and whether prior work has already solved or removed the problem.

