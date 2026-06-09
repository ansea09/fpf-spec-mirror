---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:0"
section_title: "Conventions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__002_conventions.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:0 — Conventions"
line_start: 7853
line_end: 7883
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

### A.6.B:0 — Conventions

**Keywords.** The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **SHALL** are to be interpreted as in RFC 2119/8174. Lower‑case “must/may/should” in explanatory prose is descriptive, not normative.

**Quadrant labels.** This pattern uses the routing labels **L / A / D / E** as *statement quadrants*:

* **L** — Laws & Definitions
* **A** — Admissibility & Gates
* **D** — Deontics & Commitments
* **E** — Work‑Effects & Evidence

These labels are **claim-classification labels for statements**, not MVPK face kinds and not pattern identifiers.

**Statement identifiers (recommended).** Routable statements **SHOULD** be given stable IDs with a quadrant prefix: `L-*`, `A-*`, `D-*`, `E-*`. Other sections and views **SHOULD** reference these IDs rather than restating the same constraint in new words.

**Non-collision note (informative).** The `A-*` prefix here is “Admissibility”, not Part‑A numbering and not MVPK’s `AssuranceLane` face kind. If this is a readability hazard in your program, prefer an explicit `G-*` (“Gate”) local convention while keeping the quadrant name “Admissibility”. Also avoid introducing single‑letter mnemonics for MVPK face kinds inside this cluster (MVPK has a legacy L,P,D,E mnemonic); spell face kinds in full to reduce collisions.

**Atomic claim.** An **atomic claim** is a sentence (or bullet) that performs exactly one logical role and is routable to exactly one quadrant. If a sentence mixes roles, it is **not atomic** and **MUST** be split before it can be routed.

**Adjudication substrate (for routing).** For the purposes of this square, an atomic claim is classified by the primary substrate that decides its satisfaction:

* **In‑description / in‑theory**: satisfaction is decided from the description alone (e.g., proof/type validation), or the claim is itself a governance utterance whose content is fully determined by the text.
* **In-work or in-execution**: deciding satisfaction requires observing executed work and/or inspecting carriers produced in work.

**Note (important).** `D-*` claims are authored and interpreted in the description; whether they are met is typically established indirectly via referenced `E-*` claims (or other governance procedures). This does not move `D-*` into quadrant E; it clarifies the routing distinction.

**Modality family.** A claim is either:

* **Truth‑conditional**: definitions, invariants, typing rules (“is”, “iff”, “∀”).
* **Governance**: governance conditions, obligations, commitments, and exclusions (“MUST/SHOULD/MAY”, “is admissible”, “is blocked”, “commits to”).

