---
chunk_kind: "child"
pattern_id: "B.1.5.CM"
pattern_title: "Construct and Qualify a Composite Method"
section_id: "B.1.5.CM:5"
section_title: "Archetypal Grounding — C-EC-Release-v2"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.CM/B.1.5.CM__007_archetypal-grounding-c-ec-release-v2.md"
commit_sha: "fcd12ecc699c236021602dde85b5daf345e17c0b"
heading_path:
  - "B.1.5.CM — Construct and Qualify a Composite Method"
  - "B.1.5.CM:5 — Archetypal Grounding — C-EC-Release-v2"
line_start: 43535
line_end: 43581
dependencies:
  - "A.3.1"
  - "B.1.5"
  - "B.1.5.EW"
  - "C.32.MWA.PP"
keywords:
---

### B.1.5.CM:5 - Archetypal Grounding — `C-EC-Release-v2`

The EC-417 project proposes `C-EC-Release-v2` as a whole for safety-relevant release coordination.

Under A, the team waits for signed supplier evidence before integrating the software. Under B2, it integrates from a versioned provisional edition, reconciles it with signed evidence before safety closure, and assigns most preparation of the changes between the editions to the supplier-configuration role to keep the safety engineer within the peak limit. [C.32.MWA.PP §5.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwapp53---possible-future-alternatives-a-b-and-b2) gives the timing and capacity comparison. A is selected before integration; recovery R is used when closure fails after early B2 integration.

The proposed account states:

| Whole position | Proposed content |
| --- | --- |
| intended result | a release-authorizable evidence and integration state for one safety-relevant change |
| situation family | internal or supplier-originated hardware/software changes with versioned provisional or signed pinout evidence |
| invariant | provisional evidence may support reversible early integration, but signed evidence and repeated checks are required before safety closure and release authorization |
| participants | identified `M-HW-Verify`, `M-SW-Integrate`, `M-Supplier-Approve`, and `M-Release-Authorize`; candidate reconciliation accounts remain separate |
| permitted variation | pre-entry A when signed evidence or B2 entry conditions differ; B2 for bounded early integration; post-entry recovery R after a failed B2 closure |
| bounds and stops | confidentiality, human authority, `D-8` safety peak at or below `0.40`, signed evidence before closure, and reversibility until `D-1` |
| reidentification | preserve the intended result, invariant, participant-status boundary, evidence-version guard, authority, and A/B2/R branch meanings |

The four participant Methods are identified, but the proposed whole is not. Their co-use and the proposed order do not establish that they are Method parts. The relation sets therefore remain proposed:

- provisional-evidence integration at `D-21` and signed-evidence reconciliation at `D-8`;
- signed evidence and accepted safety result before release authorization;
- supplier preparation responsibility for `1.60 h` under B2;
- separate safety and release authority;
- PLM, rig, and provider-access conditions; and
- description correspondences from evidence version through integration bundle and verification result.

For this selected trial, B.1.5.CM returns a prospective candidate account with a WorkPlan covering at most three B2 releases. The whole and relation claims remain proposed.

Before each entry, `SafetyReviewer-17` performs `W-SafetyEvidenceDecision-17` under `ASG-SafetyReview-17` and `AUTH-SafetyEvidence-17` to accept or reject the named evidence conditions; `ReleaseDecider-17` then performs `W-ReleaseDecision-17` under `ASG-ReleaseDecision-17` and `AUTH-ReleaseDecision-17` to decide branch entry and release, withhold, or next-slot disposition. Neither decision or authority relation substitutes for the other.

In B2, `TraceReviewer-17` accepts or rejects each AI trace suggestion used by the release branch under `ASG-TraceReview-17` and `PERM-TraceAcceptReject-17`. [The full EC-417 application, §16.9.5](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#fpfreference1695---5-build-the-repertoire-and-criteria-without-preselecting-an-architecture) records the one permission grant and the dated Work `W-TraceAcceptReject-17-01` that returns acceptance in the filled case. The separate relation `PEX-TraceAcceptReject-17-01` connects that dated Work to the permission it exercised. `EV-PEX-TraceAcceptReject-17-01` supplies evidence about this exercise. Each additional used suggestion requires its own dated decision Work and result, confirmation that the permission applies at that time, and its own Work-to-permission exercise relation.

Missing signed evidence after early integration triggers recovery R. In R, preserve the performed-integration record and evidence history. Repeat the evidence comparison and affected verification when evidence arrives by `D0` while the existing evidence and reversibility guards still hold. Record whether early integration is retained, rolled back, or repeated, and the added burden. If closure remains unresolved at `D0`, the release result is withhold/next-slot and this R occurrence ends as a failed B2 trial.

`ASG-TraceReview-17` and `PERM-TraceAcceptReject-17` also end at `D0`; continuing safety or release relations extend neither. The trial WorkPlan therefore contains no post-`D0` AI suggestion, trace-review Work, assignment, permission, result, or exercise, and claims no other later Work. Unresolved R may motivate later planning, but this case asserts no post-`D0` recovery WorkPlan, PlanItem, planned endpoints, qualification/currentness result, readiness, assignment, permission/authority, or later Work.

When later non-AI recovery needs coordination, the project may create a new `A.15.2` WorkPlan; `A.15.2` itself does not require planning before every otherwise valid later Work. Planned or unplanned Work would still need its separate qualification/currentness, readiness, assignment, permission/authority, and `A.15.1` occurrence as applicable. These stops preserve all earlier Work and evidence history. A is only a pre-entry alternative.

Acceptance observations include whether each trial respects confidentiality and authority, remains below the `D-8` capacity bound, preserves evidence/version correspondence, and reaches a truthful release or recovery result by `D0`. An attempted post-`D0` AI-supported continuation, or an assertion of later Work without a separately admitted `A.15.1` dated Work occurrence, is an explicit stop and failed trial observation. The withhold/next-slot result preserves earlier Work and may motivate planning; it creates neither a recovery WorkPlan nor later Work. Those observations may support, narrow, split, or reject the account. They do not by themselves identify the whole; `A.3.1` remains the identity owner.

#### B.1.5.CM:5.1 - Finish a Design Comparison Before a Trial Is Available

Suppose an earlier design use asks whether this release-coordination proposal preserves signed-before-closure, confidentiality and the A/B2/R distinctions well enough to compare with another proposal. The current sources support that account, but whole identity and composition relations remain unresolved, and the team has no rig access, allocated effort or trial window. Return the traceable prospective account with those identity and relation limits. The receiving designer can compare the proposals and finish that question on the available content.

A later opportunity with useful obtainable observations can warrant implementation or a trial and its coordination plan. The already selected three-release case above retains its WorkPlan, observations and stops.

