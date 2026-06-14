---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:8"
section_title: "Common anti-patterns and how to avoid them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:8 — Common anti-patterns and how to avoid them"
line_start: 78273
line_end: 78286
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

### F.19:8 - Common anti-patterns and how to avoid them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Lexical paint | One umbrella word is replaced by another while the object kind stays hidden. | Recover the object kind and rewrite in the object's technical name. |
| Plain-language drift | Smooth prose drops the kind named by value or admissible-use boundary. | Remove apparatus first, then restore remaining wording precision before shortening. |
| Flow smuggling | Development, projection, landing, or evaluation evidence is written as user-facing guidance. | Move the evidence to its carrier and keep only the resulting user move or boundary. |
| Role label as ontology | A role label replaces the object kind. | Name the object kind; state the role relation only when it changes the claim. |
| Slot label as ontology | A slot, field, or use-position label replaces the object kind, or the same object in several slots is treated as several kinds. | Preserve object kind and slot/use-position separately and apply the governing pattern for the content-bearing relation, signature, lens, role, method, or work claim. |
| Negative catalogue | The sentence defines an object by listing what it is not. | Lead with the positive object and action; keep only local documented confusion and exact stop condition. |
| Over-annotation as precision | The rewrite replaces a clear domain sentence with type labels, source-ontology tags, or slot names that do not change the claim. | Keep the domain sentence and annotate only the load-bearing term or relation that is under repair. |
| Overformalized precision | The rewrite preserves all terms but makes the sentence harder to think with or generalize from. | Keep the content-bearing kind and claim, drop non-load-bearing apparatus, and use a plain technical sentence plus reference named by value where needed. |
| Apparatus-preserving paraphrase | A rewrite changes wording but keeps the same status, process, or quality-proof apparatus. | Return to the apparatus/content split and repair by value. |

