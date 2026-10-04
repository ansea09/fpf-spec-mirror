---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__002_use-this-when.md"
commit_sha: "9d1e9fa535b9014addd2d1630030762f0d9d2671"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:0 — Use this when"
line_start: 84721
line_end: 84786
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
  - "a body-only term cannot support that search"
  - "and OPTIONAL are to be interpreted as described in RFC 2119"
  - "and query cue for additional familiar expressions. If the intended search sees only headings"
  - "improves auditability"
  - "inside the predicate block"
  - "or other admissibility conditions of the modeled world"
  - "structural invariants"
  - "to state definitions"
  - "typing rules"
  - "“is required to”) in normative clauses"
---

### E.8:0 - Use this when

Use `E.8` when you are writing, revising, or reviewing one FPF pattern and need to know what shape, voice, reader-recognition function, and assurance material the pattern must carry before it can be treated as mature FPF text.

For the whole account of an FPF, DPF, or LPF and its substantive profiles, reuse the twelve content functions through `E.8:4.1.4` and `E.11.PFP:4.7`. Those functions guide the explanation at each selected scale; the individual-pattern heading grammar remains the form for individual pattern bodies.

Use it especially when a draft is technically correct but hard to use: the cold reader cannot tell when to apply it, what action to take, what mistake that action prevents, which related pattern defines or constrains a specific outside claim, or which assurance material is informative rather than the first user-facing guidance.

**Not this pattern when.** Use `E.9` when the main work is deciding why FPF should change and how that decision is distributed across patterns. Use `E.19` when the main work is an admission or refresh review. Use the local domain pattern when the question is what FPF says inside that domain rather than how a pattern should be authored.

#### E.8:0.1 - What goes wrong if missed

A pattern can satisfy a checklist and still be practically unreadable. It may open with package architecture instead of a recognisable working moment, bury its payoff, hide the pattern that defines or constrains a specific outside claim, or let assurance prose silently replace the reader-facing claim. The result is a formally neat text that authors can defend but practitioners cannot reliably use.

#### E.8:0.2 - What this buys

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

#### E.8:0.3 - Pattern Kind In Plain Terms

An FPF pattern supplies action- or judgement-guiding content for a recurring working situation. In ordinary phrases such as “use this pattern” and “apply this pattern”, the acting participant is the person or other capable system; the pattern is the guidance that participant uses.

Call the pattern content a `U.MethodDescription` only when it describes one independently admitted `U.Method` under A.3.2 and that distinction matters to the current claim. Keep the Method and its description episteme separate. A `Solution` can guide future action or help choose a Method without establishing that any dated Work has happened. The intended reader, an actual performer System, local system-role classification, assignment, capability, responsibility, authority, result, and Transformation remain separate whenever those claims are current.

When a pattern or worked case does assert dated `U.Work`, first recover every actual performer's A.13 core: the admitted `U.System`, local agential kind and criterion, classification, same obtaining assignment, scope, working situation, window, and adequate core evidence; add a characteristic profile only when its own receiving use consumes it. Then independently admit the Work under A.15.1 from its performance history, enacted Method, time, and containing System. Add F.6 afterward only when the pattern also needs precise assignment-bound attribution through that same assignment. A short practitioner sentence may omit identifiers unused by its receiving claim only when every relation the claim consumes remains recoverable.

`Pattern application` is ordinary shorthand for user-side use: a user or another capable system recognizes the situation and uses the pattern's `Solution` to choose the next action or judgement. The pattern body is description-side guidance. Assert a performer, assignment, dated `U.Work`, result, or `U.Transformation` only when independently established and material to the receiving claim; a `Conformance Checklist` checks the authored description and evidenced use but does not replace the `Solution`.

The pattern's main job is constructive action or judgement guidance. In the opening `Problem frame` and `Solution`, state the primary `EntityOfConcern`, first admissible move, first useful result or practical delta, and only the boundaries that change that move. Error prevention, auditability, conformance evidence, citations, and architecture rationale remain secondary. Repeat another source's distinction only when it adds a local action, case, evidence value, or recognition needed on first reading. State what this pattern governs; do not surround it with an unbounded catalogue of other things.

Name an FPF object by its known kind and state the relation the sentence actually uses. For a neighbouring pattern, state its concrete contribution and cite the PatternID; identify an exact episteme, `ClaimGraph`, edition, or relation assertion only when that identity changes the receiving use. Put detailed discovery in its dedicated carriers, including README, ToC, `E.11`, and keep compact pattern relations late in `Relations`. Do not repeat the same boundary or reference family in small prose variants.

Use `E.8` to keep the pattern's positive subject and action guidance first. Apply `F.19` once to each changed natural span as the common precise-plain-language pass. Its connected reading owns language-general semantic completeness and contribution, coordination and foregrounding repair, kind and loss preservation, and local revalidation after wording changes. These facets form one connected `F.19` reading, not separate `E.8` checks.

For FPF authoring, `E.8` adds the pattern-specific question: can the intended reader still recognize this pattern's `EntityOfConcern`, working situation, first action or judgement, first useful result, and action-changing boundary before optional modeling and assurance? A cold reader must recover that path from the pattern body; `F.19` governs the sentence-level recovery. Do not copy its method, regression table, or result boundary into a local authoring profile.

If the `F.19` reading leaves an FPF value unresolved, take the exact `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or subject-pattern route and state that source's concrete contribution. Ordinary PatternID citation and “use this pattern” wording remain ordinary; use an identity-bearing MethodDescription or dated Work claim only when the selected route requires it. Keep development and release evidence outside practitioner guidance unless rewritten as the user's action or boundary.
When an action-adjacent pattern classifies wording or another semio-facing object, connect that classification to the reader's current action. State the admissible use now and any independently grounded boundary that changes that use. Route any other genuinely live claim to the FPF pattern that defines or constrains it.

`Semio-Echoing` is admissible only for one grounded wording-use overread that changes the reader's action or boundary. Keep the pattern's own `EntityOfConcern`, positive move, and result primary. Use a thin cue to the exact subject pattern only when its contribution is needed; do not add a generic counterreading catalogue.

