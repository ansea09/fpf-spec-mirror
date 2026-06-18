---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "U.Holon, U.System, and U.Episteme"
section_id: "A.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__007_archetypal-grounding.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.1 — U.Holon, U.System, and U.Episteme"
  - "A.1:5 — Archetypal Grounding"
line_start: 1478
line_end: 1519
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

### A.1:5 - Archetypal Grounding

#### A.1:5.1 - Water Pump as U.System

Pump #37 is a `U.System` holon in a maintenance bounded context.

```text
HolonSlotRelation:
  holonIdentity: Pump #37
  boundedContextRef: plant maintenance context
  boundaryRef: casing plus inlet and outlet flanges
  partRelationSet: motor, impeller, seals, housing
  containingWholeRef: cooling-water subsystem
  interactionSet: water flow, electrical energy, control signal
  subtypeKind: U.System
```

The pump can bear a maintenance role, enact a repair method, perform work through technicians and tools, and have selected structures such as transformation-flow, control, or module-interface structure.

#### A.1:5.2 - Scientific Theory as U.Episteme

Newtonian gravitation as taught in one edition is a `U.Episteme` holon in a physics-education bounded context.

```text
HolonSlotRelation:
  holonIdentity: Newtonian gravitation in the selected edition
  boundedContextRef: physics education context
  boundaryRef: selected axioms, vocabulary, reference scheme, and admissible claim set
  partRelationSet: definitions, laws, derivations, examples, evidence relations
  containingWholeRef: mechanics curriculum episteme
  interactionSet: citation, teaching, model-use, revision, publication
  subtypeKind: U.Episteme
```

The theory does not teach itself or revise itself. A teacher, author, student, reviewer, or software system in role may publish, explain, compare, or modify an episteme. The episteme carries claims and relations; the acting system performs the work.

#### A.1:5.3 - Team as Collection or Collective System

A list of named engineers is a collection. It becomes a `U.System` only when the project claims an acting whole: boundary, membership rule, coordination structure, role assignments, decision method, and work occurrences are current.

If the project says "the team approved the architecture", A.1 asks whether there is a collective system and whether a decision pattern or governance pattern makes that claim admissible. If not, name the specific system-in-role or decision relation that actually carries the claim.

