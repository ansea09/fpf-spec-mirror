---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__006_solution.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:4 — Solution"
line_start: 95149
line_end: 95211
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
2. **Separate content from apparatus by ontology.** For each phrase part, ask what object, head kind, claim or relation, current slot or relation position, use or publication relation, admissible use, participant, and relevant flow position it carries. A trigger-shaped phrase remains content until its actual claim is recovered. Use `E.10.ROLE` once for role-shaped wording: for example, *reviewer role* may name a local system-role kind or participation in a review relation. Use `A.6.F` once for function-shaped wording: for example, *pump function* may name an expected transformation, while *the pump is functioning* states a condition. Infer neither branch from the trigger word. If a phrase part changes a live value, keep it as content; if it only restates process, a label, negative catalogue, reference boilerplate, record, form, or quality proof, classify it as apparatus.
3. **Remove or move apparatus.** Delete the apparatus or move it to the document, record, note, or publication relation where it belongs: `DRR`, review record, quality result, architecture note, README, ToC, `E.11`, or `I.2` entry locus, projection record, release or landing evidence document, or source-side note. Do not replace it with a smoother synonym, role label, container word, status word, record, card, table, schema, data-structure wrapper, or publication-form word.
4. **Restore remaining content precision.** Restore every complement needed to determine the claim: what was selected, changed, compared, transformed, published, evaluated, or relied on. Use `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or the specific pattern that defines, constrains, or tests the remaining word, head, relation, claim, slot, use, name, or admissible-use boundary.
5. **Rewrite and check loss.** Write the shortest plain technical sentence that preserves the repaired object, kind, claim, relation, action, current slot, relation position, use relation, any live system-role, function, ordinary-wording or flow distinction, established term, and admissible use. Also preserve only the action-guiding claim details consumed by the declared use: exact predicate and participants, polarity, quantity or threshold, temporal boundary and order, criterion, tolerance, exception, applicability condition, and other explicit operational detail. The rewrite fails if it changes a live value without an accepted semantic decision or becomes harder for the declared reader to use.

Keep ontology visible only where it carries the sentence. A term-source or type annotation is needed only when it changes how the reader identifies the object, kind, relation, slot, use, publication boundary, admissible use, or applicable rule. A record, card, table, schema, data structure, dashboard, or named form remains apparatus unless it carries one of those values. If ordinary domain wording already preserves them, keep the ordinary sentence. "The aircraft flies" is better than a typed expansion unless the flight function, system kind, or slot relation is under repair.

Treat `exact`, `direct`, `current`, `governed`, `subject`, `owner`, `defining`, and similar qualifiers as content only when they distinguish live alternatives. Remove them when no such contrast changes the truth, action, stop, or reliance. A PatternID may remain an ordinary citation; expand it into a claim-bearing episteme, `ClaimGraph`, `U.MethodDescription`, `U.Method`, actor, assignment, `U.Work`, or another formal identity only when the current claim or a named later use depends on that distinction.

Keep ordinary practitioner action and instrumental pattern-use wording ordinary when it does not assert a particular dated Work occurrence. “Use `E.9` to record the decision” and “the framework maintainer compares the editions” need no invented Method, MethodDescription, performer, assignment, or Work identity.

Open the identity-bearing branch only when the sentence deliberately asserts a particular dated `U.Work` occurrence. Then point to its complete A.15.1/F.6 basis. Add a local system-role kind or a separate System-classification judgment only when that neighboring claim matters. Treat a pattern episteme as a `U.MethodDescription` only after `A.3.2` establishes that it has an already admitted Method as its `EntityOfConcern` and explains how that Method is performed. Otherwise cite the applicable pattern content as guidance and use `A.3.1` for the Method itself.

When one sentence joins unlike claims and no genuine common head covers them, split the claims and use `E.10:0.2c.17` for the resulting list. Do not invent an umbrella object merely to preserve one grammatical subject.

Use the full result form when the repair must be inspectable; otherwise a local rewrite plus the kind-preservation check is enough.

#### F.19:4.1 - Result form

| Field | Meaning |
|---|---|
| `TextSpanRef` | Bounded span under repair. |
| `ApparatusCandidateSet` | Visible pattern-application, role, record, card, table, schema, data-structure wrapping, locus, flow, status, process, negative-catalogue, reference, or quality-proof apparatus candidates. |
| `ContentCandidateSet` | Phrase parts that carry an object, claim, relation, value in `KindAndClaimMap`, action-guiding claim detail, flow position, evidence-use value, or user-facing action. |
| `ObjectOfConcern` | Object the span is about. |
| `KindAndClaimMap` | Head kind, claim kind, relation kind, current slot, relation position, use relation, publication relation when it changes admissible use, scope, and—when another pattern contributes—the pattern id plus what its content defines, constrains, or tests. |
| `ActionGuidingClaimDetails` | Only details consumed by the declared use: exact predicate and participants, polarity, quantity or threshold, temporal boundary and order, criterion, tolerance, exception, applicability condition, or another explicit operational distinction. Empty when none is current. |
| `FlowPosition` | Design, run, or coupled-flow position only when that position changes the claim or use. |
| `ApparatusDisposition` | Removed, moved, retained as content, or blocker when separation is not yet possible. |
| `RemainingContentPrecisionRestoration` | `not needed`, `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, a named pattern plus its concrete contribution, or blocker. |
| `PlainRewrite` | Short rewrite after apparatus removal and remaining-content precision restoration. |
| `KindPreservationCheck` | Pre-rewrite and post-rewrite object kind, relation or claim kind, current slot, relation position, use relation, admissible use, scope, and every `ActionGuidingClaimDetails` value; disposition is `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. |
| `LossCheck` | What became false, less actionable, less local, less current, less recoverable, or less usable—including lost quantity, threshold, polarity, order, timing, criterion, tolerance, exception, or applicability condition—if the rewrite is accepted. |

#### F.19:4.2 - Pattern-prose specialization

When the repaired prose is an FPF pattern, apply the same algorithm with one purpose test:

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

