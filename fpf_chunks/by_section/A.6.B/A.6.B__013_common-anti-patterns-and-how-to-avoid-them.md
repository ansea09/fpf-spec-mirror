---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:11"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:11 — Common Anti‑Patterns and How to Avoid Them"
line_start: 15296
line_end: 15306
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

### A.6.B:11 - Common Anti‑Patterns and How to Avoid Them

| Anti‑pattern                 | Symptom                                            | Why it fails                                                | Repair (square‑consistent)                                                                  |
| ---------------------------- | -------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Gate‑as‑law**              | Preconditions written as “laws”                    | Collapses signature or mechanism boundary; breaks substitution | Move to `A-*` in Mechanism.AdmissibilityConditions; reference `L-*` terms.                  |
| **Deontics in predicates**   | “MUST” inside definitions or gates                 | Confuses governance with truth or admissibility                | Rewrite the definition or gate as `L-*`/`A-*`; add a generic `D-*` prescription or an independently established individual-duty claim when current. |
| **Unresolved duty bearer** | “The API promises” is used for an individual duty without its actual bearer and commitment | The institutional claim cannot be settled from the interface wording | Recover the policy and generic prescription, or the actual bearer and separately obtaining `U.Commitment` when an individual duty is claimed. Keep measured property (`E-*`) and metric definition (`L-*`) separate; use `A.6.C` when ambiguity changes interpretation or use. |
| **Unestablished operational-result guarantees** | An asserted p95 result lacks its actual evaluation | The operational-result claim lacks the basis needed to settle it | Use `A.6.C:4.3` when the guarantee's meaning is ambiguous. For an operational result, state the actual Work, evaluation, or observation, predicate and object, scope/window, and result; if that basis is absent, leave the result unestablished. Add A.10 support and a `D-* → E-*` link only when the receiving reliance and duty claims need them. A carrier-existence observation alone does not complete the measured claim. |
| **Paraphrase drift** | A restatement changes the governing rule | Different faces can then imply different conditions or consequences | Reference the claim ID or canonical location and repair the explanation to preserve its meaning; use a Claim Register when useful. |
| **View‑fork semantics**      | A face introduces new L/A/D/E content              | Violates “no new semantics” publication discipline          | Put any new boundary claim in its canonical source before publishing it on a face. Mark explanatory commentary informative when it adds no boundary semantics.                  |

