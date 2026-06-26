---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:14"
section_title: "Reasoning primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__019_reasoning-primitives.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:14 — Reasoning primitives"
line_start: 82742
line_end: 82835
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:14 - Reasoning primitives

All judgements here are conceptual. They admit or reject specific cross-context sense-use moves; they are not work-enactment records.

#### F.9:14.1 - Bridge declaration

```text
Bridge(A@ContextA, B@ContextB) :
  senseFamilyA,
  senseFamilyB,
  kind,
  direction,
  CL,
  LossNotes,
  admittedUse
```

Interpretation: there is a declared Bridge between two local senses with stated attributes.

#### F.9:14.2 - Naming-only scope

```text
Bridge(A,B) with kind in {Equivalence, Narrower-than, Broader-than, Partial-overlap}
and CL >= 1
=> A and B may share a label in prose or a Naming-only Concept-Set row.
```

Interpretation: the shared label remains a label; it carries no structural, role-assignment, status, evidence, or work effect.

#### F.9:14.3 - Same-family substitution of sense

```text
Bridge(A,B) with same senseFamily,
kind in {Equivalence, Narrower-than, Broader-than},
declared direction A -> B,
CL >= 2,
and stated LossNotes
=> A may stand in for B only for the admitted same-family sense use.
```

Interpretation: same-family substitution is bounded by direction, `CL`, loss, and admitted use. For role material, this reaches RoleDescription naming or comparison only; role assignment itself remains with A.2.1 and F.6.

#### F.9:14.4 - Type-structure scope

```text
Bridge(A,B) with same Type-structure senseFamily,
kind = Equivalence,
CL = 3,
and matched invariants
=> A and B may participate in a Type-structure row.
```

Interpretation: Type-structure use is the strongest F.9 row use and requires invariant evidence.

#### F.9:14.5 - Interpretation embargo

```text
Bridge(A,B) with interpretation kind
=> Explanation-only.
```

Interpretation: design-spec-to-run-occurrence, measurement-evidence-for, policy-constraint-on, and viewpoint-correspondence Bridges explain relations across sense families but do not admit substitution.

#### F.9:14.6 - Weakest-link rule

```text
Row R uses {Bridge_i}
=> admittedUse(R) <= min_i(admittedUse(Bridge_i))
and CL(R) <= min_i(CL(Bridge_i)).
```

Interpretation: a row is never stronger than its weakest Bridge.

#### F.9:14.7 - Direction guard

```text
Bridge kind = Narrower-than with direction A -> B
=> not(B may stand in for A).
```

Interpretation: narrower-to-broader does not invert.

#### F.9:14.8 - Loss accumulation

```text
A -> B with Loss L1
B -> C with Loss L2
=> A -> C only if the same senseFamily is preserved;
   CL becomes min(CL1, CL2);
   Loss accumulates as L1 plus L2.
```

Interpretation: chained cross-context substitution is rare. If used, loss and `CL` degrade rather than disappear.

