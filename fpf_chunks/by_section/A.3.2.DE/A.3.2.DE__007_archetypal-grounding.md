---
chunk_kind: "child"
pattern_id: "A.3.2.DE"
pattern_title: "Describe a Method for Its Intended Use"
section_id: "A.3.2.DE:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2.DE/A.3.2.DE__007_archetypal-grounding.md"
commit_sha: "6e0d4301aad71e3fff553886d2598e6595d1b963"
heading_path:
  - "A.3.2.DE — Describe a Method for Its Intended Use"
  - "A.3.2.DE:5 — Archetypal Grounding"
line_start: 11671
line_end: 11714
dependencies:
  - "A.3.2"
  - "C.37"
  - "C.39"
  - "E.8"
keywords:
---

### A.3.2.DE:5 - Archetypal Grounding

#### A.3.2.DE:5.1 - Stop at the Candidate Whole

`C-EC-Release-v2` is a prospective account of a possible release-coordination whole. Its intended result, alternatives A, B2, and R, guards, authority boundaries, confidentiality, reversibility, and D0 stop make it useful, but the whole is not admitted as a `U.Method`. A.3.2.DE may improve those claims for a selection or trial-planning use; it does not return a `U.MethodDescription` for that candidate whole.

The improved account remains useful: users can compare A and B2 before integration and plan a bounded trial with recovery R after a failed B2 closure. Every downstream use keeps the account's candidate status.

#### A.3.2.DE:5.2 - A Bounded Description of an Admitted Constituent Method

For the admitted constituent `M-HW-Verify`, suppose the named use is preparing safety-verification Work for one EC-417 release. A description edition can state the applicable safety-relevant change family, the distinction between provisional and signed evidence, the comparison and affected-verification actions, the signed-before-closure bound, confidentiality conditions, and the mismatch or stale-edition stop. The use-coverage account says that it exposes those Method claims but omits dates, assignees, actual evidence versions, actual verification results, and release authority decisions.

The planner may cite that edition when constructing a WorkPlan. Supply separate claims about the Work schedule, the assignment of `SafetyReviewer-17`, the required capability, closure authorization, and whether verification occurred whenever the plan or later Work relies on them.

#### A.3.2.DE:5.3 - Turn a reconciliation reminder into an instruction

In this constructed case, a stock-reconciliation Method has already been identified. Its working rule is available, but the draft for a new storekeeper says only: "Reconcile stock and investigate discrepancies." The reader can add and subtract counts; they still need to know which counts to compare and what the difference means.

The author recovers the rule's inputs and dependencies. For one item, unit and interval, an opening stock count plus receipts minus issues gives the expected closing count, provided the movement account includes every change once. A physical count at the closing boundary supplies a different input. The author writes this instruction:

1. Select the item, counting unit and interval. Obtain the opening count, receipts and issues for that same scope, and the physical count at its closing boundary. Resolve a missing movement class, unit conversion or mismatched boundary before treating the balance as complete.
2. Calculate expected closing stock as opening stock plus receipts minus issues. The additions and subtractions represent movements into and out of the selected stock.
3. Subtract expected stock from the physical count. Return the difference with the counts and scope used. A negative difference means fewer units were counted than the movement account predicts; it does not identify the cause.
4. If the counts disagree, return the discrepancy for checking the movements and counts. Do not change a source count merely to force agreement.

With opening stock 48, receipts 12, issues 17 and a closing physical count of 41, the expected count is 43 and the discrepancy is -2. The description now supplies an operation, its operands, their origins, the reason for their combination and a useful return. Its authoring result is the instruction, not evidence that a storekeeper performed it.

The receiving-use check asks the reader to recover that calculation and return from the description. If the opening figure is in boxes while movements are in individual units and the conversion is unknown, a numerical balance remains unavailable. A comparison-only description could legitimately omit this enactment detail; this edition promises the storekeeper a way to perform the reconciliation.

#### A.3.2.DE:5.4 - Explain the Basis of a Professional Judgment

A stakeholder map can keep the same boxes and labels while the way of constructing and using it changes. In this constructed case, an admitted contact-planning Method includes people who hold the approval or supply roles needed to arrange a rollout. A proposed child account instead asks whether a new shift-handover routine covers the work of the people who produce and use the handover information. Its author cannot explain that change merely by adding "be inclusive" to the old instruction.

The receiving use is a facilitator's preparation of a handover review. Available inputs are the proposed routine, the two-shift role roster, the information each role supplies or needs, and the known limits of those accounts. The author writes the proposed instruction:

1. Start from the handover information that must reach the next shift and identify the roles that produce or use it. Include a role because of that working dependency, even when its holder has little influence over rollout approval. Use actual supplied facts; mark an uncertain dependency for clarification.
2. For each included role, obtain an account of the information needed, the action it enables and a relevant missing-information case. Distinguish what a participant or work record actually supplies from the facilitator's assumption. A manager's approval does not supply another role's working account by itself.
3. Relate those needs to the proposed routine. Show which handover action supplies each needed result and which dependency remains uncovered or unknown. Influence can help arrange contact; it does not remove a required receiving role from this check.
4. Return the map with the supported coverage and the particular missing account or handover contribution. Stop a claim of complete coverage when a material dependency remains unresolved. The result can guide a correction or a bounded trial; it does not itself authorize rollout or show that the routine works.

For a small replay, suppose a day lead approves the trial, an IT maintainer supplies the display, and a night operator uses unresolved-item flags to resume work. The approval-contact map may correctly contain the first two roles. The proposed method also includes the night operator because the operator consumes a result needed for the handover. If the routine supplies a flag but no next action, the map exposes that missing contribution. If a relief operator's information need is unknown, add that unresolved dependency rather than treating a full roster of names as complete coverage.

The explanation now makes the changed judgment recoverable: inclusion follows a working dependency, and completion requires an account of its contribution. The canvas may remain unchanged, but the operation, required evidence and stop differ. This is proposed reusable content, so retain candidate status and use A.3.1.MV:5.2 for its derivation and evidence boundaries. The replay checks whether the explanation supplies the intended distinctions; it is not a field validation of the proposed method.

