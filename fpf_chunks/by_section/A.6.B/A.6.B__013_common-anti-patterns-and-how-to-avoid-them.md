---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:11"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:11 — Common Anti‑Patterns and How to Avoid Them"
line_start: 10939
line_end: 10949
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
  - "Keeps claim text"
  - "MAY"
  - "MUST"
  - "MUST NOT"
  - "MUST NOT hide a gate predicate (that is A-)"
  - "SHALL"
  - "SHOULD"
  - "SHOULD NOT"
  - "The key words MUST"
  - "a duty or commitment D- claim MUST name its accountable subject"
  - "accountable norms and grants"
  - "actual exercise"
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
  - "institutional obtaining"
  - "laws"
  - "may"
  - "neither claim text makes its object obtain. An E-* claim MUST name the work"
  - "not a duty.)"
  - "not normative"
  - "observable effects and evidence"
  - "or (iii) assert evidence existence or measurement outcomes (those are E-*)"
  - "or (iii) assign responsibility or enforcement (that is D-*)"
  - "or MAY) as operators inside the law or definition itself"
  - "or observation that settles it and any evidence used for reliance"
  - "they report adjudicable results rather than obligations"
  - "while a grant D- claim MUST satisfy the participant and ground test in §8.4.1"
  - "“commits to”)"
  - "“is admissible”"
  - "“is blocked”"
  - "”) used as operators inside L- or A- predicates (should be D- that references L-/A-)"
---

### A.6.B:11 - Common Anti‑Patterns and How to Avoid Them

| Anti‑pattern                 | Symptom                                            | Why it fails                                                | Repair (square‑consistent)                                                                  |
| ---------------------------- | -------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Gate‑as‑law**              | Preconditions written as “laws”                    | Collapses signature or mechanism boundary; breaks substitution | Move to `A-*` in Mechanism.AdmissibilityConditions; reference `L-*` terms.                  |
| **Deontics in predicates**   | “MUST” inside definitions or gates                 | Confuses governance with truth or admissibility                | Rewrite as `L-*`/`A-*` predicate; add `D-*` duty referencing it.                            |
| **Interface‑as‑promiser**    | “The API promises or guarantees …”                    | Category error: interface descriptions do not commit              | Identify committing role assignment or admitted acting system (`D-*`), measured property (`E-*`), and metric definition (`L-*`); use `A.6.C` when contract or promise-content unpacking is live. |
| **Evidence‑free guarantees** | “Guaranteed p95 latency” with no measurement story | Unadjudicable; turns into marketing                         | Create `E-*` with carriers + conditions; link commitment as `D-* → E-*`.                    |
| **Paraphrase drift**         | Same rule restated across faces                    | Divergence becomes invisible                                | Use IDs; faces cite IDs; optional Claim Register.                                           |
| **View‑fork semantics**      | A face introduces new L/A/D/E content              | Violates “no new semantics” publication discipline          | Move new claim into canonical layer (L/A/D/E) or mark as informative only.                  |

