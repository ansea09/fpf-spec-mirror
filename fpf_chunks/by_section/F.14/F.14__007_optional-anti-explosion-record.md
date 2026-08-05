---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:6"
section_title: "Optional anti-explosion record"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__007_optional-anti-explosion-record.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:6 — Optional anti-explosion record"
line_start: 94400
line_end: 94429
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.24.PUB"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:6 - Optional anti-explosion record

Ordinary use needs no record: recover the value, choose the lightest sufficient disposition, and stop. Persist this C.2.1 description episteme only when several related candidates, a contested decision, or later replay makes the family-level reasoning useful.

```text
AntiExplosionControlRecord:
  CandidateNameFamily:
  ProposedNamingUse:
  EffectiveNamingReferenceScheme:
  CandidateExpressionRefs:
  RecoveredGovernedValueRefs:
  GovernedValueKindRefs:
  DirectGoverningPatternRefs:
  ExistingDesignationOrAliasRefs:
  LocalSenseRefsOrCellRefs?:
  LocalSenseBasisRelationRefs?:
  ModelUseStructureRef?: only when an independently selected structure changes this use
  ExactRoleRelationRefs?:
  AssignmentOrWorkRefs?:
  StatusFamilyOrWindowRefs?:
  QualifierOrDirectPatternRefs?:
  ActualBridgeRefs?:
  BlockedMinting:
  DurableNamingRefs?:
  RemainingLocalExpressions:
  ReopenTrigger:
```

The record describes the control result. It creates no governed value, naming decision occurrence, designation, local sense, Bridge, row, publication, evidence, role, status, or Work. A field is omitted when its object is not independently current; filling the record is never a completeness goal.

