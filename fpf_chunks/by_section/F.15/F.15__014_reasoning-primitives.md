---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:12"
section_title: "Reasoning primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__014_reasoning-primitives.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:12 — Reasoning primitives"
line_start: 90782
line_end: 90811
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

### F.15:12 - Reasoning primitives

```text
staticSliceOK(slice)
  only if all triggered SCR rows hold for the current moving parts.
```

Interpretation: F.15 checks only triggered rows. It does not require every possible object slot to be present.

```text
changedSliceOK(slice@t0, slice@t1)
  only if every changed moving part has an RSCR result.
```

Interpretation: a change that matters to context, sense, row, RoleDescription, Bridge, status window, alias, or name must be stated.

```text
failedRule(rule, claim)
  -> direct governing pattern must govern the claim before reuse.
```

Interpretation: a failed Bridge rule is governed by F.9; a failed RoleDescription rule is governed by F.4; a failed status-window rule is governed by F.10; a failed naming rule is governed by F.8, F.17, or F.18.

```text
bridgeAdmitsUse(beta, use)
  -> downstream claim may use beta only at that admitted use.
```

Interpretation: a Bridge may admit naming, explanation, or type-structure use. It does not admit role assignment, work attribution, or evidence use by itself.

