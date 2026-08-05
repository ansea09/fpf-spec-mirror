---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:4"
section_title: "Solution — One template, enriched by style principles"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__009_solution-one-template-enriched-by-style-principles.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:4 — Solution — One template, enriched by style principles"
line_start: 72045
line_end: 72440
dependencies:
  - "E.10"
  - "E.10.MOVE"
  - "E.11"
  - "E.11.PUR"
  - "E.13"
  - "E.19"
  - "E.21"
  - "E.23"
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
  - "I.2"
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

### E.8:4 - Solution — One template, enriched by style principles

#### E.8:4.1 - Canonical Pattern Template
Within each pattern, the **canonical** section headings **SHALL** appear in the order below.
For each **canonical content section heading (1–12)**, the `<Title>` component (after the heading separator, e.g. ` - `) **MUST** start with the canonical section title (case-insensitive match; canonical capitalisation preferred); an optional clarifier after an em dash is allowed (e.g., `Solution — …`).
The **Footer marker** (section **13**, if present) is a sentinel and is governed by **H-9** rather than the standard `<FullId> - <Title>` shape.

**Extensibility.**
Authors **MAY** add additional sections. Prefer expressing them as subsections under the nearest canonical section (e.g., `4.1`, `4.1.1` under *Solution*). If an additional pattern-level section is necessary, it **MUST NOT** delete or reorder the canonical sections and its title **MUST NOT** shadow a canonical title.

**Mandatory vs optional.**
* Canonical sections **1–13** are mandatory in every pattern.
* Canonical sections carry content. Authors must not use omission placeholders as section substitutes; when a section is intrinsically small, write the smallest content-bearing grounding, misuse, boundary, or reduced-case statement that preserves the section's role.
* **First substantive authoring seed.** The first non-empty authored body of a pattern **SHALL** already instantiate the canonical section frame by value: title line, header block, canonical sections **1–13**, and the footer marker.
* **Seed is not maturity.** The canonical frame is a minimum authoring seed, not a mature pattern claim. Before a pattern is used for public, teaching, enterprise, reliance-bearing, landing-input, release-input, or ordinary practitioner guidance, each canonical section must carry enough recognition, action guidance, worked material, source/SoTA use, boundary, consequence, and relation content for the declared use, and the pattern-quality claim is checked through `E.21`. A file with correct headings, thin bullets, scenario labels, or compressed DRR recap remains a pattern seed until that content is present or the package explicitly marks it as `seedOnly`.
* Recognition-role openings and first-minute working guidance belong **inside** that canonical frame. Any retained pre-template entry material must also stay inside that same canonical frame rather than appearing as one pre-template opening memo. Authors **MUST NOT** seed one pre-template opening memo and postpone canonical sectioning, `Conformance Checklist`, or footer-marker installation to one separate `E.19`, assembly, or review-repair pass.

**Template:**
- **Title line:** Hashes + FullId + ` - ` + Pattern Title; optional `(informative)` note.
- **Header block:** Type, Status; optional Normativity override.
1. **Problem frame**
2. **Problem**
3. **Forces**
4. **Solution**
5. **Archetypal Grounding** (Tell-Show-Show; at least one content-bearing grounding slice, reduced grounding case, or ordinary/non-use boundary)
6. **Bias‑Annotation**
7. **Conformance Checklist**
8. **Common Anti‑Patterns and How to Avoid Them** (at least one local misuse, overread, or exact boundary case; no placeholder)
9. **Consequences**
10. **Rationale**
11. **SoTA-Echoing** (post-2015 practice alignment; terminology drift and deltas; full comparison or reduced SoTA required whenever external or internal practice changes the Solution)
12. **Relations**
13. **Footer marker**

**Footer marker.** End each pattern with a single visible sentinel heading line by itself: `### <PatternId>:End`. This makes truncation detectable even when HTML comments are stripped or shown by editors. The footer marker is intentionally content-free: **do not** place prose under it.

*Note.* Pattern boundaries are still parseable by scanning for the next pattern heading (`## …`), but an explicit `:End` marker helps retrieval pipelines (and LLM prompts) distinguish “this chunk is the whole pattern” from “this chunk was cut mid‑pattern”.

##### E.8:4.1.1 - Heading & ID discipline (human tooling + retrieval)
FPF is often consumed through full‑text search and retrieval (RAG). A reader or an LLM may see a subsection without its parent headings, so headings must be **self‑identifying**.

**H-1 (Heading shape).** Every pattern heading and every subsection heading inside a pattern **SHALL** follow:
`<hashes> <FullId> - <Title> (optional note of non‑normativity)`

*Exception.* The **Footer marker** is a sentinel heading and is governed by **H-9**, not by the standard `<FullId> - <Title>` shape.

**H-2 (Heading separator).** The canonical separator between `<FullId>` and `<Title>` is ` - ` (ASCII, space-hyphen-space).
Previously authored text may use Unicode dash variants such as ` – ` or ` — ` as separators; tooling **SHOULD** treat those variants as migration candidates, and authors **SHOULD** migrate touched headings to ` - `.

**H-3 (FullId).** `FullId` is the full hierarchical address.
For a **pattern heading** it is the pattern ID (e.g., `A.2`, `E.10.D1`).
For **headings inside a pattern**, append dot‑separated ordinal section numbers after the colon (`:`) (e.g., `A.2:4.4`, `E.10.D2:3`).
*Exception:* the Footer marker uses the reserved sentinel token `:End` as defined in **H-9**.
The colon (`:`) is **reserved** for section paths and **MUST NOT** appear in pattern IDs.

**H-4 (Ordinals).** Ordinals in section paths **SHOULD** track the canonical template numbering (**1 = Problem frame**, …, **13 = Footer marker**) to maximise cross‑pattern comparability. During refactors or in previously authored patterns, ordinals **MAY** be local. In that case, the **canonical section title at the start of `<Title>`** is the semantic key; readers and tools **MUST NOT** infer section semantics from the ordinal alone.
*Note:* the Footer marker itself is exempt from ordinal encoding; it uses the reserved token `:End` (see **H-9**).

**H-5 (Where kind and normativity are declared).** Pattern **kind** (for example, Architectural or Definitional) **MUST** be declared in the **Header block**, not encoded into the heading text. Normativity (**normative** or **informative**) **MUST** also be declared in the Header block when it deviates from the default. If a reminder is needed for readers, authors **MAY** add a short parenthetical note at the end of the heading, for example `(informative)` or `(non‑normative)`, but headings **MUST NOT** use square‑bracket tags.

**H-6 (Heading levels).** Heading levels **MUST** preserve a fixed offset between structural layers (Part or Cluster (flat) → Pattern → Pattern sections):
* Part and Cluster headings **MUST** use `#` (level 1) across the file.
* A Pattern heading **MUST** use `##` (level 2).
* Inside a pattern, each nested section **MUST** add exactly one `#` per level (e.g., `## A.2 - …`, `### A.2:2 - …`, `#### A.2:2.1 - …`).

**H-7 (Ellipsis discipline).** Authors **MUST NOT** use **three consecutive full stops/dots** (`...`) as punctuation in headings or narrative prose. Authors **MUST** use the Unicode ellipsis `…` (U+2026) instead. For editorial elisions in quotations, authors **SHOULD** prefer `[…]` to make the omission explicit and distinguish it from retrieval truncation.
*Exception:* literal three‑dot sequences that are part of an external language’s syntax **MAY** appear **only inside code spans or fenced code blocks**.

**H-8 (Normative keywords).** The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119, as clarified by RFC 8174 (only when capitalised). Authors **SHOULD** avoid informal deontic phrasing (“need to”, “is required to”) in normative clauses.

**Deontics vs admissibility.** Use RFC keywords only for **deontic obligations** (requirements on authors, reviewers, implementers/tooling, or published pattern or companion texts) — i.e., things an agent can choose to do or omit. Do **not** use RFC keywords to state **definitions**, **structural invariants**, **typing rules**, or other **admissibility conditions** of the modeled world.

When you need an enforceable constraint that is *mathematical* rather than *deontic*, express it as a non‑deontic predicate using one of: `Definition:`, `Invariant:`, or `Well‑formedness constraint:` (optionally with formal quantifiers). Prefer mathematical terms like `cardinality 1..1 (total)`, `0..1 (partial)`, or `0..n` over deontic adjectives like “mandatory or optional” when the intent is cardinality, not duty.

**Admissibility predicate discipline (recommended shape).**
When expressing admissibility or validity constraints as predicates (`Definition:`, `Invariant:`, or `Well‑formedness constraint:`):
* Authors **MUST NOT** use RFC keywords inside the predicate block.
* Authors **SHOULD** give each predicate a stable identifier and short name (e.g., `RA‑1 (Locality)`, `RE‑3 (Method gate)`), so that Conformance Checklist items can reference it without re‑authoring the rule.
* Authors **SHOULD** write the constraint as a declarative predicate (optionally quantified), e.g., `role ∈ Roles(context)`, rather than as “X MUST …”.
* If the constraint needs to be checked as part of pattern conformance, authors **SHOULD** reference the predicate identifier from the Conformance Checklist, and call out validator behaviour when relevant, rather than duplicating the predicate with RFC keywords.

**H-9 (Footer marker sentinel).** Footer marker **SHALL** be a single heading line whose `FullId` is the pattern ID followed by the reserved sentinel token `:End` (no ordinals, no title, no square‑bracket tags):
`### <PatternId>:End`
It is the only allowed heading *inside* a pattern whose section token is non‑numeric. It **MUST** be the final line of the pattern and **MUST NOT** carry any prose. Tooling and readers **MUST** treat it as a boundary sentinel, not as a semantic section.

**H-10 (Publication-token classification and addressability).** Before emitting an FPF-governed token as a reference, authors **MUST** classify it under exactly one of these seven E.8-local publication-token classes and use the matching form:

- `PatternRef` names one exact current pattern body. It is addressable only when the assembled publication carries one complete H2 body, one matching `:End`, and a truthful current ToC status for the same PatternID; a structural checker may verify and report that conformance but does not supply the status or normative authority.
- `PlannedCatalogEntry` names an explicit future catalogue commitment. It has no current pattern semantics, governing force, prerequisite force, or addressable body; a useful prose mention **MUST** say `planned` or `future`, and a current semantic dependency **MUST** cite existing content that supplies the needed definition, constraint, test, method, or other rule, or state the current gap.
- `SectionRef` names one exact heading path inside one current pattern. Authors and tooling **MUST** read the complete section identifier before examining any substring.
- `LocalDeclaredId` names an exact declaration within one pattern, such as a conformance clause, component, interface row, or predicate. Its scope is local unless an explicit stable anchor or a separate promotion decision establishes wider use.
- `LocalAlias` names an explicitly declared compatibility alias and resolves to its declared canonical local target.
- `PatternFamilySelector` selects a navigable pattern family using canonical spelling `<base>.*`. It requires a current base pattern and at least one current matching member and **MUST NOT** stand in for one exact governing target.
- `NonReferenceToken` classifies a schematic example or ordinary local prose/code that neither occupies a reference-bearing position nor declares a local public ID. It explicitly denotes no reference; key-like typography or backticks alone do not change that class.

Resolution and checking are declaration-first and context-sensitive. Authors and tooling **MUST NOT** split complete SectionRefs, strip a local-ID prefix, promote a local symbol by visual resemblance, or replace these classes with an ignore list. An unresolved token in a reference-bearing authoring form is an error; ordinary code or local wording is not silently upgraded to a reference.

**H-11 (Assembled Part boundaries and title agreement).** In the assembled publication, every compact ToC Part label **MUST** be a bold separator with a blank line on both sides, not a duplicate structural Part heading. Its title and ASCII ` - ` separator **MUST** agree exactly with the corresponding `# Part <letter> - <title>` body heading. A reserved body Part that has no compact ToC table, including current Part H, does not require an empty compact label or table.

*Unification note:* historic A‑ and D‑templates differed only by the presence/absence of **Bias‑Annotation** and **Relations**; the unified template keeps the headings everywhere and requires every heading to carry content-bearing grounding, boundary, consequence, rationale, source-use, relation, or reduced-case material rather than an omission placeholder.
The Alexandrian pattern canon historically calls *Problem frame* “Context”. FPF avoids that label because **Context** is already overloaded in FPF (e.g., `U.BoundedContext` and its Plain‑register label).

#### E.8:4.1.2 - Preserve Pattern Use Value Across Material Revisions

A revision is material when the actual change can alter what a working reader recognizes, does, obtains, or must stop doing, regardless of whether the change is labelled as cleanup, clarification, terminology repair, or ontology alignment. Treat the revision as material when it can change at least one of these values:

- the primary `EntityOfConcern`, governed kind, direct relation, claim kind, or scope;
- the recurring situation or practical question that lets a reader recognize the use;
- a Solution action, action condition, result kind, first useful result, stop, return, risk disclosure, or stronger-neighbor handoff;
- the definition, constraint, test, method, cited-pattern contribution, split, merge, relocation, or source/SoTA stance that changes what the reader may do;
- the asserted commonality, member set, membership rule, order, or governing premise of a list; or
- ordinary first-use affordability.

A formatting correction, spelling repair, citation repair, exact mechanical rendering, or wording change is `not triggered` only when the smallest comparison of the actual predecessor and proposed text shows that all these values are preserved. A clean comparison needs no additional positive ledger, evidence table, or pattern section. Physical line count, file size, section count, inventory rows, and the author's label for the change do not establish materiality.

**Use one bounded material-revision loop over the actual prose.** Before treating a materially revised pattern as authored:

1. Recover the useful predecessor use at idea level: the recognizable situation and intended reader, first admissible action or judgement, first useful result, action-changing boundary or stop, and any domain claim, example, or relation needed to perform that move. Classify a changing or disappearing predecessor use only as retained, a valid outcome whose defective mechanism is repaired, an explicitly authorized retirement with a corrected action or boundary, or unsupported residue.
2. Draft the candidate's positive practitioner path in domain-recognizable language before guards: governed subject, recurring problem, action the reader can take, first useful result, and next action-changing condition or stop.
3. Compare the actual predecessor and proposed text at comparable application effort. Preserve every useful predecessor move or deliberately replace it with an at-least-equally-usable action, result, or boundary; admit a candidate-only use only from an exact accepted decision, source/SoTA stance, finding, or working need.
4. Remove exactness intensifiers, negative catalogues, role/process wrappers, formal identities, and assurance apparatus that do not change the truth, action, boundary, or reliance claim. Keep ordinary “use this pattern” or “apply this pattern” wording; open the fuller pattern-application ontology only under `E.8:0.3` when its identities matter.
5. Check that recognition, first action, and first useful result still precede optional modeling, evidence, conformance, and assurance work. Use `F.19` or `E.10` only for a residual phrase or word/head/use problem, not as a wrapper around the whole authoring path.
6. For every changed public or consumed interface—entry wording, input or result, field or position meaning, action order, stop, return, or reconsideration condition—repair each determinate stale ToC or README cue, example, relation, and true direct consumer in the same authoring increment. Find consumers by the meaning they teach or use; a shared word, identifier, or nearby reference is not enough.

Prior-edition and candidate-only uses remain different bases, and both may be present in one revision. Compare the exact predecessor and candidate editions. A prior-edition use keeps its predecessor basis and one of the four classifications above; a candidate-only use keeps its exact accepted basis and receives no old-use class or fabricated history. Treat a selected use as required when its loss changes action or boundary, and as optional when it demonstrates breadth only. Backward compatibility alone is not improvement, and a candidate-only promise is not improvement until the text supports its executable use. Use desk replay by default and escalate to a cold reader, AI-agent, or observed-work check only when ambiguity or consequence justifies it. If later independent review needs a recoverable note, use the smallest existing authoring source; do not create a card, score, universal schema, or one written row per idea.

Test first-use affordability by checking whether the positive Solution supports this short rendering:

```text
recognizable situation -> proposed action or judgement -> first useful result -> next action-changing condition or stop
```

This rendering explains the pattern; it does not claim that actual work is linear. Use an optional local mantra only when it improves recall and an ordinary walkthrough only when several rows materially improve explanation; choose the smallest form that keeps the action, result, and boundary recoverable. Explanatory rows may fade as competence or task demand permits, but an independently action-changing condition or boundary may not. Use `DemonstrativeUnfoldingSlice@Context` only after independent `A.22.CGUS` admission. Put a subject-side check immediately before the continuation it changes, and keep authoring, review, quality, and release checks outside the subject Solution.

**Resolve triggered enumerations semantically.** A list is triggered when wording or grammar asserts or implies one common kind, predicate, relation position, authority, action, or result; when its member set or membership rule changes; or when a noun sequence hides a claim or action. A locator or visual scan may find candidates but cannot close the judgment. Give every triggered list one of these resolutions:

| Resolution | Required semantic result |
| --- | --- |
| Declared closed value set | Name the governed value kind or field, state that the set is closed, and give one membership rule that covers every member. |
| Illustrative examples of a named kind or proposition | Put the kind or proposition first, state that the list is non-exhaustive, and keep examples subordinate. |
| Heterogeneous neighboring kinds | Reject the false common kind; split the list, retain explicitly heterogeneous neighbors, or route each alien member to its direct governing locus. |
| Implicit unnamed kind, relation, or structure | Recover an existing governed value and direct pattern. Use `F.18` only when the recovered name must be stable, public, Core-facing, reusable across contexts, or durable enough for later citation; block the claim when recovery fails. |
| Action or claim hidden in a noun list | Write the substantive proposition or action first, then retain examples only when they change recognition or use. |

Treat one triggered list as a small attention series. A member is a separate unit when its membership can fail independently or require a different subject predicate. A genuinely small closed set may remain one predicate-level unit only when one explicit membership rule decides every member and none has an independent disposition. Nearby nouns that assert no common membership, and unchanged declared closed sets or named-kind example lists still covered by their exact rule, take the cheap positive-control path. A blanket claim that all lists are coherent is not evidence. `E.10` detects enumeration-as-kind and vague heads, `E.10.ARCH` requires exact predicates for recovered claims, and `F.18` settles durable names; this authoring method does not duplicate their recognition or naming architecture.

#### E.8:4.2 - Stylistic Principles (S-0 ... S-19)

| # | Principle | Guideline |
|---|-----------|-----------|
| S-0 | Narrative Flow Seven-Step Heuristic | Authors are encouraged to structure major paragraphs or subsections using the seven-step mnemonic. |
| S-1 | Density without Jargon | Short declarative sentences; tool names belong in Pedagogy/Tooling. |
| S-2 | Internal Cohesion | Inline references to Pillars and related patterns. |
| S-3 | Embedded Mini-Definitions | Gloss a new term in parentheses on first appearance. |
| S-4 | Contextualisation | Brief historical or disciplinary lineage references. |
| S-5 | Prophylactic Clarification | Pre-empt common misreadings inside the prose. |
| S-6 | Quotable Closers | Finish Solution or Consequences with a memorable aphorism. |
| S-7 | Generative over Prescriptive | Present rules as enabling constraints, not bureaucracy. |
| S-8 | Trans-disciplinary Tie-ins | Illustrate using at least two distinct fields. |
| S-9 | Physical Grounding Reference | Link abstractions to a `Transformer` or physical process. |
| S-10 | Punchy Blocks | <= 5 sentences per paragraph; lists for clarity. |
| S-11 | Narrative Flow | Ensure sections read as a continuous story, not bullet soup. |
| S-12 | Full sentences over tags | Avoid “keyword soup”. Each list item SHOULD contain a subject and a verb; prefer 2-4 sentence micro-paragraphs to bare tag lists. |
| S-13 | SoTA-Echo structure | In the SoTA-Echoing section, present: **claim -> practice -> source -> alignment -> adoption status (adopt/adapt/reject)**; cite Bridges & CL when crossing Contexts/ReferencePlanes. |
| S-14 | Didactic-content sufficiency | New and substantially revised patterns carry enough didactic content to be teachable without nearby project notes. |
| S-15 | Worked slices over scenario labels | Transform-like families show at least one concrete source and resulting-publication slice; scenario names alone are not enough. |
| S-16 | Ordinary vs FPF-governed wording realism | Keep ordinary use light, and make heavier review records explicit only for disputed, high-risk, or higher-impact cases. |
| S-17 | Self-contained monolith prose | A merged pattern must explain itself inside the monolith; planning shorthand and review-context dependencies are not admissible in pattern prose. |
| S-18 | Reader-role discipline | Keep every pattern host or monolith section addressed to the intended FPF user; move package-development, architecture-placement rationale, developer, reviewer, and executor correspondence, and quality or projection evidence to separate companion, evaluation, review, projection, or release carriers unless the sentence has been rewritten as the user's admissible move or boundary. |
| S-19 | Precision before relaxation | In FPF-governed prose, restore the head kind named by a generic phrase before treating any qualifier as trustworthy claim guidance; then restore the claim kind or admissible-use boundary hidden in the qualifier before allowing any later plain, didactic, or coarsened restatement. |

Authors use the principles as a *scaffold*, not a straitjacket: the goal
is coherent, engaging insight. Engagement remains subordinate to semantic discipline: hooks, quotable lines, Plain restatements, and didactic images may improve recognition, but any ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim kind or admissible-use boundary they carry must be recoverable through the governed Tech reading or named neighboring pattern. Ordinary Plain prose without that claim kind or admissible-use boundary stays ordinary prose.

**S-0 (Narrative Flow Seven-Step Heuristic) — explanation**
Narrative flow is recommended to follow these steps: **Hook -> Frame -> Weave -> Ground -> Bridge -> Flow -> Close**.

Brief explanations:
| Step       | Purpose in a paragraph/section                             |
| ---------- | ---------------------------------------------------------- |
| **Hook**   | Open attention with a vivid but bounded image or paradox that maps back to the primary `EntityOfConcern` and claim. |
| **Frame**  | State the specific question or problem space.              |
| **Weave**  | Connect to earlier patterns or Pillars.                    |
| **Ground** | Tie to a concrete system, episteme, or physical process.     |
| **Bridge** | Show the implication for the upcoming claim or rule.       |
| **Flow**   | Deliver the formal content or argument.                    |
| **Close**  | End with a quotable line or payoff that reinforces memory. |

Narrative Flow Heuristic also operationalises S-1 (Density w/o Jargon), S-2 (Internal Cohesion), S-4 (Contextualisation), and S-6 (Quotable Closers).

#### E.8:4.2.1 - Recognition text and assurance text
Every canonical pattern SHALL stabilise one primary `EntityOfConcern`, relation record, or claim record early enough that a cold reader can tell what kind of thing the pattern is actually governing. If ordinary forms vary (`note`, `sheet`, `guided UI`, `rendering`, `review aid`), the text must make explicit which of those are merely presentation forms of one primary selected EntityOfConcern, relation, or claim and which would instead name a different act, process, work-result record, or governing companion. Recognition and assurance texts may refine that selected item differently, but they must not silently swap the central kind.

If a pattern uses a broad umbrella or head together with a narrower operative branch, the text must also make the stack explicit early enough for first reading: what the broad head names, what the current narrowed branch is, what primary `EntityOfConcern`, relation record, or claim record is actually in play, what exact action assertion and predicate are current, and what wider work or process remains outside the pattern. A qualifier alone does not restore that stack.

Under `F.18` local-first naming, the canonical pair here is **recognition text** and **assurance text**.
The earlier provisional `recognition shell` and `assurance shell` wording is retired.
These names refer to two reading-order roles carried by existing sections or projections inside one pattern; they do **not** mint new `authoritySourceRef` targets, generic neighboring-pattern relations, publication-form/face kinds, `publication-face kind`s, or a second face family.
A third didactic-content role remains optional and is justified only when the family is especially easy to misuse, easy to over-read, or hard to teach without extra scaffolding.

The **recognition text** is the first-reading text.
It is the part of the pattern that lets a cold working reader recognise the situation quickly enough to decide whether to keep reading.
It should start from a subject-domain or practice moment before internal taxonomy whenever the pattern is meant to help real work rather than only internal canon maintenance.
In practice it usually appears in an early `Use this when` line or equivalent opening, plus the upper parts of `Problem frame`, `Problem`, `Solution`, `Consequences`, and nearby worked slices.
Its job is to make visible:
- what ordinary working situation this pattern is for;
- what goes wrong if the pattern is missed;
- what the pattern buys the reader in practice;
- when this is not the right pattern;
- what primary `EntityOfConcern`, relation record, or claim record is actually being kept stable;
- and, when technical terms must appear early, a pairwise plain gloss for each early FPF-governed technical term.

The **assurance text** is the second-reading text.
It carries the heavier FPF-governed material that makes the pattern reviewable and auditable:
- declaration blocks and typed fields when those are part of the pattern's declared conformance or boundary claim;
- representation ontology, EntityOfConcern discipline, or primary-EntityOfConcern discipline;
- any minimal modeling or mathematical lens that keeps the primary `EntityOfConcern`, relation record, or claim record stable;
- guidance or check material, invariants, admissibility, and stop or neighbouring-pattern conditions;
- `SoTA-Echoing` when it carries explanatory work;
- and the review hooks that let a broader or more consequential interpretation or use be checked explicitly.

The assurance text may sharpen, justify, and discipline the recognition text.
It must **not** silently replace, strengthen, or universalize the claim that the recognition text made visible.
If the recognition text says “this pattern helps with a bounded working situation”, the assurance text must not quietly turn that into an unbacked carrier claim, unbacked guarantee, or broader universality claim.

If a pattern claims **universal** or **transdisciplinary** status, that claim must already be visible in the recognition text.
It is not enough for universality to appear only later in a guidance or check sheet, declaration block, or `SoTA-Echoing` rationale.
A broad claim should therefore be demonstrated in the recognition text through at least **three heterogeneous reader or domain situations**.
When a compact matrix helps, `F.16` is the preferred template for showing that breadth.
If `SoTA-Echoing` carries an FPF-governed claim, the practical implication of those rows should be recoverable from the recognition text and case bank rather than remaining a late-only justification layer.

A **third didactic-content role** means enough didactic and operational content that the pattern survives without nearby project documents. Typical indicators include:
- at least one concrete source and resulting-publication slice in Archetypal Grounding when the pattern defines or constrains transforms or publication change;
- at least one boundary-heavy example or anti-example when nearby patterns or other governing companion roles are easy to confuse;
- reviewer guidance that tells what to inspect first and which neighboring FPF pattern defines or constrains the failure mode and which project-side FPF kind and reference named by value carries the claim or effect;
- local mini-definitions or glossary material for recurring terms that would otherwise be recovered only from project context.

Pattern density is therefore not “more metadata” and not “longer tag lists”. It is the presence of enough recognition, assurance, and, when needed, extra didactic material that a reader can understand the pattern, apply it lightly in ordinary cases, and recognise when a heavier review profile is required.

#### E.8:4.2.2 - Package-form and neighboring-pattern reference discipline

FPF pattern prose is not free-form descriptive English. Package-form words and references to nearby patterns must keep stable semantic intent without inventing a generic relation in which a pattern contains the defining content for, governs, receives, or acts on content.

For an ordinary neighboring-pattern reference, state the concrete contribution—for example, defines a kind, constrains a relation, supplies a test or method, or provides a useful lookup—and cite the pattern id. An id, heading, file, or locator field merely helps find content; it is not a semantic owner, authority, actor, participant, or evidence that a claim is true. Identify an exact subject assertion, claim-bearing episteme, `ClaimGraph`, edition, or relation assertion only when the named receiving use depends on that identity, such as interpretation, comparison, migration, conflict, publication, or reuse.

A local `...PatternLocator` field may remain where an existing schema already uses it as a non-semantic convenience, but ordinary prose and entry cues do not require one. It never substitutes for the cited content's concrete contribution or, when the stronger identity branch is active, for the exact claim-bearing content. Changing only a locator without changing what it resolves is a representation change; changing the defining content or exact assertion may reopen the semantic object whose receiving use depends on it.

Keep the following package and relation words distinct:

- **pattern reference** = an ordinary citation to content whose concrete contribution is stated in the current sentence;
- **specialization** = an exact relation in which the child carries the required parent content plus an explicit child delta and use boundary;
- **overlay** = a cross-cutting reading or review projection over stated source content; it adds no authority or obtaining relation by name;
- **profile** = a declarative bounded-use or review projection from stated source content, not a replacement pattern or actor;
- **family** = a recurring class of cases under an explicit membership rule, not a hidden common owner;
- **bundle** = a packaged set of defaults, allowances, or coordinated members whose actual relations remain explicit;
- **cluster** = a navigation or reading-order grouping, with no semantic relation by grouping alone;
- **suite** = a coordinated set whose suite-level membership and coordination semantics are explicitly stated;
- **pack** = an editorial, source, review, or delivery grouping, not semantic authority;
- **kit** = a reusable coordinated publication or boundary-description package with exact kit-level membership and use;
- **record** = a case, report, assertion, representation, or review record under its own identity;
- **umbrella** = a provisional review head spanning possible subfamilies before an exact membership rule and the relevant claims and relations are settled.

These words are not interchangeable and do not stand in for a missing relation. Say `specialization of ... with delta ...`, `profile projecting ... for use ...`, `overlay reading ...`, `bundle containing ... under membership rule ...`, or another exact formulation. A pattern-native role word may be reused when the cited source content defines that role and the current assertion uses it in that sense; otherwise do not improvise near-synonyms for stylistic variety. The preceding receiving-use discriminator decides whether exact claim-bearing content must also be identified.

##### E.8:4.2.2.1 - Precision-restoration placement discipline

When a pattern or companion text is drafted from `E.10` or `E.10.ARCH`, distinguish two authoring objects:

* **`semanticArea`** is the Part-F semantic unit for a wording-use restoration row: one Concept-Set row, one UTS row, or an explicitly bounded row-set. It is declared with `semanticAreaBaseConcept` and `semanticAreaSenseFamily`.
* **`ontologicalNeighborhood`** is the applicability neighborhood around that named `semanticArea`: nearby primary `EntityOfConcern` kinds, relation kinds, claim records, content that defines or constrains the current use, non-use boundaries, and remaining reader use that can carry the recovered meaning after the wording is repaired.
* **`pattern nest`** is the publication and specialization placement of a pattern under a declared family or membership relation.

These are not synonyms. A precision-restoration pattern is placed in the pattern nest whose primary `EntityOfConcern`, relation record, or claim record it repairs. Its `semanticArea` states the Part-F semantic unit it repairs, while its `ontologicalNeighborhood` may name several direct relations and pattern content that defines or constrains the asserted uses. For example, quality-term repair lives in the `C.16` characterization nest, even though its neighbouring relations can include relation construction, action invitation, evidence, assurance, source-use assignment, engineering quality bundles, pattern-quality evaluation, or mathematical-lens use.

Affected patterns should use a thin pointer when the first-stage wording repair belongs elsewhere. The pointer names the selected restoration pattern and the condition that triggers it; it does not copy the trigger registry, the full `E.10.ARCH` recovery algorithm, or a second local architecture for the same repair. The affected pattern then keeps its own subject matter: the characteristic, structure, view, episteme, relation, evidence, assurance, gate, work, decision, or adequacy question it already governs.

If a draft proposes a new precision-restoration pattern, the authoring claim must show the repeated wording failure, `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, the recovered primary `EntityOfConcern` kind or relation/claim record, the intended pattern nest, the neighboring governing relations, and the admissible action left after repair. A new pattern is not justified merely because a word appears often, because a local checklist wants a bucket, or because a campaign needs a tidy grouping.

#### E.8:4.2.3 - Reader-role discipline for pattern prose

A pattern is written for its intended FPF user: the person who will use the pattern to organise thought, inspect a case, publish a note, or review a result under that pattern.
Its FPF-governed sections therefore explain what the pattern lets that user do, what it forbids, what it costs, and how it relates to neighbouring patterns in user terms. When neighbouring patterns or other governing companion roles are named, the prose should answer one user question such as `which neighboring FPF pattern applies`, `which project-side FPF kind and reference named by value carries the claim`, `which nearby pattern is easy to confuse`, or `what must stay coordinated here`; it should not read as one explanatory aside about why the package architecture was split that way.
`E.8` reader and reviewer wording is FPF pattern-authoring wording. Project-side publication readers, explanation readers, comparative review units, and participants in named project-side review relations are governed by the publication or project-side patterns that name those publication units, explanation-use relations, comparative review units, evidence paths, work records, or gate records, such as `E.17`, `E.17.ID.CR`, `E.17.EFP`, `A.10`, `A.15.4`, `A.20`, or `A.21`.

Authors must keep FPF-development or package-architecture material separate from that user-facing body.
In particular, `Problem`, `Solution`, `Consequences`, `Rationale`, worked slices, and ordinary-vs-FPF-governed wording guidance must not do the work of:
- arguing that the material is worth isolating;
- justifying overlay, profile, family, membership, or authority-reference choice as a package decision;
- discussing authority-reference freeze, naming freeze, merge state, blast radius, or safest landing form;
- or narrating future package promotion or defer decisions.

If architecture-placement commentary is still helpful, the default place is a separate companion note or ADR-like architecture note.
A pattern may include a short optional informative subsection such as `Architectural placement note (informative)` only when that placement materially helps users avoid misuse; even then, it must stay clearly separated from the user-facing solution and rationale rather than replacing them.

#### E.8:4.2.4 - Human-facing fit beyond role correctness
Human-facing fit is also subject-domain fit. A recognition text that starts from internal taxonomy, pattern-placement convenience, or package-architecture wording before the problem-domain moment is still under-authored even if its later guidance or check text is correct. When a broader umbrella name and a narrower operative branch are both used, the recognition text should also tell the reader which stack is actually active rather than leaving that reconstruction to a later declaration block or companion note.

A pattern can already be role-clean, boundary-clean, and reader-role-clean, yet still fail the first minute of use for a cold working reader.
That failure usually appears when the text is admissible but does not yet make the working situation, practical payoff, primary `EntityOfConcern`, non-use boundary, or first action-guiding move visible enough.

**P-2 epistemic precision check.** When `E.10` selects epistemic precision restoration for pattern prose, the first admissible action-guiding move must survive as remaining admissible reader use or be replaced by a neighboring FPF pattern whose content now defines or constrains that claim application. This is a direct `E.2` `P-2` and `E.12` requirement, not an optional style preference. Intentional didactic metaphors and vivid Plain recognition lines are admissible when they are ordinary recognition aids or when their claim kind or admissible-use boundary maps back to Tech under `E.10:6.2`. A precision-corrected rewrite that leaves the recognition text inert is still under-authored.

For canonical patterns, the first-reading text should behave as a **recognition text** and the heavier review/check scope should remain in an **assurance text**.

When a pattern claims practice guidance or is meant to be used by engineers, managers, researchers, or other working readers, authors should make the following visible before the heavier harness takes over:
- a recognisable `Use this when` or equivalent first-minute recognition cue;
- a concrete working situation in `Problem frame`, not only taxonomic or pattern-placement language;
- a short statement of what goes wrong if the pattern is missed or misread;
- a short statement of what this pattern buys the reader in practice;
- the first admissible action-guiding move the user should take in that situation;
- a short `Not this pattern when` boundary for ordinary nearby non-use cases;
- one minimally viable worked case or use slice that shows what changes in practice;
- when a typed declaration block, formal lens, or other compact modeling material is FPF-governed, a short user-facing statement of what kind of object the pattern is governing and what minimal lens keeps that object reviewable;
- pairwise plain glosses for any FPF-governed technical terms that must appear before the heavier declaration role arrives;
- when `SoTA-Echoing` carries explanatory work, a short working-reader implication for each row or cluster of rows and a visible link back to the case bank or worked slices that those rows discipline;
- a visible split between the recognition text and the heavier assurance text or companion material;
- and, if the draft implicitly serves several working-reader situations, an explicit primary working reader, primary concern, or primary viewpoint.

**Problem-frame recognition signature (informative).** A canonical pattern should
expose the working situation through its `Problem frame`, not through one
separate navigation block. When an `E.11` pattern-entry discoverability problem
is present, the same `Problem frame` may also carry candidate-pattern and
tempting-wrong-pattern cues; otherwise it should stay with action guidance
rather than becoming a local catalogue row.

The local recognition signature should make recoverable:

- the concrete working situation;
- the primary `EntityOfConcern`, relation named by value, claim record, or stabilized concern;
- what goes wrong if the pattern is missed or misread;
- the first admissible action-guiding move and what that move buys;
- the ordinary not-this-pattern boundary;
- the first admissible action-guiding result; when an `E.11` discoverability
  problem is present, the first admissible entry stop or entry-stabilizing result.

`Use this pattern when`, `This pattern applies when`, or equivalent `Problem
frame` prose may be used as the first sentence or compact cue of this
signature.
It is not one separate required section.

**Entry-cue authoring rule.** When a pattern needs a reader-facing entry cue, begin with one ordinary question about the user's actual current object and claim, before any PatternID, card, template label, or internal taxonomy. In the same compact cue, state what any cited content contributes and cite the pattern id; name the smallest exact result kind usable now, the stop or return condition, and one tempting overread that remains non-admissible. Add an exact subject assertion, claim-bearing episteme, `ClaimGraph`, or edition only when the cue's named receiving use depends on that identity. The cue is reading guidance, not a section schema, method, plan, work occurrence, structure, or relation; it neither constitutes the result nor makes a routed relation obtain.

Resolve the current head before coarsening it. Keep an actual holon under the A.1 kind-admission rule and each direct relation under the predicate and occurrence test supplied by `A.6.REL` or the relevant relation pattern; an independently selected `U.Structure` under A.22; a boundary-description episteme, its effective `ReferenceScheme`, and any separately obtaining empirical-grounding relation under C.2.1, with the grounding holon separately admitted under A.1; a `U.View` under E.17.0; a `U.ClaimScope` under A.2.6; a `U.WorkPlan` under A.15.2; dated `U.Work` under A.15.1; architecture and architecture-description assertions under C.30 and C.30.AD; and a publication occurrence under E.24.PUB. Keep an FPF `Map` and a decision occurrence under the patterns that define or constrain those values. In an ordinary cue, state those concrete contributions and cite the ids. Identify exact predicate-definition content, a claim-bearing episteme, or a `ClaimGraph` only when its identity changes interpretation, comparison, migration, conflict, publication, or reuse. Actual, intended, selected, expected, described, viewed, mapped, grounded, published, and performed objects remain distinct. A cue, diagram, description, file, card, suffix, template label, or public coarsening creates none of them and establishes none of their relations.

Compact candidate-pattern comparison belongs in `E.11`-distributed entry material; expanded entry-disambiguation cases belong in `I.2`.

If the prose points to neighbouring patterns or companion content, state whether that content defines a kind, constrains a relation, supplies a test or method, provides a project-side FPF kind and reference named by value, or supplies an `E.11` entry-recognition reclassification; do not present a citation as a hidden co-authority of the current pattern.

If the pattern claims broad, universal, or transdisciplinary usefulness, that breadth should already be visible in the recognition text.
At minimum the recognition text should show at least three heterogeneous reader or domain situations rather than one narrow case family with a later broad claim attached.
When a compact matrix helps, `F.16` is the preferred template for making that breadth legible.

This is not a request to flatten the pattern into plain language only.
It is a rule about ordering, assurance depth, and text consistency: the recognition text must help a working reader recognise the pattern early, while the assurance text continues to carry the full claim kind or admissible-use boundary.
If the pattern uses technical lexicon, ontological distinctions, or a mathematical lens, those structures must remain recoverable, but the first-reading text should not require the reader to decode that full stack before recognising the working situation.
The assurance text may tighten or discipline the recognition text; it must not silently shift what the recognition text claimed.

**Illustrative migration example (informative).**

Old pre-template top:

```text
Start here when the dominant question is API, protocol, SLA, published boundary, or compliance wording.
First output: Claim Register.
Neighboring pattern relations and entry-recognition reclassifications: A.6.B, A.6.C.
```

Repaired Problem-frame recognition signature:

```text
Use this pattern when boundary-facing language - API, protocol, SLO/SLA, compliance clause, or other published boundary description - mixes guidance or check clauses, admissibility gates, duties, and evidence into one sentence or published boundary description.

If missed, the text becomes boundary-claim soup: runtime behavior, governance, and evidence are treated as one undifferentiated promise.

Do not use this pattern merely because the text mentions an API or boundary description. If the question is still one unstable cue, preserve it through the admissible cue-preservation line first.

First admissible action-guiding result: one `A.6.B`-governed atomic claim set or one Claim Register whose claim/use questions are explicit enough for the pattern content that defines or constrains the claim, or for a named project-side FPF kind and reference, to inspect.
```

#### E.8:4.2.5 - Design-time and run-time referents stay separated in pattern prose

Pattern prose must keep its referent index explicit. In ordinary body sections, the default truth-makers are run-time or governed-domain objects, states, moves, boundaries, consequences, and user-facing practical effects. Normative-standard wording is still admissible when the sentence is explicitly about the standard as a normative publication, for example in marked migration navigation examples, marked informative notes, or conformance/checklist clauses.

Design-time and development-state referents are different objects. The current draft, current body, current pass, author, reviewer, handoff, packet, governing companion, landing choice, or other writing-process objects must not be smuggled in as the hidden truth-condition of pattern prose. A quick test is: what makes this sentence true? If the sentence is true because the current text is arranged a certain way, because the author or reviewer must do something next, or because the current development state says so, then it is design-time residue, not pattern content.

Move that material to the authored-slice carrier, handoff, `DRR`, or companion architecture note. If a sentence is kept in the pattern, rewrite it so that its truth depends on the governed run-time/domain object or on the standard's declared normative claim set rather than on the current writing pass.
If a pattern or example claims **autonomy** for any Role, Method, or Service:
1) Add a subsection **“Autonomy (RoC‑E.16)”** that lists:
   * `AutonomyBudgetDeclRef` (id, version, Scope (G), Γ_time),
   * `Aut-Guard policy-id (PolicyIdRef)`,
   * `OverrideProtocolRef` (SpeechAct names, SoD),
   * pointer to where **Green‑Gate** applies in the Method steps,
   * where **AutonomyLedgerEntry** is recorded on `U.Work`.
2) Include one **Tell‑Show‑Show** vignette that demonstrates **depletion** and **override** handling.
3) Use **LEX‑BUNDLE** terms (Scope (G), Γ_time, Role, Method, and Work). Avoid “validity”, “process”, “actor”, “system”, “mechanism” unless mapped to admitted U-kinds or to the concrete definitions or constraints supplied by cited patterns.

