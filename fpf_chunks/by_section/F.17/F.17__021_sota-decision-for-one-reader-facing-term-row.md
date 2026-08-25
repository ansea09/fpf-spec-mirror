---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:16"
section_title: "SoTA Decision for One Reader-Facing Term Row"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__021_sota-decision-for-one-reader-facing-term-row.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:16 — SoTA Decision for One Reader-Facing Term Row"
line_start: 96113
line_end: 96127
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
---

### F.17:16 - SoTA Decision for One Reader-Facing Term Row

Source use was checked on 2026-08-20. The bounded question is: **at the effort of settling one reusable term, what must a reader-facing row preserve beyond a familiar label, and what apparatus can be left out?** Source status is evidence about currentness, not a reason to select an architecture.

| Current line | Strong contribution | Limit at comparable one-row effort | FPF decision and receiving locus |
| --- | --- | --- | --- |
| [ISO 704:2022](https://www.iso.org/standard/79077.html), current published terminology-work standard | Separates objects, concepts, definitions, and designations and gives a disciplined route for concept systems, definitions, and term choice. | It does not identify an FPF governed value, exact episteme edition, local-sense basis relation, obtaining Bridge, bounded reuse claim, or publication occurrence. | **Adopt** value-before-label and one-decision terminology discipline in sections 4, 6, and 7. **Reject** a definition or designation as admission, identity, reuse authority, or availability. |
| W3C Ontology-Lexica Community Group, [*Lexicon Model for Ontologies: Community Report*](https://www.w3.org/2016/04/ontolex/), 2016, maintained community model rather than a W3C Standard | Separates lexical entry, form, lexical sense, and ontology reference; supports morphology, usage conditions, and explicit sense relations through semantics by reference. | A full ontology-lexicon and syntax graph is heavier than one FPF row, and the model does not decide FPF value admission, Bridge obtaining, reliance, or publication. | **Adapt** form/sense/reference separation in section 5.1 and the row schema. **Reject** mandatory full lexicon modeling and keep the exact FPF value, NameCard, cell, basis relation, and any Bridge as separate references. |
| W3C, [*SKOS Simple Knowledge Organization System Reference*](https://www.w3.org/TR/skos-reference/), Recommendation 2009, checked current on 2026-08-20 | Keeps concepts, preferred and alternative labels, notes, collections, semantic relations, and mapping relations distinct. | SKOS is a stable vocabulary baseline, but its compact label and mapping model does not carry FPF object identity, rich morphology, use-specific reliance, or publication boundaries. | **Retain as lineage** for label, note, collection, and mapping separation in sections 7, 10, and 13. Do not turn a generic mapping or shared label into an F.9 Bridge. |
| Zhu, Reinecke, and Mitra, [*Language Scent: Exploring Cross-Language Information Navigation*](https://arxiv.org/abs/2604.03604), 2026 preprint | Shows why contextual cues and recognizable local wording can help readers navigate. | The study is small, cross-language, and navigation-focused; recognizability proves neither referent identity nor cross-local equivalence. | **Adapt** its reader cue in worked wording and reader-use checks. **Reject** any inference from recognition to a second scheme, cell, Bridge, row, or publication occurrence. |

**Selected non-dominated contribution.** A plain glossary row costs less but loses the exact value, local sense, admitted and blocked uses, and reopen path. A full OntoLex graph preserves richer linguistic structure but normally costs more than the one-row reader-recovery use needs. F.17 keeps one row that refers separately to the already recovered value, NameCard, exact scheme-and-sense cell, any basis relation or obtaining Bridge, and a separate E.24.PUB availability package only when required. At this application effort, that separation gives more replayable reader recovery than a glossary without requiring a full ontology lexicon. This is a local effort/traceability result, not a claim that FPF supersedes terminology standards or OntoLex.

Currentness rule: when `F.2`, `F.3`, `F.5`, `F.7`, `F.8`, `F.9`, `F.10`, `F.14`, `F.15`, `F.18`, `C.2.1`, `E.17.0`, `E.24.UK`, `E.24.PUB`, `A.1.1`, `A.2`, `A.2.1`, `A.2.7`, `A.6.5`, `A.10`, `B.3`, `E.10.D2`, or the pattern that defines or constrains the governed value changes the value, kind, membership or obtaining rule, designation, scheme, cell, basis relation, Bridge, bounded-use claim, reliance, status and system-role boundary, edition relation, reference typing, or publication boundary, recheck only the affected rows and worked examples.

