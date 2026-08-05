---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:7"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__009_conformance-checklist.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:7 — Conformance checklist"
line_start: 97150
line_end: 97166
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

### F.19:7 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-F19-1` | The repair names the text span and visible apparatus candidates before rewriting. |
| `CC-F19-2` | The repair separates apparatus from content by object, kind, claim or relation kind, current ontic slot, relation position, use relation, publication relation when it changes admissible use, concerned actor or reader role when a role is current, and flow position when flow separation matters; lexical dislike is not enough. |
| `CC-F19-3` | Apparatus is removed or moved before wording-use precision restoration is applied to the remaining content. |
| `CC-F19-4` | Content-bearing wording remains content and is repaired by `E.10`, `E.10.ARCH`, `F.18`, or the governing pattern rather than deleted as style. |
| `CC-F19-5` | A removed apparatus word is not replaced by a synonym, metonymy, role label, container word, or status word that carries the same hidden apparatus. |
| `CC-F19-6` | Established FPF terms are preserved unless a named precision-restoration or naming pattern changes them. |
| `CC-F19-7` | Every accepted rewrite includes a `KindPreservationCheck`; a wording change that changes object kind, relation kind, claim kind, current ontic slot, relation position, use relation, admissible use, or scope without an accepted decision remains a blocker. |
| `CC-F19-8` | Development, evaluation, projection, landing, use-found, repair, and source-management evidence stay in their owning evidence, projection, release, or publication loci unless the text's own object of concern is that flow object. |
| `CC-F19-9` | The accepted rewrite is shorter or clearer without losing technical semantics; a longer rewrite is admissible only when it recovers a hidden kind, relation, role, slot, or claim boundary. |
| `CC-F19-10` | The repair records any value, usability, locality, currentness, or kind-recoverability loss. |
| `CC-F19-11` | Term-source or type annotation is used only for wording whose source ontology can change the object, kind, relation, current ontic slot, relation position, use relation, publication relation, admissible use, or governing pattern; stable ordinary prose is not expanded into type labels. |
| `CC-F19-12` | The accepted plain rewrite passes MG-DA cold-reader recovery: a reader without the `DRR`, campaign notes, or author memory can state the content-bearing object, kind or ordinary status, relation or claim position, admissible use, and next governing pattern. Broad heads such as `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, and unqualified `specialization` are not plain enough when they hide the object a practitioner must recognize. |

