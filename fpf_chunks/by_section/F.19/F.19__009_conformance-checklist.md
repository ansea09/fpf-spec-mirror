---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:7"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__009_conformance-checklist.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:7 — Conformance checklist"
line_start: 98855
line_end: 98875
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
| `CC-F19-2` | The repair separates apparatus from content by the values named in `KindAndClaimMap`, `ActionGuidingClaimDetails`, and `FlowPosition`; lexical dislike is not enough. Role- and function-shaped wording remains content until `E.10.ROLE` or `A.6.F` recovers the actual claim. |
| `CC-F19-3` | Apparatus is removed or moved before wording-use precision restoration is applied to the remaining content. |
| `CC-F19-4` | Content-bearing wording remains content and is repaired by `E.10`, `E.10.ARCH`, `F.18`, or the specific pattern that defines, constrains, or tests the remaining claim rather than deleted as style. |
| `CC-F19-5` | A removed apparatus word is not replaced by a synonym, metonymy, role label, container word, or status word that carries the same hidden apparatus. |
| `CC-F19-6` | Established FPF terms are preserved unless a named precision-restoration or naming pattern changes them. |
| `CC-F19-7` | Every accepted rewrite includes a `KindPreservationCheck`; a change to object kind, relation or claim kind, current slot, relation position, use, scope, or a live action-guiding discriminant without an accepted decision remains a blocker. |
| `CC-F19-8` | Development, evaluation, projection, landing, use-found, repair, and source-management evidence stay in the evidence, projection, release, or publication loci that carry them unless the text is about that flow object. |
| `CC-F19-9` | The accepted rewrite is shorter or clearer without losing technical semantics or action-guiding detail. A longer rewrite is admissible only when it recovers a hidden kind, relation, role or assignment distinction, function claim, slot, claim boundary, quantity, threshold, polarity, order, timing, criterion, tolerance, exception, or applicability condition needed by the declared use. |
| `CC-F19-10` | The repair records any loss of truth, action, stop criterion, value, usability, locality, currentness, kind recoverability, or explicit operational detail used by the declared reader. |
| `CC-F19-11` | Term-source or type annotation is used only when it changes the object, kind, relation, slot, use, publication boundary, admissible use, or rule the reader must apply; stable ordinary prose is not expanded into type labels. |
| `CC-F19-12` | The accepted plain rewrite passes MG-DA cold-reader recovery: a reader without the `DRR`, campaign notes, or author memory can state the content-bearing object, kind or ordinary status, relation or claim position, admissible use, next practical action, and every quantity, threshold, ordering, timing, criterion, exception, or applicability condition that changes that action. When another pattern contributes, the reader can recover its id and contribution. Broad heads such as `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, and unqualified `specialization` are not plain enough when they hide what the practitioner must recognize. |
| `CC-F19-13` | Every added qualifier or formal identity has a named live contrast: it changes truth, action, stop, migration, publication, reuse, or reliance. An ordinary PatternID citation does not by itself require a `ClaimGraph`, `U.MethodDescription`, `U.Method`, actor, assignment, or `U.Work` expansion. |
| `CC-F19-14` | After apparatus removal, the sentence names every complement and live discriminant needed to determine what was selected, changed, compared, transformed, published, evaluated, relied on, started, stopped, ordered, limited, or excepted. |
| `CC-F19-15` | Ordinary practitioner action and instrumental “use pattern X” wording stays ordinary when it does not assert identity-bearing dated Work. When it does, point to the basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. Use one thin `E.10.ROLE` or `A.6.F` route for a role- or function-shaped trigger; do not copy either recovery taxonomy. `U.MethodDescription` appears only after the `A.3.2` test passes. |
| `CC-F19-16` | A heterogeneous list is split when its members need different heads or predicates; the rewrite uses `E.10:0.2c.17` instead of inventing one umbrella head. |

