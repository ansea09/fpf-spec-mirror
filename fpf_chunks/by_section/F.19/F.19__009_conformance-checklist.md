---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:7"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__009_conformance-checklist.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:7 — Conformance checklist"
line_start: 97903
line_end: 97923
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
| `CC-F19-2` | The repair separates apparatus from content by object, kind, claim or relation kind, current ontic slot, relation position, use relation, publication relation when it changes admissible use, the exact system-role-kind, classification, assignment, other direct relation or ordinary wording recovered from any role-shaped phrase, the actual claim recovered from any function-shaped phrase, and flow position; lexical dislike is not enough. |
| `CC-F19-3` | Apparatus is removed or moved before wording-use precision restoration is applied to the remaining content. |
| `CC-F19-4` | Content-bearing wording remains content and is repaired by `E.10`, `E.10.ARCH`, `F.18`, or the specific pattern that defines, constrains, or tests the remaining claim rather than deleted as style. |
| `CC-F19-5` | A removed apparatus word is not replaced by a synonym, metonymy, role label, container word, or status word that carries the same hidden apparatus. |
| `CC-F19-6` | Established FPF terms are preserved unless a named precision-restoration or naming pattern changes them. |
| `CC-F19-7` | Every accepted rewrite includes a `KindPreservationCheck`; a wording change that changes object kind, relation kind, claim kind, current ontic slot, relation position, use relation, admissible use, or scope without an accepted decision remains a blocker. |
| `CC-F19-8` | Development, evaluation, projection, landing, use-found, repair, and source-management evidence stay in the evidence, projection, release, or publication loci that carry them unless the text is about that flow object. |
| `CC-F19-9` | The accepted rewrite is shorter or clearer without losing technical semantics; a longer rewrite is admissible only when it recovers a hidden kind, relation, system-role or assignment distinction, function or functioning claim, slot, relation position, or claim boundary. |
| `CC-F19-10` | The repair records any value, usability, locality, currentness, or kind-recoverability loss. |
| `CC-F19-11` | Term-source or type annotation is used only when it changes the object, kind, relation, slot, use, publication boundary, admissible use, or rule the reader must apply; stable ordinary prose is not expanded into type labels. |
| `CC-F19-12` | The accepted plain rewrite passes MG-DA cold-reader recovery: a reader without the `DRR`, campaign notes, or author memory can state the content-bearing object, kind or ordinary status, relation or claim position, admissible use, next practical action, and—when another pattern contributes—its id and contribution. Broad heads such as `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, and unqualified `specialization` are not plain enough when they hide what a practitioner must recognize. |
| `CC-F19-13` | Every added qualifier or formal identity has a named live contrast: it changes truth, action, stop, migration, publication, reuse, or reliance. An ordinary PatternID citation does not by itself require a `ClaimGraph`, `U.MethodDescription`, `U.Method`, actor, assignment, or `U.Work` expansion. |
| `CC-F19-14` | After apparatus removal, the sentence names every complement needed to determine what was selected, changed, compared, transformed, published, evaluated, or relied on. |
| `CC-F19-15` | Ordinary practitioner action and instrumental “use pattern X” wording stays ordinary when it does not assert identity-bearing dated Work. When it does, the text points to the complete A.15.1/F.6 basis. A local system-role kind and a separate System-classification judgment appear only for their own claims, and `U.MethodDescription` appears only after the `A.3.2` test passes. |
| `CC-F19-16` | A heterogeneous list is split when its members need different heads or predicates; the rewrite uses `E.10:0.2c.17` instead of inventing one umbrella head. |

