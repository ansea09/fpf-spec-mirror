---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__006_solution.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:4 — Solution"
line_start: 94602
line_end: 94728
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3"
  - "A.6.9"
  - "A.6.REL"
  - "C.3.3"
  - "E.10.ROLE"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
keywords:
  - "already admitted U.Work"
  - "complete post-admission A.13/A.15.1/F.6 basis"
  - "conditional profile"
  - "deprecated performedBy compatibility only"
  - "direct case fact"
  - "exact Work-assignment relation"
  - "holder equality"
  - "performedUnderAssignment"
  - "same obtaining A.13 assignment"
  - "separate evidence"
  - "temporal coverage"
---

### F.6:4 - Solution

Treat performed-Work attribution as one direct relation species under `U.Relation`.

#### F.6:4.1 - Direct Relation Declaration

```text
performedUnderAssignment : U.Relation
  WorkOccurrenceSlot: U.Work, U.EntityRef
  SystemRoleAssignmentSlot: U.SystemRoleAssignment, U.RelationRef

when performedUnderAssignment(W, RA) obtains:
  attributedPerformerSystem(W, RA) := RA.HolderSystemSlot
```

`WorkOccurrenceSlot` names a dated Work already admitted under A.15.1 from independently grounded performance history, A.13-qualified actual performer facts, Method, extent, and containment. The typed slot consumes that completed membership result; F.6 neither helps establish nor reopens `W : U.Work`. The declaration-local `SystemRoleAssignmentSlot` names one occurrence of an admitted assignment species declared under `U.SystemRoleAssignment`. Its `U.RelationRef` names that occurrence and is limited to `U.SystemRoleAssignment`. Filling the two slots, matching the holder, or finding temporal overlap does not establish that this Work was performed under this assignment; the case must independently establish that link.

For an obtaining attribution:

```text
S = attributedPerformerSystem(W, RA) = RA.HolderSystemSlot
```

`S` is the admitted System already recovered as an actual performer through A.13 and used by A.15.1 to admit `W`; F.6 does not discover it. `RA` is the assignment under which that Work is now attributed. The projection exposes the holder already carried by `RA` only to test equality with `S`; it creates neither performerhood, Work, attribution, classification, nor a generic assignment occurrence and discards none of RA's additional participants.

`performedBy` remains only a deprecated source relation name. Read it through the direct Work-assignment relation only after A.13 and A.15.1 have independently established the actual performer and admitted Work, and after holder equality is checked. New practitioner-facing claims say that the already recovered performer System performed the Work under the assignment, or name `performedUnderAssignment` when the relation name is needed; they never make the assignment the performer or use F.6 to discover one.

No evidence, log, status, MethodDescription, result, publication, context record, or assignment-state assertion is a generic attribution participant.

#### F.6:4.2 - Obtaining and Occurrence Identity

The direct Work-assignment attribution is a world-side fact, separate from any assertion or evidence. A positive check requires all of the following:

1. `W` is one exact dated `U.Work` occurrence already admitted under A.15.1 from its independently grounded candidate-action history, A.13-qualified actual performer basis, Method actually followed, temporal extent, and containing-System relation; that admission neither assumes nor depends on this F.6 relation;
2. the actual performer `S` has the A.13 core for this action, scope, working situation, and window: `S` is an admitted System, satisfies and is classified under one exact local agential system-role kind, and holds the same obtaining assignment `RA`; evidence supports those core facts, while a characteristic profile is required only for a consumed Grade, autonomy or profile result, criterion-dependent characteristic, or assurance use;
3. `RA` is one named assignment occurrence of a declared `U.SystemRoleAssignment` species, with all identity-bearing participants and its rule recovered;
4. the case establishes that `W` was performed under `RA`, rather than deriving that link from a label, common holder, assignment existence, or temporal overlap;
5. `RA.HolderSystemSlot = S`, the admitted System that actually performed `W`; and
6. RA's species predicate obtains throughout the attributed temporal extent of `W`.

Conditions 1–3, 5, and 6 are five constraints on a valid attribution but do not establish it. F.6 reuses the obtaining A.13 assignment; it does not create the A.13 classification, assignment, evidence, optional profile, or Work. Failure of condition 4 or any constraint leaves `W : U.Work` intact and leaves only this exact assignment-bound attribution unasserted.
Two overlapping assignments held by the same System may satisfy all five constraints while the case links the Work to only one. Use that case fact; if it does not distinguish the assignments, leave the attribution unresolved rather than asserting both.

If attribution concerns only a temporal, episode, or operational part of a larger Work whole, first identify that part as its own `U.Work` occurrence under A.15.1. Do not hide an unidentified Work portion inside F.6.

When a receiver needs an explicit attribution occurrence:

```text
PerformedUnderAssignmentOccurrenceKey =
  <WorkOccurrenceSlot, SystemRoleAssignmentSlot>
```

This key identifies an already obtaining relation; it does not make one obtain. The attribution extent follows `W`. Extending an open Work interval or later recording its end does not create another attribution occurrence while both participants and the direct relation remain the same. Another Work occurrence, separately identified Work part, or assignment episode yields another possible pair whose relation must be checked independently.

An assertion can state the exact pair, and evidence can support reliance on that assertion. Neither the assertion nor its evidence constitutes the world-side relation. Missing evidence leaves reliance unresolved; missing pair grounding leaves the positive attribution unasserted. A demonstrated different performer, non-covering assignment, or false direct pair can support a stronger negative claim.

#### F.6:4.3 - Preserve the Exact Assignment Species

Before checking or relying on attribution, recover RA's declared species and occurrence. This distinguishes the assignment even when the final practitioner sentence omits its full declaration. Every species declares:

- a `HolderSystemSlot` whose `ValueKind` is `U.System`;
- a declaration-local `AssignedSystemRoleKindSlot` whose `ValueKind` is the exact local system-role-kind domain admitted for that species;
- every additional participant meaning and its `ValueKind`;
- the rule, applicability, and maximal uninterrupted occurrence identity.

An assignment occurrence supplies one participant value for each slot. In particular, it supplies one local system-role-kind value from the `AssignedSystemRoleKindSlot` domain; the value does not replace or narrow that declared domain.

A simple assignment may have only holder and kind. A project appointment may also have `ReviewCommissionSlot`. F.6 accepts both through the family ValueKind and holder projection while retaining the declared species and all participants that distinguish the assignment occurrence. Those participants and the assignment rule still do not establish that the Work was performed under the assignment; the case must establish that link separately. F.6 never creates a two-participant generic assignment beside the appointment.

Taxonomy, scheme, `KindSignature`, assertion, and `assignmentInterval` can interpret or describe RA without becoming participants by default. Verify temporal coverage from whether the assignment rule actually holds, not merely from a recorded interval.

Do not replace the species with one `Context` value. Recover what the source token denotes and use its direct pattern. It can denote a system or Work locus, claim scope, or selected `BoundedModelUseStructure`; those objects are neither interchangeable nor optional participants of generic assignment or attribution signatures.

#### F.6:4.4 - Attribution Check Sequence

1. Start from the exact `U.Work` occurrence already admitted by A.15.1 without an F.6 premise.
2. Recover the assignment occurrence, including its declared species, identity-bearing participants, rule, applicability, and time span.
3. Find the case fact that directly links this Work to this assignment; do not infer that link merely because the holder and interval match.
4. Confirm that the assignment holder is the actual performer.
5. Confirm that the assignment predicate obtains throughout the attributed Work interval.
6. When all five checks pass, state the F.6 relation or say plainly that the holder System performed the Work under that assignment. If the direct link, a participant, or a required constraint is missing, retain the admitted Work and leave only this assignment-bound attribution unresolved; do not select another covering assignment.
7. Keep assertions and evidence separate: they can support reliance on the attribution claim but do not make the relation obtain.
8. Send classification, assignment state, capability, Method, evidence, source use, result, acceptance, publication, bridge, responsibility, and authority questions to their subject patterns.

This sequence is application guidance, not a new check record or workflow object. Its first useful result is the readable exact relation, an unresolved exact pair with the missing fact named, or a corrected route to the direct neighboring claim.

#### F.6:4.5 - Method and Work Boundary

`performedUnderAssignment` has no Method participant. A separate claim may say that the Work enacts one exact semantic Method. The holder System performs the Work; the Work, not the performer or assignment, enacts the Method.

The assignment, system-role kind, capability, Method, and MethodDescription do not act or perform Work. Citing a description can identify, constrain, or support a receiving use of the Method, but it neither enacts the description nor establishes `D : U.MethodDescription`; use A.3.2 to test that membership separately.

#### F.6:4.6 - Direct Neighboring Relations

| Current question | Direct exit | Why it stays separate |
| --- | --- | --- |
| Does the assignment obtain? | `A.2.1` | The declared species and predicate, the occurrence's participant values, and the occurrence-identity rule precede attribution but do not establish it. |
| Does the holder count under its system-role kind? | `A.2`, C.3.2 | Classification is not supplied by attribution. |
| Does the assignment satisfy a state predicate? | `A.2.5` | State has its own predicate, relation, window, assertion, and evidence. |
| Can the holder perform the Work? | `A.2.2` capability and fit | Ability is not actual performance. |
| Which Systems actually performed a top-level or child Work occurrence? | Recover each exact performer through `A.13`, then let `A.15.1` independently admit that Work occurrence; add one F.6 check per exact performer–assignment pair only when the receiving question also asks under which assignment the Work was performed. | A team lead, coordinator, member relation, or covering assignment cannot substitute for the full actual-performer set. Every child Work keeps its own A.13 performer basis, A.15.1 admission, and Work-part relation; assignment and F.6 are added only for an expressly consumed attribution. Missing or failed F.6 leaves the child Work intact. |
| Did a passive test article participate in Work? | the domain rule that defines passive participation; if no such rule is current, `A.6.RCD` returns `missing-governor` | Holding a test-subject assignment does not make the article a performer or establish passive participation. |
| Which Method did the Work enact? | `A.15.1`, `A.3.1`, and A.3.2 only for a separate description-membership question | Method, description, and assignment do not become performers. |
| What supports the attribution assertion? | `A.10` or the direct evidence relation | Support concerns knowledge or use, not relation obtaining. |
| Which encountered material is relied upon? | `A.15.4` | Reliance on a visible item is not attribution. |
| What changed, first existed, was measured, evaluated, delivered, or accepted? | `A.6.1` only when the claim consumes one exact operation application or returned-value binding; `A.15.PROD` plus the subject's identity rule for a produced entity or its inception; `C.2.1` for a result episteme; otherwise the exact change, measurement, evaluation, delivery, or acceptance pattern | Each claim follows its own pattern, and none supplies a performer-attribution participant. An operation binding alone establishes neither production nor a result episteme. |
| Does another context have a corresponding kind or assignment? | `C.3.3`, `F.9`, `A.6.9` | A Bridge merges neither kind nor assignment and does not retarget Work. |
| Does a selected model-use structure change this attribution interpretation? | `A.1.1` plus the receiving assertion or use | Generic assignment and attribution gain no optional structure participant. |

#### F.6:4.7 - Source Shorthand and `RoleEnactment`

`Holder#Role:Context@Window` is readable source notation only. Recover the actual system, local system-role kind, assignment species and occurrence, and the object denoted by `Context`. The source spelling is not a signature.

When source wording says `RoleEnactment` or `RoleEnactmentFact`, recover dated Work and `performedUnderAssignment`. Do not retain a second enactment kind, fact object, or relation occurrence.

#### F.6:4.8 - Lightweight Use

After the Work–assignment link and its necessary constraints are established, ordinary use can stop at:

```text
InspectionWork-17 was performed by Robot-7 under InspectionAssignment-17.
```

Expose declarations and occurrence keys only when a dependent use must distinguish occurrences, cite one as a participant, compare assertions, or preserve provenance. If the assignment cannot be recovered, lower the claim to “Robot-7 is named as performer in record R” and state the source, reliance, and evidence claims under their direct predicates.

Another pattern may require a **complete A.13/A.15.1/F.6 basis** when its receiving use needs both admitted Work and precise assignment-bound performer attribution, and may point here instead of repeating this declaration and check sequence. That combined basis has a fixed order: A.13 first supplies every performer's exact System, local agential kind and criterion, classification, obtaining assignment, needed scope, working situation, window, and adequate core evidence; A.15.1 independently admits the dated Work from its performance history, at least one obtaining `enactsMethod` relation, extent, and at least one obtaining locally declared Work-to-System containment relation; only then does F.6 test every required exact Work-assignment pair through the same obtaining A.13 assignment. The phrase is never an A.15.1 membership test. A missing F.6 relation preserves `W : U.Work` and leaves only the precise attribution unresolved. A characteristic profile remains conditional, and another enactment or containing-system relation is named only when the receiving use relies on it.

