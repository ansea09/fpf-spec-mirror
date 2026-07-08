---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:7"
section_title: "Unification conformance record"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__009_unification-conformance-record.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:7 — Unification conformance record"
line_start: 86012
line_end: 86037
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.Role"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:7 - Unification conformance record

Use this record when several moving parts are being checked together.

```text
UnificationConformanceRecord:
  SliceRef:
  BoundedContextRefs:
  ContextEditionRefs:
  SenseCellRefs:
  ConceptSetRowRefs:
  RoleDescriptionRefs:
  BridgeCardRefs:
  StatusFamilyOrWindowRefs:
  AliasRefs:
  CandidateNameOrRowDecisions:
  StaticRuleResults:
  RegressionRuleResults:
  Witnesses:
  NonAdmittedUses:
  DirectGoverningPatternRefs:
  ReopenTrigger:
```

`StaticRuleResults` and `RegressionRuleResults` name only the checks that matter for the current slice. `NonAdmittedUses` names the tempting claim that the slice does not permit, such as direct role assignment, performed-work attribution, evidence use, source authority, publication authority, status transfer, or bridge-based equivalence.

