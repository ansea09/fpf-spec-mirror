---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:9"
section_title: "Reasoning primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__010_reasoning-primitives.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:9 — Reasoning primitives"
line_start: 76617
line_end: 76653
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

### F.14:9 - Reasoning primitives

```text
candidateName(e) and recoveredValue(e, v)
  -> name decision must be made for v, not for e as a string.
```

Interpretation: the expression is a cue. The recovered value governs the naming decision.

```text
roleBundleExpression(R1, R2, C)
  -> not(newRoleValue(R1R2)).
```

Interpretation: a bundle expression may be named as an expression, but it does not mint a fused `U.Role`.

```text
roleIncompatibility(R1, R2, C, W)
  -> assignment check must consider holder and overlapping window.
```

Interpretation: separation questions need A.2.1 and F.6 checks, not prestige names.

```text
statusVariant(S, windowOrValue)
  -> keep status family S unless F.10 recovers a new family.
```

Interpretation: status values and windows do not multiply status families by default.

```text
qualifier(q) governedBy(P)
  -> q may constrain a name only after P recovers the qualifier value.
```

Interpretation: capability, method, work, evidence, source, publication, policy, and assurance qualifiers must not hide inside role or status names.

