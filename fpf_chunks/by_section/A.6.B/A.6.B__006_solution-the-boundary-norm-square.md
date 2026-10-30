---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:4"
section_title: "Solution — the Boundary Norm Square"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__006_solution-the-boundary-norm-square.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:4 — Solution — the Boundary Norm Square"
line_start: 14632
line_end: 14685
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
  - "MUST NOT"
  - "SHALL"
  - "SHOULD"
  - "SHOULD NOT"
  - "The key words MUST"
  - "accountable norms and grants"
  - "actual exercise"
  - "an individual-duty D- claim MUST name its actual bearer and exact separately obtaining U.Commitment"
  - "and SHALL have their RFC 2119/8174 meanings only when capitalized as shown"
  - "and evaluated results distinct"
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
  - "not a duty.)"
  - "observable effects and evidence"
  - "or (iii) assert evidence existence or measurement outcomes (those are E-*)"
  - "or (iii) assign responsibility or enforcement (that is D-*)"
  - "or MAY) as operators inside the law or definition itself"
  - "or observation that settles it and any evidence used for reliance"
  - "responsibility"
  - "then establish the E result under its own predicate"
  - "they report adjudicable results rather than obligations"
  - "”) used as operators inside L- or A- predicates (should be D- that references L-/A-)"
---

### A.6.B:4 - Solution — the Boundary Norm Square

#### A.6.B:4.1 - Four claim jobs and their grounds

The **Boundary Norm Square** distinguishes four jobs in a boundary account. A definition can remain fixed while a gate changes; a duty can obtain while its bearer fails to perform it. An earlier observation may still be valid evidence when a changed admission condition leads to refusal. Establish the observation’s fitness for the new check, then apply that condition to decide admission. Keeping those claims distinct makes their actual dependencies available for a change or audit decision.

Classify what the exact sentence asserts, then establish its grounds. For example, a declared entry predicate belongs in A and the result of applying it to one request belongs in E. A claim that a grant currently permits an action belongs in D; the instituting act, an evaluation of that grant and an actual exercise of it have their own E claims. The predicate definition and the individual claims remain description content, with different subjects and adjudication conditions.

#### A.6.B:4.2 — The square

| Quadrant | Job of the claim | What settles it |
| --- | --- | --- |
| **L — Laws & Definitions** | Defines vocabulary, a semantic constraint, invariant or typing rule. | The declared definition or assumptions and the corresponding inspection, proof, type validation or model reasoning. |
| **A — Admissibility & Gates** | Declares the condition for a mechanism application to enter. | The exact admission rule and its input meanings. A particular application's satisfaction or decision is a separate E claim. |
| **D — Deontics & Commitments** | States generic normative content or a claim about an individual duty or grant. | The exact normative source for generic content; the subject pattern's constitutive conditions and actual basis for an individual relation. |
| **E — Work‑Effects & Evidence** | Reports an occurrence, evaluated finding, observed condition or evidence support. | The actual facts and subject-specific conditions for that claim, with evidence support when the receiving use requires it. |

**Clarification (classify the claim by its job, not by its subject pattern).**

* Classify the exact atomic claim by what its sentence states and by the conditions that let a reader decide it.
* The exact ClaimGraph located through the subject pattern supplies the referenced object's predicate and obtaining conditions; it does not choose the claim's quadrant.
* When permission wording is present, use the single permission-word branch in §8.4.1. It separates the possible jobs of that wording without inventing a common “permission result” kind.

**Normative rule (single quadrant).** Each **atomic** boundary claim **MUST** be assigned exactly one job under L/A/D/E. Recover an unresolved meaning before assigning it. A condition or reference within one coherent claim does not by itself add another asserted claim.

**Normative rule (mixed claims).** A conforming boundary text **SHALL** separate independently asserted claims with different jobs. For example, a duty to enforce an entry rule and a report of one enforcement result have separate D and E claims referring to the A rule. Preserve the logical connection when splitting the wording.

#### A.6.B:4.3 — Canonical placements in the Signature Stack

The quadrants have canonical placements in the boundary stack:

* **L → Signature layer:** `U.Signature.Laws` (and mechanism‑local semantic laws if present).
* **A → Mechanism layer:** `U.Mechanism.AdmissibilityConditions` (entry gates / runtime admissibility predicates).
* **D → Deontics & Commitments layer:** atomic claims about a generic prescription or about one separately obtaining individual duty, recommendation-as-duty, prohibition, or commitment. When permission wording is live, §8.4.1 decides whether its claim also belongs here.
* **E → Work-Effects & Evidence layer:** truth-conditional claims whose satisfaction requires actual work, evaluation, observation, or produced carriers.

A publication face **MUST NOT** introduce new semantic claims outside this L/A/D/E-classified claim set. **E.17 (MVPK)** enforces this rule for publication faces and their selected profiles.

#### A.6.B:4.4 - Develop a boundary explanation for its receiving use

Start with the boundary passage, its available sources and the reader's question. The square helps recover what each claim contributes and what would settle it. The explanation connects the claims needed for the reader to interpret, use or change that boundary.

**1. Recover the question and the claims already made.** Establish which understanding or decision the text must support. Interpreting a metric, deciding whether a request may enter and determining whether a duty was fulfilled need different answers. Recover the draft's asserted content, modality and scope. If a word such as *guarantees* leaves the intended assertion open, use A.6.C:4.3 with the author or source to resolve that meaning. Keep a consequential unresolved meaning explicit until its source is available.

**2. Establish the grounds of the answer.** Split independently asserted jobs and classify them through §§4.1–4.3. Use the detailed procedure and conditional permission-word branch in §8.4.1 where needed. Recover the definition for a meaning claim, the declared predicate for an entry condition, the normative or constitutive basis for a duty or grant, and the facts for an occurrence or finding. Preserve the source's conditions and qualifications. A missing ground requires a targeted return to the source or the responsible practice. If the work calls for a new rule or commitment, develop and establish it through its governing practice before treating it as current boundary content.

**3. Select the claims and detail on which the reader's answer depends.** Work backward from that answer. A reported measurement needs its quantity, population, conditions and interpretation; judging fulfilment of a commitment additionally needs that commitment and its comparison rule. Follow such dependencies until the remaining premises are supplied by the text or by references the intended reader can obtain and understand. Use §6 for their actual relations. Include a detail when changing it could change the answer, when it explains why a step follows, or when the reader needs it to perform the stated use. A complete four-quadrant account is warranted when the question actually crosses all four jobs. Keep other valid claims in their canonical sources for their own uses.

**4. Compose the explanation around that reasoning.** State the answer in the reader's working terms, connect its supporting claims, and make the conditions that limit its use recoverable. Place a definition beside the claim that needs it and an observation beside the inference it supports. IDs or canonical locations preserve material dependencies under §6.1; the accompanying explanation supplies their meaning for this reader. Use a Claim Register or separate Tech and Plain forms when the reuse or publication conditions call for them. Selection and recomposition preserve the source claims; a new semantic constraint first needs its own canonical claim.

**5. Return the text to the reader's work.** Follow the intended interpretation or decision using the explanation. Identify any consequential premise the reader would still have to invent, obtain that premise or state the precise unresolved question, and revise the affected connection. Consider a relevant change of condition: show which claim must be reconsidered and which grounds remain usable. Stop when the text supports the assigned understanding or decision with its actual limits. A later question can require a different selection from the same canonical claims.

The cases in §8.4 show these authoring choices. Their claims about latency, coaxiality and project entry are the material being explained; the reusable operation is selecting and connecting that material for a reader's question.

