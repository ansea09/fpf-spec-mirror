---
chunk_kind: "child"
pattern_id: "F.1"
pattern_title: "Question-Relative Source Selection"
section_id: "F.1:4"
section_title: "Solution — select by answer-changing role"
source_path: "FPF-Spec.md"
output_path: "by_section/F.1/F.1__005_solution-select-by-answer-changing-role.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "F.1 — Question-Relative Source Selection"
  - "F.1:4 — Solution — select by answer-changing role"
line_start: 93180
line_end: 93275
dependencies:
  - "A.10"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "F.0.1"
  - "F.0.2"
  - "F.17"
  - "F.9"
keywords:
  - "SourceCutNote"
  - "answer-changing source role"
  - "exact source and edition"
  - "finite source cut"
  - "intended use"
  - "receiving question"
  - "reopen condition"
---

### F.1:4 - Solution — select by answer-changing role

#### F.1:4.1 - Minimal vocabulary

- **Exact source and edition.** The identified publication, canon, corpus, practice source, or other claim-bearing basis being considered.
- **Receiving question and use.** The independently identified question that the source-selection claims concern, plus the decision, pattern contribution, comparison, or action the answer will serve. The question is the `SourceCutNote`'s EntityOfConcern; the use is claim content.
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

#### F.1:4.2.1 - When the cut will support a SoTA claim

A source cut used to claim SoTA has a stricter role test because source relevance and source currentness do not establish the best-known answer. `E.8:11` owns the FPF definition of SoTA and the meanings of its comparison roles; F.1 neither redefines SoTA nor selects the winning line. For each retained source, record one of those roles in plain wording: **best-known-line candidate**, **serious current rival**, **failure or counterexample evidence**, **official or popular comparator**, **lineage only**, or **identity/currentness only**.

The first three roles can supply answer-changing evidence. An official or popular comparator may stay only when its named defect is necessary to the comparison. Roles are assigned by contribution, not institution: an official standard or widely used practice may instead be a best-known-line candidate when its substantive answer wins against the serious alternatives. Officiality, prevalence, maintenance, citation, freshness, or academic praise contributes nothing to that rank. An official catalogue, publisher page, or registry entry may verify the source's identity, edition, publication date, or maintenance state; it establishes neither truth, adequacy, nor SoTA rank.

For a SoTA claim, disable the generic one-source cheap exit unless the one source is itself a current critical synthesis that compares the serious alternatives for the named question and the author can state why no known action-changing rival or counterexample remains hidden. Otherwise retain the necessary rival and failure evidence or return an unresolved source gap. Do not manufacture confidence from a one-source cut.

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

#### F.1:4.4 - Optional search assistance

Use search aids only under a named local policy and only when they help find a suspected omission, rival, counterexample, or near-duplicate. When the result matters, keep the searched corpus, source editions, model or ranking method, scale or threshold, and intended interpretation recoverable.

Inspect the underlying source claims before changing the cut. A descriptor match, citation count, embedding distance, LLM answer, rank, threshold, active-learning choice, or portfolio score never admits, excludes, merges, or replaces a source by itself.

#### F.1:4.5 - Invariants

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

