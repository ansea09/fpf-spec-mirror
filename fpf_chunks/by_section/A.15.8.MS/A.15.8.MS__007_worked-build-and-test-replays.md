---
chunk_kind: "child"
pattern_id: "A.15.8.MS"
pattern_title: "Configure Methodological Support for Work"
section_id: "A.15.8.MS:5"
section_title: "Worked Build and Test Replays"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.8.MS/A.15.8.MS__007_worked-build-and-test-replays.md"
commit_sha: "996ae39ce00b4a9c9b59b48a4f1446b2175dcffb"
heading_path:
  - "A.15.8.MS — Configure Methodological Support for Work"
  - "A.15.8.MS:5 — Worked Build and Test Replays"
line_start: 32225
line_end: 32345
dependencies:
  - "A.15.8"
  - "A.19"
  - "A.3.2.DE"
  - "C.37"
keywords:
---

### A.15.8.MS:5 - Worked Build and Test Replays

#### A.15.8.MS:5.1 - Minimal One-Task Manual Replay

This small constructed replay shows the cheap branch without claiming field evidence. Assume that the named Method and MethodDescription editions are admitted and that the two retrieval occurrences are independently admitted under A.15.1; an actual use must supply those bases rather than inherit them from the example.

`CalibrationEngineer-5` must retrieve the current description of admitted Method `M-Calibrate-Sensor-B` for planned calibration Work. The pass criterion is: return `MD-Calibrate-Sensor-B-v4`, its current status, applicability to sensor family B, and the stop for an unknown serial class. The failure criterion is return of another edition or omission of status, applicability, or stop.

This is one receiver and one exact action. Candidate `REP-Cal-B-Retrieval-1` is a `C.2.1` episteme constituted by the maintained index row. Its exact use claim is that v4 is the current family-B description and carries the unknown-serial stop for this retrieval. It exposes currentness, applicability, the stop, and publication link; it withholds a stable audit digest and makes no capability, permission, authority, Work, or calibration-result claim. The A.15.8.MS task row is the owning domain result for this use and carries the receiving task criterion, observation, and return. That one embedded realization supplies the complete one-result/one-use selection boundary, so the `C.37` direct exit applies: no C.37.MP profile row and no duplicate standalone C.37 account are created. If a later decision relies on the retrieved content as evidence, its exact A.10 path and disposition must be added for that later use.

The initial shared-folder route contains v3 and v4 but exposes neither currentness nor applicability. In `W-ME10-Retrieve-Cal-B-0`, the user retrieves v3; the task returns `task-fail[wrong-edition]` without changing either edition or admitting a capability claim.

| Candidate configuration | Criterion coverage and burden | Disposition |
| --- | --- | --- |
| Rename v4 to “FINAL” and leave both files in the folder | Cheap, but the label supplies no governed currentness relation, applicability, or stop and obscures why v3 remains. | Insufficient for the declared criterion. |
| Add one manually maintained index row naming the Method, v4, currentness basis, family-B applicability, unknown-serial stop, and publication link | Covers every current criterion with one new episteme and no new platform. The folder remains a carrier; the index does not become the Method, publication occurrence, Work, or authority. | Retain as the only currently supported sufficient configuration for this one-task set; this does not exclude the untested portal. |
| Build a search portal with automated recommendations | Could add later functions, but no present criterion requires them and their provider, access, suggestion-use, and authority relations are ungrounded. | Untested and larger than this one-task need; do not claim failure. |

The repair adds only the retained index row and its maintained currentness cue. In `W-ME10-Retrieve-Cal-B-1`, the same user retrieves v4, sees family-B applicability, and stops on an unknown serial class. The receiving task result is `task-pass` for this exact retrieval action, so the use-bounded row disposition is `select` inside the stated v4/family-B window. Return if the source edition, currentness cue, applicability, unknown-serial stop, or task observation changes.

For the bounded set containing only this task, the currently supported set is the singleton containing the index row: the rename route is insufficient by its declared missing features, while the portal remains untested and is not ruled out as logically insufficient. This establishes neither unique sufficiency nor multi-task minimality, Method fit, general user capability, a selected A.22 structure, or worth in another project.

If the maintained index and matching observed retrieval result are already available when this same bounded task is raised, check that the edition, currentness basis, task conditions and acceptable burden still apply, then finish with the adequate route. No portal comparison or new minimality claim is needed. A new audit task, changed stop or defeated currentness cue reopens the affected adequacy question; the next replay shows why.

##### A.15.8.MS:5.1.1 - Configure a Tailoring Aid and Repair Its Failed Check

Extend the constructed calibration setting with a different task: prepare a plan for one named sensor using the permitted choices in the current MethodDescription. This example concerns support for that preparation; it does not report a real calibration or establish its effectiveness. Assume the following domain facts are supplied with the admitted v4 description: the planner may select an approved fixture whose working interval contains the sensor's required interval, but must retain the prescribed test points, acceptance rule, and unknown-serial stop. The current fixture register already establishes approval and intervals; matching numbers alone would not establish approval. The user's assignment, permission and required preparation are also assumed independently established for this bounded planning task.

The input is sensor B-17 with a required interval of 0–10 V, description v4, and two current approved fixture entries: F10 covers 0–10 V and F5 covers 0–5 V. The output criterion is a plan naming B-17, the exact v4 edition and a covering fixture, with the unchanged test points, acceptance rule and serial-class stop. Unknown sensor class, absent approval, incompatible units, or an interval not covered by any available fixture must return the specific missing premise before a plan is released for use. This does not authorize actual calibration.

Configure one local planning worksheet to consume those inputs. Its tailoring rule is explicit: establish sensor class and the register's currentness; check the supplied approval relation and compatible units; require `fixture lower bound <= required lower bound` and `required upper bound <= fixture upper bound`; copy the allowed selection into the plan while retaining v4's fixed operations and stops. Selecting a parameter within these declared options creates a plan for this case; it does not by itself alter reusable Method semantics. If the task needs a new acceptance rule, return to Method design and A.3.1.MV instead of silently editing the template.

In the first constructed planning Work, the worksheet lists both fixtures but checks approval only. The user chooses F5 and obtains a plan labelled ready. The task fails: 5 V does not cover the required upper bound of 10 V. The register and v4 rule are correct, so the repair belongs to the worksheet's omitted interval check. Add that check before export. In a separate repeat of the same task, F5 is rejected with the uncovered 5–10 V interval, F10 is accepted, and the resulting plan retains the prescribed operations and stops. A further changed-input probe with an unknown serial class stops before fixture selection. These are stipulated Work occurrences in the constructed replay; an actual claim needs its own admitted Work and observations.

The receiving result is bounded: the repaired worksheet supports this permitted plan adaptation under the named edition, register and task conditions. The earlier retrieval result alone supplied none of this evidence. A changed fixture register reopens its coverage and currentness premises; a changed tailoring rule reopens the affected plan construction; a failed repeat returns to the defeated worksheet check. Neither the successful preparation nor the worksheet's ready label establishes release authority, general user capability, Method fit, or the result of performing the calibration.

#### A.15.8.MS:5.2 - Two-Task Trade-off with Two Retained Candidates

Extend the constructed case with a second mandatory action. `CalibrationEngineer-5` must retrieve the current description for planned family-B calibration Work. Computational user System `AuditService-2` must use the exact v4 edition in `ReleaseAudit-7` under a stable digest and audit currentness record. These are different receiver/action pairs, so they require different use-bounded claim groups even when one maintained source could realize both. No `AuditService-2` task Work has yet occurred.

The Method-specific problem is now cross-use allocation of complementary governed representation results. The C.37.MP profile branch applies. Each row below embeds the applicable complete `C.37` group and preserves admitted Method `M-Calibrate-Sensor-B` and current A.3.2.DE result `MD-Calibrate-Sensor-B-v4` as its source. The rows select for their own actions; they do not yet constitute the C.37.MP cross-use result or select a support configuration.

| C.37.MP row and exact action | Direct result, exact claim, and reliance | Exposure and loss | Receiving result, disposition, and return |
| --- | --- | --- | --- |
| `MRP-Cal-B-Retrieve-1`: `CalibrationEngineer-5` retrieves material for planned family-B calibration Work. Qualification window: the currentness cue is checked at retrieval and remains usable only for that v4 family-B use through the planned Work. | `REP-Cal-B-Retrieval-1` is the directly governed `C.2.1` index episteme. Exact claim: v4 is current for family B and carries the unknown-serial stop and publication link. A.2.4 classifies the intended status-evidence use. A.10 path `P-Cal-B-Retrieve-v4` carries that currentness/applicability premise with `RelianceDisposition=pass` inside the stated window. | Exposes current edition, family-B applicability, stop, and link; omits the stable audit digest and audit currentness record, which this action does not require. | `task-pass` from `W-ME10-Retrieve-Cal-B-1`; `select` for this retrieval action. Return to A.3.2.DE for changed source claims, `C.2.1` or A.10 for a failed direct result, or this row when the use, window, disposition, or observation changes. Stop if the edition or cue changes, applicability no longer covers family B, or the serial class is unknown. |
| `MRP-Cal-B-Audit-1`: `AuditService-2` uses the exact edition in `ReleaseAudit-7`. Qualification window: at audit start the currentness record must identify v4 and the stable digest must identify the exact v4 bytes used by that audit run. | `REP-Cal-B-Audit-1` is a governed `C.2.1` audit-register episteme tied to a separately identified `E.24.PUB` publication result. Exact claim: the named digest and record bind the audit use to the current v4 edition. A.2.4 classifies the intended audit-evidence use. A.10 path `P-Cal-B-Audit-v4` returns `RelianceDisposition=abstain` until the digest/currentness pair is checked inside the audit window; missing, stale, out-of-window, or mismatched values stop before reliance. | Exposes edition identity, stable digest, and audit currentness record; omits the human applicability explanation and unknown-serial stop, which this action does not consume. Publication does not supply reliance or the task result. | `missing-task-test[AuditService-2]`; no audit task Work exists and no `task-pass` is claimed. The row is `unresolved`, not failed. Return to A.3.2.DE for changed source claims, `C.2.1`, `E.24.PUB`, or A.10 for a failed direct result, or this row when its use, window, stop, task observation, or disposition changes. |

C.37.MP now returns cross-use profile result `MRP-Cal-B-Retrieve-Audit-1` rather than treating row colocation as composition:

| Profile position | Cross-use result |
| --- | --- |
| shared Method source | Both rows return to admitted Method `M-Calibrate-Sensor-B` and current MethodDescription `MD-Calibrate-Sensor-B-v4`. |
| cross-use correspondence | The retrieval currentness cue and the audit digest/currentness pair must designate the same exact v4 edition. Matching the label `v4` is insufficient; a changed edition reopens both rows and this correspondence. |
| conflicting omissions | Retrieval needs family-B applicability and the unknown-serial stop but omits the stable digest. Audit needs the digest and audit-currentness record but omits the human applicability explanation and serial-class branch. Combining the presentations does not erase either omission or prove consistency. |
| edition relations | The retrieval row is qualified for the planned family-B Work window; the audit row is qualified only for the named `ReleaseAudit-7` run after its digest/currentness check. A serial-class change can reopen retrieval alone; a digest mismatch can reopen audit alone. |
| keep-separate decision | `REP-Cal-B-Retrieval-1`, `REP-Cal-B-Audit-1`, their C.37 dispositions, and their receiving task results remain separate. The profile creates no super-representation, common task pass, publication, or support arrangement. |
| profile return | Retain retrieval as `select` and audit as `unresolved`; return `missing-task-test[AuditService-2]` and the unchecked digest/currentness relation. Reopen both rows only when their shared source identity or correspondence changes. |

The configurations below compare how those two governed results and the explicit cross-use relation could be supplied and maintained. `C.37` does not choose among them, and the C.37.MP profile does not rank them; A.15.8.MS retains that configuration decision.

| Candidate configuration | Engineer retrieval row | Audit-service row | Cross-task burden and disposition |
| --- | --- | --- | --- |
| Manual index row only | Observed pass in `W-ME10-Retrieve-Cal-B-1`. | Insufficient: the editable row supplies no stable publication digest or audit currentness record. | Exclude for the two-task mandatory set. |
| One signed read-only register supplies separate retrieval and audit presentations | Untested for the engineer; its declared retrieval presentation can expose applicability and the stop. | Untested for `AuditService-2`; its declared audit presentation can expose the digest and currentness record. | One maintained source for two governed results, but the case lacks approval-latency evidence. Retain. |
| Manual retrieval index plus a signed audit log | The existing retrieval pass remains relevant to the index route. | Untested for `AuditService-2`; its declared design can expose the audit record. | Lower expected retrieval delay but duplicated currentness maintenance and an untested consistency relation. Retain. |

The last two candidates cover the declared features differently, but the case supplies neither audit-task evidence nor a priority between approval latency and duplicated currentness maintenance. The audit profile row therefore remains `unresolved`, the cross-use profile returns its unchecked correspondence and `missing-task-test[AuditService-2]`, and reliance stops; retain both candidates with `unresolved-configuration-choice[approval-latency-vs-duplicate-currentness-maintenance]`. If a receiving decision authorizes a split, name the user/task boundary, currentness owners, and consistency relation; do not call the union globally minimal.

#### A.15.8.MS:5.3 - EC-417 B2 Bounded Task Set and Evidence

The EC-417 B2 material exists, but `TraceReviewer-17`, `SafetyReviewer-17`, and `ReleaseDecider-17` need support for three distinct tasks. The intended task set has the following criteria; its tailoring operation still lacks the [definition needed for reuse](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a158ms531---missing-tailoring-definition):

| Task row | Mandatory pass and stop observations |
| --- | --- |
| retrieval by `TraceReviewer-17` | Recover `MBE-EC417-B2-1`, candidate status, prompt episteme `ATP-2`, confidentiality boundary, and D0 stop. |
| tailoring by `SafetyReviewer-17` | Use the non-confidential fixture, preserve signed-before-closure, reject a stale edition, and stop on missing permission or authority. |
| branch selection by `ReleaseDecider-17` | Distinguish A, B2, and R and stop when assignment, permission, authority, confidentiality, or reversibility is absent. |

The receiving relations remain direct: `TraceReviewer-17` retrieves the edition and prompt episteme for trace-review preparation; `SafetyReviewer-17` uses the tailoring aid in named tailoring Work; `ReleaseDecider-17` uses the selection aid in named branch-selection Work. None is release Work or the release decision.

| Candidate configuration | Evidence against the same three rows | Disposition for this case |
| --- | --- | --- |
| Published files and manual lookup only | The case supplies no performed task evidence for current status, `ATP-2`, D0, stale-edition rejection, signed-before-closure, or A/B2/R stops through this route. | Untested. Do not call it failed or insufficient from absent task evidence alone. |
| Bounded PLM retrieval and selection aids plus the non-confidential CI tailoring fixture | Retrieval and branch-selection pass their declared checks through the identified PLM and CI Systems. Tailoring observations cover the fixture, signed-before-closure and stale-edition rejection, but not the permission/authority stop. | Supported for the observed actions; The missing tailoring definition and `missing-task-test[tailoring-permission-authority-stop]` prevent a pass for the complete three-task set. No claim of global minimality or parity superiority. |
| Add an AI-provider route and feedback path | The case supplies no AI-provider interaction, used suggestion, review of such a suggestion, feedback Work, or feedback receiving use. No mandatory row currently requires this branch. | Outside the supported pass and untested; retain as named gaps, not features. |

The configured PLM/CI route includes the Method Base edition and status cues, PLM retrieval and branch-selection aids, the CI fixture and stale-edition rejection, `ATP-2`, and the confidentiality, signed-evidence, assignment, permission, authority, reversibility, and D0 stops. The manual and AI routes lack parity evidence, so this table does not select the globally smallest arrangement. It identifies the only configuration with performed observations across all three tasks; the missing tailoring definition and tailoring-stop test still prevent complete task-set support. It is not an A.22 selected structure.

##### A.15.8.MS:5.3.1 - Missing Tailoring Definition

The case names tailoring aid `TAIL-EC417-B2-1` and Work `W-MESUP-EC417-Tailor-1`, but does not identify the object and edition to adapt, the alteration or selection performed, or the resulting tailored object. The fixture and guard observations below do not recover those missing values. The method engineer configuring this support task must recover them before offering it as a repeatable tailoring instruction or claiming tailoring coverage. Until then, return `missing-task-set[tailoring-input-action-result]` and retain only the described CI-use, signed-before-closure and stale-edition observations. This missing definition is separate from the untested permission/authority stop; neither gap turns the admitted Work into a performed failure.

#### A.15.8.MS:5.4 - Three Performed Tasks and Their Bounded Reach

| User Work | System interaction and observed result | Result boundary |
| --- | --- | --- |
| `W-MESUP-EC417-Retrieve-1` by `TraceReviewer-17` | The user retrieves `MBE-EC417-B2-1` through `SYS-EC417-PLM-1` and recovers candidate status, `ATP-2`, the confidentiality boundary, and the D0 stop. The local `SupportSystemUsedInWork@EC417` occurrence obtains for that Work-System pair and interaction interval. | The result establishes this retrieval task only; it creates no general access entitlement, capability, or authority. |
| `W-MESUP-EC417-Tailor-1` by `SafetyReviewer-17` | The user applies the tailoring aid with a non-confidential `SYS-EC417-CI-1` fixture, recovers signed-before-closure, and rejects the stale edition. Its separate direct System-use occurrence obtains. | The result establishes these observations only; the [tailoring operation remains undefined](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a158ms531---missing-tailoring-definition), and stopping on missing permission or authority remains untested. It neither performs release Work nor approves closure. |
| `W-MESUP-EC417-Select-1` by `ReleaseDecider-17` | The user applies the selection aid through `SYS-EC417-PLM-1` to distinguish pre-entry A, bounded B2, and post-entry R and stops B2 when a named assignment, permission, authority, confidentiality, or reversibility condition is absent. Its separate direct System-use occurrence obtains. | The result establishes this bounded selection task only; the tool does not make the release decision or acquire authority. |

`RES-MESUP-EC417-B2-1` returns `task-pass` for retrieval and branch selection. It retains the observed tailoring fixture, signed-before-closure and stale-edition results, but returns `missing-task-set[tailoring-input-action-result]` and the separate `missing-task-test[tailoring-permission-authority-stop]` for the full tailoring task. The other user's branch-selection stop does not fill that gap. No AI-provider interaction, used AI suggestion, review of such a suggestion, feedback SpeechAct, or feedback receiving use is part of that pass. Retrieving `ATP-2` is not provider use.

No repair and rerun occurrence is asserted for EC-417: no performed task is reported as failed, and an untested tailoring stop is not a performed failure. If a later task fails, apply step 12 and add its Work and rerun rather than rewriting these histories. The minimal one-task replay supplies the filled failure-repair-rerun branch; the two-task extension supplies the unresolved-trade-off branch.

#### A.15.8.MS:5.5 - Proposed Organization, Not a Selected Structure

`PSO-EC417-B2-Use-1` is a case-local proposal designator. Its four candidate A.22 groups remain disjoint:

1. the identified collection, entries, edition, aids, prompt episteme, Systems, and three Work occurrences;
2. two instituted entry-membership occurrences and the three direct PLM and CI System-use occurrences;
3. current-edition, status, confidentiality, signed-before-closure, assignment, permission, authority, reversibility, and D0 constraints; and
4. the use frame for retrieval, comparison, tailoring, and bounded PLM and CI use for `WP-EC417-B2-Trial-1`.

The case supplies no selecting System, enacted selection Method, dated structure-selection Work, or direct participation or operation-binding facts. `ESA-EC417-B2-1` returns `missing-selection-basis` and designates no selected `U.Structure`. This gap does not erase the three task observations.

#### A.15.8.MS:5.6 - Collection and Edition Remain Subordinate Results

`MBC-EC417-B2-1` identifies the project collection and its entry-disposition rule. Two admitted curator Work occurrences, their permissions and operation applications, positive result bindings, and identified `MethodBaseEntryBelongsTo@Project` predicates establish membership for the candidate-account and WorkPlan epistemes. The collection, membership episodes, assertion or evidence accounts, optional construction account, edition, publication occurrence, and named-use reliance episteme remain separate results.

Those facts make the named material eligible for the three user tasks; they do not show that the tasks succeeded. Conversely, the bounded task results do not prove general capability, select the proposed structure, admit `C-EC-Release-v2` as a Method, perform release Work, or establish Method fit or effectiveness.

