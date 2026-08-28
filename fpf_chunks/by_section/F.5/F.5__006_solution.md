---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
section_id: "F.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__006_solution.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
  - "F.5:4 — Solution"
line_start: 92660
line_end: 92738
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.3"
  - "C.3.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.24.UK"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.6"
keywords:
  - "Plain and Tech designations"
  - "SystemRoleKindDescription label"
  - "U-kind name"
  - "local meaning"
  - "naming after ontology recovery"
  - "system-role-kind name"
---

### F.5:4 - Solution

Name after meaning. Recover the value, its kind, direct meaning source, and intended use. Then choose designations that preserve them.

Make these facts recoverable in the prose, direct admission, F.4 description, Concept-Set row, or NameCard. This is a naming checklist, not a relation signature or mandatory record:

- the exact named value and its admitted kind;
- the direct source of its meaning;
- for a local system-role-kind designation, the candidate domain, operative membership condition, intended member/non-member boundary, continuity rule, current `KindSignature`, and effective scheme, with source or practice provenance kept as a locator or comparison cue;
- for a description name, the separate F.4 `SystemRoleKindDescription` and its exact EntityOfConcern;
- the selected Tech and Plain designations;
- aliases or predecessor labels with lineage;
- morphology, neutrality, and minimal-generality checks; and
- the boundary that prevents the name from absorbing classification, assignment, capability, Method, Work, status, evidence, permission, responsibility, publication, or relation-position claims.

#### F.5:4.1 - Name Families Used Here

| Name family | Meaning source | Naming rule |
| --- | --- | --- |
| Public U-kind or durable cross-local value name | Public U-kind admitted through E.24.UK, or another exact value already recovered through the direct rule for that kind of value; a Concept-Set row may retain witness comparison but supplies neither identity nor admission | Use a neutral Tech head at minimal generality. Do not let one witness's private vocabulary win by spelling alone. |
| Concrete local system-role-kind designation | Exact C.3 kind admitted under A.2, recovered through its candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule; source or practice provenance only locates or helps compare the settlement | Use a concrete `...SystemRole` Tech designation. `SystemRole` is morphology, not a universal value; do not add `Kind` when `: U.Kind` is already explicit. |
| `SystemRoleKindDescription` designation | F.4 description episteme whose exact EntityOfConcern is one local system-role kind | Name the description separately, for example `PumpInspectorSystemRoleKindDescription`; never use the description name as the kind or assignment name. |
| Relation among system-role kinds or a system-role–Method expression | Exact relation under A.2.7 and, when current, a separately recovered Method, MethodDescription, or Work | Name the recovered relation or neighboring object. Ordinary phrasing may stay compact but must not hide independent classifications or assignments. |
| Method, Method family, Method relation structure, WorkPlan, or Work name | A.3, A.15, G.5, and the exact composition or Work pattern | Name that object directly. Shared words with a system-role-kind label create no relation or identity. |
| Mathematical or representation lens name | Description of a selected system-role-kind relation structure, Method relation structure, transformation-flow structure, or another governed structure | Name the lens only when the representation is itself the governed value. Otherwise name the underlying structure or relation. |
| Status, evidence, requirement, source, standard, publication, assurance, gate, or decision name | Exact direct relation or value | Do not treat it as a `SystemRoleKindDescription` branch. Use F.18 only after the direct object is recovered. |
| Relation slot or argument-position name | A.6.RSIR, A.6.5, and the exact relation or signature declaration | Name the participant meaning, slot, or argument position. Do not use `SystemRole` morphology unless the value is independently a local system-role kind. |

Keep four things separate: the chosen name, the local system-role kind it names, an optional F.4 description of that kind, and any assignment that the current use actually needs. The name designates the kind; the description describes it. An assignment is a separate A.2.1 occurrence of a directly declared species under `U.SystemRoleAssignment`. That species says which systems may be holders, which exact local kinds may fill the assigned-kind place, what the assignment predicate means, when it applies, how an uninterrupted occurrence keeps its identity, and whether another real participant matters. The occurrence supplies the actual holder, assigned kind, and any other participant values. If the naming use needs no assignment identity, do not invent an assignment. Spelling, a suffix, a NameCard, a public row, a description, or a citation creates none of these objects, nor any dated Work, result episteme, provenance record, or publication occurrence.

#### F.5:4.2 - Tech and Plain Designations

Use two human-facing designations when a name is durable enough to be reused:

| Designation | Job | Constraint |
| --- | --- | --- |
| Tech designation | Stable label used by the local pattern, table, or description episteme | Must fit the recovered kind and exact meaning source. |
| Plain designation | Short teaching phrase or sentence | Must point to the same value without widening the sense. |
| Symbol or source abbreviation | Optional local notation or lineage spelling | Informative only; it is not another selected Tech or Plain designation. |

For a concrete local system-role kind, the Tech designation normally ends in `...SystemRole`, for example `ReviewerSystemRole` or `PumpInspectorSystemRole`. The Plain designation may remain ordinary, for example “reviewer” or “pump inspector”, when the named practice and criterion make the intended kind clear. Add “system role” only when it prevents a live neighboring reading. The compound does not imply non-human technical systems, kind admission, candidate classification, assignment, agency, capability, Method, or Work.

For the description episteme, name the description rather than the described kind: `PumpInspectorSystemRoleKindDescription` may have Plain designation “description of the pump-inspector system-role kind”. `SystemRoleKindDescription` identifies the construction; `Kind` identifies the EntityOfConcern and `Description` already identifies the episteme.

For a coupled system-role–Method phrase, recover the local kind and Method separately before naming either one. Recover and name a MethodDescription, WorkPlan, or dated Work only when that exact object is already admitted and the naming use consumes it; a shared phrase does not require any of them to exist. `RoboticsEngineerSystemRole` may designate one admitted local kind; `RobotEngineeringMethod` names a Method or Method family. Ordinary *engineer-roboticist* may remain the Plain expression when nearby project wording makes the intended kind clear and the C.3 candidate domain, membership distinction, boundary probes, and continuity remain recoverable. The wording helps the reader; it does not identify the kind. It replaces neither a qualifying MethodDescription nor any description of planned or performed Work.

When a later naming use actually consumes one dated Work identity, that Work must already be constituted before F.5 naming begins. Recover every exact actual performer through A.13, and let A.15.1 independently admit the Work from its semantic Method, time, containing System, and other required direct facts. Add the assignment occurrence, holder equality, and F.6 relation only when the naming record or receiving use expressly represents precise assignment-bound attribution; missing or failed F.6 leaves the Work identity intact. Otherwise keep the activity in ordinary wording and do not mint a Work identifier merely to support a name.

For a U-kind, the Tech designation should be neutral enough that no witness wins by vocabulary alone. If witnesses disagree between `Observation`, `Reading`, and `MeasurementResult`, a Concept-Set row preserves the comparison; the exact shared value and invariants must still pass E.24.UK admission or their direct defining rule before an author uses F.5 to choose a name.

#### F.5:4.3 - Positive Naming Rules

1. **Recover the object first.** State the governed kind or construction of the value—for example, a U-kind, local system-role kind, description episteme, classification judgment, assignment, relation, Method, Work, status, evidence use, slot, lens, or another object.
2. **Recover the meaning source.** Use the exact E.24.UK or direct admission for a U-kind; A.2 with C.3 for a local system-role kind; F.4 for its description; A.2.7 for relations among kinds; A.3, A.15, G.5, or the exact composition pattern for Method and Work names; and the direct relation for status, evidence, source, requirement, publication, assurance, gate, decision, and relation-position names.
3. **Use minimal generality.** The designation's scope is no wider than the admitted invariants.
4. **Keep interpretation metadata out of the label.** Edition, source, witness, local boundary, reference scheme, and threshold belong in the direct declaration, description, relation, or NameCard.
5. **Make morphology object-sensitive.** Concrete local system-role kinds use `...SystemRole`; description epistemes use `...SystemRoleKindDescription`; states use state or level wording; slots say `Slot`, `Argument`, `Endpoint`, or another exact position head.
6. **Keep coupled names typed.** A compact phrase may help a reader, but one label must not carry several independently governed objects—for example, kind, assignment, capability, Method, Work, and description—at once.
7. **Do not encode thresholds or windows in the name.** Put time, state, threshold, capability envelope, or admission window in the direct claim.
8. **Use aliases only with lineage.** A source term, predecessor term, symbol, or translation does not become a second selected Tech label.
9. **Escalate only for actual reuse.** Use F.18 and F.17 for durable or public naming. When an actual cross-local relation is consumed, name the exact obtaining C.3.3 relation between local kinds or F.9 Bridge between distinct F.17 cells and keep the separate C.2.1 claim that it suits the named use. Ordinary reliance requires the exact A.10 evidence-provenance relation and `RelianceDisposition=pass`. Use B.3 only when an actual named assurance claim is current. None of the cross-local relation, use claim, evidence path, assurance result, NameCard, row, designation, or publication establishes assignment, Work, result, provenance, assurance, or publication occurrence.

#### F.5:4.4 - Neighboring Use Boundary

When a candidate contains a tempting word, recover the current claim instead of replacing words mechanically.

| Source wording | First ontological question | Direct next locus |
| --- | --- | --- |
| `EvidenceRole`, `ModelFitEvidenceRole`, or “evidence role” | Is an episteme used as evidence for a target claim with exact scope, polarity, relevance window, and provenance? | A.10, B.3, C.2.1, or the exact evidence-use relation |
| `RequirementRole` or “standard role” | Is an episteme, standard, or clause used as a requirement, source, or specification? | E.10.D2, C.28, E.17, or the exact source or requirement relation |
| `Access Role` in RBAC | Is this a policy or permission grouping rather than a work-facing kind? | Exact access, policy, permission, or status relation; F.18 only if durable naming is needed |
| “role of subject, provider, or input” | Is this participant meaning, a declaration slot, or a representation position? | E.10.ROLE, A.6.RSIR, and A.6.5 |
| `ReviewerSystemRole` | Is one exact local C.3 kind with a direct criterion current? | A.2 with C.3; F.4 for its description; A.2.1 only when assigned |
| `robotics engineer` or `engineer-roboticist` | Is this a local kind, conjunction, relation, Method, Work, or capability? | A.2.7, A.3, A.15, A.2.2, and F.18 when durable naming is current |
| `Reviewing`, `ReviewMethod`, `RobotEngineeringMethod`, `ReviewWorkflow`, or `MethodAlgebra` | Is this a Method, MethodDescription, Method relation structure, WorkPlan, performed Work, or lens? | A.3, A.15, G.5, C.29, or the exact composition pattern |
| `ReviewWork` or “review happened” | Is one performed Work occurrence current? | A.15.1 |

Select the name only after recovery. A cleaner string is not a repair if it hides the same ontological error.

