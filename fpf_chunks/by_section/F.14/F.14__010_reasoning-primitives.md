---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:9"
section_title: "Reasoning primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__010_reasoning-primitives.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:9 — Reasoning primitives"
line_start: 95931
line_end: 95964
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
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
  - "NameCard"
  - "assignment"
  - "designation"
  - "evidence use"
  - "permission"
  - "reuse"
  - "status names"
  - "system-role names"
  - "term row"
  - "vocabulary explosion"
---

### F.14:9 - Reasoning primitives

```text
candidateExpression(e) and recoveredGovernedValue(e, v) and proposedUse(u)
  -> choose a naming disposition for <v,u>, not an ontology for string e.
```

```text
existingDesignationOrLocalExpression(v, u) is sufficient
  -> stop; do not mint NameCard, SenseCell, row, or name family.
```

```text
systemRoleKindBundleRelation(K1, K2) obtains
  -> not(newSystemRoleKind(K1K2)).
```

```text
statusVariant(S, windowOrValue)
  -> keep status family S unless the pattern that defines the status claim establishes a different family.
```

```text
differentLocalSenseProjections(c1, c2)
  -> test F.9 only for a named correspondence use; not(Bridge(c1,c2)) by difference alone.
```

```text
namingObjectPresent(x)
  -> not(governedValueExists) and not(nextNamingObjectRequired).
```

These are stopping and dispatch rules. They create no values or relation occurrences.

