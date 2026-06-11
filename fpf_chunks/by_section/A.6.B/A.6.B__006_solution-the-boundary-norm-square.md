---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:4"
section_title: "Solution — the Boundary Norm Square"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__006_solution-the-boundary-norm-square.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:4 — Solution — the Boundary Norm Square"
line_start: 7913
line_end: 7950
dependencies:
  - "A.10"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26.1"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.8"
  - "F.18"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
keywords:
  - "(MUST/SHALL/SHOULD/MAY) as operators inside the law/definition itself"
  - "(ii) claim that evidence/carriers exist (that is E-)"
  - "(ii) encode runtime entry predicates (those are A-)"
  - "(they are not obligations"
  - "(“MUST/SHALL/…”) used as operators inside L- or A- predicates (should be D- that references L-/A-)"
  - "Keeps modalities separated and audit‑ready"
  - "L/A/D/E claim classification"
  - "MAY"
  - "MUST NOT"
  - "MUST NOT hide a gate predicate (that is A-)"
  - "SHOULD"
  - "SHOULD NOT"
  - "The key words MUST"
  - "admissible use"
  - "and MUST NOT cite D-*"
  - "as if it were an agent obligation"
  - "as if it were an agent obligation. (It is a gate predicate"
  - "as operators"
  - "atomic claims"
  - "belong here"
  - "boundary norm square"
  - "claim IDs"
  - "laws vs gates vs commitments vs evidence"
  - "non-admissible use"
  - "not a duty.)"
  - "not normative"
  - "or (iii) assert evidence existence/measurement outcomes (those are E-*)"
  - "or (iii) assign responsibility/enforcement (that is D-*)"
  - "they describe adjudicable effects/evidence)"
  - "triangle decomposition"
  - "“the interface/system promises” does not)"
---

### A.6.B:4 - Solution — the Boundary Norm Square

#### A.6.B:4.1 - Two independent distinctions

The **Boundary Norm Square** is the cross product of two independent distinctions:

1. **Modality family:** Truth‑conditional vs Governance
2. **Adjudication position:** In-description vs in-work

The square yields four quadrants that are *mutually exclusive for atomic claims*.

#### A.6.B:4.2 — The square

|                                | **Truth‑conditional** (definitions & invariants) | **Governance** (governance conditions & obligations) |
| ------------------------------ | ------------------------------------------------ | ------------------------------------------ |
| **In‑description / in‑theory** | **L — Laws & Definitions**                       | **D — Deontics & Commitments**             |
| **In-work or in-execution**     | **E — Work‑Effects & Evidence**                  | **A — Admissibility & Gates**              |

**Clarification (do not conflate).** The Governance column includes two different “normative” roles:
* **D** is **`U.Agent` or `U.Role` governance** (duties, commitments, prohibitions).
* **A** is **mechanism governance** (admissibility predicates: what the mechanism admits at application time).
`A-*` is not an obligation on an actor; obligations belong in `D-*` and may reference `A-*`.

**Normative rule (single quadrant).** Each **atomic** claim **MUST** be routable to exactly one quadrant **L/A/D/E**.

**Normative rule (no mixed sentences).** A conforming boundary text **SHALL** decompose any sentence that bundles multiple quadrants (typical form: “MUST … if … then … and it is logged …”) into multiple atomic claims before those claims are treated as normative.

#### A.6.B:4.3 — Canonical placements in the Signature Stack

The quadrants have canonical placements in the boundary stack:

* **L → Signature layer:** `U.Signature.Laws` (and mechanism‑local semantic laws if present).
* **A → Mechanism layer:** `U.Mechanism.AdmissibilityConditions` (entry gates / runtime admissibility predicates).
* **D → Norms & commitments layer:** role‑anchored duties, commitments, publication/accountability duties (often rendered inside MVPK `TechCard`).
* **E → Evidence bindings layer:** work‑adjudicated effects tied to carriers and measurement conditions (authored canonically in an Evidence/Carriers section; commonly rendered inside MVPK `AssuranceLane` as a projection).

A published view **MUST NOT** introduce new semantic claims outside this L/A/D/E-classified claim set. **E.17 (MVPK)** is a specialization that enforces this rule for a fixed set of publication face kinds.

