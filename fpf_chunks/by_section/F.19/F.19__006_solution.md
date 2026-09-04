---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__006_solution.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:4 — Solution"
line_start: 100488
line_end: 100578
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

Use `OntologyFirstPlainRewrite` as one connected reading and repair over a natural sentence, row, paragraph, list, or small coherent section. Take the intended reader and use from the surrounding work; do not invent an adversarial reader or a persona form.

#### One connected reading and repair

1. **State the governing message.** Say what object, claim, action, event, or distinction the span needs to convey. Mark process traces, status language, reference boilerplate, quality proof, defensive caveats, ornamental detail, and other apparatus that may be displacing it. Apparatus receives no protection merely because it is true or polished.
2. **Recover the predicate and its participants.** Identify the operation and every participant that changes it. This may be an actor, object, source, target, result, or another required operand. Apply the same question to verbal and relational nouns: recover *of what*, *for what*, *between what*, or another required participant. Leave an argument implicit only when one intended value is cheaply and uniquely recoverable from the local span.
3. **Check predicate compatibility.** Recover what the complete claim asserts under its negation, modality, or conditions, and test the subject and participants under the intended literal or metonymic reading. A positive assertion must assign its predicate to a compatible kind. A denial may correct an evidenced type mistake under the plausible-reader test below; without that ground, “evidence does not notice the error” introduces an idle alternative. Keep ordinary metonymy when the relation is established and the capable participant or work remains recoverable: a diagram may show, a framework may help, a reminder may cue, and a constraint may limit.
4. **Resolve referents and kinds.** Pronouns, demonstratives, omitted heads, and repeated labels must select one locally appropriate referent. Preserve the object kind, claim or relation kind, slot or relation position, use and publication boundary, and flow distinction whenever one changes the claim. A shared grammatical position does not make different FPF kinds interchangeable.
5. **Test contribution.** Try deleting every optional contrast, guard, modifier, example, coordinated member, and extra proposition. Remove it when the plausible intended reader can still recognize, understand, decide, and act in the same way. Local truth and grammatical fit do not earn a phrase a place by themselves.
6. **Resolve coordination and lists on two axes.** First ask whether the receiving use needs a series at all. A list or parallel construction earns its form only when the reader must distinguish or retain its members together; otherwise select the governing claim, relation, or representative case. If a series is needed, determine its membership semantics. State the proposition or action it serves; use one kind or predicate only when it fits every member; distinguish a closed set, illustrative examples, alternatives, a sequence, several direct relations, and a failed ontology. A closed set needs its kind, membership rule, and closure. Illustrative examples need the proposition or kind first and a non-exhaustive cue when a plausible reader could mistake them for a classification. Then test discourse load: keep a member only when it adds a distinct consequence; reduce coordination repeated at several grammatical levels and modifier chains that make the reader retain needless branches or postpone the governing message. Length is evidence to inspect, not a verdict. If a list hides an FPF kind, relation, or structure that ordinary reading cannot recover, use the pattern that defines or tests it, or return the unresolved meaning as a blocker.
7. **Foreground, rewrite, and compare.** Put the governing event, claim, requested action, or decision before optional atmosphere, examples, caveats, and catalogues. A prerequisite may come first when it is needed for safe interpretation or action. Write the shortest ordinary technical sentence that preserves every live predicate and participant, established term, polarity, and action-changing detail. Such detail can include quantity or threshold, sequence or timing, criterion or tolerance, exception, and applicability. Compare before and after: any unsupported change of kind, relation, scope, use, currentness, or operational effect is a loss and blocks the rewrite unless another accepted decision authorizes it.

Keep ontology visible only where it carries the sentence. A term-source or type annotation is needed only when it changes how the reader identifies the object, kind, relation, slot, use, publication boundary, admissible use, or applicable rule. A record, card, table, schema, data structure, dashboard, or named form remains apparatus unless it carries one of those values. If ordinary domain wording already preserves them, keep the ordinary sentence. "The aircraft flies" is better than a typed expansion unless the flight function, system kind, or slot relation is under repair.

**Precision before a coarsened rendering.** When head kind, qualifier claim, or comparison basis remains unresolved in FPF-governed prose, use this working order:

Restore the head kind first; a narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` does **not** by itself restore that kind. Then unpack the qualifier claim, then check whether the comparison or escalation basis is homogeneous. Only after that may a later Plain, didactic, or coarsened rendering admissibly relax the sentence, while keeping the more precise upstream interpretation recoverable.

Judge homogeneity against the comparison or condition rule actually used; recover distinct relations separately when that rule combines them. The basis may be a homogeneous claim-kind criterion, threshold, or named defining, constraining, or source-relation condition.

Treat `exact`, `direct`, `current`, `governed`, `subject`, `owner`, `defining`, and similar qualifiers as content only when they distinguish live alternatives. Remove them when no such contrast changes the truth, action, stop, or reliance. A PatternID may remain an ordinary citation; expand it into a claim-bearing episteme, `ClaimGraph`, `U.MethodDescription`, `U.Method`, actor, assignment, `U.Work`, or another formal identity only when the current claim or a named later use depends on that distinction.

Keep ordinary practitioner action and instrumental pattern-use wording ordinary when it does not assert a particular dated Work occurrence. “Use `E.9` to record the decision” and “the framework maintainer compares the editions” need no invented Method, MethodDescription, performer, assignment, or Work identity.

Open the identity-bearing branch only when the sentence deliberately asserts a particular dated `U.Work` occurrence. Then point to its basis: A.13 first, independent A.15.1 Work admission second, and F.6 afterward only for precise assignment-bound attribution. Add a local system-role kind or a separate System-classification judgment only when that neighboring claim matters. Treat a pattern episteme as a `U.MethodDescription` only after `A.3.2` establishes that it has an already admitted Method as its `EntityOfConcern` and explains how that Method is performed. Otherwise cite the applicable pattern content as guidance and use `A.3.1` for the Method itself.

#### Plausible-reader guards and cold-reader recovery

Use two reader tests for different decisions.

- The **plausible intended reader** has the knowledge and task presupposed by the text. Use this reader to decide whether a foil, guard, warning, or contrast deserves mention. Do not substitute an adversarial reader who can imagine any false inference, or the author who already knows the answer.
- The **cold intended reader** lacks the author's private context and unpublished notes. Use this reader after the rewrite: they can recover the object, predicate, participants, relevant kind or ordinary status, relation, action-changing detail, and next useful action.

Retain a negative alternative, denied consequence, warning, or non-use statement only when the exact rejected reading has an independent local ground; a plausible intended reader could take that reading here, including an evidenced type mistake; and the distinction changes truth, understanding, selection, safety, stop, reliance, or action. An earlier or source claim, an observed recurring mistake, a serious competing position, a visible representation feature, or an applicable safety risk can supply the ground. The guard itself cannot.

Even a grounded guard should be the smallest clear correction. When actor allocation is the useful content, state it positively: “On receiving new evidence, the reader decides whether to reopen checking or revision.” When currentness is the useful content, state the direct use: “This guide conveys the seminar of 1 February 2026; check current rules against the current FPF edition.” Keep material negation, documented anti-patterns, fair disputes, and safety stops when their polarity or boundary is itself the claim.

#### Result and local revalidation

The ordinary result is the repaired text, or a blocker naming the unresolved meaning. Do not require a separate result form, card, table, progress row, or recorded answer for each facet of the reading.

After changing words or syntax, reread the changed sentence and only the nearby text needed to determine its referents, predicate, participants, contrast, modality, support, action, and result. The earlier semantic verdict does not transfer to new wording. Unchanged spans and conclusions remain reusable; a local edit does not trigger an automatic whole-document pass.

When a named high-risk or disputed decision needs inspectable evidence, show the before text, repaired text, live values that had to survive, and any unresolved blocker. Use the receiving decision's existing comparison or review result. The optional fields below can structure that result when its receiver needs them; ordinary corrections need no separate form.

If ordinary reading settles the issue, stop. Open `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or an exact subject pattern only for a genuinely unresolved FPF word, kind, relation, role, function, name, source-use, or admissible-use question. A trigger helps find a candidate; it neither bans the wording nor closes the judgement.

#### F.19:4.1 - Result form

Use this optional form when the receiving decision needs the corresponding inspectable detail.

| Field | Meaning |
|---|---|
| `TextSpanRef` | Bounded span under repair. |
| `ApparatusCandidateSet` | Visible pattern-application, role, record, card, table, schema, data-structure wrapping, locus, flow, status, process, unsupported-negative-classification, reference, or quality-proof apparatus candidates. |
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

When the repaired prose is an FPF pattern, apply the same method with one purpose test:

> Does this sentence help the pattern's intended user recognize and perform the pattern, or does it record development, review, projection, landing, quality, or source-management evidence about this version?

If it records evidence about the pattern version, keep that evidence outside the pattern unless the pattern's own primary `EntityOfConcern` is that evaluation or projection object. The evidence can cause edits to the pattern; it is not automatically pattern content.

Pattern prose keeps:

- the pattern's own primary `EntityOfConcern`;
- the first useful move;
- the practical delta and cost of missing it;
- a local boundary that passes F.19:4's full independent-ground, plausible-reader, contribution, and smallest-clear-correction test; and
- short references to related patterns after the pattern's own content is visible.

Pattern prose moves out:

- package-placement rationale;
- correspondence about producing or reviewing the draft rather than using the pattern;
- quality, projection, monolith-parity, landing, and source-management evidence; and
- repeated boundary doctrine already carried by another pattern.

