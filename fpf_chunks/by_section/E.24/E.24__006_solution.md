---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__006_solution.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:4 — Solution"
line_start: 69451
line_end: 69599
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

