---
chunk_kind: "child"
pattern_id: "D.3"
pattern_title: "Describe an Ethical Conflict Across Levels or Scopes"
section_id: "D.3:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.3/D.3__005_solution.md"
commit_sha: "d325a051ac7b2bb37cd870f90b4ed8b2d0426e58"
heading_path:
  - "D.3 — Describe an Ethical Conflict Across Levels or Scopes"
  - "D.3:2 — Solution"
line_start: 96763
line_end: 96844
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
3. the declared level relation, claim scope, or Work extent that locates the concern;
4. the value premise under which the consequence matters, with a frame-edition reference when the reasoning uses one;
5. the expected benefit, harm, or constraint and its consequence horizon; and
6. the evidence use or uncertainty only when the side relies on it.

Then explain why the claims cannot all be met as stated, what would be traded, or why they remain in unresolved tension. Three or more claims may be jointly incompatible even when every pair is compatible. Name the intended use of this description and any question that remains to be settled. Stop when this makes the conflict inspectable for its intended use.

A short working note can be sufficient. Develop a more elaborate description only when its intended use requires the additional content.

#### D.3:2.2 - Reusable conflict description

When another reader or later use must cite, compare, revise, or publish the result, identify one `InterlevelEthicalConflictDescription`. This is an ordinary local name for one C.2.1 `U.Episteme`.

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

The `plainStatement` must name the incompatibility, trade-off, parity, or other tension claimed among the sides. In an ordinary case, it remains claim content in the description. If a receiving use relies on a separately obtaining direct relation, cite the relation definition and occurrence with its participants, applicability, and identity. If no adequate governor exists, record the `A.6.RCD` missing-governor result. Merely filling a reference field never makes a direct relation obtain.

#### D.3:2.3 - Add detail only when it changes the conflict or its next use

| Open this branch when... | Add... | Keep separate... |
| --- | --- | --- |
| A Method is part of a side's claim. | the exact `U.Method` under A.3.1 and, when cited, its MethodDescription under A.3.2 | Method identity from any dated performance |
| Performance occurred. | use A.13 to identify the performer System; use A.15.1 to admit the exact dated `U.Work` independently from its history, Method, extent, and containing System; if the conflict account must also identify the assignment under which the Work was performed, check that relation separately through F.6 | keep a plan, intention, assignment, capability, permission, authority, and responsibility separate from performed Work |
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

