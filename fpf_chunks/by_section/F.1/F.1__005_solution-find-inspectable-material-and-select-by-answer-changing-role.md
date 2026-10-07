---
chunk_kind: "child"
pattern_id: "F.1"
pattern_title: "Find and Select Sources for a Current Question"
section_id: "F.1:4"
section_title: "Solution — find inspectable material and select by answer-changing role"
source_path: "FPF-Spec.md"
output_path: "by_section/F.1/F.1__005_solution-find-inspectable-material-and-select-by-answer-changing-role.md"
commit_sha: "0c6ade275e9360f0c5ab9715d8f05c0dbaa13cf8"
heading_path:
  - "F.1 — Find and Select Sources for a Current Question"
  - "F.1:4 — Solution — find inspectable material and select by answer-changing role"
line_start: 106242
line_end: 106411
dependencies:
  - "A.10"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "E.11.PUR"
  - "F.0.1"
  - "F.0.2"
  - "F.17"
  - "F.9"
keywords:
  - "SourceCutNote"
  - "answer-changing role"
  - "exact source and edition"
  - "inspectable candidate material"
  - "search and access limits"
  - "source cut"
  - "unfamiliar terminology"
---

### F.1:4 - Solution — find inspectable material and select by answer-changing role

#### F.1:4.1 - Minimal vocabulary

- **Exact source and edition.** The identified publication, canon, corpus, practice source, or other claim-bearing basis being considered.
- **Receiving question and use.** What needs an answer and what that answer will serve. A plain concern can start finding. For source selection, independently identify the exact question that the selection claims concern; it is the `SourceCutNote`'s EntityOfConcern, while the intended use remains claim content.
- **Candidate material.** A passage or other source content that can be inspected for a contribution to the question. A source address without accessible content remains a lead.
- **Query variant.** Words tried to reach material for the same original question; any added interpretation is a hypothesis, not a replacement question.
- **Answer-changing role.** The inspected claim, limit, rival explanation, counterexample, transfer condition, material non-fit, or other stated contribution by which a source can change the answer.
- **Source cut.** The finite set of sources retained for that question and use.
- **`SourceCutNote`.** One C.2.1 episteme identified by its source-selection ClaimGraph, the exact receiving question as EntityOfConcern, and the named effective ReferenceScheme under which that question, source editions, and role claims are read.
- **Domain family.** An informative discovery label, such as workflow, provenance, services, sensing, types, or control. It carries no semantics and cannot admit, merge, or replace a source.
- **Local search policy.** An optional named way to prioritize candidate inspection using search terms, descriptors, citations, embeddings, distances, active learning, or portfolio readings. Its output is attention guidance, not a source-selection verdict.

Source selection, source identity, source-local meaning, source truth, source adequacy, cross-source relation, synthesis, reliance, and assurance are separate questions.

#### F.1:4.2 - Source-selection method

**Step 1 — State the receiving question and use.**
Say what answer is needed, what later use it serves, and which source difference could change that answer.

**Step 2 — Name candidate sources by exact edition.**
Use identified sources whose relevant claims can be inspected. A discipline or domain-family label may help discovery but is not a source.

**Step 3 — Inspect the answer-changing role of each candidate.**
Ask what claim or limit from that edition can change the answer. If that role depends on a disputed expression, pause selection only long enough to use F.0.1's ordinary branch: name the exact source, edition, and passage, and say in plain language what the expression means there. Then return to source selection. Do not run this branch for every candidate. Look deliberately for intended-use contributions, rival explanations, action-changing counterexamples, transfer limits, and material non-fit. One source may serve several roles.

**Step 4 — Take the smallest sufficient cut.**
Retain sources that cover distinct answer-changing roles. Exclude a candidate when no inspected claim from it changes the stated question or use. Do not optimize for a fixed count, diversity score, canonical status, or exhaustive appearance.

**Step 5 — Record exclusions, gaps, limits, and reopen conditions.**
Name deliberate exclusions and why they do not change this answer. State a load-bearing source gap rather than treating an unavailable source as irrelevant. Say which question, use, edition, rival, counterexample, or transfer-boundary change would reopen the cut.

**Step 6 — Return one `SourceCutNote`.**
Identify it under C.2.1 by three values: the ClaimGraph produced by Steps 1–5, the exact receiving question from Step 1 as EntityOfConcern, and the named effective ReferenceScheme that resolves the question, cited editions, and role claims. Keep the intended use in the ClaimGraph. Use a one-screen representation when it helps the receiver hold the result in view. Detailed source analysis stays with the receiving comparison, synthesis, or evidence method.
**Step 7 — Recover only the meanings the work needs.**
After the cut is stable, create an F.17 local-sense cell only for a retained expression that later reuse, a claim, a named receiver, or an actual relation needs. Do not postpone a meaning needed by Step 3 to this stage, and do not manufacture a cell for every retained source.

##### F.1:4.2.1 - When the cut will support a SoTA claim

A source cut used to claim SoTA has a stricter role test because source relevance and source currentness do not establish the best-known answer. `E.8:11` owns the FPF definition of SoTA and the meanings of its comparison roles; F.1 neither redefines SoTA nor selects the winning line. For each retained source, record one of those roles in plain wording: **best-known-line candidate**, **serious current rival**, **failure or counterexample evidence**, **official or popular comparator**, **lineage only**, or **identity/currentness only**.

The first three roles can supply answer-changing evidence. An official or popular comparator may stay only when its named defect is necessary to the comparison. Roles are assigned by contribution, not institution: an official standard or widely used practice may instead be a best-known-line candidate when its substantive answer wins against the serious alternatives. Officiality, prevalence, maintenance, citation, freshness, or academic praise contributes nothing to that rank. An official catalogue, publisher page, or registry entry may verify the source's identity, edition, publication date, or maintenance state; it establishes neither truth, adequacy, nor SoTA rank.

For a SoTA claim, disable the generic one-source cheap exit unless the one source is itself a current critical synthesis that compares the serious alternatives for the named question and the author can state why no known action-changing rival or counterexample remains hidden. Otherwise retain the necessary rival and failure evidence or return an unresolved source gap. Do not manufacture confidence from a one-source cut.

An original FPF or DPF answer is compared under E.8:11 on the same basis as a source-derived answer. Select the sources needed to expose serious alternatives, their limits and relevant failure evidence; do not require a prior external publication containing the authored answer. The original answer still needs that comparison, so its authorship does not restore the generic one-source exit.

The `SourceCutNote` records the `E.8:11` roles and the missing comparison, but it does not itself select the best-known line. Use `F.0.2` when an actual cross-source synthesis claim is required. Use `G.2` only when a broader refreshable evidence pack is justified; a bounded comparison does not require that apparatus by default.


#### F.1:4.3 - The `SourceCutNote`

The note's exact EntityOfConcern is the independently identified receiving question from Step 1. It is not the note, its file or one-screen form, the retained-source list, or a question-and-use bundle. The intended use remains part of what the note claims. Name the effective ReferenceScheme explicitly and make sure it resolves the question, every exact source-edition reference, and every answer-changing role statement. If either the question or scheme is unresolved, return that gap and keep the text as an ordinary working note.

Its ClaimGraph states:

- the receiving question and intended use;
- every retained source and exact edition;
- the answer-changing role of each retained source;
- for a SoTA-supporting cut, each retained source's plain role and any unresolved rival, counterexample, or synthesis gap;
- deliberate exclusions and their reasons;
- known limits and load-bearing source gaps;
- the distinction between designed and performed material when it affects the answer; and
- the conditions that reopen the cut.

A one-screen source note is a compact representation of the same episteme when it carries the same claims. If its ClaimGraph differs, it is another C.2.1 episteme rather than a second F.1 result kind. A short form does not establish source truth, adequacy, or local meaning.

<a id="f144---optional-search-assistance"></a>

#### F.1:4.4 - Find candidate material when sources or terminology are uncertain

Use this branch when the current question lacks material that can be inspected: its source, wording, location or available finding route is uncertain. Begin with the means you have. A paper catalogue, available files, a source's references, a colleague or a search service can supply a route. An already identified sufficient source can be used directly.

##### F.1:4.4.1 - Keep the question and bound the available material

Keep the original question, what an answer would change, and any unresolved condition. A plain concern can start finding; it need not yet have the independent identity required for a SourceCutNote. Separate that concern from the words tried in a search. If you add an interpretation, mark it as a hypothesis to test against the material.

Source reading can change what you understand the question to be. Keep the original receiving concern and explain what the new material changes: a different needed result, a mistaken premise or an additional condition. Use B.5.PI:4.4 when that inquiry needs reconstruction, then return with the revised question. A query variant tries another way to find material for a question; a revised question can require different material.

Establish what can actually be inspected: which publications, collections or archive portions, which editions, and what access they provide. Full bodies, titles, excerpts and an index have different reach. Record a consequential missing collection or unavailable original. This boundary makes a later no-hit result interpretable and prevents an available subset from silently standing for the whole repertoire.

##### F.1:4.4.2 - Choose an attainable first route

Choose a route that could reach the needed material at acceptable effort. Use a known address or a cheap direct text lookup when it can answer the question. When terminology is uncertain, use a likely contents area, an analogous case or an inspected passage to obtain words the source itself uses.

| Available starting point | First route and likely blind spot |
| --- | --- |
| A cited source or passage address | Obtain that edition and open the passage. A reference alone may expose no body, and a later edition may have changed the relied condition. |
| Words likely to occur in accessible text | Search the bodies for the object, action, result or distinguishing condition. A single phrase may miss another language, earlier name or differently worded explanation. |
| Unfamiliar terminology but a recognizable concern | Browse a relevant contents area or example, then use the source's wording for further lookup. A published classification can place the contribution in another area. |
| A relevant inspected source | Follow a reference or neighbouring passage that could supply the missing contribution, rival or limit. Its references can favour its own lineage. |
| A search, assistant or summarized view | Use returned candidates to choose what to inspect. Its declared fields or representation can omit body conditions; a score cannot establish their absence. |

These are alternative starting points. Choose an additional route only when a consequential gap remains and that route could recover material the first route could not reach. For example, a body search can bypass a title-only index; an older term can bypass a current-name catalogue; a referenced original can expose a condition missing from an excerpt. Repeating the same limited representation with another tool does not repair that limit.

Keep a material search aid's policy recoverable in ordinary wording: searched corpus and editions, route, relevant filter or model, and how its output is interpreted. Retain a score's scale or threshold when it changes what is inspected. No special record is required for an ordinary lookup.

##### F.1:4.4.3 - Try question-preserving variants and repair a blind spot

Form variants from the concern: the object being worked on, needed action or result, failure, and condition that changes the answer. Start with the parts likely to occur in the available text. Trying every detail as one phrase can miss a passage that explains the needed relation in different words.

Keep the original question alongside each consequential variant. Terms suggested by a colleague, an assistant or a promising source remain search hypotheses until their local use is inspected. If a variant drops a constraint to broaden discovery, restore that constraint while reading candidates. Broadening the query permits finding more material; it does not broaden what would answer the question.

After an unhelpful result, ask what that route could have missed. Change the particular term, scope or access path responsible for the suspected omission. When no available route can inspect a load-bearing original, return that access gap rather than inventing its content. Add another route for a reason, not to satisfy a fixed number of searches.

##### F.1:4.4.4 - Inspect the source around the candidate

Open the candidate with its enclosing heading and the definitions, conditions, examples or dependencies needed to understand the passage. Say how its content could contribute to the current question. A useful candidate can supply a direct answer, an operation, a rival, a counterexample or a limit. Mere word similarity supplies none of those roles.

Compare the material obtained with the contributions the next use needs. New wording, another search route or a different document can still repeat the same contribution. When several aspects matter, identify the one still unsupported and why its absence could change the receiving answer; seek material for that gap. Several documents elaborating one aspect do not supply another. Keep an unresolved aspect visible when its source cannot be inspected. A brief statement of the remaining need suffices.

Check what was actually obtained. Distinguish an inspected body passage from a title or reference to an inaccessible original. An excerpt can be returned as inspected material with its missing context stated; it cannot supply an uninspected original's omitted conditions. Recover the source and edition as far as access permits, and retain an unresolved edition identity when it affects use. If a source-role judgement turns on a disputed term, use the ordinary F.0.1 source-local reading and return here or to :4.2.

For a candidate FPF Method, retrieve the relevant complete pattern and the conditions needed for its use through the available publication. Material finding supplies that text; E.11.PUR judges a proposed use and E.11.PUA guides application of a selected pattern. A promising fragment can be enough to continue finding while remaining insufficient to perform the Method.

##### F.1:4.4.5 - Return useful material, its limits and the next move

Return the inspected candidates with source/edition and passage locations, the reason each matters, and any missing condition or access limit. A passage with a short explanation can be enough. Keep inaccessible leads and uninspected candidates visibly separate from material already inspected. State the searched scope and consequential route limits when they affect what the receiver may conclude.

Choose the continuation from the receiving need:

- Use a sufficient identified source directly for the subject question. Finding creates no source-cut obligation.
- Use :4.2 when several inspected sources could change the answer and a justified source cut is needed. Source selection then returns its own SourceCutNote.
- Use the relevant subject method for truth, applicability, synthesis, reliance or assurance. When the inspected contributions still leave an obtaining way unexplained, C.39 develops that connection or returns its precise gap. For proposed FPF uses, continue with E.11.PUR only when such a judgement is current.
- Return the exact missing material or access condition when the next use cannot yet be supplied.

Stop finding when the next use has the material it needs, or no affordable available route could presently change that result. Judge another search by the missing contribution it could supply, not by the availability of more terms or documents. A limited search with no useful hit returns “no useful material found by these routes in this accessible scope”, with the remaining gap. It establishes no claim of universal absence or completeness.

Reopen the affected finding when the question, needed result, source edition or access changes. Reuse a passage whose contribution and conditions still hold. A renamed file or new edition number alone does not require repeating the whole search; a changed relied passage or newly accessible original can. If a search representation changes, check whether it now reaches or hides material needed by the question before changing the received result.

#### F.1:4.5 - Invariants


For finding, keep the original concern distinct from search variants, identify what was actually inspected, and return consequential access limits. A no-hit result is relative to the searched scope and routes. The following invariants govern the source cut when source selection is current:

1. Every retained source has an inspected answer-changing role for the stated question and use.
2. The cut is finite, inspectable, and revisable; no universal count establishes sufficiency.
3. Exact sources and editions remain recoverable.
4. Source-local meanings remain local; F.1 does not merge or relate them.
5. The result contains no F.9 relation, synthesis conclusion, truth verdict, reliance decision, or assurance claim.
6. Domain families and search readings guide discovery only.
7. Designed descriptions and performed occurrences stay distinct when that source difference matters.
8. A changed relied premise reopens the affected cut claims; an unrelated edition-number change does not.
9. One already identified sufficient source is the ordinary cheap exit; for a SoTA claim, the stricter critical-synthesis condition in `F.1:4.2.1` applies.
10. A protocol-defined evidence review continues to follow its domain method.

#### F.1:4.6 - Self-checks


For finding:

- **Question-preservation test.** Could a changed or omitted query term change what would answer the original question? Restore that condition when inspecting candidates.
- **Reach test.** What material could the available route actually inspect, and which consequential blind spot remains? Use a complementary route only if it could repair that gap.
- **Candidate-return test.** Can the receiver obtain the inspected passage, see why it matters and distinguish missing context or an unavailable original?
- **Stop test.** Does the next use already have sufficient material, or is its exact missing basis returned? Do not turn a scoped no-hit result into a claim of absence.

For source selection:

- **Answer-change test.** What can each retained source change in the answer or action? If nothing, exclude it or state the missing role.
- **Rival-and-limit test.** Is a known rival explanation, counterexample, or transfer limit still hidden? Add the source that makes it inspectable or return the source gap.
- **One-source test.** Does one already identified source close the ordinary question? If yes, stop without additional F.1 steps. If the cut will support a SoTA claim, take this exit only when that source is a current critical synthesis of the serious alternatives and no known action-changing rival or counterexample remains hidden.
- **SoTA-role test.** Has each retained source been classified under one of the comparison roles defined in `E.8:11`? If not, classify it there before using the cut for a SoTA claim; do not recreate the role meanings in F.1.
- **Rank test.** Did official status, popularity, maintenance state, date, or a catalogue check raise a source's SoTA role? Remove that inference; keep the check only as source identity/currentness evidence.
- **Gap test.** If the best-known line cannot be established, does the note return the missing rival, counterexample, or synthesis need as a source gap rather than naming the newest available source?
- **Locality test.** Have two sources been treated as saying the same thing merely because they use the same word? If so, use the ordinary F.0.1 branch on the exact passages before deciding their roles, then return to selection.
- **Search-policy test.** Did a score decide membership before source claims were inspected? Undo that decision.
- **Memory test.** Can the receiver hold the cut and each source's role in view? Remove non-changing material or split genuinely different questions.
- **Reopen test.** Can the note say what future change would require selection again?

