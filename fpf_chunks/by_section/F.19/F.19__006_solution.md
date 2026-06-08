---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__006_solution.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:4 — Solution"
line_start: 75928
line_end: 75979
dependencies:
  - "A.19.SPR"
  - "A.6.P"
  - "A.7"
  - "C.16.P"
  - "C.2.P"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.18"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "F.18"
  - "J.4"
keywords:
---

### F.19:4 - Solution

Use `OntologyFirstPlainRewrite` as a five-step repair over one bounded span.

1. **Bound the span.** Name the sentence, row, paragraph, or small section under repair. Name visible apparatus candidates: pattern-application drift, role label, container word, status word, process trace, quality proof, negative catalogue, reference boilerplate, or other overwrap.
2. **Separate content from apparatus by ontology.** For each phrase part, ask what object, head kind, claim kind or relation kind, slot or use-position, admissible use, concerned role, and design/run or coupled-flow role it expresses. If a phrase part changes one of those values, keep it as content. If it only restates process, role label, negative catalogue, reference boilerplate, or quality proof without changing content, classify it as apparatus.
3. **Remove or move apparatus.** Delete the apparatus or move it to the carrier where it belongs: `DRR`, review record, quality result, architecture note, ToC/J.4, projection carrier, release/landing evidence carrier, or source-side note. Do not replace it with a smoother synonym, role label, container word, or status word.
4. **Restore remaining content precision.** Apply `E.10`, `E.10.ARCH`, `F.18`, or the governing pattern when a remaining word, head, relation, claim, slot/use-position, source-use role, durable name, or admissible-use boundary is still hidden.
5. **Rewrite and check loss.** Write the shortest plain technical sentence that preserves the repaired object, kind, claim/relation/action, slot/use-position, role, flow, established term, and admissible use. The rewrite fails if it changes one of those values without an accepted semantic decision, or if it becomes harder for the declared reader to use.

Use the full result form when the repair must be inspectable; otherwise a local rewrite plus the kind-preservation check is enough.

#### F.19:4.1 - Result form

| Field | Meaning |
|---|---|
| `TextSpanRef` | Exact span under repair. |
| `ApparatusCandidateSet` | Visible pattern-application, role, carrier, locus, flow, status, process, negative-catalogue, reference, or quality-proof apparatus candidates. |
| `ContentCandidateSet` | Phrase parts that may carry object, kind, claim, relation, slot/use-position, role, flow, evidence value, or user move. |
| `ObjectOfConcern` | Object the span is about. |
| `KindAndClaimMap` | Head kind, claim kind, relation kind, slot or use-position when it changes admissible use, scope, and governing pattern when another pattern governs a specific outside claim. |
| `ConcernedRoleAndFlow` | Role concerned with the object, plus design/run or coupled-flow role when it changes meaning. |
| `ApparatusDisposition` | Removed, moved, retained as content, or blocker when separation is not yet possible. |
| `RemainingContentPrecisionRestoration` | `not needed`, `E.10`, `E.10.ARCH`, `F.18`, governing pattern, or blocker. |
| `PlainRewrite` | Short rewrite after apparatus removal and remaining-content precision restoration. |
| `KindPreservationCheck` | Pre-rewrite and post-rewrite object kind, relation or claim kind, slot or use-position, admissible use, and scope; disposition is `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. |
| `LossCheck` | What became worse, less local, less current, less recoverable, or less usable if the rewrite is accepted. |

#### F.19:4.2 - Pattern-prose specialization

When the repaired prose is an FPF pattern, apply the same algorithm with one role test:

> Does this sentence address the pattern's intended user, or does it record development, review, projection, landing, quality, or source-management evidence about the pattern version?

If it records evidence about the pattern version, keep that evidence outside the pattern unless the pattern's own primary `EntityOfConcern` is that evaluation or projection object. The evidence can cause edits to the pattern; it is not automatically pattern content.

Pattern prose keeps:

- the pattern's own primary `EntityOfConcern`;
- the first useful move;
- the practical delta and cost of missing it;
- local boundary prose only for a documented local confusion and exact stop condition;
- short declarative references to related patterns after the pattern's own content is visible.

Pattern prose moves out:

- package-placement rationale;
- review/executor correspondence;
- quality-status proof;
- ToC/J.4, retrieval, card, monolith-parity, or landing evidence;
- repeated boundary doctrine already carried by another pattern.

