---
chunk_kind: "child"
pattern_id: "D.3"
pattern_title: "Describe an Ethical Conflict Across Levels or Scopes"
section_id: "D.3:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.3/D.3__005_solution.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "D.3 — Describe an Ethical Conflict Across Levels or Scopes"
  - "D.3:2 — Solution"
line_start: 97256
line_end: 97339
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.6.RCD"
  - "B.1"
  - "B.3"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "C.30.ILC"
  - "D.1"
  - "D.2"
  - "D.4"
  - "D.5"
  - "E.10.ROLE"
  - "E.17"
  - "E.24.PUB"
keywords:
  - "interlevel ethical conflict"
---

### D.3:2 - Solution

#### D.3:2.1 - First result

Identify the sides needed to explain the conflict. At least two claims are involved; include more when the tension depends on their combination. For each side, write:

1. the ethical claim that states the concern in ordinary language;
2. the affected entity;
3. how the proposed action reaches that entity. Identify the whole and constituent if composition matters, the people or work covered if their extent matters, and the conditions on which this side’s claim relies;
4. the value premise under which the consequence matters, with a frame-edition reference when the reasoning uses one;
5. the expected benefit, harm, or constraint and its consequence horizon; and
6. the evidence use or uncertainty only when the side relies on it.

An analyst can describe a concern under an explicit value premise. Report a representative’s act with its mandate and its effect for the represented party. To attribute words, personal endorsement or an act reserved to the affected party, establish that party’s own contribution. Explain which claims can hold together and what makes them incompatible or leaves the answer open. When several arrangements meet the constraints, explain what each would preserve or sacrifice under the competing value premises, or why their priority remains unsettled. Three claims can be jointly incompatible although each pair can be met. For one agreed combination, a feasible arrangement can establish compatibility. If the parties retain choices about future work, identify who decides, what each can know in time and which combinations the arrangement must accommodate. A plan for one combination establishes that combination. A constraint covering every permitted arrangement can establish impossibility. Give the conclusion this supports for the original decision and the alternatives that still matter.

A short working note can be sufficient. Develop a more elaborate description only when its intended use requires the additional content.

#### D.3:2.2 - Reusable conflict description

Identify the account of the conflict when another reader needs to cite, compare, revise or publish that account. A short note can serve. The account is one C.2.1 `U.Episteme`, here called an `InterlevelEthicalConflictDescription`. If a publication reports one observation, identify the source for that observation.

Apply the C.2.1 identity test:

- **EntityOfConcern:** one exact entity already recovered for the case, such as the plan, proposed system change, or decision situation whose ethical tension is being described. Do not use a loose bundle of several possible subjects.
- **ClaimGraph:** the claims about the affected entities, the conflicting sides and their tension, and the question for the next use. Where the description limits the cases to which those claims apply, identify its ClaimScope.
- **effective ReferenceScheme:** the designation, interpretation, measurement, comparison, and evaluation rules needed to read those claims.

Changed claim content, EntityOfConcern, or effective ReferenceScheme identifies another episteme. Say that a later description revises or supersedes an earlier one only when a C.2.1 `EpistemeEditionRelation` is asserted. A changed narrative, table layout, publication form, carrier, or publication occurrence does not by itself change the episteme.

Use this content shape when a reusable record helps:

```text
InterlevelEthicalConflictDescription — C.2.1 identity:
  entityOfConcernRef
  claimGraph:
    descriptionClaimScopeRef?
    conflictSides: at least two rows
      - sideId
        ethicalClaim: plain statement that identifies the claim; add a ClaimAddress only when reusing an existing claim
        affectedEntityRef
        declaredLevelRelationRef?
        sideClaimScopeRef?
        affectedWorkExtentRef?
        valuePremise
        valueFrameEditionRef?
        expectedConsequence: what changes and why it counts, for example, as a benefit, harm, or constraint under that value premise
        consequenceHorizon
        evidenceUseRef?
        uncertaintyStatement?
    tension:
      sideIds
      plainStatement
      directRelationDefinitionRef?
      obtainingRelationOccurrenceRef?
      missingGovernorRef?
    nextUse: plain statement; cite a question episteme only when another use needs that identity
  effectiveReferenceSchemeRef
```

When a restriction on the whole description matters, `descriptionClaimScopeRef` identifies the conditions under which its claims apply. Identify any subsystem affected on one side. The subject of the whole description can still be a fleet-wide decision. Change that subject only if the claim is now about the subsystem itself. Each side can also have its own ClaimScope or refer to a particular Work and its extent. Give the whole description its own scope when that further restriction matters.

For another setting, carry over the reasoning that connects the action to a consequence under a value premise. Check whether the same dependency, value premise and relevant constraints apply there. One affected party may belong to several groups. Count distinct people once for a headcount. For a claim about burdens, establish whether that person experiences one burden reported twice or distinct burdens. State what can be concluded about the whole under the relevant counting or composition rule.

The `plainStatement` must name the incompatibility, trade-off, parity, or other tension claimed among the sides. In an ordinary case, it remains claim content in the description. If a receiving use relies on a separately obtaining direct relation, cite the relation definition and occurrence with its participants, applicability, and identity. If no adequate governor exists, record the `A.6.RCD` missing-governor result. Merely filling a reference field never makes a direct relation obtain.

#### D.3:2.3 - Add detail only when it changes the conflict or its next use

| Open this branch when... | Add... | Keep separate... |
| --- | --- | --- |
| A Method is part of a side's claim. | the exact `U.Method` under A.3.1 and, when cited, its MethodDescription under A.3.2 | Method identity from any dated performance |
| The account relies on a particular performance. | For a dated `U.Work`, establish the acting System or Systems at the scale claimed under A.13 and admit the occurrence under A.15.1 from its history, Method, extent and containing System. Use F.6 for an expressly claimed assignment-bound attribution. | A result relevant to the affected parties can already be established while an individual contribution remains unknown. An intention, permission or capability can also precede the Work. |
| Assignment matters. | the exact assignment species and the claim with its case basis under A.2.1; cite an obtaining occurrence when the account relies on one | assignment from performance, responsibility, permission, or authority |
| Role wording or classification needs clarification. | use E.10.ROLE to recover the meaning; when System classification is claimed, identify the local kind and the separate C.2.1 classification assertion under C.3.2 with its candidate-admissibility basis | ordinary wording, classification, assignment, and the acting System from one another |
| Evidence changes a side or its uncertainty. | identify the supporting content and the grounds for this use; apply A.10 when the source-to-use relation is implicit or must be replayable | available or stored evidence from what it warrants for this side |
| A change affects who may benefit or be harmed. | identify the proposed change and its supported possible consequences; when an actual transformation is claimed, identify its occurrence and affected participants under A.3.4 | a possible or described change from an obtaining transformation |
| Membership or part-whole structure matters. | the applicable collection-membership or part-whole predicate and its supported claim or unresolved condition; an affirmative occurrence claim needs its obtaining basis | a plural name from an acting or responsible System |
| Agency is disputed. | identify the agency claim and its supporting basis; use A.13 for an FPF agency claim, adding a Characteristic, Scale or threshold only when the claim or criterion requires it | an agency claim from responsibility |
| Responsibility, permission, authority, commitment, or participation is claimed. | the applicable direct predicate, participants and supported affirmative, negative or modal claim, or the unresolved condition; an affirmative occurrence claim needs its obtaining basis, and a separate occurrence reference is added when its identity is used | the relation family from an occurrence; the occurrence from evidence for it |
| A calculation or formal comparison changes the tension. | retain the calculation's subject correspondence, applicable assumptions and operation; use C.29 when the representation's choice, transfer or supported use remains unresolved | a formula or score from the ethical conflict or decision |
| Publication or audience use changes the ethical claim. | recover the claims made available, audience and bounded use under E.24.PUB, including the expression, carrier, form or occurrence identity that changes this judgement; use E.17 when a readable face of an accepted account must be produced | the published episteme from its expression, form, carrier, publishing Work, and availability relation |
| A harm or benefit depends on causality, assurance, or architecture. | only the affected C.28, B.3, D.5, or C.30.ILC return | the conflict description from causal proof, assurance, or architecture selection |

Open no branch merely because the field exists. The detail must change a side, the tension, or the next receiving use.

