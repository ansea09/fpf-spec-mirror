---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__006_solution.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:4 — Solution"
line_start: 1985
line_end: 2118
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:4 - Solution

Use `U.Role` as a context-bound role value, not as a generic contextual classifier.

`U.Role` answers the question: **what is this acting system or acting holon being, in this bounded context, for the current work-facing claim?**

It does not answer by itself:

- who holds the role;
- whether the holder can do the work;
- which method is selected;
- which work was planned or performed;
- which evidence justifies a claim;
- which publication or description expresses the role;
- which status applies to a document, method, result, or claim;
- which relation argument position or SlotKind is current.

Those claims belong to neighboring patterns.

#### A.2:4.1 - Core Definitions

**`U.Role`.** A `U.Role` is a context-bound role value: a reusable value that names what an acting system or acting holon is being in a bounded context. It is work-facing because its primary practical use is to govern or explain role assignment, method requirements, work attribution, role-state checks, role naming, and role-related evidence about work.

Plain gloss: a role is a contextual functional mask. The gloss is helpful only if the normative object stays clear: the role value is not the holder and not the work.

**`U.RoleAssignment`.** A `U.RoleAssignment` is a typed assignment relation value governed by `A.2.1`. It links a holder, a `U.Role`, a bounded context, and any current assignment window. A.2 names why this relation is needed; A.2.1 governs its SlotSpecs.

**Role holder.** A holder of a `U.RoleAssignment` is a `U.System` or acting holon admitted by the governing work or method pattern as a system-like performer for the bounded context. An episteme is not admitted as holder merely because it is used as evidence, source, standard, requirement, definition, explanation, status bearer, publication, or assurance input.

**Role description.** A role description is an episteme that describes, constrains, teaches, publishes, or stores a role value or role assignment. The description is not the role value by default.

**Role relation-neighborhood.** A role value is surrounded by relations that are not parts of the role:

| Relation family | Governing pattern | What it preserves |
| --- | --- | --- |
| Role identity and role description | `A.2`, Part F role-description and naming patterns | The role value and the descriptions that make it recognizable. |
| Role assignment | `A.2.1`, `A.6.5` | Holder, role value, bounded context, window, and assignment-specific work-role qualifiers. |
| Capability requirements | `A.2.2` | Ability constraints of a holder; a role name does not create ability. |
| Role characterization and role state | `A.2`, `A.2.5`, `A.19` when current | Characteristic scales and state predicates used to accept or reject role use. |
| Role relation structure | `A.2.7` | Context-local role-requirement substitution, incompatibility, qualification, and role bundles. |
| Method requirements | `A.15`, `A.3.1`, `A.3.2` | Method or method-description requirements and exclusions linked to a role or assignment. |
| Work attribution | `A.15`, `A.15.1` | Work is performed by the holder under a role assignment. |
| Evidence and status about role claims | `A.10`, `B.3`, `F.10`, `C.2.1`, direct evidence-use and status-use patterns | Epistemes used as evidence or status bearers stay outside `U.RoleAssignment`. |

Do not turn every relation in this neighborhood into a slot of `U.Role`. Use SlotSpec discipline only when the governing pattern declares a slot-bearing relation.

#### A.2:4.2 - Work-Facing Role Assignment Boundary

Use the short readable notation only as a notation for a typed assignment relation:

```text
Holder#Role:Context@Window
```

The normative assignment relation is governed by `A.2.1`, not by the notation. Its core slots are:

```text
RoleAssignmentCoreSlotSpec:
  HolderSlot:
  RoleValueSlot:
  BoundedContextSlot:
  AssignmentWindowSlot:
```

`HolderSlot` is filled by a `U.System` or acting holon admitted as system-like performer for the current work or method claim.

`RoleValueSlot` is filled by `U.Role`.

`BoundedContextSlot` is filled by the context that gives the role value its local meaning.

`AssignmentWindowSlot` is filled when assignment currentness, work attribution, role-state admission, or source freshness depends on a window. An open-world missing slot means unknown, not asserted, not recovered, or not current for this claim; it does not mean no such value exists.

Direct work-role patterns may add work-role qualifier slots. Evidence-use and status-use slots are not work-role qualifier slots and do not belong in assignment provenance.

#### A.2:4.3 - What Does Not Become `U.Role`

The following are not role values merely because source language says "role":

| Source phrase or temptation | Recover as |
| --- | --- |
| "the role of this standard" | standard-use, requirement-use, source-use, or publication-use relation around an episteme. |
| "the role of this dataset" | evidence-use, source-use, freshness, provenance, or measurement relation. |
| "the role of this theorem" | claim-use, proof-use, formal-substrate, or evidence-use relation. |
| "the role of this status badge" | status assertion, status-use relation, gate result, or assurance-use relation. |
| "the role of this parameter" | SlotKind, ValueKind, RefKind, method parameter, model parameter, or source label according to the governing pattern. |
| "the role of this interface" | module-interface claim, port, signature, API, protocol, service-access package, publication face, or boundary claim. |
| "the role of this capability" | capability requirement, holder capability, method requirement, or role description claim. |
| "the role of this relation argument" | SlotKind or relation position under `A.6.5`, not `U.Role`. |

If the direct kind is not yet clear, use `A.6.RSIR`.

#### A.2:4.4 - Role Taxonomy Inside a Bounded Context

Inside one bounded context, roles may be organized by:

- role-requirement substitution;
- role incompatibility;
- role bundles;
- role-state predicates;
- holder eligibility constraints;
- capability requirements;
- method requirements or exclusions;
- naming and description conventions.

`A.2.7` governs role relation structure. It is context-local role architecture in life, not mereology, not class subsumption for systems, not generic concern algebra, not `MethodRelationStructure@BoundedContext`, and not method algebra. Algebraic, graph, matrix, embedding, or neural descriptions are only lenses over selected role relation structure when a project explicitly uses them.

Typical work-facing role families include:

| Role family | Ordinary use | Boundary |
| --- | --- | --- |
| `TransformerRole` | A system or acting holon changes, produces, maintains, selects, derives, or controls an EntityOfConcern by work under a method. | The role does not change anything by itself; the holder performs work. |
| `ObserverRole` | A system or acting holon measures, samples, inspects, monitors, or records. | The measurement record is an episteme; the observing work remains work by the holder. |
| `VerifierRole` | A system or acting holon checks a claim, result, method, or work product. | The report or proof produced by verification is evidence or publication, not the verifying role holder. |
| `CoordinatorRole` | A system or acting holon coordinates other role assignments, plans, or work occurrences. | Coordination work is still dated work under method and plan claims. |

Domains may define roles such as `CoolingCirculatorRole`, `BridgeInspectorRole`, `ClinicalTrialCoordinatorRole`, `ModelCardReviewerRole`, or `ShipyardOperatorRole`. Define them in their bounded context and connect them to role assignment, capability, method, work, and evidence only when those claims are current.

#### A.2:4.5 - Reduced Use and Reopen Conditions

A role-like word may stay in reduced use when it only helps people recognize a local conversation and no claim depends on holder, assignment, context, time, capability, method, work, evidence, status, source, publication, or gate use.

Use the fuller role pattern when a claim based on the role-like word would change what can be done, claimed, checked, relied on, or attributed:

- use `A.2` when the role value itself, bounded context, role taxonomy, or role relation-neighborhood is current;
- use `A.2.1` when holder, role value, context, window, assignment source, or work-role qualifier is current;
- use `A.2.2` when ability or capability is current;
- use `A.2.5` when role-state admission, currentness, or role-state gate is current;
- use `A.2.7` when role-requirement substitution, incompatibility, qualification, or role bundles are current;
- use `A.15` when method, method description, work plan, or performed work is current;
- use direct episteme-use patterns when evidence, status, source, publication, requirement, definition, explanation, assurance, or gate use of an episteme is current;
- use `A.6.5` when the word "role" is only a relation position or SlotKind.

If a reduced-use role label is later used for a stronger claim, do not treat the earlier reduced use as evidence. Recover the needed role value, assignment relation, neighboring value, or direct episteme-use relation before the stronger claim is made.

