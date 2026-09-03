---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:0"
section_title: "Conventions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__002_conventions.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:0 — Conventions"
line_start: 11110
line_end: 11140
dependencies:
  - "A.10"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.C"
  - "A.7"
  - "B.3"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.8"
  - "U.Commitment"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
  - "U.SpeechAct"
keywords:
  - "(MUST"
  - "(ii) claim that evidence carriers exist (that is E-)"
  - "(ii) encode runtime entry predicates (those are A-)"
  - "Keeps normative content"
  - "MAY"
  - "MUST"
  - "MUST NOT"
  - "MUST NOT hide a gate predicate (that is A-)"
  - "SHALL"
  - "SHOULD"
  - "SHOULD NOT"
  - "The key words MUST"
  - "accountable norms and grants"
  - "actual exercise"
  - "an individual-duty D- claim MUST name its actual bearer and exact separately obtaining U.Commitment"
  - "and MAY"
  - "and MUST NOT cite D-*"
  - "and SHALL are to be interpreted as in RFC 2119/8174. Lower-case must"
  - "and evaluated results distinct"
  - "and should in explanatory prose is descriptive"
  - "as if it were an agent obligation"
  - "as if it were an agent obligation. (It is a gate predicate"
  - "as operators"
  - "atomic L/A/D/E claims"
  - "conflict claims"
  - "direct obtaining conditions"
  - "entry predicates"
  - "evaluated findings"
  - "evaluation"
  - "individual institution"
  - "laws"
  - "may"
  - "not a duty.)"
  - "not normative"
  - "observable effects and evidence"
  - "or (iii) assert evidence existence or measurement outcomes (those are E-*)"
  - "or (iii) assign responsibility or enforcement (that is D-*)"
  - "or MAY) as operators inside the law or definition itself"
  - "or observation that settles it and any evidence used for reliance"
  - "responsibility"
  - "they report adjudicable results rather than obligations"
  - "“commits to”)"
  - "“is admissible”"
  - "“is blocked”"
  - "”) used as operators inside L- or A- predicates (should be D- that references L-/A-)"
---

### A.6.B:0 — Conventions

**Keywords.** The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **SHALL** are to be interpreted as in RFC 2119/8174. Lower-case `must`, `may`, and `should` in explanatory prose is descriptive, not normative.

**Quadrant labels.** This pattern uses the classification labels **L / A / D / E** as *statement quadrants*:

* **L** — Laws & Definitions
* **A** — Admissibility & Gates
* **D** — Deontics & Commitments
* **E** — Work‑Effects & Evidence

These labels are **claim-classification labels for statements**, not MVPK face kinds and not pattern identifiers.

**Statement identifiers (recommended).** Classifiable statements **SHOULD** be given stable IDs with a quadrant prefix: `L-*`, `A-*`, `D-*`, `E-*`. Other sections and views **SHOULD** reference these IDs rather than restating the same constraint in new words.

**Non-collision note (informative).** The `A-*` prefix here is “Admissibility”, not Part-A numbering and not MVPK’s `AssuranceLane` face kind. If this is a readability hazard in your program, prefer an explicit `G-*` (“Gate”) local convention while keeping the quadrant name “Admissibility”. Also avoid introducing single-letter mnemonics for MVPK face kinds inside this cluster; spell face kinds in full to reduce collisions.

**Atomic claim.** An **atomic claim** is a sentence (or bullet) that performs exactly one logical role and is classifiable under exactly one quadrant. If a sentence mixes roles, it is **not atomic** and **MUST** be split before it can be classified.

**Adjudication substrate (for classification).** For the purposes of this square, an atomic claim is classified by where its own truth condition or governance content is settled. This tells you how to classify the sentence; it does not make an individual commitment, grant, or finding exist.

* **In-description or in-theory**: an `L-*` truth condition is settled by inspecting, proving, or type-validating the description; a generic `D-*` claim states exact normative content, while an individual `D-*` claim names the commitment or grant it concerns.
* **In-work or in-execution**: deciding satisfaction requires observing executed work, inspecting carriers produced in work, or both.

**Note (important).** Writing a `D-*` claim records either generic normative content or a claim about an individual duty, commitment, or grant; it does not institute an individual relation or establish compliance. When the wording is about permission, use the permission-word branch in §8.4.1 to recover the exact object, what makes it obtain, and the evidence needed before reliance.

**Modality family.** A claim is either:

* **Truth‑conditional**: definitions, invariants, typing rules (“is”, “iff”, “∀”).
* **Governance**: prescriptions, individual obligations or commitments, grants, and exclusions (the RFC keywords `MUST`, `SHOULD`, and `MAY`, “is admissible”, “is blocked”, “commits to”).

