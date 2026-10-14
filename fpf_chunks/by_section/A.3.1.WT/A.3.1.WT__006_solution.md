---
chunk_kind: "child"
pattern_id: "A.3.1.WT"
pattern_title: "Design and Interpret a Method Work Trial"
section_id: "A.3.1.WT:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1.WT/A.3.1.WT__006_solution.md"
commit_sha: "5282e0d9d224431a858c8fccd4c1d5bd99dd565f"
heading_path:
  - "A.3.1.WT — Design and Interpret a Method Work Trial"
  - "A.3.1.WT:4 — Solution"
line_start: 10237
line_end: 10293
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.3.1.QM"
keywords:
---

### A.3.1.WT:4 - Solution

A.15.1 identifies performed Work and A.10 governs a claimed evidence use. The trial construction below determines which Work, variation, observation and stopping condition can answer the unresolved Method question. Its result is distinct from coherence, transfer and comparative worth; reuse a matching existing observation before commissioning a trial.

Select situations from the later evidence questions, arrange and observe actual Work, preserve every subject's status, and return occurrence-level evidence with explicit gaps and limits on the conclusions it supports.

#### A.3.1.WT:4.1 - Pattern-Use Unfolding

1. **Name the later decisions and trial questions.** Separate the questions that may feed A.3.1.CC coherence, A.3.1.FT situational fit or transfer, and C.11.MV practical worth. Do not hide several conclusions inside “does the Method work?”.
2. **Preserve the subject branch.** Identify the admitted Method under `A.3.1`, or keep the proposed whole as a candidate account. In the candidate branch, state which candidate claims are being compared and which constituent Methods, if any, are separately admitted and may be enacted.
3. **Select one representative situation.** Name the intended-use characteristics that matter to the question: task purpose, development phase, technical or domain conditions, performer population, holder capabilities, participating Systems, direct relations, constraints, and qualification window. State why this situation covers the current question without claiming population representativeness.
4. **Select a discriminating situation when the decision needs one.** Change or seek one condition whose outcome can show whether a live claim holds in that situation: unfamiliar technical coupling, another domain, missing support relation, changed capability envelope, stale material, or another named alternative. State the claim that could fail. Do not require every trial to contain an artificial stress case.
5. **Write the WorkPlan without backdating Work.** State intended tasks, performers, admitted Methods, support conditions, observation points, protected conditions, burdens to record, stop rules, and the later use of each observation. Keep simulation and demonstration as planned or separately typed activities unless independently admitted Work occurs.
6. **Check capability and support inputs separately.** When reliance on capability changes interpretation, identify the holder System, Work family or result class, operating envelope, measures, qualification or currentness condition, and evidence. Recover only A.15.8.MS material, access, tool, provider, feedback, and decision conditions supported for the relevant task rows; preserve retained candidates, split boundaries, untested conditions, and gaps rather than treating them as configured inputs.
7. **Admit only Work that occurred.** For each occurrence, recover every actual performer System and its A.13 basis, the action history, at least one admitted Method actually followed, temporal extent, and required containing-System relation under `A.15.1`. Add assignment attribution, System use, operation binding, affected referent, resource use, or result relations only when their own predicates obtain.
8. **Record conditions and departures.** For each Work occurrence, record the situation, relied-on Systems and direct relations, holder capabilities used in interpretation, deviations from the WorkPlan, adaptations, burdens, stops, domain results, and observations. Keep the domain result, report, log, and evidence-use relation separate from Work.
9. **Qualify the evidence reach.** Distinguish direct observation, participant report, source interpretation, observed association, contribution claim, and causal claim. Return the strongest supported level and name missing comparison, temporal, capability, relation, or alternative evidence.
10. **Return evidence by later use.** Send contradicted description or relation claims to A.3.1.CC, situation comparisons and an unlike-situation result to A.3.1.FT, and results, burdens, alternatives, side effects, and evidence limits to C.11.MV. Return `missing-performed-work`, `missing-method-admission`, `missing-capability-basis`, `missing-direct-relation`, or the named missing premise when a required condition is absent.

#### A.3.1.WT:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| trial use | Later decision, bounded trial question, qualification window, and stop. |
| subject status | Admitted Method, or candidate account plus each separately admitted constituent Method whose enactment is claimed. |
| situations | Representative and any discriminating situation, selection criteria, matched conditions, changed conditions, and claim each can test. |
| plan baseline | Intended Work, performers, Methods, support conditions, observations, burdens, protected conditions, and stop rules. |
| actual Work | Each admitted Work occurrence, actual performers, enacted admitted Methods, temporal extent, containing System, and deviations from plan. |
| relied-on conditions | Holder capabilities, Systems, Agent-performed Work, direct relations, access, assignments, permissions, authority, tools, providers, and support conditions that actually obtain or remain missing. |
| observations | Domain results, burdens, adaptations, failures, participant reports, direct observations, and their source or evidence-use relations. |
| reach and gaps | Supported observation level, unsupported contribution or causal overreads, missing evidence, and conditions that would reopen the slice. |
| return | Occurrence-level evidence routed separately to A.3.1.CC, A.3.1.FT, and C.11.MV, or a supported lower result. |

#### A.3.1.WT:4.3 - What Changes in Practice

Teams stop calling a scheduled exercise or positive report “the trial”. They can point to the actual Work, the admitted Method that was enacted, the conditions on which the result depended, and the named later question each observation can answer.

A failed or incomplete occurrence remains useful. It can expose a description defect, a representation difficulty, a missing support relation, a capability condition, or a situation boundary without being inflated into a universal verdict on the Method.

#### A.3.1.WT:4.4 - Minimal Constructed Trial Replay

The following is a constructed teaching replay, not field evidence. It shows the smallest result that lets later checks reuse the same Work without turning the trial into their conclusion.

`M-Unit-Review-1` is admitted for reviewing temperature-sensor calibration reports before release. Its current description tells the reviewer to identify every source unit, normalize values, compare them with the declared tolerance, and stop on an unresolved mismatch. `WP-ME11-1` plans two review tasks for the same week. `S-Rep-1` is a current same-unit report of the ordinary kind. `S-Disc-1` keeps the product, decision, reviewer, description, and support fixed but introduces a Celsius/Kelvin mismatch; it is selected because the live claim is that the Method lets this reviewer expose a unit mismatch before release.

The interpretation relies on `CAP-R17-1`: holder `Reviewer-17`; calibration-report-review Work family; temperature-sensor-report envelope; measure “four of four seeded unit cases detected with description edition 4”; current through day D30; qualification record `QR-R17-1`. The qualification, assignment, permission to inspect the report, and release authority remain different facts. The trial also records description edition 4 and the manually retrieved conversion table as A.15.8.MS support inputs.

Two occurrences then happen and are admitted separately. `W-Rep-1` is performed by `Reviewer-17` inside `Calibration-Team-A` from 10:03 to 10:10, enacts `M-Unit-Review-1`, accepts the same-unit report, and records seven minutes of review burden. `W-Disc-1` is performed by the same System in the same containing System from 11:14 to 11:26, enacts the same admitted Method, normalizes the Celsius/Kelvin values before comparison, detects an unresolved mismatch, stops the release decision, and returns the report for correction; it records twelve minutes and one conversion-table lookup. The WorkPlan, two Work occurrences, domain decisions, timing record, and observation account remain separate.

| Later use | Evidence returned | Stop retained |
| --- | --- | --- |
| A.3.1.CC coherence | The two occurrences identify the description edition and the operations actually followed; neither exposed an internal contradiction in this slice. | A.3.1.WT does not conclude that the whole MethodDescription or Method construction is coherent. |
| A.3.1.FT fit or transfer | The matched pair records one changed situation condition and the resulting task observations for one current holder. | One discriminating occurrence establishes no transfer to another holder, domain, tool, or qualification window. |
| C.11.MV practical worth | The domain decisions, seven- and twelve-minute burdens, lookup, and stop are available for comparison with named alternatives. | A task pass establishes neither net worth nor causal contribution. |

If `W-Disc-1` had not occurred, return `missing-performed-work`; if its enacted-Method relation or relied-on capability basis were absent, return that missing premise. A favourable plan, simulated trace, or qualification record cannot replace the occurrence.

