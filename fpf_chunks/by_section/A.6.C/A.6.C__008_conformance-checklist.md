---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__008_conformance-checklist.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:7 — Conformance Checklist"
line_start: 10359
line_end: 10387
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

### A.6.C:7 — Conformance Checklist

A boundary description conforms to A.6.C iff it satisfies all items below:

1. **CC‑A.6.C‑1 (Unpacking when contract-language appears).**
   If the text uses “contract”, “guarantee”, “promise”, or “SLA” language, it **SHALL** explicitly disambiguate the statement as referring to at least one of: **Promise content**, **Utterance** (published description), **Commitment** (duty/recommendation/prohibition), **Permission** (exact `A.2.8.PER` result), or **Performed work and evidence** (adjudication).

2. **CC‑A.6.C‑2 (No agency to epistemes).**
   The text **MUST NOT** attribute promising, committing, or obligating agency to signatures, mechanisms, interfaces, or documents. Any duty or commitment **SHALL** name an accountable role assignment, `U.Role`, or admitted acting system.

3. **CC‑A.6.C‑3 (Classify contract-language statements via A.6.B).**
   Contract-language statements **SHALL** be classifiable as atomic claims to **L/A/D/E**, with dependencies expressed by explicit references rather than paraphrase.

4. **CC‑A.6.C‑4 (Promise content ≠ Work discipline).**
   Statements about what is executed or observed **SHALL** be expressed as **E** claims about work, evidence, and carriers. Promise-content language **SHALL** refer to the **promise content** (`U.PromiseContent`, A.2.3) and its **L-defined** semantics (and to explicit `D-*` commitments represented as `U.Commitment`, A.2.8), not to execution events (`U.Work`) or runtime effects.
   Unqualified head‑noun *service* (and the co‑moving cluster *service provider* and *server*) in normative boundary prose SHALL be unpacked per **A.6.8 (RPR‑SERV)**.

5. **CC‑A.6.C‑5 (Evidence hook for operational guarantees).**
   If a “guarantee” is operational (requires reality to decide), the text **SHALL** include an **E** claim that states what evidence would adjudicate it, with the evidence carrier or evidence claim named when current.

6. **CC‑A.6.C‑6 (No second contracts via faces).**
   MVPK faces **MUST NOT** add new commitments or permission results beyond the underlying L/A/D/E-classified claims; faces may only project, summarize, or select from the canonical claim set under a viewpoint.

7. **CC‑A.6.C‑7 (RFC‑keyword discipline inside faces).**
   If an MVPK face contains BCP‑14 norm keywords, each sentence **MUST** cite the underlying classified claim ID and direct object: `U.Commitment` for duty/recommendation/prohibition or the exact `A.2.8.PER` result for permission. If it cannot, the face is non-conformant until rewritten without the BCP‑14 keyword or moved out of the face.

8. **CC‑A.6.C‑8 (No commitment-by-publication default).**
   A `Publish` or `Approve` utterance, including publication of a `…Spec`, MUST NOT be treated as instituting `U.Commitment` or `GrantedPermissionRelation@Context` by default. If a Context policy maps publication acts to deontic effects, the policy SHALL be cited; every resulting duty/recommendation/prohibition remains an explicit `U.Commitment` with an accountable subject, and every resulting strong grant remains an explicit `A.2.8.PER` relation occurrence with its exact beneficiary and ground.

