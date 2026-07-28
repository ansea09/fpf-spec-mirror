---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__005_solution.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:4 — Solution"
line_start: 90550
line_end: 90652
dependencies:
  - "A.2.4"
  - "B.3"
  - "F.1"
  - "F.18"
  - "F.3"
  - "F.9"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:4 - Solution

Treat a status claim as a context-local status-use statement, not as a free-floating adjective and not as a role assignment.

#### F.10:4.1 - Three Status Families

F.10 uses three status families as a small spine for common project work:

| Status family | Status modality | Typical target kind | What it says |
| --- | --- | --- | --- |
| `EvidenceStatus` | epistemic | claim, quantity, observation-backed claim, effect claim, model-result claim | What the available evidence says for or against a target claim in the current context and window. |
| `StandardStatus` | deontic, curatorial | method description, standard text, profile, governed product configuration, standard-governed project entity | What a canon, standard, profile, or governing register sanctions, discourages, or supersedes in the current context and edition. |
| `RequirementStatus` | deontic, compliance-facing | requirement clause, duty clause, constraint clause, acceptance criterion, obligation claim | Whether a clause applies, is satisfied, is violated, is waived, is pending, or does not bind under stated conditions. |

A project may add local sublevels or local labels, but the local label must map to one of these families or to another direct status pattern named by value. Do not create a new role kind merely because a status word is local.

#### F.10:4.2 - StatusCell and StatusUseStatement

A `StatusCell` is a context-local sense cell for a status value. It has a status family, status modality, typical target kind, polarity, and window discipline. A `StatusCell` is a meaning cell, not a work performer and not a gate decision.

A `StatusUseStatement` applies one status cell or local status value to a target in a bounded context:

```text
StatusUseStatement:
  BoundedContext:
  StatusFamily:
  StatusCellOrLocalValue:
  StatusModality:
  StatusTarget:
  StatusTargetKind:
  StatusScope:
  StatusPolarity:
  StatusWindow:
  StatusSourceOrProvenanceConstraint:
  StatusUse:
  BridgeRef:
  NotCarried:
```

`StatusTargetKind` decides relation identity. A status that qualifies a method description is not the same status-use statement as a status that qualifies a requirement clause, even when the visible label is the same. `NotCarried` names the stronger use that this status statement does not carry, such as gate passage, release permission, assurance, performed work, causal identification, global truth, or cross-context substitution.

#### F.10:4.3 - Relation Slots for Status Use

Use the A.2.4 status-use slots when a status statement must be precise enough for reliance:

| SlotKind | ValueKind | Currentness discipline |
| --- | --- | --- |
| `StatusBearerSlot` | episteme, claim, method description, publication, role assignment, work occurrence, clause, gate record, or another bearer admitted by the direct pattern | Names the value whose status is being asserted or read. It does not make the bearer a role holder. |
| `StatusTargetSlot` | claim, method, episteme, publication, work result, clause, bearer, or another governed target | Required when the status is not simply about the bearer itself. |
| `StatusScopeSlot` | bounded-context scope, claim scope, admission scope, requirement scope, or use scope | Currentness-required when scope changes the status assertion. |
| `StatusValueSlot` | status value governed by F.10 or a direct status pattern | Required for any status assertion. |
| `StatusWindowSlot` | temporal validity window, freshness policy, edition window, status-currentness relation, or source-currentness relation | Currentness-required for time-sensitive or edition-sensitive status. |
| `StatusUseSlot` | gate use, assurance use, admission use, source-currentness use, work-plan readiness use, requirement evaluation use, standard-use, or another direct use | Required when the status is consumed for that use. |
| `StatusProvenanceConstraintSlot` | source order, authority source, publication, proof, verification, register, or provenance constraint | Currentness-required when provenance decides status use. |

These SlotKinds are relation positions. They are not `U.Role` names, not work-role qualifier slots, and not a new generic status ontic by themselves.

#### F.10:4.4 - Family Spines

The following spines are deliberately small. They help contexts map local status words without pretending that every domain has the same status vocabulary.

**EvidenceStatus** values:

1. `Observed` - seen or recorded once under declared observation conditions.
2. `Measured` - quantified under a declared measurement procedure.
3. `Corroborated` - backed by more than one independent source, procedure, or observation line.
4. `Replicated` - repeated by others or under varied declared conditions.
5. `Refuted` - counter-evidence defeats the positive standing inside the same window.
6. `Inconclusive` - the available evidence is insufficient or mixed for the target claim.

**StandardStatus** values:

1. `Candidate` - proposed and not yet normative in the context.
2. `Draft` - worked text or profile, not yet the governing edition.
3. `Approved` - normative in this context and edition.
4. `Deprecated` - discouraged, allowed only under stated conditions, or being phased out.
5. `Superseded` - replaced by a newer edition, profile, or governing source.

**RequirementStatus** values:

1. `Applicable` - the clause binds in the stated context and window.
2. `Inapplicable` - the clause does not bind under stated conditions.
3. `Satisfied` - met within the stated context and window.
4. `Violated` - not met within the stated context and window.
5. `Waived` - binding is suspended or exceptioned by a named source and window.
6. `Pending` - awaiting evidence, evaluation, decision, or source-currentness repair.

#### F.10:4.5 - Bridge Discipline

Status meanings do not travel by label. A cross-context comparison, explanation, or substitution uses an `F.9` bridge with direction, bridge kind, congruence level, and loss notes.

Explanation is the ordinary cross-context use. Substitution is admitted only when the bridge kind, congruence level, window alignment, target kind, and local evaluation rule all admit the substitution. Cross-modality movement, such as evidence status being used to evaluate requirement status, is an interpretation relation; it is not equivalence.

#### F.10:4.6 - Design-Run Discipline

Keep three questions separate:

* What does the evidence show about a claim or measured quantity in this window?
* What does the standard or canon sanction for a method description, profile, or governed project entity in this edition?
* What is the requirement clause doing in this context and window?

A standard-approved method description can be a source for method selection or a condition for allowed use. It does not by itself show that a run-time clause is satisfied. Run-time evidence can help evaluate a requirement clause. It does not by itself approve the method or standard profile unless a governing context has a rule for that promotion.

