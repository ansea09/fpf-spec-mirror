---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__006_solution.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:4 — Solution"
line_start: 90058
line_end: 90160
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.REL"
  - "E.10"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "actual performing U.System"
  - "assignment coverage"
  - "exact U.RoleAssignment"
  - "performedUnderAssignment"
  - "separate assertion and evidence"
  - "world-side attribution"
---

### F.6:4 - Solution

Govern performed-work attribution as one direct relation species under `U.Relation`.

#### F.6:4.1 - Direct Relation Declaration

```text
performedUnderAssignment : U.Relation
  WorkOccurrenceSlot: U.Work, U.EntityRef
  RoleAssignmentSlot: U.RoleAssignment, U.EntityRef

when performedUnderAssignment(W, RA) obtains:
  actualPerformerSystem(W, RA) := RA.HolderSystemSlot
```

`WorkOccurrenceSlot` names the dated performed occurrence governed by `A.15.1`. `RoleAssignmentSlot` names the obtaining assignment occurrence governed by `A.2.1`.

For an obtaining attribution, the readable actual-performer cue is `S = actualPerformerSystem(W, RA) = RA.HolderSystemSlot`: `S` is the admitted `U.System` that acts, while `RA` is the assignment under which that action is attributed. The projection exposes the actor already carried by the assignment participant; it does not assert attribution when the relation fails to obtain and is not another relation kind or occurrence.

`performedBy(W, RA)` is a deprecated compatibility spelling of `performedUnderAssignment(W, RA)`. Existing claims or records may be read through that alias only after resolving `S = RA.HolderSystemSlot`. New practitioner-facing claims, examples, and conformance statements MUST use `S performed W under RA` or `performedUnderAssignment(W, RA)`, never wording that makes `RA` the performer.

No evidence, log, status, method description, result, publication, context record, or role-state assertion is a generic participant in this relation.

#### F.6:4.2 - Obtaining and Occurrence Identity

The relation `performedUnderAssignment(W, RA)` obtains when:

1. `W` is one exact dated `U.Work` occurrence governed by `A.15.1`;
2. `RA` is one obtaining `U.RoleAssignment` occurrence;
3. the holder system in `RA.HolderSystemSlot` actually performed `W` under `RA.RoleValueSlot`;
4. the assignment predicate for `RA` obtains throughout the temporal extent of `W`.

If the performer attribution concerns only a temporal, episode, or operational part of a larger work whole, first identify that part as the `U.Work` occurrence under `A.15.1` and use it in `WorkOccurrenceSlot`. Do not hide an unidentified work portion inside the attribution relation.

When a receiving use needs an explicit relation-occurrence reference, use:

```text
PerformedUnderAssignmentOccurrenceKey = <WorkOccurrenceSlot, RoleAssignmentSlot>
```

The temporal extent is inherited from `WorkOccurrenceSlot`. Extending an open work interval or later recording its end does not create another attribution occurrence while both participants remain the same. A separately identified work occurrence, including a separately identified work part, or a different assignment episode yields a different relation occurrence.

An evidence gap leaves a relied-on attribution assertion unresolved. It does not demonstrate that `performedUnderAssignment` failed to obtain. A demonstrated different performer or non-covering assignment episode can support the stronger negative claim.

#### F.6:4.3 - Recover the Exact Assignment

Before relying on the attribution, recover the four direct participants of the exact assignment occurrence `RA` that fills `RoleAssignmentSlot`:

```text
RoleAssignmentRelationSignature:
  HolderSystemSlot: U.System, U.EntityRef
  RoleValueSlot: U.Role, ByValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, ByValue
```

One assignment occurrence is the maximal continuous period during which the assignment predicate obtains for those fixed four participants. A supporting assertion or occurrence description may state `assignmentInterval`, including an open end, but that field is not a participant and does not establish temporal coverage. Verify coverage for `performedUnderAssignment` from the actual obtaining history of the exact assignment occurrence and the exact work extent.

Do not replace these participants with one `Context` value. If source notation contains `Context`, recover what that token denotes and send it to its direct pattern. It may denote an actual system or work locus, a claim scope, or an independently selected `BoundedModelUseStructure`; those objects have different kinds and relations. A selected model-use structure can qualify the receiving attribution assertion, but it is not an optional participant of generic `U.RoleAssignment`.

#### F.6:4.4 - Attribution Check Sequence

Use this short sequence for the current attribution claim:

1. Name the exact `U.Work` occurrence whose performer is being asserted.
2. Name or recover the exact `U.RoleAssignment` occurrence through its four fixed participants and uninterrupted obtaining extent.
3. Check that the holder system named by the assignment is the system claimed to have performed the work.
4. Check that the assignment episode covers the attributed work interval.
5. State the direct `performedUnderAssignment(WorkOccurrenceSlot, RoleAssignmentSlot)` relation, or keep the attribution assertion unresolved when support is insufficient.
6. Send role state, capability, method fit, evidence, source use, result, acceptance, publication, and bridge questions to their direct governing patterns.

The sequence is application guidance, not a new check record, work plan, or workflow object. Its useful result is the repaired direct relation or an explicit stop at the missing relation participant or support claim.

#### F.6:4.5 - Direct Neighboring Relations

| Current question | Direct exit | Why it stays separate |
|---|---|---|
| Does the assignment obtain? | `A.2.1` | Assignment identity and occurrence precede work attribution. |
| Does the assignment satisfy a current state predicate? | `A.2.5` | Role state has its own predicate, window, assertion, and evidence use. |
| Can the holder perform the work? | `A.2.2` capability and capability-fit relation | Ability is not actual performance. |
| Which method was enacted? | `A.3.1`, `A.3.2`, and `A.15.1` | Method, method description, and work occurrence have different identities. |
| What supports the attribution assertion? | `A.10` or the direct evidence relation | Support concerns knowledge or use of obtaining. |
| Which encountered material is being relied upon? | `A.15.4` | Reliance on a visible item is not the attribution relation. |
| What changed, first existed, was measured or evaluated, was delivered, or was accepted in connection with the work? | `A.15.1` for the work, then the exact change, A.6.1 operation-result, A.15.PROD inception, measurement, evaluation, delivery, or acceptance governor | None of these entities, values, or relations is a participant in performer attribution. |
| Does another vocabulary denote a corresponding role? | `F.9` | A bridge does not mutate either local assignment. |
| Does a model-use organization change this attribution interpretation? | `A.1.1` plus the receiving attribution assertion or use | The receiving episteme or use may designate the selected structure; generic assignment and attribution signatures gain no optional participant. |

#### F.6:4.6 - Source Shorthand and `RoleEnactment`

`Holder#Role:Context@Window` is readable source notation only. Before reliance-bearing use, recover the assignment's holder system, role value, role-taxonomy episteme, effective reference scheme, and assignment window. Recover the object denoted by `Context` separately.

When source wording says `RoleEnactment` or `RoleEnactmentFact`, recover the dated `U.Work` occurrence and the direct `performedUnderAssignment` relation. Do not retain a second enactment kind, fact object, or relation occurrence.

#### F.6:4.7 - Lightweight Use

Ordinary use can stop at a readable assertion:

```text
InspectionWork-17 was performed by Robot-7 under RoleAssignment-17.
```

Expose the relation declaration and occurrence key only when a receiving use must distinguish attribution occurrences, cite one as a participant, compare assertions, or preserve provenance. If the assignment cannot be recovered, lower the claim to "Robot-7 is named as performer in record R" and route that reliance through `A.15.4` or the direct source and evidence patterns.

