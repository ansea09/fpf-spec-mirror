---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__002_use-this-when.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:0 — Use this when"
line_start: 100425
line_end: 100457
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

### F.19:0 - Use this when

Use `F.19` when a bounded piece of technical prose is harder to understand or use than its intended claim requires. The sentence may be grammatical and every isolated statement may be true, yet the reader still has to invent a missing operand, accept an implausible relation, guess what a pronoun or relational noun refers to, interpret a list with no stated purpose, or wait through caveats and ornament before reaching the governing message.

Common signs are:

- a verb or relational noun whose needed participant is not cheaply recoverable;
- a grammatical subject that cannot bear the asserted predicate, even when that predicate appears inside a denial;
- a contrast, warning, or guard against a reading that no plausible intended reader has reason to make;
- one head or predicate imposed on unlike members;
- examples presented as a classification, or a catalogue presented instead of a proposition; and
- coordination repeated inside phrases and across clauses, or stacked modifiers, when one governing statement would do.

Item count is only a cue. Two coordinated members can already be needless, while a long inventory can be exact and useful when its kind, membership rule, and closure matter. Matching kinds and individually relevant members do not by themselves justify a series: the reader must need to distinguish or retain the members together for the intended use.

Apply the same method to FPF pattern prose and to other technical prose whose accepted domain terms, relations, claim boundaries, or use conditions must survive simplification.

**What goes wrong if missed.** The prose looks careful while introducing relations, alternatives, or branches that the work does not need. A later author or generator may then copy that shape as an acceptable technical style.

**What this buys.** The reader reaches the supported object, claim, and action sooner. Required technical distinctions remain; invented foils, false agency, reference puzzles, and catalogue rhetoric do not.

**First useful move.** State in one plain sentence what the intended reader must recognize, understand, decide, or do. Then read the whole natural span against that sentence before changing individual words.

**Not this pattern when.**

- If only one already-visible FPF word or head has an unresolved technical use, take the exact `E.10` route for it.
- If the question is a durable reusable name, use `F.18`.
- If source prose is only being observed and not admitted into governed technical prose, keep the observation source-side.
- If evocation, rhythm, ambiguity, or parallelism is the declared work of a poem, quotation, ceremonial passage, or other expressive genre, do not flatten it into technical instruction. Apply `F.19` only to the technical claim or action that must remain recoverable.
- If a language-specific grammar or idiom remains after the common semantic repair, use the applicable language profile.

**Primary EntityOfConcern in plain terms.** One sentence, row, paragraph, list, or small coherent section being repaired into precise plain technical prose.

