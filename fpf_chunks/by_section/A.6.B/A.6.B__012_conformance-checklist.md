---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:10"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__012_conformance-checklist.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:10 — Conformance Checklist"
line_start: 8353
line_end: 8364
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

### A.6.B:10 — Conformance Checklist

| ID                                       | Requirement                                                                                                                                                                                                      | Purpose                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **CC‑A.6.B.1 (Atomicity).**              | A conforming boundary text **SHALL** decompose mixed sentences into **atomic claims** such that each atomic claim belongs to exactly one quadrant **L/A/D/E**.                                                    | Makes L/A/D/E classification unambiguous; prevents contract soup.       |
| **CC‑A.6.B.2 (Quadrant routing).**       | Each atomic claim **MUST** be classified by the Boundary Norm Square and placed in its canonical stack placement (L→Signature.Laws; A→Mechanism.AdmissibilityConditions; D→Norms/Commitments; E→Evidence/Carriers). | Preserves stack modularity and evolvability.             |
| **CC‑A.6.B.3 (Form constraints).**       | `L-*` and `A-*` claims **MUST NOT** contain RFC deontic keywords as operators; `D-*` claims **MUST** name an accountable `U.Agent` or `U.Role`; `E-*` claims **SHOULD NOT** use RFC deontic keywords.                       | Keeps modalities separated and audit‑ready.              |
| **CC‑A.6.B.4 (Explicit references).**    | Where a claim depends on another L/A/D/E-classified claim, that dependency **MUST** be expressed by explicit ID reference rather than restating the other claim in new words.                                                | Prevents paraphrase drift across layers/faces.           |
| **CC‑A.6.B.5 (E‑claim adjudicability).** | Each `E-*` claim **SHOULD** include (a) observation conditions, (b) carrier class/schema reference, and (c) viewpoint/consumer.                                                                                  | Makes work‑effects adjudicable rather than aspirational. |
| **CC‑A.6.B.6 (No gate smuggling).**      | Operational admissibility predicates **MUST NOT** appear as `L-*` laws in the signature layer; they **MUST** be `A-*` claims in the mechanism layer.                                                             | Preserves substitution and signature stability.          |
| **CC‑A.6.B.7 (No upward dependencies).** | `L-*` claims **MUST NOT** reference `A-*`, `D-*`, or `E-*`; `A-*` and `E-*` claims **MUST NOT** reference `D-*`.                                                                                                   | Preserves layering and prevents hidden coupling.         |

