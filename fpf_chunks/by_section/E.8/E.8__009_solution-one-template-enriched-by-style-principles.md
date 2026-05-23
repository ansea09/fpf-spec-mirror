---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:4"
section_title: "Solution — One template, enriched by style principles"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__009_solution-one-template-enriched-by-style-principles.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:4 — Solution — One template, enriched by style principles"
line_start: 50611
line_end: 50928
dependencies:
  - "E.10"
  - "E.19"
  - "E.5.1"
  - "E.5.4"
  - "E.6"
  - "E.7"
  - "E.9"
  - "F.18"
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
* The escape hatch `Not applicable` is permitted **only** where explicitly stated below; when used, it **MUST** include a short justification (1 paragraph).
* **First substantive authoring seed.** The first non-empty authored body of a live pattern **SHALL** already instantiate the canonical section frame by value: title line, header block, canonical sections **1–13**, and the footer marker.
* Recognition-role openings and first-minute working guidance belong **inside** that canonical frame. Any retained legacy pre-template entry material must also stay inside that same canonical frame rather than appearing as one pre-template opening memo. Authors **MUST NOT** seed one pre-template opening memo and postpone canonical sectioning, `Conformance Checklist`, or footer-marker installation to one separate `E.19`, assembly, or review-repair pass.

**Template:**
- **Title line:** Hashes + FullId + ` - ` + Pattern Title; optional `(informative)` note.
- **Header block:** Type, Status; optional Normativity override.
1. **Problem frame**
2. **Problem**
3. **Forces**
4. **Solution**
5. **Archetypal Grounding** (Tell-Show-Show; System and Episteme; `Not applicable` allowed only with justification)
6. **Bias‑Annotation**
7. **Conformance Checklist**
8. **Common Anti‑Patterns and How to Avoid Them** (`Not applicable` allowed only with justification)
9. **Consequences**
10. **Rationale**
11. **SoTA-Echoing** (post-2015 practice alignment; terminology drift and deltas; full comparison or reduced SoTA required whenever external or internal practice changes the Solution)
12. **Relations**
13. **Footer marker**

**Footer marker.** End each pattern with a single visible sentinel heading line on its own: `### <PatternId>:End`. This makes truncation detectable even when HTML comments are stripped or surfaced by editors. The footer marker is intentionally content‑free: **do not** place prose under it.

*Note.* Pattern boundaries are still parseable by scanning for the next pattern heading (`## …`), but an explicit `:End` marker helps retrieval pipelines (and LLM prompts) distinguish “this chunk is the whole pattern” from “this chunk was cut mid‑pattern”.

##### E.8:4.1.1 - Heading & ID discipline (human tooling + retrieval)
FPF is often consumed through full‑text search and retrieval (RAG). A reader or an LLM may see a subsection without its parent headings, so headings must be **self‑identifying**.

**H-1 (Heading shape).** Every pattern heading and every subsection heading inside a pattern **SHALL** follow:
`<hashes> <FullId> - <Title> (optional note of non‑normativity)`

*Exception.* The **Footer marker** is a sentinel heading and is governed by **H-9**, not by the standard `<FullId> - <Title>` shape.

**H-2 (Heading separator).** The canonical separator between `<FullId>` and `<Title>` is ` - ` (ASCII, space-hyphen-space).
Legacy text may use Unicode dash variants such as ` – ` or ` — ` as separators; tooling **SHOULD** treat those variants as migration candidates, and authors **SHOULD** migrate touched headings to ` - `.

**H-3 (FullId).** `FullId` is the full hierarchical address.
For a **pattern heading** it is the pattern ID (e.g., `A.2`, `E.10.D1`).
For **headings inside a pattern**, append dot‑separated ordinal section numbers after the colon (`:`) (e.g., `A.2:4.4`, `E.10.D2:3`).
*Exception:* the Footer marker uses the reserved sentinel token `:End` as defined in **H-9**.
The colon (`:`) is **reserved** for section paths and **MUST NOT** appear in pattern IDs.

**H-4 (Ordinals).** Ordinals in section paths **SHOULD** track the canonical template numbering (**1 = Problem frame**, …, **13 = Footer marker**) to maximise cross‑pattern comparability. During refactors or in legacy patterns, ordinals **MAY** be local. In that case, the **canonical section title at the start of `<Title>`** is the semantic key; readers and tools **MUST NOT** infer section semantics from the ordinal alone.
*Note:* the Footer marker itself is exempt from ordinal encoding; it uses the reserved token `:End` (see **H-9**).

**H-5 (Where kind and normativity live).** Pattern **kind** (e.g., Architectural / Definitional) **MUST** be declared in the **Header block**, not encoded into the heading text. Normativity (**normative** / **informative**) **MUST** also live in the Header block when it deviates from the default. If a reminder is needed for readers, authors **MAY** add a short parenthetical note at the end of the heading (e.g., `(informative)` / `(non‑normative)`), but headings **MUST NOT** use square‑bracket tags.

**H-6 (Heading levels).** Heading levels **MUST** preserve a fixed offset between structural layers (Part or Cluster (flat) → Pattern → Pattern sections):
* Part and Cluster headings **MUST** use `#` (level 1) across the file.
* A Pattern heading **MUST** use `##` (level 2).
* Inside a pattern, each nested section **MUST** add exactly one `#` per level (e.g., `## A.2 - …`, `### A.2:2 - …`, `#### A.2:2.1 - …`).

**H-7 (Ellipsis discipline).** Authors **MUST NOT** use **three consecutive full stops/dots** (`...`) as punctuation in headings or narrative prose. Authors **MUST** use the Unicode ellipsis `…` (U+2026) instead. For editorial elisions in quotations, authors **SHOULD** prefer `[…]` to make the omission explicit and distinguish it from retrieval truncation.
*Exception:* literal three‑dot sequences that are part of an external language’s syntax **MAY** appear **only inside code spans or fenced code blocks**.

**H-8 (Normative keywords).** The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119, as clarified by RFC 8174 (only when capitalised). Authors **SHOULD** avoid informal deontic phrasing (“need to”, “is required to”) in normative clauses.

**Deontics vs admissibility.** Use RFC keywords only for **deontic obligations** (requirements on authors, reviewers, implementers/tooling, or published pattern or support texts) — i.e., things an agent can choose to do or omit. Do **not** use RFC keywords to state **definitions**, **structural invariants**, **typing rules**, or other **admissibility conditions** of the modeled world.

When you need an enforceable constraint that is *mathematical* rather than *deontic*, express it as a non‑deontic predicate using one of: `Definition:`, `Invariant:`, or `Well‑formedness constraint:` (optionally with formal quantifiers). Prefer mathematical terms like `cardinality 1..1 (total)` / `0..1 (partial)` / `0..n` over deontic adjectives like “mandatory or optional” when the intent is cardinality, not duty.

**Admissibility predicate discipline (recommended shape).**
When expressing admissibility/validity constraints as predicates (`Definition:` / `Invariant:` / `Well‑formedness constraint:`):
* Authors **MUST NOT** use RFC keywords inside the predicate block.
* Authors **SHOULD** give each predicate a stable identifier and short name (e.g., `RA‑1 (Locality)`, `RE‑3 (Method gate)`), so that Conformance Checklist items can reference it without re‑authoring the rule.
* Authors **SHOULD** write the constraint as a declarative predicate (optionally quantified), e.g., `role ∈ Roles(context)`, rather than as “X MUST …”.
* If the constraint needs to be checked as part of pattern conformance, authors **SHOULD** reference the predicate identifier from the Conformance Checklist (and/or call out validator behaviour), rather than duplicating the predicate with RFC keywords.

**H-9 (Footer marker sentinel).** Footer marker **SHALL** be a single heading line whose `FullId` is the pattern ID followed by the reserved sentinel token `:End` (no ordinals, no title, no square‑bracket tags):
`### <PatternId>:End`
It is the only allowed heading *inside* a pattern whose section token is non‑numeric. It **MUST** be the final line of the pattern and **MUST NOT** carry any prose. Tooling and readers **MUST** treat it as a boundary sentinel, not as a semantic section.

*Unification note:* historic A‑ and D‑templates differed only by the presence/absence of **Bias‑Annotation** and **Relations**; the unified template keeps the headings everywhere while allowing explicit `Not applicable` statements when justified.
The Alexandrian pattern canon historically calls *Problem frame* “Context”. FPF avoids that label because **Context** is already overloaded in FPF (e.g., `U.BoundedContext` and its Plain‑register label).

#### E.8:4.2 - Stylistic Principles (S-0 ... S-19)

| # | Principle | Guideline |
|---|-----------|-----------|
| S-0 | Narrative Flow Seven-Step Heuristic | Authors are encouraged to structure major paragraphs or subsections using the seven-step mnemonic. |
| S-1 | Density without Jargon | Short declarative sentences; tool names belong in Pedagogy/Tooling. |
| S-2 | Internal Cohesion | Inline references to Pillars and related patterns. |
| S-3 | Embedded Mini-Definitions | Gloss a new term in parentheses on first appearance. |
| S-4 | Contextualisation | Brief historical or disciplinary lineage anchors. |
| S-5 | Prophylactic Clarification | Pre-empt common misreadings inside the prose. |
| S-6 | Quotable Closers | Finish Solution or Consequences with a memorable aphorism. |
| S-7 | Generative over Prescriptive | Present rules as enabling constraints, not bureaucracy. |
| S-8 | Trans-disciplinary Tie-ins | Illustrate using at least two distinct fields. |
| S-9 | Physical Grounding Reference | Link abstractions to a `Transformer` or physical process. |
| S-10 | Punchy Blocks | <= 5 sentences per paragraph; lists for clarity. |
| S-11 | Narrative Flow | Ensure sections read as a continuous story, not bullet soup. |
| S-12 | Full sentences over tags | Avoid “keyword soup”. Each list item SHOULD contain a subject and a verb; prefer 2-4 sentence micro-paragraphs to bare tag lists. |
| S-13 | SoTA-Echo craft | In the SoTA-Echoing section, present: **claim -> practice -> source -> alignment -> adoption status (adopt/adapt/reject)**; cite Bridges & CL when crossing Contexts/planes. |
| S-14 | Support-content sufficiency | New and substantially revised patterns carry enough supporting content to be teachable without nearby project notes. |
| S-15 | Worked slices over scenario labels | Transform-like families show at least one concrete source and resulting-publication slice; scenario names alone are not enough. |
| S-16 | Ordinary vs load-bearing realism | Keep ordinary use light, and make heavier review records explicit only for disputed, high-risk, or higher-impact cases. |
| S-17 | Self-contained monolith prose | A merged pattern must explain itself inside the monolith; planning shorthand and review-context dependencies are not admissible in live prose. |
| S-18 | Reader-role discipline | Keep live pattern prose addressed to the intended FPF user; move package-development and architecture-placement rationale to separate companion notes or clearly marked informative placement notes. |
| S-19 | Precision before relaxation | In load-bearing prose, restore the head kind named by a generic phrase before treating any qualifier as trustworthy semantic guidance; then restore the load hidden in the qualifier before allowing any later plain, didactic, or coarsened restatement. |

Authors use the principles as a *scaffold*, not a straitjacket: the goal
is coherent, engaging insight. Engagement remains subordinate to semantic discipline: hooks, quotable lines, Plain restatements, and didactic images may improve recognition, but any ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load they carry must be recoverable through the governed Tech reading or named neighboring pattern. Ordinary Plain prose without that load stays ordinary prose.

**S-0 (Narrative Flow Seven-Step Heuristic) — explanation**
Narrative flow is recommended to follow these steps: **Hook -> Frame -> Weave -> Anchor -> Bridge -> Flow -> Close**.

Brief explanations:
| Step       | Purpose in a paragraph/section                             |
| ---------- | ---------------------------------------------------------- |
| **Hook**   | Open attention with a vivid but bounded image or paradox that maps back to the governed object and claim. |
| **Frame**  | State the specific question or problem space.              |
| **Weave**  | Connect to earlier patterns or Pillars.                    |
| **Anchor** | Tie to a concrete System/Episteme or physical process.     |
| **Bridge** | Show the implication for the upcoming claim or rule.       |
| **Flow**   | Deliver the formal content or argument.                    |
| **Close**  | End with a quotable line or payoff that reinforces memory. |

Narrative Flow Heuristic also operationalises S-1 (Density w/o Jargon), S-2 (Internal Cohesion), S-4 (Contextualisation), and S-6 (Quotable Closers).
#### E.8:4.2.1 - Recognition text and assurance text
Every canonical pattern SHALL stabilise one governed object early enough that a cold reader can tell what kind of thing the pattern is actually governing. If ordinary forms vary (`note`, `sheet`, `guided UI`, `rendering`, `review aid`), the text must make explicit which of those are merely presentation forms of one governed object and which would instead name a different act, process, work-result record, or governing support companion. Recognition and assurance texts may refine that object differently, but they must not silently swap the central object kind.

If a pattern uses a broad umbrella or head together with a narrower operative branch, the text must also make the stack explicit early enough for first reading: what the broad head names, what the current narrowed branch is, what governed object is actually in play, what move is being carried by that object, and what wider work or process remains outside the pattern. A qualifier alone does not restore that stack.

Under `F.18` local-first naming, the canonical pair here is **recognition text** and **assurance text**.
The earlier provisional `recognition shell / assurance shell` wording is retired.
These names refer to two reading-order roles carried by existing sections or projections inside one pattern; they do **not** mint new `authoritySourceRef` targets, governing-pattern relations, publication-form/face kinds, `SurfaceKind`s, or a second face family.
A third didactic support role remains optional and is justified only when the family is especially easy to misuse, easy to over-read, or hard to teach without extra scaffolding.

The **recognition text** is the first reading text.
It is the part of the pattern that lets a cold working reader recognise the situation quickly enough to decide whether to keep reading.
It should start from a subject-domain or practice moment before internal taxonomy whenever the pattern is meant to help real work rather than only internal canon maintenance.
In practice it usually lives in an early `Use this when` line or equivalent opening, plus the upper parts of `Problem frame`, `Problem`, `Solution`, `Consequences`, and nearby worked slices.
Its job is to make visible:
- what ordinary working situation this pattern is for;
- what goes wrong if the pattern is missed;
- what the pattern buys the reader in practice;
- when this is not the right pattern;
- what governed object is actually being kept stable;
- and, when technical terms must appear early, a pairwise plain gloss for each early load-bearing term.

The **assurance text** is the second reading text.
It carries the heavier load-bearing material that makes the pattern reviewable and auditable:
- declaration blocks and typed fields when those are part of the pattern's declared conformance or boundary claim;
- representation ontology, described-entity discipline, or governed-object discipline;
- any minimal modeling or mathematical lens that keeps the governed object stable;
- guidance/check, invariants, admissibility, and exit or neighbouring-pattern conditions;
- `SoTA-Echoing` when it is carrying live explanatory load;
- and the review hooks that let a broader or more consequential reading be checked explicitly.

The assurance text may sharpen, justify, and discipline the recognition text.
It must **not** silently replace, strengthen, or universalize the claim that the recognition text made visible.
If the recognition text says “this pattern helps with a bounded working situation”, the assurance text must not quietly turn that into an unsupported carrier claim, unsupported guarantee, or broader universality claim.

If a pattern claims **universal** or **transdisciplinary** status, that claim must already be visible in the recognition text.
It is not enough for universality to appear only later in a guidance/check sheet, declaration block, or `SoTA-Echoing` rationale.
A broad claim should therefore be demonstrated in the recognition text through at least **three heterogeneous reader or domain situations**.
When a compact matrix helps, `F.16` is the preferred template for showing that breadth.
If `SoTA-Echoing` is load-bearing, the practical implication of those rows should be recoverable from the recognition text and case bank rather than remaining a late-only justification layer.

A **third didactic support role** means enough didactic and operational support that the pattern survives without nearby project documents. Typical indicators include:
- at least one concrete source and resulting-publication slice in Archetypal Grounding when the pattern governs transforms or publication change;
- at least one boundary-heavy example or anti-example when nearby patterns or other governing support roles are easy to confuse;
- reviewer guidance that tells what to inspect first and which neighboring FPF pattern governs the failure mode and which exact project-side FPF kind and reference carries the claim or effect;
- local mini-definitions or glossary support for recurring terms that would otherwise be recovered only from project context.

Pattern density is therefore not “more metadata” and not “longer tag lists”. It is the presence of enough recognition, assurance, and, when needed, extra didactic support that a reader can understand the pattern, apply it lightly in ordinary cases, and recognise when a heavier review path is required.
#### E.8:4.2.2 - Package-form and governing-pattern relation role-word discipline

FPF pattern prose is not free-form descriptive English. When authors name a *package-form* or a *governing-pattern relation*, they must use role words with stable semantic intent.

Use the following distinctions explicitly:

This is a cross-cutting review discipline, not a replacement for local pattern lexica. For example, `A.6.7` / `A.19.CHR` already carry the suite/kit/pack distinction, and `E.17.1` already carries the viewpoint bundle/family/library distinction.
- **governing pattern** = the pattern that carries the primary guidance/check load of the family;
- **specialization** = a named refinement under an existing governing pattern;
- **overlay** = a cross-cutting governance or reading layer over existing governing patterns;
- **profile** = a declarative review/use role derived from a governing pattern rather than a replacement pattern;
- **family** = a recurring class of cases governed by one pattern or governing support companion;
- **bundle** = a packaged set of defaults, allowances, or coordinated members;
- **cluster** = a navigation or reading grouping; not by itself a governing-pattern claim;
- **suite** = a coordinated set of members with explicit suite semantics under the governing FPF pattern or named authority reference;
- **pack** = an editorial or review grouping, not automatically a semantic-authority claim;
- **kit** = a reusable coordinated publication or boundary-description package with kit-level semantics under the governing FPF pattern or named authority reference;
- **record** = a case, report, or review record;
- **umbrella** = a provisional or review-stage head spanning possible subfamilies before a final governing FPF pattern, accepted `DRR`, or pattern-body decision.

These words are not interchangeable. In particular, authors must not let `cluster`, `bundle`, `suite`, `family`, `profile`, `overlay`, or `umbrella` do the work of an unnamed governing-pattern relation. When that relation matters, it must be stated directly: `specialization under ...`, `profile governed by ...`, `overlay over ...`, `bundle under ...`, or another equally explicit formulation.

A pattern may reuse a pattern-native role word when that role is already defined by the governing pattern. Outside that case, authors must not improvise near-synonyms or shift between role words for stylistic variety.

#### E.8:4.2.3 - Reader-role discipline for live pattern prose

A live pattern is written for its intended FPF user: the person who will use the pattern to organise thought, inspect a case, publish a note, or review a result under that pattern.
Its load-bearing sections therefore explain what the pattern lets that user do, what it forbids, what it costs, and how it relates to neighbouring patterns in user terms. When neighbouring patterns or other governing support roles are named, the prose should answer one user question such as `which neighboring FPF pattern applies`, `which exact project-side FPF kind and reference is live`, `which nearby pattern is easy to confuse`, or `what must stay coordinated here`; it should not read as one explanatory aside about why the package architecture was split that way.
`E.8` reader and reviewer wording is FPF pattern-authoring wording. Project-side publication readers, explanation readers, comparative review units, and participants in named project-side review relations are governed by the publication or project-side patterns that name those live objects, such as `E.17`, `E.17.ID.CR`, `E.17.EFP`, `A.10`, `A.15.4`, `A.20`, or `A.21`.

Authors must keep FPF-development or package-architecture material separate from that user-facing body.
In particular, `Problem`, `Solution`, `Consequences`, `Rationale`, worked slices, and ordinary-vs-load-bearing guidance must not do the work of:
- arguing that the material is worth isolating;
- justifying overlay/profile/governing-pattern or authority-reference choice as a package decision;
- discussing authority-reference freeze, naming freeze, merge posture, blast radius, or safest landing form;
- or narrating future package promotion or defer decisions.

If architecture-placement commentary is still helpful, the default place is a separate companion note or ADR-like architecture note.
A live pattern may include a short optional informative subsection such as `Architectural placement note (informative)` only when that placement materially helps users avoid misuse; even then, it must stay clearly separated from the user-facing solution and rationale rather than replacing them.

#### E.8:4.2.4 - Human-facing fit beyond role correctness
Human-facing fit is also subject-domain fit. A recognition text that starts from internal taxonomy, pattern-placement convenience, or package-architecture wording before the problem-domain moment is still under-authored even if its later guidance/check text is correct. When a broader umbrella name and a narrower operative branch are both live, the recognition text should also tell the reader which stack is actually active rather than leaving that reconstruction to a later declaration block or companion note.

A pattern can already be role-clean, boundary-clean, and reader-role-clean, yet still fail the first minute of use for a cold working reader.
That failure usually appears when the text is admissible but does not yet make the working situation, practical payoff, governed object, non-use boundary, or first action-guiding move visible enough.

**P-2 semantic cleanup check.** When `E.10.SEMIO` is used to repair pattern prose, the first admissible action-guiding move must survive as a remaining admissible reader move or be replaced by a named neighboring-pattern handoff that now carries the live claim. This is a direct `E.2` `P-2` and `E.12` requirement, not an optional style preference. Intentional didactic metaphors and vivid Plain recognition lines are admissible when they are ordinary recognition aids or when their load maps back to Tech under `E.10:6.2`. A semantically corrected rewrite that leaves the recognition text inert is still under-authored.


For canonical patterns, the first reading text should behave as a **recognition text** and the heavier review load should remain in an **assurance text**.

When a pattern claims practice guidance or is meant to be used by engineers, managers, researchers, or other working readers, authors should make the following visible before the heavier harness takes over:
- a recognisable `Use this when` or equivalent first-minute recognition cue;
- a concrete working situation in `Problem frame`, not only taxonomic or pattern-placement language;
- a short statement of what goes wrong if the pattern is missed or misread;
- a short statement of what this pattern buys the reader in practice;
- the first admissible action-guiding move the user should take in that situation;
- a short `Not this pattern when` boundary for ordinary nearby non-use cases;
- one minimally viable worked case or use slice that shows what changes in practice;
- when a typed declaration block, formal lens, or other compact modeling support is load-bearing, a short user-facing statement of what kind of object the pattern is governing and what minimal lens keeps that object reviewable;
- pairwise plain glosses for any load-bearing technical terms that must appear before the heavier declaration role arrives;
- when `SoTA-Echoing` is carrying live explanatory load, a short working-reader implication for each row or cluster of rows and a visible link back to the case bank or worked slices that those rows discipline;
- a visible split between the recognition text and the heavier assurance text or support companion;
- and, if the draft implicitly serves several working-reader situations, an explicit primary working reader, primary concern, or primary viewpoint.

**Problem-frame recognition signature (informative).** A canonical pattern should
expose the working situation through its `Problem frame`, not through one
separate navigation block. When an `E.11` pattern-entry discoverability problem
is live, the same `Problem frame` may also carry candidate-pattern and
tempting-wrong-pattern cues; otherwise it should stay with action guidance
rather than becoming a local catalogue row.

The local recognition signature should make recoverable:

- the concrete working situation;
- the governed object or stabilized concern;
- what goes wrong if the pattern is missed or misread;
- the first admissible action-guiding move and what that move buys;
- the ordinary not-this-pattern boundary;
- the first admissible action-guiding result; when an `E.11` discoverability
  problem is live, the first admissible entry stop or entry-stabilizing result.

`Use this pattern when`, `This pattern applies when`, or equivalent `Problem
frame` prose may be used as the first sentence or compact cue of this
signature.
It is not one separate required section.
Cross-pattern comparison belongs in `J.4`; expanded case reading belongs in
`I.2`.

If the prose points to neighbouring patterns or other governing support roles, it should present them as neighboring FPF patterns, exact project-side FPF kinds and references, or `E.11` entry-load reclassifications rather than as hidden co-authorities of the current pattern.

If the pattern claims broad, universal, or transdisciplinary usefulness, that breadth should already be visible in the recognition text.
At minimum the recognition text should show at least three heterogeneous reader or domain situations rather than one narrow case family with a later broad claim attached.
When a compact matrix helps, `F.16` is the preferred template for making that breadth legible.

This is not a request to flatten the pattern into plain language only.
It is a rule about ordering, layering, and text consistency: the recognition text must help a working reader recognise the pattern early, while the assurance text continues to carry the full semantic load.
If the pattern uses technical lexicon, ontological distinctions, or a mathematical lens, those supports must remain recoverable, but the first reading text should not require the reader to decode that full stack before recognising the working situation.
The assurance text may tighten or discipline the recognition text; it must not silently shift what the recognition text claimed.

**Illustrative migration example (informative).**

Old pre-template top:

```text
Start here when the dominant live question is API, protocol, SLA, published boundary, or compliance wording.
First output: Claim Register.
Neighboring pattern exits / entry-load reclassifications: A.6.B, A.6.C.
```

Repaired Problem-frame recognition signature:

```text
Use this pattern when boundary-facing language - API, protocol, SLO/SLA, compliance clause, or other published boundary description - mixes guidance/check clauses, admissibility gates, duties, and evidence into one sentence or published boundary description.

If missed, the text becomes boundary-claim soup: runtime behavior, governance, and evidence are treated as one undifferentiated promise.

Do not use this pattern merely because the text mentions an API or boundary description. If the live question is still one unstable cue, preserve it through the admissible cue-preservation line first.

First admissible action-guiding result: one `A.6.B`-governed atomic claim set or one Claim Register whose live claim/use questions are explicit enough for the governing FPF pattern or named project-side FPF kind and reference to inspect.
```

#### E.8:4.2.5 - Design-time and run-time referents stay separated in live pattern prose

Live pattern prose must keep its referent index explicit. In ordinary body sections, the default truth-makers are run-time or governed-domain objects, states, moves, boundaries, consequences, and user-facing practical effects. Standard-plane wording is still admissible when the sentence is explicitly about the standard as a normative publication, for example in marked legacy navigation examples, marked informative notes, or conformance/checklist clauses.

Design-time and control-plane referents are different objects. The current draft, current body, current pass, author, reviewer, handoff, packet, governing support companion, landing choice, or other writing-process/control objects must not be smuggled in as the hidden truth-condition of live pattern prose. A quick test is: what makes this sentence true? If the sentence is true because the current text is arranged a certain way, because the author or reviewer must do something next, or because the current control state says so, then it is design-time residue, not live pattern content.

Move that material to the authored-slice carrier, handoff, `DRR`, or companion architecture note. If a sentence is kept in the live pattern, rewrite it so that its truth depends on the governed run-time/domain object or on the standard's declared normative claim set rather than on the current writing pass.

If a pattern or example claims **autonomy** for any Role/Method/Service:
1) Add a subsection **“Autonomy (RoC‑E.16)”** that lists:
   * `AutonomyBudgetDeclRef` (id, version, Scope (G), Γ_time),
   * `Aut-Guard policy-id (PolicyIdRef)`,
   * `OverrideProtocolRef` (SpeechAct names, SoD),
   * pointer to where **Green‑Gate** applies in the Method steps,
   * where **AutonomyLedgerEntry** is recorded on `U.Work`.
2) Include one **Tell‑Show‑Show** vignette that demonstrates **depletion** and **override** handling.
3) Use **LEX‑BUNDLE** terms (Scope (G), Γ_time, Role/Method/Work). Avoid “validity”, “process”, “actor”, “system”, “mechanism” unless mapped to kernel types.

