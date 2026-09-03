---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:8"
section_title: "Common anti-patterns and how to avoid them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:8 — Common anti-patterns and how to avoid them"
line_start: 100654
line_end: 100679
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
| Hypergeneric repair | The rewrite uses `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or `specialization` to sound precise while hiding the actual object, relation, rule, or action. | Restore the practitioner-recognizable object and relation; for specialization, say what specializes what, by which specialization relation, and which inherited or changed slots or uses matter. |
| Plain-language drift | Smooth prose drops the kind named by value or admissible-use boundary. | Remove apparatus first, then restore remaining wording precision before shortening. |
| Flow smuggling | Development, projection, landing, or evaluation evidence is written as user-facing guidance. | Move the evidence to the review record, quality result, projection record, release document, or other appropriate evidence document and keep only the resulting user-facing action or boundary. |
| Role-shaped label as ontology | The word *role* is treated as one technical value or replaces the object kind. | Keep the phrase as content; use `E.10.ROLE` when ordinary reading leaves the actual claim unresolved; do not infer a branch from the word alone. |
| Function-shaped label as ontology | The word *function* is treated as one technical value or as proof of functioning, capability, assignment, or Work. | Keep the phrase as content; use `A.6.F` when ordinary reading leaves the claim unresolved; allow metonymy or several simultaneous readings without copying its dispatch here. |
| False common head | One grammatical subject is made to select, compare, carry, publish, and evaluate unlike things. | Split the claims using F.19:4's coordination-and-list move; use `E.10:0.2c.17` for unresolved FPF meaning and retain only heads that fit every listed member. |
| Slot label as ontology | A slot, field, relation-position, or use-relation label replaces the object kind, or the same object in several slots or relation positions is treated as several kinds. | Preserve object kind, slot, relation position, and use separately; cite the specific pattern only when its definition, constraint, or test is needed. |
| Apparatus-looking data structure | A record, card, table, schema, dashboard, or data-structure word is kept because it sounds precise, but it does not carry the EntityOfConcern, slot relation, publication boundary, admissible use, or next action. | Remove it, or use `E.24.CD`, `E.24.PUB`, or the specific content pattern when the structure really carries a candidate-ontic, publication, or domain relation. |
| Unsupported negative classification | The sentence introduces one or more alternative classes only to reject them, although the exact reading fails F.19:4's grounded-contribution test. | State the positive object and action. Retain a negative alternative only under the full independent-ground, plausible-reader, contribution, and smallest-clear-correction test. |
| Over-annotation as precision | The rewrite replaces a clear domain sentence with type labels, source-ontology tags, or slot names that do not change the claim. | Keep the domain sentence and annotate only the term or relation under repair. |
| Triggerless formal expansion | A PatternID citation becomes an “exact direct current subject owner”, `ClaimGraph`, Method, actor, assignment, or Work claim even though no alternative identity changes the result. | Keep the ordinary citation and action. Open the formal branch only after naming the contrast or later use that consumes it. |
| Overformalized precision | The rewrite preserves all terms but makes the sentence harder to think with or generalize from. | Keep the content-bearing kind and claim, drop apparatus that changes neither, and use a plain technical sentence plus a reference named by value where needed. |
| Apparatus-preserving paraphrase | A rewrite changes wording but keeps the same status, process, or quality-proof apparatus. | Return to the apparatus-and-content split and repair by value. |
| Truthful noise | A true denial or caveat answers an implausible question introduced by the sentence itself. | Remove the invented question and state the positive claim or action. |
| Impossible agency under denial | An incapable subject receives a predicate only so the prose can deny it. | Name the capable participant and allocate the action positively. |
| Missing operand as elegance | A verb or relational noun omits the value that determines the operation or relation. | Restore the participant unless one intended value is cheaply and uniquely local. |
| Enumeration as coverage | Examples, near-synonyms, abstract pairs, or several kinds simulate breadth but do not state a usable proposition. | Put the proposition first; mark examples; retain only independently consequential members. |
| Locally valid accumulation | Every pair or modifier passes alone, but nested coordination creates a catalogue and delays the message. | Summarize, subordinate, split, or delete by contribution and foreground the governing clause. |
| Trigger as verdict | A word list bans normal metonymy, negation, long sets, or expressive prose, or its silence is treated as clearance. | Use triggers only to locate candidates; decide from the whole span and declared use. |
| Checklist explosion | One semantic reading becomes separate forms or progress items for valency, agency, kind, referent, lists, and style. | Perform one connected repair and return the repaired text; use comparison evidence when the receiving decision needs it. |

