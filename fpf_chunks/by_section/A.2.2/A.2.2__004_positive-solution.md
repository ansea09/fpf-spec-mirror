---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:3"
section_title: "Positive Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__004_positive-solution.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:3 — Positive Solution"
line_start: 5520
line_end: 5562
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "C.32.MWA.PP"
  - "E.23.CDI"
keywords:
  - "Method-relative capability"
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "usable Method structure"
  - "work conditions"
---

### A.2.2:3 - Positive Solution

1. **Identify the required work and whose ability matters.** Start with the proposed or required result for each recipient. Include any work already promised. Which operations, decisions or performances are entrusted to a particular holder? Which may be supplied by someone else? An organized team or a configured machine can be the holder when the required result depends on its parts working together. A claim about what one participant can do needs grounds for that participant's own part.
2. **State the qualified ability.** Name the work family, the criterion the holder meets and the configuration, tools, assistance and other conditions on which this depends. Use :2.1 if it matters who chose the Method or adapted it. A holder can carry out a decision supplied by a helper. Entrusting the decision itself to that holder requires grounds for its ability to choose.
3. **Recover sufficient grounds for this use.** Comparable earlier work, an applicable qualification, or an argument from how the System is organized may already establish what the holder can do. Check its relevance to the required action and the help that will actually be available. A first assignment under permitted supervision can be justified on those terms. Apply the receiving use's evidence and currency requirements. Preserve uncertainty when it could change the result.
4. **Compare the claim with the demand.** Use A.2.6 to test whether the declared WorkScope covers the proposed `JobSlice` and whether the holder meets the required performance criterion there. Apply any required units, bounds, translations and qualification policy. If the commission ends with this assessment, return the supported fit, the mismatch or the specific question still open.
5. **Establish what can be assigned together.** Recover the terms for the whole service. A result made once can serve several recipients if each can obtain it in time and the terms permit reuse. Separate performances, independent judgements or continuous coverage require their own provision. If the terms specify a minimum number or share, use the specified population, period and counting rule and preserve any promises to named recipients. A justified bound can settle the threshold.
6. **Test the arrangement against the conditions the promise covers.** Include existing obligations, shared help and other resources when the same means could be needed more than once. Who may allocate them, what will each decision maker know at the moment of choice, and can the required actions still finish in time? One feasible allocation can settle a choice entrusted to the planner. For a guarantee, establish that the same arrangement covers all combinations of demand, input conditions and availability allowed by the terms, including choices the recipients retain. Use the dependencies that make combinations possible. The arrangement may fix the allocation or choose later from information then available. If two situations are indistinguishable at an irreversible choice, the action taken then must work in both, possibly with different later actions. A risk allowance calls for grounds for the specified risk over its stated population and horizon. Use C.32.MWA.PP:4.7 to construct and compare arrangements when that work is needed.
7. **Return the decision its grounds warrant.** Identify the work the authorized party can assign now, or the conditions on which a later assignment depends. An allowed combination that defeats the proposed arrangement refutes its guarantee. To rule out every permitted arrangement, give grounds covering those alternatives. A shortage of shared provision can leave each holder's qualified ability intact. Use :5 for role, authority and admission, and A.15.1 for a claim about work that actually took place.

One possible statement-and-use record is shown below. It is a way to preserve the claims needed by this use, not a mandatory new entity or classification.

```text
CapabilityStatementRecord:
  capabilityHolderRef: U.System
  canDo: WorkFamilyOrResultClass
  workConditionBasis: U.WorkScope
  supportedPerformance: result criterion or grade met
  attainedMeasureBounds?:

  actualTimeOrConfiguration?:
  capabilityStatementRef?: C.2.1 episteme
  evidenceOrSourceUseRefs:
  qualificationPolicy:
  currentnessAssessmentRefs?:

CapabilityFitCheck:
  holderAbilityClaim: the qualified proposition above
  receivingJobSlice:
  requiredPerformance: receiving criterion
  requiredMeasureBounds?:

  evaluationTime:
  scopeCoverage:
  criterionSatisfied:
  measureComparison?:

  qualificationResult:
  result: fit, mismatch, or named unresolved premise
```

The record separates what is claimed about the System from the grounds for believing it and from what another use demands. The same supported ability may fit one demand and fail another.

