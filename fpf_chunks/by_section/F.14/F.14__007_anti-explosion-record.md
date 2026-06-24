---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:6"
section_title: "Anti-explosion record"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__007_anti-explosion-record.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:6 — Anti-explosion record"
line_start: 82106
line_end: 82129
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
  - "E.17"
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

### F.14:6 - Anti-explosion record

Use this record when more than one related candidate name is under pressure.

```text
AntiExplosionControlRecord:
  BoundedContextRef:
  CandidateNameFamily:
  CandidateExpressionRefs:
  RecoveredValues:
  ExistingValueOrRowRefs:
  RoleRelationStructureRefs:
  AssignmentOrWorkRefs:
  StatusFamilyOrWindowRefs:
  QualifierOrDirectPatternRefs:
  BridgeOrPublicTermRefs:
  BlockedMinting:
  DurableNamingRefs:
  RemainingLocalAliases:
  ReopenTrigger:
```

`RecoveredValues` is the center of the record. Each candidate expression is mapped to the value or relation it is trying to name. If no typed value is recovered, the expression stays local or goes to F.8 for a mint-or-reuse decision. `DurableNamingRefs` cites F.5, F.17, or F.18 only after the relevant value is recovered.

