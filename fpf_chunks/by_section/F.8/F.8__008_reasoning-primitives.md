---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:6"
section_title: "Reasoning Primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__008_reasoning-primitives.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:6 — Reasoning Primitives"
line_start: 93174
line_end: 93221
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RCD"
  - "A.7"
  - "A.8"
  - "C.11"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "decision lattice"
  - "minting new U-kinds"
  - "parsimony"
  - "reuse"
  - "role-shaped names"
  - "type explosion"
---

### F.8:6 - Reasoning Primitives

```text
candidateExpression(E) and not(independentlyRecoveredGovernedValueOrRelation(V))
  -> stop F.8; run E.10 or the direct subject pattern before naming.
```

```text
candidateExpression(E) and governedValueOrRelation(V) and directPattern(P) and proposedUse(U)
  -> choose the lightest naming disposition for <V,U>; not(establish(V)) and not(makeObtain(V)).
```

```text
existingDesignationOrLocalPhrase(V, U) is sufficient
  -> reuse or stay local; do not mint a cell, NameCard, row, identifier, or U-kind candidate.
```

```text
alias(E2, designation(E1,V))
  -> preserve kind(V), scope(V), occurrenceIdentity(V), admittedUse(V), and lineage(E1,E2).
```

```text
localSense(E, ReferenceScheme S, LocalSenseClaim L)
  -> not(crossLocalSameness) and not(Bridge) without an independently obtaining F.9 relation.
```

```text
E names one local system-role kind K
  -> use A.2/F.4/F.5 for system-role-kind-description naming; use A.2.1 for `U.SystemRoleAssignment` and A.15.1/F.6 for performed Work.
```

```text
E names an episteme-use, status-use, policy-use, source-use, publication-use, or relation-position case
  -> recover the direct pattern before selecting any durable designation.
```

```text
F17Row(Row) and admittedUse(Row,U)
  -> F.8 may reuse Row for U only; not(equivalence) and not(widerUse).
```

**Decision-occurrence check.** A decision-result episteme describes an occurrence; it does not perform the decision. Before accepting its `EntityOfConcernRef`, resolve the direct decision or choice pattern, admitted predicate, actual participants, applicability, and occurrence identity. If any of those are unavailable, return the exact `missing-governor` result and do not mint an occurrence identifier. Keep a C.11 `ChoiceResult` and any dated decision-making Work as separate objects under their own patterns.
```text
E is a proposed new U-kind
  -> require irreducibility, cross-family recurrence, E.24.UK, and an accepted direct admission basis; F.8 only routes.
```

