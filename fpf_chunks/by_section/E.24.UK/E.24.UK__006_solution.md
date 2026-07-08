---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Governance and Ontic Settlement Coupling"
section_id: "E.24.UK:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__006_solution.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "E.24.UK — U-kind Governance and Ontic Settlement Coupling"
  - "E.24.UK:4 — Solution"
line_start: 80442
line_end: 80613
dependencies:
  - "A.11"
  - "A.6.5"
  - "A.8"
  - "C.3"
  - "C.3.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "F.5"
  - "F.8"
keywords:
---

### E.24.UK:4 - Solution

Treat U-kind governance as a coupled but non-counting relation between durable `U.*` names and E.24-compatible ontic settlement.

Every durable `U.*` name needs one primary E.24-compatible settlement. That settlement may be:

- a root ontic settlement for the governed subject value;
- a dependent durable value under a root settlement;
- explicit reuse of an existing root subject U-kind;
- a C.3 typed-reasoning value when the current question is kind quantification, membership, subkind order, or kind bridge.

Every durable reusable ontic needs a named root subject U-kind or explicit reuse of one. This does not mean one full ontic pattern per U-kind, and it does not mean one U-kind per ontic. `U.Ontic` names the ontology-unit kind; it does not replace the subject kind governed by that ontology unit.

Use this compact decision relation:

```text
UKindAdmissionDecision:
  CandidateSpelling:
  SourceLocationKind: prose | table | heading | title | filename | ToC row | source quote
  RecoveredGovernedObject:
  CurrentUse:
  IdentityGroundingOrRecognitionRule:
  C3KindUse:
  E24Settlement:
  RootSubjectUKind:
  DependentValueIfAny:
  NonUDispositionIfRejected:
  NamingPatternIfRetained:
  StructuralDispositionIfRejected:
  ReopenCondition:
```

#### E.24.UK:4.1 - Positive Test For A Durable U-kind

Retain or introduce a candidate `U.*` name as a durable U-kind only if all of these are true:

1. It names a governed EntityOfConcern, not merely a source expression, local field, table column, reference suffix, publication form, or math-lens expression.
2. The value has stable identity across at least two uses or one load-bearing governing pattern.
3. The admission cites an identity, grounding, or recognition rule: direct governing pattern, C.3 membership and extent rule, Concept-Set witness set, A.6 `SubjectBlock` with `RangedValueKind`, imported signature symbol, CT2R/Compose-CAL constructive grounding for structural claims, formal-substrate or principle-frame declaration when current, or another accepted operational identity test.
4. FPF users need to make action-facing claims about that value, not only about a wording choice.
5. Existing root U-kinds plus slot and relation combinatorics cannot express the claim without losing reviewable distinctions.
6. The candidate has a primary governing pattern or another selected governing pattern in the same governed source set.
7. The candidate has an E.24-compatible settlement: root subject, SlotRelation when needed, semanticArea, ontologicalNeighborhood, admissible use, non-use boundary, and dependent-value policy.
8. Dependent patterns rely on this value by value or are expected to rely on it after the selected amendments.
9. F.18 and F.17 can name and publish the term without turning a local slot label into a kernel kind.
10. Source wording outside current FPF use is repaired by E.10, E.10.ARCH, or the governing pattern named by value.

If any row fails, the candidate is not admitted as a durable U-kind in the current form.

#### E.24.UK:4.2 - Root And Dependent U-kinds

A root U-kind is the subject value whose identity is held by the primary settlement.

A dependent durable U-kind is a reusable public U-kind name for governed individual instances whose identity is kept through the same primary settlement as a root U-kind. The head pattern states the exact dependence relation and the governing pattern for those instances. It is not automatically:

- a C.3 subkind;
- a slot name;
- a record form;
- a publication form;
- a synonym for the root;
- a title convenience.

Read the words carefully:

- A **U-kind name** such as `U.WorkPlan`, `U.RoleAssignment`, `U.MethodDescription`, or `U.Capability` names a reusable governed kind admitted by this pattern and by its direct owner.
- An **individual instance of that U-kind** is one concrete governed object under that kind, for example one work plan, one role assignment, one method description, or one holder capability. It is not a second kind named `Value`, not a slot filler by that fact, and not a record field.
- **Dependent durable** means that the individual instance has durable identity for FPF use, but its identity is held through another settlement and declared dependence relation. It is not a root beside that settlement.
- The dependency relation is an identity and governance relation, not parthood by default. A `U.RoleAssignment` depends on role, holder, bounded context, and window; that does not make the assignment a part of the role. A `U.Capability` may depend on a holder `U.System`; that does not make the capability a system part or a `U.Characteristic`.
- A statement, record, evidence relation, publication, dashboard row, source expression, or fit predicate about a dependent individual remains a neighboring object unless its own governing pattern admits it as a governed object.
- Avoid bare **value** when the contrast is kind versus instance. Use **individual**, **instance**, or **concrete governed object**. Reserve slot-filler wording for actual slot relations and record-field wording for records.

Use this small reading table when authoring:

| Form in prose | Ontological reading |
| --- | --- |
| "`U.WorkPlan` is dependent durable" | The public U-kind name is admitted, but its instances depend on method, role, time, and intended-work relations rather than forming a root beside `U.Work`. |
| "this `U.WorkPlan` instance" | One concrete intended-work episteme or plan record governed by the work-plan pattern. |
| "`U.RoleAssignment` is dependent" | Assignment instances depend on role, holder, bounded context, window, and work-facing use. |
| "this `U.RoleAssignment` instance" | One concrete assignment relation, not the role, not the holder, and not performed work. |
| "`U.Capability` is dependent" | The public U-kind name is admitted for holder-dependent capability instances under the system-holder settlement. |
| "this `U.Capability` instance" | One concrete holder capability under envelope, measures, qualification window, and currentness condition; not the statement, evidence, currentness assessment, characteristic, Q-Bundle, architecture row, or fit predicate around it. |

Examples:

| Candidate | Disposition |
| --- | --- |
| `U.Episteme` | root U-kind governed by the episteme ontic settlement. |
| `U.EpistemePublication` | dependent durable value only when the episteme/publication settlement states the dependence relation. |
| `U.View` and `U.Viewpoint` | dependent or directly governed values under episteme and multi-view settlement, not automatic roots. |
| `U.Method` | root U-kind for semantic way-of-doing and admitted non-agentive method holon kind when governed by `A.3.1` and direct method-composition patterns. |
| `U.MethodDescription` | dependent value: description episteme for a method, not a C.3 subkind by default. |
| `U.Work` | root U-kind for dated performed occurrence. |
| `U.WorkPlan` | dependent value under method, work, role, and time settlement; it does not show that work occurred. |
| `U.Role` | root work-facing role value under role patterns. |
| `U.RoleAssignment` | dependent typed assignment relation value under role, holder, bounded-context, and work settlement. |
| `RoleRelationStructure` | non-U selected relation structure unless E.24.UK evidence admits durable U-kindhood. |
| `MethodRelationStructure` | non-U selected relation structure for method-side relations that do not assert one `U.Method` whole assembled from method parts; direct method-composition patterns govern composite `U.Method` claims without promoting this relation structure to a U-kind. |

#### E.24.UK:4.3 - Combined Admission Order

Use existing rules in this order:

1. Recover the source use and governed EntityOfConcern.
2. If the current question is typed claim quantification, apply C.3 and C.3.1 first. `U.Kind` is the context-local intensional value; `U.SubkindOf` is a partial-order relation over those values.
3. Recover the identity, grounding, or recognition rule for the candidate: direct governing pattern, C.3 membership and extent rule, Concept-Set witnesses, A.6 `SubjectBlock` with `RangedValueKind`, imported signature symbol, CT2R/Compose-CAL constructive grounding when the claim is structural, formal-substrate/principle-frame declaration, or another accepted operational identity test.
4. If durable FPF kindhood is claimed, apply E.24-compatible settlement, A.11 parsimony, and A.8 universal-core testing when kernel-level status is claimed.
5. If the object is a slot, relation position, record, form, lens, local frame, expression, or source wording, do not admit a U-kind; apply the direct governing pattern for that object or claim.
6. Only after the recovered value and admission decision are stable, use F.8 for mint-or-reuse and F.5, F.18, or F.17 for naming and publication.

| Source | Contribution |
| --- | --- |
| C.3 | Typed claim quantification, intent, extent, membership, kind bridge, and typed guards. |
| C.3.1 | `U.SubkindOf` partial order over `U.Kind`, not dependent-U-kind relation. |
| E.14, B.3.5, and C.13 | Working-Model first, CT2R alias-plus-grounding, and Compose-CAL `Γ_m` traces for structural identity claims. |
| A.6.0 and A.6.1 | Construction-facing declaration shape: `SubjectKind`, `RangedValueKind`, `SliceSet`, `ExtentRule`, vocabulary, laws, applicability, realization, and argument-slot discipline. |
| A.8 | Universal-core test for kernel-level U-kind claims. |
| A.11 | Composition and parsimony before adding a new core concept. |
| E.24 | Ontic settlement and distinction among ontic, description episteme, publication, and form. |
| F.8 | Mint-or-reuse decision after recovered kind and use. |
| F.5 | Naming after recovered meaning; naming does not do ontology. |

#### E.24.UK:4.4 - Source Ontology Conversion Guide

Use this short conversion guide when a source ontology, schema, standard, class hierarchy, or top-level ontology uses words such as type, class, category, object type, entity type, kind, or subtype. BFO-style, ISO-style, OWL/RDF, database-schema, programming-language, and discipline-local type systems are source ontologies or representation regimes; they do not become FPF `U.*` names by translation.

First recover the source construct by value:

- source name and source ontology or schema;
- source identity rule, membership rule, extent rule, or recognition rule;
- source relations such as is-a, part-of, realizes, participates-in, depends-on, or equivalent local relations;
- intended source use: classification, query, modeling, exchange, validation, reasoning, implementation, or documentation.

Then select the FPF object:

| Source construct use | FPF recovery |
| --- | --- |
| claim quantification, membership, extent, subkind, or kind bridge | C.3 `U.Kind`, C.3.1 `U.SubkindOf`, and typed-reasoning rules |
| public durable FPF kind needed across patterns | E.24.UK durable U-kind admission, then E.24-compatible settlement |
| a reusable cluster of slots, fillers, and governing relations | E.24 ontic settlement with one root subject U-kind or explicit reuse of an existing root |
| imported formal symbol or declared range in a signature or mechanism | A.6 `SubjectBlock` with `RangedValueKind`, imported signature symbol, Concept-Set row, or admitted durable U-kind |
| source-name alignment across contexts | F.9 bridge, F.17 term row, F.18 naming, and explicit loss notes |
| implementation or serialization category | representation, publication form, record field, schema field, or direct implementation artifact governed by the relevant pattern |

A source "type" may become an FPF kind and may require an ontic, but only after these tests. If the source construct only supplies local classification or exchange syntax, keep it as C.3 typed reasoning, bridge material, representation material, or source wording. Do not create a rival FPF type layer beside durable U-kind governance and E.24 ontic settlement.

#### E.24.UK:4.5 - Structural Location Rule

A `U.*` spelling in a pattern title, host filename, monolith heading, or ToC row is stronger than a prose occurrence. Structural locations orient readers to the governed object.

Use this rule:

- **Prose occurrence:** recover the local claim and direct governing pattern.
- **Table row or record field:** ask whether the field is a slot, record field, publication-form element, or governed value.
- **Heading:** retain `U.*` only when the section really governs that value or directly references an already governed value.
- **Pattern title or host filename:** retain `U.*` only when the pattern's primary EntityOfConcern is that root or dependent U-kind.
- **ToC row:** retain `U.*` only when the row points to a pattern that carries the settlement; otherwise name the direct governed object or repair the wording with E.10.

Do not keep a false `U.*` structural name for memory or search convenience. Use a Plain label, local heading, Name Card, Concept-Set row, relation name, record field, or quoted source wording when that is the actual object.

#### E.24.UK:4.6 - Non-U Dispositions

If the positive test fails, select the actual governed object:

| Candidate pressure | Disposition |
| --- | --- |
| slot or relation position | SlotKind, ValueKind, RefKind, direct relation, or local field under A.6.5 and direct pattern. |
| selected relation structure | non-U selected structure or direct relation structure. |
| record or card shape | record form or publication form under the direct publication pattern. |
| graph, tuple, algebra, metric, view, or formal expression | math lens, representation lens, or direct modeled object. |
| source label or source tradition word | source wording, local sense, or reduced-use quote under E.10 and E.10.ARCH. |
| public naming pressure | F.8 decision, then F.5, F.18, or F.17 only after recovered value is stable. |

