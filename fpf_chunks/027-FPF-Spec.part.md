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
`entry orientation`, `entry lexeme support`, `worked entry reading`,
`Problem-frame recognition signature`, and `thin-echo discipline`, as part of
the amendment itself.

The amendment should therefore assign each effect to one named FPF pattern,
pattern section, field, relation, or section of a named non-pattern FPF publication
form with a support function. When such a non-pattern publication form is used,
its publication form, support function, and reference must be named by value,
and the referenced section must carry that effect. Do not let the single trigger
word `discoverability` become one semantic swamp.


The canonical settlement table for this amendment is:

| Term | Canonical job | Receiving FPF pattern, pattern section, field, relation, or selected non-pattern FPF kind-reference pair | Plain-only or deprecated neighbors |
| --- | --- | --- | --- |
| `pattern-entry discoverability` | composite entry quality over one entry-recognition stack | `E.11` | broad `discoverability` alone |
| `description recognition signature` | first-contact cue structure of one description-bearing unit | `A.6.RSIG` | `discoverability of descriptions` |
| `recognition text` | existing first reading text inside one pattern | `E.8` | invented `discoverability surface` |
| `entry neighborhood` | entry-load-oriented grouping of plausible patterns, tempting wrong patterns, entry-load reclassifications, and admissible stops | `E.11`; `J.4` only when the entry grouping is a pattern-language map | `route` |
| `entry lexeme support` | lexical and query support without alias minting | `F.17`, `F.18`, and `E.10`, coordinated by `E.11` | `lexical discoverability`, bare `search support` |
| `worked entry reading` | bounded interpretive case reading | `I.2` | `workflow`, `scenario script`, `route` |
| `thin echo` | low-detail projection pointer to the cited pattern, cited pattern section, field, relation, or section of a named non-pattern FPF publication form; the pointer makes the publication form, support function, and reference recoverable, and the referenced section carries the claim | `E.11` | duplicated guidance, parallel blurbs |

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

For one-off local phrase repair, no Name Card mode is live. Use `E.10`, `E.10.SEMIO`, or `E.17.AUD.LHR`, and record the repaired phrase only where the local repair pattern requires it. Open a Name Card only when the repair mints or changes one durable reusable name, UTS row, Core-facing term, or cross-context naming relation.

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

### F.18:6 - What *belongs* in the label—and what does not

**Belongs (keeps the label clean and durable):**

* The **core head word** that names the thing *(the **Kind** is recorded on the Card; the string need not encode it)* (e.g., “Pump”, “Standard”, “Requirement”, “Surgeon”, “Cooling”).
* A **purpose qualifier** if it is essential to the local sense and stable across editions (e.g., “Cooling” vs “Fuel”).
* A **scope qualifier** only if it is part of the *meaning* rather than the current plan (“Surgical Ward” rather than dates or batch numbers).

**Does not belong (move elsewhere):**

* **Numbers and thresholds** (put on steps, capabilities, acceptance clauses).
* **States** (use Role State Graphs and checklists).
* **Temporal windows** (work plans and history).
* **Organisational authorisations** (speech acts and assignments).
* **Imported acronyms** from other Contexts (use Bridges with loss notes instead).

**Quick litmus for authors.** If removing a number, date, or state *does not* change the *meaning* of the thing, it should **not** be in the label.

### F.18:7 - Worked triad (three short, context‑local examples)

*(Names below are illustrative; the same words in other Contexts may mean something else. The point is how the Name Card keeps them clear.)*

#### F.18:7.1 - Industrial operations Context: “Thermal Management - 2026”

* **Kind:** Service
* **Purpose / use‑domain:** industrial thermal utilities; line‑level planning and operations
* **Unified Tech label:** Cooling Supply
* **Plain label:** Chilled water for line B
* **Sense anchor:** supply of water at defined temperature/flow to boundary B
* **Concept‑Set:** “Utility service” row; local variant recorded
* **Alignment note:** Bridge to “Plant Utilities - 2026” notes that “Cooling Supply” there bundles filtration; *loss:* filtration is not guaranteed in this Context
* **Version:** 20 Feb 2024
* **NQD‑front (seed candidates):** *Cooling Supply*, *Chilled Water Service*, *Process Cooling*, *Cooling Utility*. **Chosen:** *Cooling Supply* (neutral, morphology‑stable).

**Why it’s good.** The label doesn’t encode temperature or flow limits (those live in acceptance). It names a Service; nobody will confuse it with a pump System or a Method.

#### F.18:7.2 - Clinical Context: “Hospital OR - 2026”

* **Kind:** Role
* **Purpose / use‑domain:** OR governance and staffing; credentialing and checklists
* **Unified Tech label:** Surgeon Role
* **Plain label:** Operating surgeon
* **Sense anchor:** person who is authorised to perform surgical steps under defined checks
* **Concept‑Set:** “Clinical roles” row
* **Alignment note:** Bridge to “Training & Credentialing - 2026” shows partial overlap; *loss:* that Context’s “Senior Surgeon” carries teaching duties that do not apply here
* **Version:** Feb 2025; renamed‑from “Lead Surgeon” (2025) with rationale: avoided “lead” vs “operating” ambiguity
* **NQD‑front (seed candidates):** *Surgeon Role*, *Operating Surgeon*, *Primary Surgeon*, *Operating Physician*. **Chosen:** *Surgeon Role* (Kind‑neutral string; Plain clarifies).
*Lexical Q snapshot (PSOA‑style, informative).*

| Candidate | SF | CE | OA | A‑Risk | Comment |
| --- | --- | --- | --- | --- | --- |
| Surgeon Role | Precise | Acceptable | Role‑hinting | Safe | Neutral head noun; morphology matches **Role** Kind; works across departments. |
| Operating Surgeon | Precise | Natural | Role‑hinting | Context‑dependent | Reads well, but “operating” competes with “operating theatre/room”; kept as Plain label only. |
| Primary Surgeon | Vague | Natural | Role‑hinting | Context‑dependent | “Primary” ambiguous (training vs shift); rejected for governance vocabulary. |
| Operating Physician | Vague | Jargon | Role‑hinting | High‑Risk | Collides with non‑surgical physician roles; rejected despite familiarity in some hospitals. |

**Why it’s good.** No fatigue thresholds or readiness states in the name; those live in the Role’s state graph and checklists.

#### F.18:7.3 - Public service Context: “Civic Services - 2026”

* **Kind:** Requirement
* **Purpose / use‑domain:** service performance management; public service SLAs
* **Unified Tech label:** Passport Lead‑Time
* **Plain label:** Time to issue a passport
* **Sense anchor:** elapsed time from complete application to issuance
* **Concept‑Set:** “Service quality requirements” row
* **Alignment note:** Bridge to “Legal Framework - 2026” records that legal “deadline” has different remedies; *loss:* legal exemptions not carried into this Context
* **Version:** current
* **NQD‑front (seed candidates):** *Passport Lead‑Time*, *Issuance Time*, *Service Turnaround*, *Time to Issue Passport*. **Chosen:** *Passport Lead‑Time* (neutral; Plain remains didactic).

**Why it’s good.** Target values (e.g., ≤ 20 days) are not in the label; they live in acceptance clauses.


### F.18:8 - Conformance Checklist (editor aid) — *Part I: naming & cards* (**non‑normative**)

**CCE‑F18.1 (Context pairing).**
Every name used in normative text **must** be paired with its **Context of meaning**. If you cannot name the Context, you do not have a valid name.

**CCE‑F18.2 (Kind clarity).**
Every Name Card **must** state the **kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, …). Using labels that hide kind is non‑conformant.

**CCE‑F18.2a (Purpose declared).**
Every Name Card **must** state the **Purpose / use‑domain** (families of contexts where the concept is expected to be used). Omitting Purpose is non‑conformant.

**CCE‑F18.3 (Sense anchoring).**
A minted name **must** resolve to a **Local‑Sense** in its Context. If a sense cannot be stated, label minting is deferred.

**CCE‑F18.4 (Twin registers).**
Each Name Card carries a **Unified Tech** and a **Plain** label (E.10). Tech appears in **Core** prose; Plain in teaching/examples.

**CCE‑F18.5 (No thresholds/states in labels).**
Numeric limits, readiness states, and separation‑of‑duties **must not** appear in labels. Put them on steps, checklists, and role algebra.

**CCE‑F18.6 (Bridge‑only travel).**
Cross‑context reuse of a name **must** go through an **Alignment Bridge** with an explicit relation and **loss/fit** notes. Label matching alone is forbidden.

**CCE‑F18.7 (Lexical-continuity visibility).**
Renames, splits, merges, and retirements **must** be recorded on the Name Card with dates, rationale, and forward and backward lexical-continuity pointers. Past occurrences remain valid as historical facts.

**CCE‑F18.8 (Mint‑or‑Reuse gate).**
Before minting, authors **must** check the Context’s Concept‑Set table; if a row exists, **reuse** it with a local label unless a documented reason compels a new row.

**CCE‑F18.9 (UTS entry).**
Names used in normative FPF publications **must** appear on the **Unified Term Sheet** with the specified **Name‑Card fields**; include Notes when present).

**CCE‑F18.10 (No cross‑kind labels).**
Do not reuse the same **Unified Tech label** for different kinds inside one context (e.g., “Cooling” as a Service and as a Method). If unavoidable, add a stable qualifier to disambiguate and record the decision on both Name Cards.

**CCE‑F18.11 (Manager’s clip).**
Each Name Card **should** carry a one‑line “use/avoid” note to guide everyday speech. Where omitted, editors add it during review.

**CCE‑F18.12 (Anti‑explosion check).**
If three or more near‑synonyms for the same Local‑Sense appear in drafts, authors **must** either consolidate to one label or record an intentional synonym pair with use/avoid notes and a plan to converge.

### F.18:9 - Normative Standard (what must be true)

> This section is binding. It specifies the publication Standard for unification-oriented names in the Unification Suite (Part F), with **local-first authority**, **bounded context clarity**, and **one-way unification** through declared dependency strata. It complements, and does not replace, the structural and epistemic Standards elsewhere in FPF.

**9.1 Local authority & stewardship context.**
Every unification name has a **single stewardship Bounded Context**: exactly one *Bounded Context* that authors and stewards it. That stewardship Context is responsible for the definition, examples, and lineage of the name. Cross-context reuse happens by **bridges**, not by relocating the stewardship Context.

**9.2 Minimum definitional payload.**
A published name MUST ship with a human-readable **Minimal Definitional Statement (MDS)** that states the intended sense in the stewardship context, and a **Didactic Subtitle** (≤ 12 words) that signals its pragmatic use. The MDS must be free of process slang and implementation jargon.

**9.3 Row ID plus labels.**
For each adopted name, the stewardship Context supplies:
* a **Row ID** (the opaque UTS identifier — the **identity anchor**), and
* two **labels**: a **Unified Tech** label (for Core prose) and a **Plain** label (for teaching).
  Both labels refer to the same underlying sense; **Plain** may simplify terms, not premises.

**9.4 One-way dependency strata.**
Each dependency stratum depends only on already-admitted lower strata: a name in stratum *n* can rely on names admitted in strata ≤ *n*, never sideways or upwards. Cycles are prohibited. If a dependency is not yet admitted at the required stratum, the new name remains Draft or Pilot.

**9.5 Local‑first before reuse.**
Teams MUST first **identify and stabilize the local sense** (within their Bounded Context). **Within the stewardship Context**, reuse existing **Concept-Set rows** where they fit (§4.2 **P1**). **Across contexts**, reuse occurs via **Alignment Bridges** that map the local sense to an existing sense elsewhere without collapsing the local stewardship Context.

**9.6 Sense, not string.**
Publication concerns **sense** (intended meaning in context), not the literal string. Synonyms are allowed as **Plain** labels or **aliases** only if they point to the same **Row ID** and pass the conformance checks in §15 (“CC‑F18”). Strings must not be treated as identity.

**9.7 Relation-kind discipline (structural vs epistemic).**
If the public name expresses a **structural relation**, its intended sense **MUST** be backed by *exactly one Constructive trace* in the structural calculus (Compose-CAL) and **SHALL** declare `validationMode=axiomatic` (see E.14). If the name expresses an **epistemic relation**, Constructive backing is optional; **declare** `validationMode ∈ {inferential, postulate}` and use **Logical/Mapping** and/or **Empirical Validation** as appropriate. **Do not mix relation kinds** inside a single name. *(Do not use “Tier-1/2”; formality is expressed via F per C.2.3.)*

**9.8 Member vs Component.**
Names that describe collection membership MUST NOT be used to imply part‑whole structure, and vice versa. If both aspects are needed, publish two names with their own MDS and an explicit bridge.

**9.9 Name-lineage states.**
A name travels through **Idea → Draft → Pilot → Ratified → Deprecated**. Transitions require explicit human review gates. Ratified names carry a clear stewardship contact and date.

**9.10 Anti‑duplication duty.**
Before ratification, the stewardship Context MUST perform a **near-neighbor review**: identify adjacent names, record the decision to align, merge, or keep separate, and publish the rationale in the name’s record.

**9.11 Local clarity over global neatness.**
When in doubt, prefer **local intelligibility** for practitioners over global symmetry. Global neatness can be achieved later via bridges; loss of local sense is hard to repair.

**9.12 No imported tool terms in Core names.**
Names and their MDS must not carry terms whose only meaning is tied to operating tools or pipelines. If such terms are unavoidable in pedagogy, confine them to Working-Names and examples with disclaimers.

**9.13 Human‑only conformance.**
Conformance for this protocol is judged by trained human reviewers using the author and reviewer checklists in §14 and the conformance criteria in §15 (“CC‑F18”). Automated heuristics, if any exist in an organization, have no standing in the Core.

### F.18:10 - Rationale (why this exists and why these rules)

**10.1 Local‑first unlocks velocity without lexical debt.**
Centralized naming regimes seem tidy but slow learning and create brittle compromises. Local‑first minting lets teams speak clearly **now**; unification comes from disciplined bridges and one‑way dependencies, not from premature centralization.

**10.2 One stewardship context lowers ambiguity.**
Names with several competing stewardship contexts drift. A **single stewardship Context** concentrates accountability for sense, examples, and lineage, while still enabling broad reuse via alignment bridges.

**10.3 Unified Tech + Plain serve two audiences.**
Engineers need **precise** wording; managers and stakeholders need **approachable** wording. Splitting the labels keeps the same sense while protecting accuracy and pedagogy; both are anchored by the **Row ID**.

**10.4 One-way dependency strata prevent conceptual knots.**
Acyclic dependencies cut off circular definitions and policy deadlocks. Dependency strata provide a simple mental model: build on what is already firm.

**10.5 Relation-kind discipline prevents category errors.**
Part-whole claims **(structural)** must rest on **Constructive** grounds (`tv:groundedBy → Γₘ.sum|set|slice`, `validationMode=axiomatic`). Experience-based or evaluative relations **(epistemic)** follow assurance rules (**Logical/Mapping**, and **Empirical Validation** when *postulate*), with an explicit `validationMode ∈ {inferential, postulate}`. Mixing relation kinds inside a single name confuses review and invites hidden assumptions.

**10.6 Sense over string reduces false conflicts.**
Disputes often orbit the string (“we hate that word”). By separating **sense** (what we mean) from **string** (how we say it), the protocol enables peaceful coexistence: keep the **Row ID** constant; use one **Plain** label and, where helpful, a budgeted **alias** per register.


### F.18:11 - Application Guidance (how to apply, step by step)

**11.1 Prepare (30–60 min).**

* Clarify **your Bounded Context** and audience.
* Collect 2–3 typical user stories that require the name.
* Scan near‑neighbors in adjacent contexts (see §14.2 Reviewer checklist).

**11.2 Mint locally.**

* Write the **MDS** in plain language, one paragraph.
* Draft a **Didactic Subtitle** (≤ 12 words): “what this name buys you.”
* Decide whether the intended **relation kind** is **structural** or **epistemic** (do not mix), and declare `validationMode`.

**11.3 Choose labels.**

* **Unified Tech label**: concise, morphology‑stable, neutral; avoid metaphor.
* **Plain label**: approachable phrasing for non‑specialists.
* **How to choose**: pick both **from a small NQD‑frontier** (see §4.2 P1 (candidate set), P2(read-through)): diversify by tradition, novelty/familiarity, and lexical form; record discarded contenders and rationale on the Card.

**11.4 Place in the dependency stratum.**

* Verify all dependencies are at the same dependency stratum or below.
* If a dependency is still Draft/Pilot, keep this name at most Pilot.

**11.5 Align, don’t erase.**

* Where overlap exists with another context, propose an **alignment bridge**.
* Keep your stewardship Context; record the mapping and any known divergence in reading.

**11.5a Keep support-view labels subordinate to the base candidate set or family.**

* When a naming pass talks about one palette, front, archive, shortlist, or candidate set, keep that base candidate set or family recoverable on the Name Card.
* Use thinner support-view wording when the pressure is local comparison across candidate labels, sense-seeds, rejected candidates, or guarded-head notes.
* Use atlas wording only when the naming explanation truly depends on several declared views, spaces, mappings, or distortion qualifiers being visible together, for example one cited `OutcomeMapRef` plus a `BridgeDistortionNote`.
* Those cited spaces or qualifiers stay naming-side reuse of already-declared substrate support; they do not let naming passages mint one new source-to-outcome relation or one new publication posture locally.
* A guarded-head note remains naming governance: it can explain why one head word misleads across admissible readings, but it does not decide substrate stewardship or publication policy.
**11.6 Publish and steward.**

* Publish the name with MDS, subtitle, dependency stratum, stewardship contact, examples.
* Schedule a **first refresh**: when should the stewardship Context examine usage and drift?

**11.7 Deprecate gracefully.**

* If the sense is superseded, publish **Deprecation Notes**: what to use instead, and why. Keep old Working-Names visible long enough to allow safe migration.

**11.8 The “Friday test.”**

* On a busy Friday, could a competent colleague apply the name correctly using only the MDS, subtitle, and two examples? If not, refine before ratification: it is too overloaded with meanings to be helpful.

### F.18:12 - Examples (worked mini‑cases for engineer‑managers)

> These examples are deliberately simple. They show how local-first minting, one-way unification, and dependency-stratum discipline operate together.

**12.1 “Module” vs “Component” (engineering structure).**

* *Stewardship Context A (Platform)* mints **Component** with MDS: “A physically or logically integrated part whose removal would alter the integrity of the whole.” **Structural**.
* *Stewardship Context B (App Team)* mints **Module** with MDS: “A deployable bundle of functionality maintained as a unit.” **Epistemic** (usage practice), not a structural claim.
* **Unification:** An alignment bridge states: “In Platform, every Component may include one or more Modules; Modules are not Parts.” Dependencies are one-way: *Module* depends on *Component*; *Component* does not depend on *Module*. No synonymy asserted. Both names remain in their stewardship Contexts.

**12.2 “Incident” vs “Event” (operational sense).**

* *Stewardship Context C (Operations)* mints **Incident** with MDS: “An unplanned interruption or reduction in the quality of a service.” **Epistemic**.
* *Stewardship Context D (Monitoring)* mints **Event** with MDS: “A recorded observation of a state change in a system.” **Epistemic**.
* **Unification:** Bridge notes: “Some Events are Incidents when they degrade service; not all Events are Incidents.” **Plain** labels (and at most one alias per register) may vary (e.g., “Outage” as an alias for **Incident**), but the **Row IDs** stay distinct. No part‑whole claims are implied.

**12.3 “Customer” vs “Account Holder” (business roles).**

* *Stewardship Context E (Sales)* mints **Customer**: “A party that receives value from an offering in exchange for consideration.” **Epistemic**.
* *Stewardship Context F (Finance)* mints **Account Holder**: “A party legally responsible for an account.” **Epistemic**.
* **Unification:** Bridge states overlaps and divergence: “A Customer can be an Account Holder; an Account Holder may not be a Customer (e.g., trustee).” The stewardship Contexts retain stewardship; a shared Working-Name “Client” may be used in executive materials with a clear note: **Working-Name only; see Concept-IDs for decisions**.

**12.4 “Batch” vs “Lot” (collection vs integration).**

* *Stewardship Context G (Manufacturing)* mints **Batch**: “A collection of items produced under shared conditions.” **Epistemic membership**.
* *Stewardship Context H (Quality)* mints **Lot**: “An integrated whole packaged and tracked as one item.” **Structural whole**.
* **Unification:** Bridge notes: “A **Lot** may originate from a single **Batch** or a slice of a Batch; not every Batch yields a single Lot.” Relation mapping: **MemberOf** (Batch membership) vs **ComponentOf**/**Whole** (Lot integration). *Loss note:* membership evidence does **not** imply part‑whole structure; part‑whole structure does **not** imply shared production conditions.

**12.5 “Palette label” vs “Atlas label” (NQD/OEE naming support).**

* A naming pass compares candidate labels over one active palette and shortlist. The card keeps the active palette recoverable and uses thinner support-view wording, because the question is only which label best fits the current candidate spread.
* Later, the same naming discussion must explain why one label misleads unless the reader can see the palette together with a derived archive, an `OutcomeMapRef`, and one `BridgeDistortionNote`. In that case atlas wording is allowed, but the card still names the base palette and records that the atlas is only optional support for the naming explanation.
* In both cases, guarded-head notes stay on the naming side: they explain alias risk or mismatch patterns, not who stewards the substrate or which publication face is authoritative.
### F.18:13 - Anti‑Patterns & Failure Modes (what to avoid)

**13.1 “Global name first.”**
Trying to coin a single global string before local understanding is mature. **Fix:** mint locally, publish MDS, then align.

**13.2 “Synonym storm.”**
Collecting many strings without stabilizing the Concept-ID. **Fix:** one Concept-ID per sense; multiple Working-Names only if they truly help didactics.

**13.3 “Process leakage into names.”**
Burying workflow or tool steps inside the MDS. **Fix:** keep process in method descriptions; keep names about sense, not procedure.

**13.4 “Member‑implies‑part.”**
Letting collection names induce part‑whole claims. **Fix:** separate names, separate MDS; don’t smuggle structure into membership.

**13.5 “Sideways dependency.”**
Defining a name by appealing to another Draft at the same dependency stratum or higher. **Fix:** depend only downward or postpone ratification.

**13.6 “Alias/Plain drift.”**
Letting a Plain label or alias accumulate extra meanings absent in the underlying row. **Fix:** periodic label review; prune metaphors that start bending sense; respect the alias budget.

**13.7 “Atlas label does substrate work.”**
Letting atlas or support-view language quietly replace the base candidate set or family or decide substrate stewardship or publication policy. **Fix:** keep the base palette, front, archive, or shortlist recoverable, use atlas wording only when several declared views or qualifiers are jointly load-bearing for the naming explanation, and move substrate questions and publication questions to the pattern sections that govern those objects.
### F.18:14 - Assurance & Conformance (human‑only checks)

#### F.18:14.1 - Author checklist (before requesting review).

* [ ] I identified the **stewardship Bounded Context** and audience.
* [ ] I wrote a clear **MDS** (≤ 1 paragraph) and a **Didactic Subtitle** (≤ 12 words).
* [ ] I declared the **relation kind** (structural vs epistemic) and the **validationMode**; no mixing.
* [ ] If **structural**, I can point to **exactly one Constructive trace** that backs the structural claim.
* [ ] I surveyed near‑neighbors and recorded my decision to align, merge, or keep separate.
* [ ] I produced both **Unified Tech** and **Plain** labels (per E.10), with the same sense and pointing to the same **Row ID**.
* [ ] Dependencies point **only downward**; no sideways or upward pulls.
* [ ] If I used support-view or atlas wording, the Name Card still names the base palette, front, archive, shortlist, or candidate set and states why thinner support wording did or did not suffice.
* [ ] I scheduled a **refresh date** and listed 2–3 usage examples.

#### F.18:14.2 - Reviewer checklist (at the gate).**

* [ ] One stewardship Context is declared; stewardship contact is clear.
* [ ] The MDS is free from process jargon and implementation slang.
* [ ] The declared **relation kind** is justified; **structural** claims are constructively grounded; **epistemic** claims declare `validationMode` and evidential posture.
* [ ] Member vs Component is respected where relevant.
* [ ] Alignment bridges are proposed where overlap exists, with explicit reading of convergence/divergence.
* [ ] The dependency-stratum discipline holds: acyclic, downward-only dependencies.
* [ ] The **Plain** label does not smuggle extra commitments; **Unified Tech** and **Plain** remain co‑referential and point to the same **Row ID**.
* [ ] Support-view or atlas wording, if present, leaves the base candidate set or family recoverable and does not smuggle substrate or publication decisions into a naming note.
* [ ] Name-lineage state is accurate (Idea, Draft, Pilot, Ratified, or Deprecated) and dated.

#### F.18:14.3 - Lightweight outcomes.**

* **Ratify** (meets all checks).
* **Pilot** (publish with explicit questions and a refresh date).
* **Revise** (return to author with targeted gaps).
* **Merge** (replace with an alignment to an existing name).
* **Deprecate** (publish successor guidance and sunset plan).

### F.18:15 - Conformance Criteria (normative “CC‑F18”)

> These are **language‑level** obligations for authors and reviewers. They ensure every unified name is **local‑first**, **bridge‑aware**, and **teachable**.

**CC‑F18‑1 (Context first).** Every unified name **SHALL** be grounded in **local senses** that were harvested and clustered **inside named Contexts** (“context of meaning”) prior to unification. No name may be minted from free‑floating glosses or Cross‑context intuition. Use F.1–F.3 first.

**CC‑F18‑2 (Bridge‑only sameness).** Claims of sameness across Contexts **SHALL** be expressed only via explicit **Bridges** with a stated congruence and loss note. Mere spelling similarity never licenses a unified name. Use F.9.

**CC‑F18‑3 (Twin‑register naming).** Each unified concept **SHALL** carry **two labels**—a **Unified Tech** label (used in Core prose) and a **Plain** label (used for teaching). Labels are chosen per the naming discipline of F.5 and the register rules of **E.10**.

**CC‑F18‑4 (Neutrality of the Tech label).** The **Unified Tech** label **SHALL NOT** be borrowed wholesale from any single source Context where that borrowing would re‑import that Context’s private distinctions. Prefer a **neutral** term; **Cross‑context reuse occurs only via the UTS row and explicit Bridges**. (See F.5 “allowed/forbidden forms”.)

**CC‑F18‑5 (One concept per row, one Tech label per row).** A unified concept **SHALL** be captured as **one Concept‑Set row** in the **UTS**. Exactly **one Unified Tech label** is normative for that row; additional deprecated strings are aliases in Annex (budgeted). Use F.7 with F.17.

**CC‑F18‑6 (SenseCell citations).** For each unified name, the **SenseCells** (Context × Local‑Sense) that justify it **SHALL** be cited in the UTS row with **Context name + edition**. Omit edition only if the Context has a single stable edition. See F.17 §6.

**CC‑F18‑7 (Sheet‑level coverage).** Within a thread’s UTS, the **set of rows** carrying unified names **SHALL** collectively cite **≥ 3 distinct Contexts**, ensuring breadth of evidence. Coverage is a property of the **sheet**, not of every single row. See F.17 §6 constraint.

**CC‑F18‑8 (No global words).** In Core text, **“Context” always means `U.BoundedContext`**; **discipline columns** may be used in teaching layouts but **is not** a bearer of meaning. Do not write context‑free claims of sameness. See E.10 and F.17 §5.

**CC‑F18‑9 (Didactic primacy).** A unified name **SHALL** be teachable on **one page**: its **UTS row** + a short narrative that a careful reader can replay (F.16 template). If it cannot be taught concisely, the naming attempt is premature.

**CC-F18-10 (No process-phase connotations).** Names **SHALL NOT** encode imagined “maturity stages” or time-ordering unless those are part of the concept’s intension. Stages belong in **state-space** and dynamics narratives, not in names. (See A-series CHR patterns.)

**CC‑F18‑11 (Strict distinction guard).** Names **SHALL** respect **A.7 Strict Distinction**: do not collapse **Role ↔ Method ↔ Work** or **Status ↔ Description** into one word. Align with F.11/F.12 where relevant.

**CC‑F18‑12 (Change control via F.13).** Renames, splits, merges, and retirements **SHALL** follow F.13’s lexical continuity rules; the UTS remains the canonical public term sheet for these changes.

**CC-F18-13 (Lexical Pareto discipline).** When a Name Card uses **NQD-CAL (C.18)** to score label candidates, the **chosen Unified Tech label** **SHALL** lie on the **Pareto frontier** of the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, MorphologicalActionFit, AliasRisk}` (per **C.16** ordinal discipline and P1’s NQD-front definition), unless an explicit exception is recorded. If authors deliberately select a dominated candidate (e.g., to honour legacy regulation or user muscle memory), the Name Card’s notes **MUST** state the reason for stepping off the frontier.

**CC-F18-14 (NQD-front recorded, with honest diversity).**
When a Name Card is in **MintNew** mode, the **candidate label set** and the resulting **NQD-front of non-dominated label candidates** over the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, MorphologicalActionFit, AliasRisk}` **SHALL** be explicitly recorded on the Card (at least as a small table or list), together with the NQD evidence hooks (`DescriptorMapRef`, `DistanceDefRef`, and a brief `Diversity_P` / coverage summary).
Each candidate **SHALL** carry a **head-term family** tag; morphological or prepositional variants built on the same head (e.g. “X plane”, “plane of X”, “planar X”) **MAY NOT** be counted as distinct for Diversity_P. The Card **SHALL** indicate how many distinct head-term families are represented on the NQD-front.
An NQD-front with fewer than **three** head-term families is permitted **only** if the Card records why no lexically more diverse alternatives survived the SemanticFidelity / AliasRisk filters (e.g., very narrow domain, frozen legacy idiom).

**CC-F18-15 (Selection from the front only).**
The **Unified Tech** and **Plain** labels published on the UTS row for a unified concept **SHALL** be drawn from the currently recorded **NQD-front** on the Name Card. Publishing a Tech/Plain pair that is **not** on that front (or that is dominated with respect to the declared lexical Q-components plus NQD) is **non-conformant**, except in explicit **DocumentLegacy** mode as defined in §5.1.

**CC-F18-16 (Mode declaration).**
Every Name Card **SHALL** declare its `CardMode ∈ {MintNew, DocumentLegacy}`. For Core-facing naming of **U.Types** and other canonical FPF concepts, **MintNew** is the default; **DocumentLegacy** is permitted only when recording pre-existing external names and MUST (i) cite the legacy source, and (ii) either attach an NQD-front over viable FPF variants or record a short rationale why NQD search is out-of-scope. Ordinary local phrase repair has no Name Card mode unless it mints or changes one durable reusable name, UTS row, Core-facing term, or cross-context naming relation.

**CC-F18-17 (Procedure is not optional in MintNew mode).**
A **MintNew** Name Card is **non-conformant** if it records only the chosen label, Kind, and a short rationale while omitting the seed candidate set, the NQD-front, the sense-seed read-through, or the mismatch patterns that justify the final choice. A card filled in after an intuition-first label pick does **not** satisfy F.18.

**CC-F18-18 (Support-view labels keep their base candidate set or family).**
When a Name Card or worked naming note uses support-view or atlas wording, it **SHALL** keep the base palette, front, archive, shortlist, or candidate set recoverable, **SHALL** use atlas wording only when several declared views, spaces, mappings, or qualifiers are jointly load-bearing for the naming explanation, and **SHALL NOT** let guarded-head notes stand in for substrate stewardship or publication policy decisions.
### F.18:16 - Anti‑patterns & safe rewrites (normative)

> Each item names a **speaking error** and a **local‑first repair**. Use this as an author’s lint pass before proposing a unified name.

| #  | Anti‑pattern (do **not** say)                           | Why it fails                                                    | Safe rewrite (how to speak)                                                                                         |
| -- | ------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| A1 | “These terms are the same **because they look alike**.” | Cross‑context **spelling** is not evidence of conceptual identity. | “We assert sameness **via a Bridge**; the loss note explains what survives across Contexts.” (F.9)                     |
| A2 | “Use the BPMN word as our Tech label.”                  | Imports BPMN’s local commitments into the unified term.         | “Choose a **neutral** Unified Tech label; cite BPMN as a **SenseCell** in the row.” (F.5, F.17 §6)                  |
| A3 | “Merge *process* (recipe) with *process* (execution).”  | Collapses **MethodDescription** with **Work**.                  | “Split the concepts: one row for **MethodDescription**, another for **Work**; align them in examples.” (F.11/F.16)  |
| A4 | “Our name encodes the process phase.”                 | Process-phase phrasing sneaks in time.                              | “Name the **concept**; show **state-space** changes in examples, not in the label.” (A-series CHR rationale)        |
| A5 | “Contextless glossary.”                                 | Violates local‑first; readers re‑globalise.                     | “Publish a **UTS** per thread; each row lists **Contexts** (Contexts+editions).” (F.17)                                |
| A6 | “We’ll fix synonyms later.”                             | Synonym sprawl grows costs.                                     | “Apply **E.10** rules now: one Tech, one Plain; retire extras via **F.13**.”                                        |
| A7 | “One mega‑row for everything service‑like.”             | Bundles distinct concepts; harms teachability.                  | “One **Concept‑Set per idea**; group with a **Block Plan** for pedagogy.” (F.17 §7)                                 |



#### F.18:16.1 - Canonical semantic unpacking for “contract” language (normative; used across FPF)

In FPF, everyday “contract” talk is treated as shorthand for a bundle of distinct roles. When precision matters (architecture, audit, compliance), authors **SHALL** avoid mapping “contract” to a single concept and instead disambiguate at least:

* **Service / promise clause (`U.PromiseContent`)** — the promised external effect + acceptance criteria (a spec/Standard), not a run (`U.Work`).
* **Utterance (`U.SpeechAct`)** — the published statement (a Description) that declares or invokes the promise content.
* **Commitment (`U.Commitment`)** — the deontic bond that binds an accountable `U.Agent` or `U.Role` to the promise content.
* **Work & evidence (`U.Work` + carriers)** — the actual enactment and the traces/metrics used to adjudicate fulfilment.

A “contract” bundle typically spans the whole A.6.B square; assign each piece explicitly to its A.6.B value:

* `L-*`: definitions/invariants of the signature (“what it means”).
* `A-*`: admissibility/entry predicates (“when it can be applied”).
* `D-*`: duties/SLAs/penalties and who is accountable (“who is bound to what”).
* `E-*`: evidence/observability claims (“how fulfilment/violation is adjudicated”).

Example 2 (§F.18:18.2) shows one naming instantiation of this unpacking.

### F.18:17 - Migration notes (renames, splits, merges, retirements)

**M1 — Start from Contexts, not from the old global word.** When inheriting legacy names, first **re‑harvest** terms inside the chosen Contexts (F.2–F.3). Only then decide whether to **reuse** or **mint** (F.8).

**M2 — Preserve reader muscle memory without duplicating meaning.** Keep the **Plain** label close to familiar speech, but make the **Tech** label precise. If a legacy term is overloaded, publish it as a **deprecated alias** in Annexes, not as a second Tech label. (F.13; Part H “Deprecated Aliases”.)

**M3 — Prefer split‑then‑bridge over vague merges.** If one legacy word covers two distinct concepts, **split** into two rows and add a short **relation note** between them (e.g., “recipe vs run”). Do **not** hide the split under a wide new name. (F.7; F.16.)

**M4 — Keep identifiers stable; move rows between blocks.** When the **Block Plan** evolves, move rows rather than renumbering; record the move in the row’s **Notes** field. (F.17 §16.)

**M5 — Upgrade rationale quality with worked examples.** Every rename or split should be accompanied by a **one‑page example** that shows the new row in action across at least **two Contexts**. (F.16; “tell‑show‑show”.)


### F.18:18 - Worked examples (compact)

> Each example shows **how the Protocol steers naming** so engineers and managers can communicate without hidden Cross‑context leaks.
> **Card hygiene shown explicitly:** each example **states the Kind and the Purpose/use‑domain** and **chooses Tech/Plain labels from a small NQD‑frontier** (seed set diversified by traditions, novelty/familiarity, and lexical form; see Part G patterns).
> **Head-term diversity:** each example **MUST** also state the **distinct head-term families** represented in its NQD candidate set (lexical “roots” such as *Recipe*, *Run*, *Episode*, not prepositional/morphological variants). This prevents faking Diversity_P with near-clones of one head.

#### F.18:18.1 - Example 1 — *MethodDescription* vs *Work* (recipe vs run)

* **Context harvest:**
  *BPMN 2.0 (2011):* “Process model” (recipe) and “Activity instance” (run).
  *PROV‑O (2013):* `prov:Plan` vs `prov:Activity`.
  *ITIL:* “Work instruction” vs “Change implementation record.”
* **Kind:** `U.MethodDescription` (design‑time record) **and** `U.Work` (run‑time occurrence).
* **Purpose / use‑domain:** planning/scheduling vocabulary across BPMN, PROV‑O, ITIL; separates *design recipe* from *execution episode* for governance and telemetry.
* **NQD‑front (seed candidates):**
  *design‑time:* *Procedure*, *ProcessModel*, *MethodSpec*, *WorkflowDefinition*, *Recipe*, *MethodScript*
  *run‑time:* *Run*, *Execution*, *Enactment*, *ActivityInstance*, *Job*, *Episode*
* **Head-term families used (DesignRunTag):**
  *design-time heads:* {Procedure, ProcessModel, MethodSpec, WorkflowDefinition, Recipe, MethodScript}
  *run-time heads:* {Run, Execution, Enactment, ActivityInstance, Job, Episode}
* **Chosen from frontier (Unified Tech / Plain):**
  `U.MethodDescription` / “recipe”; `U.Work` / “run”.
  *Discarded highlights:* **Procedure** (collides with governance “procedure/policy”); **Execution** (overloaded in CS/security);
* **Anti-pattern (for illustration only, non-conformant).**
 > *Bad CandidateSet (lexically narrow):* {“Reference plane”, “Plane of reference”, “Planar reference”, “Ref. plane v2”}.
 > All four are one **head-term family** (*plane*). Even if Diversity_P over raw strings looks high (four labels), **head-term diversity is 1**, so this set **fails** the F.18 diversity intent. A conformant Card would either: (a) add labels with other heads (e.g., *Layer*, *Track*, *Band*), or (b) explicitly record why other heads are rejected (AliasRisk, domain idiom) and accept low lexical Diversity_P with a rationale.
* **Enactment** (speech‑act nuance).
* **Bridges:** recipe↔run **related**, not identical; loss note “control‑flow vs. execution.”
* **Why it matters:** Managers can schedule **Work** while authors improve the **MethodDescription**—no category errors. The NQD‑front preserves tradition‑diverse, lexically stable options until a reasoned choice is made. (F.11/F.16; F.17 rows.)

#### F.18:18.2 - Example 2 — *Service* (promise) vs *SpeechAct* (utterance) vs *Commitment* (deontic)

* **Context harvest:**
  *IT service canon:* “SLA/OLA clause”, “ticket approved”.
  *Speech‑act theory:* “performative utterance”.
  *Org governance:* “approval signature”.
* **Kind:** `U.PromiseContent` (promise), `U.SpeechAct` (utterance), `U.Commitment` (deontic bond).
* **Purpose / use‑domain:** ops/governance vocabulary connecting ITSM, organizational policy, and pragmatics; separates saying, binding, and promising.
* **NQD‑front (seed candidates):**
  *promise:* *Service*, *Offering*, *Provision*, *CapabilityOffer*
  *utterance:* *SpeechAct*, *Performative*, *Utterance*, *Declaration*
  *deontic bond:* *Commitment*, *Obligation*, *Binding*, *Duty*
* **Chosen from frontier (Unified Tech / Plain):**
  `U.PromiseContent` / “service (promise)”; `U.SpeechAct` / “utterance”; `U.Commitment` / “commitment”.
  *Discarded highlights:* **Offering** (business‑model connotations); **Declaration** (too narrow for performatives); **Obligation** (legalese; narrower than commitment envelope).
* **Ontology note (informative):**
  `U.SpeechAct` and `U.Commitment` are defined normatively in Part A (A.2.9 and A.2.8 respectively). This F.18 card is a lexical/NQD anchor, not the ontology definition site.

* **Bridges:** utterance **institutes** commitment; commitment **binds** promise content; no synonymy claimed.
* **Why it matters:** Status tracking becomes intelligible without pretending that a “service” acts; the NQD‑front yields neutral, cross‑tradition readable labels. (F.12; F.17 blocks D/R.)

#### F.18:18.3 - Example 3 — *Characteristic* names without process-phase bias

* **Context harvest:**
  *Quality canon:* “maturity level”; *Performance canon:* “throughput”.
 **Kind:** `U.Characteristic` (measurement names).
* **Purpose / use‑domain:** CHR‑compatible measurements for planning and performance; bridgeable across engineering and management.
* **NQD‑front (seed candidates):**
  *readiness (ordinal):* *MaturityLevel*, *ReadinessLevel*, *PhaseReadiness*, *TRL*, *ReadinessScore*
  *throughput (ratio):* *Throughput*, *Rate*, *ProcessingRate*, *OpsPerSecond*, *FlowRate*
* **Chosen from frontier (Unified Tech / Plain):**
  `U.ReadinessLevel` / “readiness level” (ordinal); `U.Throughput` / “throughput” (ratio).
  *Discarded highlights:* **TRL** (tied to a specific scale/tradition); **Rate/OpsPerSecond** (over‑specific units baked in).
* **Narrative:** Dynamics are shown as **movement in state-space**, not via process-phase-laden names such as “pre-production process”.
* **Why it matters:** Prevents process phase/time from leaking into labels; the NQD-front ensures neutrality and recognizability. (A-series CHR rationale; F.17 §4-§6.)

### F.18:19 - FAQ (authoring hygiene)

**Q1. How many Contexts must a naming proposal cite?**
**A.** The **sheet** for a thread should cite **≥ 3** distinct Contexts overall; an individual row may cite fewer if the concept appears in fewer Contexts. The point is breadth at the **UTS** level, not token‑stuffing rows. (F.17 §6 constraint.)

**Q2. Can a Source Context’s term ever become the Tech label?**
**A.** Only if its form is **already neutral** and does **not** smuggle in that Context’s private commitments. When in doubt, pick a fresh neutral Tech label and keep the Source term in **SenseCells**. (F.5.)

**Q3. Where do we put discipline‑vantage views like “Operations” vs “Research”?**
**A.** Use the **discipline columns** in a teaching layout if helpful, but remember: **discipline columns are not Context columns** and carry no editions. (F.17 §5.)

**Q4. How do we keep names stable while the story evolves?**
**A.** Keep **row ids** stable; evolve placement via the **Block Plan** and record moves in **Notes**. Use F.13 for renames/splits/merges. (F.17 §16; F.13.)

**Q5. What if two teams insist on different Tech labels for the same concept?**
**A.** Publish **one** Tech label; treat the other as a **deprecated alias** (Annex). Bridge their local senses on the row. (F.13; Part H.)


### F.18:20 - 90‑second teaching script (for engineer‑managers)

> “**Local‑first** means we start in **context of meaning**—we harvest terms **inside** each Context and only then unify. A unified name is a **teachable promise**: one **Tech** label for precision, one **Plain** label for outreach. Its **row** in the **UTS** shows where the idea lives in real disciplines (the **SenseCells**) and how those Contexts connect (explicit **Bridges** with a brief loss note). We never equate terms by spelling; we argue sameness with a **bridge**. We also never bake stages or actors into names—those belong to **dynamics** and **roles**, not labels. When the story changes, we evolve names with **lexical continuity** rather than re‑inventing words. The result is a vocabulary managers and engineers can **hold on one page** and use the same way across projects.”

### F.18:21 - Acceptance Harness (SCR/RSCR) for F.18

**Purpose.** Provide auditable, notation‑independent checks that a proposed unified name (and its publication on a UTS line) satisfies the **local‑first** unification discipline. The harness extends the general unification checks in **F.15** with **naming‑specific** obligations.

#### F.18:21.1 - Static Conformance Rules (SCR‑UNIFY)

| ID                                                                                                                                                                                                       | Requirement (normative “SHALL/SHALL NOT”)                   | Why this exists (conceptual)                                 | Where this is reflected |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| **SCR‑U‑01 (Row‑first).** A unified Tech/Plain name **SHALL** be published **only** on a **Concept‑Set row** whose cells are SenseCells drawn from declared Contexts. No free‑floating names.               | Names are *lenses* onto a defended **row**, not vice‑versa. | **F.7** row‑as‑unit; **F.17** UTS row discipline.            | §F.7; §F.17             |
| **SCR‑U‑02 (Bridge‑only equivalence).** Cross‑context sameness **SHALL** be claimed **only** via an explicit **Bridge** with a relation kind and **CL** + loss/fit note.                                    | Prevents “string‑match identity”.                           | **F.9** Bridges; **F.0.1** principles.                       | §F.9                    |
| **SCR‑U‑03 (Neutral Tech).** The **Unified Tech** label **SHALL** be **neutral**—not lifted wholesale from any single Context **unless** the row’s Concept‑Set shows exact identity.                        | Avoids importing a local worldview as global.               | **F.5** naming neutrality; **F.17** 9.8 naming neutrality.   | §F.5; §F.17             |
| **SCR‑U‑04 (Twin registers).** Each row **SHALL** carry **Tech** and **Plain** names with the Part E register discipline; Plain is teacher‑friendly, Tech is morphology‑stable.                          | Satisfies didactic primacy without jargon creep.            | **E.10** registers; **F.5** naming rules.                    | §E.10; §F.5             |
| **SCR‑U‑05 (No window‑in‑name).** Variations by **time/phase/scale** **SHALL** be handled by **applicability windows** on **Statuses** (or examples), **NOT** by baking modifiers into the unified name. | Prevents type/status explosion by adjectives.               | **F.10/F.12** windows; **F.14** explosion guard.             | §F.10; §F.12; §F.14     |
| **SCR‑U‑06 (Heterogeneity).** A UTS block **SHALL** demonstrate **≥ 3** independent domain families across its rows, or an explicit Bias‑Annotation shall scope the claim.                               | Enforces trans‑disciplinary reach or honest scope.          | **F.17** invariants 3; **E.8** Bias‑Annotation.              | §F.17; §E.8             |
| **SCR‑U‑07 (Member≠Component sanity).** Names **SHALL NOT** imply holarchic composition when the row unifies **collections**; keep **MemberOf** distinct from **ComponentOf**.                           | Stops structural category errors.                           | Part F principles / anti‑patterns.                           | §9.8; §13               |
| **SCR‑U‑08 (One‑breath rationale).** Each row **SHALL** include a **single‑sentence** Unification Rationale that states **why** the cells belong in the same Concept-Set row despite wording differences.             | Keeps the argument visible and auditable.                   | **F.17** invariant 7.                                        | §F.17                   |
| **SCR‑U‑09 (Alias budget).** Per register, deprecated aliases on a unified name **SHALL** be **≤ 1**; additional deprecated labels go to Annex/Glossary.                                                         | Controls lexical drift while preserving continuity.         | **F.13** alias budget rule.                                  | §F.13                   |
| **SCR‑U‑10 (No Cross‑context rename).** A rename **SHALL** occur **within** the same Context or same row; Cross‑context “renames” are **prohibited**—use Bridges.                                                 | Keeps locality intact; forbids silent conflation.           | **F.13** continuity; **F.9** Bridges.                        | §F.13; §F.9             |
| **SCR‑U‑11 (Semantic read‑through).** A unified Tech/Plain name **SHALL** pass a **semantic read‑through**: the Name Card lists **5–10 diverse NQD archetypal situations** and the **NQD‑front notes** record rejected candidate and their **mismatch patterns**. | Prevents labels that mislead across the intended situations; ties lexical choice to demonstrated use. | §F.18 §4.2; §F.18 §5. | §F.18 |

#### F.18:21.2 - Regression Rules (RSCR‑UNIFY)

| ID                                                                                                                                                                       | Regression duty across editions                                        | Effect |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------ |
| **RSCR‑U‑E01 (Edition drift).** When a source Context updates, re‑validate the row: stable sense ⇒ **rename/alias**; changed sense ⇒ **split/merge** rows; never overwrite. | Preserves truthfulness without erasing history. **F.13** RSCR.         |        |
| **RSCR‑U‑E02 (CL honesty).** Bridges **SHALL NOT** increase their CL (claiming higher-CL sameness) without new witnesses; **SHOULD** reduce CL when editions diverge.     | Guards against optimism bias in equivalence. **F.17** migration cues.  |        |
| **RSCR‑U‑E03 (Alias creep).** Periodically prune aliases to the **≤ 1** budget per register.                                                                             | Maintains narratively crisp UTS. **F.13** RSCR‑Alias.                  |        |
| **RSCR‑U‑E04 (Name neutrality check).** If the Unified Tech label is traceable to one context’s idiom, re‑justify neutrality or retitle the row.                            | Keeps the name “ours,” not “theirs.” **F.17** 9.7–9.8.                 |        |
| **RSCR‑U‑E05 (Window misuse).** Reject newly proposed types that are really **windows** on an existing Status/Role.                                                      | Prevents explosion by adjectives. **F.14** S14/E11 patterns.           |        |

### F.18:22 - Migration & Deprecation Notes (informative, naming‑specific)

1. **Start from rows, not strings.** When consolidating legacy labels, **build or revisit the Concept‑Set row** first; only then pick the **Unified Tech/Plain** names. This keeps **meaning** primary. **(F.7, F.17)**
2. **Prefer alias over merge.** If the *sense* is stable but the label misleads, **rename and retain one alias**; if the sense changed, **mint a new row** (no retrofits). **(F.13)**
3. **Resist modifier types.** New adjectives (e.g., *Peak*, *Remote*, *Night*) usually belong to **windows** or **examples**, not to the unified name. **(F.10/F.12/F.14)**
4. **Keep neutrality visible.** If stakeholders push a brand‑coloured label, document why the chosen **Unified Tech** is **neutral** and include the brand as an **alias** in Glossary/Annex. **(F.5, F.17)**
5. **Don’t globalise a Context.** Never move a Context label into the unified name as if it were universal. Use **Bridges** to relate Contexts, with an explicit **loss note**. **(F.0.1, F.9)**

### F.18:23 - FAQ (authoring hygiene for engineer‑managers)

**Q1. Can we reuse a dominant industry term as the Unified Tech name?**
**A.** Only if the row’s Concept‑Set shows **exact identity** across Contexts; otherwise pick a **neutral** Unified Tech and list the industry label as an **alias** in the Glossary. **(F.5, F.17)**

**Q2. Two terms look identical across Contexts—may we skip Bridges?**
**A.** No. **Sameness is argued, not spelled.** Publish a **Bridge** with relation kind and **CL** plus a short **loss/fit** note. **(F.9, F.0.1)**

**Q3. When do we mint a new U.Type vs. add a new row vs. add an alias?**
**A.** Use **F.8 Mint‑or‑Reuse**: if the *intension* changes, **new U.Type**; if cross-context alignment needs a new Context, **new row**; if only the label misleads, **alias/rename**.

**Q4. Our team keeps proposing “qualified roles” (e.g., *Night‑Operator*). What do we do?**
**A.** Keep the **Role** unified and express qualifiers as **windows** on **Statuses** or as **example context**. This follows **F.14** and **F.12**.

**Q5. Can we compress two near‑equivalent rows into one to “simplify the sheet”?**
**A.** Only if the **one‑breath rationale** remains true after review and the Bridges support equivalence with the same CL, or a higher CL only when new witnesses justify it; otherwise keep **two rows** with explicit differences. **(F.17, F.9)**

### F.18:24 - Didactic distillation (90‑second script)

> **“Name on a row, never on a whim.”** In FPF we **speak on rows, not on vibes**: a **Name Card** ties each Tech/Plain pair to a concrete Context, Concept‑Set row, and SenseCells, with a small **NQD‑front** of rejected alternatives. This gives you **bridged precision** without losing **local comfort**. **Your UTS is the one page a careful mind can hold.**

### F.18:24a - Name-card guardrails for set-candidate language

- Keep `Palette`, `Front`, `Archive`, and `Shortlist` as distinct head families rather than as aliases of one generic `portfolio`.
- Prefer this head family when the local entry load matches it:
  - `TraditionPalette` when `SubjectKind=Tradition`
  - `Q-Front`
  - `ExplorationArchive`
  - `Shortlist`
- The shortlisted family stays internally coherent:
  - `RankedShortlist ⊑ Shortlist`
  - `ShortlistId` is one `Id` specialized to an emitted shortlist
  - `ChoiceSet` may appear only as one mathematical gloss for the shortlist's set object, not as one rival public head
- Reserve `Pareto` for actual non-domination under a declared `DominanceSet`; do not use it for weighted ranking, popularity ordering, or one post-lens shortlist.
- Treat bare `portfolio` as a guarded reject here because current `FPF` already uses `portfolio` as one broader selector/set-return family. When the local set family is recoverable, do not reuse that broader head as the local winner.
- Treat bare `shortlist` as admissible only when the selected-set family is intended and the declared source set kind plus the named lens are already recoverable nearby.
- When one set-family candidate is tied to traditions, methods, hypotheses, or environment-method pairs, say the `SubjectKind` explicitly instead of letting the head noun do the work by implication.
- When one shortlist is emitted from one front or one archive, say the declared source set kind and the named lens instead of letting `Shortlist` drift into one generic selector result.
- If one local explanation still needs `ChoiceSet`, say that it is the mathematical set gloss for the shortlist rather than letting it read like one second public set family.
- Good examples include `TraditionPalette` for a tradition-member palette, `Palette + SubjectKind=MethodFamily`, `Q-Front`, `ExplorationArchive`, `ShortlistFromQFront`, `RankedShortlistFromShortlist`, and `ShortlistId`.
- Bad examples include bare `portfolio`, `SoTA portfolio`, `Pareto shortlist`, `Pareto archive`, and `frontier set` when the declared dominance basis is still missing.

### F.18:25 - SoTA-Echoing (post-2015 practice alignment)

F.18 is local-first, kind-bound, and context-bound naming discipline. Its SoTA support must not make ordinary naming look mathematically certified. Mathematical and search traditions are admitted only when they make the Name Card more reviewable for the current naming problem.

* **Terminology work, especially ISO 704:2022 and ISO 1087:2019.** This is the direct practice support for term formation, designation, definition, and concept discipline. F.18 adopts the requirement that a reusable name must keep its kind, context, intended use, and definition recoverable, while rejecting dictionary substitution and global vocabulary rows as sufficient naming work.
* **Word-sense disambiguation and sense evaluation.** P2's sense-seed read-through is a human-scale analogy: test a candidate name against several intended-use situations and record error patterns. WSD does not prove that a Name Card must use `theta_P`, sense-seed thresholds, or any particular numeric cut-off. Those remain FPF authoring choices that are admissible only when they improve local reviewability.
* **Quality-diversity and multi-objective search, including MAP-Elites and NSGA-II families.** P1's NQD-front and **CC-F18-13** adapt the design-space lesson: keep several diverse good candidates visible instead of collapsing too early to one scalar winner. This does not validate lexical candidate selection by itself. Pareto or frontier wording is admissible only when the lexical Q-components are explicit, inspectable, and used under the ordinal discipline of C.16.
* **Design-space exploration and idea ranking in mechanical and industrial design.** Name-Card candidate tables may borrow the habit of comparing alternatives on several visible criteria. The practical gain is auditability of rejected candidates, not a claim that naming has become an engineering optimization problem.
* **Semantic transparency and morphology in interfaces and code.** These traditions support readable labels and error prevention where comprehension is live. F.18 adapts them into MorphologicalActionFit and local head-term checks, while rejecting readability as proof that the name is ontologically correct.

### F.18:26 - Relations

**Builds on:**
**F.0.1** Contextual Lexicon Principles (local meaning; bridge‑only Cross‑context claims). **F.1–F.3** Contexts → term harvesting → local sense clustering. **F.5** Naming discipline. **F.7** Concept‑Set construction. **F.8** Mint‑or‑Reuse decision lattice. **F.13** Lexical continuity (renames/aliases/splits/merges). **F.14** Anti‑explosion controls (bundles, SoD, windows). **F.15** SCR/RSCR harness. **F.17** UTS as the public term sheet.

**Constrains:**
All patterns that propose or consume unified names and rows in Part F; any Part A/C pattern that cites U.Types on UTS rows inherits these naming duties (through the UTS linkage), while keeping **structural/epistemic/temporal** aspects distinct per Part E authoring rules.

**Coordinates with.**
**A.17/A.18** for measurement lexicon when rows concern measurable notions (Characteristic/Scale/Level/Coordinate vocabulary), ensuring neutral naming aligns with canonical terms and eases external alignment via Bridges.

### F.18:End
# Part G – Discipline SoTA Patterns Kit

## G.Core - Part G Core Invariants

**Tag.** Architectural pattern (Part‑G core invariants hub; refactoring/deduplication)
**Stage.** *design‑time* (authoring discipline + ID‑stable citation discipline; no run‑time mechanism)
**Primary hooks.** E.8 (pattern template), E.10 (lexical/ontological rules), E.19 (conformance discipline), A.6.7 (SuiteObligations + suite protocol pins), A.15.3 (planned baseline), A.19 (CN‑Spec), G.0 (CG‑Spec), A.19.CHR (CHR suite boundary), C.23 (SoS‑LOG), F.17 (UTS), F.15 (RSCR).

**Status.** Stable
**Placement.** Part G core section before `G.0` (without renumbering `G.0…G.13`).
**Normativity.** Normative unless explicitly marked informative

**Purpose.** Provide *one governing definition* for Part‑G‑wide invariants (**delegation-first citation and change-control discipline**), plus a typed **RSCR trigger kind catalogue** and a **Default Governing Definition Index**, so Part G can be refactored without semantic drift or public‑ID breakage.

**Phase‑2 constraint.** `G.Core` is the only new Part‑G pattern introduced in Phase‑2; discipline/method/generator specifics remain in `G.x` as `Extensions`, citations to existing governing patterns, or Phase‑3 seeds (appendix) without new Phase‑2 norms.

**Post‑Phase‑2 evolvability policy.** The Phase‑2 restriction above is historical. From Phase‑3 onward, new Part‑G `PatternId`s are permitted when (i) they introduce a genuinely new **kit/pack class** (typically levels `G.2–G.5`), or (ii) they are required to preserve **one governing pattern per wiring extension** and wiring-only separation. Method/discipline/generator specifics SHOULD still default to `GPatternExtension` modules under `G.x:Extensions` (scoped by `PatternScopeId = G.x:Ext.*` and `GoverningPatternId`), rather than adding new Part‑G patterns.

### G.Core:1 - Problem frame

Part G contains patterns for CG‑frame characterization and its downstream artefacts (cards, evidence graphs, bridge surfaces, refresh/shipping orchestration, parity harnesses, dashboards, interop surfaces). In the current spec, several invariants are already present as **suite obligations/protocol norms** and are **reused across Part G**.

*Part‑G‑wide* invariants are governed by `G.Core` so every `G.x` can:

* cite the core invariants rather than restating them, and
* isolate pattern-scoped specifics as `Extensions` without turning each `G.x` into a mixed bag of universal rules, kit surfaces, and method/generator descriptions.

This pattern (`G.Core`) therefore acts as the **deduplication hub** for FPF Part G.

### G.Core:2 - Problem

Without one governing definition for Part‑G‑wide invariants, Part G drifts in at least six recurring ways:

1. **Shadow governing spec refs** emerge: downstream patterns restate CN‑Spec / CG‑Spec constraints, accidentally creating “local specs” that can diverge from the canonical governing spec refs.
2. **Crossing discipline becomes inconsistent**: “crossing events” and “crossing visibility” are described differently across `G.x`, causing ambiguity about what must be pinned (UTS/Path/policy‑ids/editions) and what triggers refresh/regression.
3. **Guard semantics drift**: tri‑state eligibility and “unknown handling” can be reinterpreted in local prose, producing hidden fourth statuses or implicit coercions.
4. **Hidden scalarization appears**: partial orders are silently collapsed into scalars, or totalization is introduced implicitly through “helpful” numeric summaries.
5. **Suite/kit/pack mixing blurs governing-definition assignment**: downstream patterns drift into “governing” what should remain governed by the suite boundary (`A.6.7` and `A.19.CHR`), kit surfaces (each `G.x`), or shipping (`G.10`).
6. **Refactoring breaks public IDs**: CC items and trigger labels become hard to evolve because removing duplicates risks breaking external references.

Part G requires a single place where these invariants and refactoring disciplines live, while keeping Part G patterns modular and method/discipline specifics explicitly separated.

### G.Core:3 - Forces

* **One governing definition vs. usability:** We must centralize universal invariants, but `G.x` must remain readable and pattern-scoped for authors.
* **Delegation-first vs. completeness:** Many norms already have canonical governing definitions such as `A.6.7`, `A.15.3`, `A.19`, `G.0`, `A.19.CHR`, and the relevant Part E patterns. `G.Core` must cite those governing definitions rather than duplicating semantics.
* **Public-id and alias continuity:** Public CC IDs and deprecated trigger labels must remain stable as labels; deduplication must not break citations.
* **Typed change control:** RSCR/refresh must become *id‑based* (catalogued trigger kinds) rather than prose-based “meaning”.
* **Strict distinction:** Keep governing spec refs (CN‑Spec, CG‑Spec), suites, kits/surfaces, policies, planned baselines, audits, and refresh orchestration distinct.
* **Minimal specificity naming:** New IDs must be kind‑suffixed and minimally specific, to reduce semantic lock‑in while remaining precise.
* **Phase‑2 scope discipline:** `G.Core` must not become a container for discipline/method/generator taxonomies; those remain pattern-scoped (`Extensions`), delegated to existing governing patterns, or marked Phase‑3 seeds (appendix) without new Phase‑2 norms.

### G.Core:4 - Solution

`G.Core` establishes Part‑G‑wide invariants as **delegation rules + typed catalogs + authoring discipline**.

#### G.Core:4.1 - Delegation-first citation for Part‑G‑wide invariants

`G.Core` is a *citation hub*, not a “second spec”. For any Part‑G‑wide invariant that already has a governing definition, `G.Core`:

1) standardises naming via `SuiteObligations.*` (A.6.7:4.2), and
2) records where the invariant is governed, so downstream patterns cite rather than restate.

**Delegation table (normative index; no semantic duplication).**

| Obligation handle | Canonical governing definition(s) | Part‑G note |
| --- | --- | --- |
| `transport_declarative_only` + `cg_spec_cite_required_for_numeric_ops` | A.6.7 + A.19 (CN‑Spec) + G.0 (CG‑Spec) + A.19.CHR | CN/CG are *pins*, not copies (“governing spec refs are pins, not copies”). No embedded/shadow governing spec refs. |
| `bridge_only_crossings` | A.6.7 + E.18 | Any cross-Context or cross-plane/kind move is Bridge‑mediated; no implicit crossings. |
| `crossing_visibility_required` | E.18 (CrossingBundle) + A.6.7 | Crossing visibility is a published **CrossingBundle**. `edition_key` changes on **crossing‑relevant artefacts** (Bridge/CL surfaces, BridgeCards, CrossingBundle registries, and UTS rows for crossing artefacts) are treated as crossing-bundle edits. If the required CrossingBundle is missing/non‑conformant, downstream consumers MUST **abstain** from cross-Context or cross-plane reuse (no silent crossings). |
| `two_bridge_rule_for_described_entity_change` | A.6.7 | describedEntity retargeting requires an explicit KindBridge (`CL^k`) in addition to any Context/Plane Bridge. |
| `guard_decision_tristate(pass|degrade|abstain)` + `unknown_never_coerces_to_pass` | A.6.7 + C.23 | `GuardDecision := {pass|degrade|abstain}` only; `unknown` maps to `degrade`/`abstain` via explicit SoS‑LOG branch/policy pins. |
| `penalties_route_to_r_eff_only` | A.6.7 | Penalties affect the **R lane (R_eff)** only; **F/G invariants** must not be altered by penalties. |
| `no_silent_scalarisation_of_partial_orders` + `no_silent_totalisation` | A.6.7 | Partial orders stay set‑valued; no silent scalar ranks or “helpful” totalisation. |
| `planned_slot_filling_in_work_planning_only` + `finalize_launch_values_in_work_enactment_only` + `gate_decision_separation` | A.15.3 + A.19.CHR + A.6.7 | Planned baselines are WorkPlanning‑only; launch/finalization values are WorkEnactment‑only; planning does not govern GateDecision/DecisionLog semantics. |
| `DefaultGoverningDefinitionIndex.single_governing_definition_per_DefaultId` | this pattern | Any default names exactly one governing definition; `G.Core.DefaultGoverningDefinitionIndex` is an index, not a second spec. |

This pattern also governs four pieces of Part‑G‑wide infrastructure that are **not** already governed elsewhere:

* the typed **RSCRTriggerKindId catalogue** (single writer),
* the **Default Governing Definition Index** (one governing definition per DefaultId; index only), and
* the **Δ‑discipline** for ID‑stable deduplication (delegation without public‑ID breakage), and
* the **linkage compression catalogues** (`GCoreConformanceProfileId`, `GCoreTriggerSetId`, `GCorePinSetId`) used to keep `G.x` linkage sections small.

#### G.Core:4.2 - Mandatory `G.Core linkage` manifest requirement for every `G.x`

Every pattern `G.x` in Part G SHALL include a short, explicit **Core linkage** section that is notation‑independent and id‑based.

* Relations: `Builds on: G.Core`.
* Solution: include a section named `G.x:<n> - G.Core linkage (normative)` that contains a `GCoreLinkageManifest` listing, at minimum:

  * `CoreConformanceProfileIds := { GCoreConformanceProfileId… }` *(preferred)* and/or `CoreConformanceIds := { CC‑GCORE‑… }`
  * `RSCRTriggerSetIds := { GCoreTriggerSetId… }` *(preferred)* and/or `RSCRTriggerKindIds := { RSCRTriggerKindId… }`
  * `CorePinSetIds := { GCorePinSetId… }` *(preferred)* and/or `CorePinsRequired := { … }` *(pins/refs surfaced by the kit; include policy‑id pins and edition pins when applicable; list only additions/overrides if pin sets are used)*
  * `DefaultsConsumed := { DefaultId… }` *(ids only; governing definition is resolved via `G.Core.DefaultGoverningDefinitionIndex`; cite governing definition, don’t restate)*
  * `TriggerAliasMapRef?` *(present or cited) if the pattern uses local trigger tokens*

**Nil‑elision (normative size rule).** Any field whose value is `∅` MAY be omitted; omission means `∅` and does not relax any obligation.

**Expansion rule (normative).** If profile/set ids are used, the effective `CoreConformanceIds` / `RSCRTriggerKindIds` / `CorePinsRequired` are the unions of their expansions plus any explicitly listed ids (see `G.Core:4.2.2`, `G.Core:4.2.3`, and `G.Core:4.3.4.2`).

##### G.Core:4.2.1 - `GCoreLinkageManifest` (canonical shape)

`GCoreLinkageManifest` is the minimal, pattern‑local wiring manifest for citing `G.Core` without duplicating universal prose.

A `G.x` MAY render the manifest as prose, a table, or structured notation, but the ids SHALL be recoverable by authoring review:

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds?: {GCoreConformanceProfileId…},
  CoreConformanceIds?: {CC‑GCORE‑…},
  RSCRTriggerSetIds?: {GCoreTriggerSetId…},
  RSCRTriggerKindIds?: {RSCRTriggerKindId…},
  CorePinSetIds?: {GCorePinSetId…},
  CorePinsRequired?: {…pin ids…},
  DefaultsConsumed?: {DefaultId…},
  TriggerAliasMapRef?: TriggerAliasMapRef
⟩`

##### G.Core:4.2.2 - `GCoreConformanceProfileId` catalogue (compression primitive)

A `GCoreConformanceProfileId` is a stable identifier for a named set of `CC‑GCORE‑*` items. It exists solely to reduce repetition in `G.x` linkage sections (no new semantics).

| GCoreConformanceProfileId | Expands to `CC‑GCORE‑*` (set) | Notes |
| --- | --- | --- |
| `GCoreConformanceProfileId.PartG.AuthoringBase` | `{CC‑GCORE‑CN‑CG‑1, CC‑GCORE‑CROSS‑1, CC‑GCORE‑PEN‑1, CC‑GCORE‑SET‑1, CC‑GCORE‑P2W‑1, CC‑GCORE‑DEF‑1, CC‑GCORE‑TRIG‑1, CC‑GCORE‑TRIG‑2, CC‑GCORE‑TRIG‑3, CC‑GCORE‑TRIG‑4, CC‑GCORE‑ID‑1, CC‑GCORE‑ID‑2, CC‑GCORE‑LINK‑1, CC‑GCORE‑LINK‑2}` | Default baseline for most Part‑G kits. |
| `GCoreConformanceProfileId.PartG.TriStateGuard` | `{CC‑GCORE‑GUARD‑1}` | Add when the kit defines/consumes eligibility/guard outcomes. |
| `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted` | `{CC‑GCORE‑UTS‑1}` | Add when the kit mints/evolves public ids (UTS rows). |
| `GCoreConformanceProfileId.PartG.ShippingBoundary` | `{CC‑GCORE‑SKP‑1}` | Add when shipping boundaries are in scope for the kit. |

##### G.Core:4.2.3 - `GCorePinSetId` catalogue (compression primitive)

A `GCorePinSetId` is a stable identifier for a named set of commonly recurring **pin obligations** used in Part‑G kits. It exists solely to reduce repetition in `G.x` linkage sections (no new semantics).

**Conditional pins (normative).** In pin‑set expansions below, a pin marked with `?` is **conditional**: it **MUST** be present iff the pattern actually uses the corresponding surface/artefact class; otherwise it MAY be omitted (nil‑elision permitted) and is treated as `∅`. A `G.x` MAY strengthen a conditional pin to unconditional by listing it explicitly in `CorePinsRequired`.

| GCorePinSetId | Expands to `CorePinsRequired` (set) | Notes |
| --- | --- | --- |
| `GCorePinSetId.PartG.AuthoringMinimal` | `{CG-FrameContext, describedEntity := ⟨GroundingHolon, ReferencePlane⟩, CNSpecRef.edition, CGSpecRef.edition}` | Baseline scope+spec pins for most Part‑G authoring kits (design‑time, citable, refreshable). |
| `GCorePinSetId.PartG.CrossingVisibilityPins` | `{BridgeId/BridgeCardId, BridgeMatrixId?, CL/CL^k/CL^plane, Φ/Ψ/Φ_plane policy-ids, CrossingBundleId?, UTSRowId[]?, PathId[]/PathSliceId[]?}` | Use when the kit asserts or consumes crossings (Bridge‑only + visible). Conditional pins cover “only if that bundle is used” cases (UTS publication, path‑citable evidence, explicit CrossingBundle reference). |

#### G.Core:4.3 - RSCR Trigger Catalogue and docking discipline

`G.Core` is the **single writer** for Part‑G‑wide trigger kinds.

##### G.Core:4.3.1 - Definitions

* **RSCRTriggerKindId**
  Canonical, stable identifier for a *trigger kind* (a class of “why RSCR/refresh must fire”). Cross-pattern reason code.

* **RSCRTriggerAliasId**
  Pattern-scoped human label/token kept for ergonomics and alias continuity (e.g., `G.11:T4`, `G.6:H3:lane-tag correction`).

* **TriggerAliasMap**
  Mapping table: `RSCRTriggerAliasId → {RSCRTriggerKindId…}` (1..n).

* **RSCRTrigger**
  Minimal conceptual form (notation-independent):

  ```
  RSCRTrigger := ⟨
    triggerKindId: RSCRTriggerKindId,
    scope: PathSliceId[] | PathId[] | PatternScopeId,
    payloadPins: { …id pins… }
  ⟩
  ```

  Where `payloadPins` contains any edition pins, policy-ids, Bridge ids, evidence pins, regression-set ids, etc., required to make the trigger actionable.

##### G.Core:4.3.2 - Governing-definition model

* TriggerGoverningDefinition := `G.Core`.
* Any new trigger kind SHALL be added to `G.Core` first.
* Other patterns MAY define aliases only (or cite shared alias maps), and MUST map aliases to canonical kinds.

##### G.Core:4.3.3 - Authoring rules

* **No implicit triggers:**
  Any RSCR/SCR/refresh artefact that *records reasons* MUST record canonical `RSCRTriggerKindId`. Aliases may be recorded as labels, but must not be the only reason code.

* **No implicit overloading:**
  A local token string (e.g., `T4`) SHALL NOT silently change meaning across patterns; namespace is part of the alias (`G.11:T4` ≠ `A.20:T4`).

* **Granularity discipline:**
  If a local cause is narrower than an existing canonical kind, map it to that kind and keep the nuance as a local scope note. If the difference matters for planning/selection, add a new canonical kind.

* **Multi-cause discipline:**
  When an event spans multiple canonical kinds, record multiple triggers (preferred) or map the alias to a set `{…}` and require emitting the full set.

##### G.Core:4.3.4 - Seed canonical catalogue (Phase‑2 minimum)

The Phase‑2 stabilized canonical catalogue (based on the Phase‑2 inventory; sufficient to dock deprecated `G.6:H3` and `G.11:T0…T7` trigger labels and to populate `RSCRTriggerKindIds` in `G.0…G.13`):

* `RSCRTriggerKindId.LegalitySurfaceEdit`
* `RSCRTriggerKindId.PenaltyPolicyEdit`
* `RSCRTriggerKindId.CrossingBundleEdit`
* `RSCRTriggerKindId.ReferencePlaneEdit`
* `RSCRTriggerKindId.EditionPinChange`
* `RSCRTriggerKindId.TokenizationOrNameChange`
* `RSCRTriggerKindId.PolicyPinChange`
* `RSCRTriggerKindId.TelemetryDelta`
* `RSCRTriggerKindId.FreshnessOrDecayEvent`
* `RSCRTriggerKindId.EvidenceSurfaceEdit`
* `RSCRTriggerKindId.MaturityRungChange`
* `RSCRTriggerKindId.BaselineBindingEdit`
* `RSCRTriggerKindId.DefaultGoverningDefinitionChange`

##### G.Core:4.3.4.1 - Canonical kind definitions (normative, minimal)

Each `RSCRTriggerKindId` SHALL have a short, stable definition in `G.Core` (single-writer) to prevent semantic drift.

| RSCRTriggerKindId | Minimal meaning (cause class) | Typical payload pins (non-exhaustive) |
| --- | --- | --- |
| `RSCRTriggerKindId.LegalitySurfaceEdit` | A legality surface changed (CG‑Spec: ComparatorSet/SCP/Γ_fold/MinimalEvidence, or equivalent legality inputs). | `CGSpecRef.edition`, `ComparatorSetRef.edition`, `SCPRef.edition`, `ΓFoldRef.edition` |
| `RSCRTriggerKindId.PenaltyPolicyEdit` | A penalty / Φ / Ψ / FailureBehavior / SoS‑LOG branch policy changed. | penalty policy ids, `Φ`/`Ψ` policy ids, SoS‑LOG branch id pins |
| `RSCRTriggerKindId.CrossingBundleEdit` | A crossing bundle changed (Bridge/CL routing, crossing-bundle registry cards, crossing policy pins), including `edition_key` changes of crossing‑relevant artefacts (BridgeCards, CrossingBundle registries, UTS rows for crossing artefacts). | `BridgeId/BridgeCardId`, `BridgeMatrixId?`, `CL*` ids, crossing policy ids, `UTSRowId[]`, `PathId/PathSliceId?` |
| `RSCRTriggerKindId.ReferencePlaneEdit` | ReferencePlane or plane-routing surface changed. | `ReferencePlaneId`, plane-policy ids |
| `RSCRTriggerKindId.EditionPinChange` | Any pinned edition relevant to downstream artifacts changed (including **`CNSpecRef.edition`**, `CGSpecRef.edition`, comparator/method/descriptor/distance/etc.). Crossing‑artefact edition_key changes are additionally classified as `CrossingBundleEdit` per multi‑cause discipline. | changed `*.edition` pins, affected `PathSliceId`s |
| `RSCRTriggerKindId.TokenizationOrNameChange` | A published tokenization / naming / alias surface changed in a way that can affect docking, citations, or dispatch (e.g., UTS Name Cards, twin labels, alias maps). | affected `UTSRowId[]`, `NameCardId[]`, alias ids / maps |
| `RSCRTriggerKindId.PolicyPinChange` | A policy-id pin used by characterization changed (selection, insertion, emission, routing, refresh policy, etc.). | policy ids (and other non-edition configuration pins when they are explicitly pinned) |
| `RSCRTriggerKindId.TelemetryDelta` | Telemetry inputs that influence refresh/selection changed (not merely display-only). | telemetry ids/refs, `Audit`-published pins |
| `RSCRTriggerKindId.FreshnessOrDecayEvent` | Time/freshness/decay conditions affecting validity changed (window shift, decay thresholds, freshness policy edits). | freshness window refs/ids, decay/freshness policy ids |
| `RSCRTriggerKindId.EvidenceSurfaceEdit` | Evidence graph / evidence surface changed in ways that affect admissibility/acceptance/comparison. | evidence pins, `EvidenceGraph` refs, affected `PathId`s |
| `RSCRTriggerKindId.MaturityRungChange` | Maturity rung/ladder state changed for relevant artifacts or paths. | maturity rung ids, affected scopes |
| `RSCRTriggerKindId.BaselineBindingEdit` | Planned baseline bindings changed (planned slot fillings / binding refs), requiring a re-run along the P2W path. | `SlotFillingsPlanItem` refs, planned pins, variance pins |
| `RSCRTriggerKindId.DefaultGoverningDefinitionChange` | The governing definition of a `DefaultId` (as recorded in `G.Core.DefaultGoverningDefinitionIndex`) changed, or a default row was added/deprecated. | affected `DefaultId.*`, old governing definition ref, new governing definition ref |

##### G.Core:4.3.4.2 - Canonical trigger sets (compression primitive)

`GCoreTriggerSetId` identifies a named set of `RSCRTriggerKindId` values. A `G.x` MAY cite trigger sets in `RSCRTriggerSetIds` instead of repeating long `RSCRTriggerKindIds` lists.

| GCoreTriggerSetId | RSCRTriggerKindIds (set) | Notes |
| --- | --- | --- |
| `GCoreTriggerSetId.CGSpecGate` | `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}` | Covers CG‑Spec legality‑gate kits (e.g., `G.0`). |
| `GCoreTriggerSetId.SoTAHarvestSynthesis` | `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}` | Covers SoTA harvesting/synthesis packs (e.g., `G.2`). |
| `GCoreTriggerSetId.EvidenceGraphKit` | `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.BaselineBindingEdit}` | Covers EvidenceGraph/SCR kits (e.g., `G.6`). |
| `GCoreTriggerSetId.BridgeCalibrationKit` | `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.BaselineBindingEdit}` | Covers bridge calibration/CL kits (e.g., `G.7`). |
| `GCoreTriggerSetId.RefreshOrchestration` | `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.BaselineBindingEdit}` | Covers refresh orchestration (e.g., `G.11`). |

##### G.Core:4.3.5 - Initial alias maps

These alias maps are normative docking artefacts and preserve deprecated alias labels while moving semantics to canonical ids.

**TriggerAliasMap.G11**
Based on the existing trigger catalogue in `G.11` (`T0…T7`).

* `G.11:T0 → { RSCRTriggerKindId.PolicyPinChange }`
* `G.11:T1 → { RSCRTriggerKindId.TelemetryDelta }`
* `G.11:T2 → { RSCRTriggerKindId.EditionPinChange }`
* `G.11:T3 → { RSCRTriggerKindId.EditionPinChange }`
* `G.11:T4 → { RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit }`
* `G.11:T5 → { RSCRTriggerKindId.FreshnessOrDecayEvent }`
* `G.11:T6 → { RSCRTriggerKindId.MaturityRungChange }`
* `G.11:T7 → { RSCRTriggerKindId.PolicyPinChange }`

**TriggerAliasMap.G0 (reserved; empty in Phase‑2).**
Map any stable deprecated registry-hook labels emitted/recorded by `G.0` to the canonical kinds above (typically `LegalitySurfaceEdit`, `PenaltyPolicyEdit`, `CrossingBundleEdit`, `ReferencePlaneEdit`, `TokenizationOrNameChange`), preserving the original label text as `RSCRTriggerAliasId`. If none exist, `G.0` SHOULD emit canonical `RSCRTriggerKindId` values directly.

**TriggerAliasMap.G6**
EvidenceGraph `H3` example causes → canonical kinds:

* `G.6:H3:freshness/decay change → { RSCRTriggerKindId.FreshnessOrDecayEvent }`
* `G.6:H3:Bridge CL/CL^k or loss update → { RSCRTriggerKindId.CrossingBundleEdit }`
* `G.6:H3:Φ/Ψ policy change → { RSCRTriggerKindId.PenaltyPolicyEdit }`
* `G.6:H3:lane tag correction → { RSCRTriggerKindId.EvidenceSurfaceEdit }`
* `G.6:H3:ReferencePlane correction → { RSCRTriggerKindId.ReferencePlaneEdit }`
* `G.6:H3:QD/OEE artefact updates (U.DescriptorMapRef.edition/DistanceDef, EmitterPolicyRef, InsertionPolicyRef, archive K-capacity) → { RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange }`

#### G.Core:4.4 - Default Governing Definition Index

`G.Core` provides an index of Part‑G defaults with **one governing definition** per `DefaultId`. The index is not a “second spec”; it is a cross-reference table that points to the *governing definition reference* (a CC item, policy‑id, or TaskSignature rule) and states applicability conditions.

##### G.Core:4.4.1 - Definitions

* **DefaultId**
  Stable identifier of a default (a default constant or default rule).

* **DefaultGoverningDefinitionRef**
  A reference to the governing definition of the default (e.g., a CC item id like `CC‑G5.23`, or a policy id, or a TaskSignature rule definition).

##### G.Core:4.4.2 - Rules

* Exactly one governing definition per `DefaultId`.
* Any other mention in `G.x` MUST be a citation/delegation to the governing definition, not a competing statement.
* A default may be conditional (default-rule) with explicit applicability conditions.
* The Default Governing Definition Index SHALL NOT be used to “smuggle” mandatory invariants as defaults. Invariants remain invariants (typically cited through `CC‑GCORE‑…` and their canonical governing definitions).

##### G.Core:4.4.3 - Seed Default Governing-definition assignment entries (Phase‑2 minimum)

| DefaultId                       | DefaultGoverningDefinitionRef                                           | Notes |
| ------------------------------ | --------------------------------------------------------- | ----- |
| `DefaultId.PortfolioMode`       | `CC‑G5.23`                                                | Existing governing definition; other mentions delegate to it. |
| `DefaultId.DominanceRegime`     | `CC‑G5.28`                                                | Existing governing definition; other mentions delegate to it. |
| `DefaultId.GammaFoldForR_eff`   | `CC‑G5.4`                                                 | Default Γ‑fold for `R_eff` is weakest‑link; overrides require explicit CAL support. |

This table may grow over time; the rule is that the **governing definition must already be named** (or be intentionally set to `G.Core` when the default is truly Part‑G‑wide and not governed elsewhere). Any change in a row (add/remove/change governing definition) SHALL be treated as a refresh‑sensitive edit and recorded as `RSCRTriggerKindId.DefaultGoverningDefinitionChange` (payload: affected `DefaultId.*`, old governing definition ref, new governing definition ref).

#### G.Core:4.5 - ID continuity protocol (Δ‑discipline)

When moving universal norms out of `G.x` into `G.Core`:

* existing public CC ids in `G.x` that may be referenced externally SHALL NOT be deleted or renamed;
* such CC items SHALL become **delegation** items that point to the relevant `CC‑GCORE‑…` item(s);
* each `G.x` SHALL add exactly one bridge CC item `CC‑Gx‑CoreRef` (first in its CC list) that makes linked `CC‑GCORE‑…` items mandatory for `G.x` conformance.

Deprecated trigger labels (e.g., `G.11:T*`, `G.6:H3:*`) are preserved as aliases and MUST map to canonical trigger kinds.

Non-CC public identifiers (e.g., `UTSRowId`, `RSCRTriggerAliasId`, deprecation notices, edition bumps) MUST obey the same Δ-discipline: preserve old ids; represent drift via alias/deprecation/edition evolution (see `F.17 (UTS)`); and emit canonical trigger kinds (`RSCRTriggerKindId.TokenizationOrNameChange`, `RSCRTriggerKindId.EditionPinChange`) when downstream impact is possible.

#### G.Core:4.6 - Explicit non-goals

`G.Core` does not:

* introduce CG‑frame kit entities (e.g., BridgeMatrix/ReferencePlane/Φ registries); those remain in their governing `G.x`;
* introduce method-family taxonomies, discipline packs, or generator orchestration mechanisms; those remain as `Extensions` in their governing definitions (e.g., synthesis/shipping/refresh patterns);
* define refresh algorithms; it defines trigger kinds and docking only.

---

### G.Core:5 - Archetypal grounding

**Tell.**
In Phase‑2 refactoring, `G.Core` is the hub that allows each `G.x` to become structurally predictable: (a) a short, normative “Core linkage” slice, and (b) pattern‑scoped `Extensions`. Universal obligations cite canonical governing definitions such as `A.6.7`, `A.15.3`, `A.19`, `G.0`, and `A.19.CHR`, while RSCR trigger kinds and `DefaultGoverningDefinitionRef` references become typed and cite named definitions.

**Show 1: Refresh triggers without semantic drift.**
`G.11` already uses trigger tokens `T0…T7`. `G.Core` keeps them as aliases and maps them to canonical trigger kinds (e.g., `TelemetryDelta`, `EditionPinChange`, `CrossingBundleEdit`). This makes RSCR reason codes consistent across patterns and avoids re-explaining trigger semantics in every pattern.

**Show 2: Resolving competing defaults.**
If multiple patterns imply a default for `PortfolioMode`, the Default Governing Definition Index points to one governing definition (currently `CC‑G5.23`). Other patterns (e.g., bundles/log patterns) must cite that governing definition or delegate to it, rather than restating the default with slightly different wording. This preserves intent while preventing drift and ambiguity.

### G.Core:6 - Bias-annotation (informative)

* **Centralization bias:** One governing hub can become too thick. Mitigation: delegation-first citation; keep only true Part‑G invariants and typed indices here.
* **Over-typing bias:** A trigger catalogue can become overly granular. Mitigation: granularity discipline + scope notes; only add new kinds when planning/selection needs it.
* **Refactor rigidity bias:** Preserving IDs can feel cumbersome. Mitigation: delegation items preserve IDs while enabling deduplication.
* **Default absolutism bias:** Defaults may require conditional rules. Mitigation: Default Governing Definition Index allows conditional default rules with explicit applicability conditions.
* **Single-writer bias:** prefers single‑writer *authoring* for catalogs and explicit governing-definition tables.
  *Mitigation:* delegation-first citation; keep catalogs minimal; avoid “second specs”.
* **Architectural bias:** centralizes invariants to prevent accidental coupling across `G.x`.
  *Mitigation:* keep core thin; force `Extensions` to remain pattern‑scoped.
* **Ontological/epistemic bias:** enforces strict distinction between governing spec refs, kits, mechanisms, and orchestration.
  *Mitigation:* allow didactic scope notes while keeping normative surface id‑based.
* **Pragmatic bias:** adds authoring overhead (linkage sections, alias maps).
  *Mitigation:* one small mandatory bridge CC item per pattern (`CC‑Gx‑CoreRef`) and short linkage slices only.
* **Didactic bias:** risks “glossy hub prose” that hides missing CC coverage.
  *Mitigation:* enforce CC/Solution coherence (E.19) and keep invariants checkable via `CC‑GCORE‑…`.

### G.Core:7 - Conformance checklist (normative) — **CC‑GCORE**

Conformance items are authoring obligations and are enforced transitively by `CC‑Gx‑CoreRef` in every `G.x`.

| ConformanceId        | Statement |
| -------------------- | --------- |
| **CC‑GCORE‑DEL‑1**   | A conforming `G.Core` SHALL be delegation-first: if a norm is already governed by `A.6.7`, `A.15.3`, `A.19`, `G.0`, `A.19.CHR`, or a relevant Part E pattern, `G.Core` cites that governing definition rather than duplicating semantics. |
| **CC‑GCORE‑CN‑CG‑1** | Any pattern in Part G that builds on `G.Core` SHALL cite `CN‑Spec` and `CG‑Spec` as the only spec-legality surfaces and SHALL NOT introduce shadow specs (incl. complying with `SuiteObligations.transport_declarative_only` and `SuiteObligations.cg_spec_cite_required_for_numeric_ops`). |
| **CC‑GCORE‑OBL‑1**   | A conforming `G.Core` SHALL treat the obligation vocabulary in `A.6.7:4.2` as the canonical naming surface for Part‑G‑wide obligations and SHALL NOT introduce competing obligation names for the same norms. |
| **CC‑GCORE‑CROSS‑1** | A Part‑G pattern that introduces or consumes crossings SHALL enforce `SuiteObligations.bridge_only_crossings` and `SuiteObligations.crossing_visibility_required` (CrossingBundle per E.18); SHALL prohibit implicit crossings; SHALL treat `edition_key` changes on **crossing‑relevant artefacts** (Bridge/CL/CrossingBundle registries and UTS rows for crossing artefacts) as `RSCRTriggerKindId.CrossingBundleEdit` (and, when an edition pin is involved, also `RSCRTriggerKindId.EditionPinChange` per multi‑cause discipline); and SHALL cite `SuiteObligations.two_bridge_rule_for_described_entity_change` through its canonical governing definition. |
| **CC‑GCORE‑GUARD‑1** | A Part‑G pattern SHALL treat `GuardDecision := {pass|degrade|abstain}` as the only admissibility/eligibility decision domain (`SuiteObligations.guard_decision_tristate(pass|degrade|abstain)`); `unknown` SHALL NOT silently coerce to `pass` (`SuiteObligations.unknown_never_coerces_to_pass`); “sandbox/probe‑only” SHALL be expressed via SoS‑LOG branch pins (policy/FailureBehavior) (see `C.23`), not as an extra decision value. |
| **CC‑GCORE‑PEN‑1**   | A Part‑G pattern SHALL route penalties/assurance loss to the **R lane (`R_eff`) only** (`SuiteObligations.penalties_route_to_r_eff_only`) and SHALL preserve **F/G invariants** under penalties (penalties do not alter legality/invariant lanes). |
| **CC‑GCORE‑SET‑1**   | A Part‑G pattern SHALL preserve set-return semantics for partial orders and SHALL prohibit silent scalarization/totalization (`SuiteObligations.no_silent_scalarisation_of_partial_orders`, `SuiteObligations.no_silent_totalisation`); any scalar summary SHALL be report-only unless declared as a admissible comparator surface. |
| **CC‑GCORE‑SKP‑1**   | A Part‑G pattern SHALL preserve the suite/kit/pack distinction (A.19.CHR) and SHALL keep shipping concerns governed by their canonical governing patterns (e.g., G.10) rather than embedding shipping semantics into unrelated kits or core invariants. |
| **CC‑GCORE‑P2W‑1**   | A Part‑G pattern that uses planned baselines SHALL anchor them via `SlotFillingsPlanItem` in WorkPlanning (`SuiteObligations.planned_slot_filling_in_work_planning_only`) and SHALL finalize launch values only in WorkEnactment (`SuiteObligations.finalize_launch_values_in_work_enactment_only`); gate decisions remain separated per `SuiteObligations.gate_decision_separation`. |
| **CC‑GCORE‑LINK‑1**  | Every conforming `G.x` SHALL satisfy `G.Core:4.2` by providing a `G.x:<n> - G.Core linkage (normative)` section containing a `GCoreLinkageManifest` (incl. either `CoreConformanceProfileIds` or `CoreConformanceIds`, either `RSCRTriggerSetIds` or `RSCRTriggerKindIds`, and either `CorePinSetIds` or `CorePinsRequired` (or both)). Nil‑elision is permitted for `∅` fields. |
| **CC‑GCORE‑LINK‑2**  | Every conforming `G.x` SHALL include `CC‑Gx‑CoreRef` as the first checklist item; it SHALL make mandatory the effective `CoreConformanceIds` (including expansions of any `CoreConformanceProfileIds`) declared in the linkage manifest. |
| **CC‑GCORE‑UTS‑1**   | If a Part‑G pattern mints, deprecates, or evolves any public identifier, it SHALL publish/update the corresponding UTS entries and cite them via `UTSRowId` pins, delegating UTS semantics (twin labels, alias/deprecation discipline, edition pins) to its canonical governing definition `F.17 (UTS)`. |
| **CC‑GCORE‑ID‑1**    | When deduplicating, existing public CC ids in `G.x` SHALL NOT be deleted/renamed; they SHALL become delegation items to relevant `CC‑GCORE‑…` items. |
| **CC‑GCORE‑ID‑2**    | Public id continuity applies beyond CC item ids: `UTSRowId` rows, `RSCRTriggerAliasId` tokens (e.g., `T0…T7`), deprecation notices, and edition bumps SHALL preserve prior ids and express drift via alias/deprecation/edition evolution (never by reusing/redefining an old id). When downstream behaviour can change, the change SHALL emit a canonical `RSCRTriggerKindId` (e.g., `TokenizationOrNameChange`, `EditionPinChange`). |
| **CC‑GCORE‑TRIG‑1**  | A conforming `G.Core` SHALL define the canonical `RSCRTriggerKindId` catalogue and SHALL be its single writer. |
| **CC‑GCORE‑TRIG‑2**  | Any `G.x` that uses local trigger tokens SHALL provide (or cite) a `TriggerAliasMap` mapping each alias to canonical `RSCRTriggerKindId`. |
| **CC‑GCORE‑TRIG‑3**  | Any artefact that records RSCR/SCR/refresh reasons SHALL record canonical `RSCRTriggerKindId` (aliases may be recorded as labels only). |
| **CC‑GCORE‑TRIG‑4**  | A conforming `G.Core` SHALL keep `TriggerAliasMap.*` consistent with the governing patterns’ deprecated trigger alias catalogues (e.g., `G.11:T*`). Any change to an alias mapping SHALL be treated as refresh‑sensitive; at minimum it SHALL be recorded/emitted as `RSCRTriggerKindId.TokenizationOrNameChange` (and, if the mapped trigger kinds change, the corresponding canonical kinds apply as well). |
| **CC‑GCORE‑DEF‑1**  | A conforming `G.Core` SHALL maintain a Default Governing Definition Index for Part‑G defaults, ensuring each `DefaultId.*` names exactly one governing definition (a CC item or a policy id). All other patterns SHALL cite the governing definition and SHALL NOT state competing defaults. Any governing-definition change MUST be recorded as `RSCRTriggerKindId.DefaultGoverningDefinitionChange`. |

### G.Core:8 - Common anti-patterns and how to avoid them

* **Anti-pattern:** Restating CN‑Spec/CG‑Spec rules inside a `G.x` “for convenience”.
  **Avoid:** cite `A.19` and `G.0` through `CC‑GCORE‑CN‑CG‑1`.

* **Anti-pattern:** Adding a fourth guard status (“unknown”, “maybe”, “probe-only”) as a separate decision value.
  **Avoid:** keep guard domain tri‑state; express “probe-only” as policy/branching and record via pins/audit.

* **Anti-pattern:** Treating mandatory invariants as “defaults” to centralize them.
  **Avoid:** keep invariants as invariants (CC‑GCORE‑* cited through canonical governing definitions); restrict the Default Governing Definition Index to true defaults (constants or conditional default-rules).

* **Anti-pattern:** Turning partial orders into scalar ranks silently.
  **Avoid:** keep set‑valued semantics unless a total order is explicitly declared by a comparator/policy.

* **Anti-pattern:** Competing defaults scattered across multiple patterns.
  **Avoid:** Default Governing Definition Index; delegate duplicate statements to the one governing definition.

* **Anti-pattern:** Local trigger tokens without canonical mapping.
  **Avoid:** provide/cite a `TriggerAliasMap` with namespace‑qualified aliases.

* **Anti-pattern:** Breaking public CC ids during dedup.
  **Avoid:** convert to delegation items; preserve IDs.


### G.Core:9 - Consequences

* **Positive:** Part‑G‑wide invariants cite `G.Core` as their governing definition; refactors become safer and easier to audit.
* **Positive:** RSCR becomes reason-code driven (typed triggers), improving traceability and preventing semantic drift.
* **Positive:** Default conflicts become detectable and resolvable because each `DefaultId` names one governing definition.
* **Negative:** Adds an extra authoring step (linkage sections and CoreRef CC item) to each `G.x`.
* **Negative:** Requires careful governance of the trigger catalogue to avoid excessive fragmentation.

### G.Core:10 - Rationale

Universalization of Part G requires a stable "gravity center" for invariants, otherwise each pattern becomes a competing governing source. Delegation-first citation prevents duplication and makes governing-definition assignment explicit, while typed trigger kinds and the Default Governing Definition Index turn historically prose-driven drift into checkable, id-based structure.

### G.Core:11 - SoTA alignment (informative)

Although FPF is conceptual (not a data governance framework), `G.Core` aligns Part‑G authoring with modern best practice patterns seen across post‑2015 work:

* **Selective prediction / abstention** informs tri‑state guard discipline: abstaining or degrading is a first-class outcome, not an error coerced into a scalar.
* **Set-valued / conformal methods** motivate set-return semantics: when comparability is partial or uncertainty is structural, returning sets/regions is often the SoTA-friendly representation.
* **Multiobjective optimization and quality-diversity** reinforce declared set-surface and `Archive` semantics instead of forced “best single scalar”.
* **Monotone constrained modelling** (where used) supports “legality-first” scoring/aggregation: constraints and admissibility precede optimization, mirroring CG‑Spec gate discipline.
* **Schema evolution and contract testing** motivate id-stable conformance points and typed trigger catalogues: stable identifiers + regression hooks are the practical mechanism for safe refactoring.

### G.Core:12 - Relations

* **Builds on:**

  * `E.8` pattern template and section discipline
  * `E.10` lexical/ontological rules (strict distinction; twin naming; kind‑suffix discipline)
* `E.18` CrossingBundle (crossing visibility bundle)
  * `E.19` conformance discipline
  * `A.6.7` SuiteObligations + suite protocol pins (delegation support)
  * `A.15.3` SlotFillingsPlanItem (planned baseline anchor)
  * `A.19` CN‑Spec governance card
  * `G.0` CG‑Spec legality gate
  * `A.19.CHR` CHR suite boundary and "governance cards and legality gates are cited as pins, not copied locally" discipline
  * `C.23` SoS‑LOG (tri‑state branches; sandbox/probe‑only)
  * `F.17` UTS (identifier registry; alias/deprecation discipline)
  * `F.15` RSCR (regression/conformance loop)

* **Used by:**

  * `G.0…G.13` patterns (each adds `Builds on: G.Core`, linkage section, CoreRef CC item)

* **Constrains:**

  * Part‑G authoring: no shadow specs, no silent scalarization, tri‑state guards, penalties routing, typed RSCR causes, defaults with one governing definition, and ID‑continuity refactors.

### G.Core:End

## G.0 - Frame Standard and Comparability Governance — CG‑Spec

**Tag.** Architectural pattern (foundational Standard; constrains G.1–G.5)
**Stage.** *design-time* legality gate (establishes comparison legality & evidence minima; constrains run-time gates)
**Primary output.** `CG‑Spec` — a notation-independent legality gate for a `CG‑Frame`, published to UTS (with explicit edition pins for downstream reproducibility and RSCR).
**Primary hooks.** `USM.ScopeSlice(G)`, `describedEntity`, `SCP`, `MinimalEvidence`, `CNSpecRef`, `Γ‑fold`, `Φ(CL)` / `Φ_plane` policy pins, `UTS` publication (Name Cards + edition pins).
**Non-duplication note.** Universal Part‑G invariants are governed by `G.Core` and are satisfied here **only via delegation** (`CC‑G0‑CoreRef` → `CC‑GCORE‑*`). Single‑governing definition CN/CG spec-ref discipline is enforced via `CC‑GCORE‑CN‑CG‑1` (no shadow specs; no competing defaults).

### G.0:1 - Problem frame

A team defines or evolves a `CG‑Frame` (e.g., a frame for creativity measurement, decision quality, architecture trade‑offs, or selected-set publication). Downstream mechanisms (G.1–G.5 and beyond) must compare, aggregate, and publish CHR‑typed observations in ways that are:

* lawful with respect to measurement legality (scale/unit/polarity constraints),
* auditable with explicit evidence minima and provenance,
* reproducible via pinned editions and explicit policy ids,
* portable only via explicit crossings (bridges and reference-plane moves), never via implicit semantic leakage.

`CG‑Spec` is the single design-time object that fixes *what comparisons and aggregations are lawful in this frame*, under which pinned assumptions and minimal evidence requirements, so that run-time selection and publication can be audited without inventing new “local legality gates”.

Didactic subtitle: **Design-time rules for safe, auditable comparison.**

### G.0:2 - Problem

Without a single, frame-level legality standard:

* comparisons and aggregations drift into *implicit assumptions* (hidden scalarisation; silent totalisation of partial orders),
* numeric gates run on “whatever is available” rather than declared evidence minima and lane/carrier requirements,
* cross-context reuse happens without explicit crossing visibility and stated losses,
* selection outcomes become hard to audit because legality, evidence minima, and penalty routing are not pinned and traceable.

### G.0:3 - Forces

* **Pluralism vs. comparability.** Multiple traditions must co-exist while allowing admissible comparison where justified.
* **Expressiveness vs. safety.** Rich comparator sets and aggregators vs. measurement legality constraints.
* **Locality vs. portability.** Context-local semantics first; portability only via explicit bridges and explicit losses.
* **Assurance vs. agility.** Evidence minima must meet the claim threshold while staying light enough to adopt.
* **Design-time vs. run-time.** Keep legality standards and templates design-time; run-time only cites and applies them.

### G.0:4 - Solution — CG‑Spec as the design-time legality gate

`CG‑Spec` is a **notation-independent** UTS-published object that, for a given `CG‑Frame`, defines:

* the **ComparatorSet** (explicit, finite, typed) permitted in this frame,
* the **ScaleComplianceProfile** (SCP) that constrains lawful operations per characteristic,
* **MinimalEvidence** requirements per characteristic (lanes, carriers, freshness windows, crossing allowances, failure behavior),
* the frame’s **penalty and trust folding wiring** (by explicit policy ids and edition pins),
* **AcceptanceStubs** as design-time templates (thresholds remain governed by CAL, not by CG‑Spec),
* optional method-family hooks (e.g., illumination/QD or explore↔exploit guards) *as wiring only*, with semantics governed by the corresponding patterns.

`CG‑Spec` constrains downstream gate checks by being *referenced and pinned*; it is not itself an admissibility mechanism.

#### G.0:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part-G core invariants; governing-pattern citation)

**GCoreLinkageManifest (normative; size-controlled via profiles/sets).**

Effective obligations/pins/triggers are computed by union expansion of the referenced ids (per `G.Core:4.2`).
Profiles/sets + explicit deltas; `Nil‑elision` applies.

* `CoreConformanceProfileIds :=`
  * `GCoreConformanceProfileId.PartG.AuthoringBase`
  * `GCoreConformanceProfileId.PartG.TriStateGuard`
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
* `CorePinSetIds :=`
  * `GCorePinSetId.PartG.AuthoringMinimal`
  * `GCorePinSetId.PartG.CrossingVisibilityPins`
* `CorePinsRequired :=` *(delta over PinSets)*
  * `UTSRowId[]`
  * `ReferenceMap`
  * `ComparatorSetRef.edition`
  * `SCPRef.edition`
  * `ΓFoldRef.edition?`
  * `MinimalEvidenceRef.edition?`
  * `FailureBehaviorPolicyId?`
* `DefaultsConsumed := {DefaultId.GammaFoldForR_eff}` *(governing definition: `CC‑G5.4` per `G.Core.DefaultGoverningDefinitionIndex`)*
* `RSCRTriggerSetIds := {GCoreTriggerSetId.CGSpecGate}`
* `RSCRTriggerKindIds :=` *(delta over TriggerSets)*
  * `RSCRTriggerKindId.EvidenceSurfaceEdit`
  * `RSCRTriggerKindId.TokenizationOrNameChange`
  * `RSCRTriggerKindId.DefaultGoverningDefinitionChange`
* `TriggerAliasMapRef := ∅`

#### G.0:4.2 - CG‑Spec object model (normative)

`CG‑Spec` is authored per `CG‑Frame`. It SHALL:

* be **published to UTS** as a notation-independent object,
* reference CHR characteristics by id (measurement semantics remain governed by CHR packs),
* constrain what comparisons and aggregations are lawful in this frame via explicit comparator specs and SCP bindings,
* declare minimal evidence gates per characteristic, including explicit failure behavior wiring,
* cite `CN‑Spec` for normalization/comparability policies (no duplication and no shadow specs),
* publish edition pins and policy ids so downstream selection, parity, shipping, and refresh can be reproducible and RSCR-aware.

#### G.0:4.3 - CG‑Spec conceptual model (normative)

```
CG‑Spec :=
⟨
  UTS.id, Edition,
  Context, Purpose, Audience,

  Scope := USM.ScopeSlice(G) ⊕ Boundary{TaskKinds, ObjectKinds},

  describedEntity := ⟨GroundingHolon, ReferencePlane ∈ {world|concept|episteme}⟩,
  WorldRegime? ∈ {prep|live},          // only refines ReferencePlane=world; introduces no new planes

  ReferenceMap := minimal map{term/id → UTS|CHR|SoTA-pack refs},

  CNSpecRef := ⟨A.19 ref, CNSpecRef.edition⟩,          // CN‑Spec is the governance card (one governing definition)

  Characteristics := [CHR.Characteristic.id…],          // pointers only; authored in G.3 CHR pack

  // Edition-addressable segments (pins MUST be exposed)
  ComparatorSet := ⟨ComparatorSetId, ComparatorSetRef.edition, [ComparatorSpec…]⟩,
  SCP := ⟨SCPId, SCPRef.edition, map Characteristic.id → SCPEntry⟩,
  MinimalEvidence := ⟨MinEvId, MinimalEvidenceRef.edition?, map Characteristic.id → MinEvidenceEntry⟩,  // min pin: CGSpecRef.edition

  Γ‑fold := ⟨GammaFoldId, ΓFoldRef.edition,
             defaultRef := DefaultId.GammaFoldForR_eff,
             override? := ⟨overrideRef, proof_refs, boundary_notes⟩
           ⟩,

  // Penalty routing and plane policies are by explicit policy ids.
  // Semantics (tri-state, penalties→R_eff-only, crossing visibility, set-return) are governed by G.Core.
  CL‑Routing := ⟨policy_id, map Bridge.CL → penalty_spec⟩,
  Φ := ⟨phi_policy_id, phi_table_ref?, psi_policy_id?, phi_plane_policy_id?⟩,

  AcceptanceStubs := [AcceptanceStubId…],     // templates only; thresholds remain governed by CAL (G.4)

  // Optional hooks are wiring-only; semantics are governed by governing definitions.
  E/E‑LOG Guard? := ⟨policy_id, pins…⟩,
  Illumination? := ⟨
    Q_refs ⊆ Characteristics, D_refs ⊆ Characteristics,
    DescriptorMapRef.edition?, DistanceDefRef.edition?, DHCMethodRef.edition?,
    InsertionPolicyRef?, PromotionPolicyId?
  ⟩,

  RSCR := ⟨
  RSCRTestId[]?,             // SHOULD cover: illegal_op_refusals; unit and scale legality checks; freshness windows; // partial-order scalarisation refusals; threshold semantics; CL→R_eff routing;
                            // and refusal of degrade.order on unit mismatches (MM‑CHR).
    RSCRTriggerKindId[]
  ⟩,

  Naming := UTS Name Cards (twin labels plus bridge notes),
  PublicIdContinuity := ⟨governing definition, DRR link, refresh cadence, decay and aging policy, deprecations⟩,
  Provenance := ⟨carrier types, SoTA-pack refs, DRR/SCR linkage⟩
⟩
```

**Local typing notes (non-exhaustive; normative intent but no shadow specs).**

* `ComparatorSpec` MUST be typed against SCP/CHR constraints. Examples of lawful comparators are frame-local choices and are authored here (e.g., dominance where lawful; lexicographic over typed traits; medoid/median for ordinal where lawful; explicit weighted sums only where legality is proven and units are aligned).
* `MinimalEvidenceEntry` MUST declare: lane requirements, evidence carriers, freshness window (if any), and explicit failure behavior wiring. The semantics of `{pass|degrade|abstain}` and `degrade(mode=…)` are delegated to `G.Core`.

#### G.0:4.4 - Interfaces (normative)

| Interface          | Consumes                             | Produces / constrains                                                      |
| ------------------ | ------------------------------------ | -------------------------------------------------------------------------- |
| **G.0‑1 Charter**  | CG‑Frame brief, USM scope signals    | `CG‑Spec.Scope`, `describedEntity`, `ReferenceMap`                         |
| **G.0‑2 SCP**      | CHR pack refs (G.3), legality proofs | `CG‑Spec.SCP` + bindings to lawful operators/aggregators                   |
| **G.0‑3 Evidence** | SoTA inputs (G.2), carriers (A.10)   | `CG‑Spec.MinimalEvidence`, `Γ‑fold` segment pins, `CL‑Routing`, `Φ` ids    |
| **G.0‑4 Publish**  | All above                            | Versioned `CG‑Spec@UTS` plus Name Cards, public-id continuity records, and RSCR tests and trigger kinds  |
| **G.0‑5 Expose_CrossingHooks** | `CG‑Spec` + crossing/plane/policy pins | GateCrossing inputs for `GateChecks` (`E.18/A.21`): plane checks, lane purity, lexical SD pins |
| **→ G.1**          | `CG‑Spec`                            | Generator guardrails (Comparator/SCP/MinEv pins); degrade/abstain wiring   |
| **→ G.2**          | `CG‑Spec`                            | Harvesting inclusion/exclusion and crossing policy constraints             |
| **→ G.3**          | `CG‑Spec`                            | Required CHR characteristics/scales/operators to exist                     |
| **→ G.4**          | `CG‑Spec`                            | Acceptance templates; evidence minima; Γ‑fold override proof hooks         |
| **→ G.5**          | `CG‑Spec`                            | Eligibility gates and explainability pins (Path/UTS/policy ids)            |
| **→ G.6**          | `CG‑Spec`                            | EvidenceGraph/SCR pinning surface (policy ids + Path/PathSlice discipline) |

#### G.0:4.5 - CG‑Spec authoring chassis (informative)

1. **Charter the frame.** Declare `Context`, `Scope`, `describedEntity`, boundary examples/non-examples, and `ReferenceMap`.
2. **Draft ComparatorSet and SCP.** Enumerate permitted comparator forms and bind each to CHR characteristics and legality constraints (scale/unit/polarity discipline). Attach guard bindings as explicit references/pins.
3. **Bind Characteristics.** Ensure every compared quantity is a CHR characteristic id (reuse/mint via UTS discipline).
4. **Declare MinimalEvidence.** For each characteristic: required lanes/carriers, freshness window, crossing allowances (if any), and explicit failure behavior wiring (tri-state semantics delegated to `G.Core`).
5. **Pin trust folding and penalties.** Cite the one governing definition for `DefaultId.GammaFoldForR_eff` unless explicitly overridden with proof refs; publish `Φ`/CL policy ids explicitly.
6. **Publish and register regression tests.** Publish `CG‑Spec@UTS` with edition-pinned segments; register RSCR tests for the frame’s legality surfaces and evidence minima.
7. **Public-id continuity and refresh readiness.** Declare refresh cadence and deprecations with lexical continuity notes; ensure RSCR trigger kinds are emitted as canonical ids.

#### G.0:4.6 - Extensions (pattern-scoped; non-core)

All blocks below are `GPatternExtension` modules (PatternScopeId; not new PatternIds). They store wiring only and cite governing patterns.

**GPatternExtension: SpecRefSurfaces**

* **PatternScopeId:** `G.0:Ext.SpecRefSurfaces`
* **GPatternExtensionId:** `SpecRefSurfaces`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `A.19`
* **Uses:** `{A.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CNSpecRef.edition` (and any CN-side policy ids referenced by `CG‑Spec` fields)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.LegalitySurfaceEdit}`
* **Notes (wiring-only):** `CG‑Spec` SHALL cite CN‑Spec; it SHALL NOT restate normalization/comparability semantics.

**GPatternExtension: BridgeAndCLWiring**

* **PatternScopeId:** `G.0:Ext.BridgeAndCLWiring`
* **GPatternExtensionId:** `BridgeAndCLWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `F.9`
* **Uses:** `{F.9, G.7}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `BridgeCardId/BridgeId` (when crossings are permitted)
  * `CL` / `CL^k` and `Φ`/`Φ_plane` policy ids (when penalties are in play)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (wiring-only):** Crossing semantics and penalty routing are delegated to `G.Core`; this module only lists the required pins used by `CG‑Spec` entries.

**GPatternExtension: SoTAPaletteInputs**

* **PatternScopeId:** `G.0:Ext.SoTAPaletteInputs`
* **GPatternExtensionId:** `SoTAPaletteInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `SoTA-Pack@CG‑Frame` refs used to justify comparator admissibility, evidence minima, and crossing allowances (e.g., claim sheets, operator inventory, bridge matrix ids)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** Any SoTA palette/tradition semantics are governed by `G.2`. `G.0` only requires that `CG‑Spec` entries cite the needed SoTA artefacts for auditability.

**GPatternExtension: QDAndExplorationHooks**

* **PatternScopeId:** `G.0:Ext.QDAndExplorationHooks`
* **GPatternExtensionId:** `QDAndExplorationHooks`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19, C.23}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `InsertionPolicyRef?`
  * `FailureBehaviorPolicyId` / SoS‑LOG branch policy id when `degrade(mode=…)` is used
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** `CG‑Spec` may declare optional QD/exploration hooks; semantics remain governed by the referenced method patterns.

### G.0:5 - Archetypal Grounding — Tell–Show–Show; System / Episteme

#### G.0:5.1 - Archetype 1: System comparability under mixed evidence and unit constraints

**Tell.** Two labs compare energy efficiency results of a physical system where measurements use different rigs and units, and some evidence is missing.

**Show (failure without CG‑Spec).** The team averages an ordinal safety rating, mixes units (“kWh” vs “MJ”), and silently treats missing lanes as zeros. Cross-lab reuse happens without explicit bridge and loss notes, so selection becomes a black box.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* pins the lawful comparator(s) (e.g., unit-aligned ratio comparisons only; ordinal comparisons are order-only),
* declares `MinimalEvidence` lanes/carriers and freshness windows per characteristic,
* declares explicit failure behavior wiring (tri-state semantics delegated to `G.Core`),
* exposes crossing pins (bridge ids + CL/policy ids) when reuse across rigs is attempted,
* publishes the pinned editions so parity/refresh can detect drift.

#### G.0:5.2 - Archetype 2: Epistemic comparability for selected-set publication across traditions

**Tell.** A team selects an R&D set using multiple evaluation traditions: safety assurance, cost models, and readiness heuristics.

**Show (failure without CG‑Spec).** The team collapses partial orders into a single score, hides the threshold policy in code, and cannot explain why cross-tradition penalties changed between runs.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* defines a comparator bundle (e.g., Pareto dominance + explicit lexicographic tiebreaks where lawful),
* pins `CNSpecRef.edition` and the editioned segments (`ComparatorSetRef.edition`, `SCPRef.edition`, `MinimalEvidenceRef.edition`),
* makes `AcceptanceStubs` explicit as templates while locating thresholds in CAL (G.4),
* ensures RSCR triggers are emitted when comparator or policy pins change.

### G.0:6 - Bias-Annotation

`CG‑Spec` can encode (and therefore amplify) biases if authored carelessly:

* **Tradition favoritism.** Comparator choices may privilege a tradition’s evidence style; mitigation: require explicit evidence minima and explicit crossing costs, and keep cross-tradition aggregation gated by explicit justifications.
* **Metric gaming and Goodhart effects.** Overemphasis on a single scalar can lead to gaming; mitigation: preserve set-return semantics and require explicit, auditable scalarisations when they are lawful and intended.
* **Hidden thresholds and opaque safety policy.** Embedding acceptance thresholds in prose or code hides value judgments; mitigation: keep thresholds in CAL acceptance clauses and pin policy ids.
* **Scope creep.** Comparisons leak across describedEntity or reference planes; mitigation: require explicit `describedEntity` and `ReferencePlane` pins and treat plane moves as explicit crossing events.

### G.0:7 - Conformance Checklist (normative)

| ConformanceId | Statement |
| --- | --- |
| **CC‑G0‑CoreRef** | `G.0` is conformant only if the applicable core obligations listed in `G.0:4.1` are satisfied (delegation to `CC‑GCORE‑*`; no shadow specs, no competing defaults, typed RSCR triggers, explicit pins). |
| CC‑G0‑01 | `CG‑Spec` is published as a notation-independent UTS object with explicit `Edition`, `Context`, `Scope`, `describedEntity`, and a minimum `ReferenceMap`. |
| CC‑G0‑02 | `CNSpecRef.edition` is present and is treated as an external governance-card reference (no local redefinition of CN semantics). *(Delegation target: `CC‑GCORE‑CN‑CG‑1`.)* |
| CC‑G0‑03 | `ComparatorSet` is explicit and finite; each comparator is typed and bound to `SCP` and referenced CHR characteristics; **anything not enumerated MUST be treated as illegal/abstain by default** (no implicit comparator defaults). |
| CC‑G0‑04 | `SCP` declares, per characteristic, the lawful operation regime needed for each referenced comparator (scale/unit/polarity constraints and any required proofs/refs). |
| CC‑G0‑05 | `MinimalEvidence` is declared per characteristic and includes explicit lane/carrier requirements, freshness window references (if any), and explicit failure behavior wiring (tri-state semantics delegated). If freshness windows are used, a stable window id (e.g., `PathSliceId`) MUST be pinned for audit. |
| CC‑G0‑06 | `Γ‑fold` is present as an edition-pinned segment and either (i) cites `DefaultId.GammaFoldForR_eff` (one governing definition) or (ii) provides an explicit override with proof refs. |
| CC‑G0‑07 | If crossing penalties are used, `CL‑Routing` and `Φ` policy ids are explicit and auditable (policy ids are exposed as pins/refs) **and are required pins for downstream SCR publication on penalised claims** (see `G.6`). |
| CC‑G0‑08 | `AcceptanceStubs` in `CG‑Spec` are templates only; any context-local thresholds/acceptance policies are governed by CAL acceptance artefacts (G.4) and are cited, not duplicated. |
| CC‑G0‑09 | RSCR tests and triggers for edits to legality surfaces and evidence minima are present and use canonical `RSCRTriggerKindId`s. The RSCR test set SHOULD cover at least: illegal_op_refusals; unit and scale legality checks; freshness windows; partial-order scalarisation refusals; threshold semantics; CL→`R_eff` routing; refusal of `degrade.order` on unit mismatches (MM‑CHR). |
| CC‑G0‑10 | `PublicIdContinuity` is declared: governing definition, DRR link, refresh cadence, decay and aging policy, and deprecations. Deprecations preserve lexical continuity (Δ-discipline; delegated to `CC‑GCORE‑ID‑*`). |
| CC‑G0‑11 | *(Conditional)* If `Illumination` / QD hooks are present, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and any `InsertionPolicyRef` / promotion policy ids are pinned (or explicitly marked absent) and are recorded in provenance/audit pins. |
| CC‑G0‑12 | *(Conditional)* If freshness windows influence gating/selection, they are published and enforced, and the relevant window ids (`PathSliceId` or equivalent) are recorded in SCR/audit pins. |
| CC‑G0‑13 | **Pre-flight numeric gates.** Any numeric comparison/aggregation declared in `ComparatorSet` has associated `GateChecks` for unit legality, scale legality, pinned SOP/editions, and declared comparability assumptions; failing any check yields `refuse` or `abstain` (tri-state semantics delegated). |
| CC‑G0‑14 | **GateCrossing hook exposure.** Exports provide `Expose_CrossingHooks` inputs so `GateChecks` (`E.18/A.21`) can validate plane consistency, crossing intent, lane purity, and lexical SD; failures MUST block publication. |
| **CC‑G0‑Φ** | `Φ(CL)` (and `Φ_plane`, if used) is monotone, bounded, and table-backed; policy ids are published; construction preserves `R_eff ≥ 0`. |
| **CC‑G0‑Unknowns** | *Delegated.* Unknown handling MUST follow the tri-state guard semantics `{pass|degrade|abstain}` with no silent coercions. (See `CC‑GCORE‑GUARD‑1`.) |
| **CC‑G0‑CSLC** | Scale/unit/polarity legality MUST be proven before any aggregation; illegal arithmetic on ordinal/nominal values is nonconformant. (Governed by the relevant legality patterns; `G.0` only binds and cites.) |
### G.0:8 - Common Anti-Patterns and How to Avoid Them

* **Anti-pattern: shadow legality gates in downstream code.** Avoid by requiring downstream to cite `CG‑Spec` segments by id+edition.
* **Anti-pattern: “one number to rule them all”.** Avoid by preserving set-return outputs when only partial orders are lawful; any scalarisation must be explicit, typed, and justified.
* **Anti-pattern: thresholds inside CG‑Spec or CHR.** Avoid by keeping thresholds and acceptance logic in CAL and citing from `CG‑Spec` only via stubs/templates.
* **Anti-pattern: implicit crossings.** Avoid by requiring explicit bridge ids, CL/policy ids, and reference-plane pins.

### G.0:9 - Consequences

* **Lawful comparability.** The frame declares exactly what can be compared/aggregated and under what constraints.
* **Auditable selection.** Downstream selectors can justify outcomes via pinned legality surfaces and explicit evidence minima.
* **Explicit portability costs.** Cross-context reuse becomes deliberate and costed via visible crossings and penalties.
* **Lower drift under evolution.** Edition pinning + typed RSCR triggers makes comparability drift detectable and refreshable.

### G.0:10 - Rationale

`CG‑Spec` centralises frame-level comparability constraints so that:

* CHR authorship (G.3) remains about *measurement meaning* rather than implicit thresholds,
* CAL (G.4) governs context-local acceptance/threshold policies and proof ledgers,
* selectors and dispatchers (G.5) remain policy-governed and auditable rather than encoding hidden legality assumptions,
* refresh (G.11) can treat legality edits and pin changes as explicit causes with canonical trigger ids.

### G.0:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice in evaluation and governance by:

* treating “abstain / defer” as a first-class outcome rather than forcing a single brittle scalar (cf. selective prediction / abstention and set-valued reporting practices),
* preserving multiobjective / partial-order outputs as sets (Pareto / archive thinking) rather than silently collapsing to a scalar,
* emphasising reproducibility via explicit versioning/pinning of evaluation surfaces (editions) and explicit policy identifiers,
* making evidence minima explicit and auditable (a conceptual analogue of modern reproducibility/robustness checklists and evaluation protocols),
* keeping method-family specifics modular (e.g., QD/archives, open-ended exploration budgets) via explicit wiring to governing patterns rather than embedding method semantics into the universal legality gate.

### G.0:12 - Relations

**Builds on:** `G.Core`, `A.19 (CN‑Spec)`, `A.10 (evidence carriers)`, `A.17–A.19 / C.16 (MM‑CHR legality)`, `A.18 (CSLC)`, `B.3 (trust / Γ‑fold family)`, `F.* (contexts, bridges, CL, UTS)`, `E.10 (lexical rules)`, `E.5.* (notation independence discipline)`.
**Used by:** `G.1` (generator guards), `G.2` (harvesting constraints), `G.3` (required CHR), `G.4` (acceptance templates / proof hooks), `G.5` (eligibility gates), `G.6` (evidence/pin surfaces), and downstream parity/shipping/refresh where `CG‑Spec` is pinned.
**Publishes to:** `UTS` (Name Cards + editioned `CG‑Spec` segments).

### G.0:End

## G.1 - CG‑Frame‑Ready Generator

**Tag.** architectural pattern; *generator chassis* (design‑time kit / authoring scaffold)
**Status.** stable (Phase‑2 universalisation)
**Normativity.** normative, except sections explicitly marked *informative*
**Stage.** *design‑time* authoring of a generator‑kit with a *run‑time* execution façade (policy‑governed; edition‑aware)
**Primary output.** the **six‑card chassis** `M1…M6` published as a **complete, reusable CG‑Frame kit**, plus a versioned **kit manifest** `CGKitId` that binds the six cards as a single reusable unit (view‑friendly inventory + wiring surface)
**Primary hooks.** see **§12 Relations** (notably `G.Core`, `G.0`, `G.2`, `G.5`, `G.10`, `G.11`)
**Working‑model first (informative).** prefer working models and didactic micro‑examples; escalate to formal harnesses only when risk warrants (per E.8).
**Non‑duplication note.** Universal Part‑G invariants (tri‑state guard, set-return, penalties→`R_eff`‑only, crossing visibility, typed RSCR triggers, Default Governing Definition Index, P2W split, linkage discipline, shipping boundary) are governed in `G.Core` and are **only cited** here.

**Start here when.** You are authoring a reusable generator, selector, or set-surface scaffold rather than a one-off plan, one-off comparison, or tool-specific method recipe.

**First output.** The six-card chassis `M1…M6` published as a reusable `CGKitId`-bound kit with a scope anchor, local SoTA set, variant pool, shortlist surface, and refresh-ready wiring.

**Neighboring FPF patterns.** Use `G.2` for the local SoTA set, `G.5` for governed set-return selection, `G.10` for shipping surfaces, `G.11` for refresh wiring, and `F.17` when the result must also land on a human-facing UTS surface.

**Common wrong neighboring-pattern changes.** If the real entry load is only a one-off governed comparison or shortlist, use `A.19`, `G.0`, or `G.5`; if the real entry load is project alignment rather than kit authoring, use `A.15`; if tooling choice is being treated as the first kit candidate, keep the case here only after the chassis and its bindings are explicit.

### G.1:1 - Problem frame

You are authoring a **CG‑Frame** and want a **repeatable scaffold** that connects:

* a declared **scope anchor** (`CG‑FrameContext`, `describedEntity`, governing spec refs),
* a **local SoTA set** (scoped and provenance‑anchored),
* a **variant pool** (candidate ideas / decision options / method variants),
* a **shortlist** (a set-surface outcome, not a forced singleton),
* **publication‑ready bindings** into Part‑F artefacts (UTS rows, Name Cards, RSCR tests, worked examples),
* and **refresh readiness** (telemetry hooks + RSCR wiring) without redefining refresh or shipping.

This pattern is intentionally **a chassis**, not a method specification:

* harvesting semantics are governed by `G.2`,
* selection/dispatch semantics are governed by `G.5`,
* CHR/CAL payload semantics are governed by `G.3` / `G.4`,
* shipping semantics are governed by `G.10`,
* refresh orchestration governing definition is `G.11`.

### G.1:2 - Problem

Without a chassis, CG‑Frame authoring tends to fail in repeatable ways:

* **SoTA is not locally scoped**: inputs are “in the air”, not a reconstructible set.
* **Generation is ad‑hoc**: variant candidates are emitted without a stable trace of why/when/how.
* **Selection is opaque**: eligibility/acceptance and assurance are not pinned to explicit surfaces.
* **Outputs don’t land in reusable surfaces**: no clean hand‑off into UTS / RoleDescription / Concept‑Sets / RSCR.
* **No kit‑level snapshot**: the scaffold lacks a versioned manifest, so downstream can’t reliably cite “which chassis edition” was used.
* **Refresh is unplanned**: there is no canonical wiring from edits/telemetry/decay to RSCR causes along the P2W path.

### G.1:3 - Forces

* **Breadth vs. precision:** harvest wide enough to avoid local dogma, but keep the artefact actionable.
* **Generativity vs. assurance:** encourage novelty while keeping evidence, legality, and trust inspectable.
* **Local meaning vs. portability:** keep meaning local by default; crossing must be explicit and auditable.
* **Expressiveness vs. parsimony:** resist inventing new types/slots; prefer reuse and explicit wiring.
* **Stability vs. evolution:** keep stable IDs and pins while allowing SoTA, policies, and editions to evolve.
* **Didactic clarity vs. normative minimalism:** authors need a concrete scaffold, but universal invariants must not be duplicated outside `G.Core`.

### G.1:4 - Solution

#### G.1:4.1 - G.Core linkage (normative)

```
// Canonical form: see G.Core (Nil‑elision + Expansion rule for profiles/sets/pin‑sets).
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.TriStateGuard,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  // Prefer sets; use deltas for pattern‑specific additions.
  RSCRTriggerSetIds := { GCoreTriggerSetId.SoTAHarvestSynthesis },
  RSCRTriggerKindIds := { RSCRTriggerKindId.BaselineBindingEdit },

  // Kit identifiers governed by this pattern (the “six cards”).
  CorePinsRequired := {
    SoTAPaletteDescriptionId,
    SoTA_SetId,
    VariantPoolId,
    ShortlistId,
    CGFrameLibraryId,
    RefreshReadinessCardId,
    CGKitId,

    // Local pointer-map surface for vocabulary + observables-to-CHR anchoring.
    // (May cite `G.0:CG‑Spec.ReferenceMap`; do not duplicate semantics.)
    ReferenceMap,

    // RSCR regression tests used by the chassis (if any).
    RSCRTestId[]?,

    // When the chassis is bound into WorkPlanning (P2W): planned baseline refs.
    SlotFillingsPlanItemRef[]?
  },

  // Consumed defaults (each default cites the governing definition listed in `G.Core.DefaultGoverningDefinitionIndex`).
  DefaultsConsumed := {
    DefaultId.GammaFoldForR_eff,   // governing definition: CC-G5.4
    DefaultId.PortfolioMode,       // governing definition: CC-G5.23
    DefaultId.DominanceRegime      // governing definition: CC-G5.28
  }
⟩
```

**Citation rule (normative):** `CC‑GCORE‑*`, `RSCRTriggerKindId.*`, and `DefaultId.*` semantics are governed by their canonical definitions: primarily `G.Core`, and for the defaults above the definitions listed in `G.Core.DefaultGoverningDefinitionIndex`. `G.1` MUST NOT restate or redefine those semantics.

#### G.1:4.2 - Six‑module generator chassis (normative)

**Core artefact:** `CGFrameReadyGeneratorKit := ⟨M1, M2, M3, M4, M5, M6⟩`, where each `Mi` is a **card** with an explicit I/O surface and stable identifiers.
`CGKitId` identifies the versioned **kit manifest** (`CG‑Kit@CG‑Frame`) that lists the six card ids and the minimal wiring pins needed to treat the chassis as a reusable unit (this is **not** a shipping pack; shipping remains governed by `G.10`).

The chassis is *view‑friendly*: it is an inventory of “what exists and how it is wired”, not a second specification of CN/CG/CHR/CAL/selection semantics.

##### M1 — CG‑FrameContext Card (scope anchor)

**Governs (kit surface):**

* `CG‑FrameContext` and its **binding pins**:

  * `describedEntity := ⟨GroundingHolon, ReferencePlane⟩` *(pin set: `PartG.AuthoringMinimal`)*
  * `CNSpecRef.edition`, `CGSpecRef.edition` *(pin set: `PartG.AuthoringMinimal`)*
  * `ReferenceMap` *(cite `G.0:CG‑Spec.ReferenceMap`; do not duplicate semantics)*
  * any declared crossing/policy pins *(pin set: `PartG.CrossingVisibilityPins`)*

**Purpose:** provide the *single scope anchor* used by all downstream cards.

**Notes:** any spec-legality content is **cited** via `A.19 (CN‑Spec)` and `G.0 (CG‑Spec)` (delegation target: `CC‑GCORE‑CN‑CG‑1` via `CC‑G1‑CoreRef`); this card does not introduce a local “mini‑spec”.

##### M2 — SoTA_Set@CG‑Frame (harvester output card)

**Governs (kit surface):**

* `SoTAPaletteDescriptionId` and `SoTA_SetId` bound to `CG‑FrameContext`
* explicit provenance anchors for the set (via `A.10`), and any published UTS stubs/rows when applicable

**Governing pattern:** harvesting discipline and SoTA-pack payload are governed by `G.2`.
In `G.1`, M2 is a *slot in the chassis* and a wiring surface; it does not redefine the harvesting method.

##### M3 — VariantPool (candidate inventory + emitter trace)

**Governs (kit surface):**

* `VariantPoolId` bound to `CG‑FrameContext`
* per‑candidate minimal traceability fields (emitter identity, `EmitterPolicyRef` (policy‑id/ref; defined by the governing pattern), method/generator refs when declared, edition pins, provenance anchors)
* optional, per‑candidate **assurance preview pointers** (e.g., `PathSliceId?` and/or `SCRId?` when early assurance is recorded) and optional **QD/Open‑Ended scaffolding stubs** (only when introduced by explicit `GPatternExtension` blocks)

**Guardrails (via G.Core):**

* tri‑state eligibility handling, penalties routing, crossing visibility, and set‑return constraints are not defined here; they are enforced via `G.Core` conformance.

**Governing pattern for method payload:** method‑specific emitter semantics are governed by `Extensions` (e.g., `C.17`, `C.18`, `C.19`).
M3 MUST remain method‑agnostic in its core definition: it is an inventory surface, not an algorithm spec.

##### M4 — Shortlist (selector/assurer output)

**Governs (kit surface):**

* `ShortlistId` bound to `CG‑FrameContext`
* a selected set of candidates plus rationale and assurance records (`SCRId` required; `DRRId` optional; cite `PathId/PathSliceId` when applicable)
* optional **front metadata or archive metadata** needed for reproducibility when used: ε‑front parameters and/or archive snapshot hooks, with governing-definition assignment through `G.5` / `C.18` / `C.19` (no local semantics in `G.1`)

**Governing pattern:** selection/dispatch semantics are governed by `G.5`.
M4 MUST preserve *set‑return semantics* (as governed by `G.Core`) and MUST NOT hard‑code a forced singleton outcome.

##### M5 — CG‑FrameLibrary (published bindings index)

**Governs (kit surface):**

* `CGFrameLibraryId` bound to `CG‑FrameContext`
* an index of referenced CG‑Frame artefacts ready for reuse:

  * CHR/CAL/LOG bundles (by their ids; semantics governed by `G.3`, `G.4`, `G.8`)
  * published identifiers (UTS rows, Name Cards) per Part‑F governing definitions
  * additional Part‑F binding surfaces (e.g., RoleDescription templates, Concept‑Set rows) by governing definition‑ids only
  * RSCR test identifiers (e.g., from `F.15`) and worked examples (where applicable)

**Boundary:** M5 is a **kit/library surface**, not shipping. If a shipped pack is needed, governing-definition assignment is `G.10`.

##### M6 — RefreshReadiness Card (telemetry hooks + wiring)

**Governs (kit surface):**

* `RefreshReadinessCardId` bound to `CGFrameLibraryId` (and thus to `CG‑FrameContext`)
* `CGKitId` (the versioned kit manifest) binding `M1…M6` into a single reusable unit; it MUST enumerate the card ids and MAY carry references to deprecations/edition bumps minted by the canonical governing definitions
* declared telemetry hooks (what signals are observed, with what pins)
* declared RSCR wiring: which `RSCRTriggerKindId` are relevant (canonical ids), with minimal required payload pins (including `SlotFillingsPlanItemRef[]` when the chassis is bound into WorkPlanning)

**Boundary:** orchestration semantics are governed by `G.11`.
M6 prepares *refresh‑readiness metadata* and wiring stubs; it does not define scheduling/priority heuristics.

#### G.1:4.3 - Minimal I/O surface (normative)

| Module | Consumes                                                                    | Produces                                                                               |
| ------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| M1     | CG‑Frame brief + `describedEntity` + `CNSpecRef/CGSpecRef` (edition‑pinned) | `CG‑FrameContext` + context pins                                                       |
| M2     | discovery inputs + inclusion criteria *(via G.2)*                           | `SoTA_SetId` (+ provenance anchors; optional UTS stubs/rows)                           |
| M3     | `SoTA_SetId` + local constraints + emitter policy pins *(via Extensions)*   | `VariantPoolId` (+ candidate trace/provenance; optional method payload via Extensions) |
| M4     | `VariantPoolId` + acceptance/eligibility surfaces *(via G.4/G.5)*           | `ShortlistId` (selected set / set-surface) + rationale refs                                         |
| M5     | `ShortlistId` + CHR/CAL/LOG bundle refs + UTS/Name refs                     | `CGFrameLibraryId` (library index; publish‑ready bindings)                             |
| M6     | telemetry inputs + freshness/decay policy pins + RSCR tests                 | `CGKitId` + `RefreshReadinessCardId` (wiring to `G.11`; no orchestration governance)    |

#### G.1:4.4 - Extensions (pattern‑scoped; non‑core)

All method/discipline/generator specifics MUST be expressed as `GPatternExtension` blocks.

> Guard: `G.1:Ext.*` are **PatternScopeId** values (internal, pattern‑scoped), not new patterns and not new `PatternId`.

##### GPatternExtension — `G.1:Ext.HarvesterWiring`

**PatternScopeId:** `G.1:Ext.HarvesterWiring`
**GPatternExtensionId:** `HarvesterWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2`
**Uses:** `{G.2}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoTAPaletteDescriptionId`
* `SoTA_SetId`
* `ClaimSheetId[]` / `BridgeMatrixId` *(as referenced by the chosen G.2 pack form)*
* `CNSpecRef.edition`, `CGSpecRef.edition` *(already required via `GCorePinSetId.PartG.AuthoringMinimal`)*
**RSCRTriggerSetIds:** `{GCoreTriggerSetId.SoTAHarvestSynthesis}`
**Notes (wiring‑only):** harvesting semantics (living review funnels, inclusion policy families, SoS indicator families, etc.) are defined by `G.2` and are not duplicated in `G.1`.

##### GPatternExtension — `G.1:Ext.ShortlistWiring`

**PatternScopeId:** `G.1:Ext.ShortlistWiring`
**GPatternExtensionId:** `ShortlistWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `G.5`
**Uses:** `{G.5, G.4}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ShortlistId`
* `SCRId` *(assurance and rationale record by id; semantics governed by the selector and assurance governing definitions)*
* `DRRId?` *(when a decision‑rationale artefact is minted; otherwise omitted)*
* `TaskSignatureRef?` *(if selection is task‑templated; otherwise omitted)*
* `AcceptanceClauseId[]` *(as referenced from `G.4` outputs)*
* any explicit selector policy pins *(policy‑id/ref; defined by the governing pattern)* when not defaulted (the omitted default cites its governing definition through `G.Core.DefaultGoverningDefinitionIndex`)

**Notes (wiring‑only):** `G.1` does not redefine selection: it binds M4’s output surface to the `G.5` selector/dispatcher kernel.

##### GPatternExtension — `G.1:Ext.CreativityCHR`

**PatternScopeId:** `G.1:Ext.CreativityCHR`
**GPatternExtensionId:** `CreativityCHR`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `C.17`
**Uses:** `{C.17, G.3}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `CHRPackId?` *(if creativity characteristics are published/typed)*
* edition/policy pins required by the chosen creativity characteristic set (governed by `C.17`)

**Notes (wiring‑only):** `G.1` only records which creativity characteristics are used for M3/M4 wiring; legality/typing lives in the CHR governing definitions.

##### GPatternExtension — `G.1:Ext.NQD`

**PatternScopeId:** `G.1:Ext.NQD`
**GPatternExtensionId:** `NQD`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy id / ref, as defined by the governing definition)*
* `TaskSignatureRef?` *(when QD is enabled via TaskSignature flags/traits rather than by an external switch)*
* `DHCMethodRef.edition?` *(when illumination/coverage summaries are pinned to a method)*
* `EmitterPolicyRef` *(policy‑id/ref; points to the exploration governance governing definition, e.g., `C.19` when E/E‑LOG is used)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):** QD/QD‑adjacent algorithm families and their parameterisations belong to `C.18 and C.19`; `G.1` only fixes the pins needed to make the VariantPool and Shortlist reproducible.

##### GPatternExtension — `G.1:Ext.OpenEndedFamilyWiring`

**PatternScopeId:** `G.1:Ext.OpenEndedFamilyWiring`
**GPatternExtensionId:** `OpenEndedFamilyWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2` *(family semantics are governed by SoTA cards; this block only wires pins; selector-side wiring is governed by `G.5`.)*
**Uses:** `{G.2, G.5, C.19, C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyId[]`
* `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
* `EnvironmentValidityRegionRef?`
* `CoEvoCouplerRef[]?`
* `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):** this block enables declared sets of `{Environment, MethodFamily}` pairs without redefining generator semantics in `G.1`; it should cite/align with the selector‑side wiring in `G.5:Ext.OpenEndedFamilyWiring`.

##### GPatternExtension — `G.1:Ext.RefreshWiring`

**PatternScopeId:** `G.1:Ext.RefreshWiring`
**GPatternExtensionId:** `RefreshWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.11`
**Uses:** `{G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `RefreshReadinessCardId`
* `RSCRTestId[]`
* canonical `RSCRTriggerKindId[]` emitted/recorded (aliases only as labels, if any)
**RSCRTriggerSetIds:** `{GCoreTriggerSetId.RefreshOrchestration}`
**Notes (wiring‑only):** M6 declares readiness and wiring; orchestration semantics (queueing, prioritisation, cadence) are governed by `G.11`.

##### GPatternExtension — `G.1:Ext.ShippingWiring`

**PatternScopeId:** `G.1:Ext.ShippingWiring`
**GPatternExtensionId:** `ShippingWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.10`
**Uses:** `{G.10}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `CGFrameLibraryId`
* `SoTAPaletteDescriptionId`, `SoTA_SetId`
* `CHRPackId?`, `CALPackId?`, `SoS‑LOGBundleId?`, `ParityReportId?` *(as present in the library index)*
* `EvidenceGraphId?`, `BridgeMatrixId?`, `BridgeCalibrationTableId?` *(when cited by the shipped artefacts)*
* `UTSRowId[]?` *(when any public ids are minted/published)*
* `SlotFillingsPlanItemRef[]?` *(when planned baseline is bound by id into the shipment surface)*
**Notes (wiring‑only):** this block does not define shipping; it only records the minimum wiring from the chassis/library index to `G.10` when shipping is performed.

### G.1:5 - Archetypal Grounding — Tell–Show–Show (informative)

**Tell.** Use the six‑card chassis to make a CG‑Frame authoring effort reproducible: a scoped SoTA set, a traceable candidate pool, a set‑return shortlist, a publishable library index, and refresh readiness—without redefining spec-legality/selection/refresh governing definitions.

**Show A (R&D multi‑criteria decisions; post‑2015 SoTA practice).**

* **M1:** define `CG‑FrameContext` for “R&D decision options”, pin `CNSpecRef/CGSpecRef` editions, and publish `describedEntity` + `ReferencePlane`.
* **M2:** build `SoTA_SetId` via `G.2` using a living‑review style funnel (e.g., PRISMA‑like trace + update cadence) and publish UTS stubs for reusable constructs.
* **M3:** emit a `VariantPoolId` where each candidate cites its emitter policy and provenance; if QD is used, wire `DescriptorMapRef.edition` and `DistanceDefRef.edition` via `G.1:Ext.NQD`.
* **M4:** produce `ShortlistId` as a selected-set / shortlist surface via `G.5`, with acceptance predicates sourced from `G.4`.
* **M5:** publish a `CGFrameLibraryId` indexing the chosen CHR/CAL/LOG bundles and UTS rows; register RSCR tests.
* **M6:** declare refresh readiness (telemetry pins + canonical RSCR trigger kinds) and wire to `G.11`.

**Show B (clinical operations; safety‑first acceptability).**

* **M1:** scope a CG‑Frame around dose adjustment decisions; pin legality and evidence minima explicitly.
* **M2:** harvest SoTA models and safety constraints as a reconstructible set (governed by `G.2`).
* **M3:** generate policy‑constrained candidate protocols; emitter trace and evidence pins are mandatory.
* **M4:** shortlist remains a set; “choose one” remains an explicit policy decision, not silently baked into the generator.
* **M5/M6:** publish and wire refresh (decay events, policy changes, and evidence updates retrigger along the P2W path).

### G.1:6 - Bias‑Annotation (informative)

* **Recency bias:** “newest paper wins” (mitigate with explicit inclusion criteria and update cadence in `G.2` wiring).
* **Novelty bias:** over‑rewarding novelty at the expense of legality/assurance (mitigate by making acceptance and assurance pins explicit and governed).
* **Algorithmic favoritism:** baking a preferred generator into “the chassis” (mitigate by keeping M3 method‑agnostic and pushing methods into Extensions).
* **Scalarisation bias:** collapsing selected sets or partial orders into a single score (mitigate by set‑return discipline pinned through `G.Core`).
* **Hidden‑crossing bias:** implicit reuse across contexts (mitigate by explicit crossing pins and Bridge‑only routing via `G.Core`).

### G.1:7 - Conformance Checklist (normative)

| ConformanceId     | Statement   |
| ----------------- | ----------- |
| **CC‑G1‑CoreRef** | The pattern MUST satisfy the **effective** `CoreConformanceIds` implied by `G.1:4.1` (`GCoreConformanceProfileId` expansion + deltas), per `G.Core` expansion rules.   |
| CC‑G1‑01          | The reusable CG-Frame kit MUST include all six cards `M1…M6` with stable ids **and** a versioned kit manifest `CGKitId`, including at minimum: `{CGKitId, CG‑FrameContext, SoTAPaletteDescriptionId, SoTA_SetId, VariantPoolId, ShortlistId, CGFrameLibraryId, RefreshReadinessCardId}`.  |
| CC‑G1‑02          | `M1` MUST bind the kit to a single `CG‑FrameContext` and MUST expose the required pins from `GCorePinSetId.PartG.AuthoringMinimal` (including `describedEntity` and `CNSpecRef/CGSpecRef` editions). `M1` MUST also expose (or explicitly cite) a `ReferenceMap` surface and MUST NOT restate its semantics (cite `G.0:CG‑Spec.ReferenceMap`).  |
| CC‑G1‑03          | `M2` MUST be wired to `G.2` (or explicitly cite the `G.2` artefacts governed by cited patterns) and MUST be reconstructible as a scoped set, including `SoTAPaletteDescriptionId` + `SoTA_SetId` (not free‑floating prose). Provenance MUST be anchored via `A.10` for the emitted set.  |
| CC‑G1‑04          | `M3` MUST record emitter provenance as a wiring surface, including `EmitterPolicyRef` (policy‑id/ref), edition pins, and provenance anchors (via `A.10`). Any method‑specific fields MUST be introduced only via `GPatternExtension` blocks.   |
| CC‑G1‑05          | `M4` MUST be wired to `G.5` (or explicitly cite `G.5` artefacts governed by cited patterns) and MUST preserve set-surface outcomes. `SCRId` MUST be present (or explicitly cited to the governing definition surface) so assurance is id‑addressable; `DRRId` SHOULD be present when a decision‑rationale artefact is minted.   |
| CC‑G1‑06          | `M5` MUST publish a library/index surface that points to referenced CHR/CAL/LOG artefacts and to any minted public ids (`UTSRowId[]`, Name Cards) via the canonical governing definitions (Part F), without introducing shadow specs (delegation target: `CC‑GCORE‑CN‑CG‑1` via `CC‑G1‑CoreRef`).    |
| CC‑G1‑07          | `M6` MUST publish `CGKitId` and expose refresh‑readiness wiring: canonical `RSCRTriggerKindId[]` applicability + minimal payload pins (including `SlotFillingsPlanItemRef[]` when applicable) and RSCR test ids; orchestration semantics MUST be cited to `G.11`.  |
| CC‑G1‑08          | Any method/discipline/generator specificity in `G.1` MUST be located in `G.1:4.4` as `GPatternExtension` blocks with `PatternScopeId`, `GPatternExtensionKind`, and `GoverningPatternId` (or `governing pattern not yet selected` only for Phase-3 seeds). If QD/illumination or Open‑Ended generator families are declared, the corresponding extension blocks MUST be present and MUST carry the edition and policy pins required by the governing pattern. |


### G.1:8 - Common Anti‑Patterns and How to Avoid Them (informative)

* **Anti‑pattern: “Shadow CN/CG spec inside the chassis.”**
  *Avoid:* keep CN/CG as cited governing spec refs; use pins and governing definition references only.

* **Anti‑pattern: “Chassis hard‑codes a favourite algorithm.”**
  *Avoid:* keep M3 core method‑agnostic; add algorithm families only via Extensions with explicit governing patterns and edition pins.

* **Anti‑pattern: “Shortlist = one winner.”**
  *Avoid:* preserve selected-set returns; any singleton choice must be an explicit downstream decision rule (policy‑bound).

* **Anti‑pattern: “Refresh plan described as prose triggers.”**
  *Avoid:* record canonical `RSCRTriggerKindId` and payload pins; aliases only as labels and only if docked.

* **Anti-pattern: “Packaging implies shipping governance.”**
  *Avoid:* treat M5 as a library index; treat M6 as readiness wiring; ship only via `G.10`.

### G.1:9 - Consequences (informative)

* **Repeatable authoring:** CG‑Frame work becomes reconstructible: what exists, what it depends on, and how it is refreshed.
* **Method pluralism with discipline:** multiple generator/selector families can coexist without turning the chassis into a shadow method spec.
* **Better reuse:** outputs land directly in published artefacts (UTS/Name/RSCR‑ready) rather than remaining local notes.
* **Lower refactor cost:** method changes localise to Extensions; core invariants remain stable and one governing definition.

### G.1:10 - Rationale (informative)

* **Why six cards?** It matches the minimal decomposition needed to keep scope, harvesting, generation, selection, publication, and refresh **explicitly separable** (and thus auditable and evolvable).
* **Why “kit/index” rather than “pack”?** A CG‑Frame authoring effort must stay modular; shipping is a separate governing boundary (`G.10`).
* **Why push method content into Extensions?** It prevents conflating (i) universal invariants, (ii) frame‑specific kit surfaces, and (iii) method/generator families—supporting Phase‑2 universalisation goals.
* **Why working‑model first?** Many CG‑Frames fail due to premature formalism; a chassis with didactic micro‑examples improves correctness of pins, names, and boundaries before deep formalisation.

### G.1:11 - SoTA‑Echoing (informative)

This chassis is designed to stay compatible with modern (post‑2015) practice without confusing “SoTA” with “currently popular”:

* **Evidence synthesis:** living systematic review protocols (e.g., PRISMA‑style traceability and update cadence) map naturally to M2 wiring governed by `G.2`.
* **Quality‑Diversity and archives:** modern QD families (MAP‑Elites‑class, CMA‑ME‑class, and related archive‑based exploration) fit as M3/M4 extensions (`C.18`/`C.19`) because they require explicit descriptor/distance/insertion pins and preserve set‑valued outcomes.
* **Open‑ended exploration:** post‑2015 open‑endedness systems (POET‑class, paired/adversarial environment generation lines, and modern curriculum‑generation approaches) fit when treated as generator‑family wiring (governed elsewhere) rather than as chassis semantics.
* **Set‑valued decision outputs:** modern multi‑objective and set‑valued evaluation practices align with the `G.Core` set‑return discipline, preventing hidden scalarisation.
* **Governed traceability:** contemporary reproducibility and accountability norms (mechanism disclosure, provenance anchors, and audit trails) are supported via pinned policies/editions and explicit module boundaries, without introducing data‑governance machinery.

### G.1:12 - Relations

**Builds on:** `G.Core`, `E.8`, `E.10`, `E.19`.
**Uses:** `A.10 (Provenance Anchors)`, `A.15.3 (SlotFillingsPlanItem)`, `A.19 (CN‑Spec)`, `G.0 (CG‑Spec)`, `G.2 (SoTA Synthesis Pack)`, `G.3 (CHR Pack@CG‑Frame)`, `G.4 (CAL Pack@CG‑Frame)`, `G.5 (Selector & Dispatch)`, `G.10 (Shipping)`, `G.11 (Refresh Orchestration)`, and (via Extensions) `C.17, C.18, and C.19`.
**Publishes to / consumes from:** Part‑F publication surfaces (UTS, naming, RSCR tests, Role/Concept artefacts) as cited by their governing definitions.

### G.1:End

## G.2 - SoTA Harvester & Synthesis

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative *(unless explicitly marked informative)*
>
> **Purpose.** Provide a repeatable, auditable way to **discover**, **triage**, and **synthesize** state‑of‑the‑art (SoTA) across competing `Tradition` lineages *before* minting CHR/CAL/LOG assets for a `CG‑Frame`.
> The primary output is a **`SoTA Synthesis Pack@CG‑Frame`** that feeds:
>
> * naming/publication (UTS),
> * CHR authoring (G.3),
> * CAL authoring (G.4),
> * method/generator registries and dispatch (G.5).
>
> **Scope note.** This pattern **governs** the harvesting + synthesis *generator* in Part G. Shipping governing-definition assignment is in **G.10**, refresh orchestration governing-definition assignment is in **G.11**.
>
> **Terminology note (normative).** In normative clauses below, **`Tradition`** refers to the *Tech* token `Tradition` (a plural lineage with internally coherent commitments). Plain “tradition” is allowed only as a 1:1 synonym.

### G.2:1 - Problem frame

A team extends FPF into a new `CG‑Frame`. The relevant literature is typically:

* **plural** (multiple `Tradition` lineages with incompatible commitments),
* **context‑sensitive** (results depend on `U.BoundedContext` and declared `describedEntity`),
* **method‑heterogeneous** (different evidence styles, operator sets, and validity regions),
* **time‑sensitive** (rapid drift post‑2015; frequent benchmark/protocol shifts).

Downstream Part‑G work (CHR/CAL/selection/shipping/refresh) depends on the team producing **consumable, citation‑ready artefacts** without collapsing semantic boundaries across contexts or planes.

### G.2:2 - Problem

How can we systematically assemble a SoTA view that is:

1. **pluralist but comparable** (plurality preserved; comparability is achieved only via explicit crossings),
2. **evidence‑addressable** (claims cite auditable evidence surfaces and anchors),
3. **actionable** (produces inventories and cards that G.3/G.4/G.5 can consume),
4. **refreshable** (editions/policies/windows are pinned so RSCR/refresh can re‑audit and re‑run without semantic drift)?

### G.2:3 - Forces

* **Pluralism vs. consolidation.** Consolidation is valuable, but unqualified fusion destroys meaning.
* **Breadth vs. load‑bearing depth.** Too broad becomes shallow; too deep misses rival lineages.
* **Recency vs. stability.** Freshness matters, yet durable “backbone” claims must be identified and kept visible.
* **Pedagogy vs. rigour.** Outputs must be teachable enough to support review, while remaining audit‑ready.
* **Authoring vs. operations.** This pattern lives in the authoring plane; operational runs and decisions belong to Work planes and to governing patterns.

### G.2:4 - Solution

#### G.2:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  CorePinSetIds := {GCorePinSetId.PartG.CrossingVisibilityPins},

  CorePinsRequired := {
    // Scope pins (G.2‑specific)
    CG-FrameContext,
    Tradition[],
    describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
    SoTA_SetId,
    SoTAPaletteDescriptionId,

    // Evidence / provenance pins (G.2‑specific)
    CorpusLedgerId,
    FlowRecordId,
    EvidenceAnchorRef[],
    EvidenceGraphId?,

    // Crossing / synthesis pins (delta beyond CorePinSetIds; only when used)
    GammaEpistSynthId[]?,

    // Edition / policy pins (only when used)
    HarvestPolicyRef?,
    DistanceDefRef.edition?,
    InclusionCriteriaId?,
    ScreeningRubricId?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩`

*(RSCR payload pins: `ClaimSheetId[]`, `SoTA_SetId`, `SoTAPaletteDescriptionId`, `BridgeMatrixId?`, `GammaEpistSynthId[]?`, `UTSRowId[]?`, `DistanceDefRef.edition?`, `HarvestPolicyRef?`, `InclusionCriteriaId?`, `ScreeningRubricId?`, `PathId/PathSliceId?` when path‑citable evidence or a stable freshness window is pinned.)*

**Pattern‑local default rules (governed by this pattern; not a Part‑G‑wide `DefaultId`).**

`FamilyCoverageFloorK := 3` *(unless explicitly overridden by `HarvestPolicyRef` and recorded in `FlowRecord`)*

#### G.2:4.2 - Kit: `SoTA Synthesis Pack@CG‑Frame` (surface governed by this pattern)

A conforming `G.2` publication produces a **notation‑independent pack** whose internal organisation is free, but whose exported **named components and views** are stable and citable:

Each named component is addressable via a stable **pack‑local identifier** (e.g., `CorpusLedgerId`, `ClaimSheetId`, `FlowRecordId`) for citation and RSCR scoping. If any component is minted/evolved as a **public id**, it is published and cited via `UTSRowId[]` per `CC‑GCORE‑UTS‑1` (delegation).

0. **`SoTA_Set@CG‑Frame`** *(export view; “M2 output” consumed downstream)*
   A read‑optimised view over the harvested candidate set that downstream generator/selector work treats as the “harvester output set”.
   **Constraint (normative):** `SoTA_Set@CG‑Frame` **MUST** be reconstructible from pack components by id (no “hidden extra set”).

1. **`G.2a CorpusLedger`**
   Ledger of candidate sources with Context and triage status (e.g., include / park / retire) and explicit rationale hooks.

2. **`G.2b ClaimSheets[Tradition]`**
   Typed Claim Sheets per `Tradition`, each with:

* explicit `U.BoundedContext` and `describedEntity`,
* explicit evidence anchors/citations (A.10 and/or EvidenceGraph refs when available),
* explicit freshness window notes and risk/trust cues *(cite `B.3` governing definitions when using trust/decay language)*.

3. **`G.2c OperatorAndObjectInventory`**
   Inventory of candidate CHR terms (characteristics/scales/coordinates) and candidate CAL operators/flows *as stubs* for downstream authoring.

4. **`G.2d BridgeMatrix`**
   A citable alignment/divergence surface across `Tradition`×`Tradition`, with explicit losses and row scopes.
   If any row asserts substitution or fusion across sources or across `Tradition` records, the pack **MUST** attach a `GammaEpistSynthId` record (alias: **`G.2‑F`**) per `G.2:Ext.GammaEpistSynthesis` (no silent fusion).

5. **`G.2e MicroExamples`**
   Worked micro‑examples for load‑bearing claims, each citing A.10 carriers, declaring context + `describedEntity`, and annotating assurance type(s) (`TA`/`VA`/`LA`, where applicable).

6. **`G.2f UTSProposals`**
   Draft Name Cards + Minimal Definitional Sheets (MDS) + alias proposals (incl. concept‑set linkage where applicable), with the required publication pins.

7. **`G.2g describedEntity Map`**
   Map from key terms/claims/public ids to `GroundingHolon`, `ReferencePlane`, and minimal reference cues for later CHR/CAL authoring.

8. **`G.2h PRISMA Flow Record`**
   A screening/eligibility trail for how sources entered the pack (method‑profile is allowed; see Extensions).
   *(Name is historical; the artefact remains notation‑independent.)*

9. **`G.2i SoSIndicatorFamilies`**
   Indicator *families* as variants (windows/constraints/assumptions) **with explicit Acceptance branches per variant** (branch ids/labels only; threshold semantics belong to CAL governing definitions).

10. **`G.2j MethodFamilyCards`**
    Candidate method families with a shared signature and a plurality of implementations, each with validity regions, cost/complexity notes, and known failure modes.
    When the pack targets downstream registry/dispatch, MethodFamily cards **SHOULD** include the declared refs and pins `G.5` needs (eligibility predicate refs, assurance profile cues, and the pack ids that justify the family).

11. **`G.2k GeneratorFamilyCards`** *(if applicable)*
    Candidate generator families for environment/task generation with declared validity regions and transfer hooks.

12. **`G.2l Annexes`** *(optional; governing-definition-cited; see Extensions)*
    For example: QD/NQD annexes, discipline‑specific indicator annexes, interop forms.

**SoTAPaletteDescription** *(export view; required downstream)*
A view‑friendly description object (pack‑local `SoTAPaletteDescriptionId`) that binds together:
* the `SoTA_Set@CG‑Frame` view,
* `ClaimSheetId[]`, `OperatorAndObjectInventory`, `BridgeMatrixId?`,
* `SoSIndicatorFamilies` (with variant/branch structure),
* `MethodFamilyCards` / `GeneratorFamilyCards?`,
* `MicroExamples`, `UTSProposals`,
* and the `describedEntity Map` for citation and later CHR/CAL authoring.
**Note (normative intent):** this is the primary “consumable surface” for `G.3/G.4/G.5`; it prevents downstream patterns from scraping free prose.

**Editorial template: 1‑page “SoTA Sheet” per Tradition (informative).**
When authoring `ClaimSheets[Tradition]`, teams often benefit from a single‑page template: scope + claims + evidence anchors + validity region + failure modes + freshness window + cross‑Tradition reuse notes + pointers to micro‑examples.

#### G.2:4.3 - Harvester loop (conceptual choreography; pattern-governed)

A conforming `G.2` pack publication is built by iterating the following conceptual loop until the declared gates are satisfied:

1. **Declare scope and plurality.**
   Declare `CG-FrameContext`, the initial `Tradition` set, and the `describedEntity` surface for each intended claim region. Record these declarations in the pack pins (not as implicit assumptions).

2. **Discover and triage sources (ledger‑first).**
   Populate `CorpusLedger` via:

* seed sources,
* expansion via citation chaining and keyword family exploration,
* pruning using load‑bearing relevance tests tied to the declared CG‑Frame scope.

3. **Distill claims per `Tradition`.**
   For each `Tradition`, author a Claim Sheet that preserves internal commitments and cites evidence anchors. Do not fuse cross‑`Tradition` claims at this stage.

4. **Inventory operators/objects for downstream authoring.**
   Extract candidate measurement terms and operator stubs for later CHR/CAL authoring (without asserting legality or thresholds locally).

5. **Build alignment/divergence surfaces.**
   Where reuse across `Tradition` is desired, author Bridge‑backed alignment records and explicit loss notes in `BridgeMatrix`. Any consolidation is explicitly marked as requiring alignment proof.

6. **(Alias: G.2‑F) Produce Γ_epist synthesis records when fusion/substitution is asserted.**
   If a `G.2` pack publication asserts fusion or substitution across sources or across `Tradition` records (beyond mere “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records per `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit object alignment refs + assurance tuple refs), and it **MUST** keep penalties routed to `R_eff` only by delegation (`CC‑GCORE‑PEN‑1`).

7. **Publish teachable micro‑groundings.**
   Attach worked micro‑examples to load‑bearing claims, each tied to A.10 carriers and declaring context + `describedEntity`.

8. **Apply gates and record repairs.**
   Enforce `FamilyCoverageFloorK` (and any optional diversity‑by‑distance gate). If a gate fails, the pack **MUST**:
   * record the failure and the repair iteration in `FlowRecord` and `CorpusLedger`,
   * pin the updated `HarvestPolicyRef` / criteria ids (if changed),
   * iterate the loop rather than silently weakening the gate.

9. **Emit hand‑off manifests and export views.**
   Produce explicit manifests to:

* `G.3` (CHR authoring),
* `G.4` (CAL authoring),
* `G.5` (registry/dispatch),
  so that downstream work can cite pack components by id rather than re‑authoring them.
   The pack **MUST** also export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as the default downstream consumption surfaces (ids pinned).

#### G.2:4.4 - Interfaces (minimal I/O Standard)

| Interface         | Consumes                                                      | Produces                                                                    |
| ----------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **G.2‑1 Harvest** | `CG-FrameContext`, initial `Tradition[]`, `HarvestPolicyRef?`  | `SoTA Synthesis Pack@CG‑Frame` (G.2a–G.2l)                                  |
| **G.2‑2 Extend**  | existing Pack + new sources/anchors + updated policy pins     | updated Pack + RSCR‑relevant trigger emissions (canonical kinds)            |
| **G.2‑3 HandOff** | Pack                                                          | `CHR‑handoff` (to G.3), `CAL‑handoff` (to G.4), `Registry‑handoff` (to G.5) |

*Note:* Orchestration of re‑runs is governed by `G.11`; this pattern only defines what a conforming (re)harvest produces and what pins it must expose.

#### G.2:4.5 - Extensions (pattern‑scoped; non‑core)

`Extensions` are pattern‑scoped annexes. They do not introduce Part‑G‑wide norms; they declare the additional pins required when those semantics are active and cite the corresponding governing patterns.

###### G.2:4.5.1 - GPatternExtension: GammaEpistSynthesis

**PatternScopeId:** `G.2:Ext.GammaEpistSynthesis`
**GPatternExtensionId:** `GammaEpistSynthesis`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2`
**Uses:** `{G.Core, B.3, F.9, G.6}` *(penalty routing + trust/decay cues + bridges/CL + evidence path citation when used)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GammaEpistSynthId[]` *(pack‑local ids of synthesis records; emitted iff fusion/substitution is asserted)*
* `EvidenceAnchorRef[]` *(provenance union; A.10 carriers)*
* `BridgeMatrixId` and `BridgeCardId[]` *(explicit object alignment references when crossing is involved)*
* `CL/CL^plane` + `Φ/Ψ/Φ_plane policy-ids` *(ids only; semantics governed by cited definitions; penalties → `R_eff` only by delegation)*
* `PathId/PathSliceId?` *(only when citing via `G.6`)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`

**Notes (normative intent; duplication‑avoidant):**
* `Γ_epist^synth` is an auditable record that binds: (i) provenance union, (ii) explicit object alignment refs, (iii) assurance tuple refs (via existing governing definitions) for each asserted fusion/substitution.
* This extension **does not** redefine `Γ‑fold`, `Φ`, or penalty semantics; it only requires the pins/refs needed for replayability and auditability (see `G.Core` delegations).

###### G.2:4.5.2 - GPatternExtension: HarvestProtocols

**PatternScopeId:** `G.2:Ext.HarvestProtocols`
**GPatternExtensionId:** `HarvestProtocols`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `G.2`
**Uses:** `{B.3, A.10}` *(for freshness/decay and provenance anchors, when protocol requires them explicitly)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `HarvestPolicyRef` *(declares the chosen protocol family and its parameters)*
* `FlowRecordId` *(protocol‑specific profile id or rubric id may be attached here)*
* `InclusionCriteriaId` / `ScreeningRubricId` *(ids only; semantics remain local to the protocol family)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (extension discipline):**
* This extension binds a declared protocol profile to the pack’s `FlowRecord` without redefining evidence semantics.

###### G.2:4.5.3 - GPatternExtension: DHCAlignmentHooks

**PatternScopeId:** `G.2:Ext.DHCAlignmentHooks`
**GPatternExtensionId:** `DHCAlignmentHooks`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `C.21` *(DHC semantics are governed by C.21)*
**Uses:** `{C.21, G.6, G.7}` *(DHC series + evidence path citations + bridge/CL regimes when alignment density is claimed)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DHCMethodRef.edition`
* `WindowRef?` *(if the DHC series is windowed)*
* `DHCSenseCellId[]` *(pack‑local ids for emitted DHC SenseCells; if any are public, cite via `UTSRowId[]`)*
* `UTSRowId[]?` *(only if any DHC SenseCells / series ids are minted/evolved as public ids)*
* `PathId[]` / `PathSliceId[]` *(when alignment summaries cite evidence paths via G.6)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TelemetryDelta}`

**Notes (extension discipline):**
* If DHC alignment summaries are emitted, this extension ensures the DHC method edition and the cited evidence paths are visible.
* Units/constraints (governing pattern: `C.21`) must be **pinned, not redefined** here (e.g., `bridges_per_100_DHC_SenseCells`, `CL_min = 2` for cross‑Context counting, and the “CL=3 implies free substitution” interpretation when used).

###### G.2:4.5.4 - GPatternExtension: NQDAnnex

**PatternScopeId:** `G.2:Ext.NQDAnnex`
**GPatternExtensionId:** `NQDAnnex`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` *(NQD-CAL semantics are governed by C.18; explore/exploit logging is governed by C.19 when used)*
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy‑id/ref)*
* `EmitterPolicyRef` *(policy‑id/ref)*
* `TaskSignatureRef?` *(when QD mode is trait‑gated)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (extension discipline):**
* This extension only pins the required references for replayability; it does not redefine QD semantics, dominance, or acceptance rules.

###### G.2:4.5.5 - GPatternExtension: InteropForms

**PatternScopeId:** `G.2:Ext.InteropForms`
**GPatternExtensionId:** `InteropForms`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.13`
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `MappingPolicyRef` *(policy‑id/ref)*
* `UTSRowId[]` *(for published external ids/aliases where relevant)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`

**Notes (extension discipline):**
* Interop affects only representation and citation routes; it must not introduce alternate legality gates or acceptance semantics.

#### G.2:4.6 - Palette first

- `SoTAPaletteDescription` is one plurality-preserving palette.
- It is not by itself one `Front`, one `Archive`, or one `Shortlist`.
- When that palette's members are traditions, `TraditionPalette` is the reader-facing tradition-only palette head over the same palette declaration, not one second governing definition. For methods, hypotheses, or other members, keep `SoTAPaletteDescription` or `Palette + SubjectKind` explicit instead.
- Traditions remain in the palette until a later surface declares comparison, retention, or choice semantics explicitly.
- `TraditionFront` is one derived view over the declared palette under one declared `Q`; the `Q` basis stays pinned separately and the view does not rename `Tradition` or `SoTAPaletteDescription`.
- `TraditionArchive` is one derived retention view over that same palette under one declared reachability or coverage rule; that rule stays pinned separately and the view does not turn the palette into one archive by default.
- When one derived tradition view is shown, keep the base palette recoverable at the same time.
- When comparison or retention needs richer geometry or atlas language, treat that as support for the derivation rather than as the default meaning of the palette.
- A reader should be able to say both `this is the palette` and `this is the derived tradition view currently being shown` without collapsing those two objects.

#### G.2:4.7 - Atlas views stay optional neighboring support over one declared palette and declared set surfaces

- `TraditionAtlasView` is one declared optional neighboring support view over one palette and any declared front, archive, or shortlist surfaces drawn from it, while the cited substrate-bearing line, the active source surface or active set surface, and any cited `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space refs remain recoverable.
- `TraditionAtlasView` is the `G.2` use-site specialization of `CrossSurfaceAtlasView`; keep the generic support view declaration in `A.19.SUPPORT-VIEW`.
- It is not the default meaning of `Tradition` or `SoTAPaletteDescription`.
- Stay palette-first when the harvest or synthesis question can already be judged from the declared palette together with ordinary front, archive, or shortlist surfaces.
- Use `TraditionAtlasView` only when the reader must hold several declared derived views or support qualifiers together to see why one tradition grouping, omission risk, or comparison boundary matters.
- A conforming `TraditionAtlasView` must keep the same atlas-support declaration that `A.19.SUPPORT-VIEW` requires by value: recoverable base palette, active source surface or active set surface, `TypedSetViews` when several declared set views are held together, cited `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space refs, cited mappings such as `OutcomeMapRef`, cited qualifiers such as `SpaceMetricRef`, `TransitionSupportRef`, and `BridgeDistortionNote`, and one explicit reason why thinner `CrossSurfaceSupportView` is insufficient here.
- It may help explain where one tradition, method family, or retained line sits relative to another, but it should not silently redefine the base palette or one derived front view or archive view.
- If one atlas view uses several typed views over the same source surface, keep the active set surface, any cited `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space ref, and any `BridgeDistortionNote` recoverable instead of letting `TraditionAtlasView` hide those choices.
- Treat the atlas layer as optional neighboring support, not as ordinary palette-first core. Use `SpaceMetricRef` or `TransitionSupportRef` only when one declared comparison, reachability, transition, or cross-scale state-change claim actually depends on that formal support; otherwise leave them unstated.
- Use `OutcomeMapRef` only when the atlas must show how one declared set surface maps into one outcome or effect surface; it does not turn the palette, front, archive, or shortlist into that outcome surface.
- If one atlas reading would materially change the base source-to-outcome relation or distortion posture, reopen the substrate declaration instead of treating that change as one local `G.2` convenience.
- If one thinner `CrossSurfaceSupportView` already keeps the question legible, prefer that thinner support form and leave atlas specialization unused.
- `SearchSpaceRef` and `OutcomeSpaceRef` doctrine, transition-aware novelty, metric-transfer loss, and cross-scale geometry belong to a heavier formal layer: keep them outside ordinary palette-first use unless the current comparison, reachability, transition, or multilevel claim explicitly needs them, and do not pull them in merely because one richer comparative reading is mathematically available.
- If no declared atlas view is needed, stay with the simpler palette-first and declared-derived-view surfaces.
- Different atlas views may rely on different declared spaces, metrics, bridges, or transition supports; keep that plurality visible rather than forcing one geometry monoculture across every neighboring view.
- If several mathematical traditions remain plausible, keep that plurality visible rather than pretending the atlas already fixes one final formalism.
- If the question is naming-side only, use `F.18` for that wording choice rather than letting atlas support language carry the naming decision by itself.

### G.2:5 - Archetypal Grounding (System / Episteme)

| Template element   | `U.System` illustration                                                                                                                                                                                                                                                  | `U.Episteme` illustration                                                                                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tell**           | A safety engineering team needs to choose a control stack across multiple engineering “schools” (robust control, learning‑based control, formal verification), under a declared operational context and a concrete `describedEntity` (the vehicle + operating envelope). | A research group must synthesize SoTA on “decision quality” across competing lineages (causal decision theory, evidential variants, bounded rationality, and active‑inference‑style formalisms), each with distinct evidence norms and semantics.       |
| **Show (failure)** | The team merges terms across contexts, treats incompatible test protocols as comparable, and collapses multiple partially ordered trade‑offs into one unqualified score. The resulting design cannot explain why a later safety review disagrees.                        | The group produces a single “best” metric of decision quality and retrofits definitions to fit it. Later, conflicting claims cannot be traced because evidence anchors and crossing losses were never made explicit.                                    |
| **Show (repair)**  | A conformant `G.2` pack keeps parallel Claim Sheets per `Tradition`, publishes explicit alignment/loss notes where reuse is attempted, and emits hand‑offs so CHR/CAL/selection can be authored without re‑inventing semantics.                                          | A conformant `G.2` pack preserves plural claims, publishes explicit bridge‑backed alignment where justified, represents indicators as families/variants, and makes evidence anchors and freshness windows visible so downstream re‑audits are possible. |

### G.2:6 - Bias-Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Selection bias (Gov/Onto).** Any harvesting protocol can over‑represent certain venues, languages, or evidence styles.
  *Mitigation:* pluralism floor + explicit `CorpusLedger` + explicit protocol pins.

* **Consolidation bias (Onto/Epist).** Pressure to “merge” lineages can erase incompatible commitments.
  *Mitigation:* keep Claim Sheets disjoint by default; require explicit alignment proof for fusion; preserve loss notes.

* **Recency bias (Prag).** Overweighting newest papers can hide durable backbone results; underweighting them misses SoTA drift.
  *Mitigation:* publish freshness windows and make them RSCR‑relevant.

* **Didactic bias (Did).** Micro‑examples can steer interpretation toward familiar domains.
  *Mitigation:* require heterogeneous substrates and explicit A.10 anchors.

### G.2:7 - Conformance Checklist (normative) — **CC‑G2**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                                                                                        | Purpose / Notes                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **CC‑G2‑CoreRef**         | A conforming `G.2` artefact **MUST** satisfy the **effective** core obligations declared by the `GCoreLinkageManifest` in `G.2:4.1` (per `G.Core` Expansion rule).                                                                                                                                                                                 | Phase‑2 bridge clause: ensures universal invariants are not redefined inside `G.2`. |
| **CC‑G2‑Pluralism‑1**     | A conforming pack **MUST** include at least **two** `Tradition` lineages and at least **three** distinct declared `U.BoundedContext` entries across the corpus.                                                                                                                                                                                        | Prevents single‑lineage “SoTA” from masquerading as synthesis.                      |
| **CC‑G2‑Ledger‑1**        | A conforming pack **MUST** include `G.2a CorpusLedger` with inclusion/triage status and explicit rationale hooks per entry.                                                                                                                                                                                                                        | Makes discovery/triage auditable.                                                   |
| **CC‑G2‑FlowRecord‑1**    | A conforming pack **MUST** include `G.2h FlowRecord` that traces identification → screening → eligibility → included at a minimum granularity sufficient to reproduce the corpus boundary.                                                                                                                                                         | Prevents “mystery inclusion” and supports refresh.                                  |
| **CC‑G2‑ClaimSheets‑1**   | For each included `Tradition`, a conforming pack **MUST** include a `ClaimSheetId` that declares `U.BoundedContext`, `describedEntity`, evidence anchors, and freshness notes; it **MUST NOT** fuse cross‑`Tradition` claims by default.                                                                                                                 | Keeps plurality explicit and prevents hidden crossings.                             |
| **CC‑G2‑Palette‑1**       | A conforming pack **MUST** export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as citable views (via `SoTA_SetId`, `SoTAPaletteDescriptionId`) and ensure both are reconstructible from pack components by id (no hidden extra structure).                                                                                                      | Prevents downstream scraping of prose; keeps “M2 output” explicit.                  |
| **CC‑G2‑Palette‑2**       | If the pack exports one derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep `SoTAPaletteDescription` explicit as the default base palette, keep that derivation recoverable, and cite the declared `Q` or reachability/coverage rule that disciplined that view. Derived tradition views **MUST NOT** silently replace the palette's default meaning. | Keeps non-default tradition views recoverable without redefining palette-first semantics. |
| **CC‑G2‑AtlasSupport‑1**  | If the pack exports `TraditionAtlasView`, it **MUST** satisfy the same support view declaration required by `A.19.SUPPORT-VIEW`: keep the base palette and active source surface or active set surface recoverable, name `TypedSetViews` when several declared set views are held together, cite any active `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space refs, cite any active `OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, or `BridgeDistortionNote` only when they do real explanatory work, state why thinner `CrossSurfaceSupportView` is insufficient here, and **MUST NOT** use atlas form when palette-first or thinner `CrossSurfaceSupportView` is sufficient. | Keeps the `G.2` specialization at least as constraining as the general `CrossSurfaceAtlasView` declaration and preserves space-role recoverability. |
| **CC‑G2‑describedEntityMap‑1** | A conforming pack **MUST** include `G.2g describedEntity Map`, mapping (at minimum) each load‑bearing claim family and each minted/evolved public id to `describedEntity := ⟨GroundingHolon, ReferencePlane⟩`, and citing the relevant `ClaimSheetId` and evidence anchors (A.10 and/or G.6 paths when used).                                         | Keeps plane/holon boundaries explicit and citable.                                  |
| **CC‑G2‑Alignment‑1**     | Any cross‑`Tradition` consolidation **SHALL** be presented as either (i) disjoint parallel claims with explicit divergence, or (ii) an explicitly justified alignment proof; any reuse across `Tradition` boundaries **MUST** use explicit crossing bundles per `CC‑GCORE‑CROSS‑1` (delegation).                                                  | Prevents silent semantic leakage.                                                   |
| **CC‑G2‑GammaSynth‑1**    | If the pack asserts **fusion or substitution** across sources or across `Tradition` records (not merely “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records satisfying `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit alignment refs + assurance tuple refs). If no fusion or substitution is asserted, the pack **SHALL** state so explicitly. | Restores the load‑bearing synthesis artefact (alias: `G.2‑F`) without shadow specs. |
| **CC‑G2‑Inventory‑1**     | A conforming pack **MUST** include `G.2c OperatorAndObjectInventory`, sufficient for downstream CHR/CAL authoring to begin without re‑harvesting terms.                                                                                                                                                                                            | Ensures the pack is actionable.                                                     |
| **CC‑G2‑Inventory‑2**     | `G.2c OperatorAndObjectInventory` entries **MUST** be treated as **stubs** for downstream authoring: they **MUST NOT** embed acceptance thresholds or claim legality decisions locally. If an entry is not a citation of an already governed CHR/CAL artefact, it **MUST** be explicitly marked as `stub` (typing/lawfulness `TBD`) and **MUST NOT** be used as if lawful. Legality/threshold semantics are governed by `G.3` for CHR and `G.4` for CAL via explicit ids/pins. | Prevents “shadow CHR/CAL” and preserves lawfulness discipline without redefining it locally. |
| **CC‑G2‑MeasurementLawful‑1** | If any inventory entry is presented as **non‑stub** (i.e., already lawful/typed), the pack **MUST** cite the governing lawfulness discipline (e.g., `A.17–A.19/C.16` as applicable) and provide the minimal evidence anchors needed to justify that typing claim.                                                                                      | Prevents “quietly lawful” measurement claims inside the harvester pack.             |
| **CC‑G2‑MicroExamples‑1** | For every load‑bearing claim family, a conforming pack **MUST** include **at least two** worked micro‑examples on **heterogeneous substrates**, each with explicit A.10 carrier anchors, declared context + `describedEntity`, and an assurance tag (`TA`/`VA`/`LA`, where applicable).                                                          | Makes the synthesis teachable and anchor‑grounded.                                  |
| **CC‑G2‑UTS‑1**           | If the pack proposes or evolves any public ids, it **MUST** publish UTS proposals *(Name Cards + MDS where applicable)* and cite them via `UTSRowId[]`, satisfying `CC‑GCORE‑UTS‑1` (delegation).                                                                                                                                               | Keeps naming and evolution disciplined.                                             |
| **CC‑G2‑Families‑1**      | SoS indicators and candidate evaluation constructs **SHALL** be represented as **families/variants** (windows/constraints/assumptions) **with explicit Acceptance branch structure per variant** (branch ids/labels only), not as single unqualified scalars; any scalar summary **MAY** be included only as report‑only unless explicitly promoted by governing patterns. *(Set-return discipline is delegated to `CC‑GCORE‑SET‑1`.)* | Prevents covert scalarization and keeps acceptance governed by downstream patterns.                |
| **CC‑G2‑HandOff‑1**       | A conforming pack **MUST** emit hand‑off manifests to `G.3`, `G.4`, and `G.5` that cite pack components by id and identify which families/operators are intended for downstream formalisation or registry entry.                                                                                                                                   | Prevents downstream re‑authoring and drift.                                         |
| **CC‑G2‑CoverageGate‑1**  | The pack **MUST** declare `FamilyCoverageFloorK` and enforce it as a harvesting gate. It **MUST** either (i) specify `k` explicitly in an explicit `HarvestPolicyRef`, or (ii) use the pattern‑local default rule governed by `CC‑G2‑CoverageGate‑1`. *Default rule (pattern-local):* `k=3`. If the gate fails, the pack **MUST** (a) record the repair iteration in `FlowRecord`, and (b) broaden the search radius (new venues/corpora/contexts/traditions) rather than silently weakening the gate; if an exploration policy is used for this broadening, it **MUST** be pinned as a policy id/ref. | Makes “coverage floor” explicit and prevents “silent narrowing” under failure.      |
| **CC‑G2‑DistanceGate‑1**  | If a diversity‑by‑distance gate is used, the pack **MUST** pin `DistanceDefRef.edition` and the declared threshold (δ), and treat edits as RSCR‑relevant per `CC‑GCORE‑TRIG‑*` (delegation). If no such gate is used, the pack **SHALL** explicitly state that it is not used.                                                                     | Avoids implicit distance defaults and improves refreshability.                      |
| **CC‑G2‑RSCR‑1**          | A conforming pack **MUST** emit canonical `RSCRTriggerKindId` causes (not free text) for edits to evidence surfaces, name/tokenization surfaces (e.g., UTS proposals/aliases), crossings, planes, edition pins, and harvesting policy pins (`HarvestPolicyRef`), per `CC‑GCORE‑TRIG‑1…TRIG‑4` (delegation).                                                                                      | Keeps refresh reason codes stable and typed.                                        |
| **CC‑G2‑Ext‑GammaEpist‑1** | If `G.2:Ext.GammaEpistSynthesis` is used (i.e., any fusion/substitution is asserted), the pack **SHALL** expose the required pins listed in that extension and **SHALL NOT** redefine `Γ‑fold/Φ/penalty` semantics locally (cite governing definitions by delegation).                                                                                       | Keeps synthesis auditable without creating shadow specs.                            |
| **CC‑G2‑Ext‑HarvestProtocols‑1** | If `G.2:Ext.HarvestProtocols` is used, the pack **SHALL** expose the required pins/criteria ids listed in that extension and **SHALL NOT** redefine evidence/quality semantics outside the declared protocol profile.                                                                                                                            | Keeps protocol variation explicit and separately citable.                           |
| **CC‑G2‑Ext‑DHC‑1**       | If `G.2:Ext.DHCAlignmentHooks` is used, the pack **SHALL** (a) expose the required pins listed in that extension, including `DHCSenseCellId[]`, and (b) declare the unit/constraint pins required by `C.21` (e.g., `bridges_per_100_DHC_SenseCells`, `CL_min=2`) without redefining their semantics locally (governing pattern: `C.21`).                                                             | Keeps DHC extension pins auditable and non‑shadowing.                              |
| **CC‑G2‑Ext‑NQD‑1**       | If `G.2:Ext.NQDAnnex` is used, the pack **SHALL** expose the required pins/editions/policies listed in that extension and **SHALL NOT** redefine QD semantics locally.                                                                                                                                                                             | Keeps QD/OEE extension pins replayable and non‑shadowing.                          |
| **CC‑G2‑Ext‑Interop‑1**   | If `G.2:Ext.InteropForms` is used, the pack **SHALL** expose the required interop pins and **SHALL NOT** introduce alternative legality/acceptance semantics.                                                                                                                                                                                      | Prevents “foreign gate” shadowing.                                                  |

### G.2:8 - Common Anti‑Patterns and How to Avoid Them

* **AP‑G2‑1: “One true SoTA score.”**
  **Avoid:** selecting a single unqualified scalar metric as “the” SoTA.
  **Do instead:** represent evaluation constructs as families/variants; keep partial orders set‑returning (delegated).

* **AP‑G2‑2: Fusion without explicit alignment proof.**
  **Avoid:** merging rival `Tradition` claims into one statement “by common sense.”
  **Do instead:** preserve parallel Claim Sheets; if consolidation is required, publish explicit alignment proof or keep a divergence record.

* **AP‑G2‑3: Hidden protocol drift.**
  **Avoid:** changing the harvesting protocol (inclusion criteria, windowing, screening rubric) without pins.
  **Do instead:** pin harvesting policy/profile ids and treat changes as RSCR‑relevant.

* **AP‑G2‑4: Unanchored pedagogy.**
  **Avoid:** micro‑examples without carriers (they become folklore).
  **Do instead:** bind micro‑examples to A.10 anchors and declare `describedEntity`.

* **AP‑G2‑5: Atlas by default.**
  **Avoid:** writing as if every tradition comparison or NQD/OEE note needs `TraditionAtlasView`, or as if atlas wording renames the palette itself.
  **Do instead:** keep the base palette and derived front, archive, or shortlist explicit; use atlas form only when several declared views or support qualifiers must be held together, and prefer thinner `CrossSurfaceSupportView` when that is enough.

### G.2:9 - Consequences

* **Positive:** Downstream CHR/CAL/dispatch work becomes faster and less ambiguous because the pack is citable and structured.
* **Positive:** Plurality is preserved while still enabling disciplined comparability through explicit crossings.
* **Positive:** Refresh becomes tractable because pins and typed causes exist.
* **Negative:** Adds authoring overhead (ledger, flow record, micro‑examples, explicit pins).
* **Negative:** Requires governance discipline to prevent the pack from becoming an uncontrolled “everything bucket”.

### G.2:10 - Rationale

SoTA synthesis is a bottleneck for new `CG‑Frame` work: without a disciplined harvest, downstream formalization (CHR/CAL) and operational selection (G.5) either (i) inherit hidden semantic collisions, or (ii) re‑invent incompatible “mini‑standards.”
`G.2` resolves this by treating SoTA work as a **publishable kit**: explicit plurality, explicit crossings, explicit evidence anchors, and explicit hand‑offs.

### G.2:11 - SoTA-Echoing (informative)

This pattern aligns its *method options* (via Extensions and authoring practice) with widely used post‑2015 SoTA practices, while keeping FPF’s semantics stable and id‑based:

1. **PRISMA 2020 reporting discipline** (Page et al., 2021)
   *Status:* **Adopt (adapted)** — we adopt the idea of a transparent screening trail as `FlowRecord`, but keep it notation‑independent and concept‑level.

2. **Living systematic reviews** (Elliott et al., 2017 and subsequent living‑review practice)
   *Status:* **Adopt (as optional protocol family)** — the “living” stance is expressed as a harvesting protocol profile (Extension), with explicit freshness windows and RSCR‑relevant change causes.

3. **AMSTAR 2 critical appraisal** (Shea et al., 2017)
   *Status:* **Adapt** — we adapt the idea of structured quality appraisal into Claim Sheet evidence cues, without turning it into a single scalar rating.

4. **Science of Science synthesis** (Fortunato et al., 2018)
   *Status:* **Adopt (as content discipline)** — SoS indicators are treated as families/variants and wired as citable artefacts, not as a single “score”.

5. **Disruption / team‑structure indicators** (Wu, Wang & Evans, 2019 and follow‑on work)
   *Status:* **Adopt (as exemplar family)** — useful as an example of a SoS‑indicator family with material dependence on windowing and corpus definition.

6. **Quality‑Diversity and open‑ended generation** (e.g., Fontaine et al., 2020 for CMA‑ME; Wang et al., 2019 for POET)
   *Status:* **Adopt (as optional annex with explicit pin declarations)** — when QD/OEE is relevant for the `CG‑Frame`, we include generator/method family cards and pin the required edition/policy surfaces via `G.2:Ext.NQDAnnex`, without embedding those semantics into the core pack.

### G.2:12 - Relations

* **Builds on:**

  * `G.Core` (core invariants, typed RSCR causes, Default Governing Definition Index)
  * `E.8` (pattern template discipline)
  * `E.10` (lexical/ontological rules; strict distinction; kind‑suffix discipline)
  * `E.19` (conformance discipline)
  * `A.10` (provenance anchors / carriers)
  * `A.19.SUPPORT-VIEW` (generic support-view and atlas discipline when `TraditionAtlasView` is used)
  * `A.6.P` (space/view/publication precision restoration when palette/support claims collapse)
  * `B.3` (trust, freshness/decay as cited governing patterns)
  * `F.9` (bridges and CL as cited governing patterns)
  * `F.17` (UTS publication discipline; via delegation)
  * `G.0` (CG‑Spec legality gate; cited when legality surfaces are referenced)
  * `G.6` (EvidenceGraph / path citation surfaces when used)

* **Used by:**

  * `G.1` (generator chassis consumes harvested SoTA sets)
  * `G.3` (CHR authoring consumes operator/object inventory and claim sheets)
  * `G.4` (CAL authoring consumes operator stubs, acceptance branch scaffolding)
  * `G.5` (registry/dispatch consumes MethodFamily/GeneratorFamily cards)
  * `G.10` (shipping cites the pack as payload)
  * `G.11` (refresh orchestration can re‑invoke harvest via typed causes)

* **Relates to:**

  * `G.13` (interop surfaces when external indices are used)
  * `F.18` (naming-side support wording when the question is label choice rather than synthesis geometry)

### G.2:End

---

## G.3 - CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates

**Tag.** Architectural pattern (CHR kit; publishes lawful measurement primitives; constrains CAL authoring and selector/dispatch use)
**Stage.** *design‑time* (authoring & publication; enables admissible run-time consumption by `G.4` / `G.5`)
**Primary output.** `CHR Pack@CG‑Frame` — a notation‑independent, UTS‑published CHR bundle that provides: typed Characteristics/Scales/Levels/Coordinates, legality + guard surfaces, aggregation/comparison specs, RSCR hooks/tests, and provenance pins.
**Primary hooks.** `G.1` (CG‑FrameContext), `G.2` (SoTA synthesis inputs), `A.19.CHR` (CHRMechanismSuite boundary + pins), `A.15.3` (SlotFillingsPlanItem baseline), `A.18/C.16` (MM‑CHR legality), `F.1–F.9` (Contexts/UTS/Bridges), `B.3` / `B.3.4` (trust, freshness/decay), `A.10` (provenance anchors/carriers), `G.6` (EvidenceGraph/Path citation), optional `C.18 and C.19` (QD/OEE wiring), `G.11` (refresh orchestration).
**Non‑duplication note.** Universal Part‑G invariants (bridge‑only crossings, tri‑state semantics, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, defaults with one governing definition, linkage discipline) are governed by `G.Core`. This pattern cites them via `G.3:4.1` and delegates where needed.

### G.3:1 - Problem frame

A team is defining or evolving a `CG‑Frame` (via `G.1`) and has plural, competing SoTA traditions and constructs (via `G.2`). The team needs a *admissibility-ready CHR publication* that makes downstream work possible without hidden semantic drift:

* **CAL authoring (`G.4`)** needs typed, admissible operands and guard/legality surfaces to build admissibility and acceptance rules (thresholds and policy cut‑offs remain governed by CAL).
* **Selector/dispatch (`G.5`)** needs CHR‑typed quantities and explicit provenance pins so selection can remain set-returning and auditable under admissible orders.
* **Cross‑context reuse** must be explicit (bridges + loss accounting + pinned policy ids), and refresh must be tractable by typed RSCR causes rather than prose.

The resulting publication is a **CHR Pack** that is **CG‑Frame‑scoped**, **notation‑independent**, and **UTS‑published**, with explicit edition/policy pins sufficient for reproducibility and RSCR.

### G.3:2 - Problem

Without a disciplined CHR authoring layer, teams repeatedly produce “measurable slots” that are *numerically manipulable but semantically unlawful*:

* **Meaning leaks** across contexts (same token, different referent/sense).
* **Illicit arithmetic** (e.g., averaging ordinals, mixing units, laundering polarity).
* **Hidden normalizations** that silently change scale type, polarity, or admissible transforms.
* **Unreproducible comparisons** (missing edition pins for methods/distances/policies; unclear reference plane).
* **Unscoped reuse** (no explicit bridge and loss notes; unclear `describedEntity` changes).
* **Un-auditable aggregation** (no explicit legality surface and guard surface; no proof hooks; unclear Γ‑fold governing-definition assignment).
* **Refresh chaos** (changes in names/editions/policies do not map to typed RSCR causes).

### G.3:3 - Forces

| Force                                             | Tension                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Pluralism vs comparability**                    | Preserve tradition‑specific meaning ↔ enable admissible cross‑tradition use.       |
| **Expressiveness vs legality**                    | Model rich measurement semantics ↔ block illegal operations “by construction”. |
| **Portability vs honesty**                        | Encourage reuse ↔ forbid implicit crossings and hidden loss.                   |
| **Ease of authoring vs auditability**             | Keep authoring teachable ↔ require explicit pins, provenance, and tests.       |
| **Downstream flexibility vs upstream discipline** | Let CAL/selector choose policies ↔ keep thresholds/policy cut‑offs out of CHR. |

### G.3:4 - Solution — CHR authoring kit and publication surface

#### G.3:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative; size‑controlled).**

`GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
},
CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
GCorePinSetId.PartG.CrossingVisibilityPins
},

// Pins strengthened for CHR authoring (delta over PinSets)
CorePinsRequired := {
// NOTE: `CG-FrameContext`, `describedEntity`, `CNSpecRef.edition`, `CGSpecRef.edition` are already required
// by `GCorePinSetId.PartG.AuthoringMinimal` (cite, don’t restate here).
UTSRowId[],                      // required: CHR terms are public ids (Name Cards plus public-id continuity records)
PathId[]/PathSliceId[],          // required: worked examples/tests and refresh anchoring cite paths
ReferencePlane,                  // required: definitional claims are plane-scoped
Φ/Ψ/Φ_plane policy-ids?,         // iff crossings/plane moves are exercised in examples or imports
ΓFoldRef.edition?                // iff an explicit Γ-fold artefact is pinned (otherwise use DefaultId)
// NOTE: method-/discipline-specific pins (e.g., DescriptorMapRef/DistanceDefRef/DHCMethodRef/InsertionPolicyRef)
// are declared only inside Extensions (e.g., `G.3:Ext.QD_OEE_Wiring`) to keep core linkage universal.
},

// consumed iff any published `CHR.AggregationSpec` relies on default Γ-fold (no explicit override pinned)
DefaultsConsumed := { DefaultId.GammaFoldForR_eff },

RSCRTriggerKindIds := {
RSCRTriggerKindId.EvidenceSurfaceEdit,
RSCRTriggerKindId.TokenizationOrNameChange,
RSCRTriggerKindId.CrossingBundleEdit,
RSCRTriggerKindId.ReferencePlaneEdit,
RSCRTriggerKindId.EditionPinChange,
RSCRTriggerKindId.PolicyPinChange,
RSCRTriggerKindId.DefaultGoverningDefinitionChange,
RSCRTriggerKindId.FreshnessOrDecayEvent,
RSCRTriggerKindId.LegalitySurfaceEdit,
RSCRTriggerKindId.BaselineBindingEdit
}
⟩`

*(Nil‑elision + expansion rule are per `G.Core:4.2`. This pattern does not redefine the semantics of core conformance ids, trigger kinds, or defaults; it only declares applicability and required pins.)*

#### G.3:4.2 - Output surface: `CHR Pack@CG‑Frame` (normative)

`CHR Pack@CG‑Frame` is the CHR kit payload that downstream patterns cite and pin (it is not a “shadow spec” for CN/CG).

**Minimum exported objects (kit surface):**

* `CHR.Characteristic[]`
* `CHR.Scale[]`
* `CHR.Level[]` *(when the scale type requires explicit level sets / order structure)*
* `CHR.Coordinate[]` *(encodings + legality annotations; never an implicit “upgrade” of measurement structure)*
* `CHR.Guards` *(guard macro surface; semantics governed by cited definitions; see `G.Core` and `A.18`)*
* `CHR.LegalityMatrix` *(admissible operations per scale type / unit / polarity regimes)*
* `CHR.AggregationSpecs` *(typed aggregators/comparators + proof hooks + edition pins where applicable)*
* `UTS` publication bundle: Name Cards (twin labels), public-id continuity notes, and (when applicable) bridge and loss notes
* RSCR artefacts: `RSCRTestId[]` + worked examples + provenance pins (ReferencePlane, Path/PathSlice, policy ids)

**Mandatory provenance pins (conceptual, notation‑independent):**

* `ReferencePlane`
* `PathId/PathSliceId` citations for worked examples/tests
* R‑anchors (conceptual; KD‑CAL lanes when used) realised via `PathId/PathSliceId` and, where applicable, `A.10` anchor/carrier refs
* policy pins used by crossings or plane moves (when exercised)
* edition pins for any referenced method or metric definitions that affect interpretation

#### G.3:4.3 - CHR authoring chassis (S1–S8)

**S1 — Charter the measurement scope (scope anchor).**
Declare the CHR `U.BoundedContext` and scope for the CG‑Frame, including: `describedEntity` boundaries, `ReferencePlane`, freshness/decay expectations, and the list of contested terms likely to require bridging. Output a design‑time `MeasurementCharter` and `KindMap@Context`.
If freshness/decay expectations are anything beyond an explicit “non‑decaying” declaration, wire them via
`G.3:Ext.DecayWiring` (governing pattern: `B.3.4`) rather than encoding decay semantics in CHR prose.
If assurance‑subtype lane tags are used (e.g., TA/VA/LA), declare the lane regime here so downstream evidence discipline can remain lane‑pure (taxonomy/semantics governed by `B.3`; evidence‑path representation & audit governed by `G.6`; this pattern only records wiring).
**Lane docking (wiring‑only; normative).**
If `EvidenceLanes` are used, the charter MUST:
* enumerate the lane tags used (e.g., TA/VA/LA) and cite their governing pattern taxonomy (governed by `B.3`), plus the upstream provenance for their use when available (e.g., `SoTAPaletteDescriptionId` via `G.3:Ext.SoTAPackInputs`);
* expose any lane‑dependent tolerances / proof requirements via explicit pins (policy‑id and/or edition‑pinned refs), not prose;
* treat lane tags as provenance metadata (not Contexts): they MUST NOT be “bridged away” or silently mixed;
* if any cross‑lane comparison/aggregation is claimed, it MUST be explicit and pinned to the governing acceptance/evidence policy (typically `G.4`) and auditable via evidence paths (`G.6`); otherwise downstream consumers treat it as illegal.
*Crossing semantics and penalty routing are cited via `G.Core` (do not restate).*

**S2 — Mint or reuse terms (UTS‑first).**
For each candidate characteristic, scale, level, or coordinate term: attempt reuse; otherwise mint via UTS Name Cards with twin labels and public-id continuity notes. When a term is imported across contexts, the import must be explicit and auditable (bridge and loss notes live with the crossing artefacts; CHR only cites them).

**S3 — Define `CharacteristicCard` (the CHR unit of meaning).**
A CharacteristicCard is the minimum unit CHR publishes for downstream legality. It SHOULD include (field names are indicative; semantics governed by cited definitions):

`CharacteristicCard := ⟨
  UTSRowId,
  Context,
  ReferencePlane,
  ObjectKind,
  Intent,
  Definition (typed),
  ObservableOf := ⟨instrument/protocol (A.10 anchors/carriers), uncertainty model, validity window⟩,
  EvidenceLanes? (KD‑CAL lanes; wiring only; semantics governed by `G.4` / `G.6`),
  ScaleRef,
  Polarity ∈ {↑, ↓, ⊥},
  Domain/Range,
  UnitSet,
  Bounds / zero semantics (as applicable),
  Freshness / half‑life (or explicit `NonDecayingDecl`; freshness/decay semantics governed by `B.3.4`),
  Missingness semantics (typed; include a classification/mapping when non‑trivial; downstream tri‑state handling is per G.Core),
  Stability/Reliability notes,
  RoleDecls? := RoleDecl[] (wiring‑only; each role declaration names its governing pattern + required pins; see `G.3:4.5`),
  QD.Role? ∈ {Q, D, QD-score} (interop alias for `RoleDecl` with `GoverningPatternId = C.18`; see `G.3:Ext.QD_OEE_Wiring`),
  Micro‑examples (R‑anchors: Path/PathSlice cited; lane tags where applicable)
⟩`

Where `RoleDecl := ⟨ roleLabel, GoverningPatternId, EditionPins?, PolicyPins? ⟩` (wiring-only; the value of `GoverningPatternId` names the FPF pattern that governs the role declaration semantics).

Rules (CHR‑governed intent, semantics governed by cited definitions where indicated):

* Scale/unit/polarity legality obligations cite MM‑CHR governing definitions (`A.18` and `C.16`) and must be *checkable* by downstream patterns.
* Missingness must be typed so downstream can apply tri‑state outcomes without silent coercion (tri‑state semantics are governed by `G.Core`).
* If `EvidenceLanes` are recorded, they are only lane tags for downstream evidence discipline (taxonomy governed by `B.3`; audit surface: `G.6`; any cross‑lane policy is governed by `G.4`); this pattern does not introduce lane semantics or invent bridge‑like constructs.
* If `RoleDecls` are used, each declaration MUST cite the FPF pattern that governs the declaration, for example `C.18` or `C.19`, and surface the edition and policy pins required by that governing pattern; CHR does not define role semantics locally.
* **Role docking (normative, wiring-only):** if any `RoleDecl` is present with `GoverningPatternId = X`,
  then `G.3` MUST include (or explicitly cite) a corresponding `GPatternExtension` block whose governing definition is `X`
  (or whose `Uses` includes `X`) and that surfaces the required pins for that role family. Otherwise the role
  declaration is non-conformant (it is an undocked semantic fragment).
* **Freshness docking (normative, wiring-only):** if a characteristic’s freshness/half-life is defined via a named
  decay model/policy (rather than a pure local statement), the relevant policy/ref MUST be pinned and cited through `B.3.4`
  via `G.3:Ext.DecayWiring`.
* If a characteristic is intended to be *promoted into* `CG‑Spec`, the linkage is explicit and edition‑pinned (wiring lives in an Extension; semantics governed by `G.0`).

**S4 — Define `ScaleCard` and `LevelCard` (lawful measurement).**
Publish the scale type and admissible transforms, plus levels/orders when applicable. CHR does not invent new legality semantics; it cites MM‑CHR governing definitions and makes the legality surface concrete for the frame’s characteristics.

Typical distinctions that must be representable:

* **Nominal / categorical:** equality + counting; transforms are permutations.
* **Ordinal:** order‑preserving transforms; no arithmetic that presupposes intervals.
* **Interval:** affine transforms; differences meaningful; means may be lawful if justified.
* **Ratio:** positive scalar transforms; ratios meaningful; products/sums subject to unit discipline.
* **Count / rates:** explicit exposure/timebase requirements; rate conversions must be explicit.
* **Cyclic:** wrap‑around discipline + principal interval declaration.

**S5 — Define `CoordinatePolicy` (encodings without hidden cardinalization).**
When a numeric coordinate/embedding is used for convenience or tooling, CHR MUST publish:

* what invariants are preserved (order only / ratios / topology / wrap‑around),
* what remains illegal,
* what proof hooks are required if a structure with higher scale-type commitment is claimed.

A coordinate never silently upgrades a scale type; if an upgrade is claimed, the proof requirement is explicit and carried by MM-CHR governing definitions.

**S6 — Publish legality + guard surfaces (Guard Macros + LegalityMatrix).**
CHR publishes a `CHR.LegalityMatrix` and a `CHR.Guards` surface that downstream operators can reference.

Guard macro names are allowed as authoring ergonomics, but their semantics MUST cite governing definitions (no “shadow semantics” in this pattern). Examples of macro intents (governing definitions in parentheses):

* `CSLC_PROOF_REQUIRED(x)` (MM‑CHR legality governing definitions: `A.18/C.16`)
* `UNKNOWN_TRI_STATE(x)` (tri‑state semantics governed by `G.Core`)
* `UNIT_CHECK(x)` (MM‑CHR legality governing definitions)
* `RETURN_SET_FOR_PARTIAL_ORDERS()` (set‑return semantics governed by `G.Core`)
* `METRIC_EDITION_REF(...)` (edition‑pin discipline governed by `G.Core`; metric semantics governed by `C.18`/`C.21` as applicable)

**S7 — Publish `AggregationSpecs` (typed, admissible, reproducible).**
CHR may publish typed aggregation/comparison specs that are *safe by construction* and usable as building blocks by `G.4` and `G.5`. For any published spec:

* The legality regime is explicit (scale/unit/polarity constraints + required proof hooks).
* If a contributor folding policy (Γ‑fold) is used and not explicitly overridden, cite `DefaultId.GammaFoldForR_eff` through `G.Core.DefaultGoverningDefinitionIndex`; do not restate the default here.
* If method‑role declarations imply metric‑driven comparisons (e.g., QD roles), the relevant edition/policy pins are surfaced (wiring lives in an Extension; semantics governed by the referenced patterns).

**S8 — Publish, test, and evolve (UTS + RSCR readiness).**
Publish the CHR pack and associated Name Cards to UTS. Attach:

* RSCR tests that check legality and guard coverage and reject illegal ops,
* worked examples with Path/PathSlice provenance,
* refresh/decay notes and deprecations with lexical continuity.

This step prepares the RSCR loop but does not govern orchestration (governing definition: `G.11`).

#### G.3:4.4 - Interfaces (normative)

| Interface                           | Consumes                                          | Produces                                                         |
| ----------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------- |
| **G.3‑1 Charter_CHR**               | `CG‑FrameContext` (`G.1`), SoTA inputs (`G.2`)    | `MeasurementCharter`, `KindMap@Context`                          |
| **G.3‑2 MintOrReuse_Terms**         | candidate terms + UTS registry                    | Name Cards + UTS ids for `Characteristic/Scale/Level/Coordinate` |
| **G.3‑3 Define_Characteristic**     | `MeasurementCharter`, candidate semantics         | `CHR.Characteristic[]` (CharacteristicCards)                     |
| **G.3‑4 Define_ScaleLevel**         | CharacteristicCard + MM‑CHR rules                 | `CHR.Scale[]`, `CHR.Level[]`                                     |
| **G.3‑5 Define_CoordinatePolicy**   | Scale/Level + use‑case constraints                | `CHR.Coordinate[]` + legality annotations                        |
| **G.3‑6 Publish_GuardsAndLegality** | Scale/Level/Coordinate set                        | `CHR.Guards`, `CHR.LegalityMatrix`                               |
| **G.3‑7 Publish_AggregationSpecs**  | CHR set + legality hooks + (optional) metric refs | `CHR.AggregationSpecs` (+ proofs/refs + pins)                    |
| **G.3‑8 Publish_CHRPack**           | all CHR artefacts + tests/examples                | `CHR Pack@CG‑Frame` + UTS rows + RSCR tests                      |

#### G.3:4.5 - Extensions (pattern‑scoped; non‑core)

All blocks below are `GPatternExtension` modules (PatternScopeId-scoped; **not** new PatternIds). They store wiring only and cite governing patterns.

**GPatternExtension: SuiteBoundaryLinkage**

* **PatternScopeId:** `G.3:Ext.SuiteBoundaryLinkage`
* **GPatternExtensionId:** `SuiteBoundaryLinkage`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `A.19.CHR`
* **Uses:** `{A.19.CHR, A.15.3}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CHRMechanismSuiteDescriptionRef.edition?` *(when the suite description is cited as a reproducibility baseline)*
  * `CHRMechanismSuiteSlotFillingsPlanItem` refs *(when planned baseline binds CHR artefacts into WorkPlanning)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.BaselineBindingEdit, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):** This module binds CHR authoring outputs to the P2W seam (`SlotFillingsPlanItem`); suite semantics and membership are governed by `A.19.CHR`.

**GPatternExtension: SoTAPackInputs**

* **PatternScopeId:** `G.3:Ext.SoTAPackInputs`
* **GPatternExtensionId:** `SoTAPackInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `ClaimSheetId[]` / operator & object inventory refs (as cited inputs)
  * `SoTAPaletteDescriptionId?` (when palette/traces are cited; used to dock contested‑term inventory and (if present) lane tags/tolerances)
  * `BridgeMatrixId?` (when terms/constructs are imported across traditions)
  * `UTSRowId[]` drafts/aliases from synthesis
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.CrossingBundleEdit}`
* **Notes (wiring‑only):** SoTA pluralism inputs are governed by `G.2`; this module only specifies which synthesis artefacts are cited while authoring CHR.

**GPatternExtension: CGSpecPromotionWiring**

* **PatternScopeId:** `G.3:Ext.CGSpecPromotionWiring`
* **GPatternExtensionId:** `CGSpecPromotionWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `G.0`
* **Uses:** `{G.0}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CGSpecRef.edition` *(when a characteristic is promoted/linked into `CG‑Spec`)*
  * `CHR.Characteristic.id` pointers included in `CG‑Spec.Characteristics := [...]` *(no shadow ids; CG‑Spec stores pointers, see `G.0`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** Promotion semantics and legality gate governing-definition assignment stays with `G.0`; CHR only pins and cites.

**GPatternExtension: MMCHRLegalityWiring**

* **PatternScopeId:** `G.3:Ext.MMCHRLegalityWiring`
* **GPatternExtensionId:** `MMCHRLegalityWiring`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `A.18`
* **Uses:** `{A.17, A.18, C.16}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * CSLC legality proof anchors/carriers (ids/refs as defined by MM‑CHR governing definitions; cite `A.18/C.16`)
  * Unit coherence references (where units exist)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.ReferencePlaneEdit}`
