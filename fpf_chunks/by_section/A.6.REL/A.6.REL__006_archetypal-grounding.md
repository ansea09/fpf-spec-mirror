---
chunk_kind: "child"
pattern_id: "A.6.REL"
pattern_title: "Relation Obtaining and Individuated Relation Occurrences"
section_id: "A.6.REL:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.REL/A.6.REL__006_archetypal-grounding.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.6.REL — Relation Obtaining and Individuated Relation Occurrences"
  - "A.6.REL:5 — Archetypal Grounding"
line_start: 11523
line_end: 11561
dependencies:
  - "A.6.0"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "E.24"
  - "E.24.UK"
  - "F.18"
keywords:
---

### A.6.REL:5 - Archetypal Grounding

#### A.6.REL:5.1 - Admitted repeated role assignment through the relation-object architecture

Start with `Robot-7 holds InspectorRole`, interpreted by `MaintenanceRoles-2026` under `Maintenance-Scheme-A`, and trace only the objects needed by the current use.

1. **World-side participants and occurrence.** `Robot-7` remains an admitted `U.System`; `InspectorRole` remains a `U.Role` value; `MaintenanceRoles-2026` remains the exact role-taxonomy episteme; and `Maintenance-Scheme-A` remains the effective `U.ReferenceScheme`. Under `A.2.1`, those are the four actual participants of one `U.RoleAssignment` occurrence.
2. **Direct settlement.** `A.2.1` supplies the four participant meanings, the obtaining predicate, and the same-versus-new-occurrence rule. The occurrence continues while that predicate obtains without interruption for the same four participants. A demonstrated non-assignment gap ends it; later resumption starts another occurrence. An evidence gap by itself does neither.
3. **Reusable declaration.** For typed reuse, the `RelationSignature` for `U.RoleAssignment` contains `HolderSystemSlot : U.System / U.EntityRef`, `RoleValueSlot : U.Role / ByValue`, `RoleTaxonomyEpistemeSlot : U.Episteme / U.EpistemeRef`, and `EffectiveReferenceSchemeSlot : U.ReferenceScheme / ByValue`. `AssignmentInterval` remains assertion or occurrence-description content, not a fifth participant SlotSpec.
4. **Assertion and participant designations.** A `RoleAssignmentAssertion` contains designations corresponding to those four SlotSpecs and states the currently known `assignmentInterval` separately. Its claim may say that `Robot-7` currently holds `InspectorRole`. If later work only needs that current report, keep the assertion and stop without naming the occurrence.
5. **Occurrence identity, designator, and reference.** Suppose the same four participants occur in two inspection shifts separated by a demonstrated non-assignment period. A history or work-attribution claim applies the A.2.1 continuity rule, distinguishes the second occurrence, and may designate that occurrence. A roster row identifier, copied field set, or reused source key cannot collapse the two episodes.
6. **Representation.** A roster row or diagram edge may represent the assignment assertion or an occurrence-description episteme under `C.29`. Its source fields and key keep their representation-side meanings. An explicit declaration or C.29 correspondence relates a source field to the exact SlotKind and the carried value or reference to the participant designation; using the same spelling for field and SlotKind is optional and establishes no identity. Representation identity does not replace the A.2.1 occurrence rule.

The practical payoff is visible at each stop. A current staffing report keeps the readable direct sentence. Typed reuse opens the existing declaration. A history or work-attribution claim opens occurrence identity only when it must distinguish the repeated episode. Stable cross-reference use may then motivate naming and reference work.

#### A.6.REL:5.2 - Hypothetical installed-part boundary

`Bearing_B isPartOf Pump_P` may be a readable source claim, but current A.14 does not supply an `InstalledPart` relation kind, installed-part participant meanings, an installed-part obtaining predicate, or its same-versus-new-occurrence rule. Names such as `InstalledPartRelationSignature`, `InstalledPartSlot`, and `AssemblyWholeSlot` are therefore hypothetical candidates, not current declarations. Do not use them to claim conformance or an individuated installed-part occurrence.

A future accepted direct owner could make installation work or a continuous installation interval identity-bearing, but A.6.REL does not choose that ontology. Until such an owner exists, keep the physical entities, installation work, proposed part relation, assertion, occurrence description, designator, reference, and database or drawing representation separate, and stop before an occurrence-identity result.

#### A.6.REL:5.3 - Formal reduced case

The expression `3 < 5` is assertion content written in a mathematical notation. Under the referenced arithmetic structure, the values three and five satisfy the less-than predicate. The expression is not thereby a relation occurrence. No receiving use in this case needs the obtaining less-than relation occurrence explicitly individuated under `U.Relation`, so the engineer stops at the assertion. A graph edge or RDF reifier introduced by tooling remains a representation of the proposition or assertion and is not an occurrence-identity rule in the formal subject domain.

#### A.6.REL:5.4 - Relation occurrence as a participant

`C.22.PFR` has one actual-condition relation occurrence and one problem-criterion-applicability relation occurrence as world-side participants. Each is individuated under its own direct identity rule. The PFR direct pattern states those two participant meanings, its obtaining condition, and its identity rule; the PFR `RelationSignature` episteme declares the corresponding SlotSpecs. A PFR assertion designates the two occurrences according to those SlotSpecs. PFR is a direct relation, not an episteme whose content merely groups two assertions.

#### A.6.REL:5.5 - Description and publication recursion through the relation-object architecture

Let `R1` be the already individuated second `U.RoleAssignment` occurrence from 5.1.

1. An assignment-occurrence description episteme `E1` has `R1` as its EntityOfConcern. In the C.2.1 declaration, the entity-of-concern relation-participant meaning corresponds to `EntityOfConcernSlot`. In a card representation of `E1`, the source field `entityOfConcernRef` corresponds to that SlotKind only through a declared C.29 correspondence; its `U.EntityRef` value is the relation-participant designation that resolves to `R1`. Neither spelling nor containment identifies the field, SlotKind, designation, or occurrence.
2. A second episteme `E2` contains the result of evaluation work concerning the adequacy of `E1`. Its own `EntityOfConcernSlot` designation resolves to `E1`, not to `R1`. The two epistemes therefore have different EntitiesOfConcern and retain separate C.2.1 identities: `E1` describes `R1`, while `E2` evaluates the adequacy of `E1`.
3. Under a publication-relation occurrence, the current edition of `E1` is available to a declared audience and use. The selected episteme edition is an actual participant of that publication relation under the publication pattern's participant meaning. The publication form and its representation elements retain their own kinds and correspond to the published episteme only through the declared publication and representation relations.

A system performing revision work can establish another edition of `E1` or `E2`; a system performing publication work can establish another publication-relation occurrence for a selected edition. `R1` continues or ceases only as the A.2.1 obtaining predicate and occurrence-identity rule determine from the assignment facts. This recursive case preserves the distinction: a description episteme can itself become the actual participant or EntityOfConcern of another relation without becoming the relation occurrence it describes.

