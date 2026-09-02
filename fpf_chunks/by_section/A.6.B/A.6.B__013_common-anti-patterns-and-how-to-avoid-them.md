---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:11"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:11 — Common Anti‑Patterns and How to Avoid Them"
line_start: 11732
line_end: 11742
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

### A.6.B:11 - Common Anti‑Patterns and How to Avoid Them

| Anti‑pattern                 | Symptom                                            | Why it fails                                                | Repair (square‑consistent)                                                                  |
| ---------------------------- | -------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Gate‑as‑law**              | Preconditions written as “laws”                    | Collapses signature or mechanism boundary; breaks substitution | Move to `A-*` in Mechanism.AdmissibilityConditions; reference `L-*` terms.                  |
| **Deontics in predicates**   | “MUST” inside definitions or gates                 | Confuses governance with truth or admissibility                | Rewrite the definition or gate as `L-*`/`A-*`; add a generic `D-*` prescription or an independently established individual-duty claim when current. |
| **Interface‑as‑promiser**    | “The API promises or guarantees …”                    | Category error: interface descriptions do not commit              | Recover the exact policy and generic prescription, or the actual bearer and separately obtaining `U.Commitment` when an individual duty is claimed; keep measured property (`E-*`) and metric definition (`L-*`) separate, and use `A.6.C` for promise-content or agreement-like wording. |
| **Evidence‑free guarantees** | “Guaranteed p95 latency” with no measurement story | Unadjudicable; turns into marketing | Create `E-*` with carriers and conditions; link the exact generic prescription or individual-duty claim as `D-* → E-*`. |
| **Paraphrase drift**         | Same rule restated across faces                    | Divergence becomes invisible                                | Use IDs; faces cite IDs; optional Claim Register.                                           |
| **View‑fork semantics**      | A face introduces new L/A/D/E content              | Violates “no new semantics” publication discipline          | Move new claim into canonical layer (L/A/D/E) or mark as informative only.                  |

