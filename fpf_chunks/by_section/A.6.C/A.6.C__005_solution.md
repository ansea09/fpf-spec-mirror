---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__005_solution.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:4 — Solution"
line_start: 10164
line_end: 10265
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.8"
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
  - "(RFC 2119 + RFC 8174)"
  - "A as predicates (“is admissible iff…”)"
  - "Boundary Norm Square (L/A/D/E)"
  - "MVPK faces “no new semantics”"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SLA/guarantee claim classification"
  - "accountable commitment vs exact permission result"
  - "and E as observable/evidenced properties. If a BCP‑14 keyword or synonym appears in an L/A/E claim"
  - "and OPTIONAL"
  - "as a disciplined modality family"
  - "contract bundle unpacking"
  - "exercise"
  - "finding"
  - "in L/A/E claims"
  - "including common synonyms such as SHALL"
  - "non-violation"
  - "permission projections cite the corresponding D- and exact A.2.8.PER grant"
  - "phrase L as definitions or invariants (“is defined as…”"
  - "promise content ≠ work"
  - "promise-act/utterance separation"
  - "the face is non-conformant until rewritten without the BCP‑14 keyword or moved out of the face"
  - "the sentence MUST be rewritten to remove the keyword or moved out of the face"
  - "“holds iff…”)"
---

### A.6.C:4 — Solution

A.6.C introduces a **Contract Bundle** lens for boundary writing. It is not a new foundational entity kind; it is a disciplined way to interpret and rewrite contract-language under A.6.B.

#### A.6.C:4.1 — The Contract Bundle (four positions; deontic position has two direct-result branches)

Whenever a text uses “contract”, “guarantee”, “promise”, “SLA”, or “interface agreement” language, unpack it into four parts:

1. **Promise Content (Promise content)**

   * The promised value or effect (the promise *content*) in the intended scope.
 * In FPF terms (A.2.3), **`U.PromiseContent` is promise content**—a **promise content**, not an execution event (`U.Work`) and not (by itself) an accountable deontic binding (`U.Commitment`).
 * **Prose head rule (normative).** When referring to `U.PromiseContent` in normative prose, authors SHALL use the head phrase **promise content** (or **service offering clause** or **service promise clause**) and SHALL NOT rely on the bare head noun *service*. If the surrounding text also talks about endpoints, systems, and operations, apply **A.6.8** to select facet‑typed phrases (service access point, service delivery system, service delivery work, and so on) rather than collapsing them into “service”.
   * **Recommendation:** give the promise-content a stable local ID (e.g., `SVC-*`) so it can be cited from commitments, gates, evidence, and MVPK faces without paraphrase drift.
 * **Claim-classification discipline:** keep the semantics and definitions of the promised behavior in **L**; express *who is accountable for satisfying the promise* as a **D** claim (`U.Commitment`) that **references** the `U.PromiseContent` (plus any `A-*` and `E-*` claims as needed).

2. **Utterance Package (speech act + published descriptions)**

   * The work occurrence of stating, publishing, or approving (a `U.SpeechAct <: U.Work`, A.2.9) **and** the utterance descriptions it produces or updates (versioned **epistemes** on carriers) that carry the L/A/D/E-classified claim set.
   * A speech act **may** institute or update commitments or strong granted permissions, but only under an explicit context policy that recognizes that `actType` as having the corresponding institutional force.
   * The published utterance descriptions (signature or mechanism descriptions plus MVPK faces) carry L/A/D/E-classified claims. The act is not “the contract”; it is the work occurrence that created or updated the descriptions and, when recognized, instituted the separately represented commitments or granted permissions.
   * **Default interpretation rule (normative).** A conformant boundary model **MUST NOT** infer `U.Commitment` or `GrantedPermissionRelation@Context` occurrences solely from a `Publish` or `Approve` `U.SpeechAct`. Publication creates or updates utterance descriptions and MAY institute publication/status claims (for example, “Published”, “Approved as Standard”, or “Deprecated”), but commitments and strong grants exist only as explicit direct-owner objects under an exact context policy.
   * If a bounded context defines a policy mapping publish or approve act types to deontic effects, the model **MUST** cite that policy. Resulting duties, recommendations-as-duty, or prohibitions **MUST** still be explicit `U.Commitment` objects with accountable subjects; resulting strong permissions **MUST** still be explicit `A.2.8.PER` grant occurrences with their exact beneficiaries and ground.

3. **Deontic governance (commitment and permission kept separate)**

   * Accountable obligations, recommendations-as-duty, and prohibitions (including accountability for satisfying a promise content) are one or more explicit `U.Commitment` records under A.2.8.
   * A strong grant, weak non-prohibition/non-violation finding, actual permission exercise, or permission conflict is an exact `A.2.8.PER` result. It is not stored in `U.Commitment.modality` and is not inferred from a permit carrier or `MAY` token.
   * **Commitment-branch checklist (A.2.8 minimal structure):**
     * `id` (stable; often the `D-*` claim ID),
     * `subject` (accountable role or party; never an episteme),
     * `modality` (the exact A.2.8 `DeonticModalityToken`: `MUST | MUST_NOT | SHOULD | SHOULD_NOT`),
     * `scope` (`U.ClaimScope`) and `validityWindow` (`U.QualificationWindow`),
     * `referents` (by reference or ID: promise content IDs like `SVC-*`, plus `L-*`, `A-*`, `MethodDescriptionRef(...)`, or `PromiseContentRef(...)` as needed),
     * optional `owedTo` (beneficiary or counterparty),
     * optional `adjudication.evidenceRefs` when the commitment is meant to be auditable (point to `E-*`),
     * optional `source` when authority or provenance matters (issuer + instituting `speechActRef` + description reference),
     * optional `notes` for explicitly informative commentary (not part of the binding).
   * **Permission-branch pointer:** cite the exact selected `A.2.8.PER` grant, finding, exercise, non-violation, or conflict object and preserve its own schema, participants, and references; do not reuse the commitment checklist as a generic permission record.
   * A commitment is not “the spec text”: utterance descriptions carry the statement, but the binding is the `U.Commitment` object (A.7 and A.2.8).
4. **Performed work and evidence (Adjudication substrate)**

   * The executed work and observable carriers and traces that can adjudicate whether a commitment was met or whether actual work exercised a grant or was non-violating in the checked frame.
   * This is **E quadrant**: “what evidence is produced, exposed, or retained, under what conditions, and how it is interpreted”.
   * Work is not “the contract”; it is what makes any operational claim testable.
   * In FPF terms, evidence is normally expressed as **carrier-referenced `E-*` claims**, evidence paths, witness relations, or assurance claims governed by `A.10`, `B.3`, or the direct evidence pattern named by value.

#### A.6.C:4.2 — Classification recipe into A.6.B (L/A/D/E)

After unpacking, classify each **atomic** statement using the Boundary Norm Square as defined normatively in **A.6.B** (quadrant semantics + form constraints + cross‑quadrant reference discipline). A.6.C does not redefine `L/A/D/E`; it applies them to contract-language as follows:

* **Promise content → L/A (promise semantics + eligibility).**
  * Put meanings, invariants, and metric definitions for what is promised in **L** (`L-*` in signature laws and definitions).
  * Put “eligible, covered, or valid iff …” predicates as **A** (`A-*` admissibility or gate predicates), not as deontic obligations.
* **Deontic governance → D (which direct result).**
  * Put “MUST, SHALL, or commits to …” statements as **D** (`D-*`), preferably as `U.Commitment` payloads (A.2.8).
  * Put strong/weak permission, exercise, non-violation, and conflict statements as **D** with the exact `A.2.8.PER` result; do not convert them to commitment modality.
  * If compliance requires satisfying or enforcing a gate, the commitment **MUST** reference the relevant `A-*` ID(s) (D→A).
  * If the commitment is meant to be auditable, include evidence hooks by referencing `E-*` (D→E), preferably via `U.Commitment.adjudication.evidenceRefs`.
* **Performed work and evidence → E (how we can tell).**
  * Put observable traces, audit records, measurement windows, and carrier semantics as **E** (`E-*`) with explicit carrier and observation or measurement conditions (A.6.B:5.4).
**Keyword placement rule (canonical claim set).**
Within the canonical L/A/D/E-classified claim set, BCP‑14 norm keywords (RFC 2119 + RFC 8174) and their common synonyms (for example SHALL, REQUIRED, RECOMMENDED, and OPTIONAL) are statement operators, not ontology selectors. `MUST`, `MUST NOT`, `SHOULD`, and `SHOULD NOT` route to `U.Commitment` only when the recovered claim is an accountable duty, recommendation-as-duty, or prohibition. `MAY` and `OPTIONAL` route to `A.2.8.PER` when the recovered claim is strong or weak permission; when they express only mechanism entry, rewrite the claim as an `A-*` predicate. Authors **SHOULD** avoid these keywords in **L/A/E** claims; phrase **L** as definitions or invariants (“is defined as…”, “holds iff…”), **A** as predicates (“is admissible iff…”), and **E** as observable/evidenced properties. If a BCP‑14 keyword or synonym appears in an **L/A/E** claim, it **SHOULD** be rewritten into predicate or definition form or explicitly marked informative before publication.

A helpful rewrite rule:

> First recover what “allowed” asserts: an entry condition becomes an **A** predicate; an actual strong/weak permission, exercise, non-violation, or conflict claim becomes **D** plus its exact `A.2.8.PER` object; an accountable duty to satisfy or enforce a gate becomes **D** plus `U.Commitment`; observable adjudication remains **E**. The keyword alone selects none, and references across these claims follow A.6.B.

#### A.6.C:4.3 — “Guarantee” disambiguation

Treat “guarantee” as ambiguous until classified:

* **Semantic guarantee** → **L** (“by definition or invariant”).
* **Governance guarantee** → **D** (“provider commits or implementer must”).
* **Operational guarantee** → **E** (measured property with evidence expectations; optionally referenced by D as the adjudication target).

If none of these fits, the statement is likely rhetorical and should be rewritten or explicitly marked as aspirational or informative.

#### A.6.C:4.4 — MVPK faces are not second contracts

A contract bundle has one canonical claim set. Publication faces are **views** of that set under viewpoints:

* Faces may **select, summarize, and render** claims for audiences.
* Faces must not **introduce new semantic commitments or permission results** beyond the underlying claim set.
* Any face-level decision-relevant or normative-looking statement **SHOULD** cite the underlying claim ID(s). If it cannot be traced to claim IDs, it **MUST** be explicitly presented as informative commentary.

**Keyword rule (faces).**
If a face contains BCP‑14 norm keywords (RFC 2119 + RFC 8174), including common synonyms such as SHALL, REQUIRED, RECOMMENDED, and OPTIONAL, each sentence MUST project an existing classified claim and cite its underlying claim ID. Duty/recommendation/prohibition projections cite the corresponding `D-*` and `U.Commitment`; permission projections cite the corresponding `D-*` and exact `A.2.8.PER` grant, finding, exercise, non-violation, or conflict result with that object's own participants and references. A face-level `MAY` or `OPTIONAL` cannot manufacture any direct object. If no underlying claim and direct object are traceable, the sentence MUST be rewritten to remove the keyword or moved out of the face.
To avoid keyword‑evasion, equivalent deontic phrasings (e.g., “is required to…”, “is prohibited from…”) SHOULD follow the same trace-by-ID discipline even when no BCP‑14 keyword is present.

Projection may be paraphrased for audience fit, but it **MUST NOT** change the deontic or semantic claim; if exactness is critical or disputed, use verbatim.

This prevents faces from becoming “second contracts” by paraphrase drift.

#### A.6.C:4.5 — Default register: Contract Claim Register (recommended)

Use the **A.6.B Claim Register** (IDs, statements, quadrant, and canonical location). Add two optional columns that make A.6.C auditable without adding new ontology:

* `bundleId: ContractBundleId` (local stable ID grouping the claims that constitute one boundary “contract bundle”)
* `bundlePart ∈ {PromiseContent, Utterance, Commitment, Permission, WorkEvidence}` (the deontic position has two direct-result branches)
* `faceRefs = {PlainView|TechCard|InteropCard|AssuranceLane : …}` (where the claim is rendered)

