---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:4"
section_title: "Solution — The Local‑First Naming Protocol"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__006_solution-the-local-first-naming-protocol.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:4 — Solution — The Local‑First Naming Protocol"
line_start: 74534
line_end: 74717
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:4 - Solution — The Local‑First Naming Protocol

F.18 defines **eight rules** (R‑rules) and **six practices** (P‑practices). Together they produce **Name Cards** that any reader can interpret **ontologically** without guessing, and that slot cleanly into the rest of Part F.

**Path Card (subset of Name Card).** A **Name Card** whose named FPF value is an **EvidenceGraph Path**: it cites a **PathId** (or **PathSliceId**), **Context**, **ReferencePlane**, **Γ_time**, and any **Bridge id(s) + CL/CL^plane** (with loss notes). Used by **G.6** and **G.10** to make justifications portable on UTS.

#### F.18:4.1 - The Eight R‑rules (normative)

**R1 — Speak every name *with its Context*.**
A name is **never** context‑free. When you introduce or use a name, **pair it with the Bounded Context** where it lives (the “Context of meaning”), and with the **edition** of that Context if relevant. In everyday speech: “X, *in* Y.” Cross‑context use requires a Bridge; labels alone do not travel.

**R2 — State the ontological *Kind* on the Card.**
Every Name Card **must** state the **Kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This prevents category errors and keeps Role–Method–Work alignment clean. *Clarification:* this is a **Card requirement**, not a demand that the label string begin with the Kind. The Kind field uses an accepted FPF kind or an explicitly marked extension candidate; the Name Card does not itself create a `U.Kind`, `RelationKind`, `GateProfile`, `EvidenceKind`, MVPK face kind, or Bridge.

**R3 — Declare the *Purpose / use‑domain* on the Card.**
In addition to **Kind**, the Name Card **must** state the intended **Purpose / use‑domain** that situates the concept in practice and signals **which families of contexts** are expected to use it (e.g., mathematical formalism, engineering practice, computer science, systems management). This enables reconstruction of usage from the lexicon and reduces unintended scope drift. *Clarification:* this is a **Card field**; it does **not** require the label string to carry the purpose qualifier.

**R4 — Resolve the name to a *Local‑Sense*.**
A minted name must resolve to a Local-Sense inside its Context (the result of F.2–F.3). If a name points to a Role Description, state that template and its sense basis. Avoid heavily overloaded label words: when needed, prefer concise two-word Tech labels that hint at the intended sense.

**R5 — Use *Twin Registers* (Unified Tech + Plain).**
Provide two human‑oriented labels on the Name Card, per **E.10** register discipline:
* a **Unified Tech** label (short, morphology‑stable, neutral in wording);
* a **Plain** label (reader‑friendly phrasing for managers and subject‑matter experts).

The **Unified Tech** label is the only one used in **Core** normative prose; **Plain** is for teaching and examples. Both remain **context‑local**; neither establishes Cross‑context identity (that is the job of the **UTS row** and **Bridges**).

**R6 — Keep thresholds and states *out of the name*.**
Do not encode numeric limits, separation‑of‑duties, or readiness states in the label. Put thresholds on **Method steps** (capability/acceptance), states in **Role State Graphs**, and SoD via **incompatibility** relations. Names carry *what this is* and *which Context claims it*—not *when and how it may act*.

**R7 — Cross‑context only by *Bridge* with loss notes.**
When another Context needs to reference a name, use an **Alignment Bridge** that states the relation (equivalent, narrower, broader, analogous) and its **Congruence Level** with explicit **loss/fit** annotations. Never equate two names by label alone.

**R8 — Make renames and merges *first‑class events*.**
When a label changes, or two labels consolidate or split, record it on the Name Card as a lineage action (rename, merge, split, retire) with rationale and dates. Past uses *remain valid as historical facts*; continuity comes from lineage, not silent edits.

#### F.18:4.2 - The Six P‑practices (normative process)
**P1 — Candidate set (*NQD-front* of seed-words).**
Do **not** pick a label “in one shot”. Build a **small, non-dominated candidate set** (an *NQD-front*, typically 5–10 items) by seeding and varying along:
**Traditions** — mathematics, physics, engineering, computer science, systems thinking, management, etc. with their typical contexts and situations; use maximum diversity here;
 **Novelty/Familiarity** — from careful **reuse** of established terms to sharper **neologisms** from recent SoTA traditions;
 **Lexical form** — distinct **head terms** and morpheme families, readability/pronounceability, inflection/declension, transparency.
Use the **Novelty–Quality–Diversity** discipline from **Part G** to maintain only **non-dominated** candidates; when appropriate, you may implement this via **Γ_nqd.generate**. Record the **seeds** and the short rationale in the Card’s notes. Choose final **Unified Tech**/**Plain** labels **from this frontier**; if a high-quality candidate is discarded, briefly note why.

For the purposes of **Diversity_P**, group candidates into **head-term families** (same base noun/verb + minor prepositions or case endings). Variants such as *“Reference plane”*, *“Plane of reference”* and *“Referred plane”* **count as one family**, not three distinct candidates. An NQD-front with multiple near-clones from one family **does not** satisfy the diversity requirement. Aim for **≥ 3 distinct head-term families** in the CandidateSet; if the front ends up with fewer families (e.g. due to a very narrow domain or high AliasRisk on other heads), the Name Card **MUST** record a brief rationale in the NQD-front notes.

**Lexical Q-components for the NQD-front**
When P1 uses **NQD-CAL (C.18)**, treat the **Quality vector** over candidates as part of the same archive as C.18’s **NQD-frontier**. Recommended components (all **ordinal; no arithmetic means**):

 * **SemanticFidelity (P — Ontological precision).**
  *Question.* Does the label verify against the **Minimal Definitional Statement (MDS)** and Concept‑Set row without adding or losing core invariants?
  *Scale (ordinal; ↑ better).* `{Misleading, Vague, Precise, Exact}` with `Exact ≻ Precise ≻ Vague ≻ Misleading`.
  *Link to P2.* When **P2** is run, derive the SemanticFidelity rating from the per‑sense‑seed judgements: candidates with any **core** sense‑seeds classified as `wrong‑prototype` **MUST** be rated **Misleading**; candidates rated **SemanticFidelity ≥ Precise** **SHOULD** have at least a configurable fraction `θ_P` (default `θ_P = 0.7`) of sense‑seeds in `on‑target` and **NONE** in `wrong‑prototype`. Discard candidates that remain **Misleading** after revision.

* **CognitiveErgonomics (S — Sociolinguistic admissibility).**
  *Question.* Can the target **RoleEnactors** (engineers, managers) read, pronounce, and recall the label without specialist training?
  *Scale (ordinal; ↑ better).* `{Alienating, Jargon, Acceptable, Natural}` with `Natural ≻ Acceptable ≻ Jargon ≻ Alienating`. Prefer labels **≥ Acceptable** in the stewardship Context.

* **MorphologicalActionFit (O — Morphological/action alignment).**
  *Question.* Does the morphology of the label hint at its role in **methods/morphisms** (object vs process vs result) and support the required derivational family (noun/verb/participial forms)?
  *Scale (ordinal; ↑ better).* `{Opaque, Role‑hinting, Action‑aligned}`. Action‑aligned labels make it obvious whether we are naming an **actor**, an **activity**, or a **publication result** (e.g., *ReviewerRole* vs *Reviewing* vs *ReviewRecord*).
  *Kind-sensitive cues.* When the **Kind** on the Card is a **Role**, prefer agentive/holder morphology (*…Role*, *…er*, *…or* or local equivalents); when the Kind is **Method or MethodDescription**, prefer verbal or gerundive forms; when the Kind is **Holon**, prefer result nouns, when **Work**, prefer verb. Misaligned morphology (e.g., a Role named with a pure process noun) should be treated as a **penalty on MorphologicalActionFit** and, if retained for legacy or regulatory reasons, called out explicitly in **Card notes**. See F.5/F.11/F.12 and **LEX-BUNDLE §8**.

* **AliasRisk (A — Lexical overload).**
  *Question.* How likely is a careful reader to import a **wrong sense** from neighbouring FPF records/publications or external canons when they see this string?
  *Scale (ordinal; ↓ better).* `{Safe, Context‑dependent, High‑Risk, Overloaded}` with `Safe ≻ Context‑dependent ≻ High‑Risk ≻ Overloaded`. Avoid adopting **Overloaded** labels unless required by legacy and called out explicitly in notes. When C.18’s **DomainDiversitySignature** is available, AliasRisk MAY be refined into a CHR‑typed characteristic with the same polarity.

Use these components for **Pareto comparison only** (per **C.16** ordinal discipline). Do **not** collapse them into a single scalar score; the NQD-front is computed over the **vector of lexical Q-components** together with **Novelty** and **Diversity_P**.

**P2 — Semantic read‑through against archetypal situations.**
Alongside the NQD‑front of label candidates, maintain a **small set of 5–10 archetypal situations** (“**sense‑seeds**”) that instantiate the intended use (purpose) across different traditions. For **each** candidate label and each sense‑seed, perform a **read‑through test**:
– write **1–2 short example sentences per sense‑seed** (e.g., “In case X, we perform \<Label\>”);
– classify the outcome, for a careful reader in the stewardship Context, as one of `{too-narrow, on-target, too-wide, wrong-prototype}`.
Maintain, on the Name Card, a small tally per candidate of how many sense-seeds fall into each class. Use these tallies both to **prune candidates** and to instantiate **SemanticFidelity** (P-component): labels with a sustained pattern of `wrong-prototype` hits on core sense-seeds **SHALL** be removed from the NQD-front (or kept only as deprecated aliases with an explicit warning). Candidates rated **SemanticFidelity ≥ Precise** **SHOULD** satisfy the `θ_P` constraint from the SemanticFidelity definition (fraction of `on-target` seeds) and have no `wrong-prototype` counts.
Record **rejected candidates** and their **mismatch patterns** in the Name Card’s **NQD‑front notes**.

**P3 — Mint‑or‑Reuse gate (F.8).**
Before minting, search your Context’s **Concept‑Set table**. If a row already covers your sense, reuse it and only add a **local label**. If not, propose a **new row** and capture the decision in a brief rationale.

**P4 — Concept‑Set linkage (F.7).**
Every Name Card **must** indicate its Concept‑Set row (or record “not applicable” for intentionally Context‑unique names). This is the handle for alignment and anti‑explosion control.

**P5 — UTS registration (F.17).**
Publish each Name Card to the **Unified Term Sheet** with Context, kind, twin labels, sense anchor, edition, and lineage status. Keep the UTS the single, human-readable table of record.

**P6 — Lexical-continuity hygiene (F.13).**
Apply the same discipline to renames, splits, merges, and retirements; leave forward and backward pointers so readers can trace lexical continuity at a glance.


#### F.18:4.3 - Guarded-head note for locally risky labels
Some locally useful heads remain risky because they already carry different load-bearing readings in different admissible local texts. In such cases, authors may publish a **guarded-head note** as a thin naming-governance companion.

A guarded-head note does **not** create a new governing term, does **not** establish Cross-context sameness by itself, and does **not** replace the meaning fixed in the cited authority text, governing FPF pattern, or accepted `DRR`. It simply records that one publication-facing head should stay deconflicted while local-first naming continues to govern minting, reuse, aliases, and Bridges.

This is especially useful when one head already appears in more than one admissible local reading, such as `projection` in `A.16` move language and in `F.9.1` bridge stance language. The note should therefore name the consumer sites, keep each local reading explicit, and resist any temptation to flatten them into one global head.

#### F.18:4.3a - Durable-head settlement for entry/discoverability vocabulary

When naming work touches the discoverability amendment, `PCP-TERM` plus `F.18`
and `A.6.P` must settle the durable heads used here, including
`pattern-entry discoverability`, `description recognition signature`,
`entry orientation`, `entry lexeme retrieval aid`, `worked entry reading`,
`Problem-frame recognition signature`, and `thin-echo discipline`, as part of
the amendment itself.

The amendment should therefore assign each effect to one named FPF pattern,
pattern section, field, relation, or section of a named non-pattern FPF publication
form with a support function. When such a non-pattern publication form is used,
its publication form, companion function, and reference must be named by value,
and the referenced section must carry that effect. Do not let the single trigger
word `discoverability` become one semantic swamp.


The canonical settlement table for this amendment is:

| Term | Canonical job | Receiving FPF pattern, pattern section, field, relation, or selected non-pattern FPF kind-reference pair | Plain-only or deprecated neighbors |
| --- | --- | --- | --- |
| `pattern-entry discoverability` | composite entry quality over one entry-recognition stack | `E.11` | broad `discoverability` alone |
| `description recognition signature` | first-contact cue structure of one description-bearing unit | `A.6.RSIG` | `discoverability of descriptions` |
| `recognition text` | existing first reading text inside one pattern | `E.8` | invented `discoverability surface` |
| `entry neighborhood` | entry-load-oriented grouping of plausible patterns, tempting wrong patterns, entry-load reclassifications, and admissible stops | `E.11`; `J.4` only when the entry grouping is a pattern-language map | `route` |
| `entry lexeme retrieval aid` | lexical and query retrieval aid without alias minting | `F.17`, `F.18`, and `E.10`, coordinated by `E.11` | `lexical discoverability`, bare `search support` |
| `worked entry reading` | bounded interpretive case reading | `I.2` | `workflow`, `scenario script`, `route` |
| `thin echo` | low-detail projection pointer to the cited pattern, cited pattern section, field, relation, or section of a named non-pattern FPF publication form; the pointer makes the publication form, companion function, and reference recoverable, and the referenced section carries the claim | `E.11` | duplicated guidance, parallel blurbs |

One canonical term per job is the settled target of this amendment.
Deprecated wording may remain only as plain search cues or explicit deprecated-alias guards while the wording is being repaired by value.


#### F.18:5.1 - Card purpose & mode guard (normative)

To prevent “post-hoc justification” of intuitively chosen labels, every **Name Card** SHALL declare its
**CardMode ∈ {MintNew, DocumentLegacy}**:

* **MintNew.** The Card is the **output of an NQD-style lexical search** over a **candidate label set** generated inside
  the stewardship Context(s), using the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, MorphologicalActionFit,
  AliasRisk}` together with **Novelty (N)** and **Diversity_P** (per A.0 / C.17–C.18 / B.5.2.1).
  – The Card SHALL record:
    – a minimal **CandidateSet** (the labels actually evaluated), with **head-term family** tags for each candidate;
    – the resulting **NQD-front** of **non-dominated candidates** over ⟨Q-tuple, N, Diversity_P⟩;
    – the **sense-seeds** used for P2 read-through and their mismatch patterns;
    – a short **selection note** explaining why the chosen Tech/Plain pair was picked from that front
      (e.g., “better CognitiveErgonomics at equal SemanticFidelity”).

  – A single-element NQD-front is permitted only if the Card records a brief rationale why **no alternative candidate
    survived** the lexical and NQD filters (e.g., legacy constraints, high AliasRisk on all other options).
  – A MintNew card is **non-conformant** if authors fill only the top fields after choosing a label by intuition.
    Recording the chosen label, Kind, and a short rationale is **not** a substitute for the seed set, NQD-front,
    sense-seed read-through, and explicit non-dominated selection.

* **DocumentLegacy.** The Card documents an **externally imposed legacy label** (e.g., a regulatory or de facto Standard)
  and its mapping to FPF structures. In this mode the Card MAY omit a full NQD-front, but SHALL:
  – state the **legacy source and provenance**;
  – either (i) provide at least a **sketched NQD-comparison** of viable internal variants against the legacy label, or
    (ii) record a short **out-of-scope rationale** (e.g., “name frozen by law; see cited Standard”) explaining why NQD
    search is not being used for selection.

For all **Core-facing naming of U.Types and other canonical FPF concepts**, **MintNew** is the **default** CardMode; using
DocumentLegacy for such names requires an explicit justification on the Card.

For one-off local phrase repair, no Name Card mode is live. Use `E.10`, `C.2.P`, or `E.17.AUD.LHR`, and record the repaired phrase only where the local repair pattern requires it. Open a Name Card only when the repair mints or changes one durable reusable name, UTS row, Core-facing term, or cross-context naming relation.

A **Name Card** is the authoritative, human‑readable record of a name inside its Context. It has these fields; teams may add local notes.

1. **Row ID** — the stable, opaque **UTS row identifier** (the identity anchor).
2. **Twin labels** — **Unified Tech** and **Plain** (per E.10).
3. **Context of meaning** — the Bounded Context and, if relevant, its edition.
4. **Kind** — what sort of thing this is (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This is an **ontological category**, not a spelling prefix.
5. **Purpose / use‑domain** — the intended area(s) of use (which families of contexts are expected to use it).
6. **Minimal Definitional Statement (MDS)** — one-paragraph intended sense in the stewardship context (no tool/process slang).
7. **Didactic subtitle** — ≤ 12 words that signal pragmatic use.
8. **Sense reference** — a Local‑Sense reference (how F.2–F.3 clustered it).
9. **Concept‑Set linkage** — Concept‑Set reference or “not applicable” (with rationale).
10. **Alignment note** — if a Bridge exists to other Contexts, cite it and record **loss/fit** in plain words (no formulas required on the Card).
11. **Relation kind** — if the name is for a relation, declare **structural** vs **epistemic** and `validationMode ∈ {axiomatic, inferential, postulate}`. For **structural** relations, provide **Constructive** grounding (`tv:groundedBy → Γₘ.sum|set|slice`). If the name is not for a relation with arity ≥ 2, set this field to “n/a”.
12. **Manager’s clip** — one‑line “use/avoid” guidance for everyday communication.
13. **Archetypal situations (sense‑seeds)** — **5-10 short “X‑case” lines** used by **P2** for the semantic read‑through; keep them **edition‑aware** and **context‑local**. For **MintNew** cards these are required evidence, not optional examples.
14. **NQD‑front notes** — brief rationale for discarded candidates (**include mismatch patterns from P2, the head-term family mix, and any lexical Q‑scores used in P1**).
15. **SemanticFidelity/CognitiveErgonomics/MorphologicalActionFit/AliasRisk** scores for the NQD-front labels, recorded at least ordinally for the surviving candidates.
16. **Version**  — current status and history of editions.
17. **Card notes** — optional free text with comments about the name (e.g., recommended translations, etymology, pronunciation).

**Manager’s reading habit.** When two names collide in a meeting, ask for their **Context**, **Kind**, **Purpose/use‑domain**, and **Sense anchor**. If any of those differ, you are comparing different things; switch to **Bridge** talk, not label talk.

