---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Relation)"
section_id: "A.2.8:6"
section_title: "Invariants and Reasoning Primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__009_invariants-and-reasoning-primitives.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Relation)"
  - "A.2.8:6 — Invariants and Reasoning Primitives"
line_start: 6905
line_end: 6932
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.RCD"
  - "A.7"
  - "C.3"
  - "F.6"
keywords:
  - "actual bearer"
  - "constitutive rule"
  - "do not identify an individual bearer or institute a duty. Adapt"
  - "individual duty"
  - "instituting basis"
  - "obligation"
  - "prohibition"
  - "recommendation-as-duty"
  - "validity interval"
---

### A.2.8:6 - Invariants and Reasoning Primitives

1. Every positive `U.Commitment` has one actual system or party as duty bearer.
2. A system-role kind or assignment can be a rule ground but never the duty bearer.
3. Generic normative content, individual relation, and describing assertion remain separate.
4. The direct predicate includes an applicable constitutive rule and the actual basis that rule requires.
5. Modality, scope, validity, and referents are explicit.
6. Missing evidence makes reliance unresolved; it does not invent or negate the relation.
7. Assignment turnover does not transfer a duty automatically.
8. Responsibility, permission, authority, access, Work, result, and compliance remain separately governed.
9. Compatible record correction does not decide world-side continuity.
10. A Bridge or similar wording in another context creates no local commitment.

```text
applicable current policy and exact constitutive rule
  and admitted actual bearer and referents
  and required instituting basis and facts obtain
  and modality, scope, validity, and continuation conditions hold
  and no defeat, revocation, expiry, or supersession applies
  -> one U.Commitment occurrence obtains.
```

```text
policy mentions one system-role kind
  or one system-role assignment obtains
  -> no individual U.Commitment follows without the exact rule, bearer, and basis.
```

