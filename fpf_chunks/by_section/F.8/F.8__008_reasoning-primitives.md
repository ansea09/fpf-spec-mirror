---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:6"
section_title: "Reasoning Primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__008_reasoning-primitives.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:6 — Reasoning Primitives"
line_start: 91843
line_end: 91894
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "A.8"
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
E names one work-facing Role R
  -> use A.2/F.4/F.5 for role-description naming; use A.2.1 for assignment and A.15.1/F.6 for performed Work.
```

```text
E names an episteme-use, status-use, policy-use, source-use, publication-use, or relation-position case
  -> recover the direct pattern before selecting any durable designation.
```

```text
F17Row(Row) and admittedUse(Row,U)
  -> F.8 may reuse Row for U only; not(equivalence) and not(widerUse).
```

```text
DecisionResultEpisteme(R) and entityOfConcern(R,D)
  -> R describes decision occurrence D; not(R = D) and not(recordPerformsDecision(R)).
```

```text
E is a proposed new U-kind
  -> require irreducibility, cross-family recurrence, E.24.UK, and an accepted direct admission basis; F.8 only routes.
```

