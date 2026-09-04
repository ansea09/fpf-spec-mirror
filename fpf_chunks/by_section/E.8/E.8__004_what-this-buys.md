---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__004_what-this-buys.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:0.2 — What this buys"
line_start: 73165
line_end: 73193
dependencies:
  - "E.10"
  - "E.10.MOVE"
  - "E.11.PFP"
  - "E.11.PUR"
  - "E.13"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4.DPF"
  - "E.5.1"
  - "E.5.4"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.8.ECSPF"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
  - "). The key words MUST"
  - "MAY"
  - "MUST NOT"
  - "MUST NOT appear inside Definition:/Invariant:/Well-formedness constraint: blocks. When enforceable"
  - "Prevents ambiguity between obligation language and model validity"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SHALL"
  - "SHALL NOT"
  - "SHOULD"
  - "SHOULD NOT"
  - "and OPTIONAL are to be interpreted as described in RFC 2119"
  - "improves auditability"
  - "inside the predicate block"
  - "or other admissibility conditions of the modeled world"
  - "structural invariants"
  - "to state definitions"
  - "typing rules"
  - "“is required to”) in normative clauses"
---

### E.8:0.2 - What this buys

`E.8` gives FPF authors one shared pattern shape and one shared authoring discipline: recognition text first, assurance text second, canonical sections present, terminology kept stable, SoTA used as current practice grounding rather than decoration, and practical consequences visible before a reader has to reconstruct the architecture.

**First useful move.** Put the working situation, first action-guiding move, practical payoff, ordinary boundary, and nearest heavier assurance condition into the recognition text before tightening template details or conformance material.

**Solution and working move.** `Solution` gives the pattern's conditional answer to its `Problem frame`, `Problem`, and `Forces`: what the reader should do or decide, under which conditions, what result to seek, and when to stop or return. A **working move** is ordinary reader-facing wording for one such action or judgement. Reserve `U.Move`, dated `U.Work`, and `U.Transformation` for claims that actually assert those admitted objects. `E.11.PUA` governs use of one selected `Solution` to reach the first useful result. When alternatives are formally qualified under `A.22.CGUS`, call them `continuation candidates`; `E.18.3` applies only when the selected CGUS uses a qualifying transformation-flow substrate.

**Move wording in pattern prose.** In ordinary prose, say **recommend this pattern use**, **coordinate these uses**, or **show their total order** when those are the actual claims. When the durable governed object matters, use its exact published designation under `E.11.PUR`: `PatternUseRecommendation@Context`, `PatternUseCoordination@Context`, or `PatternUseSequence@Context`; the suffix is retrieval wording, and the sequence designation requires an admitted total order for the named use. For any other claim, recover the actual relation under its governing pattern. State what cited content contributes and use `E.10.MOVE` when the current relation remains unclear.

**Cheap stop.** If the draft already gives a cold reader the working situation, first useful move, practical payoff, ordinary boundary, and nearest heavier assurance condition, do not add more authoring apparatus just to look mature. Use conformance material to verify that guidance; do not let it replace the guidance.

**FPF-governed wording extension.** Add heavier assurance, conformance, SoTA, or relation material only when it changes correctness or use: it repairs a false claim, stabilizes the primary `EntityOfConcern`, supplies a missing concrete contribution, grounds a practical payoff, or states an action-changing boundary. Cite the exact pattern that defines or constrains the live value.

When an authoring pass claims quality improvement rather than ordinary drafting, keep these pattern responsibilities distinct: `E.22` frames the improvement-oriented quality-evaluation question, the object-under-improvement evaluation such as `E.21` or `E.9.DA` supplies value meanings and stop meanings, `C.16.Q` repairs overloaded quality and evaluative-characterization wording, `C.25` carries engineering quality-family endpoints when those endpoints are claimed, and `E.23` governs any repeated quality-improvement method. Closing checklist rows or satisfying a review profile is not by itself quality improvement.

When a pattern claims practical payoff through a visible score or other proxy, name the intended value and the relation by which the proxy bears on it. If the proxy is being treated as the value itself, apply `E.13` before admitting the payoff claim.


**Quality or projection evidence placement.** Development, quality-review, projection, assembly, and landing evidence belongs in its own evaluation, review, projection, or release carrier rather than in the pattern body. Keep it in a pattern only when that work is the pattern's declared `EntityOfConcern` and intended-reader use. A Part E pattern may govern FPF authoring, review, evaluation, entry, or publication, but it does not narrate the development of its own current version. Judge placement by the sentence's use, not by a blacklist of words.

**Pattern positions across coupled flows.** During drafting, `E.21` questions may guide a focused author-side check. A product-level conclusion still requires an independent `E.21` evaluation and the applicable `E.19` admission review. Keep their objects and evidence distinct even when an applicable flow relation connects drafting, review, publication, use, and later refresh. A publication may guide or constrain later Work; assert the actual Work and its evidence only through the patterns that admit those claims.

**Maturity rule.** Section completeness is not pattern maturity. A pattern matures when its `Problem frame`, `Solution`, worked cases, boundaries, source/SoTA use, relations, consequences, and conformance checks all point to the same usable action guidance for the declared reader and use. If the reader still needs the DRR, source notes, campaign handoff, or author memory to know what to do, the pattern is not mature for that use.

**Primary EntityOfConcern in plain terms.** The primary `EntityOfConcern` of `E.8` is the authored FPF pattern: its canonical sections, reader-recognition function, wording discipline, examples, rationale, anti-patterns, SoTA-Echoing, and relations.

**Primary working reader.** The first reader is an FPF author or reviewer shaping pattern prose for later practitioners and managers. The downstream practitioner is the reader the pattern must ultimately serve, so the authoring guide must model the same recognition discipline it requires.

