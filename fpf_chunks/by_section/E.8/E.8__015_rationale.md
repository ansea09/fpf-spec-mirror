---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__015_rationale.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:10 — Rationale"
line_start: 60616
line_end: 60628
dependencies:
  - "E.10"
  - "E.11"
  - "E.13"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.5.1"
  - "E.5.4"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.8.ECSPF"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
  - "). The key words MUST"
  - "MAY"
  - "MUST NOT"
  - "MUST NOT appear inside Definition:/Invariant:/Well-formedness constraint: blocks. When enforceable"
  - "Prevents ambiguity between obligation language and model validity"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SHALL"
  - "SHALL NOT"
  - "SHOULD"
  - "SHOULD NOT"
  - "and OPTIONAL are to be interpreted as described in RFC 2119"
  - "improves auditability"
  - "inside the predicate block"
  - "or other admissibility conditions of the modeled world"
  - "structural invariants"
  - "to state definitions"
  - "typing rules"
  - "“is required to”) in normative clauses"
---

### E.8:10 - Rationale
Structure and style function as FPF’s *grammar*. By unifying what were
once separate “template” and “style guide” patterns, authors face a
single reference point that satisfies:

* **P‑1 Cognitive Elegance** – uniform, minimal surprises.
* **P‑2 Didactic Primacy** – narrative flow, dual archetype examples.
* Guard‑Rails 1 & 2 – no tool jargon, no notation lock‑in inside prose.

A unified template also improves retrieval: a chunk containing `A.2:<n> - Bias‑Annotation` remains self‑identifying even when parent headings are missing, and the recommended footer marker makes truncation detectable.

International and industry standards often speak in terms of *conformance criteria*. FPF uses the label **Conformance Checklist** to make adoption easier for engineers and managers.

