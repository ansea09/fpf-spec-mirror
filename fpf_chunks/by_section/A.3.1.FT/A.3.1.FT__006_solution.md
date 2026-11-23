---
chunk_kind: "child"
pattern_id: "A.3.1.FT"
pattern_title: "Qualify Method Fit and Transfer"
section_id: "A.3.1.FT:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1.FT/A.3.1.FT__006_solution.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "A.3.1.FT — Qualify Method Fit and Transfer"
  - "A.3.1.FT:4 — Solution"
line_start: 11321
line_end: 11375
dependencies:
  - "A.3.1"
  - "A.3.1.QM"
  - "C.11"
  - "C.39.RQ"
keywords:
---

### A.3.1.FT:4 - Solution

Method identity under A.3.1 does not settle fit. Work back from the receiving result to the operations and conditions on which the Method’s contribution depends. Identify grounds for those conditions in the receiving situation. A shared premise, an invariant, a sufficient bound, applicable records or an observed performance may settle the question. A failed necessary condition can exclude the proposed use. For a claim drawn from observed Work, establish which features made that observation relevant and whether they carry over.

Keep Method semantics and status fixed for the comparison. Separate a demonstrated failure from insufficient grounds for transfer. Seek a discriminating observation only where an open difference could change the conclusion. Report what the established grounds warrant for the receiving work.

#### A.3.1.FT:4.1 - Pattern-Use Unfolding

1. **Name the decision, subject, and status.** State whether the question concerns fit in one receiving situation, an applicability boundary, or transfer of one supported claim. Identify the `A.3.1`-admitted Method, or preserve the candidate account and name only separately admitted Methods whose enactment is claimed.
2. **Bound the situations needed for the decision.** For local fit, name the situation or situation family and required result. For transfer, name both source and receiving families; for an applicability boundary, name the situations that can establish that limit. Record the conditions that matter to the claim, such as project purpose, development phase, technical or domain problem, performer population, holder capabilities, participating Systems, direct relations, constraints, support, qualification window and domain result.
3. **Recover the grounds for the claim.** Trace the argument or source observation to the premise it supplies. Establish its applicability to the receiving conditions, including required capability, compatibility, support and timing. When relying on observed Work, recover the performers, enacted admitted Method, temporal extent, containing System, conditions, relevant adaptations, burdens and outcomes. A report may supply evidence for that account. Admission of a Work occurrence follows A.15.1.
4. **Select discriminating evidence when the claim needs it.** When existing grounds leave a consequential boundary or transfer question open, select or seek a receiving or held-out situation with a condition capable of defeating the claim: technical coupling, project phase, domain, performer or capability envelope, support relation, organizational condition, information availability, authority boundary, or another named condition. State why it matters. If minimality matters, name the alternatives, ordering criterion, and basis for treating one change as smaller or weaker; otherwise record concurrent changes and unknowns without ranking them.
5. **Qualify comparability when making a comparison.** Separate matched, changed, and unknown conditions. Do not call conditions controlled unless the basis supports it. Record concurrent changes and missing facts; use `missing-comparability-basis` when the comparison cannot distinguish the claimed boundary.
6. **Establish any required receiving performance independently.** Admit receiving Work and every claimed enacted Method under their direct governors. Distinguish plans and reports from performed activity. For simulation, demonstration, training or support tasks, identify what was actually performed and what was only represented or planned; a demonstration may itself perform the Method in the required receiving situation. If the Work needed for the selected conclusion did not occur, return `missing-performed-work`.
7. **Track adaptations and Method semantics.** Record changes to operations, dependencies, participant or responsibility conditions, stops, representations, support, and local Work. Ask whether reusable Method semantics stayed within the admitted Method. If they changed, return `variant-question[...]` to A.3.1.MV and evaluate the unchanged and changed branches separately.
8. **Assess domain results and evidence reach.** Assess the required result and the burdens, deviations, failures and limitations that affect the fit decision. Compare results across situations when the selected claim requires it. Distinguish direct observation, report, association, contribution, and causality. Do not use immediate self-report as long-term transfer without the missing time evidence.
9. **Classify the bounded result.** Return `fit-within[...]`, `failure-within[...]`, `applicable-if[...]`, `transfer-supported-between[...]`, `transfer-not-supported`, `missing-performed-work`, `missing-comparability-basis`, or the named missing premise. Plain labels may be used, but the situation, claim, evidence, and window must remain inspectable.
10. **Route a defeated claim by result kind.** Return a failure directly only to the C.39.RQ situational requirement, C.32.MWA.PP architecture decision, B.1.5.CM construction result or admitted Method claim, or A.3.1.MV applicability or variant entry that the evidence contradicts. When the evidence may contradict an A.3.2.DE description, direct C.37 representation-use result or C.37.MP Method representation profile row, or A.15.8.MS support claim, return the bounded observation to A.3.1.CC; A.3.1.CC identifies and rechecks the maintained correction owner, including the direct governor of any lower representation result. Do not reopen every carrier.
11. **State non-transfer and reopen conditions.** State the supported applicability boundary and any uncovered use that matters to the receiving decision. Reopen when one condition crosses the declared boundary, Method semantics change, evidence currentness expires, or a new unlike situation defeats the claim.

#### A.3.1.FT:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| validation use | Fit, applicability, or transfer question; receiver; decision; claim; qualification window; stop. |
| subject status | Admitted Method, or candidate account plus separately admitted enacted Methods. |
| situation and grounds | Receiving conditions, required outcome and the premises that bear on it. For claims depending on actual Work, include the relevant performance, capabilities, support, adaptations, result and evidence reach. |
| source and receiving situations | For transfer, identify both sets of conditions and the grounds for carrying the particular conclusion between them. For a broader applicability boundary, establish where those grounds hold and where they fail or remain open. |
| discrimination | When a boundary or transfer claim needs a discriminating situation, state the selected condition and why it matters. In a comparison, separate matched, changed and unknown conditions. |
| semantic continuity | Preserved Method semantics, local Work or support changes, and any reusable semantic change returned as a variant question. |
| assessment | Result against the local fit criteria; differences across situations when needed; burdens and deviations needed for interpretation, evidence strength, and material limits on contribution or causal claims. |
| return | Bounded fit, failure, applicability, transfer, or missing-evidence result; direct C.39.RQ, C.32.MWA.PP, B.1.5.CM, or A.3.1.MV return, or a bounded A.3.1.CC observation for a possible A.3.2.DE description, direct C.37 representation-use result, C.37.MP Method representation profile-row, or A.15.8.MS support contradiction; non-transfer and reopen conditions; unaffected results preserved. |

Keep the distinctions needed for the selected decision in the assessment and its referenced evidence. A table is optional; no separate record is needed for each position.

#### A.3.1.FT:4.3 - What Changes in Practice

The practitioner can answer for the named use and show what the argument establishes if circumstances change. For transfer, identify the premise responsible for the original result and test it against the receiving conditions. Use occurrence evidence where the conclusion depends on what a participant actually did.

A narrow result such as “Fits this decision for this holder and support window; transfer untested” can support a decision to use the Method now while protecting later teams from a universal claim.

#### A.3.1.FT:4.4 - Constructed Fit Case

Continue the constructed A.3.1.WT case for admitted `M-Unit-Review-1`. A release manager asks whether `Reviewer-17` can use it on the eligible temperature-sensor reports through D30, including reports with mixed Celsius/kelvin inputs. First establish which part of that decision the trial already answers.

`W-Rep-1` and `W-Disc-1` are actual Work in `Calibration-Team-A`. The same reviewer, capability input `CAP-R17-1` with qualification record `QR-R17-1`, MethodDescription edition 4, manually retrieved conversion table, release boundary, and containing System are recorded. The discriminating change is the Celsius/Kelvin mismatch in `S-Disc-1`; it can defeat the claim that the Method exposes a unit mismatch before the release decision. In `W-Disc-1`, the reviewer normalizes values, detects the mismatch, stops release, and returns the report. A.3.1.CC has separately corrected direct use result `C37-UR-Flow-4` and its governed representation result `REP-UR-Flow-4`, which had omitted normalization for that named use.

Return `fit-within[Reviewer-17, S-Rep-1 and S-Disc-1 as observed, edition 4, manual conversion table]` for the two reviews under the recorded conditions. The qualification record reports detection of all four seeded unit cases with edition 4. The qualification remains current through D30 under its own criterion. To extend the result to every eligible report through D30, establish what those reports may contain, how the reviewer can recognise and handle each relevant case by the release decision, and whether the necessary support will be available then. For example, a missing unit label may require information that arrives too late. If the method permits timely referral and the commission allows a report to be held, a justified hold can be the right outcome. A promise to clear every report by a deadline needs grounds for clearance as well. Where the trial and other grounds leave one of these conditions open, report that limit on the through-D30 claim. Transfer to another reviewer, product family or support route also depends on the conditions of that use. A claim of causal superiority or practical worth would require its own comparison.

For the narrower decision about the same-unit report already reviewed in `W-Rep-1`, its observed acceptance can support fit for that named situation, reviewer and support window. `W-Disc-1` is not a prerequisite for this narrower result. Evidence about mixed-unit handling is needed when that condition enters the receiving question.

For a different commission, suppose two reporting systems express the same readings in Celsius and kelvin, use a verified exact unit conversion, and apply equivalent tolerances at the same resolution. The conversion preserves the comparison with the applicable limit. Those facts carry the comparison rule to the new system before anyone runs a report there. A question about whether the next reviewer will recognize the units in time still depends on their preparation, available indications and support. A claim that the review actually occurred requires its own evidence.

If the reviewer had changed the reusable operation from unit normalization to an approximation rule absent from `M-Unit-Review-1`, preserve the observed Work but return `variant-question[approximation-rule]` to A.3.1.MV. Do not call the changed branch successful transfer of the unchanged Method.

