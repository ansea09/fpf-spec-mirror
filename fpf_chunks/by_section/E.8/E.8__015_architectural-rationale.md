---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__015_architectural-rationale.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:10 — Architectural Rationale"
line_start: 73731
line_end: 73745
dependencies:
  - "E.10"
  - "E.10.MOVE"
  - "E.11.PFP"
  - "E.11.PUR"
  - "E.13"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4.DPF"
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

### E.8:10 - Architectural Rationale
Structure and style function as FPF’s *grammar*. By unifying what were
once separate “template” and “style guide” patterns, authors face a
single reference point that satisfies:

* **P‑1 Cognitive Elegance** – uniform, minimal surprises.
* **P‑2 Didactic Primacy** – narrative flow, dual archetype examples.
* Guard‑Rails 1 & 2 – no tool jargon, no notation lock‑in inside prose.

A unified template also improves retrieval: a chunk containing `A.2:<n> - Bias‑Annotation` remains self‑identifying even when parent headings are missing, and the required footer marker makes truncation detectable.

The ASCII ` - ` separator in H-2 keeps heading entry inexpensive: authors can type it directly on ordinary keyboards, and readers can reuse the same characters in search and plain-text tools. Typographic dash variants require an extra input or conversion step while adding no information to the boundary between an identifier and its title. Where a prose dash is useful, `--` is a keyboard-accessible option; the identifier/title separator remains ` - `.

International and industry standards often speak in terms of *conformance criteria*. FPF uses the label **Conformance Checklist** to make adoption easier for engineers and managers.

