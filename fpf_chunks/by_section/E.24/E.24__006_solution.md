---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__006_solution.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:4 — Solution"
line_start: 78328
line_end: 78564
dependencies:
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "A.6.5"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.27.TA"
  - "C.29"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.14"
  - "E.18"
  - "E.2.DA"
  - "E.20"
  - "E.21"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.24:4 - Solution

This pattern selects `U.Ontic` as the FPF kind for an ontic. `U.Ontic` is the `EntityOfConcern` of E.24: a connected ontology fragment whose stable identity, slots, admissible slot values, neighboring ontology units, dependent pattern obligations, and non-use boundary must be held together before FPF can use that fragment safely in action-facing patterns.

Keep three objects distinct:

- the `U.Ontic` being introduced or rejected;
- the `OnticIntroductionCandidate`, which is a pattern-set architecture problem: duplicated slots, hidden slot boundaries, hidden relation boundaries, weak identity, scattered invariants, high coupling, low cohesion, or dependent patterns copying the same local ontology;
- the publication that describes the selected ontic, usually one head pattern plus dependent patterns.

The introduction decision is not the publication form. A pattern section, table, source row, or relation list may describe the ontic after the decision, but it is not evidence by itself that the pattern set needs a durable ontic.

Start from the ontic, not from its description or publication. An ontic may then have:

- a description episteme that describes the ontic and its slot relation;
- a publication of that description episteme, often as a head pattern plus dependent patterns;
- publication forms, views, examples, and source rows that help users apply it.

Those are downstream of the EoC distinction. A pattern file, section, table, card, packet, review note, or publication form is not the ontic. It may describe or publish the ontic after the ontic has been selected as the object under concern.

A `U.Ontic` names the connected set of:

- the `semanticArea` being settled: the meaning area that lets users recognize the family of claims or uses under concern;
- the `onticSlotRelation`: the small typed slot relation that gives the ontic its identity, required and optional slots, value kinds, reference kinds, relation set, species or record forms, non-slot components, description boundary, and publication boundary;
- the `ontologicalNeighborhood`: the current FPF patterns that carry claims about the ontic, its slots, its values, its neighboring `EntityOfConcern` uses, and its admissible neighboring uses and boundaries;
- the governing head pattern or accepted local frame that describes the ontic when current FPF use needs a citeable description;
- the dependent-pattern obligations that rely on that settlement without copying the whole slot relation.

FPF ontology is therefore not treated here as one flat class list. It is a connected set of ontics. That prevents ontology explosion: FPF can keep a small number of durable ontology units while allowing many project `EntityOfConcern` values, source labels, project-side identifiers, role assignments, records, methods, mechanisms, work plans, descriptions, publications, and other values to appear as slot fillers inside several ontics. A value filling a slot in one ontic does not thereby become a different entity, a different `U.*` kind, or a second ontology.

The `U.Ontic` decision is selected because the repeated semantic-area, ontic-slot-relation, ontological-neighborhood, and dependent-pattern set is now itself a governed object in FPF. Without a named kind, the same architecture unit would be re-described as a semantic area, pattern nest, ontology family, local frame, slot relation, or description and publication arrangement in different places, recreating the duplicate-ontology problem E.24 is meant to prevent. With `U.Ontic`, DRRs and patterns can cite one kind for the ontology-architecture unit while still keeping each filled value under its own governing pattern.

The cost is kernel growth and metamodel risk. E.24 contains that cost by making `U.Ontic` narrow. A local use frame, source label, project-side expression, recurring table, pattern nest, or draft ToC row is not a `U.Ontic` merely because it looks ontology-shaped. It becomes a `U.Ontic` only when the E.24 decision names stable identity, an ontic slot relation, selected semantic area, selected ontological neighborhood, dependent pattern obligations, existing-pattern reuse, and non-use boundary by value.

U-kind admission is a neighboring E.24-family question, not the main body of E.24. E.24 keeps the minimal invariant:

- a durable ontic is a connected action-facing ontology unit;
- durable `U.*` kindhood requires an E.24-compatible settlement;
- ontic settlement and U-kind count are not one-to-one;
- ontic, ontic-description episteme, publication, and publication form stay distinct.

Use `E.24.UK` when a `U.*` spelling, type or kind wording, title, filename, heading, ToC row, or structural name must be retained, governed by `C.3` typed reasoning, kept as a dependent durable value, or renamed to the actual governed object. `E.24.UK` owns the detailed U-kind admission law, root and dependent U-kind governance, relation to `C.3` typed reasoning, and structural `U.*` handling. E.24 only records the result when the ontic-introduction decision needs to say whether a candidate name is retained as a root U-kind, retained as a dependent durable value, governed by `C.3` typed reasoning, or treated as a non-U object governed elsewhere.

#### E.24:4.0 - Constructive Foundation And Math-Lens Boundary

If a reader asks where FPF ontics get constructive grounding, start here and then follow the chain named by the current claim. E.24 supplies the ontic and slot-relation decision: the ontic is the `EntityOfConcern`, its `onticSlotRelation` is the ontology unit being settled, and the description and publication stay downstream.

For structural identity claims, the constructive chain is `E.14 -> B.3.5 -> C.13`: Working-Model relation first, declared `validationMode`, `tv:groundedBy`, and a reconstructible `Γ_m.sum`, `Γ_m.set`, or `Γ_m.slice` trace. That trace is a mathematical or constructive lens for grounding the claim; it does not become the public relation vocabulary and it is not required for non-structural ontics.

For non-structural ontics, use the governing identity, grounding, or recognition rule named by the direct pattern: for example episteme slot relation, work occurrence identity, `C.3` typed reasoning, `A.6` declaration shape, Concept-Set witnesses, formal-substrate or principle-frame declaration, or another accepted identity test. Use `C.29` when the mathematical lens itself is current; use `E.24.UK` when a `U.*` name is being admitted; use `E.24.PUB` when the question is description or publication.

`A.14`, `B.2`, and `A.15.1` carry BORO- and CCO-compatible identity and occurrence discipline. They support the constructive foundation; they do not create a separate durable-kind ontology.

Keep ontic levels separate before dependent patterns rely on the ontic.

An ontic is selected when FPF needs one governed `SlotRelation`: a typed n-ary relation with `SlotSpec` discipline that keeps several different typed objects together without fusing them into one umbrella kind. The ontic is the relation architecture: it says which SlotKinds exist, what ValueKinds and RefKinds can fill them, which governing pattern owns each filler, and what claims become admissible or blocked when a filler changes. A filled use is a value assignment over that relation. Under `C.29`, that filled assignment may be viewed as a tuple for tuple reasoning, or drawn as a graph or hypergraph for dependency reasoning, but tuple, graph, and hypergraph are mathematical-lens views, not alternate ontology heads.

Use the lens that preserves the current question. A tuple view is useful when the question is "which slots and values are present in this assignment?" A graph or hypergraph view is useful when the question is "which values depend on, constrain, or reopen which other values?" Neither view establishes that the filled values form one new kind; both must return to the same `SlotRelation`, SlotSpecs, and governing patterns for fillers.

When several partial ontologies already exist for the same project concern, E.24 does not pick one and delete the others. It selects the head ontic or local frame that can relate them without fusing their kinds: the existing objects become slot fillers, relation positions, graph-valued expressions, descriptions, publications, or neighboring governed values. This prevents duplicate ontology: a `U.Method`, `U.Work`, `U.Mechanism`, a source-local graph-position claim or current `TransformationFlowStructure` expression, role assignment, and publication can participate in one typed relation without becoming the same kind.

1. **Ontic root and identity.** Name the durable ontic or accepted local frame under concern and its stable identity criterion.
2. **Type-level `onticSlotRelation`.** State the SlotKinds, ValueKinds, RefKinds, relation set, required slots, optional-in-use slots, participation slots and check slots, species or record forms when needed, non-slot components, description boundary, and publication boundary. This is the reusable schema, not one filled use.
3. **Filled value assignment or ordinary-use core.** Give a compact filled instance or first-use frame only when users need one concrete application shape. It fills the type-level slots; it is not a second ontology and not a competing slot relation. Under `C.29`, that filled assignment may be viewed as a tuple when tuple reasoning is current.
4. **Description episteme and publication.** Claims about the ontic, its slots, its slot fillers, or relations among those values use `C.2.1`; a pattern section, table, diagram, publication, card, or view may describe the ontic, but it is not the ontic.
5. **Participation slots, check slots, and relation references.** Method, mechanism, work, evidence, source, gate, result, temporal adequacy, math lens, publication, and other typed values may be fixed slot positions in an ontic when claims about the ontic change admissible use, evidence relation, identity, responsibility, enactment, observation, modeling, permission, acceptance, refresh, or dependent-pattern obligations when those fillers change. They are not identity slots unless the ontic identity criterion explicitly depends on them.

Use these criteria when deciding whether a possible slot belongs to the ontic slot relation:

1. **Claim-impact.** A claim about the ontic becomes stronger, weaker, blocked, differently evidenced, or differently usable when the slot filler changes.
2. **Stable participation relation.** The filler specifies, constrains, enables, enacts, observes, models, times, evidences, publishes, authorizes, accepts, refreshes, or otherwise participates in the ontic through a stable relation.
3. **Duplicate-ontology resistance.** Leaving the slot outside would make dependent patterns copy negative catalogues, local tables, or shadow kinds.
4. **Kind preservation.** Including the slot lets the filler keep its governing pattern instead of fusing several kinds into one umbrella value.
5. **First-use cost.** Including the slot gives a bounded disposition check; it does not force a full neighboring-pattern application unless the current claim depends on that value.

The `?` marker or optional-in-use status does not mean "weakly belongs to the ontic." It means that every use considers the slot and records a disposition, while only some uses recover or assert a filler. Under open-world discipline, an unfilled slot means unknown, not recovered, not asserted, or not current for this claim; it does not assert that no such value exists.

Not every ontic needs every named layer. Add a named signature or kind level only when dependent patterns must rely on slot constraints across species or morphisms. Add a named filled-value assignment only when patterns need a publication-form-agnostic filled value; use C.29 tuple-view language only when tuple reasoning is current. Add named card, view, or publication species only when holonic working forms, views, or publication forms are themselves governed by the ontic. Name attached or non-slot components only when common adjacent structures must stay recoverable while remaining outside the ontic identity.

Keep annotation proportional. E.24 requires source-ontology recovery only for wording that can change the ontic, slot, filled value, governing pattern, admissible use, or dependent-pattern obligation. If a domain sentence already preserves those values, do not replace it with a typed paraphrase merely to show that an ontic exists.

This differs from pure ontology engineering because FPF patterns are action-facing: they help an engineer-manager decide what can be done, claimed, relied on, repaired, compared, or stopped in a problem situation. Ontic settlement supplies the object discipline that makes those actions intelligible. It says which objects and relations the pattern acts with, while the subject pattern still carries the practical move, boundary, evidence, and consequence.

Precision restoration uses the same discipline without turning it into lexical style. First recover the ad hoc ontic implied by the source situation: which meaning area, candidate object of concern, slots, neighboring patterns, and typed values are being compressed by the wording or source-side situation. Then repair toward the normative FPF ontic and linked typed values when such an ontic exists. If no normative ontic exists, use the direct governing patterns, keep the frame local, or open an E.24 ontic-introduction decision.

E.24 is the governing description pattern for `U.Ontic`. In that sense it is the ontic-of-ontics pattern: it describes the `U.Ontic` EoC, its slot relation, and its decision discipline. That self-application is allowed only under the same checks it imposes on other ontics; it is not a license for every local ontology-shaped bundle to become a `U.*` kind.

E.24 is compatible with modular ontology and ontology-design-pattern practice: modular ontology libraries and ontology design patterns show why reusable small ontology structures matter, and recent process-modeling work shows that implicit process patterns must be made explicit for reuse. E.24 is narrower and more FPF-specific: it selects when FPF should introduce a durable action-facing ontic, rather than importing an external microtheory or treating every reusable repair table as ontology.

If the choice between "write an ontic" and "keep the existing pattern constellation" needs reusable scoring, build a separate evaluation `CharacteristicSpace` through `A.19.ECS`. The evaluated object is then the FPF pattern-set architecture alternative, not the ontic itself: current constellation, local frame, or durable ontic. Candidate architecture characteristics include cross-pattern coupling, subject cohesion, explicit `onticSlotRelation` and `SlotSpec` discipline, invariant recoverability, duplicate-ontology resistance, dependent-pattern thinness, change-impact locality, first-use cost, and FPF ecology fit. E.24 uses these as diagnostic pressure for the introduction decision; it does not itself become the full architecture-characteristic evaluation pattern.

Within this split, E.24 contains the object split and the ontic-introduction decision needed before dependent patterns rely on a durable ontic. Publication-section rules, adequacy scales, wording-use restoration rules, and general pattern-set architecture evaluation are handled by the neighboring patterns named above.

Use the current split this way:

- use `E.24` for `U.Ontic` identity, type-level `onticSlotRelation`, semantic area, ontological neighborhood, dependent-pattern obligations, and non-use boundary;
- use `E.24.CD` when the current problem is detection of an ontic candidate, hidden-form classification, or sufficiency rationale for deciding whether a recurring construct is a durable ontic, a local use frame, direct governing-pattern use, or source wording only;
- use `E.24.PUB` when the current problem is the distinction among the ontic, the ontic-description episteme, the publication of that description, and publication forms such as cards, records, tables, schemas, diagrams, views, or source packets;
- use `A.19.ECS` only when the contested question is how to construct an evaluation `CharacteristicSpace` for comparing pattern-set architecture alternatives, such as current constellation, local frame, or durable ontic.

This split keeps E.24 ontic-first. Candidate detection, publication discipline, and contested evaluation remain neighboring governed objects rather than sections that make E.24 a general discovery, documentation, or scoring pattern.


Introduce or rely on a durable FPF ontic only after the ontic-introduction decision satisfies four checks.

#### E.24:4.1 - Check 1: Existing Governing Pattern Check

Name the current claim under decision and ask whether an existing pattern already carries it.

Use direct governing patterns first. If the case is method semantics, use `A.3.1`; if it is method description, use `A.3.2`; if it is mechanism meaning, use `A.6.1` and `E.20`; if it is work planning or dated work, use `A.15.2` or `A.15.1`; if it is evidence, gate, source, assurance, decision, release, or publication use, use that governing pattern.

Do not introduce a durable ontic only because several patterns are near each other or because one source word appears often.

#### E.24:4.2 - Check 2: Stable Identity Test

A durable ontic must have stable identity beyond one local wording issue, source expression, or first-use frame.

Ask:

1. What is the primary `EntityOfConcern`?
2. What changes the identity of this ontic?
3. What does not change identity, even if the publication form, notation, view, or local record changes?
4. Which bounded context is required for identity?
5. Which dependent patterns may rely on that identity?

If those questions cannot be answered, keep the construct as a local use frame or direct governing-pattern use.

#### E.24:4.3 - Check 3: Typed Slot Relation Test

A durable ontic must publish a small typed slot relation.

The ontic-introduction decision states:

One-screen first-use card:

```text
OnticIntroductionDecisionCard:
  concern: a recurring FPF subject looks spread across several typed values or patterns.
  decision: durable ontic | local use frame | direct governing-pattern use | source label only.
  onticRootIfSelected: the EntityOfConcern and stable identity criterion.
  typeLevelSlotRelation: required slots, optional-in-use slots, ValueKinds, RefKinds, and governing patterns for fillers.
  filledAssignmentExample: one concrete assignment over the slot relation, not a second ontology.
  publicationBoundary: pattern text, table, card, or diagram may describe the ontic; it is not the ontic.
  blockedLocalOverread: one tempting shadow kind, duplicate ontology, or publication-as-object error.
```

Before opening the heavier record, run two cheap guards. First, a slot-position label is not a filler kind: name the SlotKind, ValueKind, RefKind, and direct governing pattern separately under A.6.5. Second, role participation is not automatic `U.Role` admission: use A.2, A.2.1, and A.15 only when a work-facing role value or role-assignment claim is current; otherwise keep the value as a slot filler or neighboring relation governed by its own pattern.

Filled replay slice:

```text
OnticIntroductionDecisionCard:
  concern: bounded change talk compresses method, work, mechanism, timing, evidence, result, and flow-structure claims.
  decision: durable ontic selected.
  onticRootIfSelected: `U.Transformation`, identified by transformed entity or structure, bounded context, pre-state and post-state or delta, transformation relation, and boundary condition.
  typeLevelSlotRelation: `TransformationCore` plus linked participation slots for method, method description, mechanism, work plan, work occurrence, evidence relation, result relation, temporal aspect, and flow-structure relation; fillers keep their own governing patterns.
  filledAssignmentExample: pump-station backup architecture change, with `A.3.4` transformation core, `A.15` method and work chain, `C.27.TA` two-release-cycle recovery timing, and evidence references plus result references only where those claims are being made.
  publicationBoundary: `A.3.4` describes the ontic and its slot relation; a table, card, diagram, or transformation-flow view may publish that description but is not the transformation.
  blockedLocalOverread: one "transformation" label does not make method, mechanism, work plan, performed work, evidence, and result the same typed value.
```

The full replay form is heavier:

For ordinary first use, stop at the one-screen card unless dependent patterns will rely on the proposed ontic, the current claim changes admissible use, or a reviewer needs replayable evidence for why a local frame was not enough.

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
    settlementObligation:
  SemanticAreaBaseConcept:
  SemanticArea:
  SemanticAreaSenseFamily:
  OnticSlotRelation:
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

The slot relation must use `A.6.5` slot discipline and must not define a second slot discipline. A role-like, method-like, mechanism-like, source-like, publication-like, temporal, or architecture-like slot-position label is not a kind decision. It becomes a kind decision only when the governing pattern names that filled value by value and admits that kind.

#### E.24:4.4 - Check 4: Placement and Dependent-Pattern Obligation

Declare:

- `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`;
- selected `ontologicalNeighborhood`;
- pattern nest and why that placement follows the primary `EntityOfConcern`, relation, or claim;
- first subject pattern to write;
- dependent patterns that may rely on the slot relation;
- draft-only or missing loci that cannot yet govern current claims;
- names that pass `F.18`;
- evaluation pattern for the resulting pattern or DRR, usually `E.21` for a pattern and `E.9.DA` for the DRR.

If the decision selects a durable ontic, write the governing head pattern before dependent patterns rely on it. If only a bounded local frame exists, name it as non-governing and state the claims it carries and does not carry by value. If no governing head pattern is written, do not cite the proposed ontic as governing current FPF use.

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

