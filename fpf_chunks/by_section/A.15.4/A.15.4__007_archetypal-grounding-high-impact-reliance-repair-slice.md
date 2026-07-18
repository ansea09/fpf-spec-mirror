---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:3.2"
section_title: "Archetypal Grounding - High-Impact Reliance-Repair Slice"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__007_archetypal-grounding-high-impact-reliance-repair-slice.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:3.2 — Archetypal Grounding - High-Impact Reliance-Repair Slice"
line_start: 23903
line_end: 23923
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.16.0"
  - "A.2.1"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.MOVE"
  - "E.17"
  - "E.17.EFP"
  - "U.Work"
keywords:
  - "allowed use now"
  - "appearance overread blocked"
  - "appearance-based reliance"
  - "claim/effect position"
  - "copied approval"
  - "credential view"
  - "dashboard display"
  - "generated explanation"
  - "project-side claim/effect reference"
  - "publication face"
  - "reliance appearance"
  - "required claim before use"
  - "required instituted effect before use"
  - "work or reliance use"
---

### A.15.4:3.2 - Archetypal Grounding - High-Impact Reliance-Repair Slice

A lab manager sees a green tile for `CRISPR-guide-G42 ready` and a copied message saying the edit is approved. `A.15.4` does not ask the manager to decide whether the tile is a good UI. It asks what work or reliance claim is about to be made.

```text
A.15.4 local repair record:
  RelianceAppearanceRef: green guide-readiness tile plus copied approval-looking message
  RelianceAppearanceKind: dashboard display plus copied wording
  WorkOrRelianceUseKind: intended work
  WorkOrRelianceUseRef: proceed with the planned gene-editing work for sample batch B-17
  RequiredClaimBeforeUseRef: current protocol and current lab work plan for batch B-17
  RequiredInstitutedEffectBeforeUseRef: authorization for intervention when carried by an approval act or gate decision
  ClaimOrEffectPatternRef: A.2.9 or A.21 for authorization, A.2.1 for role assignment, A.10 for evidence and currentness, A.15.2 for the work plan
  ClaimOrEffectPositionKind: speech-act ref, gate decision, role-assignment ref, evidence relation, currentness relation, and work-plan record
  ClaimOrEffectPositionRef: positions named by the project records for batch B-17
  ProjectSideClaimOrEffectRef: current protocol publication, approval record or gate record when required, role assignment, evidence relation, currentness relation, and A.15.2 work plan
  AllowedUseNow: source-finding and source-relation refresh; no intervention until the required records and relations are named
  AppearanceOverreadBlocked: tile color and copied message do not authorize biological work or prove safety
  RecoveryOrStopCondition: reopen when the protocol, approval record or gate decision, evidence relation, role assignment, and work plan are current for batch B-17
```

