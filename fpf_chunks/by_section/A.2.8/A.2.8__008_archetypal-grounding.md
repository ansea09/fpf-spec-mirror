---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Relation)"
section_id: "A.2.8:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__008_archetypal-grounding.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Relation)"
  - "A.2.8:5 — Archetypal Grounding"
line_start: 6881
line_end: 6911
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.RCD"
  - "A.7"
  - "C.3"
  - "F.6"
keywords:
  - "actual bearer"
  - "constitutive rule"
  - "do not identify an individual bearer or institute a duty. Adapt"
  - "individual duty"
  - "instituting basis"
  - "obligation"
  - "prohibition"
  - "recommendation-as-duty"
  - "validity interval"
---

### A.2.8:5 - Archetypal Grounding

#### A.2.8:5.1 - Incident Response

Current `IncidentResponsePolicy-2026` says that systems assigned to `ProviderSystemRole` are subject to a four-hour incident-response prescription. That policy and its kind reference remain generic content.

`OpsTeamProviderAssignment-2026` is an assignment occurrence with admitted System `OpsTeam` as holder; its species is declared under `U.SystemRoleAssignment`. If the policy contains the holder-application rule, speech act `SA-Issue-IncidentDuty-2026 : U.SpeechAct` is the policy-recognized instituting Work, and the predicate is satisfied, then `IncidentResponseCommitment-2026 : U.Commitment` obtains with `OpsTeam` as duty bearer. Its modality is `MUST`; its referents include `SVC-SLO-RESP-4H` and the Sev-1 applicability claim; its scope is `IncidentManagement`; and its validity window is the interval established by the rule.

The commitment assertion may cite `E-SLO-RESP-1`, incident tickets, timestamps, and the selected clock source for adjudication. Those values make reliance testable; `SA-Issue-IncidentDuty-2026` remains the policy-recognized instituting Work.

If `OpsTeamProviderAssignment-2026` ends and `RecoveryTeamProviderAssignment-2026` begins, apply the constitutive rule's continuity conditions. When the rule ties duty continuity to the assignment, the OpsTeam commitment ends and a RecoveryTeam commitment begins only after its own required basis and facts obtain. If the rule instead preserves the duty for the same system across a replacement assignment, the continuity decision says so. A different bearer always means another occurrence. Likewise, a second policy-recognized act reissuing the same uninterrupted duty identifies another commitment only when the constitutive rule makes that instituting basis identity-bearing; otherwise the new act is a new ground or record for the continuing occurrence.

A policy-recognized speech act can also institute `ShutdownNoticeCommitment-7` directly for admitted system `PlantController-7`.

`IncidentResponseCommitment-2026` can obtain while no incident-ownership responsibility relation exists. Conversely, an admitted `MaintenanceActionResponsibilityRelation@Plant` can obtain while no `U.Commitment` obtains. Both can obtain for the same system and interval only as separately identified relations with separate predicates, participants, bases, and occurrence identities.

If the corpus lacks the constitutive rule or the required instituting-relation predicate, return `missing-governor[individual commitment institution]`. If the available facts establish that the rule's required instituting act did not occur, `IncidentResponseCommitment-2026` does not obtain under §4.2. If deciding evidence is unavailable, reliance on the commitment assertion is `unknown`. A speech act, assignment, policy publication, or D-claim supplies only the facts it actually establishes.

#### A.2.8:5.2 - Protocol Rule

A protocol description says: “Participants MUST follow the state machine; invalid traces are rejected; traces are retained for audit.” Recover separate claims:

- L-claims define the state machine and its safety or progress properties;
- A-claims define which runtime traces are admissible;
- one generic normative claim states the participant prescription;
- one actual `U.Commitment` is asserted only for an admitted bearer after an applicable constitutive rule and its required basis obtain;
- the duty referents cite the state-machine, admissibility, and trace-retention content by exact identifiers; and
- evidence claims and trace carriers support later adjudication.

A `ParticipantImplementerSystemRole` reference in the policy names a kind. Identify the actual bearer and apply the constitutive rule with its required basis before asserting the individual commitment.

