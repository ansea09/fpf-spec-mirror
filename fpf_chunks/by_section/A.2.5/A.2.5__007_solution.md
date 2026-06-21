---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__007_solution.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:4 — Solution"
line_start: 3778
line_end: 3889
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:4 - Solution

Use `RoleStateRelation@BoundedContext` for the state-space relation of one `U.Role` in one `U.BoundedContext`.

```text
RoleStateRelation:
  RoleValueRef:
  BoundedContextRef:
  RoleStateSet:
  EnactableStateSet:
  StatePredicateSet:
  StateChangePredicateSet:
  StateAssertionRelation:
  RoleRelationStructureHooks:
  UKindDisposition: non-U selected relation structure
```

This is a relation value. A role description, policy, register, diagram, checklist, or publication may describe or store the relation value. The description or register is not the role-state relation itself by default.

Do not promote this object to a separate `U.*` kind. `RoleStateRelation@BoundedContext` has action-facing use because it controls role-state admission, but the identity is reducible to slot and relation combinatorics over existing governed values: `U.Role`, `U.BoundedContext`, role-state values, state predicates, state assertions, and the work-admission relation through `U.RoleAssignment`. The durable U-kind remains `U.Role`; A.2.5 supplies the selected state relation inside the role `ontologicalNeighborhood`.

#### A.2.5:4.1 - Core SlotSpecs

| SlotKind | ValueKind | Slot-use disposition | Meaning |
| --- | --- | --- | --- |
| `RoleValueRef` | `U.Role` | identity slot | The role value whose states are being described. |
| `BoundedContextRef` | `U.BoundedContext` | identity slot | The context that gives state names and predicates their meaning. |
| `RoleStateSet` | finite set of context-local state values | identity slot | The named states relevant to this role in this context. |
| `EnactableStateSet` | subset of `RoleStateSet` | admission slot | The states that admit a work or method-step claim when a valid state assertion exists. Empty set is allowed when the role is never work-admitting in that context. |
| `StatePredicateSet` | predicates over role characteristics, observations, evaluations, work records, speech acts, source relations, or context values | recognition slot | The predicates used to assert that a holder is in a state for a window. |
| `StateChangePredicateSet` | predicates for entering, maintaining, or leaving states | consideration slot | Used when state change matters. It does not define method order. |
| `StateAssertionRelation` | relation from role assignment, state, window, and evidence values to an assertion verdict | currentness-required when role-state admission is claimed | The relation that justifies "this role assignment is in this state for this window." |
| `RoleRelationStructureHooks` | references to `A.2.7` role-requirement substitution, incompatibility, or bundle expressions | current when role relation structure affects admission | State-aware checks for role-requirement substitution, incompatibility, and bundles. |

The SlotSpecs are open-world. A casual role-state note may only name role, context, and a state. A safety-critical work claim may require state predicates, evidence, assignment window, role-state window, capability checks, and method-step relation. Missing relevant content lowers or blocks the stronger claim; it does not assert that the value cannot exist.

#### A.2.5:4.2 - State and State Assertion

**Role state.** A role state is a context-local value in the `RoleStateSet` for one `U.Role` and one bounded context. Names such as `Ready`, `Calibrated`, `Suspended`, `Authorized`, `Stale`, or `Blocked` are local labels until their predicates are named.

**Enactable state.** An enactable state is a role state admitted by `EnactableStateSet`. A method-step claim or work-attribution claim that requires the role can use that state only with a current `StateAssertion`.

**State assertion.** A `StateAssertion` says that one `U.RoleAssignment` is in one role state for one window, with named evidence or source relations.

```text
StateAssertion:
  RoleAssignmentRef:
  RoleStateRef:
  AssertionWindow:
  PredicateEvaluation:
  EvidenceOrSourceUseRefs:
  AssertionStatus:
```

`PredicateEvaluation` is governed by the evaluation or evidence pattern that owns the claim. The assertion does not make the evidence episteme a role holder.

#### A.2.5:4.3 - Enactable-State Admission

Use this admission predicate when a method or work claim depends on role state:

```text
EnactableStateAdmission:
  requiredRole: U.Role
  roleAssignment: U.RoleAssignment
  requiredContext: U.BoundedContext
  workOrMethodClaim:
  window:
  admitted iff StateAssertion(roleAssignment, state, window)
              and state is in EnactableStateSet(requiredRole, requiredContext)
```

This predicate admits or blocks the work or method-step claim. It does not create work, select a method, grant capability, or prove that work occurred.

#### A.2.5:4.4 - State Predicates and State-Change Predicates

State predicates answer: **is this assignment in this state for this window?**

Examples:

- `CalibrationAge <= 30 days`;
- `AuthorizationDecision exists within the stated window`;
- `FatigueScore below threshold`;
- `IndependenceFrom(holder, conflictingAssignment) is true`;
- `ObservationProcedureActive and calibration trace is current`;
- `NoOpenIncident above declared severity`.

State-change predicates answer: **what evidence or event changes the state relation?** They may reuse the same observations or decisions, but their use is different. A predicate that says calibration expired can justify a `Stale` state assertion; it still does not prescribe the method order for recalibration work.

#### A.2.5:4.5 - Role Relation Structure Hooks

When `A.2.7` declares role-requirement substitution, incompatibility, or bundle expressions, A.2.5 adds state-sensitive admission.

| Role relation | State-sensitive reading |
| --- | --- |
| `AcceptedRoleForRequirement <= RequiredRole` | A state assertion for the accepted role can satisfy the required-role requirement only when the context declares a state refinement relation and enactability is preserved. |
| `RoleA incompatibleWith RoleB` | The conflict is usually about overlapping enactable states for one holder in one window, not about labels alone. |
| `RoleA plus RoleB` bundle | A work claim requiring both roles needs state assertions for both role assignments in the same window, unless the bounded context declares a composite role with its own `RoleStateRelation@BoundedContext`. |

Do not construct product state spaces by default. Product states are admitted only when the bounded context actually maintains a composite role value and gives it its own `RoleStateRelation@BoundedContext`. A graph or state-machine diagram may describe that relation; it is not the relation in life.

#### A.2.5:4.6 - Separation From Capability, Method, Work, Evidence, and Status

| Temptation | Recover as |
| --- | --- |
| "Assigned, therefore able" | Role assignment in `A.2.1` plus capability claim in `A.2.2`. |
| "Ready, therefore work happened" | State assertion here plus performed-work claim in `A.15.1` only if a `U.Work` occurrence is named. |
| "Authorized, therefore method selected" | Role-state or decision claim here; selected method remains governed by `A.3.1`, `A.3.2`, and `A.15`. |
| "Report has evidence role" | Evidence-use relation around an episteme, not a role state. |
| "Standard has normative role" | Requirement-use, standard-use, status-use, source-use, or publication-use relation around an episteme. |
| "Dashboard is monitoring role" | Publication, interface, source, or evidence relation for the dashboard; observing work belongs to a holder under `U.RoleAssignment`. |
| "`RoleEnactment` occurred" | Use `U.Work` with `performedBy = U.RoleAssignment`; use `RoleEnactmentFact` from `A.2.1` only as a derived fact when naming the fact helps. |

