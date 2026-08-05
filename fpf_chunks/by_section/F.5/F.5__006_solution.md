---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and RoleDescription Labels"
section_id: "F.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__006_solution.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and RoleDescription Labels"
  - "F.5:4 — Solution"
line_start: 90987
line_end: 91061
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
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
  - "U-kind naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "role-description labels"
  - "twin registers"
---

### F.5:4 - Solution

Name after meaning. For each candidate name, first recover the named value, its meaning source, and its intended use. Then choose labels that preserve that meaning.

For each naming decision, make the following facts recoverable in the prose, governing admission, role-description episteme, Concept-Set row, or Name Card. This is a naming checklist, not a new relation signature or mandatory record:

- the exact named value and its admitted kind;
- the direct source of its meaning;
- for a role label, the described `U.Role`, exact role-taxonomy episteme, and effective `U.ReferenceScheme`;
- the selected Tech label and its Plain teaching gloss;
- any aliases or previous labels with lineage;
- the morphology, neutrality, and minimal-generality checks;
- the neighboring-use boundary that prevents the name from absorbing assignment, capability, method, work, status, evidence, permission, publication, or relation-slot claims.

#### F.5:4.1 - Name Families Governed Here

| Name family | Meaning source | Naming rule |
| --- | --- | --- |
| U-kind or cross-context concept name | Exact value admitted by `E.24.UK` or its direct governing pattern; a Concept-Set row may retain witness comparison and evidence but supplies neither value identity nor admission | Use a neutral Tech label at minimal generality. Do not use one witness context's private term when a neutral head exists. |
| RoleDescription label for one `U.Role` | Role-description episteme, described `U.Role`, exact role-taxonomy episteme, effective reference scheme, and local sense | Use role-faithful morphology. Do not smuggle assignment, capability, method, work, evidence, status, permission, or publication into the label. |
| Role-relation, role-expression, or role-method expression name | `A.2.7` role relation structure whose participating roles are interpreted through their exact role taxonomies and effective schemes, plus `A.3.1`, `A.3.2`, or `A.15` when method or work is current | Ordinary labels may name qualified role expressions or role-bundle expressions without a `Role` suffix. Hyphenation can mark a recovered factor, domain, practice, method-family qualification, or combined expression; it must not mechanically concatenate operands or hide independent assignments. |
| Method, method-family, method relation structure, work-plan, or work name | Direct method and work patterns: `A.3.1`, `A.3.2`, `A.15`, `G.5`, and any direct method-composition pattern when current | Do not make the name a role-relation result because it shares words with role labels. Name the method value, method family, method relation structure, work plan, or work value directly and cite the role relation separately when it constrains use. |
| Mathematical or representation lens name | Lens or representation description over a selected role relation structure, method relation structure, transformation-flow structure, or other governed structure | Name the lens only when it is the governed value. Otherwise name the recovered role relation, method relation structure, method, work, or assignment. |
| Status, evidence, requirement, source, standard, publication, assurance, gate, or decision name | Direct governing status-use, evidence-use, source-use, publication-use, requirement-use, assurance, gate, or decision pattern | Do not treat it as a RoleDescription branch. Use `F.18` for durable naming only after the direct relation is recovered. |
| Relation slot or argument-position name | `A.6.5` SlotSpec discipline and the governing relation or signature pattern; use an interface-governing pattern only when interface meaning is current | Name the slot as a slot or argument position, not as a `U.Role`, unless a direct role-assignment relation is truly current. |

For every role-facing name, keep three objects distinct: the selected label or designator `L`, the described `U.Role` value `R`, and the F.4 role-description episteme `RD`. Under the effective `U.ReferenceScheme`, `L` designates `R`; under C.2.1, `RD` has `R` as its exact EntityOfConcern and names the governing role-taxonomy episteme in its ClaimGraph. Spelling, a `Role` suffix, a NameCard, a public row, or a source citation creates none of `L`'s governed referent, `R`, `RD`, a role assignment, dated work, a result or claim-bearing episteme, provenance, or publication occurrence.

#### F.5:4.2 - Tech and Plain Labels

Use two human-facing labels when the name is durable enough to be reused:

| Label | Job | Constraint |
| --- | --- | --- |
| Tech label | The stable label used by the local pattern, table, or role-description episteme. | Must fit the recovered kind and meaning source. |
| Plain label | A short teaching gloss. | Must explain without widening the sense. |
| Symbolic alias | Optional symbol or source abbreviation. | Informative only; it is not the Tech label. |

For a role-description label, the Tech label may be an agentive noun, local role term, or role phrase such as `ReviewerRole`, `PumpInspectorRole`, `Participant`, or `Approver`. The suffix `Role` is a disambiguator, not a universal law. Use it when it prevents confusion with a status, method, work occurrence, organization unit, publication, or access-policy term. Do not add it merely to make the name look formal.

For a coupled role-method label, recover the role expression and the method value or work value separately before naming. `RoboticsEngineerRole` may be a durable Tech label for a robotics-qualified engineering role value. `RobotEngineeringMethod` names a method or method family. The ordinary label "engineer-roboticist" can be useful when the role taxonomy, effective scheme, and method relation make the coupled meaning recoverable, but it must not replace the method description or work description.

For a U-kind, the Tech label should be neutral enough that no witness context wins by vocabulary alone. If witnesses disagree between `Observation`, `Reading`, and `MeasurementResult`, a Concept-Set row can preserve that comparison, but the selected head is admissible only when `E.24.UK` or the direct governing pattern has already admitted the exact shared value and invariants. The row, a source title, or the selected spelling does not perform admission.

#### F.5:4.3 - Positive Naming Rules

Use these rules when choosing or checking a name.

1. **Recover kind first.** State whether the named value is a U-kind, `U.Role`, role-description episteme, role-relation expression, method, work, status-use value, evidence-use relation, relation slot, lens description, or another named kind.
2. **Recover meaning source.** Use the exact `E.24.UK` or direct-pattern admission for a U-kind, retaining any Concept-Set row only as witness-comparison evidence; use the role-description episteme, described `U.Role`, exact role-taxonomy episteme, and effective reference scheme for role labels; use `A.2.7` for role-relation expressions; use `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern for method, method-family, method relation structure, or work names; use the direct governing pattern for statuses, evidence, source, requirement, publication, assurance, gate, decision, and relation slots.
3. **Use minimal generality.** The name's scope stays no wider than the admitted invariants.
4. **Keep interpretation metadata out of the label string.** Edition, source, witness, role taxonomy, and effective reference scheme belong in their governing admission, Concept-Set row, role-description episteme, reference-scheme relation, or Name Card, not inside the main label.
5. **Make morphology kind-sensitive.** Agentive role names fit work-facing roles. State or level forms fit statuses. Verbal or gerund forms fit methods only when the method pattern admits them. Slot names should say `Slot`, `Argument`, `Endpoint`, or another declared slot or position head when current.
6. **Keep coupled role-method names typed.** A phrase like "engineer-roboticist" may be the ordinary label for a qualified role expression; "robot engineering" may be a method or work name. Do not make one label carry holder assignment, role value, method, work, and capability at once.
7. **Do not encode thresholds or windows in the name.** Put time, state, threshold, capability envelope, or admission window in the governing pattern.
8. **Use aliases only with lineage.** A source term, previous term, symbol, or translation can be an alias; it does not create a second Tech label.
9. **Escalate when reuse becomes public or cross-scheme.** Use `F.18` and `F.17` for durable or public naming. When an actual cross-taxonomy or cross-scheme correspondence is consumed, first name the exact obtaining F.9 Bridge occurrence, then keep the separate current C.2.1 claim that it is suitable for the named bounded use. Reliance follows F.9's two branches. Ordinary below-threshold use with no assurance claim requires the exact A.10 evidence-provenance graph relation and `RelianceDisposition=pass` for that same use. When an assurance claim is made or B.3's material-reliance threshold is met, enter B.3 and first decide whether a current assurance claim exists; positive reliance requires a positive current assurance claim carrying the same bounded assurance use with its sufficient minimum reliance safety assurance record, while an exact `no-assurance-claim`, `insufficient-record`, `narrowed`, `rejected`, `withdrawn`, `abstaining`, or `blocked` disposition stops or narrows the use. A Bridge, profile, NameCard, row, label, evidence path, assurance record, or publication neither authorizes the use nor establishes assignment, work, result, provenance, assurance, or publication occurrence.

#### F.5:4.4 - Neighboring Use Boundary

When a label contains a tempting word, recover the current claim instead of replacing words mechanically.

| Source wording | First ontological question | Likely governing pattern |
| --- | --- | --- |
| `EvidenceRole`, `ModelFitEvidenceRole`, or "evidence role" | Is an episteme being used as evidence for a target claim with scope, polarity, relevance window, and provenance? | `A.10`, `B.3`, `C.2.1`, or the direct evidence-use pattern |
| `RequirementRole` or "standard role" | Is an episteme, standard, or clause used as a requirement, source, or specification-use item? | `C.28`, `E.10.D2`, `E.17`, or the direct requirement-use or source-use pattern |
| `Access Role` in RBAC | Is this a policy or permission-set term, not a work-facing behavioral role? | Direct access, policy, or status-use pattern; `F.18` for naming when durable |
| "role of subject, provider, or input" | Is this a relation position? | `A.6.5` |
| `ReviewerRole` | Is this a work-facing role value under one exact role-taxonomy episteme and effective reference scheme? | `A.2`, `F.4`, `A.2.1` when assigned |
| `robotics engineer` or `engineer-roboticist` | Is this a qualified role expression, independent role conjunction, method name, work name, or capability name? | `A.2.7`; `A.3.1`, `A.3.2`, or `A.15` when method or work is current; `F.18` for durable naming |
| `Reviewing`, `ReviewMethod`, `RobotEngineeringMethod`, `ReviewWorkflow`, or `MethodAlgebra` | Is this a method, method description, method relation structure, work plan, performed work, or lens over one of those objects? | `A.3.1`, `A.3.2`, `A.15`, `G.5`, `C.29`, or a direct method-composition pattern when current |
| `ReviewWork` or "review happened" | Is this performed work? | `A.15.1` |

Select the name only after this recovery. A cleaner string is not a repair if it hides the same kind error.

