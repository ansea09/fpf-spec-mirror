---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
section_id: "A.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__006_solution.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.1 — Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
  - "A.1:4 — Solution"
line_start: 1385
line_end: 1526
dependencies:
  - "A.1.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.22"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.20"
  - "C.30"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.UK"
keywords:
---

### A.1:4 - Solution

Use A.1 to decide whether the current object is only a referenceable entity, a holon, or a directly admitted holon kind.

```text
U.Entity
  U.Holon
    U.System
    U.Episteme
    U.Work             only under A.15.1
    U.BoundedContext   only under A.1.1
    U.Discipline       only under C.20
    named C.3 U.Kind   only when a direct governing pattern admits holon treatment
```

This is not a classical taxonomic ladder and not a publication hierarchy. It is a governed admission discipline for part-whole treatment in FPF.

#### A.1:4.1 - U.Entity

`U.Entity` is anything that can be individuated and referenced under a bounded context. It carries no part-whole, acting, claim-bearing, or architecture assumption by itself.

Use `U.Entity` when the current move only needs to point to something: a number, claim, named product, material batch, data value, legal clause, role value, source reference, document, or object under concern.

Do not apply holon aggregation, part-whole grounding, acting-system roles, or architecture claims to a bare `U.Entity` unless a current pattern also admits the entity as `U.Holon` or as a directly governed holon kind.

#### A.1:4.2 - U.Holon

`U.Holon` is the broad part-whole EntityOfConcern: a `U.Entity` considered as a whole with parts and as a possible part of larger wholes in a bounded context.

A holon claim is admissible only when the current text names the bounded context, the identity or recognition rule, the current part relation, and the governing pattern that admits the object under that part-whole treatment.

The A.1 holon slot relation is:

```text
HolonSlotRelation@Context:
  holonRef: U.Holon
  boundedContextRef: U.BoundedContext
  identityOrRecognitionRule:
  partRelationRefs:
  selectedStructureRefs?
  holonDelimitationRelationRefs?
  holonBoundaryCrossingRelationRefs?
  containingWholeRefs?
  admittedHolonKindRef?: U.System | U.Episteme | U.Work | U.BoundedContext | U.Discipline | named C.3 U.Kind admitted by a direct governing pattern
```

This relation is a selected SlotRelation expression, not a new U-kind and not a record that acts. Under open-world discipline, an omitted slot means "not current or not recovered for this claim", not "absent in the world".

#### A.1:4.3 - Admitted Holon Kinds

Current accepted holon-kind examples are:

- `U.System`, governed here as the acting physical or operational holon kind;
- `U.Episteme`, governed here only as a non-agentive claim-bearing holon, with full slot discipline in `C.2.1`;
- `U.Work`, governed by `A.15.1` as a dated 4D occurrence holon;
- `U.BoundedContext`, governed by `A.1.1` as a semantic-frame holon;
- `U.Discipline`, governed by `C.20` as a field-level practice-and-knowledge holon.

No blank "other kind" escape hatch is selected. If a source claims another holon kind, the current FPF use must name the concrete C.3 `U.Kind`, the part-whole relation, the direct governing pattern, and the slot discipline that makes holon treatment admissible before any part-whole, architecture, role, work, evidence, or source-use claim relies on it.

#### A.1:4.4 - U.System

`U.System` is an acting physical or operational holon kind. It can bear work-facing role assignments, capabilities, methods, mechanisms, work occurrences, transformation participation, and responsibility-bearing claims when the direct neighboring patterns make those claims current.

The A.1 system participation relation is:

```text
SystemParticipationRelation@Context:
  systemRef: U.System
  boundedContextRef: U.BoundedContext
  holonDelimitationRelationRef?
  roleAssignmentRefs?
  capabilityRefs?
  methodRefs?
  methodDescriptionRefs?
  mechanismRefs?
  workPlanRefs?
  workOccurrenceRefs?
  transformationParticipationRefs?
  functioningOrFunctionalElementRefs?
  evidenceRelationRefs?
  assuranceRelationRefs?
  temporalAspectRefs?
  dynamicsAspectRefs?
```

This relation links acting-system participation across role, capability, method, mechanism, work, transformation, functioning, evidence, assurance, temporal, and dynamics concerns. It does not collapse those concerns into one kind. Role assignment remains role discipline; method remains method discipline; performed work remains work discipline; transformation remains `U.Transformation`; functioning and functional element remain their direct owners.

#### A.1:4.5 - U.Episteme

`U.Episteme` is a claim-bearing, non-agentive holon kind. It can be changed, used, cited, published, represented, versioned, structured, compared, interpreted, or relied on by acting systems, but it does not act by itself.

Use `C.2.1` and the episteme family for episteme slot relation, claim graph, viewpoint, reference scheme, evidence relation, publication relation, source-use relation, and claim-bearing structure. A.1 only says that an episteme can be treated as a holon when part-whole treatment of the claim-bearing object is current.

Do not say that an episteme decides, approves, performs work, promises, revises itself, authorizes action, or bears responsibility. A system in role may do those things with or about an episteme.

#### A.1:4.6 - Holon Delimitation And Boundary Crossing

Do not create `U.Boundary` or `U.Interaction` from boundary or interaction wording.

Use `HolonDelimitationRelation@Context` when the current claim is about where the holon is delimited in a bounded context: identity rule, membership or part relation, environment relation, selected structure, or current boundary condition.

Use `HolonBoundaryCrossingRelation@Context` when the current claim is about a relation crossing that delimitation: transformation, signal, control, measurement, source use, publication use, evidence relation, probe relation, coupling, or another direct relation. If bounded change under conditions is current, use `A.3.4` for `U.Transformation`; the boundary-crossing relation may point to it but is not the transformation itself.

Do not call every boundary an interface. Use interface language only when a governing signature, module, architecture, port, or interface pattern makes interface meaning current.

External holon vocabularies do not admit FPF kinds by label. If a source says `AgentHolon`, `OrganisationHolon`, `DataHolon`, `ProcessHolon`, `Portal`, `Projection`, or a similar semantic-web holon class, recover the FPF claim before using it. Acting-agent and organization claims require `U.System` admission; data, document, and projected-content claims usually require `U.Episteme`, publication, source, evidence, or description owners; process-holon wording requires work, method, work-plan, or transformation owners; portal or traversal wording requires an access, boundary-crossing, policy, or evidence relation. A.1 admits only the holon or system claim when that claim is current.

Do not call a Markov blanket a holon boundary, interface, interface module, physical component, statistical separator, or agency proof until the current claim is recovered. If source wording says `Markov blanket`, first decide whether it names accepted local Markov dynamics, a mathematical or probabilistic lens, a holon delimitation or boundary-crossing relation, a physical interface module or component, a functional element, a boundary description or publication, or an agency-threshold claim. Apply the direct governing pattern. A.1 admits only the holon and delimitation claim when those are current.

#### A.1:4.7 - Collections, Collection-As-Whole, And Acting Collectives

A list, set, batch, fleet, pool, clientele, community, supplier base, or coverage zone does not become a `U.System` by wording.

First recover whether the source claims:

- membership only, governed by A.14 relation vocabulary;
- collection-as-whole constructive grounding, governed by C.13 and B.3.5 where assurance grounding is current;
- whole-level characteristic, governed by C.16;
- acting collective system, governed by `U.System` admission plus A.15 and role, method, and work owners;
- whole reidentification, governed by B.2.

An acting collective `U.System` needs boundary, coordination, role assignments, capability or method evidence, and work-facing participation. If those are not current, keep the object as a collection or collection-as-whole claim under direct owners.

#### A.1:4.8 - Constructional Grounding

A.1 names holon admission. It does not replace part-whole grounding.

Use:

- A.14 for relation vocabulary such as component, portion, aspect, phase, member, and part-whole relation;
- C.13 for constructive grounding such as `Gamma_m.sum`, `Gamma_m.set`, or slice treatment when the constructional grounding question is current;
- B.3.5 for Working-Model assurance grounding when the part-whole claim is used for assurance or evidence.

FPF avoids unrestricted composition. A set of nearby objects, a graph, a diagram, a role bundle, a method algebra, or a source table does not become a holon merely because it can be described as a whole.

#### A.1:4.9 - Slot Position Does Not Create A Kind

A system in a role-assignment holder slot remains a system. An episteme in an EntityOfConcern slot remains an episteme. A holon whose structure is described does not become the description of that structure. A system changing another holon may fill transformation participation slots without becoming that holon's super-holon. A publication, dashboard, model, or digital twin may describe a holon without becoming that holon.

Use the direct governing pattern for the current slot relation before creating a durable name.

