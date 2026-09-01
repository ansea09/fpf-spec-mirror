---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:5"
section_title: "Quadrant specifications"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__007_quadrant-specifications.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:5 — Quadrant specifications"
line_start: 11197
line_end: 11304
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

### A.6.B:5 — Quadrant specifications

This section is the normative “API” of the square: what each quadrant is for, how it is written, and what it must not contain.

#### A.6.B:5.1 — Quadrant L: Laws & Definitions

**Intent.** State truth‑conditional content: definitions, invariants, typing and well-formedness constraints, equational laws.

**Adjudication.** In‑description: can be checked by inspection, proof, type validation, or model reasoning.

**Canonical form.** `Definition:` / `Invariant:` / predicate‑style constraints using “is / iff / for all”.

**Prohibitions.**

* An `L-*` statement **MUST NOT** contain RFC deontic keywords (**MUST, SHALL, SHOULD, or MAY**) as operators inside the law or definition itself.
* An `L-*` statement **MUST NOT** encode runtime gate predicates (those are `A-*`).
* An `L-*` statement **MUST NOT** assert evidence availability or measurement outcomes (those are `E-*`).

**A.7 EntityOfConcern binding.** `L-*` claims are **Descriptions**: they specify semantics of the signature or mechanism description, not work.

**Typical dependence.** `A-*` and `E-*` claims may reference `L-*` IDs for vocabulary, metric definitions, and invariants needed for interpretation.

#### A.6.B:5.2 — Quadrant A: Admissibility & Gates

**Intent.** Specify when a mechanism application is admissible: runtime entry predicates, validity gates, and applicability checks that require context or execution environment. An `A-*` predicate may consume a separately established result as one input, but it does not create or settle that result. If the sentence uses permission wording, choose its job with the branch in §8.4.1.

**Common mistake #0 — Applicability ≠ Admissibility (informative).** Signature `Applicability` scopes *intended use and bounded context*; it is not a runtime entry gate. Runtime entry checks and admissibility predicates belong in `U.Mechanism.AdmissibilityConditions` as `A-*`. If prose reads “clients must satisfy the applicability”, separate the `A-*` gate from either a generic `D-*` prescription or, when independently instituted, an individual duty linked to that gate.

**Adjudication.** In‑work: evaluated at mechanism entry (or operationally at the point the mechanism is applied).

**Canonical form.** Predicate style, e.g.:

* “A request is admissible iff …”
* `admissible(x) iff P(x)` (conceptual form; no particular syntax is required)

**Prohibitions.**

* An `A-*` statement **MUST NOT** be placed in `U.Signature.Laws`.
* An `A-*` statement **MUST NOT** use RFC deontic keywords as if it were an agent obligation. (It is a gate predicate, not a duty.)
* An `A-*` statement **MUST NOT** claim that evidence exists (that is `E-*`) or that someone must enforce the gate (that is `D-*`).

**A.7 EntityOfConcern binding.** `A-*` claims are **Descriptions** of a mechanism gate. They are not “what a client must do”; they are “what the mechanism admits”.

**Required references (explicit).** If an `A-*` predicate relies on defined terms or invariants, it **SHOULD** reference the relevant `L-*` IDs (or at minimum the signature that defines them).

#### A.6.B:5.3 — Quadrant D: Deontics & Commitments

**Intent.** State one atomic deontic claim. A generic prescription states what one exact policy or other normative episteme requires; it does not create an individual duty bearer or commitment occurrence. A claim that one actual System or separately governed party has that duty instead cites one separately obtaining A.2.8 `U.Commitment`. When a sentence sounds permissive, use §8.4.1; only its **Grant or norm** row enters D. Writing the `D-*` sentence neither institutes a relation nor establishes compliance.

**Adjudication.** For a generic prescription, inspect the exact normative source, its applicable rule content, scope, and current edition. For an individual duty, apply A.2.8 to the separately obtaining commitment and its actual basis. The wording itself decides neither obtaining nor compliance.

**Canonical form.** First choose the route. A generic D claim names the normative episteme and the rule content being stated, without inventing an individual bearer. An individual-duty D claim names the actual bearer and exact `U.Commitment`; a system-role kind or assignment may be a rule ground but is neither bearer nor duty. A responsibility claim uses an admitted domain responsibility predicate and its actual participants, or returns its exact missing governor. A permissive-looking word does not by itself select D; use §8.4.1 for the grant route. Examples:

* Generic: “`APIEntryPolicy-v4` requires covered clients to satisfy `A-…`.” No individual commitment is asserted.
* Individual: “Actual bearer `ClientIntegrator-A` has commitment `COM-17` to satisfy `A-…`.”

**Canonical assertion (recommended; lintable).** Use a `CommitmentAssertion` only when an individual-duty claim must be reused or audited. It concerns one exact separately obtaining `U.Commitment` and makes explicit:

* `entityOfConcernRef`, resolving to one exact `U.Commitment` occurrence, and the `D-*` claim ID;
* exactly one actual bearer branch: `dutyBearerSystemRef` or `dutyBearerPartyRef`;
* non-empty exact `dutyReferentRefs` and any actual counterparties;
* the A.2.8 `DeonticModalityToken`, scope, and validity window;
* the exact current constitutive policy, individualizing rule, and actual instituting basis required by that rule; and
* evidence-claim or carrier references only when the receiving reliance or adjudication needs them.

The assertion states and supports a claim about the relation. Its fields, publication, and evidence do not make the relation obtain.

**Prohibitions.**

* A generic `D-*` statement **MUST NOT** invent an individual bearer or commitment; name its exact normative source and rule content. An individual-duty `D-*` statement **MUST NOT** use “the system, service, interface, or specification” as a vague subject; name the actual duty-bearing system or separately governed party and exact `U.Commitment`, with an assignment only when the constitutive rule uses it as a ground. Use `A.6.C` when promise, utterance, approval, guarantee, or agreement-like boundary language is live.
* A `D-*` statement **MUST NOT** restate `L-*` or `A-*` predicates in new words when an ID exists; it **SHOULD** reference the ID.
* A `D-*` statement **MUST NOT** pretend that a duty, commitment, or grant is a law or that writing the claim makes it obtain.

**A.7 EntityOfConcern binding.** A generic `D-*` claim episteme concerns the exact normative rule content it states. An individual `D-*` claim concerns the exact duty, commitment, or grant named by its content and does not substitute for that object. When permission wording is live, the branch in §8.4.1 names the subject pattern and the obtaining or non-obtaining test.

**Required references (explicit).**

* If a `D-*` statement imposes compliance with a gate, it **MUST** reference the relevant `A-*` ID(s).
* If a `D-*` statement is meant to be auditable, it **SHOULD** reference the `E-*` claim(s) that provide evidence and the carrier classes involved.

#### A.6.B:5.4 — Quadrant E: Work‑Effects & Evidence

**Intent.** State a truth-conditional result that can be settled only from actual work, evaluation, observation, or produced carriers.

**Adjudication.** In-work or by an exact evaluation of work and its conditions. Reading a subject-pattern description or seeing a record is not enough.

**Canonical form.** Write the ordinary result first, then make recoverable only what settles it:

1. the exact predicate and object that the claim concerns;
2. the participants, work or evaluation occurrence, scope/window, comparison frame, and other conditions required by that predicate; and
3. the evidence or source-use relation and its carrier only when a gate, plan, audit, or assurance decision relies on that support. A carrier may support the claim but does not create the work, effect, or finding.

When permission wording is current, use the branch in §8.4.1 for the exact occurrence or finding, its failure test, predicate, and subject-pattern locator; do not repeat that subject-question catalogue here.

**Prohibitions.**

* `E-*` statements **SHOULD NOT** use RFC deontic keywords; they report adjudicable results rather than obligations.
* An `E-*` statement **MUST NOT** hide a gate predicate; gate predicates are `A-*`.
* An `E-*` statement **MUST NOT** assign agency to an interface, record, or publication. For any precise cited Work, first recover each exact actual performer through A.13 and let A.15.1 independently admit the dated Work. Add an exact A.2.1 assignment reference and F.6 only when this claim or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither the assignment nor the performer, and missing or failed F.6 leaves the Work intact. If enforceability or commitment is intended, express a separate `D-*` claim.

**A.7 EntityOfConcern binding.** An `E-*` claim episteme concerns the exact work effect, evaluated finding, evidence relation, or carrier condition named by its predicate. A record or carrier is a separate object and becomes the concern only when its existence or condition is itself the claim.

**Required references (explicit).**

* If the result is conditioned on a gate decision, the `E-*` statement **SHOULD** reference the relevant `A-*` ID(s).
* If another object is needed to settle the predicate, reference that object's subject pattern without importing its quadrant.
* If evidence is used for reliance, cite the exact A.10 or G.6 evidence-use relation rather than treating carrier presence as truth.

