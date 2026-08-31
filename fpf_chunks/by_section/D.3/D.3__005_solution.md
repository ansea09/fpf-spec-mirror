---
chunk_kind: "child"
pattern_id: "D.3"
pattern_title: "Interlevel Ethical Conflict Structure"
section_id: "D.3:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.3/D.3__005_solution.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "D.3 — Interlevel Ethical Conflict Structure"
  - "D.3:2 — Solution"
line_start: 68630
line_end: 68710
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
---

### D.3:2 - Solution

#### D.3:2.1 - First useful result

Start with two sides and one tension statement. For each side, write:

1. the ethical claim that states the concern in ordinary language;
2. the exact affected entity;
3. the declared level relation, claim scope, or Work extent that locates the concern;
4. the value-frame edition under which the consequence matters;
5. the expected benefit, harm, or constraint and its consequence horizon; and
6. the evidence use or uncertainty only when the side currently relies on it.

Then say why the sides cannot both be met as stated, what would be traded, or why they remain in unresolved tension. Name the next live use: mediation, refusal, a decision, an evidence or causal question, assurance, or architecture return. Stop there when this makes the conflict inspectable for that use.

This first result can remain a short working note. It does not need a schema, publication, assurance package, responsibility model, or complete account of every participant.

#### D.3:2.2 - Reusable conflict description

When another reader or later use must cite, compare, revise, or publish the result, identify one `InterlevelEthicalConflictDescription`. This is an ordinary local name for one C.2.1 `U.Episteme`, not a newly admitted `U.*` kind.

Apply the C.2.1 identity test:

- **EntityOfConcern:** one exact entity already recovered for the case, such as the plan, proposed system change, or decision situation whose ethical tension is being described. Do not use a loose bundle of several possible subjects.
- **ClaimGraph:** the exact claim content containing the conflict sides, their tension, and the next-use question. When those claims are explicitly restricted to part of the situation, it also identifies the description's ClaimScope.
- **effective ReferenceScheme:** the designation, interpretation, measurement, comparison, and evaluation rules needed to read those claims.

Changed claim content, EntityOfConcern, or effective ReferenceScheme identifies another episteme. Say that a later description revises or supersedes an earlier one only when an exact C.2.1 `EpistemeEditionRelation` is asserted. A changed narrative, table layout, publication form, carrier, or publication occurrence does not by itself change the episteme.

Use this compact content shape when a reusable record helps:

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
        valueFrameEditionRef
        expectedConsequence: what changes and why it counts, for example, as a benefit, harm, or constraint under that value frame
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

When present, `descriptionClaimScopeRef` identifies the declared part of the situation covered by the whole description. Do not add it merely to complete the shape. A side's ClaimScope or Work extent says where that side applies; it never substitutes for the whole-description scope.

The `plainStatement` must name the exact incompatibility, trade-off, parity, or other tension claimed among the sides. In an ordinary case, it remains claim content in the description. If a receiving use relies on a separately obtaining direct relation, cite the exact relation definition and occurrence with its participants, applicability, and identity. If no adequate governor exists, record the exact `A.6.RCD` missing-governor result. Merely filling a reference field never makes a direct relation obtain.

#### D.3:2.3 - Add detail only when it changes the conflict or its next use

| Open this branch when... | Add... | Keep separate... |
| --- | --- | --- |
| A Method is part of a side's claim. | the exact `U.Method` under A.3.1 and, when cited, its MethodDescription under A.3.2 | Method identity from any dated performance |
| Performance actually occurred. | use A.13 to identify the actual performer System; use A.15.1 to admit the exact dated `U.Work` independently from its history, Method, extent, and containing System; if the conflict account must also identify the assignment under which the Work was performed, check that relation separately through F.6 | keep a plan, intention, assignment, capability, permission, authority, and responsibility separate from performed Work |
| Assignment matters. | the exact assignment species and its obtaining occurrence under A.2.1, with actual participants and applicability | assignment from performance, responsibility, permission, or authority |
| Role-shaped wording or classification matters. | one E.10.ROLE recovery, then the local kind and a separate C.2.1 classification assertion episteme under C.3.2 after the candidate passes its admissibility test | the word *role*, kind, assertion, assignment, and acting System from one another |
| Evidence changes a side or its uncertainty. | the evidence episteme and the exact A.10 evidence-use or reliance result | stored evidence from reliance on it |
| A transformation changes who benefits or is harmed. | the exact transformation occurrence under A.3.4 and its affected participants | a transformation description from the occurrence |
| Membership or part-whole structure matters. | the exact collection-membership or part-whole predicate and obtaining occurrence | a plural name from an acting or responsible System |
| Agency is disputed. | the exact Characteristic, Scale, threshold, and supporting evidence use | an agency reading from responsibility |
| Responsibility, permission, authority, commitment, or participation is claimed. | the exact relation definition and obtaining occurrence, or the exact A.6.RCD missing-governor result | the relation family from an occurrence; the occurrence from evidence for it |
| A calculation or formal comparison changes the tension. | the exact C.29 representation, its correspondence to the independently recovered objects, and the operation used | a formula or score from the ethical conflict or decision |
| Publication or audience use changes the ethical claim. | the selected episteme edition, publication occurrence, form, carrier, audience, and bounded use under E.17 and E.24.PUB | the published episteme from its form, carrier, publishing Work, and availability relation |
| A harm or benefit depends on causality, assurance, or architecture. | only the affected C.28, B.3, D.5, or C.30.ILC return | the conflict description from causal proof, assurance, or architecture selection |

Open no branch merely because the field exists. The detail must change a side, the tension, or the next receiving use.

