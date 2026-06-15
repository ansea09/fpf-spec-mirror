---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext Semantic Frame"
section_id: "A.1.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__006_solution.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.1.1 — U.BoundedContext Semantic Frame"
  - "A.1.1:4 — Solution"
line_start: 1659
line_end: 1757
dependencies:
  - "A.1"
  - "A.15"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.24"
  - "E.24.PUB"
  - "F.0.1"
  - "F.18"
  - "F.9"
  - "U.Holon"
keywords:
---

### A.1.1:4 - Solution

Model `U.BoundedContext` as a semantic-frame holon.

```text
BoundedContextSlotRelation:
  contextIdentity:
  contextBoundary:
  localVocabulary:
  localInvariantSet:
  localRoleTaxonomy:
  bridgeRelationSet?:
  stewardingSystemOrCommunityRef?:
  editionOrWindowRef?:
```

The context is the `EntityOfConcern` when the claim is about semantic locality itself. It may also fill `BoundedContextRef` in role assignments, episteme descriptions, characteristic spaces, architecture descriptions, and other patterns.

#### A.1.1:4.1 - Context Identity

`contextIdentity` names the semantic frame, not a territory, department, document, storage place, team, or domain family.

Good context names are specific enough to decide meaning:

- `Hospital.OR_2025`
- `BPMN_2_0`
- `Theory.SpecialRelativity.SelectedEdition`
- `FactoryLineB.MaintenanceRules.2026`
- `FPF.PatternQuality.E21`

Broad labels such as "healthcare", "physics", "software", "workflow", or "architecture" are informative domain families unless they are narrowed into a bounded context with local vocabulary, invariants, role taxonomy, and bridge relations.

#### A.1.1:4.2 - Context Boundary

`contextBoundary` says where local meaning holds. It can be bounded by edition, standard, organization, product line, theory, practice, regulation, contract, operating mode, or another governed boundary.

The boundary is not a document boundary by default. A document may publish a context description. The context is the semantic frame that the document describes.

#### A.1.1:4.3 - Local Vocabulary

`localVocabulary` gives local senses for terms. It does not create global meanings.

When a word crosses contexts, do not infer sameness from spelling. Use a bridge relation with direction, relation kind, fit, loss, and scope.

Example: `ticket` in an airline context may denote a travel authorization; `ticket` in an IT service context may denote a work item. Those are different local meanings unless a bridge relation is declared for a specific use.

#### A.1.1:4.4 - Local Invariant Set

`localInvariantSet` names rules that hold inside the context.

Examples:

- in a hospital operating-room context, one person cannot fill surgeon and independent auditor roles for the same case;
- in a workflow-standard context, one work item cannot move from `InProgress` to `Done` without an accepted review transition;
- in a theory context, selected postulates constrain admissible derivations.

An invariant does not become global because it is well written. Cross-context reuse requires a bridge relation or a new local declaration.

#### A.1.1:4.5 - Local Role Taxonomy

`localRoleTaxonomy` defines roles valid in the context. A role assignment uses one context:

```text
RoleAssignment:
  holderRef:
  roleRef:
  boundedContextRef:
  windowRef?:
```

The same holder may have different role assignments in different contexts. The same role name may denote different roles in different contexts. A "global role" is not a valid shortcut; it is either a role value defined in a selected context or a wording problem to repair.

#### A.1.1:4.6 - Bridge Relation Set

`bridgeRelationSet` records cross-context relations. A bridge is not a hidden merge. It states how a meaning, role, rule, unit, status, or claim in one context relates to one in another context.

A bridge relation should state:

```text
BridgeRelation:
  sourceContextRef:
  targetContextRef:
  sourceValueRef:
  targetValueRef:
  relationKind:
  direction:
  fit:
  loss:
  scope:
```

If a bridge cannot be stated, the cross-context use remains unsupported for that claim.

#### A.1.1:4.7 - Non-Enclosing Boundary

Do not use bounded context as an enclosing object for everything nearby. A bounded context localizes meaning; it does not automatically contain every system, document, team, work plan, source, or architecture that mentions its vocabulary.

Objects can be governed by, described under, interpreted inside, or bridged across a context without being parts of the context holon. Use the relevant slot relation for each claim.

