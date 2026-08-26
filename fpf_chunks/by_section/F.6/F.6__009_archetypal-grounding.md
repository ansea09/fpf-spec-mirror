---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:7"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__009_archetypal-grounding.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:7 — Archetypal Grounding"
line_start: 91817
line_end: 91861
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3"
  - "A.6.9"
  - "A.6.REL"
  - "C.3.3"
  - "E.10.ROLE"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
keywords:
  - "Work attribution"
  - "exact assignment occurrence"
  - "holder equality"
  - "performedUnderAssignment"
  - "performer System"
  - "separate evidence"
  - "temporal coverage"
---

### F.6:7 - Archetypal Grounding

#### F.6:7.1 - Robot Inspection

`MaintenanceInspectionAssignment` is a declared species under `U.SystemRoleAssignment`. Its participants include a `HolderSystemSlot` for the assigned System and a local `AssignedSystemRoleKindSlot` whose value is an `InspectorSystemRole`. Its rule applies within the Plant A maintenance scheme and says that the fixed holder is assigned under that kind to supply the inspection contribution; one occurrence is the maximal uninterrupted interval for which that rule stays true for the same participants.

```text
InspectionAssignment-17 : MaintenanceInspectionAssignment
  HolderSystemSlot: Robot-7
  AssignedSystemRoleKindSlot: InspectorSystemRole
  predicateTrueInterval: [2026-07-13T09:00, 2026-07-13T17:00]

InspectionWork-17 was performed under InspectionAssignment-17.
```

The case basis directly links that Work to that assignment; the matching holder and interval only confirm necessary conditions. Robot-7 is the actor. Separately, the inspection Work enacts `TurbineInspection@Maintenance-2026` as its Method. `InspectorSystemRole`, a sensor capability, algorithm-possession wording, the Method, and `TurbineInspectionProcedure-v3` do not perform the inspection. Use A.3.2 to decide whether that last episteme is a MethodDescription. Calibration state, Method adequacy, report quality, and acceptance remain separate.

#### F.6:7.2 - Two Review Commissions

`ProjectReviewAppointmentAssignment` is a declared species. It declares three participant positions: `HolderSystemSlot`, local assigned kind, and `ReviewCommissionSlot`. `ReviewAssignment-A` and `ReviewAssignment-B` are two occurrences with Alice and `ReviewerSystemRole` in common but different commissions, and both cover the same interval. The case says that Alice performed `ReviewWork-A` under assignment A and `ReviewWork-B` under assignment B; it does not establish either crossed pairing. If the facts say only that Alice performed review Work while both appointments covered the interval, leave the attribution unresolved. The readable projection “Alice is reviewer” selects neither assignment and creates no generic assignment.

#### F.6:7.3 - Reviewer and Review Report

`CommissionReviewAssignment` is a declared species. It declares three participant positions: holder, local reviewer kind, and commission. Its rule applies to admitted review commissions and says that the fixed holder is appointed under the identified commission to supply the review contribution; one occurrence is the maximal uninterrupted interval for which that rule stays true. `ReviewAssignment-82` is its occurrence for Alice and `Commission-82`, and it covers `ReviewWork-82`. The case identifies this as the assignment under which Alice performed that Work. `ReviewReport-82` is a separate `U.Episteme`; it may state the attribution, and evidence may support reliance on that statement, but neither creates the Work–assignment fact. Use A.15.PROD only for a current report-inception claim. The report is neither the performer nor the attribution.

#### F.6:7.4 - Standard Used during Safety Work

A safety MethodDescription cites a standard, and source prose says that the standard has a “normative role”. Do not create an assignment for the standard. The standard remains an episteme in the external-rule, source-use, specification-use, or evidence relation selected by the claim.

A safety engineer or tool System can separately hold a covering safety-analysis assignment and perform dated safety Work. Attribution names the assignment occurrence and the case fact linking it to the Work; it does not use the standard as performer.

#### F.6:7.5 - Access Label and Approval Work

An access directory says Alice has `DB-Admin`. That entry describes an access or policy relation under its own scheme; it is not automatically an `ApproverSystemRole` assignment.

`ApprovalCommissionAssignment` is a declared species. It declares three participant positions: holder, local approver kind, and `ApprovalScopeSlot`. Its rule applies to admitted release scopes and says that the fixed holder is commissioned to supply approval within the identified scope; one occurrence is the maximal uninterrupted interval for which that rule stays true. `ApprovalAssignment-481` is its occurrence for Alice and the current release scope. If it covers `ApprovalWork-481` and the case identifies it as the assignment under which Alice performed that Work, the attribution is grounded. The directory entry may support a separate authorization claim but cannot substitute for the assignment or its link to the Work.

#### F.6:7.6 - Distributed Performers and Child Work

`ReviewTeam-9` and `Alice`, both admitted as `U.System`, perform `JointReviewWork-9`. `TeamReviewAssignment-9` covers the team; `MemberReviewAssignment-A9` covers Alice. The case establishes one F.6 attribution for each performer and assignment. Neither assignment can stand for the other performer. If `AliceFindingCheckWork-9` is separately admitted as child Work, it keeps Alice as performer, its own covering assignment and F.6 attribution, and its Work-part relation to `JointReviewWork-9`.

#### F.6:7.7 - Passive Test Article

`TestArticle-7`, admitted as a `U.System`, holds `TestSubjectAssignment-7` throughout `ValidationWork-7`. `ValidationRig-2`, also admitted as a `U.System`, actually performs the Work under its own `ValidationPerformerAssignment-7`; only that Work-attribution link is established. The test article's assignment and presence during the interval do not make it a performer. If the project needs to say that the article participated passively in the validation, use the domain rule that defines that participation; while no such rule is current, return the A.6.RCD `missing-governor` result rather than treating the assignment as participation.

