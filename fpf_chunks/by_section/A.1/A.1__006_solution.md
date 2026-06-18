---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "U.Holon, U.System, and U.Episteme"
section_id: "A.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__006_solution.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.1 — U.Holon, U.System, and U.Episteme"
  - "A.1:4 — Solution"
line_start: 1384
line_end: 1477
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.22"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "C.30"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.PUB"
keywords:
---

### A.1:4 - Solution

Use the A.1 holon stack:

```text
U.Entity
  U.Holon
    U.System
    U.Episteme
```

This is not a publication hierarchy. It is the root ontology for cross-domain composition in FPF.

#### A.1:4.1 - U.Entity

`U.Entity` is anything that can be individuated and referenced under a bounded context. It carries no part-whole assumption by itself.

Use `U.Entity` when the current move only needs to point to a thing: a number, a claim, a named product, a material batch, a data value, a legal clause, a role value, a source reference, or another object under concern.

Do not apply holon aggregation, membership tests, or acting-system roles to a bare `U.Entity` unless the current pattern also models it as a `U.Holon` or a subtype of `U.Holon`.

#### A.1:4.2 - U.Holon

`U.Holon` is a `U.Entity` treated as a whole with parts and as a participant in larger wholes under a bounded context.

The A.1 holon slot relation is:

```text
HolonSlotRelation:
  holonIdentity:
  boundedContextRef:
  boundaryRef:
  partRelationSet:
  containingWholeRef?
  interactionSet?
  subtypeKind?: U.System | U.Episteme | other accepted subtype
  selectedStructureRef?
```

The boundary is current for the bounded context. A holon may have several possible boundary descriptions across contexts or viewpoints, but one current holon use must say which boundary governs the claim being made.

`partRelationSet` names the part-whole relations current for the use. Under open-world discipline, an omitted part list means "not recovered or not current for this claim", not "there are no parts."

#### A.1:4.3 - Boundary and Interaction

`U.Boundary` delimits the holon from its environment in the current bounded context.

`U.Interaction` names what crosses that boundary when such crossing is current: matter, energy, information, control signal, material flow, document transfer, claim update, or another governed crossing kind.

Do not call every boundary an interface. Use interface language only when a governing module, signature, mechanism, architecture, or boundary pattern makes interface meaning current.

#### A.1:4.4 - Holon Membership Test

When a candidate part is contested, use the holon membership test:

1. **Dependency:** removing the candidate breaks a core invariant of the holon.
2. **Internal interaction:** the candidate participates in interactions within the holon boundary that matter for the current claim.
3. **Emergence:** the candidate contributes to a collective property that justifies treating the whole as one holon.

Passing one or more tests can justify part membership for the current claim. Failing all three keeps the candidate outside the holon boundary for that claim.

#### A.1:4.5 - U.System

`U.System` is a holon that can act physically or operationally. It can bear roles, enact methods, perform work, participate in mechanisms, maintain state, transform other entities, and produce effects.

Use `U.System` when the current claim needs acting-system eligibility:

- role assignment to a system in a bounded context;
- method enactment or work occurrence;
- physical or operational boundary crossing;
- system architecture or selected structure;
- mechanism realization or transformer participation.

A collective system is not the same as a set. If a group of people, machines, services, or agents is expected to act, model the acting whole as a `U.System` with a boundary and role assignments. If no acting whole is claimed, keep it as a set or collection under the governing relation.

#### A.1:4.6 - U.Episteme

`U.Episteme` is a holon whose parts are claim-bearing and interpretation-bearing values: claims, definitions, reference schemes, viewpoints, evidence relations, argument structures, model content, or other episteme components governed by `C.2.1`.

`U.Episteme` is non-agentive. It does not decide, promise, authorize, perform work, or revise itself. A system in role may write, revise, publish, compare, transform, or use an episteme. The episteme remains the claim-bearing holon under the `C.2.1` slot relation.

An episteme can be an `EntityOfConcern`. This does not make it an acting system. It means the current description, evaluation, architecture claim, or transformation claim is about that episteme as the subject under concern.

#### A.1:4.7 - Cross-Level Use

The same project object can appear at different levels without changing kind by wording:

- a system can fill `GroundingHolonSlot` in an episteme description;
- an episteme can be the `EntityOfConcern` of another episteme;
- a system can publish or transform an episteme;
- a selected structure can be about a system, episteme, organization, document set, model, or research program when that object is treated as a holon.

Slot position does not create a new kind. A system filling a role-assignment holder slot remains a system. An episteme filling an EntityOfConcern slot remains an episteme. A holon whose structure is described does not become the description of that structure.

