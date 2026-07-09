---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:6"
section_title: "Reasoning Primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__008_reasoning-primitives.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:6 — Reasoning Primitives"
line_start: 84443
line_end: 84474
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
Candidate expression E has no recovered kind or relation
  -> do not mint; run E.10 or direct precision restoration first.
```

```text
E names one local sense in context C
  -> reuse local label in C unless durable public use is current.
```

```text
E names one work-facing Role R in context C
  -> use F.4 and F.5 for RoleDescription naming; use A.2.1 for assignment.
```

```text
E names an episteme-use, status-use, policy-use, source-use, or relation-position case
  -> recover the direct pattern before any durable name is selected.
```

```text
E needs cross-context reuse
  -> use F.9 bridge plus F.7 row; F.8 only consumes the admitted row use.
```

```text
E is a proposed new U-kind
  -> require irreducibility, cross-family recurrence, and an accepted decision record.
```

