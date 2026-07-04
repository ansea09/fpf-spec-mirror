---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__006_solution.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:4 — Solution"
line_start: 87404
line_end: 87457
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

### F.19:4 - Solution

Use `OntologyFirstPlainRewrite` as a five-step repair over one bounded span.

1. **Bound the span.** Name the sentence, row, paragraph, or small section under repair. Name visible apparatus candidates: pattern-application drift, role label, container word, status word, process trace, quality proof, negative catalogue, reference boilerplate, record, card, table, schema, data-structure wrapping, or other overwrap.
2. **Separate content from apparatus by ontology.** For each phrase part, ask what object, head kind, claim kind or relation kind, current ontic slot, relation position, use relation, publication relation, admissible use, concerned actor or reader role when a role is current, and design, run, or coupled-flow position when flow separation matters. If a phrase part changes one of those values, keep it as content. If it only restates process, role label, negative catalogue, reference boilerplate, record, card, table, schema, data-structure wrapping, or quality proof without changing content, classify it as apparatus.
3. **Remove or move apparatus.** Delete the apparatus or move it to the document, record, note, or publication relation where it belongs: `DRR`, review record, quality result, architecture note, README, ToC, `E.11`, or `I.2` entry locus, projection record, release or landing evidence document, or source-side note. Do not replace it with a smoother synonym, role label, container word, status word, record, card, table, schema, data-structure wrapper, or publication-form word.
4. **Restore remaining content precision.** Apply `E.10`, `E.10.ARCH`, `F.18`, or the governing pattern when a remaining word, head, relation, claim, current ontic slot, relation position, use relation, source-use relation, durable name, or admissible-use boundary is still hidden.
5. **Rewrite and check loss.** Write the shortest plain technical sentence that preserves the repaired object, kind, claim, relation, action, current ontic slot, relation position, use relation, actual role value when current, flow position when current, established term, and admissible use. The rewrite fails if it changes one of those values without an accepted semantic decision, or if it becomes harder for the declared reader to use.

Keep ontology visible only where it carries the sentence. A term-source or type annotation is needed when the wording can change the object, kind, relation, current ontic slot, relation position, use relation, publication relation, admissible use, or governing pattern. A record, card, table, schema, data structure, dashboard, or named form remains apparatus unless it carries one of those values. If ordinary domain wording already preserves those values, keep the ordinary sentence. "The aircraft flies" is better than a typed expansion unless the flight function, system kind, or slot relation is under repair.

Use the full result form when the repair must be inspectable; otherwise a local rewrite plus the kind-preservation check is enough.

#### F.19:4.1 - Result form

| Field | Meaning |
|---|---|
| `TextSpanRef` | Bounded span under repair. |
| `ApparatusCandidateSet` | Visible pattern-application, role, record, card, table, schema, data-structure wrapping, locus, flow, status, process, negative-catalogue, reference, or quality-proof apparatus candidates. |
| `ContentCandidateSet` | Phrase parts that may carry object, kind, claim, relation, current ontic slot, relation position, use relation, actual role value when current, flow position, evidence-use value, or user-facing action. |
| `ObjectOfConcern` | Object the span is about. |
| `KindAndClaimMap` | Head kind, claim kind, relation kind, current ontic slot, relation position, use relation, publication relation when it changes admissible use, scope, and governing pattern when another pattern governs a specific outside claim. |
| `ConcernAndFlowPosition` | Concerned actor or reader role only when a role is current; design, run, or coupled-flow position when it changes meaning. |
| `ApparatusDisposition` | Removed, moved, retained as content, or blocker when separation is not yet possible. |
| `RemainingContentPrecisionRestoration` | `not needed`, `E.10`, `E.10.ARCH`, `F.18`, governing pattern, or blocker. |
| `PlainRewrite` | Short rewrite after apparatus removal and remaining-content precision restoration. |
| `KindPreservationCheck` | Pre-rewrite and post-rewrite object kind, relation or claim kind, current ontic slot, relation position, use relation, admissible use, and scope; disposition is `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. |
| `LossCheck` | What became worse, less local, less current, less recoverable, or less usable if the rewrite is accepted. |

#### F.19:4.2 - Pattern-prose specialization

When the repaired prose is an FPF pattern, apply the same algorithm with one role test:

> Does this sentence address the pattern's intended user, or does it record development, review, projection, landing, quality, or source-management evidence about the pattern version?

If it records evidence about the pattern version, keep that evidence outside the pattern unless the pattern's own primary `EntityOfConcern` is that evaluation or projection object. The evidence can cause edits to the pattern; it is not automatically pattern content.

Pattern prose keeps:

- the pattern's own primary `EntityOfConcern`;
- the first useful move;
- the practical delta and cost of missing it;
- local boundary prose only for a documented local confusion and named stop condition;
- short declarative references to related patterns after the pattern's own content is visible.

Pattern prose moves out:

- package-placement rationale;
- correspondence about producing the draft rather than using the pattern;
- quality-status proof;
- README, ToC, `E.11`, `I.2`, retrieval, card, monolith-parity, or landing evidence;
- repeated boundary doctrine already carried by another pattern.

