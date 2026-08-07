---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:8"
section_title: "Common anti-patterns and how to avoid them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:8 — Common anti-patterns and how to avoid them"
line_start: 97412
line_end: 97428
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
| Hypergeneric repair | The rewrite uses `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or `specialization` to sound precise while hiding the actual object, relation, rule, or action. | Restore the practitioner-recognizable object and relation; for specialization, say what specializes what and which inherited or changed slots or uses matter. |
| Plain-language drift | Smooth prose drops the kind named by value or admissible-use boundary. | Remove apparatus first, then restore remaining wording precision before shortening. |
| Flow smuggling | Development, projection, landing, or evaluation evidence is written as user-facing guidance. | Move the evidence to the review record, quality result, projection record, release document, or other governing evidence document and keep only the resulting user-facing action or boundary. |
| Role label as ontology | A role label replaces the object kind. | Name the object kind; state the role relation only when it changes the claim. |
| Slot label as ontology | A slot, field, relation-position, or use-relation label replaces the object kind, or the same object in several slots or relation positions is treated as several kinds. | Preserve object kind, slot, relation position, and use separately; cite the specific pattern only when its definition, constraint, or test is needed. |
| Apparatus-looking data structure | A record, card, table, schema, dashboard, or data-structure word is kept because it sounds precise, but it does not carry the EntityOfConcern, slot relation, publication boundary, admissible use, or next action. | Remove it, or use `E.24.CD`, `E.24.PUB`, or the specific content pattern when the structure really carries a candidate-ontic, publication, or domain relation. |
| Negative catalogue | The sentence defines an object by listing what it is not. | Lead with the positive object and action; keep only local documented confusion and named stop condition. |
| Over-annotation as precision | The rewrite replaces a clear domain sentence with type labels, source-ontology tags, or slot names that do not change the claim. | Keep the domain sentence and annotate only the term or relation under repair. |
| Triggerless formal expansion | A PatternID citation becomes `exact/direct/current subject owner`, `ClaimGraph`, Method, actor, assignment, or Work language even though no alternative identity changes the claim. | Keep the ordinary citation and action. Open the formal branch only after naming the contrast or later use that consumes it. |
| Overformalized precision | The rewrite preserves all terms but makes the sentence harder to think with or generalize from. | Keep the content-bearing kind and claim, drop non-governing apparatus, and use a plain technical sentence plus reference named by value where needed. |
| Apparatus-preserving paraphrase | A rewrite changes wording but keeps the same status, process, or quality-proof apparatus. | Return to the apparatus-and-content split and repair by value. |

