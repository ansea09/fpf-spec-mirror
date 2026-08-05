---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
section_id: "A.2.7:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__006_solution.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "A.2.7 — Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
  - "A.2.7:4 — Solution"
line_start: 5761
line_end: 5952
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.5"
keywords:
  - "bundles (⊗)"
  - "incompatibility (⊥)"
  - "requiredRoles substitution"
  - "role algebra"
  - "separation of duties (SoD)"
  - "specialization (≤)"
---

### A.2.7:4 - Solution

Select one `RoleRelationStructure : U.Structure` over a declared role-value substrate. Populate it only with exact relation occurrences governed below. Use supported assertions about those occurrences as premises in work performed by a system under the receiving method, gate, or decision pattern.

```text
RoleRelationStructure : U.Structure {
  declaredRoleValueSubstrate: FinSet(U.Role), byValue,
  roleTaxonomyEpistemeRef: U.EpistemeRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  selectedRoleRelationOccurrenceRefs: FinSet(U.EntityRef),
  admissibleUse,
  nonAdmissibleUse,

}
```

Each `selectedRoleRelationOccurrenceRefs` value resolves to one explicitly individuated occurrence of one of the four direct A.2.7 relation species. This declaration is a compact recovery aid. The A.22 identity is the declared role-value substrate together with the selected organization of obtaining relations under the stated interpretation. A changed rendering, publication, diagram, table, identifier, or receiving-use model selection does not change that selected structure. A changed role-value substrate or relation organization does. When a selected `BoundedModelUseStructure` changes one receiving interpretation, designate it in that receiving assertion or use rather than in this structure declaration.

#### A.2.7:4.1 - Relation Realism and Constructive Settlement

Each governed relation is a direct species of `U.Relation`. Apply the order established by `A.6.REL`:

1. the exact predicate obtains for its participant fillings under the named role interpretation;
2. the occurrence is admitted under its direct relation species;
3. a receiving use explicitly individuates the occurrence only when it needs identity;
4. an identifier designates the individuated occurrence only when stable reference is needed;
5. a later assertion, check, or decision refers to it.

The role-taxonomy episteme and effective reference scheme fix the meanings of the role values and the by-value predicate. They therefore have explicit `SlotKind` declarations in each relation signature. The taxonomy episteme may contain an assertion that the predicate obtains, but an assertion, database row, policy text, graph edge, or publication does not become the relation occurrence by form.

Generic A.2.7 relations are predicate-realistic: the direct predicate determines obtaining. If a specialized role-governance ontology says that an accepted decision or installation act constitutes a relation, that specialization must name the constituting act and its acceptance condition. A.2.7 does not silently make every taxonomy statement constitutive.

Logical form contributes the predicate, argument discipline, and relation laws. Constructive ontology additionally requires grounded participant values, an obtaining condition, and an occurrence identity rule for any receiving use that needs one occurrence as an object of attention. Taxonomy nesting alone therefore admits neither a relation occurrence, a selected structure, nor a holon.

Relation predicates are often written as verbs, but the grammatical form does not admit an action, `U.Work`, `U.Method`, `U.Transformation`, acting system, or holon. The four A.2.7 relation species have typed participants, obtaining conditions, and occurrence identities; this pattern admits no own part relation, constructive assembly, or meta-holon transition for them. When actual change, a way of doing, or dated performance is current, state the neighboring `U.Transformation`, `U.Method`, or `U.Work` through its direct pattern. A.3.4 identifies one `U.Transformation` as an actual bounded change at the resolution and boundary needed by the current use; it supplies neither a transformation-composition governor nor holonhood. `U.Method` and `U.Work` are admitted holon kinds under A.3.1/B.1.5 and A.15.1, but an exact candidate still passes A.1 only through independently grounded constituents, whole-forming relations and assembly, reidentification, a composition-grounded whole-level characteristic, and larger-assembly compatibility. Verb-shaped wording supplies none of those facts. `U.Role` remains a non-holon role value held only through an assignment to an admitted `U.System`.

`RelationSignature` names the whole declaration. Each `SlotSpec = <SlotKind, ValueKind, refMode>` names one local position, its admitted filler kind, and its by-value or reference mode. In Plain explanation, a SlotKind may be called a position. `Place` is not introduced as another technical object. A role value can fill a SlotKind; the SlotKind does not thereby become a `U.Role`.

The four generic declarations below contain only the actual role-value or role-value-set participant, by-value predicate, role-taxonomy episteme, and effective reference scheme needed by that relation species. They contain no temporal participant. `RoleRelationExtent` is a local content ValueKind for an affirmative assertion or occurrence description; it states the currently known extent of one independently established occurrence. A predicate may declare how a receiving-use window is tested, while the receiving assertion or check may separately state `declaredRoleRelationEvaluationWindow`. Neither temporal value is a SlotSpec or makes the world-side relation obtain. For fixed participants, the actual occurrence extent is derived as the maximal continuous interval during which the exact predicate obtains.

#### A.2.7:4.2 - Role-Admission Substitution Relation

Use `RoleAdmissionSubstitutionRelation` when the engineering question in a receiving use is whether an assignment to one role value may satisfy an admission condition written for another role value.

```text
RoleAdmissionSubstitutionRelation : U.Relation
RelationSignature:
  CandidateAssignmentRoleValueSlot: U.Role, byValue
  AdmissionConditionRoleValueSlot: U.Role, byValue
  RoleAdmissionSubstitutionPredicateSlot: RoleAdmissionSubstitutionPredicate, byValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, byValue
```

`RoleAdmissionSubstitutionPredicate` states the exact receiving-use condition under which an assignment to the candidate role can satisfy the role condition. Its truth condition names the receiving `EntityOfConcern`, the applicability scope, and every direct predicate on which substitution depends instead of hiding that dependence in the role labels.

The relation is directional. Reversing its role-value fillings requires another predicate evaluation. Its claim is limited to admission substitution between the two interpreted role values. A.1 governs holder system kind, A.2.1 governs the current assignment, A.2.2 governs capability fit, A.2.5 governs role state, and A.15 governs performed work. The system performing the receiving check resolves the needed neighboring claims and applies the selected admission method.

The relation obtains while the fixed by-value substitution predicate is true for the two fixed role values under the fixed role-taxonomy episteme and effective reference scheme. Its occurrence extent is the maximal continuous interval of that truth. A mere label hierarchy, job grade, or taxonomy indentation is evidence at most; it is not the truth condition.

#### A.2.7:4.3 - Role Incompatibility Relation

Use `RoleIncompatibilityRelation` when two role assignments cannot be jointly admitted under one exact condition.

```text
RoleIncompatibilityRelation : U.Relation
RelationSignature:
  IncompatibleRoleValueSlot[1]: U.Role, byValue
  IncompatibleRoleValueSlot[2]: U.Role, byValue
  RoleIncompatibilityPredicateSlot: RoleIncompatibilityPredicate, byValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, byValue
```

The two indexed SlotKinds distinguish the two fillings in the declaration; the relation obeys the symmetry law

```text
incompatible(r1, r2, p) = incompatible(r2, r1, p)
```

`RoleIncompatibilityPredicate` states the exact rule over assignment configurations: which same- or different-holder test, receiving `EntityOfConcern` or work identity, temporal-overlap test, and other joint-admission condition makes the two interpreted role values incompatible. In the safety case below, the rule tests the same holder and same hazard-analysis work item during overlapping assignment windows. The exact `U.RoleAssignment` occurrences later evaluated are inputs to the receiving check under A.2.1; they are not copied into this role-value relation signature or occurrence identity. The relation obtains while the fixed rule truthfully characterizes the two fixed role values under the fixed taxonomy episteme and scheme. A conflicting allocation is a case satisfying the rule, not what creates the role relation.

The role-value relation does not itself reject an assignment. A system in the checking role applies the receiving method to the two current assignment occurrences and records the resulting admit, reject, defer, or unresolved outcome under the receiving pattern.

#### A.2.7:4.4 - Role Qualification Relation

Use `RoleQualificationRelation` when one role value narrows the interpreted meaning of another role value under a declared predicate.

```text
RoleQualificationRelation : U.Relation
RelationSignature:
  QualifiedRoleValueSlot: U.Role, byValue
  BaseRoleValueSlot: U.Role, byValue
  RoleQualificationPredicateSlot: RoleQualificationPredicate, byValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, byValue
```

The predicate states the exact semantic restriction. `RoboticsEngineerRole` may qualify `EngineerRole` by the robotics domain and the engineering methods for which the role is interpreted. The qualification claim concerns interpreted role meaning. C.3 separately governs `U.SubkindOf`, A.1 governs holder system kind, A.2 governs the non-holonic role value, A.2.2 governs capability, and `RoleAdmissionSubstitutionRelation` governs any additional admission-substitution claim.

The relation obtains while the fixed by-value qualification predicate is true for the two fixed role values under the fixed role-taxonomy episteme and effective reference scheme. Its occurrence extent is the maximal continuous interval of that truth. A shared word stem or a nested row in a taxonomy rendering does not establish that truth.

#### A.2.7:4.5 - Role Bundle Relation

Use `RoleBundleRelation` when a receiving use needs a finite set of role assignments jointly and the allocation rule matters.

```text
RoleBundleRelation : U.Relation
RelationSignature:
  BundledRoleValueSetSlot: FinSet(U.Role), byValue, cardinality at least 2
  JointRoleAdmissionPredicateSlot: JointRoleAdmissionPredicate, byValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, byValue
```

`JointRoleAdmissionPredicate` states the allocation rule over candidate assignment configurations: whether one system may hold several assignments, distinct systems must hold specified assignments, some assignments may be shared, and how a receiving work window or method-applicability interval is tested. Exact current assignments and the selected receiving window remain inputs to the receiving check under their direct owners; they are not copied into this role-value-set relation signature. The relation does not create a combined role value. A durable combined role value requires its own A.2 settlement and assignment use; a convenient name for this bundle remains a name for the relation unless that stronger settlement exists.

The relation obtains while the fixed by-value allocation rule truthfully characterizes the fixed interpreted role-value set under the fixed role-taxonomy episteme and effective reference scheme. Its occurrence extent is the maximal continuous interval of that truth. A list of role labels without an allocation predicate is not a bundle relation occurrence.

#### A.2.7:4.6 - Occurrence Identity and Continuity

Do not replace the world-side identity rule with a database, graph, or tuple key. One occurrence begins when the exact fixed participant fillings of one direct relation species satisfy its fixed predicate. It continues while those same participants remain fixed and the predicate obtains without interruption. Its identity therefore uses the direct relation species, exact role-value or role-value-set filling, exact by-value predicate, exact role-taxonomy episteme, exact effective reference scheme, and the derived maximal continuous obtaining extent.

For symmetric incompatibility, exchanging the two role-value fillings does not change identity. For a bundle, set order does not change identity. Changing a role value, predicate, taxonomy episteme, or effective scheme identifies another occurrence even if every displayed label remains the same.

A.2.7 defines each relation-specific obtaining predicate and same-versus-new-occurrence rule. It does not inspect a current case and does not establish that one current occurrence obtains. Relevant current case facts or accepted constituting history must satisfy the direct predicate. When a receiving use needs one occurrence as a referent, a system performing explicit-individuation work applies the identity rule to those facts and recovers the already obtaining occurrence before any assertion or identifier designates it. If no receiver needs occurrence identity, keep the readable direct relation and stop before individuation.

An affirmative assertion or occurrence description may state the currently known `roleRelationExtent` only after that predicate-satisfaction and identity application have recovered the occurrence. `[relationStart, open]` can describe the current extent before its end is known. Later closure refines the temporal description of the same occurrence when obtaining was uninterrupted. A demonstrated predicate-false interval ends the occurrence; later resumption begins another. Missing evidence leaves reliance on the assertion unresolved and does not demonstrate a non-obtaining gap. A target `declaredRoleRelationEvaluationWindow` belongs to the receiving assertion or check, not to the direct relation signature or occurrence identity.

A selected model-use structure does not enter these generic relation signatures or identities. A genuinely structure-dependent relation species requires its own direct pattern, required structure participant, stronger obtaining predicate, and explicit identity law. A changed publication or rendering of the same taxonomy episteme creates no relation occurrence. An F.9 Bridge between changed scheme-local meanings likewise never preserves or merges A.2.7 occurrence identity; it can support only a separately stated bounded use across the independently identified meanings.

#### A.2.7:4.7 - Assertion and Receiving Check

A relied-on role-relation claim is an ordinary C.2.1 assertion episteme, not the relation occurrence. Keep three moves in this order:

1. A.2.7 defines the direct relation predicate, applicability, and same-versus-new-occurrence rule.
2. Relevant current case facts or accepted constituting history satisfy or fail that predicate. Predicate satisfaction makes the direct relation obtain. When the receiving use needs one occurrence as an exact referent, a system performing explicit-individuation work applies the A.2.7 identity rule to those facts and recovers that already obtaining occurrence.
3. Only then may an affirmative assertion use the recovered occurrence as its exact `EntityOfConcern` and designate its currently known `roleRelationExtent`. The assertion states the result; it neither establishes predicate satisfaction nor individuates the occurrence.

When no positive occurrence has been recovered, a negative, candidate, counterfactual, or unsupported affirmative claim normally uses the exact admitted A.2.7 direct relation kind as its C.2.1 `EntityOfConcern`. Its ClaimGraph carries the proposed role-value fillings, by-value predicate, effective scheme, and exact polarity or modality. If the claim instead concerns another independently identified exact entity, name that entity by value and state the relation proposal in the ClaimGraph. A tuple of proposed fillings, a policy row, or a convenient label is not an alternative EntityOfConcern. Neither branch carries a positive occurrence reference or an actual `roleRelationExtent`.

Unresolved reliance preserves the assertion's stated polarity; it is not a third polarity and does not create or erase an occurrence. In every branch the C.2.1 identity triple remains claim content, exact `EntityOfConcern`, and the assertion's effective reference scheme. Evidence, currentness, and supported, refuted, or unresolved reliance remain separate and make no world-side occurrence obtain.

Supported assertions about selected role relations serve as typed premises for another method; the selected structure is not the checker. A system performing a receiving check normally makes these moves:

1. resolve the current facts and any exact `U.RoleAssignment` or A.2.5 role-state occurrences needed to test the direct A.2.7 predicate under their own patterns;
2. test that predicate for the fixed role values, taxonomy episteme, and effective scheme;
3. when the receiving use needs occurrence identity, apply the direct identity rule and recover the exact role-relation occurrence without copying assignment or role-state objects into its participant set;
4. establish the appropriate C.2.1 assertion: designate the recovered occurrence only for the affirmative recovered-occurrence branch, or use the direct relation kind or another independently identified entity for a no-recovered-occurrence branch;
5. evaluate any separate A.2.2 capability-fit, resource, interface, risk, evidence, currentness, or assurance conditions under their direct patterns; and
6. perform the checking work by the selected method and record the check outcome defined by the receiving pattern.

This order keeps three layers visible: case facts make the role relation obtain, explicit-individuation work recovers one occurrence only when a receiver needs it, and an episteme asserts it with some support before a system may use that assertion while performing a check. None of these layers substitutes for the others.

#### A.2.7:4.8 - Recovering Apparent Role Decomposition

When ordinary wording says `subrole`, `role part`, or `combined role`, start from the engineering question rather than the word:

| Engineering question | Recovered object |
|---|---|
| May this assigned role satisfy a condition written for another role? | `RoleAdmissionSubstitutionRelation` |
| Does this role value narrow another role's interpreted meaning? | `RoleQualificationRelation` |
| Must these role assignments not overlap under an exact condition? | `RoleIncompatibilityRelation` |
| Must these role assignments be present together under an allocation rule? | `RoleBundleRelation` |
| Who holds the role and when? | `U.RoleAssignment` under A.2.1 |
| Is the assignment in a work-admitting state? | `RoleStateRelation` under A.2.5 |
| Can the holder perform within an operating envelope? | capability and capability-fit relations under A.2.2 |
| Are ways of doing or work occurrences composed? | method composition under A.3 and B.1.5, or work structure under A.15 |

This recovery is constructive. `U.Role` has no admitted part relation or meta-holon transition. The recovered relations and neighboring objects remain available without pretending that they are role parts.

#### A.2.7:4.9 - Representation, Model-Use, and Cross-Scheme Boundaries

A graph, table, matrix, algebra, embedding, policy file, or organization chart may describe a `RoleRelationStructure` or support a `C.29` mathematical-lens use. It is not the selected structure or any selected relation occurrence by form. State what organization the representation preserves and loses before relying on it.

Role semantic locality normally comes from one role-taxonomy episteme and effective reference scheme. Reference an independently selected `BoundedModelUseStructure` only when interpretation depends on its DDD-style model-use organization; designate it in the receiving assertion or use, not in a generic A.2.7 signature.

When a proposed comparison, substitution, translation, or reuse crosses schemes, first recover the exact F.17 sense cells and exact obtaining F.9 Bridge. Then state a separate C.2.1 assertion about that Bridge naming the bounded use `u`, source-to-receiving direction `d`, use-specific correspondence rule `r`, tolerated semantic loss `t`, affirmative or negative polarity, and effective reference scheme. For ordinary reliance below B.3's material-reliance threshold and with no assurance claim, require the exact current A.10 evidence-provenance graph relation and `RelianceDisposition=pass` for that same use. When an assurance claim is made or the threshold is met, B.3 first asks whether a current positive assurance claim exists: only one carrying the same use with a sufficient minimum reliance safety assurance record supports it; otherwise an explicit no-assurance, insufficient-record, narrowed, rejected, withdrawn, abstaining, or blocked disposition stops or narrows the use. Neither branch supplies authorization.

The Bridge, its profile, or an optional Bridge Card alone establishes neither bounded-use suitability nor an A.2.7 relation, assignment, receiving-check outcome, or performed work. If a receiving check uses the bounded-use assertion while evaluating an A.2.7 predicate, that assertion remains a separate premise; any local role relation that obtains keeps the participant set and identity declared here, and the actual check remains work performed by a system under its direct owner.

#### A.2.7:4.10 - Lightweight Path

Ordinary prose may state a readable relation and stop:

```text
For pump pressure-test work, SeniorHydraulicsTechnicianRole may satisfy
the role condition written for HydraulicsTechnicianRole.
```

Add a full signature when reusable typing matters. Individuate an occurrence when another claim depends on its identity. Assign an identifier only when stable reference matters. Build a `RoleRelationStructure` only when several selected relations or constraints must be used together. Completeness is not a reason to materialize every layer.

