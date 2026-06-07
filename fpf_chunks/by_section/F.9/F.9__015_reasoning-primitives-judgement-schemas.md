---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:13"
section_title: "Reasoning primitives (judgement schemas)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__015_reasoning-primitives-judgement-schemas.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:13 — Reasoning primitives (judgement schemas)"
line_start: 71217
line_end: 71274
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
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

### F.9:13 - Reasoning primitives (judgement schemas)

> **All judgements are conceptual.** They support or reject specific *thinking moves*-not enactment steps and not process-enactment records.

#### F.9:13.1 - Bridge declaration

`Bridge(A@RA, B@RB) : senseFamily, kind, dir, CL, Loss, scope`

*Reading:* There exists a declared Bridge between SenseCells `A` and `B` with stated attributes.

#### F.9:13.2 - Substitution scope (senseFamily-preserving)

`Bridge(A,B): same senseFamily f, kind in {Equivalence, Narrower-than, Broader-than}, dir A->B, CL>=2, Loss L -> A may stand in for B at senseFamily f (Role-Assignment/Enactment-eligible)`

*Reading:* A **Substitution Bridge** on the same senseFamily with **CL >= 2** supports **Role-Assignment/Enactment-level** substitution **in the stated direction**. (`Type-structure` requires **CL = 3**.)

#### F.9:13.3 - Naming-only scope

`Bridge(A,B): kind in {Equivalence, Narrower-than, Broader-than, Partial-overlap}, CL>=1 -> A and B may share a label (Naming-only)`

*Reading:* A Bridge with **CL >= 1** supports using a shared label in prose or Concept-Set **Naming-only** rows, without structural or Role Assignment & Enactment commitments.

#### F.9:13.4 - Prohibition by kind

`Bridge(A,B): kind=Disjoint -> no substitution and no shared row`

*Reading:* **Disjoint** supports neither substitution nor rows; only contrastive teaching remains supported.

#### F.9:13.5 - Interpretation embargo

`Bridge(A,B): kind in {Design-spec -> Run-trace, Measure-of, Policy-implies} -> Explanation-only`

*Reading:* **Interpretation Bridges** never support substitution or rows.

#### F.9:13.6 - Weakest-link rule for rows

`row R uses {Bridge_i} -> scope(R) = min_i(scopeSupported(Bridge_i)) and CL(R) = min_i(CL_i)`

*Reading:* The **row scope** and **row CL** are bounded by the weakest participating Bridge.

#### F.9:13.7 - Direction guard

`Bridge kind=Narrower-than with dir A->B -> not(B may stand in for A)`

*Reading:* Narrower>Broader does **not** invert; only A may substitute into B under the stated scope.

#### F.9:13.8 - SenseFamily purity

`Bridge scope=Role Assignment & Enactment-eligible -> same senseFamily(A,B) and same stance(A,B)`

*Reading:* Role Assignment & Enactment-level substitution requires **same senseFamily** and same stance (run-time or design time).

#### F.9:13.9 - Loss accumulation

`A->B with Loss L1 and B->C with Loss L2 -> A->C is supported only if the same senseFamily is preserved, CL=min(CL1,CL2), and Loss accumulates as L1 union L2`

*Reading:* Chained substitution is rarer; if used, **accumulate Loss** and respect the **minimum CL**. When in doubt, avoid chaining across Contexts.

