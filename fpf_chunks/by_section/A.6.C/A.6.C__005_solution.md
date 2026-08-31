---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__005_solution.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:4 — Solution"
line_start: 11856
line_end: 11963
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "E.10"
  - "E.17"
  - "F.12"
  - "F.18"
  - "U.Commitment"
  - "U.PromiseContent"
  - "U.SpeechAct"
  - "U.Work"
keywords:
  - "MUST NOT"
  - "MVPK no-new-semantics"
  - "OPTIONAL"
  - "SHOULD"
  - "a mechanism entry predicate enters A"
  - "an individual duty"
  - "and SHOULD NOT enter D for a generic prescription or"
  - "and authority-looking synonyms trigger the A.6 A6-AW-* branch: a current norm or grant enters D"
  - "are statement operators"
  - "atomic L/A/D/E rows"
  - "commitment or grant"
  - "dated Work"
  - "description and publication"
  - "four-question contract lens"
  - "gate"
  - "not ontology or quadrant selectors. MUST"
  - "obtaining versus representation"
  - "or prohibition. MAY"
  - "promise content"
  - "recommendation-as-duty"
  - "rewrite it or mark it informative"
  - "separate result and evidence"
  - "speech-act Work"
  - "when separately instituted for an actual bearer"
---

### A.6.C:4 — Solution

A.6.C introduces a four-question boundary-language lens. It interprets and rewrites contract-like source wording under A.6.B without admitting a `Contract` object or another ontology branch.

#### A.6.C:4.1 — Four questions for contract-like boundary wording

Whenever a text uses “contract”, “guarantee”, “promise”, “SLA”, or “interface agreement”, ask the four questions below. A question may yield zero, one, or several atomic Claim Register rows; the question itself is not a bundle part or direct-object kind.

1. **What was promised?**

   * The promised value or effect (the promise *content*) in the intended scope.
   * In FPF terms (A.2.3), **`U.PromiseContent` is promise content**—a **promise content**, not an execution event (`U.Work`) and not, by itself, an obtaining individual deontic relation (`U.Commitment`).
   * **Prose head rule (normative).** When referring to `U.PromiseContent` in normative prose, authors SHALL use the head phrase **promise content** (or **service offering clause** or **service promise clause**) and SHALL NOT rely on the bare head noun *service*. If the surrounding text also talks about endpoints, systems, and operations, apply **A.6.P:4.11a** only when the current relied-on use still hides which concrete subject or relation is meant; examples include a service access point, service delivery system, or service-delivery Work occurrence. Mere proximity to those words creates no additional claim or recovery duty.
   * **Recommendation:** give the promise-content a stable local ID (e.g., `SVC-*`) so it can be cited from commitments, gates, evidence, and MVPK faces without paraphrase drift.
   * **Claim-classification discipline:** keep meanings and definitions of the promised behavior in **L**. A generic prescription about that behavior is a separate **D** claim about its exact normative source and applicable rule content. If an actual System or separately governed party has that duty, state a separate **D** claim about the exact `U.Commitment`, plus any `A-*` and `E-*` references needed by that claim.

2. **What was said, published, or instituted?**

   * **Speech-act row:** if the boundary decision depends on who stated, published, or approved something, record that exact A.2.9 `U.SpeechAct <: U.Work` occurrence.
   * **Description/publication rows:** record the versioned utterance epistemes separately from their publication occurrences, forms, renderings, and carriers. None is the speech act.
   * A speech act **may** institute or update a commitment or strong grant only when the exact context policy recognizes that act type and the subject pattern's obtaining conditions are met.
   * The published utterance descriptions (signature or mechanism descriptions plus MVPK faces) carry L/A/D/E-classified claims. The act is not “the contract”; it is the Work occurrence that created or updated those descriptions and may have a separately governed institutional effect.
   * **World-side obtaining rule (normative).** The predicates defined in A.2.8 and the cited context policy decide whether a commitment obtains; the predicate defined in A.2.8.PER together with that policy decides whether a strong grant obtains. They use the actual instituting speech act, participants, scope/window, current policy, and any revocation or supersession conditions. A Claim Register row, utterance description, publication, carrier, or identifier creates or proves neither relation. Publication or approval may establish a publication/status relation only through that relation's exact predicate and obtaining facts.
   * **Representation and reliance rule (normative).** The model **MAY assert or rely on** a commitment or grant only through a separate atomic claim that identifies the exact `U.Commitment` or `GrantedPermissionRelation@Context` occurrence and cites its exact predicate, `SubjectPatternLocator`, instituting act and policy, participants, scope/window, and the currentness or evidence required by that use. Never infer the relation from `Publish`/`Approve` wording, a document, carrier, or completed-looking record alone.

3. **What governance or permission-looking claim exists?**

   * A generic prescription states what one exact policy or other normative episteme requires; it does not create an individual duty bearer or commitment occurrence. A claim that one actual System or separately governed party has that duty instead cites one separately obtaining A.2.8 `U.Commitment`. Here the normative episteme may be a contract, SLA, protocol, or policy, and the generic claim also states where its rule applies.
   * When the model asserts or relies on an individual obligation, recommendation-as-duty, or prohibition, write a separate atomic D claim whose direct object is that exact separately obtaining `U.Commitment`. The claim describes that relation for use; it neither institutes it nor proves that it obtains.
   * For permission-looking wording, select one A.6 `A6-AW-*` row. Only `A6-AW-NORM-GRANT` enters D; `A6-AW-GATE` enters A; exercise, weak evaluation, conflict, and observed-source claims enter E when their closing facts are present. Classification under A.2.8.PER alone selects no quadrant.
   * **Individual-commitment checklist (use only for the individual branch):**
     * identify one exact `U.Commitment` occurrence and the separate D-claim or `CommitmentAssertion` about it;
     * select exactly one actual bearer branch: an admitted `U.System` or separately governed party;
     * name non-empty exact duty referents, any actual counterparties, normalized modality, scope, and validity window;
     * cite the exact current constitutive policy, its individualizing rule, and the actual instituting basis required by that rule;
     * cite a system-role assignment only when that rule uses the assignment as an applicability ground—the assignment is neither bearer nor duty; and
     * add evidence-claim or carrier references only when the receiving reliance or adjudication needs them.
   * **Permission-branch pointer:** cite the selected `A6-AW-*` row, its exact A.2.8.PER object when applicable, and that atomic claim's quadrant. Preserve the object's own schema, participants, and references; do not reuse the commitment checklist.
   * A commitment is not “the spec text”: an utterance description carries the statement, while `U.Commitment` is the separately obtaining relation described by that statement (A.7 and A.2.8).
4. **What happened, what followed, and what supports reliance?**

   * **Work:** For one exact dated `W : U.Work`, recover each exact actual performer through A.13 and let A.15.1 independently admit the occurrence from that performer, enacted Method, extent, and containing System. Add an exact A.2.1 assignment reference and F.6 only when this account or a receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither the assignment nor the performer, and missing or failed F.6 leaves the Work intact. The Work can exist without a result, production, delivery, evidence-use, or acceptance claim.
   * **Result or consequence:** only when the sentence asks for one, select the matching `A.15.1:4.6` row—an A.6.1 application/result binding or independently obtaining `WorkResultRelation`, A.15.PROD production branch, A.3.4 change, evaluation result, subject-specific delivery/transfer relation, or acceptance relation. An absent row stays absent.
   * **Evidence:** only when a receiving use relies on Work or one of those consequences, state an A.10 claim-bound evidence path and carrier. Evidence supports the named claim; it creates neither the Work nor its result.

#### A.6.C:4.2 — Classification recipe into A.6.B (L/A/D/E)

After unpacking, classify each **atomic** statement using the Boundary Norm Square as defined normatively in **A.6.B** (quadrant semantics + form constraints + cross‑quadrant reference discipline). A.6.C does not redefine `L/A/D/E`; it applies them to contract-language as follows:

* **Promise content → L/A (promise semantics + eligibility).**
  * Put meanings, invariants, and metric definitions for what is promised in **L** (`L-*` in signature laws and definitions).
  * Put “eligible, covered, or valid iff …” predicates as **A** (`A-*` admissibility or gate predicates), not as deontic obligations.
* **Governance and permission-looking claims → claim-specific quadrant.**
  * Put a generic contract, SLA, protocol, or policy prescription in **D** as a claim about its exact normative source and applicable rule content. Put an individual-duty claim in **D** only when it cites an exact separately obtaining `U.Commitment` under A.2.8; do not use a completed record as the relation.
  * For authority-looking wording, select one A.6 `A6-AW-*` row: norm/grant → **D**, gate → **A**, and actual exercise or evaluated finding/conflict/source → **E**. Cite the exact A.2.8.PER object only where that row requires it; the selected subject pattern or kind of direct object does not choose the sentence's quadrant.
  * If a generic prescription or individual duty requires satisfying or enforcing a gate, its `D-*` claim **MUST** reference the relevant `A-*` ID(s) (D→A).
  * If reliance on either D branch needs evidence, cite the relevant `E-*` claim or evidence-use relation (D→E); for the individual branch, a `CommitmentAssertion` may carry that reference. Evidence does not make `U.Commitment` obtain.
* **Performed Work → E (did it happen?).**
  * Name the exact A.15.1 Work occurrence and its performer, assignment, method, extent, and containing system. Do not add an output or delivery field.
* **Result or consequence → E when current (what else happened?).**
  * Use the one applicable `A.15.1:4.6` predicate and exact subject assertion for the returned value, production, change, evaluation result, delivery/transfer, or acceptance claim; retain its pattern only as a locator.
* **Evidence → E when relied on (how can the claim be used?).**
  * Name the exact A.10 path, observation conditions, and carrier for the Work or consequence claim being supported. Carrier presence establishes none of those objects.
**Keyword placement rule (canonical claim set).**
Within the canonical L-, A-, D-, or E-classified claim set, BCP-14 keywords are statement operators, not ontology or quadrant selectors. `MUST`, `MUST NOT`, `SHOULD`, and `SHOULD NOT` enter D for a generic prescription or, when separately instituted for an actual bearer, an individual duty, recommendation-as-duty, or prohibition. `MAY`, `OPTIONAL`, and authority-looking synonyms trigger the A.6 `A6-AW-*` branch: a current norm or grant enters D, a mechanism entry predicate enters A, and an actual exercise or evaluated finding enters E. If the wording does not expose the branch and direct object, rewrite it or mark it informative.

A helpful rewrite rule:

> First recover what “allowed” asserts by selecting one A.6 `A6-AW-*` row. Put only the current norm/grant in D, the entry predicate in A, and actual exercise or evaluated findings in E; cite each direct object and source. The word and A.2.8.PER membership select neither quadrant nor obtaining.

#### A.6.C:4.3 — “Guarantee” disambiguation

Treat “guarantee” as ambiguous until classified:

* **Semantic guarantee** → **L** (“by definition or invariant”).
* **Governance guarantee** → **D** (“provider commits or implementer must”).
* **Operational guarantee** → **E** (measured property with evidence expectations; optionally referenced by D as the adjudication target).

If none of these fits, the statement is likely rhetorical and should be rewritten or explicitly marked as aspirational or informative.

#### A.6.C:4.4 — MVPK faces are not second contracts

The atomic claims grouped for one boundary use live in one canonical A.6.B Claim Register set; the four-question lens creates no parallel claim set. Publication faces are **views** of that set under viewpoints:

* Faces may **select, summarize, and render** claims for audiences.
* Faces must not introduce a new commitment or any new object or claim selected through `A6-AW-*`; they project the existing classified claim.
* Any face-level decision-relevant or normative-looking statement **SHOULD** cite the underlying claim ID(s). If it cannot be traced to claim IDs, it **MUST** be explicitly presented as informative commentary.

**Keyword rule (faces).**
If a face contains a BCP-14 keyword, each sentence MUST cite its existing classified claim ID and direct object. Duty/recommendation/prohibition and current-grant projections cite their D claim; a gate projection cites its A claim; exercise or evaluated-finding projections cite their E claim. Use the selected A.6 `A6-AW-*` row for permission-looking wording. A face-level keyword manufactures no object or quadrant; without a traceable claim, remove the keyword or mark the sentence informative.
To avoid keyword‑evasion, equivalent deontic phrasings (e.g., “is required to…”, “is prohibited from…”) SHOULD follow the same trace-by-ID discipline even when no BCP‑14 keyword is present.

Projection may be paraphrased for audience fit, but it **MUST NOT** change the deontic or semantic claim; if exactness is critical or disputed, use verbatim.

This prevents faces from becoming “second contracts” by paraphrase drift.

#### A.6.C:4.5 — A.6.B Claim Register additions (recommended)

Use the **A.6.B Claim Register** (IDs, statements, quadrant, and canonical location). Add the following A.6.C fields without minting another record or ontology kind:

* `bundleId` (optional local ID grouping atomic claims discussed together)
* `questionRef` (optional pointer `Q1`, `Q2`, `Q3`, or `Q4` to the four questions above; it selects no kind, subject predicate, or quadrant)
* `directObjectDesignation` (use `U.RelationRef` constrained to the exact relation family for a relation occurrence, the applicable `U.EpistemeRef` for a whole episteme, or the admitted reference kind for another independently identified entity. When one claim inside an episteme is the direct object, use `C.2.1 ClaimAddress`: exact episteme-edition reference plus intrinsic claim identity declared by that edition's ClaimGraph. The entity-reference branches designate independently identified objects; the claim branch designates content inside the named edition. Neither carries the designated content.)
* `directObjectPatternLocator` (the exact pattern-description locator for the ClaimGraph that defines or constrains that direct object; it asserts no ownership relation)
* `faceRefs` (optional mapping from `PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane` to where this same claim is rendered)

Each row still uses the A.6.B fields for one exact statement, claim ID, quadrant, and canonical location. Do not create a second boundary-language record or a `Permission`, `Utterance`, `WorkEvidence`, or result-or-evidence umbrella kind.

