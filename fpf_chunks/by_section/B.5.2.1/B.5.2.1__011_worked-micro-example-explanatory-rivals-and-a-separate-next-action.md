---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:10"
section_title: "Worked micro-example: explanatory rivals and a separate next action"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__011_worked-micro-example-explanatory-rivals-and-a-separate-next-action.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:10 — Worked micro-example: explanatory rivals and a separate next action"
line_start: 52713
line_end: 52741
dependencies:
  - "A.17"
  - "A.18"
  - "B.4"
  - "B.5"
  - "B.5.2"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.5"
keywords:
---

### B.5.2.1:10 - Worked micro-example: explanatory rivals and a separate next action

**Question and case facts.** In a constructed service case, O1 is a latency rise above eight concurrent requests, O2 an increase in blocked threads, O3 a higher cache-miss rate, and O4 normal latency in a serial replay. The question is what explains this contrast. These are stipulated teaching inputs, not empirical results about a real service.

**Construction.** Declare hypothesis grammar v1 with three mechanism flags: lock contention, cache churn and scheduler stalls. The seeds are A, a lock-contention explanation, and B, a cache-churn explanation. NQD-Generate enumerates two declared variations: combine A with B to construct C, an interacting lock/cache explanation; replace A’s mechanism with scheduler stalls to construct D. The finite budget is four hypotheses including the seeds. Provenance records each seed, constructor and resulting claim. The comparison’s must-constraints are that a candidate addresses these service observations using the declared mechanism grammar and makes a discriminating prediction. All four pass after construction.

**Coordinates and comparison.** Q has two ordered count Scales: predicted observations among O1–O4, maximized, and auxiliary assumptions not established by the case facts, minimized. Prediction coverage is calculated under each candidate’s stated auxiliary assumptions; it is not independent confirmation.

A predicts O1/O2/O4 with one unverified lock-scope assumption. The seed cache model B predicts O1/O3 from the stipulated inputs with no additional assumption. C predicts all four using the lock-scope and lock/cache-coupling assumptions. D predicts O1/O4 using unverified scheduler-threshold and recovery assumptions. Their complete comparison is:

| Hypothesis | Descriptor (lock, cache, scheduler) | Predicted observations ↑ | Unverified auxiliaries ↓ | Novelty | Front result |
| --- | --- | ---: | ---: | ---: | --- |
| A: lock contention | (1,0,0) | 3 | 1 | 0 | retained |
| B: cache churn | (0,1,0) | 2 | 0 | 2 | retained |
| C: interacting lock/cache | (1,1,0) | 4 | 2 | 1 | retained |
| D: scheduler stalls | (0,0,1) | 2 | 2 | 2 | dominated by A, B and C |

The declared DominanceSet is exactly the two Q coordinates, with ε=0. Novelty is Hamming distance on the three Boolean flags to the preceding archive containing A only; it is an integer count from 0 to 3 and stays outside dominance. The descriptor grid has one cell per flag tuple, K=1. Exact duplicate claims are removed; none of these four is a duplicate.

D’s scheduler cell is retained under the stated stepping-stone policy even though D is dominated. No D, Surprise or IlluminationSummary reading is needed in this example.

Of the four eligible hypotheses assessed here, A, B and C form the complete front. Each trades prediction coverage against auxiliary assumptions. C.18 records that front separately from the retained archive {A,B,C,D}, and its generation record names this NQD-Generate procedure and the seed/operator provenance. No front thinning is applied. A reviewer can reconstruct this front from the four supplied rows. A request to repeat the enumeration also requires another execution under the requested conditions.

To see what these two counts preserve, consider a possible rival predicting O1, O3 and O4 with one unverified assumption. Its Q vector would equal A's. The coordinates suffice to locate that vector in the stated ordering. A recipient asking about blocked threads in O2 needs to know which observations each candidate explains. Preserve the prediction for O2 and the proposed mechanism for that comparison. This hypothetical rival tests the choice of coordinates and contributes no new assessed candidate to the four-hypothesis run.

**Qualified abductive result.** For a bounded answer to why the blocked threads in O2 occur, B.5.2 compares candidates that explain O2 with at most one unverified auxiliary assumption. A meets that stated plausibility criterion; C needs two, while B and D leave O2 unexplained. A is the qualified prime conjecture, conditional on the lock-scope assumption. A leaves O3 open. Return to the original question about all four observations. Among the candidates compared, C accounts for all four on two unverified assumptions. The one-assumption limit used for the O2 enquiry does not eliminate C as an explanation of the full contrast. Check the assumptions or establish another ground for preferring an explanation at that scope. Evidence that the blocked threads never wait on the proposed lock would defeat A’s explanation of O2. Generation and the coordinate counts supply no assurance level or empirical corroboration.

**Next-use choice.** The separate C.11 question is which available diagnostic action fits a one-hour budget. Reading the existing lock traces takes one hour and addresses A’s open assumption; the combined intervention needed for C takes three hours. Under the declared criterion of addressing the blocked-thread question within that budget, choose the trace reading and decline C’s intervention for this action. C remains a front member and D remains an archive stepping stone. This choice authorizes no performance beyond its independently applicable permission conditions.

