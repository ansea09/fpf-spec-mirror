---
chunk_kind: "child"
pattern_id: "A.3.1.FT"
pattern_title: "Qualify Method Fit and Transfer"
section_id: "A.3.1.FT:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1.FT/A.3.1.FT__006_solution.md"
commit_sha: "8c72429c9a0797d8d48f59b88dce036ac713c78c"
heading_path:
  - "A.3.1.FT — Qualify Method Fit and Transfer"
  - "A.3.1.FT:4 — Solution"
line_start: 10648
line_end: 10696
dependencies:
  - "A.3.1"
  - "A.3.1.QM"
  - "C.11"
  - "C.39.RQ"
keywords:
---

### A.3.1.FT:4 - Solution

Method identity under A.3.1 and one successful Work occurrence do not establish fit in another situation. The operation below compares source and receiving conditions, necessary adaptations and retained evidence, so that an independently usable transfer conclusion can be returned without silently inheriting the source qualification.

Compare actual source and receiving Work through a decision-relative situation account, include one condition capable of defeating the claim, preserve Method semantics and status, and return only the fit or transfer result supported by that comparison.

#### A.3.1.FT:4.1 - Pattern-Use Unfolding

1. **Name the decision, subject, and status.** State whether the question concerns fit in one receiving situation, an applicability boundary, or transfer of one supported claim. Identify the `A.3.1`-admitted Method, or preserve the candidate account and name only separately admitted constituent Methods whose enactment is claimed.
2. **Bound the source and receiving situation families.** Record project purpose, development phase, technical or domain problem characteristics, performer population, holder capabilities, participating Systems, Agent-performed Work, direct relations, constraints, support conditions, qualification window, and the domain result relevant to the claim.
3. **Recover source Work and evidence.** Use A.3.1.WT evidence only for actual Work whose performers, enacted admitted Method, temporal extent, containing System, conditions, deviations, burdens, adaptations, results, and evidence path are recoverable. A report can support the account but does not admit Work by citation.
4. **Select a receiving or held-out situation that can discriminate.** Select or seek one named condition change capable of defeating the claim: technical coupling, project phase, domain, performer or capability envelope, support relation, organizational condition, information availability, authority boundary, or another named condition. State why it matters. If minimality matters, name the alternatives, ordering criterion, and basis for treating one change as smaller or weaker; otherwise record concurrent changes and unknowns without ranking them.
5. **Separate matched, changed, and unknown conditions.** Do not call conditions controlled unless the basis supports it. Record concurrent changes and missing facts; use `missing-comparability-basis` when the comparison cannot distinguish the claimed boundary.
6. **Recover receiving Work independently.** Admit the receiving Work occurrence and every claimed enacted Method under their direct governors. Preserve WorkPlan, simulation, demonstration, report, training, and support tasks as separate results. If receiving Work did not occur, return `missing-performed-work` rather than a transfer claim.
7. **Track adaptations and Method semantics.** Record changes to operations, dependencies, roles, stops, representations, support, and local Work. Ask whether reusable Method semantics stayed within the admitted Method. If they changed, return `variant-question[...]` to A.3.1.MV and evaluate the unchanged and changed branches separately.
8. **Compare domain results and evidence reach.** Compare the result relevant to the fit claim together with burdens, deviations, failures, and limitations needed to interpret it. Distinguish direct observation, report, association, contribution, and causality. Do not use immediate self-report as long-term transfer without the missing time evidence.
9. **Classify the bounded result.** Return `fit-within[...]`, `failure-within[...]`, `applicable-if[...]`, `transfer-supported-between[...]`, `transfer-not-supported`, `missing-performed-work`, `missing-comparability-basis`, or the named missing premise. Plain labels may be used, but the situation, claim, evidence, and window must remain inspectable.
10. **Route a defeated claim by result kind.** Return a failure directly only to the C.39.RQ situational requirement, C.32.MWA.PP architecture decision, B.1.5.CM construction result or admitted Method claim, or A.3.1.MV applicability or variant entry that the evidence contradicts. When the evidence may contradict an A.3.2.DE description, C.37.MP Method representation profile row, or A.15.8.MS support claim, return the bounded observation to A.3.1.CC; A.3.1.CC identifies and rechecks the maintained correction owner, including the direct governor of any lower representation result. Do not reopen every carrier.
11. **State non-transfer and reopen conditions.** Name the populations, domains, capability envelopes, support arrangements, times, alternatives, and causal claims not covered. Reopen when one condition crosses the declared boundary, Method semantics change, evidence currentness expires, or a new unlike situation defeats the claim.

#### A.3.1.FT:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| validation use | Fit, applicability, or transfer question; receiver; decision; claim; qualification window; stop. |
| subject status | Admitted Method, or candidate account plus separately admitted enacted constituent Methods. |
| source situation | Situation-family conditions, actual Work, performers, capability inputs, Systems, Agent-performed Work, direct relations, adaptations, domain results, burdens, and evidence reach. |
| receiving situation | The same positions for actual receiving or held-out Work, including missing facts. |
| discrimination | Condition selected to challenge the claim, why it matters, matched conditions, changed conditions, and unknowns. |
| semantic continuity | Preserved Method semantics, local Work or support changes, and any reusable semantic change returned as a variant question. |
| comparison | Result differences, burdens and deviations needed for interpretation, evidence strength, and unsupported contribution or causal claims. |
| return | Bounded fit, failure, applicability, transfer, or missing-evidence result; direct C.39.RQ, C.32.MWA.PP, B.1.5.CM, or A.3.1.MV return, or a bounded A.3.1.CC observation for a possible A.3.2.DE description, C.37.MP Method representation profile-row, or A.15.8.MS support contradiction; non-transfer and reopen conditions; unaffected results preserved. |

#### A.3.1.FT:4.3 - What Changes in Practice

Teams stop transferring a Method by title or rejecting it after an unexplained local failure. They can show the source conditions, receiving conditions, actual Work, semantic continuity, one discriminating change, and the exact claim that survived or failed.

A narrow result such as “Fits this decision for this holder and support window; transfer untested” can support a decision to use the Method now while protecting later teams from a universal claim.

#### A.3.1.FT:4.4 - Minimal Constructed Fit Replay

Continue the constructed A.3.1.WT evidence for admitted `M-Unit-Review-1`. The immediate decision is whether the Method fits pre-release review of temperature-sensor reports for `Reviewer-17` through day D30 when mixed Celsius/Kelvin inputs may occur. It is not yet a decision about another reviewer, product family, tool, or organization.

`W-Rep-1` and `W-Disc-1` are actual Work in `Calibration-Team-A`. The same reviewer, capability input `CAP-R17-1` with qualification record `QR-R17-1`, MethodDescription edition 4, manually retrieved conversion table, release boundary, and containing System are recorded. The discriminating change is the Celsius/Kelvin mismatch in `S-Disc-1`; it can defeat the claim that the Method exposes a unit mismatch before the release decision. In `W-Disc-1`, the reviewer normalizes values, detects the mismatch, stops release, and returns the report. A.3.1.CC has separately corrected direct use result `C37-UR-Flow-4` and its governed representation result `REP-UR-Flow-4`, which had omitted normalization for that named use.

Return `fit-within[Reviewer-17, temperature-sensor reports, edition 4, manual conversion table, through D30]` for the named release-review decision. Also return `transfer-not-tested` for other holders, product families, support routes, qualification windows, or organizations. The two occurrences do not establish causal superiority or practical worth.

If the reviewer had changed the reusable operation from unit normalization to an approximation rule absent from `M-Unit-Review-1`, preserve the observed Work but return `variant-question[approximation-rule]` to A.3.1.MV. Do not call the changed branch successful transfer of the unchanged Method.

