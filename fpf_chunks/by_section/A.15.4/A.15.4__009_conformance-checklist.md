---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:4"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__009_conformance-checklist.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:4 — Conformance Checklist"
line_start: 23930
line_end: 23937
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

### A.15.4:4 - Conformance Checklist

| ID | Requirement (Normative Predicate) | Purpose and Rationale |
| :--- | :--- | :--- |
| **CC-A15.4-1 (Work-relevant appearance-based reliance repair)** | Before an authority-looking case guides work or reliance, a conforming `A.15.4` use produces the ordinary local repair record: `RelianceAppearanceRef`, `RelianceAppearanceKind`, `WorkOrRelianceUseKind`, `WorkOrRelianceUseRef`, `RequiredClaimBeforeUseRef`, `RequiredInstitutedEffectBeforeUseRef`, `ClaimOrEffectPatternRef`, `ClaimOrEffectPositionKind`, `ClaimOrEffectPositionRef`, `ProjectSideClaimOrEffectRef`, `AllowedUseNow`, `AppearanceOverreadBlocked`, and `RecoveryOrStopCondition`. The record names the governing pattern and governing position that carry the requested claim or instituted effect; if that value is absent or stale, the disposition is limited to orientation, source-finding, contested use, governing-position repair request, bounded reversible probe, or blocked unsupported claim. | Prevents appearance-based reliance while keeping ordinary use cheap. |
| **CC-A15.4-2 (P2W publication use boundary)** | A principle scheme, functional diagram, scenario, screen, or explanation that exposes a P2W chain guides only the `A.15` work or planning kind selected by the project use: method-family selection, selected method, `U.WorkPlan`, dated `U.Work`, work-result record, or result measurement. Claims outside that selected use require their own governing pattern position or source relation named by value. | Keeps P2W publication use tied to the work use under repair instead of turning publication form into project authority. |
| **CC-A15.4-3 (Lowering and refresh)** | When the governing pattern, governing pattern position, source-currentness relation, revocation relation, affected work target, relying context, or time window cannot be recovered, the disposition for the work or reliance claim is orientation, source-finding, contested use, bounded reversible probe, repair request, or blocked unsupported claim. The record states the return or refresh condition for changes to source currentness, revocation, governing decision, evidence relation, role-state register, credential-status register, context-state record, copied-source relation, generated-source relation, or publication relation. | Keeps A.15.4 useful without admitting source as a new kind. |

