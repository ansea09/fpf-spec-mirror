---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__006_archetypal-grounding.md"
commit_sha: "31f4cb0b7f8000e0115098b50b44f80c8c36a671"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:5 — Archetypal Grounding"
line_start: 65115
line_end: 65168
dependencies:
  - "A.3.3.TR"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
  - "E.18.2"
keywords:
---

### C.29.BB:5 - Archetypal Grounding

#### C.29.BB:5.1 - A transfer line changes which balance answers the tank question

Use a constant-density liquid, measured by volume in litres. At the start, tank A holds 30 L and tank B holds 10 L. Over the chosen interval, an external supply adds 12 L to A, and an external outlet removes 7 L from B.

First suppose the line transfers 15 L from A to B with no change in its liquid content. Then

    A: 30 + 12 - 15 = 27 L
    B: 10 + 15 - 7 = 18 L
    A+B: 40 + 12 - 7 = 45 L.

The internal 15 L cancels. The larger balance gives the combined amount without needing that internal transfer, while the separate balances give each tank's amount.

Now change the condition: the line begins empty, receives 15 L from A, delivers 13 L to B, and retains 2 L. The results become

    A: 27 L
    B: 10 + 13 - 7 = 16 L
    line: 0 + 15 - 13 = 2 L.

The two tanks contain 43 L. Their boundary excludes the line, so 15 L leaves that boundary and 13 L re-enters. The combined tank change is 12 - 7 - 15 + 13 = 3 L. Including the line gives 45 L and recovers the five-litre increase from the external exchanges alone.

If the line's increase is known only to lie between 0 and 2 L, the final tank total lies between 43 and 45 L. This bound settles a request for at least 42 L in the tanks. A request for at least 44 L needs a tighter bound or the line's actual content. No additional observation is required for the first request.

#### C.29.BB:5.2 - Moving and reworking a job preserve one count but change its distribution

Count accepted jobs that have not yet been completed. Each job occupies one of two stages, including any processing position in that stage. Initially A contains 6 jobs and B contains 4.

During an interval, 12 new jobs arrive at A, 9 move from A to B, and 7 are completed at B. With no other arrivals, completions or membership changes,

    A at end = 6 + 12 - 9 = 9
    B at end = 4 + 9 - 7 = 6
    unfinished total at end = 10 + 12 - 7 = 15.

A limit of 12 unfinished jobs is therefore exceeded at the endpoint. Determining whether the limit was exceeded earlier requires the event history or a bound on its prefixes.

If 2 of B's remaining jobs return to A for rework before the endpoint, the stage totals become 11 and 4; the unfinished total remains 15. The extra work is consequential, but moving the same jobs changes their distribution rather than their count.

If the question instead counts separately created work orders, specify that new population and its creation rule. A parent job and two newly opened orders cannot be mixed into the earlier job count without changing its meaning. The next operations-management question may need workload or completion-time modeling in addition to this balance.

#### C.29.BB:5.3 - One shared transfer preserves the computational total

Two computational cells store amounts 10 and 20. One step adds 5 from outside to cell A, removes 2 from cell B, and transfers 3 from A to B. Using one transfer amount gives

    A' = 10 + 5 - 3 = 12
    B' = 20 + 3 - 2 = 21
    A' + B' = 33 = 30 + 5 - 2.

Suppose A subtracts 3 but B adds 2.9. The resulting total is 32.9; the inconsistent interface updates lose 0.1 in that step. Repairing the shared amount restores the aggregate balance. Whether the transfer approximates the intended transport well remains a separate question.

Now let both sides use 2.9. The result is A'=12.1, B'=20.9 and total 33. The aggregate balance holds, but the supplied transfer of 3 requires the local values 12 and 21. Agreement between the two interface amounts preserves the total; their accuracy must still be established for the requested local result.

If the cells store average densities, first multiply by their volumes to obtain the amounts. Summing unequal-volume cells' densities would test another quantity.

