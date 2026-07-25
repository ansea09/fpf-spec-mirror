---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:14"
section_title: "SoTA‑Echoing (post‑2015 practice alignment)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__016_sota-echoing-post-2015-practice-alignment.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:14 — SoTA‑Echoing (post‑2015 practice alignment)"
line_start: 10166
line_end: 10178
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

### A.6.B:14 — SoTA‑Echoing (post‑2015 practice alignment)

> **Informative.** Alignment notes; not normative requirements.

**Representative sources (post‑2015; illustrative).** See also A.6:11 for a fuller list.
* ISO/IEC/IEEE 42010:2022 (`U.View` and `U.Viewpoint` discipline).
* Leijen (2017) / Hillerström & Lindley (2018) (effects & handlers).
* OpenTelemetry Specification (v1.0+, 2021–) (evidence carriers as traces, logs, and metrics).

* **Effect systems & handlers:** clear separation between operation signature (L) and handler and runtime behavior (A/E), with governance duties (D) attached to accountable operators and implementers.
* **Behavioural and session typing:** protocol laws (L) and admissibility (A) remain distinct from commitments (D) and runtime traces (E), improving interpretability of “progress and safety” style boundary guarantees.
* **SRE and observability discipline:** treating traces, logs, and metrics as evidence carriers (E) and separating evidence semantics from retention and exposure duties (D) mirrors contemporary operational practice while staying tool‑agnostic.

