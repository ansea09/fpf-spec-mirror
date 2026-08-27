---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__003_problem-frame.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:1 — Problem frame"
line_start: 98280
line_end: 98299
dependencies:
  - "A.19.SPR"
  - "A.6.P"
  - "A.7"
  - "C.16.P"
  - "C.2.P"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "F.18"
  - "I.2"
keywords:
---

### F.19:1 - Problem frame

Mature technical languages accumulate enough ontology that many bad sentences are not bad because the terms are unknown. They are bad because a simple technical claim is wrapped in process language, role language, status language, quality-proof evidence, pattern-reference boilerplate, or repeated negative distinctions.

The repair question is:

> What content remains when words that add no object, kind, relation, claim, system-role or function distinction, flow, evidence value, or user-facing action are removed?

Examples inside FPF:

- "`A.15` handles the claim" when the text needs to say that `A.15` applies to a work-planning claim;
- "pattern text" when the text means "the pattern" or "the pattern of concern";
- "governing relation" when the named object is a pattern, not a relation;
- long "not X, not Y, not Z" paragraphs when the text needs a positive object, action, and one stop condition;
- corpus-projection proof written inside a pattern whose own user-facing action is not corpus projection.

The same defect appears outside pattern prose. A system note may hide an evaluation claim inside process language; a project note may treat a dashboard as evidence authority when it is a publication form; an architecture memo may replace a scale-preference claim over alternatives with a platform label.

These failures confuse coupled transformation flows. A pattern under development, a pattern being applied, a quality evaluation of that pattern, a project work occurrence, a source publication, and a projection record are different objects. They may influence one another; they do not become one another by being mentioned in the same paragraph.

