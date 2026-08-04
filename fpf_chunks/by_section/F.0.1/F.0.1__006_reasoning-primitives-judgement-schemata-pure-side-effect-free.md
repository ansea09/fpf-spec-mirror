---
chunk_kind: "child"
pattern_id: "F.0.1"
pattern_title: "Contextual Lexicon Principles"
section_id: "F.0.1:5"
section_title: "Reasoning Primitives (judgement schemata; pure, side‑effect‑free)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.1/F.0.1__006_reasoning-primitives-judgement-schemata-pure-side-effect-free.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "F.0.1 — Contextual Lexicon Principles"
  - "F.0.1:5 — Reasoning Primitives (judgement schemata; pure, side‑effect‑free)"
line_start: 89438
line_end: 89457
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.4"
  - "A.7"
  - "A.8"
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "U.BoundedContext"
  - "bridge"
  - "congruence"
  - "context"
  - "lexicon"
  - "local meaning"
  - "semantic boundary"
---

### F.0.1:5 - Reasoning Primitives (judgement schemata; pure, side‑effect‑free)

*These capture **allowable mental moves**; they do not prescribe storage, APIs, or workflow.*

* **Context qualification**
  `Context(C) ∧ mentions(C, s) ⊢ uses(s@C)`
  *Reading:* If a string *s* is used under Context *C*, we treat it as the local term *s\@C*.

* **Local sense formation**
  `uses(t@C) ∧ gloss_C(t) ⊢ SenseCell⟨t@C⟩`
  *Reading:* A Context‑true gloss yields a SenseCell for *t* inside *C*.

* **Admissible Cross‑context relation**
  `SenseCell⟨x@A⟩ ∧ SenseCell⟨y@B⟩ ∧ declare(rel, CL) ⊢ Bridge(x@A, y@B, rel, CL)`
  *Reading:* Only an explicit declaration generates a Bridge; no name‑matching inferences.

* **Bridge‑to‑Concept‑Set hint** *(for F.7)*
  `Bridge(x@A, y@B, rel≈equiv, CL≥k) ⊢ candidate_same_row(x, y)`
  *Reading:* High-CL, near‑equivalence bridges can *nominate* cells for one Concept‑Set row (final decision in F.7).

