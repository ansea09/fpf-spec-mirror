---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Context Slices & Scopes"
section_id: "A.2.6:8"
section_title: "Locality, Time & Version Semantics"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__010_locality-time-version-semantics.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Context Slices & Scopes"
  - "A.2.6:8 — Locality, Time & Version Semantics"
line_start: 5182
line_end: 5205
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.2.2"
  - "A.22"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "C.2.1"
  - "C.2.2"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "E.24.UK"
  - "F.9"
keywords:
  - "& guard style)"
---

### A.2.6:8 - Locality, Time & Version Semantics

#### A.2.6:8.1 - Local interpretation without a context owner

A scope is not owned by a `U.BoundedContext`. Interpret its predicate under the effective reference scheme and exact local senses named by the claim or scope declaration. Evaluate it against exact `U.ContextSlice` values.

Do not assume that a similarly named selector elsewhere has the same sense. Use ordinary designation resolution when it suffices. Use `translate` only when exact local senses need an obtaining F.9 Bridge and a separate affirmative C.2.1 claim states the proposed translation's direction, rule, and tolerance; establish the current A.10 or B.3 reliance branch before acting on the returned scope.

#### A.2.6:8.2 - Time selector `Γ_time`

When membership depends on time, the scope predicate and target slice name an exact `gammaTime` point, interval, or policy and state which boundary changes a slice from member to non-member or back. Implicit “latest” is forbidden. When time does not change membership, omit the selector. Evidence freshness remains a separate R-lane predicate.

#### A.2.6:8.3 - Standards, versions & notations

When a standard, interface, or schema edition affects membership, name the exact edition. A notation change with faithful designation resolution does not change G. If exact local senses require translation, the F.9 Bridge establishes their relation, the separate C.2.1 claim states this translation's rule and tolerance, and A.10 or B.3 governs reliance; none redefines membership truth.

#### A.2.6:8.4 - Determinism of evaluation

For a fixed exact scope, exact slice, and available evaluation inputs, the evaluation method returns one reproducible result. `false` stops the attempted use. `unknown` also blocks admission but does not assert non-membership.

#### A.2.6:8.5 - Interaction with R (freshness & decay)

For empirical claims and operational capabilities, **R** typically binds evidence freshness windows. Scope does not decay with time; **trust in the support** does. Guards MAY combine “Scope covers” with “Evidence freshness holds” as separate predicates.

