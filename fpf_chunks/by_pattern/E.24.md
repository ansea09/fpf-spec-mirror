---
chunk_kind: "parent"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/E.24.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
line_start: 69391
line_end: 69740
dependencies:
  - "A.15"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.29"
  - "C.3"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "E.21"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

## E.24 - U.Ontic and Ontic Introduction Discipline

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24:0 - Use This When

Use this pattern when FPF work appears to need a durable ontic: a connected ontology-architecture unit whose meaning is spread across several typed values, slots, relation positions, pattern nests, and nearby governing patterns.

Typical moments:

- a repeated local use frame starts behaving like a hidden object;
- a source label or project-side expression keeps pointing to several FPF values at once;
- a draft ToC locus names a calculus or object family, but no current pattern carries its governing meaning;
- a subject pattern begins to carry local slot-graph doctrine that other patterns also need;
- a proposed term would sit across one `semanticArea`, one `ontologicalNeighborhood`, and several dependent patterns.

**First useful move.** Decide whether the construct is a durable ontic, a direct use of existing governing patterns, a local use frame for one bounded application family, or a source label that must remain quote-only or reduced-use.

**What goes wrong if missed.** FPF grows shadow ontology. The same project concern becomes a method in one place, a mechanism in another, a record in a third, and a local checklist in a fourth. Later uses then fight symptoms instead of settling the underlying kind, slot, and governing-pattern question.

**What this buys.** A durable ontic gets an explicit slot graph like `U.EpistemeSlotGraph`, or the construct is explicitly kept as a local use frame with pointers to the typed values and governing patterns that already carry the work.

**Not this pattern when.**

- If one existing governing pattern already carries the claim, use that pattern directly.
- If the issue is only one wording-use repair row, use `E.10` and `E.10.ARCH`.
- If the issue is only a new or revised mechanism meaning, use `E.20`.
- If the issue is only durable naming, use `F.18`.
- If the issue is only a pattern publication-form or section-order matter, use `E.8`.

### E.24:1 - Problem Frame

Some FPF governed objects are small enough to define with one relation or one record. Others require a durable ontic. `U.Episteme` is the central example: it needs identity criteria, typed slots, slot-filling discipline, tuple/card/publication species, carrier separation, relation to `U.Signature`, and dependent episteme-morphism and publication patterns. `C.2.1` works because it makes the small ontic slot graph explicit.

The same failure recurs elsewhere. A project label such as "algorithm", "process", "model", "architecture", "service", "quality", "time", "rhythm", "change", or "source" can point to several typed FPF values. If FPF answers only by choosing a better word, the old compression returns. If FPF creates a new `U.*` kind too early, the new kind becomes a duplicate ontology over values that already have governing patterns.

E.24 governs that ontic-introduction decision.

### E.24:2 - Problem

Without this discipline:

1. **Local use frames become pseudo-kinds.** A repeated local table or record starts to look like a new FPF object even though its rows are only links to existing values.
2. **Draft-only loci become false authorities.** A ToC row such as `C.4 Method-CAL` is cited as if it already supplied current governing text.
3. **Pattern nests are mistaken for semantic units.** The placement label becomes the ontic, while `semanticArea` and `ontologicalNeighborhood` stay unstated.
4. **Slot graphs are copied without identity.** Several patterns list similar slots but no pattern says what identifies the ontic, which slots are required, and which dependent patterns may rely on them.
5. **Existing typed values are duplicated.** A new head repeats `U.Method`, `U.Mechanism`, `U.WorkPlan`, `U.Work`, evidence, gate, source, or result relations under a new name.

### E.24:3 - Forces

| Force | Tension |
| --- | --- |
| Ontic stability vs local use | A durable FPF ontic needs identity and slots; a local use frame only needs enough structure for one bounded application family. |
| Reuse vs overgrowth | Dependent patterns need a stable slot graph when they rely on one; premature `U.*` growth creates another ontology. |
| Semantic area vs pattern placement | `semanticArea` names the semantic unit; `ontologicalNeighborhood` names the applicability neighborhood; `pattern nest` is only placement. |
| Draft citeability vs current governance | Draft ToC rows can guide investigation, but current pattern text or an accepted DRR must carry governing meaning. |
| Naming vs ontology | F.18 can make a name better, but naming cannot decide the kind, slot graph, species, and dependent-pattern duties by itself. |

### E.24:4 - Solution

This pattern selects `U.Ontic` as the FPF kind for an ontic. `U.Ontic` is the `EntityOfConcern` of E.24: a connected ontology fragment whose stable identity, slots, admissible slot values, neighboring ontology units, dependent pattern obligations, and non-use boundary must be held together before FPF can use that fragment safely in action-facing patterns.

Start from the ontic, not from its description or publication. An ontic may then have:

- a description episteme that describes the ontic and its slot graph;
- a publication of that description episteme, often as a head pattern plus dependent patterns;
- publication forms, views, examples, and source rows that help users apply it.

Those are downstream of the EoC distinction. A pattern file, section, table, card, packet, review note, or publication form is not the ontic. It may describe or publish the ontic after the ontic has been selected as the object under concern.

A `U.Ontic` names the braid of:

- the `semanticArea` being settled: the meaning area that lets users recognize the family of claims or uses under concern;
- the `onticSlotGraph`: the small typed slot graph that gives the ontic its identity, required and optional slots, value kinds, reference kinds, relation set, species or record forms, non-slot components, and description/publication boundary;
- the `ontologicalNeighborhood`: the current FPF patterns that carry claims about the ontic, its slots, its values, its neighboring `EntityOfConcern` uses, and its admissible exits;
- the governing head pattern or accepted local frame that describes the ontic when current FPF use needs a citeable description;
- the dependent-pattern obligations that rely on that settlement without copying the whole slot graph.

FPF ontology is therefore not treated here as one flat class list. It is a connected set of ontics. That prevents ontology explosion: FPF can keep a small number of durable ontology units while allowing many project `EntityOfConcern` values, source labels, project handles, role assignments, records, methods, mechanisms, work plans, descriptions, publications, and other values to appear as slot fillers inside several ontics. A value filling a slot in one ontic does not thereby become a different entity, a different `U.*` kind, or a second ontology.

The `U.Ontic` decision is selected because the repeated `semanticArea`/`onticSlotGraph`/`ontologicalNeighborhood`/dependent-pattern braid is now itself a governed object in FPF. Without a named kind, the same architecture unit would be re-described as a semantic area, pattern nest, ontology family, local frame, slot graph, or description/publication arrangement in different places, recreating the duplicate-ontology problem E.24 is meant to prevent. With `U.Ontic`, DRRs and patterns can cite one kind for the ontology-architecture unit while still keeping each filled value under its own governing pattern.

The cost is kernel growth and metamodel risk. E.24 contains that cost by making `U.Ontic` narrow. A local use frame, source label, project-side expression, recurring table, pattern nest, or draft ToC row is not a `U.Ontic` merely because it looks ontology-shaped. It becomes a `U.Ontic` only when the E.24 decision names stable identity, an ontic slot graph, selected semantic area, selected ontological neighborhood, dependent pattern obligations, existing-pattern reuse, and non-use boundary by value.

Slot discipline is the governing protection. A slot-position label says which relation position or use-position is being filled. It does not create a new entity kind, and it also does not erase an already governed entity kind. A value can fill a slot in an ontic graph while remaining governed by its own pattern.

Use this distinction:

- If the name only identifies a position in the current graph, keep it as a `SlotKind`, relation label, or local field.
- If the name has independent `EntityOfConcern` identity, stable identity criteria, a governing pattern, admissible use boundaries, and dependent-pattern reliance, it may remain or become a `U.*` kind after an E.24 decision.
- If both are true, keep both levels explicit: the slot belongs to the ontic graph; the filler keeps its governing kind. A `methodSlot` can be filled by a `U.Method`; a `workOccurrenceSlot` can be filled by `U.Work`; an `EntityOfConcernSlot` can be filled by a `U.Entity`. The slot name does not make the filler a different entity, and the filler kind does not make the whole slot graph one super-kind.

Role and slot participation require unification, not a second ontology. `U.Role` and `U.RoleAssignment` remain governed by the role and alignment patterns because a holon can participate in a bounded context under a functional mask and enact work through that assignment. At the same time, `U.RoleAssignment` is a typed relation with holder, role, context, and window positions, so role participation is a holon-facing specialization of relation/slot discipline when the role-governing pattern is live. Do not generalize this into "every slot is a role" or "roles are merely labels"; say instead that role participation uses slot discipline while the filled holon, role, context, and window keep their own governing kinds.

When an existing `U.*` name appears to be only a slot-position label, run the same check explicitly. Retain the `U.*` name only if its pattern gives a standalone `EntityOfConcern`, identity criterion, and action-facing gain that cannot be reduced to "value filling this slot." Otherwise demote the use to a slot or relation label and do not keep the U-kind by inertia.


This differs from pure ontology engineering because FPF patterns are action-facing: they help an engineer-manager decide what can be done, claimed, relied on, repaired, compared, or stopped in a problem situation. Ontic settlement supplies the object discipline that makes those actions intelligible. It says which objects and relations the pattern acts with, while the subject pattern still carries the practical move, boundary, evidence, and consequence.

Precision restoration uses the same discipline without turning it into lexical style. First recover the ad hoc ontic implied by the source situation: which meaning area, candidate object of concern, slots, neighboring patterns, and typed values are being compressed by the wording or source-side situation. Then repair toward the normative FPF ontic and linked typed values when such an ontic exists. If no normative ontic exists, use the direct governing patterns, keep the frame local, or open an E.24 ontic-introduction decision.

E.24 is the governing description pattern for `U.Ontic`. In that sense it is the ontic-of-ontics pattern: it describes the `U.Ontic` EoC, its slot graph, and its decision discipline. That self-application is allowed only under the same checks it imposes on other ontics; it is not a license for every local ontology-shaped bundle to become a `U.*` kind.

E.24 is compatible with modular ontology and ontology-design-pattern practice: modular ontology libraries and ontology design patterns show why reusable small ontology structures matter, and recent process-modeling work shows that implicit process patterns must be made explicit for reuse. E.24 is narrower and more FPF-specific: it selects when FPF should introduce a durable action-facing ontic, rather than importing an external microtheory or treating every reusable repair table as ontology.

Introduce or rely on a durable FPF ontic only after the ontic-introduction decision satisfies four checks.

#### E.24:4.1 - Check 1: Existing Governing Pattern Check

Name the current claim under decision and ask whether an existing pattern already carries it.

Use direct governing patterns first. If the case is method semantics, use `A.3.1`; if it is method description, use `A.3.2`; if it is mechanism meaning, use `A.6.1` and `E.20`; if it is work planning or dated work, use `A.15.2` or `A.15.1`; if it is evidence, gate, source, assurance, decision, release, or publication use, use that governing pattern.

Do not introduce a durable ontic only because several patterns are near each other or because one source word appears often.

#### E.24:4.2 - Check 2: Stable Identity Test

A durable ontic must have stable identity beyond one repair pass.

Ask:

1. What is the primary `EntityOfConcern`?
2. What changes the identity of this ontic?
3. What does not change identity, even if the publication, carrier, notation, view, or local record changes?
4. Which bounded context is required for identity?
5. Which dependent patterns may rely on that identity?

If those questions cannot be answered, keep the construct as a local use frame or direct governing-pattern use.

#### E.24:4.3 - Check 3: Typed Slot-Graph Test

A durable ontic must publish a small typed slot graph.

The ontic-introduction decision states:

```text
OnticIntroductionDecision:
  ProposedOnticName:
  ProposedConceptHead:
  OnticAsEntityOfConcern:
  BoundedContext:
  StableIdentityCriterion:
  UKindDecision:
    verdict: selected U-kind, no U-kind, or blocked
    selectedUKindName:
    gain:
    cost:
    duplicateOntologyRisk:
    migrationObligation:
  SemanticAreaBaseConcept:
  SemanticArea:
  SemanticAreaSenseFamily:
  OnticSlotGraph:
    RequiredSlotKinds:
    OptionalSlotKinds:
    ValueKinds:
    RefKinds:
    RelationSet:
    SpeciesOrRecordForms:
    NonSlotComponents:
    DescriptionEpistemeBoundary:
    PublicationBoundary:
  OntologicalNeighborhood:
    HeadPattern:
    DependentPatterns:
    NeighboringGoverningPatterns:
    DirectUsePatternsBeforeNewConcept:
  ExistingGoverningPatternsReused:
  DependentPatternObligations:
  SlotPositionLabelsThatAreNotNewKinds:
  NonUseBoundary:
```

For E.24 itself, this record is already decided: `ProposedOnticName = Ontic`, `OnticAsEntityOfConcern = connected ontology fragment under FPF settlement`, and `UKindDecision.verdict = selected U-kind` with `selectedUKindName = U.Ontic`. Other proposed ontics must still fill the record by value; they do not inherit the `U.*` decision from E.24.

The slot graph must use `A.6.5` slot discipline and must not define a second slot discipline. A role-like, method-like, mechanism-like, source-like, publication-like, temporal, or architecture-like slot-position label is not a kind decision. It becomes a kind decision only when the governing pattern names that filled value by value and admits that kind.

#### E.24:4.4 - Check 4: Placement and Dependent-Pattern Obligation

Declare:

- `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`;
- selected `ontologicalNeighborhood`;
- pattern nest and why that placement follows the primary `EntityOfConcern`, relation, or claim;
- first subject pattern to write;
- dependent patterns that may rely on the slot graph;
- draft-only or missing loci that cannot yet govern current claims;
- names that pass `F.18`;
- evaluation pattern for the resulting host, usually `E.21` for a pattern and `E.9.DA` for the DRR.

If the decision selects a durable ontic, write the governing head pattern now or state the accepted stub with current named non-satisfied conformance rows. If no governing head pattern is written, do not cite the proposed ontic as governing current FPF use.

#### E.24:4.5 - Local Use Frame Decision

Use a local use frame when a recurring construct is useful for one bounded application family and its filled positions are already governed elsewhere.

A local use frame:

- names the concern, use, or relation being handled in that bounded application family;
- links separately governed typed values without turning the link into a new `U.*` kind;
- points each value to its governing pattern;
- blocks one overread or shadow-kind temptation;
- does not mint a `U.*` kind;
- does not become a project record, evidence record, gate record, method, mechanism, work plan, or work occurrence.

Precision restoration may use a local use frame in one of its slots, but the frame is not defined by repair. P2W, work planning, evidence use, gate use, architecture use, or publication use may use the same subject ontology in different slots for different practical purposes.

### E.24:5 - Archetypal Grounding

Use these slices as archetypes for the ontic-introduction decision. They are not a recommended progression. Each slice shows which object is being governed, which ontic or local use shape is selected, and which tempting overread is blocked.

#### E.24:5.1 - Episteme as Durable Ontic

`U.Episteme` passes E.24. It has stable identity, a normative `U.EpistemeSlotGraph`, required slots, optional slots, tuple/card/publication species, carrier separation, and dependent patterns in C.2, A.6.2-A.6.4, and E.17. `C.2.1` is therefore the right form: a subject pattern with a small typed ontic slot graph and dependent-pattern obligations.

#### E.24:5.2 - Method, Work, and Change as a Subject-Ontology Constellation

A project phrase such as "algorithm", "process", "solver", or "workflow" can point to one recognizable concern about changing, producing, selecting, deriving, controlling, maintaining, planning, performing, measuring, or carrying a result for an `EntityOfConcern`. That concern may involve `U.Method`, `U.MethodDescription`, `U.Mechanism`, formal-substrate declaration, mathematical-lens use, `U.WorkPlan`, dated `U.Work`, evidence relation, source relation, gate relation, result relation, publication relation, or temporal relation.

Do not decide this case by the fact that SEMIO-05 found it through wording restoration. Method, work, and change material is subject ontology first. It is already governed by the current FPF constellation around `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.15`, `A.15.1`, `A.15.2`, `E.18`, `E.18.1`, evidence, source, gate, result, publication, and temporal patterns. P2W uses that constellation to solve problem-side carry-through; work and planning patterns use it to coordinate intended and performed work; evidence and gate patterns use linked values for reliance; `E.10.ARCH` uses the same subject ontology only when wording-use precision restoration is the current use.

SEMIO-05 therefore does not introduce a durable `U.Ontic` named `MethodWorkChangeOnticGraph`. The reason is not that the material is "only recovery"; the reason is that the current subject ontology is already carried by named governing patterns, and SEMIO-05 has not selected one new stable identity, one head pattern, and one slot graph that would replace that constellation. The current settlement is to cite the governing-pattern constellation, keep each filled value under its own pattern, and use `E.24` again only when a campaign actually selects a new durable ontic by value and writes its governing head pattern.

Dependent subject patterns may keep a thin cue: when one recognizable project concern spans method, mechanism, formal substrate, mathematical lens, plan, work, evidence, source, gate, result, publication, or temporal relations, name the current relation being made and use that relation's governing pattern. They must not copy a full negative formula, must not call the constellation a recovery graph, and must not assign one typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits that dual typing. Slot-position labels do not create alternate ontology.

When FPF material shows that a slot filler currently named as `U.*` lacks standalone `EntityOfConcern` identity, stable identity criterion, or action-facing gain, apply E.24 again and demote that use to a SlotKind or relation label. When FPF needs a durable change, temporal, method-work, or process ontic, introduce it through its own E.24 decision and governing pattern before citing it as current FPF ontology.

#### E.24:5.3 - Method-CAL Draft Locus

`C.4 Method-CAL` may appear in a ToC row or older source wording. If no current pattern text carries it, it is not a governing pattern for current FPF use. Use `A.3.1`, `A.3.2`, `A.15`, `A.6.1`, `E.20`, `C.29`, and `E.18` as the current sources. A Method-CAL pattern can govern other patterns only after it has its own E.24-style ontic decision, stable identity, slot graph, and dependent-pattern declaration.

#### E.24:5.4 - System-Like Head Concepts

`system`, `episteme`, `architecture`, `method`, `mechanism`, `temporal claim`, `dynamics`, and `change` can each appear as a broad head for many dependent FPF patterns. That breadth is not itself enough to create a durable FPF ontic. Apply E.24 before treating a broad head as current governing ontology: name the primary `EntityOfConcern`, stable identity, `onticSlotGraph`, selected `semanticArea`, selected `ontologicalNeighborhood`, dependent patterns, and description/publication boundary. If those rows are missing, use the current governing patterns that already carry the claim and do not cite the broad head as if it supplied current slot discipline.

#### E.24:5.5 - Mature Comparator Discharge

`E.24` is mature only when its selected mature-pattern ingredients are present in the body, not only in a separate planning or evaluation note.

| Comparator | Selected mature ingredient | Current E.24 locus | Lowering condition |
| --- | --- | --- | --- |
| `C.2.1` | stable identity plus small typed slot graph for a durable ontic | `E.24:4.2`, `E.24:4.3`, `E.24:5.1` | Lower if E.24 asks for fields but no longer asks what preserves or changes identity. |
| `E.20` | introduction discipline for one governed subject family | `E.24:4.1`, `E.24:4.4`, `E.24:8` | Lower if mechanism-specific doctrine is copied here instead of left with `E.20`, `A.6.1`, and related patterns. |
| `E.8` | publication-form and section-order boundary | `E.24:0`, `E.24:4.4`, `E.24:6`, `E.24:8` | Lower if E.24 starts regulating pattern format instead of the ontic-introduction decision. |
| `E.10.ARCH` | wording-use restoration architecture that uses existing subject ontology before sending wording symptoms to the governing precision-restoration pattern | `E.24:4.1`, `E.24:4.5`, `E.24:5.2`, `E.24:7` | Lower if a local use frame is treated as a durable ontic or if a wording trigger alone creates a new ontology unit. |
| `F.18` | durable naming after ontology is settled | `E.24:4.4`, `E.24:6`, `E.24:7` | Lower if a new name substitutes for identity, slot, and dependent-pattern settlement. |

#### E.24:5.6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**.
Scope: the authoring decision for a durable ontic, direct governing-pattern use, or local use frame, not the subject matter governed by the resulting pattern.

This pattern intentionally biases toward explicit identity, typed slots, and governing-pattern reuse. It resists five recurring distortions:

- **shadow-kind bias:** repetition of a local use frame is mistaken for a new object;
- **placement bias:** a pattern nest or draft ToC row is mistaken for semanticArea or governing text;
- **name bias:** a cleaner term hides unresolved kinds, slots, and relations;
- **semio-bias:** discussion of descriptions, publications, or review evidence displaces the ontic or subject matter being introduced;
- **process-bias:** development-state, publication-state, evaluation-state, or process-proof status is copied into ontic or subject-matter content.

The mitigation is the same in each case: recover the primary `EntityOfConcern`, stable identity, typed slot graph, selected `semanticArea`, selected `ontologicalNeighborhood`, and governing-pattern reuse before naming, placement, dependent pattern reliance, or publication form becomes load-bearing.

#### E.24:5.7 - Rationale

FPF needs a pattern for ontic introduction because many important FPF ontology units are not one term, one field, one taxonomy branch, or one U-kind. They are small typed relation graphs with identity criteria, slots, admissible values, record or publication species, dependent patterns, and action-facing use boundaries.

The compactness gain is the central reason for `U.Ontic`. A taxonomy-heavy design tends to create a new type for each contextual position: reviewer, evidence reviewer, architecture reviewer, work reviewer, mechanism reviewer; method, mechanism, procedure, process, algorithm; record, evidence record, gate record, authority record. An ontic design instead keeps a small number of governed ontology units and lets many objects fill typed relation slots. A relation slot works like a parameter position in a relation-function: the value is typed and constrained by the slot, but it does not become a new kind merely because it fills that position.

`U.Episteme` is the proof case inside FPF. `C.2.1` does not define epistemes by a long taxonomy of descriptions. It defines stable identity and a small slot graph: EntityOfConcernSlot, claim graph, viewpoint, reference scheme, grounding, publication and carrier boundaries, and dependent episteme/publication patterns. The same small graph can hold many claim kinds, descriptions, views, publications, and project cases without minting a new episteme kind for each one.

Role/slot participation is the second proof case. `U.Role` remains useful because holons participate in contexts through role assignments and enactments. But a role assignment is also a typed relation with holder, role, context, and window positions. The compact design is not "roles are just slots" and not "every slot is a role"; it is that holon-facing role participation is governed through slot discipline when the role pattern is live. This prevents a separate ontology for every participation name while preserving the real action-facing gain of role patterns.

Without E.24, FPF ontology development oscillates between two bad moves. One move invents a new umbrella name and leaves the mixed ontology intact. The other refuses the new name but still leaves several patterns carrying duplicated local slot doctrine. E.24 gives a bounded authoring decision: use an existing governing pattern, introduce a durable ontic, keep a local use frame local, or keep the source label quote-only or reduced-use.

The pattern is deliberately about the introduction decision. It does not define every ontic and does not become a registry of system, episteme, method, mechanism, architecture, source, quality, temporal, dynamics, or change objects. Each accepted subject matter still needs its own governing pattern or accepted local frame.

#### E.24:5.8 - SoTA-Echoing and Currentness

E.24 does not claim to replace ontology engineering or OWL/UFO-style formal ontology. Its load-bearing basis is the current FPF need for action-facing ontology compactness, plus a narrow SoTA echo:

| Source family | Current lesson for E.24 | FPF decision |
| --- | --- | --- |
| W3C [SKOS Reference](https://www.w3.org/TR/skos-reference/), 2009, and W3C [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/), 2012. | SKOS is useful for controlled vocabularies, labels, broader/narrower relations, and concept schemes; OWL shows that ontology work also needs classes, properties, individuals, axioms, and declarative semantics. | Do not present FPF ontology as one taxonomy tree. Use taxonomy relations where they fit, but introduce an ontic only when stable identity and typed slot graph are required. |
| Modular ontology design patterns, MODL/MOMo, and commonsense ontology micropatterns, including [Shimizu and Hitzler 2024](https://arxiv.org/abs/2411.09601) and [Eells, Dave, Hitzler, and Shimizu 2024](https://arxiv.org/abs/2402.18715). | Current ontology-engineering work emphasizes reusable small ontology structures and pattern libraries, including LLM-assisted ontology engineering where modularity becomes more important, not less. | E.24 adapts the modular-pattern lesson: a durable ontic is a reusable FPF ontology unit with a governing head pattern and dependent-pattern obligations, not a local checklist copied across hosts. |
| [Qiang 2025/2026 ontology-interoperability ecosystem](https://arxiv.org/abs/2507.12311). | Overlapping and conflicting concepts block interoperability; current approaches combine design patterns, matching/versioning, and validation across the ontology lifecycle. | E.24 prevents shadow ontology and type explosion before matching/versioning becomes a rescue operation. It asks whether a proposed head is a durable ontic, existing governing-pattern use, local use frame, or non-use. |
| [Norouzi, Hertling, Waitelonis, and Sack 2025 process-representation ODP work](https://arxiv.org/abs/2509.23776). | Process/workflow ontologies often contain implicit design patterns; reuse suffers when those patterns are not explicit and accessible to domain experts. | E.24 supports the SEMIO-05 decision not to hide method/work/process material in one recovery graph. If a process or temporal ontic is needed, write its own slot graph and governing pattern. |
| [Almeida, Guizzardi, Sales, and Fonseca 2026 gUFO](https://arxiv.org/abs/2603.20948); UFO/OntoUML role, relator, situation, and high-order type practice. | Current foundational-ontology work uses type typology, reification of intrinsic and relational aspects, situations, and high-order types to avoid naive taxonomic flattening. | E.24 keeps role/slot, relation/signature/interface, episteme/publication, and mechanism/method/work distinctions as slot-governed ontology architecture rather than one taxonomic tree. |

This SoTA echo supports a bounded conclusion: ontic-based FPF ontology architecture gives compactness and structure compared with a taxonomy-only design when the governed subject depends on identity, relation slots, dependent patterns, and action-facing use. It does not make every modular ontology pattern an FPF ontic. External sources become load-bearing only when the DRR selects their payload for the specific ontic or subject matter under decision.

Use external sources when one ontic or subject matter itself depends on a source tradition. Put that source decision in the DRR and in the governing pattern for that subject matter. Do not make E.24 carry a borrowed external theory of every durable ontic.

#### E.24:5.9 - Currentness and Lowering Logic

Treat E.24 as current for ontic-introduction decisions only while the current FPF slot, precision-restoration, naming, and pattern-quality apparatus remain the governing basis. Reopen this pattern when one of these changes:

- a new accepted FPF pattern changes slot discipline, `EntityOfConcern` discipline, or durable-name discipline;
- a local use frame begins to be reused as if it were a durable ontic;
- a draft locus becomes a current pattern and changes the ontic-introduction decision;
- dependent patterns start copying a slot graph instead of relying on the governing head pattern;
- external source work becomes load-bearing for the introduction method itself rather than for one selected ontic or subject matter.

Lower the decision before use when E.24 cannot decide among durable ontic, local use frame, existing governing-pattern use, or quote-only/reduced-use source label. A failed decision is not repaired by adding more fields; it is repaired by returning to `E.24:4.1` and settling which object, slot graph, semantic area, ontological neighborhood, and governing patterns are actually live.

### E.24:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-E24-1` | The authoring decision names the primary `EntityOfConcern`, bounded context, and current claim before proposing a durable ontic. |
| `CC-E24-2` | Existing governing patterns are checked by value before a new ontic is selected. |
| `CC-E24-3` | A durable ontic publishes stable identity criteria and says what does and does not change identity. |
| `CC-E24-4` | A durable `onticSlotGraph` names SlotKinds, ValueKinds, RefKinds, relation set, species or record forms, non-slot components, and description/publication boundary. |
| `CC-E24-5` | The decision declares the selected `ontic` components by value: `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, `onticSlotGraph`, selected `ontologicalNeighborhood`, pattern nest, and dependent-pattern obligations, without treating any of them as synonyms. |
| `CC-E24-6` | Draft-only loci are marked non-governing until a current pattern or accepted stub carries named conformance gaps. |
| `CC-E24-7` | A local use frame is explicitly non-`U.*`, non-ontic, and points typed values to their governing patterns. |
| `CC-E24-8` | The selected name passes `F.18`; the name does not hide a second ontology or one umbrella for several kinds. |
| `CC-E24-9` | Pattern-quality and DRR-adequacy checks stay in `E.21` and `E.9.DA`; they are not copied as user-facing ontic or subject-matter content. |
| `CC-E24-10` | Dependent patterns state how they rely on the head ontic or local use frame without duplicating the whole slot graph. |
| `CC-E24-11` | Slot-position labels, including role-like labels, method-like labels, mechanism-like labels, temporal labels, source labels, and publication labels, do not create alternate ontology; the governing pattern names the filled value by value when a kind decision is live. |

### E.24:7 - Common Anti-Patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Shadow-kind by repetition | The same local record appears in several hosts and starts being cited as an object. | Apply E.24; either write a durable ontic pattern or rename it as a local use frame. |
| Draft locus as authority | A ToC row is cited as if it supplied current governing text. | Treat it as investigation cue only; use current governing patterns until the pattern exists. |
| Slot list without identity | A pattern lists fields but never says what identifies the ontic. | Add stable identity criteria or lower the construct to a local use frame. |
| Pattern nest as ontology | The numbering area is treated as the semantic unit. | Declare `semanticArea`, `ontologicalNeighborhood`, and primary `EntityOfConcern` separately. |
| New name as solution | The repair invents a smoother term while the typed values remain mixed. | Recover kinds, slots, semantic area, and ontological neighborhood first; name only after the ontology is settled. |
| Slot-position kind inflation | A role-like, method-like, temporal, source, or publication position receives a fresh kind name only because it occupies a slot. | Keep the value's kind under its governing pattern and record the slot position separately. |

### E.24:8 - Relations

- **Builds on:** `E.8`, `E.9`, `E.9.DA`, `E.10`, `E.10.ARCH`, `E.20`, `E.21`, `F.18`, `A.6.5`, and `C.2.1`.
- **Coordinates with:** governing patterns that describe durable ontics or their filled values, especially `C.2.1` for epistemes, `A.6.1` and `E.20` for mechanisms, `A.3.1` and `A.3.2` for method and method description, `A.15` for role-method-work alignment, and precision-restoration patterns such as `C.2.P`, `C.2.P.DR`, and `C.30.STRAT`.
- **Used by:** DRRs and pattern authors when repeated slot-graph-shaped material may become either a durable ontic or a local use frame.

### E.24:9 - Consequences

- FPF can introduce rich ontology units without letting every local use frame become a new ontology.
- Draft-only loci stop acting like current governing patterns.
- Dependent patterns get a stable slot graph when a durable ontic is selected.
- The cost is a short ontic-introduction decision before writing or relying on a durable ontic.

### E.24:End

# **Part F — The Unification Suite (U‑Suite): Concept‑Sets, SenseCells & Contextual Role Assignment**

