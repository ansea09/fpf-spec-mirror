> _axiomatic_ → **Constructive** grounding (Γₘ trace via `tv:groundedBy`); _inferential_ → **Logical** grounding (reasoned chain, often KD‑CAL‑backed for epistemic ties); _postulate_ → **Empirical Validation** (evidence bundle with scope and timespan). Empirical Validation (**LA**) may also accompany _inferential_ or _axiomatic_ claims as real‑world confirmation. **Mapping** contributes **TA**, **Logical/Constructive** contribute **VA**, and **Empirical** contributes **LA** (per the Trust & Assurance calculus; no calculus variables appear on the Working‑Model surface).

> **E.14‑P.6 – Parsimony at the surface.**
> No new Working‑Model relation types are introduced if the existing Logical aliases plus Constructive grounding suffice to capture the intended meaning.

> **E.14‑P.7 – Evidence is a first‑class support.**
> When *postulate* is chosen, authors **SHALL** attach an **evidence pointer** (Empirical Validation) appropriate to the claim and context, governed by `U.EvidenceRole` within a declared `U.BoundedContext`.

> **E.14‑P.8 – Working-model-first is not explanation-thin.**
> Human-facing parsimony does **not** license under-explained pattern prose. When a pattern claims a Working‑Model benefit, it **SHALL** still provide enough problem framing, rationale, and worked slices that readers can tell what the model clarifies, what remains on the assurance shoulders, and when a heavier review path is required.

### E.14:5 - Layer Standard & Downward Flow (Working‑Model → Assurance)

This section defines **what each layer is for**, **what it guarantees**, and **how a single Working‑Model statement is carried down**.

#### E.14:5.1 - Working‑Model (what humans see)

**Purpose.** A small, curated graph of kinds and relations that a mixed team can read at a glance.

**Elements.**

* **Kinds** — one **chosen concept** per node (no slash‑labels).
* **Relations** — a short list intelligible to non‑specialists (e.g., *Component‑of*, *Member‑of*, *Aspect‑of*, plus a small number of cross‑disciplinary ties such as *Interface‑of* or *Constituent‑of*).
* **Language register badges** — labels shown in the Working-Model are L‑1 or L‑2; L‑3/L‑4 remain in Mapping as synonyms or symbols.

**Obligations.**

* Every Working‑Model edge and node is **grounded downward** (see below).
* The Working‑Model **does not display** constructor jargon, proof terminology, or evidence identifiers; those live in Assurance and are **available on demand**.

#### E.14:5.2 - Assurance‑1: Mapping (from words to kinds)

**Role.** Consolidate human labels from varied sources and **bind them to the chosen kinds** used on the Working‑Model.

**Guarantee.** For any Working‑Model label, there exists a **stable alignment** to exactly one kind; synonyms, abbreviations, locales and registers are recorded here, **not** in the displayed Working-Model. Mapping primarily raises **Typing Assurance (TA)** by consolidating synonyms/registers and binding tokens/labels to **one chosen kind**; calculus‑level metrics live outside Part E.

**Deliverable.** A compact alignment table per scope that makes it obvious which **one label** the Working‑Model will show and which alternatives are tolerated in background sources.

*(Rationale: Working teams speak many dialects; the Working‑Model speaks one. Mapping is the interpreter.)*

#### E.14:5.3 - Assurance‑2: Logical (from Working‑Model relations to alias semantics)

**Role.** Give each Working‑Model relation **a precise alias meaning** and **its admissible use‑cases**, keeping the surface vocabulary small.

**Guarantee.** A Working‑Model edge such as *Component‑of* or *Aspect‑of* **carries one intended reading** (transitivity/antisymmetry expectations, scope notes), sufficient for auditors to assess whether the **use is legitimate** in a given context.

**Deliverable.** A short set of alias rules: “When an edge is labeled *Component‑of* at the surface, it intends the structural reading that is later verified by construction.” The Logical layer is **the Standard** that ties human labels to accepted meanings (CT2R alias rules); it primarily contributes **Verification Assurance (VA)**. Calculus‑level symbols are not used in E‑patterns.

*(Rationale: logical aliasing protects the small surface from relation proliferation while keeping meanings crisp.)*

#### E.14:5.4 - Assurance‑3: Constructive (from meanings to generative traces)

**Role.** Provide **extensional guarantees** by **constructing** the wholes, collections, and slices that Working‑Model relations speak about.

**Guarantee.** For structural edges, **there exists a constructional narrative** (e.g., *sum*, *set*, *slice*) that, if told, would recreate the whole from its parts or the aspect from its bearer; this makes identity and containment **trackable and testable** across scales.

**Deliverable.** A **single generative story** per structural link (axiomatic justification). For non-structural ties on the surface (e.g., epistemic links), Constructive may be absent; Logical/Empirical take the lead. Constructive contributes **VA** (extensional identity via Γₘ); for **structural** edges, `tv:groundedBy` **MUST** reference exactly one Γₘ trace.

*(Rationale: constructional grounding turns everyday part‑whole talk into statements whose identity conditions are not left to taste.)*

#### E.14:5.5 - Assurance‑4: Empirical Validation (from claims to observed world)

**Role.** Record when and where a Working‑Model claim meets reality.
**Guarantee.** Every empirical binding names a **`U.BoundedContext`**, a **target claim/scope**, and a **timespan**; **staleness/refresh** are managed per context policy.
**Deliverable.** A `U.EvidenceRole` binding (status‑only) anchored into the Evidence–Provenance chain. Empirical Validation contributes **LA** (raises empirical **R** and constrains **G** to its validated envelope).

#### E.14:5.6 - The downward grounding for a single surface statement

Consider a Working‑Model arrow **A –Component‑of→ B**:

1. **Mapping** shows that the words *A* and *B* are the chosen labels for their kinds; it retains tolerated synonyms and symbols in the background.
2. **Logical** confirms that **Component‑of** on the surface means the **structural reading** with its ordinary mereological expectations; if the surface used *Member‑of* instead, Logical would similarly certify the intended reading and its boundaries.
3. **Constructive** exhibits the **constructional narrative** (e.g., a _sum_ of parts resulting in **B** with **A** among them), which yields **axiomatic justification** for the structural edge, sets `validationMode=axiomatic`, and binds the edge via **`tv:groundedBy → Γₘ.sum|set|slice`**.
4. **Empirical Validation** records the **evidence pointer** and scope that make the claim auditable within its `U.BoundedContext` (required for *postulate*; optional reinforcement for other stances).

Together, these three **ground the human arrow without leaking their machinery upward**. The Working‑Model remains simple; the Assurance stack carries the proof.

### E.14:6 - Archetypal Grounding *(System / Episteme)*

> **Tell–Show–Show.** The principle is stated once, then shown on a `U.System` case (structural) and on a `U.Episteme` case (knowledge‑bearing), in line with the authoring template.

#### E.14:6.1 - `U.System` — Working‑Model first, Constructive grounding available

* **Publication (Working‑Model).** Authors state structure using familiar relations (e.g., *Impeller* **ut\:ComponentOf** *Pump*; *Pump* **ut\:ComponentOf** *Skid*). Nothing else is required for readers to follow the design.
* **Assurance (downward grounding).** When a higher-assurance claim is sought, the same author **narrates** the constructive story of the whole as a composition of parts and, where appropriate, attaches a downward grounding to that narrative (sum / set / slice). The narrative remains concept‑level and notation‑neutral; order and time stay out of structure and are expressed in their own planes.
* **Canonization move.** Readers continue to see Working‑Model relations as the primary surface; the constructive story is *supporting*, not *defining*.

#### E.14:6.2 - `U.Episteme` — Working‑Model first; Logical/Mapping preferred; Empirical evidence as appropriate

* **Publication (Working‑Model).** Authors connect meaning-bearing epistemes or publications using knowledge relations (e.g., **RepresentationOf**, **UsageOf**) in the same human‑oriented style.
* **Assurance (downward grounding).** Here assurance typically flows to the **Logical** or **Mapping** shoulders (reasoned argument; type/lexical alignment). **Empirical Validation** is used where observation is the right currency (status‑only roles on epistemes); Constructive grounding is optional and used only where a structural interpretation is genuinely intended.
* **Canonization move.** Again, Working‑Model text is the public form; assurance is attached deliberately and separately, without leaking method or time semantics into structure.

**6.3 - Pattern lesson (both cases)**
The **Working‑Model layer remains the canonical publication surface** for authors and reviewers; **assurance layers** (Mapping / Logical / Constructive) are **opt‑in** and used purposefully, with grounding flowing **downwards** from the Working‑Model to the appropriate shoulder. This presentation respects the authoring template’s *Archetypal Grounding* requirement and keeps notational choices illustrative rather than defining.


### E.14:7 - Bias‑Annotation *(what to watch for, and the counter‑moves)*

| Bias (name)                       | Symptom in drafts                                                                           | Conceptual counter‑move                                                                                                                        | Where this is governed                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Formalism capture**             | Treating a constructive narrative as “the real thing,” with **ut:\*Of** reduced to a label. | Re‑assert Working‑Model primacy: publish in **ut:\*Of**; attach assurance **downwards** only when needed.                                      | E.8 template; Notational‑Independence guard‑rail.                    |
| **Canonical inversion**           | Demanding constructive grounding for epistemic links by default.                            | Keep the **progressive** stance: prefer Logical/Mapping assurance for knowledge claims; raise to Constructive only when structure is at issue. | Authoring template; Working‑Model pattern family.                    |
| **Layer leakage (order/time)**    | Encoding sequence or phase as part–whole to “strengthen” claims.                            | Keep **order**/**time** in their planes; do not smuggle them into structure.                                                                   | Style/structure guidance in Part E; flavour separation in Γ‑family.  |
| **Collection ↔ Composition swap** | Using **MemberOf** as if it implied **ComponentOf** identity.                               | Keep collections (*set*) distinct from assemblies (*sum*); do not upgrade membership to component status.                                      | Working‑Model mereology guidance (Part B/C linkage).                 |
| **Notation lock‑in**              | Letting a diagram or syntax define meaning.                                                 | Apply **Notational Independence**: define semantics in prose (maths if needed); treat renderings as informative.                               | Notational‑Independence guard‑rail.                                  |
| **Backwards dependency**          | Letting an assurance publication or record redefine public terms.                                        | Preserve **unidirectional dependence**: Working-Model terms do not derive their meaning from assurance publications or records.                              | Part E guard‑rails (dependency discipline).                          |
| **Silent stance**                 | Publishing claims with no declared assurance stance.                                        | Declare the stance explicitly (e.g., working claim vs reasoned vs constructive).                                                               | Style/authoring discipline in Part E.                                |

> **Reading reminder.** Bias checks are *conceptual* reading aids; they never introduce notational or tooling mandates.

### E.14:8 - Conformance Checklist *(normative; author‑facing duties for thought and prose)*

| ID                                         | Requirement                                                                                                                                                                      | Purpose                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑E14‑1 (Working‑Model primacy).**      | Authors **SHALL** publish claims in **Working‑Model** form (human‑oriented **ut:\*Of** relations or equivalent domain statements) as the canonical surface for readers.          | Preserve human‑first canon and didactic clarity.              |
|**CC‑E14‑2 (Downward grounding).** | When assurance is attached, grounding **SHALL** flow **downwards** from the Working‑Model to the appropriate assurance shoulder (**Mapping / Logical / Constructive / Empirical**) and **SHALL NOT** impose vocabulary back onto the Working‑Model. | Maintain plane separation and cognitive economy. |
| **CC‑E14‑3 (Stance declaration).**         | For any claim where assurance matters, the author **SHALL** declare `validationMode` (*postulate / inferential / axiomatic*).                                                    | Make assurance intent explicit and readable.                  |
| **CC‑E14‑4 (No order/time in structure).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage as part–whole; keep them adjacent in their own planes.                                           | Prevent layer leakage and category errors.                    |
| **CC‑E14‑5 (Collection ≠ Composition).**   | Authors **SHALL** keep **membership** claims distinct from **component** claims; no implicit upgrade from collection to assembly.                                                | Guard extensional identity and reader expectations.           |
| **CC‑E14‑6 (Notational independence).**    | Core meaning **MUST NOT** hinge on a specific diagram or syntax; any rendering present **SHALL** be marked informative.                                                          | Ensure longevity and cross‑discipline portability.            |
| **CC‑E14‑7 (Layer direction).**            | Authors **SHALL** avoid back-defining Working-Model terms by their assurance publications or records; dependence is one‑way (Working‑Model → Assurance).                                       | Preserve unidirectional dependence of layers.                 |
| **CC‑E14‑8 (Template compliance).**        | Sections **SHALL** follow the canonical pattern order; *Archetypal Grounding* is mandatory for architectural patterns.                                                                            | Keep patterns comparable and auditable by reading.            |
| **CC‑E14‑9 (Progressive formality).**      | Authors **SHOULD** escalate assurance deliberately (from working claim to reasoned to constructive), and use **Empirical Validation** where observation is the right currency.    | Support staged formality without overloading early drafts.  |
|**CC-E14-10 (Structural grounding handshake).** | For **structural** edges on the Working-Model, authors **SHALL** set `validationMode=axiomatic` and provide **Constructive** grounding with `tv:groundedBy → Γₘ.sum|set|slice` (see **Compose-CAL** and **CT2R-LOG**). Exactly **one** Γₘ trace is permitted per edge (CI rule alignment). | Aligns E.14 with CT2R-LOG and Compose-CAL; ensures extensional identity. |
| **CC‑E14‑11 (Empirical bindings).**        | When `validationMode=postulate` (or when adding real‑world confirmation), authors **SHALL** bind evidence via `U.EvidenceRole` in a declared `U.BoundedContext` with an explicit **timespan** and provenance anchors. | Aligns with Evidence Graph Referring and empirical ageing policies. |
| **CC-E14-12 (F-declaration).**             | Normative Working-Model publications **SHALL** declare `U.Formality = Fk` per **C.2.3** (**recommended F ≥ F3** for readable surfaces). Assurance publications or records **MAY** carry higher F; **min-F** applies to composites. | Aligns E.14 with the unified Formality characteristic; avoids legacy “tiers/modes”. |
| **CC‑E14‑13 (Light records, not thin prose).** | Authors **SHALL NOT** use the Working‑Model-first stance as a reason to strip problem framing, rationale, or worked slices out of the pattern text. Ordinary use may stay light, but readers **MUST** still be able to understand the pattern without nearby project notes. | Keeps human-facing economy from collapsing into under-explained prose. |
| **CC‑E14‑14 (Recognition text before assurance text).** | When a pattern claims a Working‑Model or other human-facing benefit, authors **SHALL** keep recognition-first working text distinct from the heavier assurance text. The assurance text **MAY** refine and justify the working text, but it **SHALL NOT** silently change the recognition-text claim. If the pattern claims broad or transdisciplinary reach, the working text **SHOULD** show heterogeneous situations early, preferably through an `F.16`-style example matrix or an equally explicit alternative. | Keeps Working‑Model-first drafting from collapsing into either thin prose or late-only universality. |

*All obligations above are **conceptual** and apply to thought and prose; they introduce no notational or data‑processing requirements.*

**E — Conceptual Examples (no notation, no data handling)**

1. **Assembly from parts → “Component Of”**
   A pump skid is agreed to be nothing over and above its pump, frame, reservoir, and valve set considered together. Because the whole is conceptually *constructed* from those parts, the team may safely speak of each part as *Component Of* the skid. The justification is the construction itself: if any listed part were removed, the very same skid would no longer exist as that whole. This keeps identity extensional and makes the engineer‑facing alias (“Component Of”) truthful rather than conventional.

2. **Parallel elements gathered → “Member Of”**
   A test rig has four identical cartridges used in parallel. The rig treats them as a conceptual *gathering*; membership is fixed by inclusion in that gathering, not by sequence or timing. Speaking of each cartridge as *Member Of* the rig’s cartridge bank is then licensed by the same gathering act. Engineers can keep saying “member,” while architects know the warrant is the underlying construction of the bank as a collection, not an accidental tagging.

3. **Focused facet carved → “Aspect Of”**
   When the team talks about the *thermal envelope* of a reactor, they are not multiplying entities; they are taking the already‑agreed reactor and conceptually *carving out* its thermal facet for focused reasoning. Calling that carve‑out an *Aspect Of* the reactor is justified because the aspect owes its identity to the parent and the chosen facet, and nothing else. This licenses disciplined talk about “boundary,” “interface,” or “envelope” without mistaking them for independent systems.

> **Notes across the examples**
> • Everyday aliases (*Component Of, Member Of, Aspect Of*) remain the only labels engineers need to see; their truth is anchored by prior constructional choices.
> • Structural links draw on **Constructive** grounding; **epistemic links**—like “Representation Of” or “Usage Of”—may instead rely on **Empirical Validation** (evidence bundles) or **Logical** grounding appropriate to the claim.

**F — Resulting Context (after you apply the pattern)**

**What improves**

* **Single dial for containment.** Teams can ask one plain question, “what is inside what?”, and trust that all structural talk reduces to shared constructional choices rather than ad-hoc relation lists. Ontologists keep rigorous warrants without overloading day-to-day readers.
* **Extensional identity by default.** Wholes are the wholes they are because of the parts gathered; collections are the collections they are because of their members; aspects inherit identity from their parent and facet. This prevents silent drift when labels change.
* **Layer harmony.** Engineer‑facing aliases live at the same level as other relation names, while their warrants live one step below, keeping human language clean and the generative basis auditable.

**What to watch**

* **Discipline for structural relation kinds.** A structural link that lacks a constructional warrant is conceptually unsafe. Conversely, forcing epistemic links to pretend they are structural over-physicalises knowledge claims; for those, evidence or argument is the right currency.
* **Author workload moves, not grows.** Day-to-day model authors stay with aliases; specification authors carry the responsibility for ensuring every structural statement really follows from a sum, a gathering, or a carve-out. This is a conscious shift of complexity away from operations and into the pattern's foundation.

**Invariants you must preserve**

* **Parsimony of constructors.** Build wholes by summing parts; build banks by gathering elements; focus facets by carving aspects. Do not invent extra generative acts for parallelism or time‑slicing; those concerns belong to other conceptual services.
* **Two-relation-kind justification.** Structural talk rides on construction; epistemic talk rides on evidence or proof. Keep the boundary sharp so that later reasoning (about reliability, compliance, or policy) remains clear.

**Known consequences**

* **Stable queries, fewer surprises.** Because aliases are backed by shared constructions, teams from different disciplines can interoperate without renegotiating meanings at hand‑off.
* **Audit trail without jargon.** Reviewers can trace every structural claim to a prior constructional choice, while everyday collaborators keep using familiar relation names.


### E.14:9 - Consequences

| Benefits                                                                                                                                                      | Trade‑offs / Mitigations                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Human‑first clarity.** Readers see the **Working‑Model layer** as the canonical publication form; Assurance layers remain optional and purpose‑driven.      | **Extra author discipline.** Declaring the stance and (when needed) a short grounding narrative takes effort; mitigated by the authoring template and style guide.           |
| **Progressive assurance.** Teams can start light and raise strictness deliberately (Mapping → Logical → Constructive) without changing the visible relations. | **Risk of “forever‑light.”** Some models may remain in low‑assurance stances; mitigated by formal maturity checks and reviewer prompts to escalate where risk warrants.  |
| **Layer hygiene.** Order/time remain outside mereology; structural identity is neither overloaded nor diluted.                                                | **Split attention.** Authors must learn to keep planes distinct; mitigated by the Tell‑Show‑Show pedagogy across architectural patterns.                                             |
| **Spec cohesion.** The same section order and safety subsections (Bias‑Annotation, Conformance Checklist) keep patterns comparable and auditable.             | **Tighter prose.** Patterns grow by a few concise checks; mitigated by the canonical template.                                                                               |

> **Quotable closer.** *“One layer to speak, three layers to justify—only when needed.”*


### E.14:10 - Rationale

**Why Working‑Model is canonical.** FPF privileges **human‑oriented relations** as the primary interface for thinking and communication. This satisfies didactic primacy while preserving conceptual integrity: formal work serves the human layer, not the other way around. The canonical template and style principles institutionalise this choice without inviting notation lock‑in.

**Why grounding flows downward.** Mapping, Logical, Constructive, and Empirical supports are **assurance shoulders** that sit *beneath* the Working‑Model claim. Authors select the shoulder(s) that fit purpose and risk: type/lexical alignment (**TA**), reasoned consequence (**VA**), constructive reconstruction (**VA**), and real‑world confirmation (**LA**). This keeps the Kernel small, avoids plane‑mixing, and provides a clear path to higher-assurance guarantees when warranted.

**Why patterns teach before they tighten.** The Tell‑Show‑Show requirement couples each universal rule with System/Episteme illustrations, reducing cognitive load and preventing premature formalism. It is the didactic mechanism that makes Human‑Centric Canonization practical across disciplines.

**Why no notation talk in Core.** Guard‑rails and the style guide prohibit tool jargon and notation dependence inside normative prose; meanings are given in words and mathematics, with any renderings treated as illustrative only. This preserves longevity and cross‑disciplinary portability.

### E.14:11 - Relations

**Builds on:**

* **E.8 Authoring Conventions & Style Guide** — section order, style principles, and mandatory safety subsections used here.
* **E.7 Archetypal Grounding** — the Tell‑Show‑Show rule applied in this pattern’s own Grounding section.
* **C.2.3 Unified Formality Characteristic (F)** — declares the **F** scale and **ΔF** moves for progressive rigor; Working-Model publications **SHALL** declare **F** and remain notation-agnostic.

**Coordinates with.**

* **CT2R‑LOG — Working‑Model Relations & Grounding** — alias rules and `tv:groundedBy` Standard for edges grounded in Γₘ.
* **Compose‑CAL (Constructional Mereology)** — provides the constructive shoulder (Γₘ: **sum | set | slice**) used to ground structural edges.
* **E.10 Lexical Discipline & Stratification** — ensures naming discipline and register hygiene when the human layer is published.

**Constrains:**

* All architectural patterns that publish relations **SHALL** present them in the Working‑Model layer and **MAY** attach assurance only as needed, preserving plane separation and notational independence. (Template conformance as per E.8.)

**Informs.**

* Part F unification practices (context of meaning, bridges, fit levels) by reinforcing the preference for human‑readable labels with explicit alignment notes rather than silent formal substitutions.

### E.14:End


## E.15 - Lexical Authoring & Evolution Protocol  (LEX‑AUTH)

> *Author patterns as evidence‑bearing epistemes, evolve them via governed open‑ended search, and publish an auditable trace that improves quality—not just compliance.*

### E.15:1 - Context

FPF patterns are the **canon**: they define the generative rules that other artifacts depend on. Teams need to **change** patterns as the SoTA moves, but ad‑hoc edits lead to drift, low comparability, and brittle downstream updates. We need a **method** that (a) *generates* better alternatives, (b) *selects* them against explicit quality/assurance targets, and (c) *publishes* a machine‑ and human‑checkable **trace** that can be replayed, audited, and re‑run. (Built to cohere with **DRR (E.9)**, **LEX‑BUNDLE (E.10)**, **Canonical Evolution Loop (B.4)**, **NQD/E‑E (C.18 and C.19)**, **Evidence Graph Referring (A.10)**, **Trust (B.3)**, **F‑Suite validation (F.15)**.)

### E.15:2 - Problem

Without a disciplined authoring protocol:

* **One‑shot generation** dominates; there is no *evolutionary* path from vN → vN+1.
* “Trace” degenerates into a proof‑of‑work: *a method ran*, not *quality improved*.
* Pattern edits blur **lexicon vs. norms vs. examples**, breaking didactics and tool‑independence.
* SoTA content is cited but not **integrated** via Bridges & CL; claims get over‑ported.

### E.15:3 - Forces

| Force                                       | Tension we must resolve                                                           |
| ------------------------------------------- | --------------------------------------------------------------------------------- |
| **Generativity vs Assurance**               | Open‑ended idea generation must not erode safety/traceability.                    |
| **SoTA speed vs Canon stability**           | Frequent small updates must preserve conceptual integrity and roll‑up invariants. |
| **Local meaning vs Global reuse**           | Context‑local meaning must cross contexts only via **Bridges** with CL penalties. |
| **Notational independence vs Checkability** | Text must stay notation‑free yet be verifiable by Tooling harnesses.              |

### E.15:4 - Solution — A *governed evolutionary* authoring method with a publishable **LEX‑AUTH Trace (LAT)**

LEX‑AUTH defines **how** a pattern is **proposed, varied, selected, validated, and merged**, with artifacts and evidence fit to the FPF kernel.

#### E.15:4.1 - Method (design‑time choreography)

**Stage A — Frame & Scope (Context, Objectives, Invariants)**

1. **Anchor** the work in a **`U.BoundedContext`** for the spec (e.g., `FPF/Core`), cite governing guard‑rails (**E.5.\***), and state **objectives** for the change (e.g., clarity ↑, universality ↑, assurance cost ↓).
2. **Declare the Delta‑Class** (see §4.3) and **impact radius** (dependent patterns, bridges, tests).
3. **Fix acceptance targets** (see §4.4 Quality & SoTA metrics).

**Stage B — Generate candidates (SoTA + NQD)**
4. **Harvest SoTA** inputs (standards, rival patterns, lived domain idioms) and **bind** them as *evidence* via `U.EvidenceRole` with **claim/claim‑scope/timespan** (empirical vs deductive lines).
5. **Generate candidate variants** using **NQD‑CAL** engines (Novelty/Quality/Diversity) with an **E/E policy** (explore↔exploit governor) to populate a **Pareto front** of pattern phrasings/structures. *(No single shot; multiple candidate clauses compete.)*

**Stage C — Shape & Align (Structure, Bridges, USM)**
6. **Shape** top candidates into the standard **architectural template** (Context → Problem → Forces → Solution → CC → Consequences → Rationale), obeying **LEX‑BUNDLE** (no tooling jargon; twin registers allowed).
7. **Bridge across Contexts** explicitly (F.9): any imported definitions/claims declare **CL** and *loss notes*; propose scoped **narrowing** where needed.
8. **Type scopes** with **USM (A.2.6)**: keep **ClaimScope (G)** distinct from **WorkScope**; no “applicability/envelope” smuggling.

**Stage D — Validate & Decide (Assurance, Tests, DRR)**
9. **Run the harness**: update **SCR/RSCR** (F.15), lint lexical rules (E.10), run **Γ‑consistency** and **RSG/SoD** checks where relevant.
10. **Score** candidates on **Quality & SoTA metrics** (§4.4) and **assurance deltas** (Δ⟨F,G,R⟩).
11. Record a **DRR** (E.9) with *options considered*, *trade‑offs*, chosen candidate, *blast‑radius*.
12. **Merge** the winner; version pattern **SemVer** by Delta‑Class.

**Stage E — Publish & Monitor**
13. Publish the **LEX‑AUTH Trace (LAT)** (§4.2) as the separate authoring/evidence record for the change.

14. Schedule **evidence refresh** windows and an **evolution watchpoint** (B.4 loop): when metrics or SoTA inputs decay, reopen Stage B.

#### E.15:4.2 - The **LEX‑AUTH Trace (LAT)** — what it is and why it matters

A LAT is **not** “we ran a script.” It is a **structured episteme** that lets others **reproduce quality gains** and **re‑run** the search when SoTA shifts.

**LAT minimal contents (publish with the pattern):**

1. **Context & version** (pattern id, context, SemVer, Delta‑Class).
2. **Objective vector** (what we tried to improve: clarity, universality, assurance cost, etc.).
3. **SoTA pack** (sources bound as `U.EvidenceRole` with claim/scope/time and polarity).
4. **NQD settings** (emitters/lenses, diversity characteristics) + **E/E policy** used.
5. **Candidate set** (top K variants with NQD scores + short deltas from baseline).
6. **Bridge ledger** (all cross‑context imports with **CL** and loss notes).
7. **Assurance delta** (Δ⟨F,G,R⟩ from baseline; penalties from CL applied).
8. **Harness results** (checks passed/failed, test diffs).
9. **DRR link** (decision rationale id).
10. **Refresh policy** (evidence decay windows and triggers).

**Uses of the LAT:**
*Reproducibility* (re‑run B‑stages as SoTA changes), *assurance* (explicit impact on F/G/R), *portfolio health* (diversity/coverage), *teaching* (didactic before/after), and *cross‑context safety* (no silent imports).
Publish the pattern with its **DRR**, and publish the **LAT** as the separate authoring/evidence record for the change. The LAT carries the reproducible authoring trace and cites the DRR as the governing decision record. The DRR remains complete without LAT citations; it may summarize already-available decisive evidence by value when that evidence materially shaped the content choice. If later LAT or refresh evidence motivates a reopened or revised choice, carry that evidence into the successor DRR or other admissible decision record rather than retrofitting the accepted DRR.


**Example of a LAT‑stub**
```
LAT:
  context: FPF/Core, pattern: F.15, semver: x.y+1, delta-class: Δ‑2
  objectives: {clarity↑, universality↑, assurance-cost↓}
  SoTA-pack: {OpenAlex 2025‑Q3, SPECTER2‑23, DPP‑2019, MAP‑Elites‑2015+}
  NQD-settings: {CharacteristicSpace: domain‑family × …, grid: CVT@k=16}
  candidates: K=4 (wording of RSCR‑F04 & gates)
  bridge-ledger: none (intra‑canon refs only)
  assurance‑delta: ΔF=+, ΔG=+, ΔR=+ (after CL‑penalties=0)
  harness: LEX‑BUNDLE lint pass; F‑suite pass; Γ‑consistency ok
  DRR-id: DRR‑2025‑09‑DFCM‑roll‑in
  refresh: F1‑Card edition refresh window = 6 mo
```

#### E.15:4.3 - What counts as “changed the pattern as a whole” — **Delta‑Classes & versioning**

Classify the intended change **before** work starts (declare it in the DRR framing; echo it in the LAT or evidence record when one is used):


* **Δ‑0 Lexical polish** — wording/ordering only; **no** change to CC or semantics. → *Patch* (x.y.**z**+1).
* **Δ‑1 Didactic restructure** — narrative/layout; **unchanged** Conformance Checklist (CC). → *Minor* (**x.y**+1.0).
* **Δ‑2 Normative refinement** — CC tightened/clarified; *semantics preserved* by test equivalence. → *Minor* (**x.y**+1.0) + **RSCR** required.
* **Δ‑3 Semantic change** — CC **adds/removes** requirements; downstream requirements shift. → *Major* (**x**+1.0.0) + **impact review** + **bridges refresh**.

> **Definition of “pattern changed as a whole”:** any **Δ‑2/Δ‑3** change (i.e., the **normative surface** or **semantics** changed) counts as a pattern change in the canonical corpus and triggers harness & bridge reviews.

#### E.15:4.4 - Quality & SoTA metrics (selection lenses)

**Mandatory lenses** (declare in LAT; higher is better unless noted):

* **Clarity** (readability; plain‑register score from didactic rubric).
* **Universality** (C‑1): *≥3 heterogeneous domains* anchored in the Archetypal section.
* **Lexical discipline** (E.10): 0 violations (DevOps lexicon, process/function conflations).
* **Assurance delta**: ΔF (formality), ΔG (scope clarity), ΔR (reliability after CL penalties).
* **Bridge integrity**:  Bridge integrity (policy lens): declare minimum CL thresholds per Context policy; penalties route to R only (B.3/F.9); record policy‑id in LAT.
* **Test conformance**: F‑suite pass; RSCR clean.
* **Exploration health** (NQD): diversity coverage > threshold; no premature convergence.
* **Didactic economy**: length vs density ratio within band; “Tell‑Show‑Show” present.

**Optional lenses** (context‑specific): *Ethical/SoD guard strength; cross‑scale roll‑up integrity; aggregation proofs present;* etc.
### E.15:5 - Conformance Checklist (normative)

**CC‑LA‑1 (Context anchoring).**
Every authoring run **MUST** declare a `U.BoundedContext`, Delta‑Class, objectives, and acceptance lenses **before** generating candidates.

**CC‑LA‑2 (SoTA as evidence).**
External inputs **MUST** be bound as `U.EvidenceRole` epistemes with **claim, claim‑scope, polarity, timespan** (formal/empirical lines). No raw links.

**CC‑LA‑3 (Open‑ended generation).**
At least **K≥3** candidate variants **MUST** be generated via **NQD‑CAL** with a declared **E/E policy**; single‑shot edits violate LEX‑AUTH.

**CC‑LA‑4 (Bridges & CL).**
Any cross‑context reuse **MUST** appear in a **Bridge** with **CL** and *loss notes*. CL penalties apply to **R‑lane** when scoring.

**CC‑LA‑5 (Harness).**
The candidate winner **MUST** pass **LEX‑BUNDLE** lint, **SCR/RSCR** tests, Γ‑consistency, and SoD/RSG gates where applicable.

**CC‑LA‑6 (Assurance deltas).**
The LAT **MUST** publish Δ⟨F,G,R⟩ relative to baseline, explicitly accounting for CL penalties and any narrowed scopes.

**CC‑LA‑7 (DRR).**
A **DRR** entry is mandatory for Δ‑2/Δ‑3 changes; it records options considered, rationale, and impact radius.

**CC‑LA‑8 (Refresh plan).**
Empirical evidence in the LAT **MUST** carry a **decay/refresh** window; a watchpoint **MUST** be scheduled in the Canonical Evolution Loop.

**CC‑LA‑9 (Publication).**
Publish the **pattern + LAT** together; past LATs are immutable. New runs produce new LATs.

### E.15:6 - Consequences

**Benefits.**
*Evolutive quality*: patterns improve through **search + selection**, not edits by fiat. *Auditability*: a re‑runnable **LAT** shows *why* the chosen variant won. *Safety*: cross‑context reuse is explicit and penalized appropriately. *Comparability*: Δ‑classes & SemVer let downstream readers predict blast‑radius.

**Trade‑offs.**
Some ceremony (LAT/DRR, NQD lenses) and maintenance (evidence refresh, bridge upkeep). These costs buy reproducibility and SoTA tracking.

### E.15:7 - Rationale & Links (informative)

LEX‑AUTH extends the FPF constitution by **operationalising pattern evolution**: it plugs **B.4 Canonical Evolution Loop** into **E.9 DRR**, binds **SoTA** via `U.EvidenceRole` and **KD‑CAL**, drives **candidate generation** with **C.18 NQD‑CAL** under **C.19 E/E‑LOG**, enforces **lexical discipline** via **E.10 LEX‑BUNDLE**, and validates with **F.15** regression harnesses. Cross‑context safety is carried by **F.9 Bridges** with **CL penalties** in **B.3 Trust**. The whole remains **notation‑independent** (E.5.2) and stays within the **Core → Tooling → Pedagogy** dependency rule (E.5.3).

### E.15:8 - Operators (authoring deltas you are allowed to apply)

* **Refine** (tighten CC without changing acceptance meaning).
* **Split/Merge** (factor patterns; preserve links; update Bridges).
* **Generalise/Constrain** (expand/restrict ClaimScope (G) with proofs or loss notes).
* **Rephrase** (clarify language; leave CC untouched).

Each operator carries a default **Delta‑Class** and test obligations.

### E.15:9 - Self‑application Work Log (how this very pattern was authored)

> *This is **not** chain‑of‑thought; it is the required **`U.Work` evidence** for LEX‑AUTH.*

**Context.** `FPF/Core` (Canon); **Delta‑Class:** Δ‑2 (normative refinement by addition of method & CCs).
**Objectives.** Add an *evolutionary* authoring method; make trace *useful* (quality‑bearing); align with SoTA machinery already in spec.
**SoTA pack (evidence bound).** Prior FPF kernel commitments to **DRR (E.9)**, **E.10 LEX‑BUNDLE**, **B.4 Evolution**, **C.18 and C.19** NQD/E‑E, **F.15** harness, **F.9** Bridges, **B.3** Trust; these are treated as the authoritative internal SoTA for the Canon here.
**NQD/E‑E.** Generated ≥3 alternative Solution sections; finalist chosen for clearer Δ‑classes and actionable LAT contents.
**Bridges.** No cross‑external mapping; intra‑canon references only (CL=3).
**Harness.** LEX‑BUNDLE lint (no tooling jargon), CCs unique/atomic, didactic “Tell‑Show‑Show” via Self‑application log, Universality criterion met by cross‑kernel applicability.
**Assurance Δ.** F: + (explicit method & CCs); G: + (scope separation & Δ‑classes); R: + (LAT obligations + bridge penalties).
**DRR.** Recorded: alternatives considered (lighter trace vs full LAT), chosen design (full LAT).
**Refresh.** Reopen when SoTA (e.g., G‑suite authoring kit or CHR templates) evolves or when LAT misuse is seen in reviews.

### E.15:End

## E.16 - RoC‑Autonomy Budget & Enforcement

**Intent.** Make any claim of autonomous behavior testable and enforceable via a published **AutonomyBudgetDecl**, **Guarded enactment**, **Override SpeechActs with SoD**, and a **Work‑anchored AutonomyLedger**.
**Rule (summary).** If a Role/Method/Service claims autonomy, authors **MUST**: (i) publish an `AutonomyBudgetDecl` with `AdmissibilityConditionsId` and `OverrideProtocolRef`; (ii) gate Method steps with `requiresAutonomyBudget`; (iii) write a `AutonomyLedgerEntry` on every admitted Work; (iv) block on depletion until a `ResumeAutonomy` SpeechAct passes SoD; (v) surface autonomy fields in UTS rows.

**Builds on:** A.2 / A.2.1 / A.2.5 / A.15 / A.21; B.3; C.16; E.8; E.10; E.18; F.4; F.6; F.8; F.15; F.17.
**Coordinates with:** A.13 (Agential Role), C.9 (Agency‑CHR), C.24 (Agent‑Tools‑CAL) where applicable; G.4–G.5–G.8–G.9–G.10 (method authoring/selection/shipping).

### E.16:1 - Problem Frame

Autonomy‑claiming **performers** (*RoleAssignments* over services/robots/teams operating without continuous human direction) must **stay within declared limits** (safety, risk, resource, remit) and **yield** to governance when required. Without a uniform rule, “autonomy” drifts into tacit norms, cannot be benchmarked or audited, and undermines selection (Part G) and publication (Part F).

### E.16:2 - Problem

* **Opaque autonomy.** Patterns assert “autonomous” behavior with no **budget** or **enforcement**.
* **Un‑gated execution.** Methods can execute beyond authority or risk limits.
* **Ad‑hoc overrides.** No standard **SpeechAct** for pausing/de‑scoping; SoD is unclear.
* **Non‑portable publication.** **UTS (Unified Term Sheet)** rows cannot surface autonomy‑critical data for parity or selection.

### E.16:3 - Forces

| Force                          | Tension                                                                  |
| ------------------------------ | ------------------------------------------------------------------------ |
| **Creativity vs Safety**       | Exploration autonomy vs hard constraints and override duties             |
| **Locality vs Comparability**  | Context‑local rules vs cross‑context selection (G‑suite)                 |
| **Simplicity vs Auditability** | Lightweight authoring vs ledger‑grade evidence                           |
| **Autonomy vs SoD**            | Helpful self‑action vs separation‑of‑duties and human‑in‑the‑loop points |

#### E.16:3.1 - Bias-Annotation

**Lenses tested:** `Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`. **Scope:** Universal for any Role/Method/Service that claims autonomous operation (unsupervised decision or actuation) and is admitted via `AutonomyBudgetDecl` + Green‑Gate. It is **not** aimed at purely assistive “suggestion‑only” tools where each action is confirmed by a human at the point of execution.

* **Gov.** Bias toward enforceable oversight (hard gates, SoD, canonical override SpeechActs). Mitigation: exploration autonomy is still allowed, but only inside an explicit budget and time window.
* **Arch.** Bias toward gate‑and‑ledger structure (Green‑Gate + Work‑anchored `AutonomyLedger`). Mitigation: `telemetrySpecRef` can scope what is emitted when full deltas are unnecessary.
* **Onto/Epist.** Bias toward typed, testable constraints (MM‑CHR tokens, explicit admissibility checks). Mitigation: budgets are optional‑field (`?`) so low‑risk contexts can start minimal and tighten over time.
* **Prag.** Bias toward measurable quotas may under‑express “soft” autonomy goals. Mitigation: pair `decision_tokens` with `risk_bands` to capture non‑counting limits.
* **Did.** Bias toward explicit mechanics increases authoring surface area. Mitigation: provide a default `AutonomyBudgetDecl` template and minimal harness cases in **F.15**.

### E.16:4 - Solution — **Rule‑of‑Constraints (RoC) for Autonomy**

This RoC **applies whenever** a Role/Method/Service **claims autonomous operation** (any phrasing that implies unsupervised decision or actuation).

**E.16‑S1 (Autonomy Budget — mandatory).**
Any autonomy claim **MUST** publish an **AutonomyBudgetDecl** as a *named, versioned* object in the **same `U.BoundedContext`**:

```
AutonomyBudgetDecl {
  id, version
  scope: ClaimScope (G)                              // where this budget applies
  budget: {                                          // all typed via MM‑CHR (C.16)
    action_tokens?     : Unitful quota / rate
    decision_tokens?   : Unitful quota / rate
    risk_bands?        : CHR vector with acceptance bands
    resource_caps?     : set of unitful caps (Γ_work categories)
    time_window?       : Γ_time window & cadence
  }
  AdmissibilityConditionsId : PolicyIdRef                          // Aut-Guard policy naming gates & penalties
  overrideProtocolRef : Episteme                     // SpeechAct & SoD for pause/resume/escalate
  telemetrySpecRef? : Episteme                       // what to emit into AutonomyLedger
  editionPins : { RoleRef?, MethodDescRef?, CHR refs, …  }
}
```

**E.16‑S1.A (Scout / probe / commit partition for bounded specialization).**
When an autonomy-bearing method uses bounded specialization scouting, the budget declaration **MUST** keep scout budget, probe budget, and commit checkpoint as distinct control surfaces rather than collapsing them into one undifferentiated burn envelope. A successful probe does not by itself authorize a committed route, wider burn, or scope widening. Leaving probe state requires one explicit checkpoint decision through the declared guard or override path, with budget burn and residual budget recorded in the `AutonomyLedger`. `E.16` governs this budget partition plus guard and ledger enforcement; it does not replace the dyadic move of `A.15` or the `CheckpointReturn` plan semantics of `C.24`.
**E.16‑S2 (Guarded enactment — Green‑Gate).**
A **Method step** that *requires* autonomy **MUST** list `requires: [RoleX]` **and** `requiresAutonomyBudget: AutonomyBudgetDecl.id`. A **Work** instance is admissible *iff* at enactment time:

* the performer’s **RoleAssignment** is valid and in an **enactable** RSG state (A.2.5);
* the budget accounting for the **AutonomyBudgetDecl** indicates **tokens/limits remaining** for *this* budget in the declared **Γ_time** window (derived from the AutonomyLedger);
* all **guard checks** defined by `AdmissibilityConditionsId` evaluate to **pass** (e.g., risk ≤ band, resource ≤ cap).

Failing any gate **blocks** enactment (no “soft warnings” on Core surface).

**E.16‑S3 (Autonomy Ledger).**
All admissible Work **MUST** record **AutonomyLedger entries**:

```
AutonomyLedgerEntry {
  workId, performedBy: RoleAssignmentId
  budgetId, version, time
  deltas: { action_tokensΔ?, decision_tokensΔ?, riskΔ?, resourceΔ? }
  guardVerdicts: { name → pass|fail }
  pathIds: { PathId, PathSliceId }                  // for G‑suite parity/refresh
}
```

The ledger is **evidence**: attach to `U.Work` (A.15.1) and fold under **Γ_work** and **Γ_time** for reporting.

**E.16‑S4 (Overrides — SpeechActs & SoD).**
Every budget **MUST** reference an **OverrideProtocolRef** that defines canonical **SpeechActs**:

* **PauseAutonomy(budgetId)** — immediate stop of autonomy‑gated steps;
* **ResumeAutonomy(budgetId)** — resume after conditions;
* **NarrowAutonomy(budgetId, Δscope)** — apply stricter limits;
* **Escalate(budgetId)** — handover to a declared **SupervisorRole**.

**SoD:** The override caller **MUST NOT** be the same **RoleAssignment** that is consuming the budget (enforce `⊥` in the Context). All overrides are **Work** (SpeechActs) with **ledger entries** (zero or negative deltas as per policy).

**E.16‑S5 (Depletion behavior).**
When a budget **depletes** (no tokens / envelope exceeded / cap breached):

* **Block** further autonomy‑gated steps in the **same Γ_time window**;
* Emit **DepletionNotice** (SpeechAct), and either **Escalate** or **Park** per policy;
* Only a **ResumeAutonomy** SpeechAct from an admissible Role (per SoD) may reopen the gate.

**E.16‑S6 (Publication in UTS).**
UTS rows that describe a **Role**, **Method**, **Service**, or **Selector** with autonomy **MUST** include:

* `AutonomyBudgetDeclRef` (id & version);
* `Aut-Guard policy-id (PolicyIdRef)`;
* `OverrideProtocolRef`;
* declared **Scope (G)** and **Γ_time** window;
* edition pins for the referenced Role/Method/CHR.
* *(optional, if a scale preference is declared)* `ScaleLensPolicyRef` and `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`.

**E.16‑S7 (Scale & selection — optional lens).**
When autonomy interacts with open‑ended search (C.18 and C.19), **budget consumption** and **guard violations** are **selection lenses** in Part G (G.5/G.9). Applying a **Scale‑Lens / Bitter‑Lesson** preference is **OPTIONAL**. Authors **MAY** declare a **ScaleLensPolicy** for the autonomy claim; when declared, it **MUST** state:
* **Trigger criteria** — evidence that expected utility‑of‑scale is monotonic/non‑saturating on held‑out tasks, and a threshold at which scaling beats structured heuristics.
* **Budget fit** — compute/latency/cost targets **within** the declared `AutonomyBudgetDecl` (Γ_time, resource_caps).
* **Safety invariants** — guards and SoD remain **non‑weakened** under scaling; no policy may bypass E.16 gates.
* **Fallback** — a degrade‑gracefully plan if scaling fails to clear the trigger criteria within budget.
If no **ScaleLensPolicy** is declared, selection remains **neutral** with respect to Bitter‑Lesson; RoC does **not** authorize ignoring scale‑safety guards under any policy.

### E.16:5 - Archetypal grounding (Tell‑Show‑Show; human‑centric)

**Show‑A (U.System — mobile robot).**
`Robot_R7#NavigatorRole:Warehouse_2026` executes `Navigate_v3`.
`AutonomyBudgetDecl`: `action_tokens=10 k steps/day`, `risk_bands={maxSpeed ≤ 1.2 m/s, minDist ≥ 0.5 m}`, `resource_caps={battery ≥ 20%}`; `AdmissibilityConditionsId=Aut‑Guard‑R7‑v1`; override via `PAUSE`, `RESUME`, `ESCALATE` SpeechActs by `FloorSupervisorRole ⊥ NavigatorRole`. Ledger entries decrement `action_tokens`, track `minDist`. Depletion at 0 tokens halts autonomous moves and pages supervisor.

**Show‑B (U.PromiseContent — autonomous deploy).**
`DeployerRole` performs step “Promote to prod” under `AutonomyBudgetDecl` with `decision_tokens=3/day`, `risk_envelope={error‑budget burn ≤ 2% / day}`, guard “all pre‑deploy checks pass”. Overrides only by `CABChair#AuthorizerRole ⊥ DeployerRole`.

### E.16:6 - Conformance Checklist (SCR — E.16‑CC)

| ID            | Requirement                                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **E.16‑CC‑1** | Any autonomy claim **MUST** reference an **AutonomyBudgetDecl** in the same `U.BoundedContext`.                                                                             |
| **E.16‑CC‑2** | **Method steps** that depend on autonomy **MUST** declare `requiresAutonomyBudget: AutonomyBudgetDecl.id` (and `requires: [RoleX]`) and **MUST** be Green‑Gated by the budget’s guards at enactment. |
| **E.16‑CC‑3** | A **Work** admitted under autonomy **MUST** carry an **AutonomyLedgerEntry** with deltas and guard verdicts.                                                                |
| **E.16‑CC‑4** | **Overrides** are **SpeechActs** with SoD enforced (`⊥` between consumer and overrider roles); each override creates a ledger entry.                                        |
| **E.16‑CC‑5** | **Depletion** **MUST** block autonomy‑gated steps until a **ResumeAutonomy** SpeechAct passes SoD and guard checks.                                                         |
| **E.16‑CC‑6** | **UTS rows** for autonomy‑bearing Roles/Methods/Services **MUST** include `AutonomyBudgetDeclRef`, `Aut-Guard policy-id (PolicyIdRef)`, `OverrideProtocolRef`, `Scope (G)`, and `Γ_time`. |

| **E.16‑CC‑7** | When bounded specialization scouting is in scope, scout budget, probe budget, and commit checkpoint **MUST** stay explicit, and a successful probe **SHALL NOT** count as automatic committed rollout. |

### E.16:7 - Consequences

* **Testability.** Autonomy is measurable (tokens/envelopes), audit‑ready (ledger), and stoppable (SpeechActs).
* **Comparability.** UTS surfaces autonomy metadata for fair selection & parity.
* **Safety.** Guards are hard gates; depletion halts further autonomy‑gated Work.

#### E.16:7.1 - SoTA‑Echoing (post‑2015 practice alignment)

> Each item states **Adopt / Adapt / Reject**, and why. Vendor/tool tokens are kept as *informative*, not normative.

1. **Corrigibility & safe interruptibility (2016→).**
   **Adopt/Adapt.** Work on safe interruption and “off‑switch” incentives argues that capable systems should remain *stoppable* and should not be rewarded for resisting oversight (Orseau & Armstrong, 2016; Hadfield‑Menell et al., 2017). E.16 adapts this into canonical **PauseAutonomy / ResumeAutonomy** SpeechActs plus **SoD** and *hard* gating on depletion.

2. **AI safety as concrete operational hazards (2016→).**
   **Adopt.** “Concrete Problems in AI Safety” pushes instrumentation and testable safety constraints over informal assurances (Amodei et al., 2016). E.16 mirrors this by turning “autonomy” into a **budget + ledger + guards** specification that can be benchmarked and audited.

3. **SRE error budgets & “stop the line” operations (2016→).**
   **Adopt/Adapt.** Error‑budget practice treats reliability as a measurable envelope that gates risky change when depleted (Beyer et al., *Site Reliability Engineering*, 2016; Höller et al., *The Site Reliability Workbook*, 2018). E.16 adapts the idea into `risk_bands` and depletion behavior that blocks autonomy‑gated steps until governed resume.

4. **Risk management frameworks for AI systems (2023→).**
   **Adopt/Adapt.** Contemporary risk frameworks emphasize governance, continuous measurement, and traceable controls (NIST AI RMF 1.0, 2023; ISO/IEC 23894, 2023). E.16 adapts these into **UTS publication** + **Work‑anchored ledger evidence** for parity and audit.

5. **Policy‑as‑code and provenance gating (2019→).**
   **Adopt.** Modern supply‑chain integrity systems emphasize *policy‑checked actions with verifiable provenance* (in‑toto, 2019→; SLSA, 2021→). E.16 echoes the same principle for autonomy: **no autonomy‑gated enactment without passing declared guards and emitting ledger evidence** (without importing any specific tooling).

6. **Scaling laws & the Bitter Lesson (2019→).**
   **Adapt/Reject.** Empirical scaling work and the Bitter Lesson motivate considering compute‑heavy search when returns are monotonic (Sutton, 2019; Kaplan et al., 2020). E.16 adapts this into an **optional** ScaleLensPolicy (E.16‑S7) constrained by the *same* budgets and guards, and **rejects** any interpretation that lets “scale” bypass safety gates.

7. **Budgeted specialist acquisition and checkpointed exploitation (2024→).**
   **Adopt/Adapt.** Recent agentic tool-use, self-play, and open-ended search lines reinforce that the competition variable is time or budget to threshold plus fast exploitation after a viable route is found. E.16 adapts this into distinct scout/probe/commit control surfaces and rejects any reading where early probe success authorizes rollout without an explicit checkpoint.
#### E.16:7.2 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
| --- | --- | --- | --- |
| **Autonomy-by-label** | “Autonomous” is claimed but there is no `AutonomyBudgetDecl` or ledger | Autonomy becomes opaque; cannot be audited or compared | Require **E.16‑S1/S3**; reject publication without `AutonomyBudgetDeclRef` + version |
| **Soft gates** | Budget/guards only warn; enactment proceeds anyway | Violates Safety and SoD; makes budgets non-enforceable | Make Green‑Gate **blocking** on Core surface (**E.16‑S2**) |
| **Self‑override** | Same RoleAssignment consumes the budget and calls Resume/Narrow | Conflict of interest; SoD collapse | Enforce `⊥` between consumer and overrider (**E.16‑S4**) |
| **Budget bypass via “scale”** | Scaling preference relaxes guards or ignores caps | Undermines declared limits; breaks comparability | In ScaleLensPolicy, **guards/SoD must remain non‑weakened** (**E.16‑S7**) |
| **Untyped quotas** | Tokens/caps are recorded without units, or units are mixed | Ledger becomes non-comparable; audits become meaningless | Type budgets and deltas via **MM‑CHR (C.16)**; keep unitful rates/quotas |
| **Ledger-as-logging** | Logs exist but are not Work‑anchored (no workId/budgetId/version/pins) | Evidence is non-portable; cannot support parity/refresh | Require `AutonomyLedgerEntry` attached to `U.Work` with ids, versions, and edition pins |

### E.16:8 - Rationale & E‑/F‑/G‑links

* **E.8** — follows the pattern template (Context → Problem → Forces → Solution → Grounding → CC → Consequences).
* **E.10** — uses LEX‑BUNDLE: Scope via **ClaimScope (G)**, time via **Γ_time**, no “validity/process/actor/agent‑as‑noun” language; new lexical rule **L‑AUTO** added in edits below.
* **Mint/reuse authority (policy-ids).** Mint/reuse authority is expressed via **F.8:8.1** (`PolicyIdRef`: `PolicySpecRef` + `MintDecisionRef?`) and explicit **GateCrossing** checks (**E.18**) evaluated by the active **GateProfile/GateFit** (**A.21**); no tier ladder is required.
* **Part F** — integrates with **F.4** Role Description (RCS includes *AgencyLevel*; RSG gates), **F.6** Role Assignment & Enactment (Green‑Gate), **F.15** SCR/RSCR (harness includes depletion/override tests), **F.17** UTS (columns, incl. optional ScaleLens fields).
* **Part G** — **G.4/G.5**: method authors must declare budgets & guards; **G.9** parity includes autonomy consumption & violations; **G.10** shipping requires UTS autonomy fields.

### E.16:9 - Mini conformance checklist (cross‑E–F; author’s quick use)

1. **Declare** `AutonomyBudgetDecl` (scope, budgets, AdmissibilityConditionsId, overrides).
2. **Gate** steps with `requiresAutonomyBudget`.
3. **Emit** an `AutonomyLedgerEntry` for each admitted Work.
4. **Enforce SoD** on override SpeechActs; **block on depletion**.
5. **Publish** UTS autonomy fields for any autonomy‑bearing Role/Method/Service.

*(These five are sufficient for a working test harness in Part F.)*

### E.16:End

## E.17.0 - `U.MultiViewDescribing — Viewpoints, Views & Correspondences`

> **Tech‑name:** `U.MultiViewDescribing`
> **Plain‑name:** multi‑view describing (viewpoints, views, correspondence for families of descriptions/specifications)

**Status & placement.** Part E (Describing & Publication). Normative architectural pattern.
**Builds on:** C.2.1 `U.EpistemeSlotGraph` (DescribedEntity, Viewpoint, and View slots), A.6.2 `U.EffectFreeEpistemicMorphing`, A.6.3 `U.EpistemicViewing`, A.6.4 `U.EpistemicRetargeting`, A.7 (Strict Distinction; I/D/S versus publication-form and carrier lanes), E.10.D1 (Context), E.10.D2 (I/D/S discipline).
**Used by:** E.17 (MVPK — publication as a specialisation of multi‑view describing for morphisms), E.17.1 `U.ViewpointBundleLibrary`, E.17.2 `TEVB`, E.18:5.12 (E.TGA engineering viewpoint families), domain‑specific description schemes (architecture, safety cases, governance, research).

**Guard (lexical).**

**C.2.1 lane binding.** `U.MultiViewDescribing` does not mint a generic semio kind. When the family describes or views knowledge claims, the claim-bearing value is `U.Episteme`; when that episteme is made available as a published episteme, use `U.EpistemePublication` or governed `U.Episteme` publication. Publication forms, episteme-lane `U.View` values, MVPK faces, source-finding cues, and SCR and RSCR carriers remain separate lanes. If a family crosses into a later FPF pattern or a non-pattern `authoritySourceRef` target, name `governingPatternRef` or `authoritySourceRef` rather than a container label.


* `U.Viewpoint` is the ValueKind of `ViewpointSlot` and denotes **intensional viewpoint specs**, not `SurfaceKind` values or carriers.
* `U.View` is an alias of `U.EpistemeView`, i.e. an **episteme-lane view**, not a document or file. Views are epistemes; `PublicationSurface` and `InteropSurface` are L-SURF `SurfaceKind` values; concrete renderings and carriers remain A.7, SCR, and RSCR concerns.
* `ViewFamilyId` is a lexical tag for **families of viewpoints** (e.g. TEVB), never for view kinds, MVPK `U.View` values, `U.ViewFamily(-)` bundles, or `SurfaceKind` values. MVPK face kinds remain `{PlainView, TechCard, InteropCard, AssuranceLane}`.

### E.17.0:1 - Problem frame  *(informative)*

Complex systems (social‑technical, cyber‑physical, organisational) are routinely described from **many perspectives**:

* functional vs structural vs deployment vs behavioural views,
* safety vs performance vs cost vs governance views,
* formal specs vs operational runbooks vs regulatory dossiers.

Post‑2015 MBSE and architecture practice emphasise **viewpoints and views** (ISO 42010, SysML v2), and contemporary model‑based toolchains treat views as **queries or projections over shared models** rather than independent documents.

In FPF terms:

* the things we talk about — systems, methods, services, epistemes — are `U.Entity` or `U.Holon` values in `DescribedEntitySlot`;
* descriptions and specifications of those things are `U.Episteme` instances (`…Description` or `…Spec`) with a **DescriptionContext** = `⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`;
* episteme-lane views are `U.View` (`U.EpistemeView`) that slice ClaimGraphs under specific viewpoints and representation schemes.

What we lack without this pattern is a **universal way to organise families of descriptions/specifications under multiple viewpoints** — for any entity‑of‑interest, not only for architecture, and without collapsing “view” into “document” or “diagram”.

### E.17.0:2 - Problem  *(informative, but sharp)*

Without `U.MultiViewDescribing`:

1. **Viewpoints, views, `PublicationSurface` and `InteropSurface` kinds, and carrier renderings collapse.**
   In practice, “architecture view”, “diagram”, “spec”, and “published deck” are used interchangeably. This:

   * confuses *episteme* (`U.View`) with `PublicationSurface` or `InteropSurface` kind or with a concrete carrier rendering,
   * hides which **concerns and stakeholders** a description is written for,
   * makes it impossible to check whether a given description family is “complete enough” for a chosen viewpoint library.

2. **Descriptions float without viewpoints.**
   Legacy I/D/S discipline distinguishes Intension vs Description vs Spec, but does not, on its own, forbid “view‑from‑nowhere” descriptions (no declared viewpoint). That contradicts the pragmatic stance encoded in C.2.1: **no episteme without concerns**.

3. **Each domain reinvents multi‑view semantics.**
   Architecture, safety cases, governance frameworks, and research engineering processes all use local notions of “view”, “viewpoint”, and “consistency between views”. Without a shared pattern:

   * E.TGA, MVPK, and discipline packs introduce their own “view” rules and invariants, duplicating work;
   * cross‑domain reasoning (e.g. mapping a safety view to an architecture view) becomes ad‑hoc;
   * we cannot give a single formal story for consistency, correspondence, and EpistemicViewing across families of descriptions.

4. **No place to attach correspondence.**
   ISO 42010‑style *correspondences* and modern BX/consistency relations have nowhere canonical to live. We need a **CorrespondenceModel over families of D/S epistemes** that integrates with `U.EpistemicViewing`, `U.EpistemicRetargeting`, and C.2.1’s slot graph.

### E.17.0:3 - Forces  *(informative)*

| Force                                  | Tension                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**      | One pattern should handle engineering, safety, governance, research, etc. ↔ domain communities expect their own jargon (architecture description, safety case, dossier…).              |
| **Viewpoint locality vs reuse**        | Viewpoints must be local to families of descriptions (`EoIClass`, Context) ↔ we want reusable **viewpoint bundles** (libraries) across projects and domains.                           |
| **I/D/S strictness vs pragmatics**     | Intension ≠ Episteme; D/S are epistemes with DescriptionContext ↔ engineers think in “views over a system”, not in pure I/D/S algebra.                                                 |
| **Slot discipline vs approachability** | C.2.1 and A.6.5 give a clean SlotKind, ValueKind, and RefKind discipline ↔ authors want to talk about “functional view” and “safety view” without carrying all slot jargon in didactic support content. |
| **Epistemic versus publication-form and carrier lanes** | Views (epistemes) must be clearly separated from `PublicationSurface` and `InteropSurface` kinds and carriers ↔ authors often conflate “viewpoint”, “view”, and “document”.                                         |
| **Consistency vs incremental change**  | We want tight correspondence between views ↔ views evolve asynchronously; partial inconsistency must be representable and repairable (BX‑style).                                      |

### E.17.0:4 - Solution — `U.MultiViewDescribing` as the universal multi‑view scaffold  *(normative core)*

#### E.17.0:4.1 - Overview

`U.MultiViewDescribing` organises **families of descriptions/specifications** for a shared entity‑of‑interest into a multi‑view structure with:

* **explicit viewpoints** (`U.Viewpoint`) as intensional specs of stakeholders, concerns, allowed D/S kinds, and conformance rules;
* **episteme-lane views** (`U.View = U.EpistemeView`) as view-epistemes over those descriptions/specs;
* a **CorrespondenceModel** capturing correspondences between D/S and their views across viewpoints.

The pattern's described-entity class is explicit:

> **Described-entity class:** `EoIClass ⊑ U.Entity` — the class of entities-of-interest
> (typical species: `U.Holon` for engineering holons, `U.Morphism` for morphism publication, `U.Episteme` for meta-describing epistemes).

All members of a `U.MultiViewDescribing` family for that described-entity class share:


* `DescribedEntitySlot` value in that `EoIClass`, and
* a `BoundedContextRef` (E.10.D1) forming a **DescriptionScope** together with the entity.

Informally:

* Fix an entity `T ∈ EoIClass` and a bounded context `C`.
* The **multi‑view family** for `<T,C>` consists of a set of `…Description` / `…Spec` epistemes, each under a declared viewpoint, plus their `U.View` views, together with a correspondence model relating them.

#### E.17.0:4.2 - Core constructs

##### E.17.0:4.2.1 - `EoIClass` and DescriptionScope

1. **EoIClass.**
   A `U.MultiViewDescribing` instance declares an `EoIClass ⊑ U.Entity` that acts as a **species constraint** on the ValueKind of `DescribedEntitySlot`.

   * In engineering species (TEVB) this is typically `U.Holon` restricted to `U.System` or `U.Episteme`.
   * In MVPK, `EoIClass = U.Morphism`.

2. **DescriptionScope (informal).**
   For a fixed `T ∈ EoIClass` and `C : U.BoundedContext`, the **DescriptionScope** `Scope(T,C)` is the notional scope under which:

   * all descriptions/specifications have `DescribedEntityRef = T` and `BoundedContextRef = C` in their DescriptionContext;
   * all views (`U.View`) attached to this family preserve that `DescribedEntityRef` and `BoundedContextRef` (for D/S views).

   Formal USM treatment of `U.DescriptionScope` is fixed in E.10/L‑SURF; here we only rely on the intuition “**we are describing this thing, in this context**”.

##### E.17.0:4.2.2 - `U.Viewpoint` (intensional viewpoint spec)

`U.Viewpoint` is already introduced in C.2.1 as the ValueKind of `ViewpointSlot`; E.17.0 fixes its **internal structure** for describing families.

**Definition (normative, intensional).**
A `U.Viewpoint` is an intensional specification:

* `EoIClassSpec ⊑ U.Entity` — the class of entities this viewpoint is defined for (must be compatible with the family’s `EoIClass`);
* `StakeholderFamilies : FinSet(U.RoleEnactor)` — stakeholder / RoleEnactor families the viewpoint speaks for (e.g. “safety engineers”, “operations teams”).
* `Concerns : FinSet(U.Concern)` — concern set (qualities, risks, requirements) that matter under this viewpoint.
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindId)` — which D/S episteme kinds are admissible as **primary descriptions** and as **derived views** under this viewpoint (e.g. system-behaviour description, test harness spec, safety case, CG-Spec slice).
* `ConformanceRules` — a structured bundle of rules/tests describing when a D/S episteme or view **conforms** to the viewpoint, including:

  * minimal content requirements (e.g. “must cover all safety‑critical functions”),
  * admissible `U.EpistemicViewing` pipelines to derive views from base descriptions,
  * allowed degrees of incompleteness and evidence requirements (link to GateProfiles/`OperationalGate(profile)` checks and Part F harnesses).

**Slot alignment.**

* `ViewpointSlot` has ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`; episteme fields are named `viewpointRef : U.ViewpointRef?`.
* For D/S epistemes in a `U.MultiViewDescribing` family, `viewpointRef` is **mandatory** as part of `DescriptionContext`.

##### E.17.0:4.2.3 - `U.View` (episteme-lane views)

`U.View` is an alias for `U.EpistemeView`, a species of `U.Episteme` whose kind includes:

* `ClaimGraphSlot` (often a sliced or projected ClaimGraph),
* `DescribedEntitySlot`,
* `ViewpointSlot`,
* `ReferenceSchemeSlot` (and usually a `RepresentationSchemeSlot` in C.2.1+).

Normatively:

* A `U.View` in `U.MultiViewDescribing` is obtained via a `U.EpistemicViewing` morphism from some base D/S episteme in the family (see 4.3). It **shares the same `describedEntityRef`** and usually the same `BoundedContextRef`.
* `ViewSlot` is reserved for **references to such views** in meta‑structures (e.g. correspondence models, MVPK view families), never for carriers.

##### E.17.0:4.2.4 - `U.CorrespondenceModel` (view–view correspondence)

`U.CorrespondenceModel` is an episteme (typically a `U.EpistemeCard`) whose ClaimGraph expresses **correspondence relations between D/S epistemes and/or views** within a DescriptionScope:

* cross‑viewpoint correspondences (e.g. “this safety requirement is realised by this design element”),
* structural/behavioural consistency conditions (BX‑style consistency relations),
* change‑impact links (which views must be revisited when some view changes).

`CorrespondenceModel` is **used, but not defined, by A.6.3**: species of `U.CorrespondenceEpistemicViewing` reference it when computing views that depend on multiple epistemes or representation regimes.

#### E.17.0:4.3 - Multi‑view families and their rules/invariants (MVD‑0…MVD‑7)  *(normative)*

We now fix the rules and invariants that any `U.MultiViewDescribing[EoIClass]` instance must satisfy.

##### E.17.0:4.3.0 - MVD‑0 - Family objects

For a fixed `EoIClass` and bounded context `C`, a **multi‑view family** for an entity `T ∈ EoIClass` consists of:

* a (finite) set `D_S(T,C)` of D/S epistemes such that for each `E ∈ D_S(T,C)`:

  * `E : U.Episteme` of some kind in `AllowedEpistemeKinds` of its viewpoint,
  * `subjectRef(E)` decodes to `DescriptionContext(E) = ⟨DescribedEntityRef = T, BoundedContextRef = C, ViewpointRef(E)⟩`,
  * `viewpointRef(E)` lies in the family’s viewpoint set `Σ ⊆ FinSet(U.Viewpoint)`;
* a set `Views(T,C) ⊆ U.View` of view‑epistemes over those D/S epistemes, obtained by declared `U.EpistemicViewing` species (see MVD‑3);
* zero or more `U.CorrespondenceModel` epistemes over `{D_S(T,C), Views(T,C)}`.

Families are **scoped**: the same entity in a different `U.BoundedContext` belongs to a different family.

##### E.17.0:4.3.1 - MVD‑1 - Viewpoint locality and totality for D/S

For any multi‑view family:

1. **Viewpoint‑totality for D/S.**
   Each D/S episteme in `D_S(T,C)` **MUST** have a `viewpointRef` either:

   * explicitly populated, or
   * deterministically derived from a `U.ViewpointBundle` the family declares (see E.17.1).

   There are no “viewpoint‑free” D/S epistemes inside a `U.MultiViewDescribing` family.

2. **Viewpoint locality.**
   `ViewpointRef` values for `D_S(T,C)` must belong to a **finite viewpoint set `Σ`** declared for the family (locally or via a bundle). Cross‑family reuse happens **via bundles and Bridges**, not by silently sharing viewpoints across unrelated scopes.

3. **DescriptionContext alignment.**
   `DescriptionContext(E)` for any D/S episteme in the family must use the **same `DescribedEntityRef` and `BoundedContextRef`** as the family; any change of described entity or context is **outside this family** and must be expressed via `U.EpistemicRetargeting` and/or Context Bridges.

#### E.17.0:4.3.2 - MVD‑2 - Views are EpistemicViewing results

For any `V ∈ Views(T,C)`:

1. There exists a base episteme `E ∈ D_S(T,C)` and a morphism `v : E → V` such that:

   * `v` is a species of `U.EpistemicViewing`, i.e. an **effect‑free, describedEntity‑preserving** episteme morphism;
   * `describedEntityRef(V) = describedEntityRef(E) = T`,
   * `BoundedContextRef(V) = BoundedContextRef(E) = C`,
   * `viewpointRef(V)` is either:

     * the same as `viewpointRef(E)` (internal normalisation), or
     * a viewpoint in the same family `Σ`, with the change recorded in the family’s `CorrespondenceModel` (see MVD‑4).

2. No view may be introduced “out of thin air”: every `U.View` in the family is traceable to at least one D/S episteme (or a finite diagram thereof) via a **documented EpistemicViewing pipeline**.

3. Views **do not introduce new intensional commitments** about `T` beyond what is licensed by EFEM & EpistemicViewing invariants (no new atomic claims about the same described entity). Strengthening Intension requires new D/S under A.7/E.10.D2, not a view.

#### E.17.0:4.3.3 - MVD‑3 - Applicability profiles for viewings

Any EpistemicViewing species used inside `U.MultiViewDescribing` **MUST**:

* declare an Applicability profile as per EV‑6: permitted `EoIClass`, grounding, viewpoint ranges, and representation schemes;
* for D/S epistemes in a family:

  * **preserve** `DescribedEntityRef` and `BoundedContextRef` of `DescriptionContext`,
  * either preserve `ViewpointRef` or change it **within the family’s viewpoint bundle**, with constraints recorded in `CorrespondenceModel`,
  * never widen ClaimScope beyond EFEM/EpistemicViewing allowances.

Any change of described entity (even “small”, e.g. subsystem→system) must be expressed via `U.EpistemicRetargeting` and is **not** a MultiViewDescribing view refinement.

#### E.17.0:4.3.4 - MVD‑4 - CorrespondenceModel for cross‑view correspondences

When views or D/S epistemes under different viewpoints are meant to be **kept in correspondence** (in ISO 42010 or BX sense), the family **SHALL**:

1. Provide a `U.CorrespondenceModel` episteme whose `ClaimGraph` captures correspondences and consistency relations over `{D_S(T,C), Views(T,C)}`.

2. Ensure that any `U.CorrespondenceEpistemicViewing` that depends on multiple epistemes or representation schemes:

   * references that `CorrespondenceModel`, and
   * publishes witnesses (proof objects, trace links) that make diagrams commute up to declared isomorphism (oplax naturality allowed).

3. Treat temporary inconsistency explicitly: there may be states where some correspondences are violated; this is represented as **facts in the correspondence ClaimGraph**, not as hidden weakening of viewing invariants.

#### E.17.0:4.3.5 - MVD‑5 - Separation from publication (MVPK)

`U.MultiViewDescribing` is purely **epistemic**:

* D/S epistemes and views live entirely in Ep‑space (`U.Episteme`);
* it does **not** define `PublicationSurface`/`InteropSurface` kind, carriers, or rendering;
* MVPK (E.17) sits **on top**:

  * taking morphisms and/or D/S epistemes as input,
  * using `U.EpistemicViewing` plus publication‑specific viewpoints,
  * emitting `U.View` instances declared against `PublicationSurface`/`InteropSurface` kind via L‑SURF.

MultiViewDescribing therefore **does not re‑define I→D/D→S** (`Describe_ID`, `Specify_DS`) and does not introduce any `U.Work` on carriers; those remain in A.7/E.10.D2 and E.17.

Explanation-facing renderings over the same source `U.Episteme` claims may later be classified by `ExplanationFaithfulnessProfile` on top of existing publication faces, but that profile does not create a second viewpoint calculus here. `U.MultiViewDescribing` continues to govern the epistemic distinction between viewpoints, views, and correspondences.


#### E.17.0:4.3.6 - MVD‑6 - I/D/S alignment

For any `U.MultiViewDescribing` instance:

1. Every `…Description` and `…Spec` episteme in the family must satisfy E.10.D2:

   * be an episteme with `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
   * be linked to a unique Intension via `isDescriptionOf` / `isSpecOf` with the additional `ViewpointRef` parameter.

2. Viewings and correspondence operations **must not**:

   * collapse Intension into episteme,
   * confuse D/S with `PublicationSurface`/`InteropSurface` kind or carrier rendering,
   * reinterpret described entity without going through A.6.4 retargeting.

#### E.17.0:4.3.7 - MVD‑7 - Slot discipline

All constructs in this pattern **SHALL** respect `U.RelationSlotDiscipline`:

* SlotKinds (`DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot`) and their ValueKinds/RefKinds follow A.6.5 and C.2.1.
* `*Slot` suffix is reserved for SlotKinds; `*Ref` for RefKinds/fields, never for Kinds or objects.
* MultiViewDescribing patterns **must not** invent parallel slot disciplines for “roles in relations”; they reuse SlotKind as the notion of position.

### E.17.0:5 - Archetypal grounding  *(informative)*

1. **Engineering holon (TEVB).**
   * `EoIClass = U.Holon` (restricted to `U.System`/`U.Episteme`).
   * TEVB (E.17.2) supplies a viewpoint bundle with canonical engineering viewpoints: Functional, Structural, Role‑Enactor, Module‑Interface, etc.
   * For a particular system `S` in context `C`, D/S epistemes include functional descriptions, structural designs, role‑enactment models, and interface specs.
   * Views derived via EpistemicViewing include sliced safety views, performance‑focused views, and minimal runbooks.
   * `CorrespondenceModel` records how functional elements are realised structurally, where hazards map to components, etc.

2. **Morphism publication (MVPK).**
   * `EoIClass = U.Morphism`.
   * D/S epistemes capture the semantic characterisation of morphisms (pre‑/post‑conditions, CG‑Specs, CHR pins).
   * Viewpoints are publication‑oriented (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`); views are MVPK faces over those morphisms.
   * CorrespondenceModel states how the same morphism appears as a simple narrative, a typed card with units, an interoperability card, and an assurance lane with evidence bindings — all without new claims.

3. **Safety case vs architecture vs operations.**
   * `EoIClass = U.Holon`.
   * Viewpoints: SafetyCase, Architecture, Operations.
   * Families tie together safety requirements, architectural structures, and operational procedures for the same plant `P` in context `C`.
   * Views: a safety‑focused slice of the architecture description, an operational runbook annotated with safety invariants, etc.
   * CorrespondenceModel expresses coverage and consistency between these views, enabling BX‑style repair when one side changes.

### E.17.0:6 - Conformance checklist (author’s quick use)  *(normative)*

When defining a new `U.MultiViewDescribing` species or using it in a discipline pack:

1. **Declare the EoIClass.**
   *Explicitly state `EoIClass ⊑ U.Entity` and ensure all families restrict `DescribedEntitySlot` accordingly.*

2. **Define the viewpoint set Σ.**
   *List `U.Viewpoint` instances (possibly via a `U.ViewpointBundle`) with stakeholders, concerns, allowed EpistemeKinds, and conformance rules.*

3. **Require DescriptionContext for D/S.**
   *Ensure every `…Description`/`…Spec` episteme in the family has `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` and that `ViewpointRef ∈ Σ`.*

4. **Specify admissible EpistemicViewing species.**
   *List the `U.EpistemicViewing` profiles used to derive views; declare their Applicability profiles and assert they are describedEntity‑preserving (EV‑6).*

5. **Attach CorrespondenceModel where needed.**
   *Whenever cross‑view consistency matters, introduce a `U.CorrespondenceModel` episteme and reference it from any `U.CorrespondenceEpistemicViewing`.*

6. **Separate describing from publication.**
   *Check that pattern text does not treat I→D/D→S as “publication”, and that any talk of `PublicationSurface`/`InteropSurface` kind or carriers is clearly delegated to MVPK/L‑SURF.*

7. **Respect SlotKind/ValueKind/RefKind discipline.**
   *Use `*Slot` only for SlotKinds, `*Ref` only for RefKinds/fields; avoid `Subject`/`Object` roots in episteme types; use `DescribedEntitySlot` and `viewpointRef` instead.*

### E.17.0:7 - Consequences  *(informative)*

* **Unified multi‑view story across domains.**
  Engineering descriptions, safety cases, governance dossiers, research epistemes/publications — all become instances of the same multi‑view pattern, enabling coherent tooling and education.

* **Explicit, testable viewpoints.**
  Viewpoints move from vague labels (“architecture view”) to first‑class objects (`U.Viewpoint`) with stakeholder families, concerns, allowed D/S kinds, and conformance rules. This allows `OperationalGate(profile)` checks and better review practices.

* **Views as disciplined projections, not new documents.**
  `U.View` is an episteme generated by viewings, not a free‑floating PowerPoint. This constrains what tools are allowed to do when “generating views”, and prevents silent strengthening of commitments.

* **Correspondence as a first‑class citizen.**
  Consistency and traceability between views are expressed via ClaimGraphs in `U.CorrespondenceModel`, not as scattered hyperlinks or spreadsheet columns.

* **Clean separation of describing vs publishing.**
  `U.MultiViewDescribing` ends the long‑standing conflation between describing (I→D→S) and publication (D/S→`PublicationSurface`/`InteropSurface` kind plus carrier rendering). MVPK becomes a clean specialisation on top, not a second I/D/S discipline.

* **Slot-specific interoperability.**
  C.2.1/A.6.5 slot discipline applies uniformly; new domains can introduce viewpoint bundles and multi‑view families without inventing new ontologies for “view positions” or “roles in relations”.

### E.17.0:8 - Rationale & SoTA‑echoing  *(informative)*

* **ISO 42010 and viewpoint libraries.**
  ISO 42010 distinguished *viewpoints* (stakeholders + concerns + conventions) from *views* (descriptions under those viewpoints) and introduced viewpoint libraries. `U.MultiViewDescribing` generalises this beyond “architecture descriptions” to **any descriptions/specifications**, with `EoIClass` parameter and explicit viewpoint bundles used by TEVB and MVPK.

* **MBSE & SysML v2 views‑as‑queries.**
  Modern MBSE treats views as **queries over shared models** with controlled rendering. That aligns with `U.EpistemicViewing` as a pure, describedEntity‑preserving morphism, and with `U.View` as an episteme view derived from D/S under a viewpoint.

* **BX / model synchronisation.**
  Bidirectional transformations literature treats consistency relations and repair as first‑class. `U.CorrespondenceModel` and `U.CorrespondenceEpistemicViewing` provide FPF-native correspondence objects for such relations, ensuring that consistency rules live in ClaimGraphs and respect episteme morphism invariants, rather than being buried in tool code.

* **Optics and displayed categories.**
  With C.2.1 and A.6.3, epistemes form a category fibred over described entities; viewings act like optics over the episteme slot graph. `U.MultiViewDescribing` is the **displayed‑category‑like** organisation of families indexed by `DescribedEntitySlot` and `ViewpointSlot`, making later categorical reasoning (e.g. structured cospans for view composition) straightforward.

* **Hybrid symbolic/latent representations.**
  By treating `U.RepresentationScheme` and `U.RepresentationOperation` as episteme components, families can mix symbolic specs, diagrams, code, and latent representations (e.g. LLM‑based summaries) while staying within the same multi‑view discipline and EpistemicViewing invariants.

### E.17.0:9 - Relations  *(informative summary)*

* **Builds on C.2.1 `U.EpistemeSlotGraph`.**
  Uses `DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot` as the structural backbone for descriptions, views, and correspondence.

* **Builds on A.6.2–A.6.4.**
  Families rely on `U.EffectFreeEpistemicMorphing` for view‑producing morphisms, `U.EpistemicViewing` for describedEntity‑preserving views, and `U.EpistemicRetargeting` for moves that change the described entity (outside a given family).

* **Constrains E.17 (MVPK).**
  MVPK is a **publication‑specialised MultiViewDescribing for morphisms**: its viewpoints are publication viewpoints; its ViewFamily is a special case of `Views(T,C)` with `T` a morphism; its rules/invariants must respect MVD‑0…MVD‑7.

* **Constrains E.17.1 / E.17.2.**
  `U.ViewpointBundleLibrary` and TEVB provide concrete viewpoint bundles populating `Σ` for particular `EoIClass` (e.g. engineering holons), but they must treat viewpoints as `U.Viewpoint` values in `ViewpointSlot`, not as ad‑hoc tags.

* **Coordinates with E.10.D2 (I/D/S) and E.10 LEX‑BUNDLE.**
  Ensures every D/S episteme in a family has a DescriptionContext, keeps “Describe/Specify” distinct from “Publish”, and respects lexical guards around `View`, `Viewpoint`, `SurfaceKind`, `ViewFamilyId`, `*Slot`, `*Ref`.

* **Coordinates with B.5.* / F‑cluster.**
  Viewpoints’ stakeholder families and concerns link naturally with RoleEnactment (B.5.\*) and Part F role descriptions, assignments, harnesses — without overloading `U.Role` as a coordinate in I/D/S or episteme slots.

### E.17.0:End

## E.17.1 - `U.ViewpointBundleLibrary` - Reusable Viewpoint Bundles

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Viewpoint bundle library.

**Builds on.**
`A.6.2-A.6.4` (episteme morphism classes), `A.6.5 U.RelationSlotDiscipline`, `A.7`, `E.7`, `E.10`, `E.10.D1`, `E.10.D2`, `E.17.0 U.MultiViewDescribing`.

**Used by.**
`E.17.2` (TEVB engineering viewpoint bundles), `E.18:5.12`, and domain-specific viewpoint families for architecture, governance, safety, research, or assurance.

### E.17.1:1 - Problem frame

`U.MultiViewDescribing` lets a description family state that one entity-of-interest is rendered through several viewpoints with declared correspondences. In practice many such viewpoint families recur across projects and schools: engineering teams reuse functional / procedural / structural / interface viewpoints; governance teams reuse risk / control / compliance / operations viewpoints; research teams reuse theory / experiment / inference / limitation viewpoints.

FPF therefore needs one explicit governing pattern for reusable viewpoint families so that authors can import them, name them stably, review them once, and keep intensional viewpoint identity separate from document labels and publication surfaces.

### E.17.1:2 - Problem

Without a viewpoint-bundle library pattern:

1. **Each domain invents local viewpoint families.**
   Similar families reappear under slightly different labels, but no stable catalogue object records whether the underlying viewpoints are actually the same.
2. **Viewpoint identity drifts.**
   A family called `functional`, `capability`, or `operational` may differ only lexically, or may differ semantically, but there is no disciplined place to tell which is which.
3. **`U.MultiViewDescribing` cannot reuse a family cleanly.**
   Every instance must restate its finite viewpoint family locally instead of importing an existing bundle.
4. **ISO 42010-style viewpoint libraries remain external.**
   FPF lacks a native place where reusable viewpoint libraries can be expressed as first-class, reviewable objects.
5. **Reader-facing labels leak into semantics.**
   Authors reuse the same name for viewpoints, views, publication faces, or folders, and the intensional object boundary becomes unclear.

### E.17.1:3 - Forces

| Force | Tension |
|---|---|
| **Reuse vs local fit** | Authors want reusable viewpoint families, but a local project may still need a subset or a context-specific extension. |
| **Stable identity vs evolution** | Bundles must stay stable enough for long-term reuse while still admitting editioned change. |
| **Intensional clarity vs label convenience** | Viewpoint bundles are intensional catalogue objects, yet teams often prefer one reader-facing label across `U.Viewpoint`, `U.View`, publication-face, and folder objects. |
| **Engineering vs publication discipline** | Engineering viewpoints and publication viewpoints both matter, but they must not collapse into one id namespace. |
| **Rich libraries vs cognitive economy** | A library should be rich enough for real reuse without becoming so large that authors cannot choose from it coherently. |

### E.17.1:4 - Solution - `U.ViewpointBundleLibrary`

`E.17.1` introduces `U.ViewpointBundleLibrary` as the reusable catalogue object for reusable viewpoint families. The library is a catalogue object: it packages named bundles of `U.Viewpoint` values and related metadata, but it does not define new kernel episteme kinds, new surfaces, or new publication carriers.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** via `ViewFamilyId`;
- **which `U.Viewpoint` values belong to that family;**
- **under what entity-of-interest class and edition discipline** the family is valid.

This lets `U.MultiViewDescribing` import a finite viewpoint family from a stable catalogue object instead of restating it ad hoc in every local description family.

#### E.17.1:4.2 - `U.ViewpointBundleLibrary` (library object)

A `U.ViewpointBundleLibrary` is a catalogue of viewpoint bundles with at least:

- `libraryId : LibraryId`
- `editionId : EditionId`
- `bundles : FinSet(U.ViewpointBundle)`
- optional governance metadata such as responsibility role assignment, change-control note, or scope tags

Normative constraints:

1. Within one library edition, each `ViewFamilyId` **SHALL** be unique.
2. Libraries **SHALL NOT** define new kernel episteme kinds or surface kinds.
3. Libraries **MAY** be specialized as core FPF libraries or organization-local extensions that preserve the same bundle discipline.

#### E.17.1:4.3 - `U.ViewpointBundle` and `ViewFamilyId`

A `U.ViewpointBundle` is a finite, non-empty family of compatible `U.Viewpoint` values packaged for reuse.

Minimal structure:

- `viewFamilyId : ViewFamilyId`
- `EoIClassSpec <: U.Entity`
- `viewpoints : FinSet(U.Viewpoint)`
- optional `ArchetypalCards : FinSet(U.ArchetypalGroundingRef)`
- optional `AlignmentNotes` for ISO 42010 or domain-standard correspondences
- optional typed annex references for lexical, bridge, routing, example, or SoTA support material

`ViewFamilyId` names the bundle. It does **not** name a `U.View`, a publication face, or a file-system surface.

#### E.17.1:4.4 - Import discipline into `U.MultiViewDescribing`

When a `U.MultiViewDescribing[EoIClass]` family declares a `ViewFamilyId`:

- its finite viewpoint family `Sigma` **SHALL** be a subset of the referenced bundle's `viewpoints`;
- every D/S episteme in the family **SHALL** use `viewpointRef` values drawn from that imported family;
- every associated `U.View` **SHALL** preserve viewpoint attribution rather than silently retyping or relabeling the imported viewpoints.

If more than one bundle is used, the family shall make the partition explicit rather than relying on unnamed mixture.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- `ViewFamilyId` is a lexical family id, not a surface kind.
- Engineering viewpoint ids and publication viewpoint ids may coexist, but they **SHALL** remain disambiguated.
- Bundle semantics come from the owned `U.Viewpoint` definitions, not from the spelling pattern of the family id.

### E.17.1:5 - Archetypal Grounding

**Tell.** A viewpoint bundle library lets FPF say "use this already-defined viewpoint family" without confusing that family with the concrete views or publication faces that later realize it.

**Show (System).** A TEVB engineering bundle can define a reusable family such as `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, and `VP.ModuleInterface` for holon descriptions. Later `U.MultiViewDescribing` families import that bundle rather than redefining the same engineering viewpoints each time.

**Show (Episteme).** A governance-oriented bundle can package `VP.Risk`, `VP.Control`, `VP.Compliance`, and `VP.Operations` as one reusable family for service or program descriptions. Publication surfaces may later expose that family, but the bundle itself remains an intensional catalogue object, not the report surface.

### E.17.1:6 - Bias-Annotation

The pattern biases FPF toward bundle-first reuse and against ad hoc local re-invention of recurring viewpoint families. That bias is intentional. The small cost of maintaining libraries and editions is lower than the long-term cost of unstable viewpoint identity.

### E.17.1:7 - Conformance Checklist

- `CC-VBL-0` Within one library edition, each `ViewFamilyId` **SHALL** identify exactly one `U.ViewpointBundle`.
- `CC-VBL-1` Every viewpoint in a bundle **SHALL** have `EoIClassSpec` compatible with the bundle's declared `EoIClassSpec`.
- `CC-VBL-2` A `U.MultiViewDescribing` family that declares a `ViewFamilyId` **SHALL** import only viewpoints from the referenced bundle.
- `CC-VBL-3` `ViewFamilyId` **MUST NOT** be used as a `SurfaceKind`, publication-face kind, or carrier kind.
- `CC-VBL-4` Bundles intended for non-expert reuse **SHOULD** provide archetypal grounding coverage for their viewpoints.
- `CC-VBL-5` Changes to bundle membership or meaning **SHALL** be editioned rather than silently mutating an existing family id.
- `CC-VBL-6` If a family combines several bundles, the contributing `ViewFamilyId` values **SHALL** remain explicit.

### E.17.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Surface hijack** | A `ViewFamilyId` is reused as a publication-face name or document type. | `CC-VBL-3` keeps family ids lexical and bundle-local. |
| **Bundle equals view collection** | A folder or report pack is called a viewpoint bundle even though no `U.Viewpoint` family is declared. | `E.17.1` defines the bundle as an intensional family of viewpoints, not a file grouping. |
| **Silent local drift** | A local project keeps the old family id but swaps in different viewpoints. | `CC-VBL-5` requires editioning for semantic or membership change. |
| **Namespace collapse** | Engineering viewpoint ids and publication viewpoint ids are mixed as if they were one namespace. | The solution keeps id spaces distinct and requires explicit attribution. |

### E.17.1:9 - Consequences

| Benefit | Trade-off / Mitigation |
|---|---|
| **Reusable viewpoint families.** Stable bundle ids let many projects reuse the same family without restating it. | Libraries need governance and edition discipline. |
| **Cleaner `U.MultiViewDescribing`.** A family can import a reviewed bundle instead of spelling out every viewpoint locally. | Local exceptions must be made explicit rather than hidden in prose. |
| **Better architectural alignment.** ISO 42010-style viewpoint-library practice gains a native FPF catalogue object. | Initial bundle authoring requires care in naming and grounding. |
| **Lexical hygiene.** Bundle ids, viewpoint ids, views, and publication surfaces stop collapsing into one label. | Authors must learn the separation once and then keep it. |

### E.17.1:10 - Rationale

`U.MultiViewDescribing` already assumes that viewpoint plurality exists. `E.17.1` supplies the governing pattern for that plurality, including cases where viewpoints are used to re-express positions in `U.LanguageStateSpace` or trajectories in `U.LanguageStateTransductionTrajectory`. Without it, every domain can only improvise locally, and long-term correspondence between viewpoint families remains fragile.

### E.17.1:11 - SoTA-Echoing

The pattern aligns with post-2015 multi-view practice: ISO 42010 viewpoint libraries, model-based systems engineering viewpoint catalogues, assurance-oriented viewpoint families, and reusable concern bundles in architecture and governance work. FPF adopts the reusable-library idea, but keeps the ontology stricter by separating bundle ids, viewpoint ids, views, and publication surfaces.

### E.17.1:12 - Relations
- **Builds on:** `C.2.1` slot discipline through `ViewpointSlot` / `ViewSlot`, `A.6.2-A.6.4`, `A.7`, `E.7`, and `E.10`.
- **Constrains:** `E.17.0 U.MultiViewDescribing` whenever it imports viewpoint families from reusable bundles.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `E.17`, `E.17.2`, `E.18:5.12`, `F.9`, `F.9.1`, and any domain-specific viewpoint family that needs stable reuse.
- **Protects:** lexical and ontological separation between viewpoint families, concrete views, and publication surfaces.
#### E.17.1:12.1 - Typed annex manifests for thin bundles

`VF.*` and other reusable viewpoint bundles may reference typed `AnnexManifestRef` assets with roles such as `lexical`, `bridge`, `routing`, `examples`, optional `sota`, and optional `pilotTrace`. This keeps the bundle itself thin while allowing routing notes, lexical baggage, and bridge annexes to remain explicit and typed rather than folded into the bundle core.


### E.17.1:13 - Bundle Anatomy and Member Discipline

A viewpoint-bundle library becomes thin and reusable only when the bundle itself stays stable while the member viewpoints remain explicit enough to review independently. The bundle therefore has two simultaneous obligations: coherence at the family level and clarity at the member level.

#### E.17.1:13.1 - What a viewpoint member should make explicit

Each member `U.Viewpoint` inside a reusable bundle should make explicit at least:

- the **concern family** it brings into focus,
- the **stakeholder families** for whom that concern matters,
- the **entity-of-interest class** for which it is admissible,
- the **allowed description/specification kinds** that usually realize it,
- and any **bundle-specific conformance or correspondence notes** that later view families should preserve.

`E.17.1` does not redefine the internals of `U.Viewpoint`. It states what must remain visible if a viewpoint is to be reused as part of a bundle rather than as an undocumented local label.

#### E.17.1:13.2 - Bundle-level coherence

A bundle is not just a bag of viewpoints with one shared prefix. A coherent bundle should answer a recognizable family-level question, such as:

- *which engineering concerns are standard for holon description?*
- *which governance perspectives are required for a service review?*
- *which research-method viewpoints recur across inquiry reports?*

If the member viewpoints do not share that family-level purpose, the result is not one bundle but an uncurated catalogue fragment.

#### E.17.1:13.3 - Thin bundles, rich annexes

`E.17.1` intentionally allows bundles to stay thin. Rich supporting material such as:

- lexical discipline notes,
- bridge overlays,
- routing notes,
- worked examples,
- or SoTA references

may live in typed annex manifests. This preserves a stable bundle core while still letting reuse packages carry enough didactic and review support.

### E.17.1:14 - Import, Subset, and Multi-Bundle Coordination

The value of viewpoint bundles appears most clearly when they are imported, subsetted, and coordinated across several reused families. Those cases need explicit discipline so that a local project does not quietly mutate what it claims to be reusing.

#### E.17.1:14.1 - Subset selection

A `U.MultiViewDescribing` family may legitimately import only a subset of a bundle's viewpoints. When it does so, it should declare:

- which `ViewFamilyId` is the source,
- which viewpoint members are actually in local use,
- and whether the omitted members are simply unused or are intentionally excluded because the local scope does not require them.

The local family must not speak as if it had imported the whole bundle while silently dropping inconvenient viewpoints.

#### E.17.1:14.2 - Local overlays vs new bundles

A local project often wants a small adaptation: one extra concern note, one narrower stakeholder emphasis, one local naming convention. `E.17.1` prefers explicit overlays or new editions over silent mutation.

A practical rule is:

- if the local project is merely selecting a subset or adding local didactic publications, keep the original bundle id and declare the overlay clearly;
- if the local project changes viewpoint membership or meaning, publish a new local bundle or a new edition.

This is how bundle reuse remains trustworthy across organizations.

#### E.17.1:14.3 - Multi-bundle coordination

Many real description families need more than one bundle, for example:

- one engineering viewpoint family,
- one safety or assurance family,
- and one governance or publication-oriented family.

In such cases, `E.17.1` expects the family to preserve the provenance of each member viewpoint rather than flattening everything into one unnamed `Sigma`. Cross-family correspondence should then cite both the participating viewpoint ids and their `ViewFamilyId` origins.

#### E.17.1:14.4 - Engineering vs publication families

Some contexts need both engineering viewpoints and publication viewpoints. `E.17.1` permits both, but it does not allow one family id to erase the distinction. A family that imports both kinds must keep the namespaces and bundle origins explicit so that authors do not confuse *how the holon is being understood* with *how a publication surface chooses to expose that understanding*.

### E.17.1:15 - Worked Bundle Families

#### E.17.1:15.1 - TEVB engineering family

A TEVB engineering bundle for holons may include viewpoints such as:

- `VP.Functional`,
- `VP.Procedural`,
- `VP.RoleEnactor`,
- `VP.ModuleInterface`.

The important point is not the vocabulary alone. The bundle states that these viewpoints are intended to recur together for one engineering family of concerns. A later description family then imports that engineering bundle rather than re-inventing a local list of "roughly similar" viewpoints.

#### E.17.1:15.2 - Governance and risk family

A governance bundle may group viewpoints such as:

- `VP.Risk`,
- `VP.Control`,
- `VP.Compliance`,
- `VP.Operations`.

This bundle is valuable precisely because the four viewpoints recur together but are not interchangeable. Keeping them as one family id makes the reuse visible while still preserving the distinct member meanings.

#### E.17.1:15.3 - Research-method family

A research-method bundle may include viewpoints such as:

- `VP.Theory`,
- `VP.Experiment`,
- `VP.Inference`,
- `VP.Limitations`,
- and, where appropriate, `VP.Reproducibility`.

A local inquiry note might import only three of these viewpoints, but the import remains legible because the omitted ones still belong to a reviewed family rather than disappearing into ad hoc prose.

#### E.17.1:15.4 - Cross-family description stack

A serious project may use TEVB engineering viewpoints for the design family, a governance bundle for program oversight, and a publication-oriented family for public surfaces. `E.17.1` makes this stack lawful by preserving which bundle each viewpoint came from and by preventing the final publication surface from masquerading as the viewpoint library itself.

### E.17.1:16 - Authoring and Review Guidance

#### E.17.1:16.1 - For bundle authors

Bundle authors should ask:

- what recurring family is being named,
- which viewpoints truly belong together in that family,
- what local didactic publications or examples belong in annexes instead of the bundle core,
- and whether the bundle is stable enough to deserve a reusable `ViewFamilyId`.

A good bundle is not maximal. It is coherent, reviewable, and reusable.

#### E.17.1:16.2 - For reviewers

Reviewers should inspect both levels:

- **member level** - are the included viewpoints individually explicit enough to be reused?
- **bundle level** - do they actually form one coherent family rather than one convenient list?

They should also check whether a local project has silently forked the bundle while still using the inherited family id.

#### E.17.1:16.3 - For integrators and librarians

Integrators should keep libraries small, curated, and editioned. It is usually better to publish:

- one stable core bundle,
- one explicit local extension,
- and one clear subset declaration

than to let one giant family absorb every recurring viewpoint a domain has ever used. Library sprawl destroys the cognitive advantage that reusable bundles are supposed to provide.

### E.17.1:17 - Edition and Migration Notes

#### E.17.1:17.1 - Rename vs semantic change

A lexical rename that leaves viewpoint meaning and membership unchanged may be treated as a naming-layer migration. A change in membership, concern, admissibility, or member semantics is not just a rename; it requires a new edition or a new local bundle.

#### E.17.1:17.2 - Migration from local `Sigma` lists

Legacy `U.MultiViewDescribing` families often publish only one local list of viewpoints. Migration should proceed by:

1. identifying recurring families across several such local lists,
2. publishing those families as explicit bundles,
3. then rewriting the local families to import the new `ViewFamilyId` and declare any subset selection explicitly.

This sequence preserves provenance and avoids pretending that the reusable family had always existed.

#### E.17.1:17.3 - Migration from surface-bound naming

If a legacy practice uses one label interchangeably for a viewpoint family, a report section, and a publication face, migration should separate those roles explicitly. `ViewFamilyId` remains at the bundle layer; `U.Viewpoint` ids remain at the viewpoint layer; publication-face names remain publication-layer vocabulary.

#### E.17.1:17.4 - Boundary to annex growth

Annex manifests are useful, but a bundle should not become a thin shell hiding all of its meaning elsewhere. The core bundle still needs enough explicit member and family structure to stand on its own. Annexes deepen reuse; they do not replace the bundle's primary declaration.
### E.17.1:18 - Import Collision and Alias Discipline

#### E.17.1:18.1 - Family id is not a synonym bag
A `ViewFamilyId` does not mean that all member viewpoints are interchangeable labels for one concern. It means that a reviewed family of viewpoints is intended to recur together. Authors should therefore resist the common drift where one convenient bundle name begins to substitute for all of its members.

#### E.17.1:18.2 - Import collision rule
When two imported bundles contribute viewpoints with overlapping lexical names, the publication should preserve the originating viewpoint ids and bundle provenance rather than silently merging the members. Bundle reuse is lawful only if collisions remain inspectable.

#### E.17.1:18.3 - Alias boundary
Local teaching aliases may be added for readability, but the alias must dock to explicit member viewpoints and must not erase bundle provenance. If the alias starts doing bundle-selection work by itself, it is making an unsupported bundle-selection claim and should be replaced by explicit member references.

### E.17.1:19 - Bundle Projection and Comparative Use

#### E.17.1:19.1 - Projection to local subsets
A description family may project only a subset of a reusable bundle. This is lawful if the omitted members remain visible as omitted rather than disappearing into an ad hoc local list. Projection keeps bundle provenance intact while acknowledging that local publication rarely uses every member.

#### E.17.1:19.2 - Comparative bundle use
Bundles may be compared across contexts only if the comparison preserves member ids, member meanings, and subset/projection decisions. Comparing two bundle labels alone is not enough, because similarly named families may contain materially different viewpoint sets.

#### E.17.1:19.3 - Boundary to publication-face design
A publication face may choose to surface one composite presentation of several viewpoints, but the face is not the bundle. `E.17.1` therefore requires the underlying member structure to remain recoverable even when a public-facing document flattens it for readability.

### E.17.1:20 - Review Matrix and Library Governance

A reviewer can test a viewpoint bundle library with five questions:

1. **Do the member viewpoints still have explicit standalone meaning?**
2. **Does the bundle name describe one coherent recurring family rather than one convenience list?**
3. **If a subset is imported, is the omitted remainder still visible as omission rather than silent deletion?**
4. **If several bundles interact, is provenance preserved across collisions and local aliases?**
5. **Has a publication face started impersonating the library itself?**

Library governance should therefore prefer small, editioned, provenance-preserving bundles over lexical mega-families that are easy to name but hard to reuse truthfully.
### E.17.1:End

## E.17.2 - `TEVB — Typical Engineering Viewpoints Bundle`

> **Tech‑name:** `TEVB` (Typical Engineering Viewpoints Bundle, bundle id `VF.TEVB.ENG`)
> **Plain‑name:** typical engineering viewpoints bundle for holons
> **Tag:** Archetypal species of `U.ViewpointBundle` for engineering holons

**Status.** New; archetypal, notation‑agnostic species of `U.ViewpointBundle` / `U.ViewpointBundleLibrary`.
It is an engineering‑level bundle over holons; it does not itself constitute an architecture framework or architecture‑specific viewpoint library. Architecture‑focused viewpoint bundles are introduced as separate `U.ViewpointBundle` species that may import TEVB.

**Builds on.**
* **E.17.0 — `U.MultiViewDescribing`.** Supplies the generic notion of `U.Viewpoint`, `U.View`, and `ViewFamily` over an `EoIClass ⊑ U.Entity` (here: `EoIClass = U.Holon`).
* **E.17.1 — `U.ViewpointBundleLibrary`.** Provides the generic `U.ViewpointBundle`/`ViewFamilyId` structure; TEVB is a concrete bundle (`VF.TEVB.ENG`) in the core library.
* **A.1 — Holon.** Holon kinds `U.System` and `U.Episteme` as the typical engineering entities‑of‑interest.
* **A.6.2–A.6.4 — Episteme morphisms.** `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, `U.EpistemicRetargeting` as the generic morphism classes behind engineering views.
* **A.7 / E.10.D2 — Strict Distinction & I/D/S.** I/D/S discipline and DescriptionContext; engineering descriptions/specifications under TEVB are D/S‑epistemes with explicit `ViewpointRef`.
* **C.2.1 — `U.EpistemeSlotGraph`.** Provides `DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot` and the slot discipline (A.6.5) used by TEVB‑aligned descriptions/specs.

**Used by.**
* **E.18:5.12 — E.TGA viewpoint map.** As a canonical consumer, E.TGA binds its engineering transduction families (Functional, Procedural, Role‑Enactor/Device‑Structure, Module‑Interface) to TEVB viewpoints `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface`.
* **E.17 (MVPK).** Publication of engineering morphisms uses TEVB engineering viewpoints on the description/spec side and PublicationVPs on the Surface side.
* **Engineering description/spec patterns.** System, method, module/interface and role‑related description/spec patterns for holons (`U.System`, `U.Episteme`) refer to TEVB when declaring their `ViewpointRef`.
* **ISO‑aligned architecture‑description bundles.** Future species patterns for architecture‑specific viewpoint bundles reuse TEVB as the canonical engineering view family (Functional vs Structural etc.) over systems and their epistemes.

**Guard (lexical & ontological).**
1. **Engineering scope only.** TEVB applies to `EoIClass = U.Holon` with typical cases `U.System` and `U.Episteme`. Using TEVB viewpoints for non‑holonic entities (e.g., pure data structures, abstract theories) requires an explicit species‑level justification; by default it is a conformance violation.
2. **Viewpoint vs Surface.** `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface` are **viewpoints** (intensional `U.Viewpoint` specifications), **not** Surface kinds. They MUST NOT be used as carrier/Surface names (those remain `{PlainView, TechCard, NormsCard, InteropCard, AssuranceLane, …}` under L‑SURF).
3. **EngineeringVPId vs PublicationVPId.** `VP.*` in this pattern are **EngineeringVPId** values (E.18:5.12) and SHALL NOT be reused as PublicationVPs in MVPK. MVPK must introduce separate `PublicationVPId` symbols, linked to TEVB viewpoints only through correspondences.
4. **No new role coordinates in I/D/S.** TEVB references stakeholder groups via `U.RoleEnactor` families but does not introduce `U.Role` as a coordinate in I/D/S signatures (E.10.D2). Role semantics remain confined to RoleEnactment patterns (A.15, F‑R family).
5. **No extra viewpoints inside TEVB.** TEVB defines a **fixed core set** of four engineering viewpoints. Other labels such as “Assurance‑Oriented”, “Interop‑Oriented”, “Information/Data‑Oriented”, “Operational/Deployment”, “Mission/Context” may appear only as **lexical aliases** in E.18:5.12 (e.g. as `ViewFamilyId` / `AliasInViewFamilies` values for transduction species). They MUST NOT extend `TEVB.EngBundle.viewpoints` and MUST NOT be interpreted as additional `U.Viewpoint` kinds in this bundle; when SoTA or local practice demands explicit assurance, information, or mission viewpoints, these SHALL be provided as **separate `U.ViewpointBundle` species** that can be imported alongside TEVB rather than by mutating `VF.TEVB.ENG`.
6. **Not an architecture framework.** TEVB is an engineering‑level viewpoint bundle; architecture‑specific viewpoint bundles and architecture frameworks MUST be introduced as separate `U.ViewpointBundle` species that may import TEVB. They MUST NOT redefine `VF.TEVB.ENG` as an “architecture viewpoint library” or extend it with architecture‑only viewpoints.

### E.17.2:1 - Problem frame  *(informative)*

Engineering teams almost always talk about systems and their models through a **small set of recurring “views”**:
* *What capabilities and behaviours does the system enact?* — function‑oriented, transduction‑oriented talk.
* *What sequences, workflows, and control logics does it realise?* — procedure/process/state‑oriented talk.
* *Who or what enacts which roles?* — role‑enactment, organisational and socio‑technical talk.
* *How is the system decomposed into modules and interfaces?* — physical/logical architecture talk.

In industry, these lenses show up under many names: *functional view, logical view, behavioural view, process view, structural/physical view, deployment view, responsibility view,* and so on. Modern standards and tools (ISO/IEC/IEEE 42010:2022, INCOSE SE Handbook, SysML v2 “views as queries”) all recognise that **viewpoints should be reusable structures**, not ad‑hoc labels.

In FPF, E.17.0 and E.17.1 give the **generic machinery**:
* `U.Viewpoint` as an intensional specification (stakes/concerns/allowed D/S kinds),
* `U.View` as an episteme‑level view (epistema under a viewpoint),
* `U.ViewpointBundle` / `ViewFamilyId` as reusable collections of viewpoints.

E.TGA (E.18:5.12) already assumes a **canonical engineering family** with names like “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, “Module‑Interface”. Without a formal bundle tying these together, those names drift and the mapping between E.TGA, MVPK and I/D/S becomes fragile.

TEVB addresses this by defining a **single, explicit engineering bundle** with a fixed `ViewFamilyId` and a small set of canonical engineering viewpoints over `U.Holon`.

### E.17.2:2 - Problem  *(informative)*

Without TEVB, several failure modes recur:
1. **Inconsistent “functional/structural/behavioural” vocabularies.** Different teams define “functional view” or “process view” differently, even within one organisation; E.TGA E.18:5.12 then has to guess how to map transduction graphs onto whichever interpretation is currently in play.
2. **Architecture frameworks leak into the kernel.** 4+1‑style and similar architectural frameworks get hard‑coded as if they were universal; FPF loses its holonic neutrality and becomes biased to a particular school.
3. **Viewpoints conflated with surfaces and files.** “Functional view” is used both for the underlying viewpoint and for a concrete document or dashboard; MVPK faces, E.TGA transduction families, and I/D/S disciplines become entangled.
4. **Role leakage into I/D/S.** Engineering views that are about role‑enactors are written directly in terms of `U.Role`, blurring the boundary between RoleEnactment (A.15) and description/spec layers, and breaking A.7/E.10.D2.
5. **Poor reuse across systems.** Even when organisations want to reuse the same engineering views across products, plants, or models, there is no canonical bundle to import; each programme recreates “its own” functional/structural views.

TEVB makes engineering viewpoint families **first‑class reusable bundles** and pins them to an explicit `EoIClass` (engineering holons) so that E.TGA, MVPK and discipline‑packs can align on the same vocabulary.

### E.17.2:3 - Forces  *(informative)*

| Force                                       | Tension                                                                                                                                                                       |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**           | We need engineering viewpoints that work for *any* holon (hardware/software/socio‑technical), yet remain recognisable to practitioners steeped in domain‑specific frameworks. |
| **Parsimony vs expressiveness**             | A small, stable **NQD‑front** set of engineering view families (Function, Behaviour/Process, Role‑Enactor, Module‑Interface) vs the temptation to proliferate specialised views for every stakeholder group or quality attribute. |
| **Neutral core vs architecture frameworks** | FPF core must stay neutral and not encode a specific framework (4+1, DoDAF, etc.), while still being compatible with them.                                                    |
| **Consistency vs organisational autonomy**  | Central TEVB definitions must be stable, yet individual organisations need room to refine concerns and episteme kinds within the bundle.                                      |
| **I/D/S clarity vs convenient shortcuts**   | Viewpoints must not re‑introduce `Role` as a coordinate in I/D/S, nor blur Description/Spec/Surface distinctions, even though practitioners informally mix these.             |

TEVB resolves these by fixing a **minimal engineering bundle** and leaving customisation to **species patterns and ViewpointBundleLibrary entries** that refine concerns and allowed episteme kinds without changing the core families.

### E.17.2:4 - Solution — TEVB as a core `U.ViewpointBundle` for holons  *(normative)*

#### E.17.2:4.1 - TEVB bundle identity

TEVB is the **core engineering viewpoint bundle** over holons.

* **Bundle object.** There exists a canonical `U.ViewpointBundle` instance:

  ```
  TEVB.EngBundle : U.ViewpointBundle
  ```

* **ViewFamilyId.**

  ```
  TEVB.EngBundle.viewFamilyId = VF.TEVB.ENG
  ```

  `VF.TEVB.ENG` is reserved for **“Typical Engineering Viewpoints (Engineering)”** in the FPF core ViewpointBundleLibrary.

* **EoIClassSpec (holon scope).**

  TEVB is parameterised by

  ```
  TEVB.EngBundle.EoIClassSpec =
    { h : U.Holon | holonKind(h) ∈ {U.System, U.Episteme} }
  ```

  That is, TEVB applies to holons that are either `U.System` or `U.Episteme`. Other holon kinds MAY be added by species patterns but MUST be justified and documented; the default conformance profile assumes systems and epistemes.

* **Library placement.**

  TEVB lives in the core viewpoint library:

  ```
  TEVB.Library : U.ViewpointBundleLibrary
  TEVB.Library.libraryId = FPF.Core.Viewpoints
  TEVB.Library.bundles ⊇ { TEVB.EngBundle }
  ```

  Additional organisational libraries MAY import and specialise TEVB, but SHALL NOT redefine `VF.TEVB.ENG` with incompatible semantics.

* **Viewpoint set.**

  TEVB defines a **finite set of canonical engineering viewpoints**:

  ```
  TEVB.EngBundle.viewpoints =
    { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
  ```

The selection `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the current **NQD-frontier** for engineering holon viewpoints in Part G: it realises a Function-Behaviour-Structure-plus-Role (`F-B-S+R`) cut that is non-dominated against candidate families including explicit information/data, assurance/safety, and mission/context viewpoints under the N/U/C/D characteristics (C.18, G.0). Part G records the SoTA candidate set and rejected alternatives; TEVB only fixes the **core four** where each `VP.* : U.Viewpoint` is defined below. These four are the **only** viewpoints in the core TEVB bundle.

  > **Note.** Other ViewFamilyId values used in E.TGA (e.g., *Assurance‑Oriented*, *Interoperability‑Oriented*, *Information/Data‑Oriented*, *Operational/Deployment*, *Mission/Context*) remain **lexical families only** for transduction species (E.18:5.12). They do not add viewpoints to TEVB; they are orthogonal to TEVB’s `viewpoints` set.

#### E.17.2:4.2 - TEVB engineering viewpoints

Each TEVB viewpoint is a `U.Viewpoint` with:
* `viewpointId : ViewpointId` (concrete identifier, e.g., `VP.Functional`);
* `EoIClassSpec` **inherited from the bundle** (`U.Holon` with `System`/`Episteme` kinds);
* `StakeholderFamilies : FinSet(RoleEnactorFamilyId)` — families of `U.RoleEnactor` that are the primary audience;
* `Concerns : FinSet(ConcernId)` — engineering concerns this viewpoint foregrounds;
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindRef)` — description/spec kinds admissible under this viewpoint (all obeying I/D/S discipline and C.2.1 slot discipline);
* `ConformanceRules : FinSet(RuleId)` — references to checklist items in conformance packs (CV/GF/engineering checklists).

The subsections below fix the **normative intent and minimal field profiles** for each TEVB viewpoint. Species patterns and discipline‑packs may refine `Concerns`, `AllowedEpistemeKinds` and `ConformanceRules`, but MUST preserve the intent.

##### E.17.2:4.2.1 - `VP.Functional` — capability & transduction viewpoint

**Intent.** Look at a holon in terms of **what it can do** under roles: capabilities, transductions, and functional responsibilities, rather than in terms of modules or procedures.

* **viewpointId.**

  ```
  VP.Functional : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**
  Same as the bundle: `U.Holon` with `System`/`Episteme` kinds.

* **StakeholderFamilies (typical examples).**
  Actual `StakeholderFamilies : FinSet(U.RoleEnactor)` values are defined in RoleEnactment discipline packs; labels below are informal.
  * System engineering leads and architects (e.g. SysEng‑lead enactors).
  * Product owners / capability owners.
  * Reliability / performance engineers when reading capability envelopes.

* **Concerns (typical).**
  * Capabilities and functions provided by the holon (`CapabilityConcerns`).
  * Behaviour under roles (`RoleBehaviourConcerns`).
  * Non‑functional envelopes: throughput, latency, availability, energy, safety (`NFPEnvelopeConcerns`).
  * Compositional semantics of functions/transductions (`TransductionCompositionConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.Functional` admits descriptions/specifications whose **DescribedEntitySlot** is a holon’s **capability/Method/Mechanism** under a role, e.g.:
  * `SystemFunctionalDescription`, `SystemFunctionalSpec` (species of `U.EpistemeKind` describing system‑level capabilities and their interconnection).
  * `TransductionDescription`, `TransductionSpec` (E.TGA functional lanes).
  * `ServiceCapabilityDescription`, `ServiceCapabilitySpec` (when a holon is in Service role).

  All such epistemes MUST:
  * obey I/D/S discipline: `…Description`/`…Spec` as D/S‑layers for `U.Method`/`U.Mechanism`/`U.PromiseContent`;
  * make their `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` explicit, with `ViewpointRef = VP.Functional`.

* **ConformanceRules (examples).**
  * Functional flows are **total** over their declared domain (no implicit dangling capabilities).
  * Transductions are typed at interfaces (A.6.0, A.6.1) and respect A.6.2/A.6.3 purity/conservativity.
  * When functional views participate in retargeting patterns (e.g. structural reinterpretation species based on `U.EpistemicRetargeting`), they MUST satisfy the relevant retargeting constraints from A.6.4; concrete consumer patterns (such as E.TGA structural reinterpretation, E.18) MAY impose additional rules.

* **SoTA echo (informative).** `VP.Functional` corresponds to the “functional view” in ISO-aligned architecture descriptions and domain reference architectures (functional viewpoints in IoT and space reference architectures, functional/logical layers in sector frameworks), and to the **Function** concern in FBS-style design ontologies. It is also the natural viewpoint-family placement for SysML/SysML-v2 capability and logical architecture models and for “logical view” slices in 4+1-style frameworks, once recast into holon/capability terms.

##### E.17.2:4.2.2 - `VP.Procedural` — process & control viewpoint

**Intent.** Look at a holon in terms of **how behaviours are sequenced and controlled**: workflows, state machines, operational procedures, and control logic.

* **viewpointId.**

  ```
  VP.Procedural : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Operations and run‑time owners (`OperationsEnactorFamily`).
  * Control engineers and automation specialists (`ControlEngineerEnactorFamily`).
  * Safety engineers concerned with procedural correctness (`SafetyEngineerEnactorFamily`).

* **Concerns (typical).**
  * Control flow and ordering of actions (`OrderConcerns`).
  * State‑machine behaviour and lifecycle (`StateLifecycleConcerns`).
  * Concurrency, synchronisation, and error handling (`ConcurrencyConcerns`).
  * Operational modes and transitions (startup, shutdown, degraded modes) (`OperationalModeConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.Procedural` admits descriptions/specifications where the **DescribedEntitySlot** is a method/process/control Behaviour for the holon, e.g.:
  * `MethodDescription`, `MethodSpec` for operational procedures (A.3.1–A.3.2).
  * `ControlLogicDescription`, `ControlLogicSpec` (IEC 61131‑3 style step diagrams/statecharts).
  * `WorkflowDescription`, `WorkflowSpec` (business processes, orchestration logic).

  These epistemes:
  * must respect the **order discipline** (Γ_method, Γ_ctx) and A.15 (Role–Method–Work alignment);
  * must carry I/D/S‑conformant DescriptionContext with `ViewpointRef = VP.Procedural`.

* **ConformanceRules (examples).**
  * Pre/post‑conditions at step boundaries are explicit and type‑checked (A.3.1/A.3.2, Γ_method).
  * No embedding of Work or calendars inside procedural descriptions (A.7/E.10.D2).
  * Failure modes and recovery actions are declared and traceable to safety analyses (F.15 harnesses where relevant).

* **SoTA echo (informative).** `VP.Procedural` captures the dynamic/process dimension found in SoTA architecture and MBSE practice: process views in 4+1, operational/behavioural views in defence and enterprise frameworks, behaviour diagrams in SysML (activity, sequence, state, interaction), and procedure/control‑oriented models in industrial standards. TEVB abstracts this into a notation‑agnostic “behaviour over time” viewpoint for holons.

##### E.17.2:4.2.3 - `VP.RoleEnactor` — role & device‑structure viewpoint

**Intent.** Look at a holon in terms of **who/what plays which roles** and **how physical/organisational structure supports those roles**. This viewpoint covers both socio‑technical role assignments and “device view” readings of transduction graphs (E.TGA).

* **viewpointId.**

  ```
  VP.RoleEnactor : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Organisational designers and operations managers (`OrgDesignEnactorFamily`).
  * Safety and compliance officers concerned with separation of duties (`SegregationOfDutyEnactorFamily`).
  * Hardware/system engineers concerned with which devices carry which functions (`DeviceEngineerEnactorFamily`).

* **Concerns (typical).**
  * Which holons enact which roles under which contexts (`RoleEnactmentConcerns`).
  * Allocation of capabilities to devices/subsystems (`CapabilityAllocationConcerns`).
  * Organisational constraints: segregation of duties, responsibilities, escalation paths (`GovernanceConcerns`).
  * Device‑view readings of functional graphs (E.TGA Device‑View).

* **AllowedEpistemeKinds (shape).**
  `VP.RoleEnactor` admits descriptions/specifications where the **DescribedEntitySlot** is a **role structure or capability allocation** associated with the holon, e.g.:
  * `RoleDescription`, `RoleSpec` (F.4, F.18) for human or system roles.
  * `RoleEnactmentDescription` for mappings `Holder#Role:Context` (A.15).
  * `DeviceAllocationDescription` mapping functions/transductions to physical modules or devices.

  As with other TEVB viewpoints, these are D/S‑epistemes with `DescriptionContext.ViewpointRef = VP.RoleEnactor`.

* **ConformanceRules (examples).**
  * Role vs Method vs Work vs Capability separation is upheld (A.7, A.15).
  * Device‑view reinterpretation from functional flows MUST be expressed as `U.EpistemicRetargeting` with an explicit `KindBridge` witness (A.6.4). Specific retargeting schemes (for example, E.TGA’s structural reinterpretation in E.18) may add further constraints but are not fixed by TEVB itself.
  * No “role as behaviour” conflation: Roles are masks, behaviours remain Methods/Work.

* **SoTA echo (informative).** `VP.RoleEnactor` aligns with the allocation/responsibility and resource/organisational view clusters seen across MBSE frameworks: allocation views in UAF/NAF, role-responsibility matrices and RACI-style artefacts, and “who/what plays which role” slices in usage and operational viewpoints. Many post-2015 reference architectures treat this concern implicitly; TEVB makes it explicit and holon-centred while remaining compatible with socio-technical and device-allocation practices.

##### E.17.2:4.2.4 - `VP.ModuleInterface` — module & interface viewpoint

**Intent.** Look at a holon in terms of its **modules, interfaces, and structural composition**: what parts exist, how they connect, and how their interface specifications are stated.

* **viewpointId.**

  ```
  VP.ModuleInterface : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**
  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Hardware and software architects responsible for structure (`StructureArchitectEnactorFamily`).
  * Integration and test engineers (`IntegrationEngineerEnactorFamily`).
  * Lifecycle and maintenance planners looking at replaceable units (`MaintenancePlannerEnactorFamily`).

* **Concerns (typical).**
  * Module decomposition and containment (mereology) (`ModuleMereologyConcerns`).
  * Interfaces and specifications — ports, APIs, physical connectors (`InterfaceConcerns`).
  * Dependency structures and allowed couplings (`DependencyConcerns`).
  * Replaceability and variation points (`VariabilityConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.ModuleInterface` admits descriptions/specifications where the **DescribedEntitySlot** is a **structural architecture** of the holon, e.g.:
  * `SystemStructureDescription`, `SystemStructureSpec` (module/connector descriptions).
  * `ModuleInterfaceDescription`, `ModuleInterfaceSpec` (signature, interface specifications, physical interface definitions).
  * E.TGA‑style interface/port descriptions over `Signature`/`Mechanism` graphs.

  These epistemes describe the carrier (structure) rather than capability. Functional↔physical reinterpretations between `VP.Functional` and `VP.ModuleInterface` are expressed via `U.EpistemicRetargeting` + `KindBridge` (A.6.4, E.18).

* **ConformanceRules (examples).**
  * Interfaces are typed and explicitly bound to standards where applicable (A.6.0, F‑specs).
  * No inlining of Methods/Work into structure (strict separation of structure vs behaviour).
  * Reinterpretations from functional views into structure MUST respect the applicable `U.EpistemicRetargeting`/Bridge constraints (A.6.4). When combined with a concrete retargeting scheme (e.g. E.TGA structural retargeting, CC‑TGA‑06‑EX), that scheme’s additional rules also apply.

* **SoTA echo (informative).** `VP.ModuleInterface` matches the structural/implementation/deployment families that dominate SoTA architecture descriptions: development and physical views in 4+1, construction/deployment viewpoints in IoT reference architectures, logical/physical architecture layers in UAF/NAF and RASDS‑style frameworks, and structural and interface‑focused models in SysML‑based MBSE. TEVB treats all of these as specialisations of a single holonic “modules and interfaces” viewpoint.

### E.17.2:5 - Archetypal grounding  *(informative)*

A minimal TEVB instantiation looks as follows:

```
TEVB.EngBundle :
  U.ViewpointBundle {
    viewFamilyId   = VF.TEVB.ENG
    EoIClassSpec   = { h : U.Holon | HolonKind(h) ∈ {System, Episteme} }
    viewpoints     = { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
    LibraryRef     = FPF.Core.Viewpoints
  }
```

Each `VP.*` viewpoint is a `U.Viewpoint` as in E.17.0, with:

* `viewpointId ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `EoIClassSpec` inherited from `TEVB.EngBundle`,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` aligned with the subsections above.

**Engineering holon (example).**

Let `Plant_X : U.System` be a production plant, and `ControlStack_X : U.Episteme` be its control and optimisation stack as a holon.

* Under `VP.Functional`, `Plant_X` is viewed as a bundle of capabilities and transductions: material/energy/product flows, optimisation functions, safety envelopes.
* Under `VP.Procedural`, `Plant_X` is viewed as sets of procedures and control sequences: startup/shutdown, normal operation, emergency handling.
* Under `VP.RoleEnactor`, `Plant_X` is viewed as networks of role‑enactors: human operators, controllers, subsystems enacting roles in SOPs and safety cases.
* Under `VP.ModuleInterface`, `Plant_X` is viewed as modules and interfaces: equipment units, pipelines, control modules, buses, and their interfaces and specifications.

Each of these is a **family of D/S‑epistemes** with `DescriptionContext = ⟨DescribedEntityRef(Plant_X or ControlStack_X), BoundedContextRef, ViewpointRef=VP.*⟩` and TEVB ensures that E.TGA and MVPK can rely on this common structure.

### E.17.2:6 - Conformance checklist  *(normative)*

**CC‑TEVB‑1 (Bundle identity).**
Any artefact claiming to be “TEVB engineering viewpoints” MUST:

* refer to `viewFamilyId = VF.TEVB.ENG`,
* have `EoIClassSpec = {h : U.Holon | HolonKind(h) ∈ {System, Episteme}}`,
* enumerate `viewpoints = {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` and no others.

**CC‑TEVB‑2 (Viewpoint definition).**
Each `VP.*` viewpoint MUST be a well‑formed `U.Viewpoint` per E.17.0:

* `viewpointId` equal to one of the four engineering IDs,
* `EoIClassSpec` equal to the bundle’s,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` explicitly declared.

**CC‑TEVB‑3 (DescriptionContext completeness).**
Every D/S‑episteme participating in a TEVB‑managed multi‑view family for a holon MUST have a `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` with:

* `DescribedEntityRef` referencing a `U.System` or `U.Episteme`,
* `ViewpointRef ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `BoundedContextRef` pointing to the engineering context (E.10.D1).

**CC‑TEVB‑4 (Separation from PublicationVPs).**
`VP.*` identifiers from TEVB MUST NOT be used as `PublicationVPId` in MVPK. Publication viewpoints live in MVPK and may **correspond** to TEVB engineering viewpoints via `CorrespondenceModel`, but are separate symbols.

**CC‑TEVB‑5 (No Role coordinate in I/D/S).**
TEVB-aligned descriptions/specs MAY reference `U.RoleEnactor` families in `StakeholderFamilies` but SHALL NOT add `Role` or `RoleEnactor` as characteristics in I/D/S signatures beyond what A.7/E.10.D2 already provides. Role semantics stay in RoleEnactment patterns; TEVB just selects concerns.

**CC‑TEVB‑6 (Alignment with consumer viewpoint maps).**
When a pattern defines engineering viewpoint families named “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, or “Module‑Interface” over the same `EoIClass` and claims TEVB alignment (for example, E.TGA E.18:5.12 viewpoint map), it MUST bind them to TEVB viewpoints as follows:

* “Functional” → `VP.Functional`,
* “Procedural” → `VP.Procedural`,
* “Role‑Enactor (Device‑Structure)” → `VP.RoleEnactor`,
* “Module‑Interface” → `VP.ModuleInterface`.

Any deviation MUST be explicitly documented as a species‑level extension and MUST NOT reuse `VF.TEVB.ENG`.

### E.17.2:7 - Rationale & SoTA echoing  *(informative)*

#### E.17.2:7.1 - NQD‑grounded choice of the core four

Part G’s NQD discipline treats candidate viewpoint families as points in an N/U/C/D quality space (Use‑Value, Constraint‑Fit, Novelty, Diversity_P). Applied to a SoTA‑harvested candidate set of engineering viewpoints (Functional, Behavioural/Procedural, Structural/Module, Allocation/Role, Information/Data, Assurance/Safety, Mission/Context, Deployment/Operational, Business/Usage), this yields a small Pareto frontier for *engineering holon* viewpoints. On that frontier, the `F–B–S+R` cut implemented by `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the minimal set that:
* spans the Function-Behaviour-Structure ontology used in contemporary design theory while adding an explicit allocation/responsibility concern;
* aligns with the “functional/process/structural/deployment” clusters recurrent in standards and architecture frameworks;
* stays neutral with respect to domain‑specific qualities (`‑ilities`) and business/mission framing, which are captured in separate Q‑Bundles and governance-oriented viewpoint bundles rather than in TEVB itself.

Other candidates (e.g. dedicated information, assurance, or mission viewpoints) remain important but either duplicate concerns already captured by TEVB (when specialised to engineering holons) or are better modelled as orthogonal quality bundles (C.25) or non-engineering viewpoint bundles (business and governance viewpoint bundles). TEVB therefore pins only the core four and leaves the rest to specialised families.

#### E.17.2:7.2 - Alignment with post‑2015 engineering practice

* Modern architecture standards built on ISO/IEC/IEEE 42010 describe viewpoint libraries in which functional, behavioural/process, structural/deployment, and business/usage concerns are the dominant clusters; sector RAs such as IoT RA 30141 and space‑domain RAs provide explicit functional and construction/implementation viewpoints alongside business/usage and trustworthiness viewpoints. TEVB reuses the functional and construction/structural clusters as `VP.Functional` and `VP.ModuleInterface`, while treating business and trustworthiness as separate bundles.
* Model-based systems engineering practice (INCOSE MBSE guidance, SysML v2 “views-as-queries”, UAF/NAF view grids) converges on a small set of core diagram families: structure vs behaviour vs allocation/responsibility vs requirements/mission. TEVB’s `VP.Procedural` and `VP.RoleEnactor` correspond to the behaviour and allocation/responsibility concerns, respectively, and are designed to be notation-neutral over SysML/UAF/UML/Capella-style models.
* The FBS family of design ontologies (Function–Behaviour–Structure and extensions) provides a widely used conceptual basis for separating what a system is for, what it does over time, and what it consists of. TEVB’s four viewpoints intentionally implement an FBS+R split at the holon level: `VP.Functional` ≈ Function, `VP.Procedural` ≈ Behaviour, `VP.ModuleInterface` ≈ Structure, with `VP.RoleEnactor` capturing the explicit mapping from functions/behaviours to role‑enacting carriers.
* Within FPF itself, E.TGA’s “viewpoint families” (Functional, Procedural, Role‑Enactor/Device‑Structure, Module‑Interface, plus assurance/interoperability/data/operational/mission aliases) are harmonised by letting the **core four** be TEVB viewpoints and treating the rest as lexical or bundle‑level overlays, not as new kernel viewpoints.

#### E.17.2:7.3 - Why TEVB stays small

TEVB is deliberately *not* a complete architecture framework. It gives FPF a stable, holon‑centred engineering bundle that:
* is small enough to keep in working memory and to govern via EpistemeSlotGraph discipline;
* is expressive enough to represent mappings from SoTA architecture frameworks (4+1, domain‑specific RAs, UAF/NAF grids, SysML‑based MBSE method kits);
* can be safely combined with additional `U.ViewpointBundle` species (safety/assurance packs, business/mission packs, information/data packs) without mutating the core four;
* sits conceptually **below** architecture‑specific viewpoint libraries, which are introduced as separate `U.ViewpointBundle` species layering TEVB with mission/quality/business viewpoints instead of redefining TEVB.

As SoTA evolves, new bundles can be added or TEVB can gain a new edition with a revised NQD‑frontier, but the TEVB‑A edition fixed here remains the archetypal engineering bundle for holons.

### E.17.2:8 - Relations  *(informative)*

* **Builds on.** E.17.0 (`U.MultiViewDescribing`), E.17.1 (`U.ViewpointBundleLibrary`), A.7/E.10.D2 (I/D/S), C.2.1 (EpistemeSlotGraph), A.6.2–A.6.4 (episteme morphisms).
* **Constrains.** E.18:5.12 (E.TGA viewpoint map), engineering description/spec patterns, MVPK engineering publication profiles.
* **Coordinates with.** L‑SURF/L‑PUBSURF (Surface kinds), F‑R family (Role, RoleDescription, RoleSpec), F.18 (naming discipline for ViewFamilyId / ViewpointId / EngineeringVPId / PublicationVPId).
* **Non‑goals.** TEVB does not prescribe modelling notations (SysML, BPMN, IEC 61131‑3, etc.), storage formats, or tool APIs. It only fixes the **conceptual viewpoint bundle** that such tools must respect when claiming FPF alignment.

### E.17.2:End

## E.17 - Multi‑View Publication Kit

**At a glance.** Use `E.17` when one source-backed episteme, episteme-lane view, morphism, or functional relation must be published in several readable faces for different readers without changing the underlying claim.

**Use this when.** The engineering team needs a plain view, technical card, interoperability card, or assurance lane that helps people read, inspect, exchange, or cite the same source-backed relation without turning the face into work occurrence, evidence, gate passage, engineering justification, control architecture, or release permission by presentation alone.

**First output.** One source-pinned publication face with the underlying `U.Episteme`, `D` episteme, or `S` episteme, publication scope, face kind, admissible publication use, and any live downstream typed value named only as far as the current use needs, such as a `GateDecision`, evidence path, work occurrence, status source, or authority-reference relation.

**Working action spine.** Publish one source-pinned face -> separate source episteme or episteme-lane view, face, carrier, admissible publication use, and any live downstream typed value plus its governing FPF pattern/reference -> use the face for inspection, source-finding, review, exchange, or planning preparation -> output one source-pinned publication face -> apply the exact neighboring FPF pattern if work, evidence, gate, engineering-justification, control, or release use becomes live.

**Ordinary formality rule.** If the face only supports orientation, source-finding, review, comparison, or planning preparation, keep the publication light: one pinned face or compact card plus a clear admissible-use line is enough.

**Load-bearing formality rule.** Add the fuller MVPK record only when the face will support external-impact reliance, cross-context exchange, evidence citation, gate or release pressure, engineering-justification use, disputed interpretation, or another use where a concrete overclaim would change the next engineering move.

**Stop condition.** Do not create a new publication record merely because a face exists. Stop when the current face changes no next engineering move and blocks no concrete overclaim.

**Admissible publication-use examples.**

| Admissible publication use | Source-finding or bounded inspection with no downstream claim or effect | Non-admissible publication use |
| --- | --- | --- |
| A source-pinned MVPK face lets the team inspect one morphism, review it, exchange it, or prepare planning without changing the claim. | A face helps planning support, but the team still needs to recover the exact method, evidence, gate, control, or carrier source before work, evidence, gate, control, carrier, or other downstream use. | A face, screen, export, or diagram is treated as performed work, gate passage, evidence, engineering justification, supervisory relation or control relation, or release permission by layout or readability alone. |


**Boundary aid pointer.** If one encountered publication-facing item is easy to read as work, evidence, gate, approval, status, explanation, comparison, or narrower-use rendering, handle one live claim or effect at a time using `E.17:5.1d`.

Here in the first-screen read, keep only the MVPK publication move: one source-pinned face, one admissible publication use, and exact neighboring FPF patterns or typed downstream values only as far as the current use needs.


**Not this pattern when.** Not this pattern when the live issue is performed `U.Work`, a work plan, evidence path, provenance path, engineering justification, gate decision, control architecture, carrier work, OCR work, or a narrower-use rendering that needs its own source-bearing return. Use the exact FPF pattern that governs that issue.

> **Tech‑name:** `U.MultiViewPublicationKit` (**MVPK**)
> **Plain‑name:** Multi‑view publication kit. The morphism-publication profile is the canonical formal profile.
> **General publication-face form:** one MVPK face is a `U.View` emitted over one source `U.Episteme` or episteme-lane `U.View`, under one publication `U.Viewpoint`, one `U.PublicationScope`, declared pins where needed, one face kind, and one admissible publication use. The face adds no claim by readable form. Evidence use, authority use, gate use, work use, release use, and engineering-justification use require the exact neighboring FPF pattern and typed project-side value/reference that carry that downstream use, such as a `GateDecision`, evidence path, work occurrence, status source, or authority-reference relation.
> **Canonical morphism profile (conceptual form):**  `MVPK : (U.Morphism, Σ_viewpoints) ↦ U.ViewFamily` with per‑viewpoint components
> `ViewObj_s : U.Object → U.ViewObj_s` and `Emit_s(-) : U.Morphism → U.ViewMorph_s`,
> such that `(ViewObj_s, Emit_s)` forms a functor `U → View_s(U)`. For each `s ⪯ t`, a **reindexing coercion**
> `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` exists and is **natural in `X`**: for every `f : X → Y`,
> `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X` (see Rules §6.2).
> **Notation:** `Σ_viewpoints` is abbreviated as `Σ` where convenient.
> **Twin‑register aliases (naming discipline):**
> • **Tech:** `Emit_PlainView`, `Emit_TechCard`, `Emit_InteropCard`, `Emit_AssuranceLane`; `PromoteView[s→t]_-`.
> • **Plain:** `PlainView(x)`, `TechCard(x)`, `InteropCard(x)`, `AssuranceLane(x)`; “Promote to *t*”.

> **USM binding (overview):** `PublicationScope` is a **USM‑class** object that parameterizes MVPK; see §5.0.
> **Episteme lane.** MVPK treats each face as a `U.View` in the sense of C.2.1 and E.17.0 (species `U.EpistemeView`). For any MVPK face, the source is a named `U.Episteme` or episteme-lane `U.View`; the face declares a publication `U.Viewpoint` (`PublicationVPId`) drawn from a `U.ViewpointBundle` (E.17.1 and E.17.2). In the morphism profile, every `Emit_s(f)` has `DescribedEntitySlot` and `DescriptionContext` target `f : U.Morphism`. In a non-morphism publication, the face names the exact source episteme, episteme-lane view, described entity, or claim relation that the face publishes, and no functorial composition claim is live unless the corresponding FPF pattern supplies it. Slot discipline (`ViewSlot` and `ViewRef`) is inherited from C.2.1 and A.6.5 and is not redefined in MVPK.

### E.17:1 - Intent

Provide a disciplined way to publish one source episteme or episteme-lane view across multiple didactic faces without adding semantics, while keeping publication viewpoints explicit and auditable. The canonical formal profile is morphism publication: a small view-pack applied to any `U.Morphism`, including compositions, yields a family of views that commute with arrow composition and respect edition and measurement pinning.

### E.17:2 - Problem frame

* Teams routinely need several **faces** of the *same* arrow: a **`TechCard`** for the catalog, an **`InteropCard`** for machine exchange, a **`PlainView`** for narrative, and an **`AssuranceLane`** for evidence.
* Informal “renderings” quietly **drift semantics**; **composite arrows** are often published piecemeal, breaking traceability; **evidence** forgets unit, scale, and edition pins.
* “View” and “viewpoint” are **blurred** in practice; authors conflate **publication** with **mechanism**.
* L‑SURF requires **`SurfaceKind` token discipline**; Core allows only **PublicationSurface** or **InteropSurface**; faces are named **...View**, **...Card**, or **...Lane** (no ad‑hoc `...Surface` kinds).

**MVPK** fixes this by making publication a typed projection from existing source epistemes or episteme-lane views via species of `U.EpistemicViewing` subject to explicit viewpoint specs and pinning guards. In the morphism profile, this projection is the functorial D and S episteme publication discipline described below. **Part E is conceptual:** no machine-exchange formats are specified here.

### E.17:3 - Problem

1. **Semantic drift in publication.** Unchecked “presentations” introduce claims not present in the D-side or S-side epistemes about the arrow (epistemes with `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` in the sense of E.10.D2 and E.17.0).
2. **Non‑compositionality.** Publishing `g∘f` yields faces that do not match composing the faces of `f` and `g`.
3. **View vs viewpoint confusion.** A single template is treated as “the view”, with no declared concerns or conformance rules.
4. **Unpinned numbers.** Numeric claims lack unit, scale, reference‑plane, and **edition pins** from Part F or Part G, undermining auditability.

### E.17:4 - Forces

| Force | Tension |
| --- | --- |
| **Compositionality vs legibility** | Preserve arrow invariants across views ↔ keep each view didactic and audience‑appropriate. |
| **Neutral naming vs domain idioms** | Use vocabulary stable across domains ↔ allow local templates (SOPs, APIs, checklists). |
| **Publication-face independence (A.7)** | Publication must not mutate I-, D-, and S-semantics ↔ authors expect rich presentations. |
| **Evidence discipline** | Views must cite CG‑Spec and CHR anchors ↔ authors want compact cards. |

### E.17:5 - Solution — the **MVPK Kit**

#### E.17:5.0 - USM anchoring (normative)
* **PublicationScope (USM).** `U.PublicationScope` is defined in **USM** (A.2.6 §6.5) analogously to `U.WorkScope` and `U.ClaimScope` as a **set‑valued scope object** over `U.ContextSlice`. In MVPK, every emitted `U.View` SHALL declare a `U.PublicationScope` that bounds where that face is admissible.
  * **Non‑overload rule.** `U.PublicationScope` MUST NOT encode viewpoint choice, MVPK profile selection, or Publication Characteristics (PC); those are governed by `PublicationVPId`/`U.Viewpoint` and MVPK profile rules (§5.1/§5.2/§5.5).
* **Scope lineage.** `U.PublicationScope` participates in the same USM lineage regime as `U.WorkScope`/`U.ClaimScope` (Δ‑moves, editioning and migration rules); MVPK emits faces **under** a declared `PublicationScopeId`.
* **MVPK profile (kit configuration).** The canonical MVPK profiles (MVPK‑Min, MVPK‑Lite, MVPK‑SetReady, and MVPK‑Max) fix:
  * (a) the **viewpoint index** `Σ` and its partial order `⪯`,
  * (b) the admissible **Publication characteristics (PC)** and required **pinning requirements**,
  * (c) any cross‑Context or cross-plane constraints (Bridge and CL policies) applicable to emitted faces.
* **MVPK face-name quartet.** The canonical MVPK-Max profile enumerates exactly four **face kinds**: `PlainView (P)`, `TechCard (T)`, `InteropCard (I)`, `AssuranceLane (A)`. MVPK face ids, `SurfaceKind` values, claim quadrants, `governingPatternRef`, and local field values must not use an L-, P-, D-, and E-mnemonic; use the P-, T-, I-, and A-face-name initials only when an abbreviation is unavoidable.

#### E.17:5.1 - Terminology (normative)

* **View** (`U.View`): an episteme-lane view (`U.EpistemeView` in the sense of C.2.1 and E.17.0) produced under a publication viewpoint. In MVPK each face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) is such a `U.View`. In the morphism profile its `DescribedEntitySlot` and `DescriptionContext` target is a `U.Morphism`; in a non-morphism publication, the target is the exact source episteme, episteme-lane view, described entity, or claim relation named by the source.
  Every MVPK `U.View` **SHALL** declare:
  `SurfaceKind ∈ {PublicationSurface, InteropSurface}`, `PublicationVPId : U.ViewpointRef`, references to the underlying D epistemes and S epistemes produced by `Describe_ID` or `Specify_DS` in `A.7` and `E.10.D2`, and a `U.PublicationScope` (USM §6.5).
  Any carrier rendering is separate **`U.Work` on SCR and RSCR carriers** and is not part of `U.View`.
* **Publication vs presentation vs rendering vs representation (guard):**
    * **Publication** = typed projection from existing source epistemes or episteme-lane views into a `U.View` governed by a `PublicationSurface` or `InteropSurface` `SurfaceKind` via species of `U.EpistemicViewing` (`A.6.3`). In the morphism profile, the source epistemes are the D and S epistemes about a morphism under the I, D, and S discipline of `A.7` and `E.10.D2`.
    * **Presentation** = rhetorical arrangement of a published carrier; **notation-neutral**, adds no claims and is **not** a `SurfaceKind`.
    * **Rendering** = display layout of a carrier, purely graphical formatting; **`U.Work` on carriers** (A.7), not a `SurfaceKind`.
    * **Representation** = episteme↔referent relation (`C.2.1`, `A.6.2` through `A.6.4`); **not** a publication operation and not a `SurfaceKind` operation. Use **publication** and **view** here; treat presentation and rendering as **`U.Work` on carriers** (`A.7`).
* **ISO mapping note.** ISO **viewpoint** → `PublicationVPId` (publication lane); **engineering viewpoint** → `EngineeringVPId` (E.TGA E.18:5.12). An ISO **view** may be a single MVPK face; “bundles” are packaging only.
* **No‑mechanism equivalence:** MVPK **is not** a mechanism; any operational activity, such as build, render, or upload work, is **separate `U.Work` by a system on carriers** (A.7; see **Rule 5 — No Γ-leakage** in §6).
* **ViewpointSpec (`U.Viewpoint`)** — a typed specification that declares stakeholders, concerns, conformance rules, allowed **Publication Characteristics**, and pinning requirements per profile. The index set `Σ` consists of identifiers of `U.Viewpoint` instances, typically drawn from `U.ViewpointBundle` species (E.17.1 or E.17.2) (see §5.3).
* **Explanation-use profile values.** Existing faces may state an explanation-use profile value as `SourcePinnedExplanation`, `SourceLinkedExplanationReconstruction`, `DidacticRetelling`, or `SpeculativeRetelling`, but those are local profile values over already existing MVPK faces rather than new face kinds, explanation kinds, or carrier-rendering kinds. Per-face pins, provenance anchors, and no-new-A.6.B-boundary-claims discipline still apply.

#### E.17:5.1a - Episteme-publication lane binding  *(normative)*

For functional-description publications, MVPK governs the publication lane only.

**Publication lane.** A principle scheme, functional diagram, comparison table, screen, export, scenario, explanation, or code-like method description may support interpretation, source-finding, comparison, selected-method inspection, or work-planning support.

**Unsupported neighboring claims.** The publication does not by itself assert performed `U.Work`, gate passage, evidence, engineering justification, supervisory relation or control relation, release permission, or a new TGA kind.

**Interface and protocol proximity.** When interface, protocol, schema, boundary, or API wording appears beside a functional-flow description, keep the operational boundary, interface, or protocol claim with its own project claim set and exact typed project-side value and reference, governed by the relevant FPF pattern such as `A.6.B`, `A.6.C`, or `E.18`. Do not absorb it into the functional-flow publication by layout proximity.

**Retargeting.** If the publication changes the governed target from an already described component, process, material `U.Entity`, or source claim into a functional, control, or flow architecture claim, this is not a same-entity publication-use change. Use `A.6.4`, `OntologicalReframing`, or `E.18` as applicable.

**Source recovery.** When a requested use requires an exact typed project-side value and reference beyond the publication face, the engineer first recovers the corresponding existing project-side FPF value if one already carries the needed claim:

- work-relevant source restoration under `A.15.4`;
- project `U.Method`, `U.WorkPlan`, or work-result record under `A.15`;
- evidence and provenance path under `A.10`;
- engineering-justification record under `B.3`;
- constraint or gate decision under `A.20` or `A.21`;
- supervisory or control architecture record under `B.2.5`;
- carrier, export, OCR, or front-end record under `A.7`;
- same-entity textual relation under `A.6.3.CR`;
- representation relation under `A.6.3.RT`;
- reduced-use-rendering relation under `A.6.3.CSC`.

**No backdating.** If no existing exact typed project-side value and reference carries a claim that was supposed to be already supported, do not create a backdated source. Create only a prospective repair request, decision request, future work-plan entry, or explicit source-gap note, and treat the earlier claim or effect as unsupported until the required source exists.

Ordinary orientation and source-finding can stay as an inline note.

**Functional-description guard (`CC-MVPK-FD`).** A functional-description publication face must separate the source `U.Episteme` or episteme-lane `U.View`, the MVPK face, any live carrier or rendering work, the admissible engineering use, and non-admissible neighboring use. The guard applies only when a functional-description face is present; it is not the first universal MVPK conformance gate.

MVPK inherits the C.2.1 distinction between `U.Episteme`, `U.EpistemePublication`, publication form, `U.View`, carrier, and authority-reference relation. MVPK does not introduce a generic semio kind and does not let a publication face act as `governingPatternRef`, `authoritySourceRef`, or the source claim for a claim.

When a morphism publication is encountered or reused, name the relevant lane before relying on it:

* the underlying `U.Episteme`, `D` episteme, or `S` episteme whose ClaimGraph is being projected;
* the `U.EpistemePublication` or governed `U.Episteme` publication when the episteme is available as a published episteme;
* the publication form used by the local pattern, if one is live;
* the `U.View`-typed MVPK face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) that renders the publication for a viewpoint;
* the SCR/RSCR carrier or rendering work that holds or displays it;
* the exact typed project-side value and reference or authority-reference relation when the next work or reliance claim depends on that named authority-reference relation, approval source, gate source, release source, or exact typed project-side value and reference.

The practical payoff is that a reader can recover exactly what may be relied on: the episteme claim, the published form, the view, the carrier, the exact typed project-side value and reference, or the authority-reference relation. A dashboard tile, generated explanation, card face, credential view, or carrier can guide source-finding, but it does not by itself become the source claim or effect, gate decision, evidence relation, assurance claim, role or status, work occurrence, or permission.

**Source-exposure rule.** A publication face, carrier, rendering, dashboard tile, credential view, status view, comparison unit, explanation rendering, signed decision memo, release decision record, approval speech-act publication, or gate dashboard may expose, cite, or carry an exact typed project-side value and reference only when that value is recoverable under its governing FPF pattern and exact source relation. It does not become that value by readability, layout, title, color, fluency, proximity, copying, generation, or reuse. When the exposed value is a real `SpeechAct`, `GateDecision`, evidence path, credential source, status source, `U.Work` occurrence record, `U.Episteme`, or `U.EpistemePublication`, rely on that typed and recoverable value and its FPF-governed source relation; otherwise treat the face, carrier, display, or rendering as orientation or source-finding only.

**No retroactive source creation.** When required source support is missing, a new entry can be only a prospective repair request, future decision request, prospective work-plan entry, or explicit source-gap note. It must not be read as earlier evidence, approval, gate passage, instituting speech act, `U.Work` occurrence, release permission, engineering justification, or assurance for the unsupported past claim or effect.

#### E.17:5.1b - Shared source-support posture vocabulary

Use this vocabulary when a publication face, rendering, generated text, comparison note, narrower-use rendering, source-finding cue, or authority-looking display may be over-read as carrying wider source support than it actually carries. The vocabulary names support posture for one claim or use. It does not instantiate evidence, gate, assurance, work, commitment, speech act, decision, release, or authority.

| Source-support posture | Meaning for the local claim or use |
| --- | --- |
| `source-pointer-only` | The item points to a possible source but does not show that the source is available, was used, or supports the claim. |
| `source-support-unknown` | The item does not yet show whether the needed source relation exists or supports the local claim. This blocks the downstream use until checked; it does not show that the underlying world claim is false. |
| `source-support-not-needed` | No operative work, reliance, evidence, gate, assurance, bridge, source-dispute, release, or durable-naming claim is live for this item. Orientation, learning, source-finding, review, or planning preparation may proceed without inventing source support. |
| `source-not-recoverable-here` | The needed source relation may exist elsewhere, but it is not recoverable from this publication-facing item or its stated source anchors. Treat the item as orientation or source-finding only, or reopen the source-bearing side. |
| `source-support-absent` | The needed source relation is known absent from the current item and available source set for the stated use. Block that use; do not infer that the underlying world claim is false merely from this absence. |
| `source-available` | The cited source can be recovered or inspected for the current use. This does not yet show that the rendering used it correctly. |
| `source-retrieved` | The cited source has actually been recovered for the current check. This still does not show that it was used correctly or supports the local claim. |
| `source-used` | The inspectable generation, rewrite, rendering, comparison, work, or reliance source-use relation actually used the named source rather than only similar background. If that relation is unavailable, treat the item as pointer-only or orientation-only until a source-use relation is recovered. |
| `source-faithful` | The item stays within the source claim relation or source support relation for the stated use; omissions, declared source-loss modes, and additions are visible enough to inspect. |
| `claim-supported` | The local claim is recoverable from the source, declared correspondence support, or required exact typed project-side value and reference for the stated use. |
| `claim-unsupported` | The local claim is not recoverable from the source support currently available. |
| `claim-contradicted` | The local claim conflicts with the available source support. |
| `claim-plausible-only` | The claim may sound reasonable, but the source support currently available does not carry it. |
| `source-omitted` | Relevant source claim, source passage, qualifier, condition, alternative, caveat, or uncertainty is missing from the item. |
| `source-loss-declared` | The item declares a source-loss mode such as omitted-detail, qualifier-loss, redaction, aggregation, scope-narrowing, recoverability-loss, representation-factor-loss, or coarsening-loss for the local source-to-rendering relation. |
| `claim-widened` | The item turns a source possibility, hypothesis, bounded condition, low-confidence statement, narrower permission, or source-finding cue into a wider claim or use. |
| `added-linkage` | The item adds a causal, explanatory, bridge, comparison, work, evidence, gate, or authority relation not already carried by the source support. |
| `independent-verification-present` | A separate check supports the local claim or use independently of the item only through a named governing pattern and exact record, such as an `A.10` evidence path, `B.3` assurance claim, `A.21` `GateDecision`, `A.20` constraint profile, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, or `F.9` Bridge Card. |
| `admissible-for-this-use` | The item is admissible for the named use only; wider downstream use still needs the exact neighboring FPF pattern and exact typed project-side value and reference. |
| `downstream-use-forbidden` | The item must not be used for the named downstream claim or effect because the needed source support is absent, source-loss-declared, contradicted, or outside scope. |
| `reopen-trigger-present` | A stated change, dispute, use escalation, source update, context shift, missing support, or contradiction forces return to the source-bearing side or to the governing FPF pattern and exact typed project-side value and reference. |

Patterns may use shorter local field names such as `sourceSupportPosture`, `explanationSourcePosture`, or `representationValiditySupportPosture` when the local object is clear. Comparative patterns split source-support posture from comparative-relation posture instead of using one overloaded field. The local field must still be interpretable through the vocabulary above, and the admissible use must be named beside it when downstream reliance could change.

For ordinary use, only name the posture distinction that changes the next admissible use. The common light states are `source-pointer-only`, `source-support-unknown`, `source-support-not-needed`, `source-not-recoverable-here`, `admissible-for-this-use`, `downstream-use-forbidden`, and `reopen-trigger-present`. The vocabulary is not an ordered scale, maturity ladder, source-record taxonomy, authority-reference source taxonomy, or project-side support substitute. If source support is missing from the publication-facing item, only the unsupported downstream use is blocked; the missing support does not by itself prove the underlying world claim false. If `independent-verification-present` is relied on, name the separate governing pattern and exact record that performs that independent support: `A.10` evidence path, `B.3` assurance claim, `A.21` `GateDecision`, `A.20` constraint profile, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, or `F.9` Bridge Card.

#### E.17:5.1c - Shared use-boundary terms

Use these terms when a publication face, rendering, narrower-use rendering, explanation, comparison note, source-finding cue, or authority-looking display may be read beyond the support it carries. Define them once here and link back to this section from local patterns instead of minting local synonyms.

| Term | Meaning for FPF use |
| --- | --- |
| `orientation use` | The item helps a reader find, inspect, triage, compare, teach, discuss, or prepare planning while the item itself does not support a downstream work, reliance, claim, or effect. |
| `reliance use` | The item is used as support for an engineering claim or effect that changes a next work or reliance move, such as method choice, work plan, performed-work claim, release, gate, approval, role or status, evidence, assurance, or external-impact move. |
| `work, reliance, claim, or effect` | A claim or instituted effect about method selection, selected method, `U.WorkPlan`, performed `U.Work`, work result, gate or release, role or status, evidence, assurance, boundary or policy effect, or another exact typed project-side value and reference. |
| `operative claim` | A claim whose acceptance would change the next admissible work or reliance move, the exact typed project-side value and reference to recover, or the cross-context use of the item. Explanatory prose, examples, and source-finding cues are not operative claims unless they are used that way. |
| `non-admissible downstream use` | A wider use that the current item source relation does not carry. It requires narrowing the use, returning to the source-bearing side, recovering source support, or using the exact neighboring FPF pattern and exact typed project-side value and reference that governs the wider claim or effect. |
| `reopen trigger` | A dispute, use escalation, missing, stale, or contradictory source support, source update, context or window change, or wider claim or effect that requires source-bearing return, source refresh, re-expansion, or use of the governing pattern. |
| `authority-looking case` | A recognition phrase for an encountered item that may be over-read as permission, approval, evidence, gate passage, role or status, work occurrence, assurance, or release support. It is not a `U.*` kind, not an exact typed project-side value and reference, and not a governing pattern. |

#### E.17:5.1d - Compact Boundary Aid For The Live Claim or Effect

When a publication-facing item, publication face, rendering, narrower-use rendering, explanation, comparison note, dashboard tile, credential view, status view, carrier, or generated item creates more than one possible reading, separate the live claim or effect being used now and cite the exact governing source relation for that claim or effect. This is a compact boundary aid, not a standing selection guide, project process order, software call path, or item taxonomy. The same encountered item may expose several typed records; handle one live claim or effect at a time instead of pretending there is one overall governing relation for the encountered item.

**Mixed-case precedence.** When several publication-use patterns appear possible, repair the smallest unstable reading that changes the current admissible use before applying a neighboring pattern whose claim or effect is live:

1. If one local head is the only unstable part, apply `E.17.AUD.LHR` or `E.10.SEMIO` and stop when the repaired sentence names the local kind, relation, and admissible use.
2. If the bounded `PublicationUnit` or its primary described-entity reading is unstable, apply `E.17.AUD` or `E.17.AUD.OOTD` before using `E.17.ID.CR` or `E.17.EFP`.
3. If the unit is stable and the live problem is comparison overread, apply `E.17.ID.CR`; use `F.9`, `C.11`, `A.20`, or `A.21` only when equivalence, recommendation, selection, decision, gate, or release claim is actually live.
4. If the unit is stable and the live problem is explanation overread, apply `E.17.EFP`; use `A.10`, `B.3`, `A.20`, `A.21`, or `A.15.4` only when evidence, engineering-justification, gate, release, work, or reliance claim is actually live.
5. If the live problem is a durable reusable name, UTS row, Core-facing term, or cross-context naming relation, apply `F.18`; otherwise keep the lighter local repair pattern.

| Live claim or effect question | Apply or recover |
| --- | --- |
| Is the item being used to guide a work or reliance move by appearance, while the acting user still needs the exact typed project-side value and reference before proceeding? | `A.15.4` for the restoration step; the recovered value may then be `A.15`, `A.15.1`, `A.10`, `B.3`, `A.20`, `A.21`, `A.2.8`, `A.2.9`, `A.6.B`, or another exact typed project-side value and reference. If that exact value is already the live question, use it directly. |
| Is the item being used as evidence, provenance, attestation, currentness, freshness, or claim-bound support? | `A.10` evidence, provenance, or currentness path for the exact claim. |
| Is the item being used as engineering justification, assurance, confidence, readiness, or limitations support? | `B.3` assurance or engineering-justification claim with evidence, limits, and decay explicit. |
| Is the item being used as gate passage, constraint validity, adjudication, or release decision support? | `A.20` or `A.21` project records, including gate profile, constraint profile, decision record, log reference, scope, window, replay support, and freshness support. |
| Is it the same described entity with textual restatement only? | `A.6.3.CR Conservative Retextualization`. |
| Is it the same described entity with representation scheme or reasoning medium changed? | `A.6.3.RT Representation Transduction`. |
| Is it deliberately reduced-use and useful only under narrower admissible use, non-admissible downstream use, and source-bearing reopen? | `A.6.3.CSC Controlled Semantic Coarsening`. |
| Is the primary issue explanation-facing rendering class on an existing MVPK face? | `E.17.EFP ExplanationFaithfulnessProfile`. |
| Is the primary issue one bounded comparative review unit over sources? | `E.17.ID.CR ComparativeReading`. |
| Did the described entity, target, ontology frame, or governed claim change? | `A.6.4`, `OntologicalReframing`, or the exact retargeting or reframing pattern. |
| Is the item being used as bridge, substitution, equivalence, "same", "equivalent", "align", or "map" wording, or cross-context comparison support? | Use Part F and `A.6.9` for repairing "same", "equivalent", "align", or "map" wording into explicit bridge work; use `F.9` or `F.9.1` for Bridge Cards, bridge kind, direction, `CL`, loss notes, admissible use, and stance overlays. Comparison alone is not a bridge. |
| Is the live question carrier, export, OCR, screen, front-end behavior, or work on carriers? | `A.7` and the exact carrier relation, front-end relation, or work-on-carrier record. |

**Evidence-path boundary.** An `A.10` evidence, provenance, attestation, freshness, or currentness path supports only the exact claim it instantiates. It does not approve or authorize work, pass a gate, perform work, supply release permission, or raise assurance or engineering-justification posture unless the exact typed project-side value and reference that carries that downstream claim is also instantiated, such as `A.15.4`, `A.15`, `A.20`, `A.21`, or `B.3`.

**Gate-display boundary.** A dashboard tile, status view, or release screen may expose a gate decision only when the `GateDecisionRef`, gate or constraint profile version, target release or work scope, time window, currentness, freshness or replay support, and evidence path are recoverable. Without that exact gate support, the display remains orientation or source-finding only; it is not a gate decision, gate passage, release permission, or performed-work record by color, label, layout, or proximity.

#### E.17:5.1e - Local review fields are not FPF kinds

Local review fields and values in CR, RT, CSC, EFP, ID.CR, or a neighboring publication-use pattern are local review aids for one case. They are not `U.Kind`, `SurfaceKind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `SlotKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, publication face, `authoritySourceRef` target, or exact typed project-side value and reference unless another governing FPF pattern explicitly instantiates that object. When a local field starts carrying one of those downstream claims, cite or apply the governing FPF pattern and exact typed project-side value and reference that carry it.

#### E.17:5.1f - Shared anti-overread invariants for publication-facing items

Use the exact FPF pattern that governs the live claim or effect. Keep any local review field local, preserve reduced admissible use, and assign only the non-admissible wider claim or effect to its governing source relation.

**Source-relation minimality.** Name the smallest exact FPF source relation sufficient for the live use. A source pointer, source-exposure relation, evidence path, engineering-justification record, gate decision, and release decision are different FPF relations; choosing one does not license another. Do not apply `A.10`, `B.3`, `A.20`, or `A.21` when the live use only needs source finding, orientation, or inspection of an existing source `U.Episteme`, source `U.EpistemePublication`, or status-register entry.

**Local repair vs publication redesign.** A local semantic repair is enough only when it can preserve the current publication face or `PublicationUnit` while fixing one head, boundary, source relation, admissible use, explanation class, or unsupported downstream claim. If layout, grouping, visual emphasis, comparison arrangement, generated explanation, hidden source limitation, or mixed described-entity packaging still induces overread after the local relation is repaired, create a redesigned publication face or `PublicationUnit` instead of adding warning text around the misleading form.

**Most-likely careful reading constraint.** Design and word a publication-facing item so its most likely careful reading does not exceed its named source relation, admissible use, and governing FPF pattern. A visible head such as `Approved` needs a visible `GateDecision` or a different head; a sorted comparison needs its comparator or sorting basis visible if no recommendation claim is intended; a generated explanation separates inferred links from pinned source claims by wording, label, or source anchor.

**Visual cue claim pressure.** Layout, order, color, prominence, icon, grouping, and proximity are carrier or front-end cues that can carry publication-move pressure even when the words do not. Green color may imply readiness, top position may imply preference, grouping may imply equivalence, proximity to evidence may imply support, a badge form may imply approval, and a lock or checkmark may imply verification. If the visual cue would make the reader treat the item as evidence, gate passage, decision, recommendation, reliance support, bridge support, or approval, recover the exact governing FPF pattern and exact project-side kind and reference, or redesign the publication face so the overread is no longer invited.


**Extraction survival.** When a `PublicationUnit` is excerpted, quoted, screenshotted, summarized, copied into a tutorial, retold by a generator, or moved to a slide, it keeps only the claims, source pins, boundary line, exact references, and admissible use carried in that extracted item. Any use that depended on hidden neighboring context is lost unless that context is carried by source pins, a boundary line, or an exact reference. A dashboard screenshot does not carry the underlying gate record, a quoted comparison row does not carry the full comparison basis unless the basis is included or referenced, a copied explanation paragraph does not carry source pins unless pins remain recoverable, and a pattern excerpt does not carry the whole pattern boundary unless the excerpt states or cites it.






**No-extra-pattern case.** If a publication-facing item only supports ordinary orientation, learning, source-finding, review, comparison, or planning preparation, and no operative work or reliance, evidence, gate, assurance, bridge, source-dispute, or release claim is live, keep the existing publication source relation and proceed with ordinary use. The visible closure may be: no operative work or reliance, evidence, gate, assurance, bridge, source-dispute, release, durable naming, or project-side support claim recovered; ordinary publication wording remains admissible for the current use.

**Pattern-inflation anti-pattern.** Do not apply a neighboring pattern merely because the publication-facing item resembles a worked example. Apply the neighboring pattern only when a live claim or effect changes the next admissible project move.

**Strategic overread invariant.** Apply the same anti-overread rules whether the misleading reading is accidental, conventional, incentive-driven, or intentionally induced by publication design. Green status color without `GateDecisionRef`, reviewed-looking wording without approval, selective source links without operative-claim support, comparison ordering without selection decision, hidden caveats behind a source link, or pins for trivial claims beside unpinned causal linkage do not create evidence, gate, decision, assurance, work, release, or bridge support by design pressure.

**Carrier-travel invariant.** A copied, exported, screenshotted, summarized, generated, translated, or re-rendered publication-facing item may carry orientation or source-finding cues. It does not carry evidence support, authority-reference support, gate passage, approval, engineering-justification support, work occurrence, currentness, or release support unless the governing FPF pattern and exact typed project-side value and reference remain recoverable for that exact use.

**Derivative-chain decay.** A second-order rendering inherits at most the admissible use that is explicitly carried from the prior source relation. It does not inherit source faithfulness, source support, currentness, authority-reference support, gate support, work support, or reliance support by default.

**Publication-face snapshot and refresh identity.** A publication face may keep the same visible layout, face name, or carrier while its source pins, source data window, source-support posture, freshness or currentness support, `EditionId`, or admissible use changes. Visual sameness across time is not source, evidence, or use-boundary sameness. When a refreshed, revised, translated, regenerated, screenshotted, or re-rendered face is used beyond orientation or source-finding, name the face edition or snapshot, the source pins or data window that still carry the claim, and any changed admissible use. If those cannot be recovered, treat the face as orientation or source-finding only, or reissue the face under the governing pattern before work, evidence, gate, assurance, release, or reliance use continues.

**Claim-level support only.** Do not assign one whole-item support posture unless every operative claim in that publication-facing item has the same support relation for the same use and non-admissible downstream uses are explicit.

**Modality and deontic-force preservation.** Publication-facing transformations must preserve possibility, obligation, permission, recommendation status, decision status, confidence, scope, and temporal window when those are load-bearing. If one of these changes, narrow the admissible use or apply the governing pattern that carries the changed claim or effect. Comparison does not become recommendation or decision; explanation does not become evidence; a publication face does not become authority; a publication unit does not smuggle a downstream effect; source-linked does not mean source-supported for reliance; ready-looking does not mean gate-passed.

This preservation rule also applies across extraction, translation, screenshotting, summary, and generated retelling. A translated permission is not wider permission, a screenshot of approval-looking display is not an approval record, a summary of evidence is not an evidence path, and a generated retelling of a decision is not the decision record unless the exact governing source relation and source pins survive in the new publication-facing item.


**Reader position is not project role.** Reader position, audience, target user model, verifier position, reviewer position, and learner position do not become project roles, role assignments, decision authority, gate authority, issuer roles, or work roles unless a typed project-side value and reference instantiates that role relation.

**Source-gap states.** When support is missing, say which gap is live: source not named; source named but unavailable; source available but not used; source used but insufficient; source stale or outside its window; source contradicted; source accountable role or register mismatch. Block only the unsupported effect and keep any reduced admissible use available.

**Measure and display overread.** A number, score, percentage, color, rank, confidence value, similarity value, dashboard state, or measurement display is orientation only until the measurement source, aggregation rule, validity window, population or scope, calibration or evidence path, and intended use are governed by the exact typed project-side value and reference. Evidence-like use applies `A.10`; assurance-like use applies `B.3`; gate-like use applies `A.20` or `A.21`; work or reliance use applies `A.15.4` and then the recovered exact typed project-side value and reference; bridge or substitution use applies `F.9` or `F.9.1`.


**World-contact stop.** Publication-facing items do not self-refresh after source update, revocation, policy change, system-state change, incident, model update, environmental change, or new external observation. A live outside change requires source refresh, reissued publication, or a new governed exact typed project-side value and reference before work, evidence, gate, control, carrier, or other downstream use continues.

**Functional-description boundary.** A functional, architectural, descriptive, representational, or explanatory fit claim does not create permission, obligation, approval, gate passage, release support, performed-work evidence, or engineering justification. Those uses require the exact neighboring FPF pattern and exact typed project-side value and reference.

**Mixed bundle no-shared-evidence-support rule.** A bundle with source-pinned, reduced-use, speculative, didactic, comparison, and evidence-facing parts cannot be read under one shared evidence-support class or admissible-use posture borrowed from another member. Each operative claim keeps its own source relation and non-admissible downstream use.

**Educational usefulness.** Didactic, onboarding, tutorial, and workshop usefulness is real orientation support. It is not evidence, gate passage, approval, work occurrence, engineering justification, release permission, or bridge support.

**Comparison exposes conflict; it does not adjudicate it.** A comparison note may expose contradiction, asymmetry, different foregrounding, or unresolved residue. It does not settle the conflict, select an option, approve release, pass a gate, or create bridge or substitution support unless the exact neighboring FPF pattern and exact typed project-side value and reference carry that result.

**Same publication-facing item, multiple readings.** A green release dashboard can be one MVPK face for source-finding, an `A.10` currentness path or evidence path when the evidence query is recoverable, an `A.21` gate-decision view when the `GateDecisionRef` is recoverable, or an unsupported release cue when those sources are missing. A generated comparative explanation can be an `E.17.EFP` explanation-use case, an `E.17.ID.CR` comparison case, a `A.6.3.CR` generated-summary case, or source-finding only; it is never all of those under one shared evidence-support class or admissible-use posture by fluency alone.

**Archetypal publication-use cases.** Use these as quick recognition slices, not as a closed taxonomy:

- **Green dashboard tile.** A tile says `Model ready`. Treat the tile as the `PublicationUnit` when that tile carries the live release overread. The useful action is source-finding and status orientation unless an exact `GateDecisionRef`, gate profile, source relation, and evidence or currentness support are recoverable. Without those, the tile is not release permission or gate passage by green color or placement.
- **Generated explanation with source links.** A generated text explains a method and cites sources. The explanation rendering is not source replacement. Source links support only the pinned operative claims they actually carry. If work or reliance is live, use `A.10` for the exact evidence path or keep the rendering as reader help; if the rendering is deliberately reduced-use, use `A.6.3.CSC`.
- **Comparison table.** A table compares two methods and places one first. Ordering is not selection. The comparison basis, source anchors, shared review frame, and unsupported downstream claim remain visible. Choice or decision needs `C.11`; equivalence or bridge support needs `F.9` or `F.9.1`.
- **Unrecovered source wording.** A draft uses source-object wording, support-view shorthand, or generic unit wording without naming the FPF kind. Recover the FPF kind stack instead of minting support-object or support-view pseudo-kinds. Use `PublicationUnit` only when a bounded reader-inspected unit inside a publication is live; otherwise use the exact episteme, view, publication, carrier relation, section of a named non-pattern FPF publication form whose support function and reference are recoverable, `A.6.P` relation claim, or exact typed project-side value and reference.

- **Translated tutorial.** A translated tutorial may improve reader access to an FPF pattern. It is a derivative rendering, not the original source. Operative claims need source mapping for reliance, translated heads may need `E.17.AUD.LHR` or `E.10.SEMIO`, and `F.18` is live only when durable naming, UTS, Core-facing, or cross-context naming work is intended.

**Practical harm prevented by neighboring pattern.** Use this map when the reader asks what the discipline buys in practice:

**Blocked overread with useful action remaining.**

- A comparison table appears to select option B. Block the selection reading when no `C.11` `ChoiceResult`, decision record, or visible selection basis exists. Useful action remains: use the table as a bounded comparison under `E.17.ID.CR`, or apply `C.11` when selection is intended.
- A green dashboard tile appears to permit release. Block the release or gate-passage reading when no `GateDecisionRef`, gate profile, evidence or currentness support, and source relation are recoverable. Useful action remains: use the tile for source-finding and status orientation, then inspect the exact gate or evidence source if release work is intended.
- A generated explanation appears to prove a causal relation. Block the evidence or assurance reading when source pins and evidence path are absent or insufficient. Useful action remains: use the explanation as reader help or source-finding, then apply `A.10` or `B.3` only for the exact evidence or engineering-justification claim they govern.


- `E.10.SEMIO` prevents the wrong object from being treated as source, the wrong relation from being treated as support, and a loose phrase from being treated as an FPF kind.
- `E.17.AUD` and `E.17.AUD.OOTD` prevent action on a publication unit whose primary described entity, carried publication move, or outside boundary shifted silently.
- `E.17.ID.CR` prevents a comparison unit from being used as decision, equivalence, bridge, evidence, or release basis.
- `E.17.EFP` prevents fluent explanation from laundering unsupported claims into reliance, assurance, gate, or evidence use.
- `E.17` MVPK prevents a readable publication face from being treated as evidence, gate, work, authority, or release support by display quality.
- `F.18` prevents a local name from becoming global identity without context, kind, lineage, and bridge or cross-context naming support.

**Anti-escalation examples.** Do not apply a neighboring pattern when its live claim is absent:

- Do not apply `F.18` when a one-off local phrase repair restores the local kind, relation, and admissible use without minting a durable reusable name.
- Do not apply `A.10` when the publication-facing item is not being used for reliance, evidence, provenance, currentness, or claim-bound support.
- Do not apply `A.21` when a dashboard tile is merely status orientation and no `GateDecisionRef` or gate profile is live.
- Do not apply `F.9` when a comparison does not claim sameness, substitution, bridge support, or cross-context equivalence.
- Do not apply `E.17.EFP` when the text is only a same-entity rewrite or representation change governed by `A.6.3.CR` or `A.6.3.RT`.

**Concrete reopen trigger.** A reopen trigger must name the condition and the nearest source-bearing side or governing pattern. A vague "reopen if needed" does not preserve source support.

#### E.17:5.2 - Allowed `SurfaceKind` values at Part E (L-SURF discipline)
Part E restricts `SurfaceKind` values to **PublicationSurface** and **InteropSurface**. Concrete publication faces SHALL be named **...View**, **...Card**, or **...Lane**.

**USM linkage (normative).** Every `U.View` **SHALL** declare a `U.PublicationScope` (USM §6.5).
For a view **about an episteme** `E`: `PublicationScope(view_E) ⊆ ClaimScope(E)`.
For a view **about a capability** `C`: `PublicationScope(view_C) ⊆ WorkScope(C)`. This is the publication scope of a capability description, not permission to perform work and not evidence that work occurred. Work admissibility still requires `A.15.4` source restoration when the view is used for work or reliance, and the `A.15` role, method, plan, and work source relation for the actor, target, context, scope, and time window in use.
Cross‑context views **SHALL** cite Bridge + CL; **CL penalties apply to R only** (scope membership unchanged).

**L‑PUBSURF naming discipline**
 * Allowed `SurfaceKind` values: **PublicationSurface**, **InteropSurface**.
 * Concrete faces MUST be named **...View**, **...Card**, or **...Lane**.
* The tokens **carrier, bearer, and holder** MUST NOT name a `U.View` or any publication entity.
  Use **`U.View`** (PlainView, TechCard, InteropCard, or AssuranceLane) for conceptual publication faces.
  Reserve **carrier** exclusively for **SCR/RSCR** (symbol, document, or data carriers) and **`U.Work` on carriers**.
* Avoid geometric metaphors such as axis or dimension for publication forms; use **Characteristic** or **CharacteristicSpace** only when referring to CHR‑MM entities.
* **Non‑collision guard.** `ViewFamilyId` (lexical tag for viewpoint families) MUST NOT be used to name any `U.View` or `SurfaceKind`; MVPK face kinds remain **{PlainView, TechCard, InteropCard, AssuranceLane}** only.

**MVPK‑Max viewpoints (normative; exactly four; governed by the MVPK profile):**
* `PlainView` (explanatory prose view)
* `TechCard` (typed catalog card)
* `AssuranceLane` (evidence bindings and lanes)
* `InteropCard` (conceptual interoperability view; **mapping to concrete exchange formats lives in the interop annex; Part E does not specify schemas**)

`AssuranceLane` may expose evidence bindings, evidence-carrier references, pins, and presence bits. It is not a `B.3` assurance claim, readiness or confidence verdict, engineering-justification record, or evidence-sufficiency result. When a published face is used to raise or lower assurance, readiness, confidence, limitation, or engineering-justification posture, the governing source relation is `B.3`; the lane only helps recover the cited evidence bindings.

**Lean profiles (small‑team friendly, optional; as MVPK kit profiles):**
* **MVPK‑Min (F0–F1):** Σ = {`PlainView`, `TechCard‑Lite`}. `AssuranceLane` omitted. No interop face.
* **MVPK‑Lite (F1–F3):** Σ = {`PlainView`, `TechCard‑Lite`, `AssuranceLane‑Lite` gated by crossing trigger}. `InteropCard` only if external consumers exist.
* **MVPK‑SetReady (F3–F5):** add `InteropCard` when replayability or external interchange is required (details outside Part E).
* **Profile‑upgrade triggers:** (i) cross‑Context reuse or ReferencePlane crossing; (ii) QD replay needs or OEE replay needs; (iii) external consumption.
* **“‑Lite” variants (definition):** A *‑Lite* face removes optional fields only (never claims), keeps the same typing as its full counterpart, and MUST retain pins for any numeric content. Upgrading from *‑Lite* to full is a monotone **add‑fields** operation (no retractions).

#### E.17:5.3 - The kit (constructs)

1. **Object component** `ViewObj_s` for each viewpoint (see §5.1), to make types explicit.
2. **Viewpoint set** `Σ : FinSet(U.Viewpoint)` with declared **partial order** `⪯` for formality or refinement (default chain: `PlainView ⪯ TechCard ⪯ InteropCard`; `AssuranceLane` is an **independent evidence-binding face** and not ordered with respect to others).
3. **Emitters** `Emit_s(-) : U.Morphism → U.ViewMorph_s` (one per `s ∈ Σ`).
4. **Coherence** (rules and invariants §6) + **Pin Characteristics** policy (UnitType, ScaleKind, ReferencePlane, and EditionId) for any numeric or comparable content, grounded in CHR and UNM.
5. **Interop anchors (conceptual)** for `InteropCard` (concerns and semantics only); **any concrete schema or exchange mapping is outside Part E** (Annex or Interop).

**Result:** `MVPK(f, Σ)` returns `U.ViewFamily(f)` whose components are `Emit_s(f)`. Reindexing across `s ⪯ t` is mediated by total view-object coercions `PromoteView[s→t]_X` (see §6.2).

#### E.17:5.4 - Intensional Input and Output vs Publication (normative convention)
1) **Input and Output are intensional.** The **Input and Output** sections of a morphism describe **intensional** data types (I, D, and S) only; they do **not** depend on any publication face.
2) **No duplication on faces.** MVPK faces **do not duplicate** Input and Output lists; they publish a **minimal profile**: **presence‑pins**, **CG‑Spec and CHR anchors**, and **EditionId** only.
3) **Signature reserved to intensional.** Use **“Signature”** exclusively for intensional objects (`U.Signature`, `U.PrincipleFrame`, …). On faces, avoid “signature” and use **TechName** or **PlainName**.
4) **Admissible orders, return sets.** Whenever a face shows **selection or comparison**, it **returns sets or admissible partial orders** and **never hides scalarization**; cite a **ComparatorSetRef** for any total order.
5) **Bridge crossing penalties.** Crossings cite **Bridge and CL**; publish **Φ(CL)** and **Φ_plane** ids; penalties apply to **R only** (never F or G).
6) **Carrier anchoring and lanes.** On first mention, anchor carriers (**SCR/RSCR**); keep **Work occurrences** distinct from **epistemic claims** via lanes.
7) **Publication ≠ execution.** No time or resource semantics on faces; any build, render, or upload work is separate **`U.Work`**.

#### E.17:5.5 - Pin & Publication characteristics (normative; never “axes”)
**Intent.** Make pinning and publication-time measurement claims explicit, typed, and auditable without importing geometric metaphors. This section introduces **Publication characteristics** (PC) as CHR-grounded, publication-facing facets that can admissibly appear on MVPK faces.

**Terminology (aligned with CHR‑MM & UNM).**
* **Characteristic** (`U.Characteristic`): a measured aspect as defined in CHR‑MM (entity characteristic or relation characteristic with a chosen **Scale**).
* **CharacteristicSpace** (`U.CharacteristicSpace`): a CHR‑typed product of slots used by dynamics and measurement theories (A.19).
* **Publication characteristic** (`U.PubCharacteristic`, **PC**): a **declarative facet** that a view, card, or lane may expose *about a morphism* under a stated **Viewpoint**. Each PC is **backed by** CHR and CG‑Spec publications and **pinned** by unit, scale, reference‑plane, and edition. PCs are **not** geometry and do **not** define “axes”.

**PC catalog (initial set).** MVPK defines a minimal open set of PCs that are frequently shown on publication faces:
* **PC.Number** — numeric or comparable entries (thresholds, budgets, counts). **Pins required:** unit, scale, reference‑plane, edition.
* **PC.EvidenceBinding** — bindings to evidence carriers and policies (e.g., PathSliceId, BridgeId, CL notes).
* **PC.ComparatorSetRef** — an explicit comparator family for admissible partial orders on faces.
* **PC.CharacteristicSpaceRef?** — optional pointer when a face needs to cite the **space** in which a claim is interpreted (e.g., dominance on a declared space).
The catalog **MAY** be extended (see “Extensibility” below); PCs **must** remain declarative (no embedded mechanisms).

**Norms (E17‑PC).**
* **E17‑PC‑1 (CHR grounding).** Every PC that yields numeric or comparable content **SHALL** cite CHR and CG‑Spec anchors and carry pins {unit, scale, reference‑plane, edition}.
* **E17‑PC‑2 (Lexical discipline — no geometry).** Faces and PCs **MUST NOT** use “axis”, “dimension”, or geometric metaphors; use **Characteristic**, **slot**, **CharacteristicSpace** where applicable (**E.10**; see also A.19).
* **E17‑PC‑3 (No hidden arithmetic).** Faces **MUST NOT** smuggle aggregation or normalization; any such logic lives in **CG‑Spec** (UNM or NormalizationMethod) and is cited by **…Ref.edition**.
* **E17‑PC‑4 (Plane & crossing).** When a PC depends on **ReferencePlane** or crosses ReferencePlane crossings or Context crossings, the face **SHALL** cite `BridgeId` and **CL** policy‑ids; penalties apply to the **R‑channel only**.
* **E17‑PC‑5 (Edition pinning).** PCs that rely on maps or distances **SHALL** pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and, if used, both `CharacteristicSpaceRef.edition` and `TransferRulesRef.edition`.
* **E17‑PC‑6 (Viewpoint scope).** Each PC instance declares the **Viewpoint** under which it is valid; promotion `PromoteView[s→t]` **MUST NOT** add or widen claims; at most, it reindexes or annotates.
* **E17‑PC‑7 (Comparator or SetSemantics edition).** `PC.ComparatorSetRef` and any `SetSemanticsRef` **SHALL carry edition identifiers**; cards MUST be re‑emitted upon edition change with migration notes.

**Publication faces and responsibilities.**
* **PlainView** MAY include **PC.Number** iff fully pinned; otherwise it uses **compare‑only** language.
* **TechCard** SHOULD carry **PC.Number**, **PC.ComparatorSetRef**, and **PC.CharacteristicSpaceRef?** when faces enable admissible ordering.
* **AssuranceLane** SHALL carry **PC.EvidenceBinding** and the pins for any numeric claims it relays.
* **InteropCard** MAY reference PCs conceptually but SHALL remain notation‑neutral in Part E (schemas map in the interop annex).

**Rationale.** MVPK is a publication discipline, not a measurement calculus. By naming **Publication characteristics** and pinning them to CHR and UNM, we:
1) prevent geometric leakage (no “axes”);
2) keep publication neutral yet auditable;
3) enable admissible set and ordering behavior on faces via explicit **ComparatorSet**;
4) make plane-crossing requirements first-class and checkable by declared publication checks or **OperationalGate(profile)** GateChecks.

**Extensibility.**
* **E17‑PC‑Ext‑1 (Open catalog).** New PCs MAY be added under `U.PubCharacteristic` provided they are declarative and CHR- and UNM-grounded.
* **E17‑PC‑Ext‑2 (Kinding).** New PCs MUST declare `kind ∈ {Number, EvidenceBinding, SelectorHint, ...}` and a **pinning requirement**.
* **E17‑PC‑Ext‑3 (Twin‑register names).** Supply **Tech** and **Plain** twins; avoid tokens that collide with E.10 bans; do not coin “…Space” names for publication forms.
* **E17‑PC‑Ext‑4 (Edition discipline).** If a PC depends on a definition or specification publication, **edition‑pin** the reference (`…Ref.edition`) and document migration rules.

**Adding invariants.**
1) Place **new invariants** for PCs in **CG-Spec** (specification lane), not on faces; supply acceptance tests.
2) Version any affected **CharacteristicSpace**; publish embeddings if semantics change; never mutate slots in place.
3) Update the relevant **GateChecks** or **GateProfiles** (`A.21`, including GateCrossing checks and crossing-visibility checks from `E.18`, `F.9`, and relevant Part G bridge or crossing wiring) to warn or block on invariant violations; never weaken functorial invariants.
4) **Document** edition and migration rules; extend §9 with a conformance item and provide **Lean‑profile downgrade** (advisory vs block) where applicable.

#### E.17:5.6 - Author ergonomics (non‑normative)
*Quick author steps (three steps and a micro-template):*
1. **Declare Σ and profile.** Choose `{PlainView, TechCard, …}` and whether faces are full or *‑Lite*.
2. **Pin once, reuse everywhere.** Attach `{UnitType, ScaleKind, ReferencePlane, EditionId}` to the arrow; cards reference these pins by ID (no duplication).
3. **Emit & verify.** Generate all faces from the arrow.

*Guidance:* treat *‑Lite* as **field‑drop only**; never add claims in *‑Lite*.

### E.17:6 - Rules and Invariants (normative)

**Publication-composition local test bundle.** A face that claims compositional publication passes only when five local tests are visible:

1. `identity`: `Emit_s(id_X)` is the identity view for `ViewObj_s(X)`.
2. `composition witness`: the published face for `g∘f` matches the composition of the published faces for `f` and `g`, or the face is marked non-compositional or explanatory-only.
3. `no-new-claim diff`: red-line against the governing D-side or S-side episteme shows formatting, indexing, pinning, or view-refinement work only.
4. `monotone promotion`: promotion from a plainer face to a richer face adds fields, pins, or typing without retracting or strengthening the source claim.
5. `scope non-widening`: `PublicationScope` stays within the relevant `ClaimScope` or `WorkScope`, and promotion does not widen it.



For any composable arrows `X —f→ Y —g→ Z` in `U`, and any `s, t ∈ Σ_viewpoints`:

1. **Functoriality & typing (per‑viewpoint).**
    * (a) **Identity:** `Emit_s(id_X) = id_{ViewObj_s(X)}`.
    * (b) **Composition:** `Emit_s(g∘f) = Emit_s(g) ∘ Emit_s(f)`. A face that claims compositional status carries a local witness: compare the published face for `g∘f` with the composition of the published faces for `f` and `g`. If the witness is absent or fails, mark that face non-compositional or explanatory-only and do not use it to satisfy the composition rule.

    * (c) **Typing (totality):** if `f : X → Y` then `Emit_s(f) : ViewObj_s(X) → ViewObj_s(Y)` is **total**; ill-typed composites must be fixed via `ViewObj_s`, not by weakening invariants.
    * *Intuition:* every viewpoint acts functorially on arrows; publication does not break arrow algebra.
2. **Reindexing coherence (monotone refinement + naturality).**
    * (a) If `s ⪯ t` then the `t`‑view **refines** the `s`‑view for the same morphism (**no content extension**; increased formality and typing only).
    * (b) For each `s ⪯ t` there are **object‑components** `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` natural in `X`, i.e., for every `f : X → Y`
      `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.
    * (c) **Coherence:** `PromoteView[s→s]_X = id_{ViewObj_s(X)}`, and if `s ⪯ t ⪯ u` then `PromoteView[s→u]_X = PromoteView[t→u]_X ∘ PromoteView[s→t]_X` for all `X`.
    * *Defaults:* `PlainView ⪯ TechCard ⪯ InteropCard`.
    * *Note:* `AssuranceLane` is independent of the formality chain; it binds **evidence‑about‑claims** and MUST NOT introduce new claims **of** the morphism.
3. **D-side and S-side sourcing and EpistemicViewing compatibility (A.7 and E.10.D2, A.6.2–A.6.3, E.17.0).**
    * (a) Inputs to `Emit_s(-)` are **existing D-side or S-side epistemes** about the same arrow (for example, `MethodDescription`, `MethodSpec`) produced by `Describe_ID` and `Specify_DS` or `Formalize_DS` in A.7 and E.10.D2. MVPK does **not** redefine or collapse these I→D→S morphisms.
    * (b) Each `Emit_s(-)` SHALL be realised as a species of `U.EpistemicViewing` (A.6.3) over those D-side or S-side epistemes: describedEntity‑preserving, effect‑free and conservative in the sense of A.6.2 and A.6.3. Publication adds no new commitments beyond what is present in the referenced D-side or S-side epistemes.
    * (c) Edition governance respects `U.EditionSeries` and UTS; rows remain the identity anchors for names; MVPK faces MUST be (re‑)emitted when the underlying D-side or S-side editions change.
4. **Pin discipline (Part F and Part G).**
     * Any numeric or comparable content in a view SHALL pin {UnitType, ScaleKind, ReferencePlane}. **EditionId MAY be coarse at Lean profiles**; if units and scale are unknown, **declare ordinal compare-only** and **forbid arithmetic** until CHR pins are available.  Pins upgrade monotonically with profile and risk.
5. **No Γ‑leakage (publication independence).**
    Publication morphisms carry **no** Γ\_method, Γ\_time, or Γ_work semantics. Any build, render, or upload activity is **separate `U.Work` by a system on carriers** (`A.7`).
     **Lean assurance lane:** `AssuranceLane‑Lite` MAY expose only presence bits for {PathId or PathSlice?, Γ_time window?, BridgeId?}; unknowns propagate (tri‑state) with an explicit {degrade|abstain|sandbox} policy note.
6. **Carrier provenance.**
    Every emitted view records its **SCR/RSCR ids** on first occurrence (A.7 §5.6).
7. **Isomorphism preservation.**
    * If `f` is an isomorphism in `U`, then `Emit_s(f)` is an isomorphism in `View_s(U)`; inverses map accordingly.
8. **Cross‑Context and ReferencePlane bridging.**
    * If a view crosses contexts or reference planes, it **SHALL** cite the **Bridge + CL policy ids** (A.7 §5.8, bridge crossing). Such crossings MUST be explicit on `TechCard` and `AssuranceLane`.
9. **Totality of publication morphisms.**
    * Publication maps are total on their domains; when a composition in a view would be ill‑typed, the author **must** fix the view-object mapping (via `ViewObj_s`) rather than weakening functoriality or reindexing rules.
10. **PublicationScope discipline (subset & composition).**
    * (a) **Subset rule:** If a view `v` is about episteme `E` then `PublicationScope(v) ⊆ ClaimScope(E)`; if about capability `C` then `PublicationScope(v) ⊆ WorkScope(C)` only as the publication scope of a capability description, not as work admissibility, gate passage, release permission, or evidence that `U.Work` occurred.
    * (b) **No widening by refinement:** If `s ⪯ t`, then promotion `PromoteView[s→t]` MUST NOT widen `PublicationScope`.
    * (c) **Compositional bound:** For composable arrows `X —f→ Y —g→ Z`,
      `PublicationScope(Emit_s(g∘f)) ⊆ PublicationScope(Emit_s(g)) ∩ PublicationScope(Emit_s(f))`.

### E.17:7 - Structure & participants
```
                 Σ_viewpoints
                      │
            ┌─────────┴─────────┐
            │                   │
        Emit_s(-)           Emit_t(-)      … (family)
            │                   │
U :  X ──f──▶ Y ──g──▶ Z    X ──f──▶ Y ──g──▶ Z
        U.ViewMorph        U.ViewMorph
            │                   │
        Emit_s(f),…         Emit_t(f),…
```
* **Author** chooses `Σ_viewpoints` (declared concerns + conformance rules).
* **MVPK** emits `U.ViewFamily(f)` for each arrow `f`.
* **Declared publication checks** verify that pins, anchors, and IDs are present and that MVPK invariants are respected. Use `OperationalGate(profile)` GateChecks only when a live project gate profile actually governs the next project move.

### E.17:8 - Examples (SoTA-aligned Local Tests)

Read these examples as local tests for MVPK invariants, not as source citations by reputation.


1. **Composite service pipeline (`InteropCard` + `AssuranceLane`).**
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability **view** whose path set equals the **relational composition** of the two cards; `AssuranceLane(g∘f)` cites test records as evidence **carriers** with edition pins. (Carriers, not semantics; concrete envelope formats are outside Part E.)
2. **Control loop morphism (`TechCard` + `PlainView`).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed stacks.)
3. **Optics-informed composition witness.**
    * Profunctor and optic accounts are useful only as a source idea for why compositional publication matters. The local FPF test is still the MVPK witness: emit the face for `g∘f`, compose the emitted faces for `f` and `g`, and compare them. If the comparison is not supplied or fails, the face stays non-compositional or explanatory-only; optics vocabulary does not carry the rule by analogy.

4. **Functional-description publication (`PlainView` + `TechCard`).**
    A principle scheme or functional diagram can publish a readable relation from signature or principle episteme content to method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement. The MVPK faces may help a team inspect that relation and prepare a work plan, but they do not turn the diagram, table, screen, or export into work occurrence, gate passage, evidence, engineering justification, or supervisory or control architecture. For those uses, the team first recovers the existing exact typed project-side value and reference that carries the claim when available: work-relevant source restoration under `A.15.4`, project `U.Method`, `U.WorkPlan`, and dated `U.Work` occurrence under `A.15` and `A.15.1`, evidence or provenance path under `A.10`, engineering-justification record under `B.3`, gate or constraint decision under `A.20` or `A.21`, or supervisory or control architecture record under `B.2.5`. If no existing source carries the needed claim, create only a prospective repair request, future decision request, prospective work-plan entry, or explicit source-gap note; do not backdate evidence, gate passage, work occurrence, release permission, engineering justification, or assurance for the earlier claim.


### E.17:9 - Conformance checklist (normative)

`CC-MVPK-FD` is the functional-description guard in §5.1a. It is conditional on a functional-description publication face and must not read as the first universal MVPK gate.

A conformance check is retained only if it changes the next admissible use of the publication face, blocks a concrete overclaim, or preserves a source anchor or reopen condition needed for the declared admissible use.

#### E.17:9.1 - Core ordinary checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC‑MVPK‑1 (Viewpoint explicit)** | Each view declares its **Viewpoint** (stakeholders, concerns, conformance) as a publication `U.Viewpoint`. | Cards show `PublicationVPId` (or equivalent publication‑viewpoint field) and concerns. |
| **CC‑MVPK‑3 (No content extension)** | `PlainView`, `TechCard`, and `InteropCard` add **no new claims** beyond the underlying D-side or S-side epistemes. | Red‑line vs D-side or S-side episteme output (`Describe_ID` or `Specify_DS`) shows only formatting or indexing. |
| **CC‑MVPK‑4 (Pins & anchors)** | Numbers and thresholds pin {...}. **Lean exception:** at MVPK‑Min or MVPK‑Lite profiles, EditionId MAY remain coarse; ordinal claims are admissible only as compare‑only (no means or z-scores). | Validation shows pins present or compare‑only mode engaged. |
| **CC‑MVPK‑4j (PublicationScope present)** | Each view **declares `U.PublicationScope`** (USM §6.5). | Field present; presence‑bit green. |
| **CC‑MVPK‑5 (Carrier anchoring)** | First mention includes **SCR/RSCR** ids when carrier work or rendering work is live. | SCR ids visible on the card when used. |

#### E.17:9.2 - Conditional checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC‑MVPK‑0 (Lean publication guard)** | For Lean profiles, a minimal guard runs: (i) set‑returning selection present; (ii) ReferencePlane present; (iii) any crossing cites BridgeId+CL with penalties applied to R only. | Validation report shows presence bits; penalties apply to R only. |
| **CC‑MVPK‑2 (Functoriality)** | `Emit_s(id)` is identity; `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)`. | Compose two cards and diff with the card of the composite. |
| **CC‑MVPK‑3b (Boundary claim‑set integrity)** | If a published arrow is a boundary, interface, or protocol and an A.6.B claim set exists (`L-*`, `A-*`, `D-*`, and `E-*`), then any normative text on faces **MUST** be traceable to that claim set (prefer claim‑ID citations); faces **MUST NOT** become a second boundary specification. | Lint flags uncited normative clauses; faces reduce to {claim‑ID citations + informative commentary}. |
| **CC‑MVPK‑4b (Lean assurance)** | If `AssuranceLane‑Lite` is used, presence bits for {PathSliceId?, BridgeId?} suffice; full evidence-carrier lists stay with the governing evidence source. | Presence bits visible; required evidence-carrier refs stay outside Lite. |
| **CC‑MVPK‑4c (Input and Output vs publication)** | Faces **do not** restate Input and Output; they carry **presence‑pins + anchors + EditionId** only. | Face inspection shows no Input and Output duplication. |
| **CC‑MVPK‑4d (Admissible orders)** | Any selection or comparison on faces **returns sets or admissible partial orders** with a **ComparatorSet** citation. | No hidden scalarization; ComparatorSetRef present. |
| **CC‑MVPK‑4e (Signature on faces — banned)** | The term **“signature”** is **not used** on faces; use **TechName** or **PlainName**. | Token scan: no “signature” on faces. |
| **CC‑MVPK‑4f (PC discipline)** | Any numeric or comparable publication uses **Publication characteristics** (PC) and carries pins {unit, scale, reference‑plane, edition}. | Cards show PC fields + pins; validation passes. |
| **CC‑MVPK‑4g (No axis or dimension)** | Faces avoid “axis”, “dimension”, and “plane” metaphors except **ReferencePlane**; use CHR terms (**Characteristic**, slot, or **CharacteristicSpace**). | Lexical check flags none; only `ReferencePlane` appears. |
| **CC‑MVPK‑4h (Edition pins on defs)** | Where maps, distances, or spaces are cited, the face pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition?`. | Validation shows edition fields populated. |
| **CC‑MVPK‑4i (Crossings gated)** | ReferencePlane crossings or Context crossings cite **Bridge + CL** policies; penalties apply to **R‑channel** only. | IDs present; R-channel penalty application verified in harness logs. |
| **CC‑MVPK‑4k (Subset‑of underlier)** | For views about epistemes or capabilities, `PublicationScope ⊆ ClaimScope or WorkScope`; reindexing **does not widen** it. | Subset witness passes; promotion diff shows no widening. |
| **CC‑MVPK‑6 (Γ‑separation)** | No cost, time, or data-spend on publication morphisms. | CI shows proof records or witness records; gate validation passes. |
| **CC‑MVPK‑7 (Reindexing monotone)** | If `s ⪯ t`, then `Emit_s(x) ⪯ Emit_t(x)`. | `TechCard` ≤ `InteropCard` (more structure, same claims). |
| **CC‑MVPK‑8 (`SurfaceKind` discipline)** | Only **PublicationSurface** or **InteropSurface** are used; faces are named **...View** or **...Card**. | Token scan; no “rendering” or “presentation” as `SurfaceKind` values. |
| **CC‑MVPK‑9 (Reindexing naturality)** | Reindexing coercions `PromoteView[s→t]` exist, are total, and commute with composition. | Witness shows `PromoteView[s→t]_Z ∘ Emit_s(g∘f) = (Emit_t(g) ∘ Emit_t(f)) ∘ PromoteView[s→t]_X`. |
| **CC‑MVPK‑10 (Iso‑preservation)** | Isomorphisms in `U` remain isomorphisms under each viewpoint. | Cards show mapped inverses or an iso‑witness. |
| **CC‑MVPK‑11 (Typing & totality)** | Ill‑typed composites are rejected at `ViewObj_s` rather than weakening functoriality. | Type‑check fails early; no “best‑effort” composition in cards. |
| **CC‑MVPK‑12 (Bridge+CL on crossings)** | Any cross‑Context view or ReferencePlane-crossing view cites **Bridge + CL** policy ids. | IDs present on `TechCard` or `AssuranceLane`. |

### E.17:10 - Anti‑patterns (with fixes)

1. **“Presentation logic” as semantics.**
    *Fix:* Move any logic to `Describe_ID`, `Specify_DS`, CG‑Spec, or KD‑CAL; keep views declarative; publication adds **zero** claims.
2. **Publishing only view objects.**
    *Fix:* MVPK **acts on arrows**. Always emit views for `g∘f`, not just for `ViewObj_s(X)`, `ViewObj_s(Y)`, and `ViewObj_s(Z)`.
3. **Unpinned numbers.**
    *Fix:* Reject card; supply **pins** plus CG and CHR anchors.
4. **Viewpointless views.**
    *Fix:* Define Viewpoint; attach concerns + conformance; re‑emit.
5. **`InteropCard` equivalent to `TechCard` duplication.**
    *Fix:* `InteropCard` may refine typing or shape but cannot contradict `TechCard` (reindexing monotone).

### E.17:11 - Consequences

| Benefit | Why it matters | Trade-off and mitigation |
| --- | --- | --- |
| **Arrow traceability.** | Composition preserved across views enables chain‑of‑evidence on pipelines. | Slight authoring overhead → MVPK templates. |
| **Review-ready faces.** | Pins + CHR anchors make numeric claims verifiable. | Declared publication checks perform MVPK checks; project gates stay with the relevant `OperationalGate(profile)` or `GateDecision` source when the gate claim is live. |
| **Terminology hygiene.** | Clear View vs Viewpoint, Publication vs Presentation. | Enforce L‑SURF tokens in CI. |
| **Notation independence.** | Viewpoints talk concerns, not tools. | Provide adapters to local stacks. |

### E.17:12 - SoTA Alignment: Adopted And Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.

| Source idea and current source | Local FPF invariant and practical local test | Adopted, adapted, or rejected shortcut |
| --- | --- | --- |
| Joint ISO, IEC, and IEEE 42010:2022 architecture-description practice separates architecture description, stakeholder concern, viewpoint, view, model kind, correspondence, and correspondence rule instead of letting one readable model face stand in for all of them. | MVPK publishes one source-pinned face over an existing source `U.Episteme` or `U.View`; every load-bearing face names its publication `U.Viewpoint` and the `PublicationVPId` reference when that reference is used, names concerns, keeps `U.View`, viewpoint, carrier work, rendering work, correspondence support, concrete exchange envelope, and evidence envelope separate, and passes the no-new-claim diff before any work, evidence, gate, assurance, carrier, or bridge use is considered. | Adopt explicit source, concern, view, viewpoint, correspondence, and model-kind separation; reject the shortcut where a readable architecture or model face becomes evidence, work occurrence, gate passage, release permission, bridge support, or concrete exchange authority by presentation alone. |
| Profunctor and optic accounts (2017-2019; source maturity = research or theory line, not load-bearing without local witness) support compositional views that compose like arrows. | MVPK adopts only local publication-composition tests: identity, composition witness, no-new-claim diff, monotone promotion, and scope non-widening. | Adopt the five-test publication-composition bundle; reject optics vocabulary as proof by analogy or as a replacement for local witnesses. |
| Refinement-typed ecosystems (2016+; source maturity = widely used technical practice) keep units, scales, and type-like constraints attached to values. | MVPK publication faces carry pins and CHR and CG anchors; local test: numbers, thresholds, and characteristic claims on faces have units, scales, reference-plane support, and edition support where load-bearing. | Adapt pin discipline; reject readable numbers as self-validating values. |
| Interoperability and evidence-envelope practice (source maturity = mature standards or practice, depending on concrete envelope) separates exchange format and carrier evidence from the claim being carried. | MVPK faces may expose evidence carriers or exchange envelopes, but concrete formats live outside Part E; local test: the face adds no claim and points back to the governing source or evidence path. | Adapt envelope discipline; reject treating envelope presence as semantic authority, evidence sufficiency, work occurrence, or gate passage. |

(References are selected because they support local MVPK invariants and tests; MVPK remains notation-agnostic.)


### E.17:13 - Relations

* **Builds on:** `A.7` and `E.10.D2` for carrier and front-end discipline plus strict I-, D-, and S-discipline; `A.6.2`-`A.6.3` for episteme morphisms, `U.EffectFreeEpistemicMorphing`, and `U.EpistemicViewing`; `E.17.0` for `U.MultiViewDescribing`; `E.8` and `E.10` for authoring and publication-language discipline; Part F and Part G for bridge, terminology, characteristic, and pin discipline.
* **Constrains:** publication-face-emitting automation and hand-written publication faces. They remain species of `U.EpistemicViewing` over existing D-side and S-side epistemes and may not become a second I->D->S mechanism, evidence path, gate decision, work occurrence, assurance record, release source, or bridge declaration by readable form.
* **Current neighboring-pattern boundaries from `E.17:5.1d`:** work or reliance support applies `A.15.4`, with `A.15` for role, method, plan, and work alignment and `A.15.1` for one dated `U.Work` occurrence; evidence, provenance, attestation, currentness, and freshness apply `A.10`; engineering justification, assurance, confidence, readiness, and limitations apply `B.3`; gate passage, constraint validity, adjudication, and release decision support apply `A.20` or `A.21`; same-entity textual restatement applies `A.6.3.CR`; same-entity representation-scheme or reasoning-medium change applies `A.6.3.RT`; deliberately narrower-use rendering applies `A.6.3.CSC`; explanation-facing rendering applies `E.17.EFP`; bounded comparative review applies `E.17.ID.CR`; changed described entity, target, ontology frame, or governed claim applies `A.6.4`, `OntologicalReframing`, or the exact retargeting or reframing pattern; carrier, export, OCR, screen, front-end behavior, or work on carriers applies `A.7`.
* **Part F bridge wording boundary:** when the publication face uses or invites "same", "equivalent", "align", "map", substitutable, interchangeable, attribute, entity, or profile matching, or other bridge-wording claim pressure across contexts, the wording repair belongs to Part F and `A.6.9`; the bridge support belongs to `F.9` or `F.9.1`. `E.17` does not create a local bridge taxonomy.
* **Coordinates with:** B-operators for no Gamma-leakage, C-cluster selection or archive patterns where views remain publication faces rather than selections, CHR and UNM for measurement and normalization semantics, `F.9` or `F.9.1` for bridge support, `A.6.9` for sameness wording, and the neighboring source patterns named above. This section is a relation and neighboring-pattern boundary statement for publication use, not a standing decision tree or process order.

### E.17:14 - Minimal authoring template (Part E)

**Header:** `MVPK v⟨edition⟩ — Σ = {PlainView ⪯ TechCard ⪯ InteropCard, AssuranceLane ⟂}`
**For each arrow `f`:** emit `{Emit_s(f) | s ∈ Σ}` (or use the plain aliases `{PlainView(f), TechCard(f), …}`) with: **PublicationScope**, ViewpointId, pins, CHR and CG anchors, SCR ids, Bridge+CL ids (if crossing), and—if composite—machine‑checkable witnesses that `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)` **and** for each `s ⪯ t` the naturality square `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.

### E.17:15 - Manager’s one‑page review (copy‑paste)

> “We publish every **morphism** under a declared **set of viewpoints** using **MVPK**. Each **view** that claims functorial composition carries the local composition witness; without that witness it stays non-compositional or explanatory-only. Each face **adds no new claims** and pins **unit, scale, reference‑plane, and edition** with **CHR and CG** anchors. **`InteropCard`** views clarify concerns and semantics only (concrete exchange lives outside Part E); **`AssuranceLane`** cites evidence carriers (SCR). Any cross‑Context or cross-plane view cites **Bridge+CL** (Φ→R only). Publication build, render, or upload activity is **`U.Work` on carriers**, not a mechanism change.”

### E.17:End
## E.17.EFP - ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**One-line summary.** `ExplanationFaithfulnessProfile` states how explanation-facing renderings over already available claims, traces, and pins on existing MVPK faces may be used. It helps a publication-side reviewer or explanation reader distinguish source-pinned rendering, source-linked reconstruction, didactic retelling, and speculative retelling without creating a second face family or a second semantic rule track.

**Governed object in plain terms.** One explanation-facing rendering on an existing MVPK face; not the whole face family, not the whole source `U.Episteme` or source `U.EpistemePublication`, and not a second semantic track.

**Governing move in plain terms.** State how that rendering relates to already available source `U.Episteme` or source `U.EpistemePublication`, source pins, traces, and provenance anchors, which explanation-use class it belongs to, and what downstream claim or effect still stays outside the profile.

**Use this when.** Use this profile when one note, memo, sheet, screen, table, or short section is trying to help a reader understand an already available source `U.Episteme` or source `U.EpistemePublication` on an existing face and you need to say what kind of explanation it is without turning that help into a second semantic rule track.

**Start here when.** The first decision is about one explanation-facing rendering on an existing MVPK face, and the real question is whether it stays source-pinned, becomes bounded reconstruction, is openly didactic, or has already shifted into speculation or non-admissible downstream claim or effect.

**What goes wrong if missed.** Helpful explanation quietly turns into a second semantic rule track, hidden bridge-comparison load, or unsupported downstream guidance because the rendering is read as if it were canonical content.

**What this buys.** One honest explanation class on an existing face with visible source anchors, admissible-use boundary, and explicit neighboring-pattern boundaries when the rendering has stopped being merely explanatory help.

**Not this pattern when.** Not this profile when the real job is same-entity rewrite (`A.6.3.CR`), representation change (`A.6.3.RT`), bounded comparative reading (`E.17.ID.CR`), changed described entity (`A.6.4`), deliberately coarsened rendering that now needs narrower admissible claim or effect, non-admissible downstream claim or effect, and reopen to the source `U.Episteme` or source `U.EpistemePublication` (`A.6.3.CSC`), downstream work or reliance (`A.15`, `A.15.4`), assurance or engineering justification (`B.3`), or gate-bearing content (`A.20`, `A.21`).

**First output.** One compact explanation-use note: explanation class, source anchor, admissible explanation-reader use, non-admissible downstream use, and reopen or boundary condition. MVPK face, pins, provenance, and source fields are inherited by reference unless ambiguity or a load-bearing source-relation question makes them live.

**Ordinary-output claim inventory.** After `ExplanationFaithfulnessProfile`, the author has claimed only that this explanation-facing rendering has this explanation class, this source relation, this source anchor posture, and this admissible use. The author has not claimed model truth, evidence path, assurance, safe reliance, gate passage, work occurrence, release support, or source replacement unless the exact neighboring FPF pattern and exact project-side FPF kind and reference are named.

**Working action spine.** One explanation-facing rendering is helping a reader -> separate source-pinned rendering, bounded reconstruction, didactic retelling, and speculative retelling -> use the explanation for understanding, source navigation, bounded restatement, teaching, or exploration according to class -> output one class plus safe next action -> apply the neighboring FPF pattern if reliance, evidence, work, gate, engineering justification, comparison, narrower-use rendering, or new-claim load appears. Use `E.17:5.1c` for `orientation use`, `reliance use`, `operative claim`, `non-admissible downstream use`, and `reopen trigger`; use `E.17:5.1d` when the primary live question may be same-entity rewrite, representation change, coarsening, comparison, bridge or substitution, work or reliance, gate, evidence, assurance, retargeting, or carrier work or front-end work instead of explanation-facing rendering.

**Ordinary use.** If the explanation only helps reading, source-finding, review, comparison, or planning preparation, one compact review note naming the explanation class, source anchor, and non-admissible downstream claim or effect is enough.

**Load-bearing use.** Open the fuller explanation review only when the rendering will guide work or reliance, be externally relied on, be disputed, cross context, affect person or team status, or be cited as evidence, approval, engineering justification, gate, or release support.

**Stop condition.** Stop once the explanation class changes no next reading, review, source-finding, comparison, or planning-preparation move and blocks no concrete overclaim about source support, work or reliance, evidence, approval, gate, or release.

**Admissible explanation-use examples.**

| Admissible explanation use | Source-finding check with no downstream claim or effect | Non-admissible explanation use |
| --- | --- | --- |
| A `SourcePinnedExplanation` or `SourceLinkedExplanationReconstruction` helps navigation, bounded restatement, or source inspection with pins and trace visible. | A didactic explanation helps onboarding or helps the team find the source, while operative claims still return to the source-pinned face or `A.10` evidence path. | A fluent explanation is used as assurance, evidence, approval, gate passage, release permission, or work-occurrence support. |


**Neighboring project records and governing patterns.** `E.17.ID.CR` governs bounded comparative reading; `A.6.3.CR` or `A.6.3.RT` govern same-entity rewrite or representation change; `A.6.3.CSC` governs a rendering that stays honest only through narrower admissible claim or effect, non-admissible downstream claim or effect, and reopen to the source `U.Episteme` or source `U.EpistemePublication`; `A.6.4` or `OntologicalReframing` govern changed described entity; `A.15` and `A.15.4` govern downstream work or reliance, `B.3` governs assurance and engineering justification, and `A.20` or `A.21` govern gate-bearing claim or effect.

**Common wrong escalations and boundary transfers.** Do not use this profile to hide new claims, bridge-comparison load, action-selection pressure, or gate-bearing guidance inside helpful prose. If the rendering is really a bounded comparison, apply `E.17.ID.CR`; if it is only same-entity rewriting or representation shift, apply `A.6.3.CR` or `A.6.3.RT`; if it is a deliberately coarsened rendering whose narrower admissible claim or effect, non-admissible downstream claim or effect, and source-bearing reopen now govern the case, apply `A.6.3.CSC`; if it is already making world, work or reliance, assurance, or gate-bearing claims, leave `E.17.EFP` for the more exact downstream FPF pattern or project-side record.

**Generated-explanation repaired case.** When a generated explanation is used to help reliance, this profile only states the explanation relation, source-finding posture, and `E.17:5.1b` source-support posture needed for the current use. The explanation becomes usable for an operative claim only when an `A.10`-governed evidence path maps that claim to the exact source passage, carrier path, or exact project-side FPF kind and reference that supports it in the relying context. If that path or exact project-side FPF kind and reference is missing, create only a prospective repair request, explicit source-gap note, or future evidence-work plan; it does not become retroactive support for the earlier explanation-based claim. Do not open an `A.10` path for ordinary reader help; otherwise the generated explanation remains reader help, not approval, authorization, evidence, assurance, gate passage, or work-occurrence support.

**Generated-retelling survival.** A generated retelling preserves only the reader help, source-finding cue, quoted source pins, explicitly repeated source relation, and explicitly repeated admissible-use boundary that remain inspectable in that retelling. It does not become or preserve the source `U.Episteme`, source `U.EpistemePublication`, evidence path, assurance, gate passage, decision status, permission, or source replacement merely by fluency, completeness-looking wording, or citation-like links. If the generated retelling compresses, omits, strengthens, or changes source claims, treat the result as a new explanation-use case, a narrower-use rendering under `A.6.3.CSC`, or reader help only.


