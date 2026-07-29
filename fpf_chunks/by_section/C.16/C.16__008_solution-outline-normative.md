---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:5"
section_title: "Solution - Outline (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__008_solution-outline-normative.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:5 — Solution - Outline (Normative)"
line_start: 46892
line_end: 47047
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:5 - Solution - Outline (Normative)

**S1 — Exported objects.** C.16 **exports** four measurement constructs to be used by any FPF pattern:

1. **`U.DHCMethod`** — a *measurement template* (a Definition) that binds **one `U.Characteristic`** to **one Scale form**, with declared **polarity** and (optionally) a **citation point** to the governing FPF pattern, method description, Bridge, or specification record for any non-trivial equivalence or comparability claim that is relied upon elsewhere. **References** to this template use `U.DHCMethodRef`. It is a *measurement-definition specification*, not a record layout.
2. **`U.Measure`** — an *assertion* that a **subject** occupies a **Coordinate** (or **Level**, if discrete) on that Scale; the measure **references** its template and carries a **conceptual pointer to evidence** (`U.EvidenceStub`).
3. **`U.Unit`** — the *unit kind* associated with the Scale where applicable (physical quantities, normalized “points”, “stars”, “%”); unit coherence is part of comparability conditions.
4. **`U.EvidenceStub`** — a *conceptual locator* of grounds for the asserted value (type, identifier, brief summary, optional integrity notion); sufficiency criteria are **conceptual** (see §9 below).

**S2 — Comparability stance (boundary‑aware).** C.16 states only the **direct** comparability condition for measurement claims: *same template* (hence, same Characteristic, Scale, and Unit semantics by reference to A.17 and A.18). Any comparability claim that relies on transformations (normalization, scoring, aggregation, cross‑context transport, bridge losses, admission gating) MUST cite the governing CN-Spec record, CG-Spec record, or relevant mechanism pattern. C.16 does not define those transformations or their laws. (Details: §7–§8 below.)

**S3 — Evidence stance.** A measure that, by its template, **requires** evidence, is **inadmissible** without a meaningful `U.EvidenceStub`. C.16 defines **what it means conceptually** for evidence to “connect” the subject, the Characteristic, and its symbolic description; mechanisms are out of scope. (Details: §9 below.)

**S4 — Role-state-relation framing (open‑endedness).** Readiness, calibration, and revision of metric notions are expressed as role-state-relation assertions and checklist-governed state changes (e.g., “characteristic bound”, “Scale typed”, “Unit coherent”, “ScoringMethod declared”), allowing **re‑entry** when distinctions change; there is no terminal “lifecycle”. (Details: §10 below.)

#### C.16:5.1 - Lexical Discipline & Registers (Normative)

**L1 — Canon.** Use **Characteristic, Scale, Level, Coordinate, Value, Score, Unit, and ScoringMethod** in **Tech** register; their `U.*` counterparts in **Formal**. Narrative labels (e.g., *axis*, *points*, *stars*) are **didactic only**, and are mapped at first mention to the Tech canon (E.10).
**L1‑bis — “metric”.** The noun *metric* is **not** a Tech‑register canonical token for measurables; use **Characteristic, Scale, Coordinate, Score, and ScoringMethod**. It **may** appear in the pattern title and in the Formal names `U.DHCMethodRef` and `U.Measure`. Do not use *metric* as a synonym for **Characteristic** or **Score** in normative prose.
**L2 — Characteristic/template vs Description.** Keep C.16 measurement-definition objects (`U.DHCMethodRef`, `U.Characteristic`) distinct from **descriptions** (rubrics, exemplars) and from **claims** (`U.Measure`). No collapsing of names across these positions.
**L3 — No synonym sprawl.** In normative clauses do **not** substitute *dimension*, *axis*, *property*, or *feature* for **Characteristic**; A.17 governs canonicalization. (C.16 inherits A.17’s rename policy.)
**L4 — Bridge‑only unification.** Cross‑vocabulary sameness appears only via **F.9 Bridges** with **CL** and **loss notes**; C.16’s lexicon is the *source* side for measurement rows.
**L5 — Plain‑register shorthand.** In **Plain** register *metric* MAY be used as shorthand for “template + readings”, but on first use it MUST be mapped to **`U.DHCMethod` (template)** and **`U.Measure` (reading)**, and to the Tech canon terms that matter for meaning.
**L6 — No local CHR-mechanism terminology canon.** Tokens and laws governed by characterization mechanisms (e.g., normalization method tokens, invariant-value notions, indicatorization policy terms) MUST be introduced only by their governing FPF patterns. C.16 may mention them only as **cited** external terms, never as locally defined canon.

#### C.16:5.2 - Relations (pointers; details below)

**To A.17 and A.18.** C.16 *uses* A.17’s canonical **Characteristic** and A.18’s **CSLC sufficiency**; it neither re‑states nor weakens them.
**To Part F.** C.16 is the **exporting pattern** behind measurement rows in UTS rows and Bridges (e.g., **result‑value** ↔ SOSA `Result`, ISO `QuantityValue`).
**To Arch‑CAL.** Architectural qualities (*Coupling, Cohesion, Evolvability*) become **Characteristics** measured via C.16 templates; architectural dynamics read as trajectories in **CharacteristicSpace** (A.17 context).

#### C.16:5.3 - Normative Core Model (types & Standards)

> **Position.** MM‑CHR does **not** redefine kernel terms; it **binds** them to an FPF‑level Standard that every metric must satisfy. Canonical vocabulary and CSLC duties are inherited from **A.17** and **A.18** and referenced here without duplication.
>
> **Governing references.** A.17 and A.18 govern Canon and CSLC; C.16 **adopts by reference** and keeps restatements of their definitions out of scope. C.16 only **exports** `U.*` constructs, comparability stance, evidence semantics, and role-state-relation touch-points.
>
> **CHR boundary reminder.** Any notion that belongs to characterization mechanisms (normalization, indicatorization, scoring, aggregation, comparison, selection) appears in C.16 only as a **pointer** to its governing FPF pattern or specification record. C.16 MUST NOT become a shadow governing pattern for any such terminology or laws.

##### C.16:5.3.1 - `U.DHCMethod` — the measurement template (normative)

**Function.** A measurement-template **Standard** that fixes *what is measured* and *how values must be read*—without producing any values itself. It is a *Definition*, not a Measure. **References** to this template use `U.DHCMethodRef`. *(Didactic: think “the meaning declaration for a reading”.)*

**R-MT-1 (CSLC binding).** A DHCMethod **SHALL** bind to **exactly one** `U.Characteristic` and **exactly one** **Scale‑form** admissible for that Characteristic (cf. A.18). Level is **optional** (used when the scale is enumerated); otherwise values are given directly as Coordinates.

**R‑MT‑2 (Unit).** If the scale carries units (interval or ratio), the template **SHALL** designate a **Unit** of presentation. For ordinal or nominal scales, unit may be absent or a nominal label (e.g., “stars”). (Old MM‑CHR Annex A already listed these structural elements; here we fix the conceptual obligation. )

**R‑MT‑3 (Polarity).** For any ordered scale, the template **SHALL** declare polarity (*higher-is-better*, *lower-is-better*, or *target-is-best*), as a semantic reading aid and as an input to consuming patterns. If polarity is *target-is-best*, the template **SHALL** name the target value (or target set) and MAY cite by reference the governing method description, scoring pattern, normalization pattern, selection pattern, or policy publication that carries any tolerance or fall-off convention used by downstream mechanisms or methods. C.16 does **not** standardize tolerance or fall-off semantics.

**R‑MT‑4 (Applicability).** A template **SHALL** state the **applicability frame** (what kinds of subjects it meaningfully applies to) in conceptual terms; this is a property of the definition, not of any measure.

**R‑MT‑5 (Template vs description).** The template is a **measurement template**. Any rubric, checklist, or prose that explains it is a **Description**; they are related but not identical (E.10 discipline).

**R‑MT‑6 (Cardinality hint).** A Template **MAY** declare its intended **cardinality semantics** for a subject within a **time stance** (e.g., *latest‑only*, *at‑most‑one‑per‑day*, *time series*).
Where declared, claims outside that semantics are **inadmissible conceptually** (they must be reframed or versioned). *Purpose:* prevent silent duplicates and mixed regimes without imposing storage logic.

**R‑MT‑7 (MAY).** `UncertaintyPolicy` — optional conceptual guidance on how uncertainty is expressed or read (e.g., band, confidence interval, or quantile), without prescribing methods/tools.
*(Informative examples: calibrated probability with a confidence band; a prediction interval; a set‑valued reading such as a prediction set.)*

##### C.16:5.3.2 - `U.Measure` — the recorded reading (normative)

**Function.** A **claim** that a subject occupies a **Coordinate** (or named **Level**) on the template’s scale, backed by a minimal pointer to its grounds.

**R‑ME‑1 (Template binding).** Every Measure **SHALL** reference exactly one DHCMethodRef; its **Value or Coordinate** must be **valid** for that template’s scale (type, range, category).

**R‑ME‑2 (Subject).** A Measure **SHALL** identify its **subject‑of‑measurement** (the bearer) unambiguously in the same Context of meaning as the template’s applicability frame.

**R‑ME‑3 (Evidence stub).** Where the template requires it, a Measure **SHALL** include an **EvidenceStub**—a conceptual pointer sufficient to support independent reasoning about the claim’s origin. Use only the conceptual grounding role here; storage-level traceability and provenance mechanisms are governed elsewhere.

**R‑ME‑4 (Time stance).** A Measure **SHALL** carry a **time stance** (e.g., “as‑observed at T”, or “as‑aggregated over W”), expressed conceptually; it disambiguates the reading’s intended window without prescribing formats.

**R‑ME‑5 (Entity vs relation).** If the Characteristic is **relational**, the subject is a **tuple** (pair, k‑tuple); the wording of the claim reflects that arity and the template’s relation topology (cf. A.17).

**R‑ME‑6 (MAY).** `UncertaintyStub` — optional conceptual pointer to the adopted uncertainty estimation for this Measure, **if** required by the template.

> *Informative source reference.* The “Article Completeness” example illustrates the split template/measure/evidence; **C.16** keeps the split but keeps storage-level talk out of scope.

##### C.16:5.3.3 - `U.Unit` — semantics of quantities (normative)

**Function.** A conceptual marker of **quantity kind** and admissible **conversions** within that kind; not every scale requires it.

**R‑UN‑1 (Quantity kind).** Where units apply, the template **SHALL** indicate the **quantity kind** (e.g., Time, Length, Dimensionless‑Score). Units are meaningful only **within** one kind.

**R‑UN‑2 (Convertibility).** Comparisons across different units are valid **iff** they are **convertible** by kind-preserving transformation (ratio or interval scales); for ordinal or nominal scales, no numeric conversions exist.

**R‑UN‑3 (Canonical labels).** `%` denotes “fraction×100”; “points” denotes dimensionless magnitudes used for scores; “stars” denotes discrete ordinal marks. These are **labels** of representation, not new characteristics.

**R-UN-4 (Quantity-kind bridge).** A Template on an interval or ratio Scale **SHOULD** name the underlying **quantity kind** (e.g., ISO 80000/QUDT category) to enable safe external bridges. This does **not** import external vocabularies; it declares an alignment point.

##### C.16:5.3.4 - `U.EvidenceStub` — pointer to grounds (normative)

**Function.** A compact **tie** from a Measure to the grounds sufficient for **reasoned audit** (not a repository prescription).

**R‑EV‑1 (Minimal sufficiency).** An EvidenceStub **SHALL** carry, at minimum, a **type‑of‑ground** and an **identifier** sufficient to retrieve or reconstruct the grounds in the appropriate Context of meaning.

**R‑EV‑2 (Compositionality).** Multiple grounds may be **composed** as a finite set; composition is **commutative, associative, and idempotent** at the level of stubs, enabling conceptual merge of corroborations.

**R‑EV‑3 (Soundness axiom).** A Measure is **MM‑CHR‑admissible** only if at least one **auditable chain of grounds** can be stated from the bearer to the Characteristic via an appropriate description episteme that carries the measured subject, characteristic, and evidence relation. *(Note:* mechanism‑level admissibility gates (e.g., admission thresholds or evidence thresholds in CG‑frames or CHR mechanisms) are governed by their FPF patterns or specification records; C.16 defines only the conceptual “has grounds” link.)
**R‑EV‑3 (Soundness axiom).** A Measure is **MM‑CHR‑admissible** only if at least one **auditable chain of grounds** can be stated that connects:
`bearer (subject) -> grounds -> Characteristic -> Coordinate or Level on the declared Scale`,
in the appropriate Context of meaning. *(Informative: this is the measurement-claim binding chain.)*
*(Boundary note:* mechanism‑level admissibility gates (e.g., admission thresholds or evidence thresholds in CG‑frames or CHR mechanisms) are governed by their FPF patterns or specification records; C.16 defines only the conceptual “has grounds” link.)

#### C.16:5.4 - Polarity, Comparability, and ScoringMethods (normative)

> **Notation.** To avoid clashes with the kernel’s global aggregation symbol, this FPF pattern denotes a **ScoringMethod** (score‑level mapping) by **𝒢** (calligraphic 𝒢).

**R‑POL‑1 (Declared polarity).** Every ordered scale **SHALL** declare polarity at the **template**. Any disclosed scoring method **𝒢** that issues a **Score** for that template **SHALL** be order‑compatible with the declared polarity semantics (monotone for ↑/↓ polarity; target‑aware only when the target semantics is explicitly declared and cited where it depends on external conventions).

**R‑CMP‑1 (Direct comparability).** Two readings are **directly comparable** only when they reference the **same `U.DHCMethodRef`** (hence share Characteristic, Scale, and Unit semantics by reference to A.17 and A.18). “Same‑template” is the only comparability relation defined by C.16.
*(Clarification:* sharing a name, unit label, or scale type across distinct templates is **not** sufficient for comparability in MM‑CHR; cross‑template comparability must be established via **R‑CMP‑2**.)*

**R‑CMP‑2 (Transformed comparability is cited, not defined).** If a comparison relies on any transformation or supporting step (e.g., normalization, indicatorization, scoring, aggregation, cross‑context transport, bridge conversions, admission gates), that step **SHALL** be **named and cited** via its governing FPF pattern or specification record. C.16 does not define such transformations, their law sets, or their admissibility conditions.

**R‑G𝒢‑1 (ScoringMethod disclosure).** If a pattern issues a **Score** (a value on a score scale), its scoring method **𝒢 : Coordinate -> Score** **SHALL** be identified **by reference** to its governing method-description episteme or FPF pattern, and SHALL disclose:
(i) a **bounded codomain** and score range, and
(ii) an explicit **order‑compatibility statement** (e.g., monotonicity) consistent with the template’s declared polarity.
When reproducibility matters, the reference SHOULD be edition-pinned according to that episteme or pattern's authoring discipline.
C.16 does not define scoring methods; it only requires that a score be interpretable as a reading on a declared scale.

**R‑G𝒢‑2 (Ordinal respect).** For ordinal inputs, any cited scoring method must be **order‑preserving**; interval assumptions **MUST NOT** be smuggled in. *(Normative source for scale admissibility remains A.18; C.16 only enforces “no silent semantics upgrade”.)*

#### C.16:5.5 - Entity vs Relation bindings (normative clarifications)

**R‑ER‑1 (Arity preservation).** If the Characteristic is `U.EntityCharacteristic`, the subject is **one** bearer; if `U.RelationCharacteristic`, the subject is a **k‑tuple** (k ≥ 2). The Measure’s claim text **SHALL** reflect this arity.

**R‑ER‑2 (Relation scale).** Relation‑valued scales **SHALL** fix their symmetry/antisymmetry and directionality (e.g., distance symmetric; influence directional), at the **template** level.

**R‑ER‑3 (Bridge to CG‑frames).** In architectural CG‑frames, **Coupling/Cohesion** are Characteristics over **modules** (structure) or **roles** (function). Their measures are relational (**Coupling**) or unary (**Cohesion** within an element), but both live in the same MM‑CHR substrate.

#### C.16:5.6 - Acceptance (conceptual, role-state-relation aware)

> Acceptance here is **thought‑level**. It uses the `RoleStateRelation@BoundedContext` (A.2.5) pattern to organise mental checks—no “lifecycle” narratives.

**SCR‑C16‑A (Template sufficiency).** You can check—without invoking tooling—that the template has:
(i) a fixed **Characteristic** (A.17),
(ii) a typed **Scale form** (A.18), and
(iii) coherent **Unit** semantics where applicable (plus declared polarity for ordered scales).

**SCR‑C16‑B (Reading sufficiency).** For a given subject, you can check that the reading:
(i) cites the template,
(ii) states a value valid for the Scale (Coordinate/Level),
(iii) states a time stance,
(iv) names **𝒢** when a Score is issued, and
(v) provides EvidenceStub(s) where the template requires them.

**SCR‑C16‑C (Comparability).** When two readings are placed side‑by‑side, you can state in one breath whether they are **comparable as‑is** or only **after 𝒢**, and **why**.

**SCR‑C16‑D (Evidence adequacy).** For any required EvidenceStub, you can sketch at least one **auditable chain of grounds** from the subject to the Characteristic via a Description in the right Context.

#### C.16:5.7 Cross-references & source references

* **A.17 (CHR‑NORM).** Canonical **Characteristic** and Entity/Relation split; lexical rules and alias sunset.
* **A.18 (CSLC‑KERNEL).** One Characteristic + one Scale per template; Level optional; operation guard by scale type.
* **MM-CHR source examples.** Cross-domain alignment hints for Characteristics, Observations, and Quantities across ISO 80000, ISO/IEC 25024, QUDT, SOSA/SSN are used here only as conceptual witnesses.

