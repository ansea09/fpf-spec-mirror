---
chunk_kind: "child"
pattern_id: "A.7.CP"
pattern_title: "Constructive-Premise Compact and Reasoning-Basis Use"
section_id: "A.7.CP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.CP/A.7.CP__006_solution.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.7.CP — Constructive-Premise Compact and Reasoning-Basis Use"
  - "A.7.CP:4 — Solution"
line_start: 22107
line_end: 22175
dependencies:
  - "A.7"
  - "A.7.1"
  - "A.7.2"
keywords:
  - "ClaimUsedAsReasoningBasisRelation@Context"
  - "claim content"
  - "constructive-premise compact"
  - "reasoning-basis use"
---

### A.7.CP:4 - Solution

#### A.7.CP:4.1 - Publish the compact once

The compact carries these stable claim contents:

1. **`A7CP-01 Existence and obtaining`.** World-side obtaining is not created by a claim, database row, predicate, or publication merely representing it.
2. **`A7CP-02 Constructive settlement`.** When identity, constitution, dependence, or obtaining changes a consequence, name the construction or direct governing relation that grounds it; a reconstructible trace is not itself the world construction.
3. **`A7CP-03 Constitution and social objects`.** Constituting acts, admitted systems, and the relations they institute remain distinct from descriptions of those acts and relations.
4. **`A7CP-04 Epistemic openness and fallibility`.** Evidence and reliance may remain unresolved without turning unresolved evidence into a third world-side obtaining mode.
5. **`A7CP-05 Representation boundary`.** Descriptions, logical forms, database rows, graphs, and publications represent or carry claims under exact relations; their form does not prove the represented ontic.
6. **`A7CP-06 Agency and work attribution`.** A method episteme describes a way of working; an admitted system under a role assignment performs dated work and produces results.
7. **`A7CP-07 Kind discipline`.** Use direct existing kinds and local admission before proposing a universal kind, root relation, or role-like surrogate.
8. **`A7CP-08 Scoped pluralism`.** Different source traditions or apparatuses may be useful for different receiving claims; compatibility is tested by consequences, not achieved through prestige hierarchy.
9. **`A7CP-09 Structure and wholeness`.** A description of structure is not the structure; not every construction is mereology, and `C.13` remains the owner of constructional mereology only.
10. **`A7CP-10 Time, identity, and currentness`.** World-side temporal qualification, occurrence identity, claim/publication currentness, and source supersession are separate questions.
11. **`A7CP-11 Direct-owner separation`.** Capability, state, architecture, role, method, work, evidence, permission, and relation families retain their direct owners even when an ontology method diagnoses a conflict among them.
12. **`A7CP-12 Formal projection non-reversal`.** CT2R and formalization may preserve, collapse, or omit structure. Logical validity or representation form does not reverse-infer a unique world construction.

The twelve IDs form a stable closed compact in this pattern. They are not steps, completeness criteria for every ontology use, or twelve intrinsic premise kinds.

#### A.7.CP:4.2 - Record actual reasoning-basis use

`Premise` and `assumption` name postures of exact claim use, not disjoint claim kinds.

```text
ClaimUsedAsReasoningBasisRelation@Context <: U.Relation

RelationSignature:
  BasisClaimSlot:
    SlotKind: BasisClaimSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef
  ReasoningWorkSlot:
    SlotKind: ReasoningWorkSlot
    ValueKind: U.Work
    refMode: WorkRef

semanticDirection: BasisClaimSlot -> ReasoningWorkSlot
ReasoningBasisPostureValue ::= adoptedPremise | conditionalAssumption

RelationOccurrenceQualifiers:
  basisClaimIdRef: ClaimIdRef
  boundedContextRef: U.BoundedContextRef
  declaredReasoningUseRef: U.EntityRef
  posture: ReasoningBasisPostureValue
  relianceInterval: QualificationWindowPolicy
```

`BasisClaimSlot` is the exact claim-bearing episteme and exact compact claim ID used. `ReasoningWorkSlot` is the dated reasoning, choice, ontology-analysis, or reconciliation work that relies on it. `WorkRef` resolves to `U.Work`; the work's `performedBy` role assignment supplies the admitted system. The words “premise” and “assumption” are not relation participants.

The relation obtains during the maximal interval in which the named work actually relies on the exact claim in an inference, comparison, or choice for the declared context and use. Access, citation, publication, or co-location alone is insufficient. It applies only to reasoning-basis use; source currentness, evidence, publication, and work method remain with their owners.

One occurrence is identified by exact claim episteme and claim ID, exact work occurrence, bounded context and declared use, posture, and maximal continuous reliance interval. A change to claim edition, work occurrence, context/use, posture, or interval ends or splits the occurrence.

#### A.7.CP:4.3 - Keep posture and transition explicit

`adoptedPremise` means the work presently proceeds on the claim as accepted basis in its declared scope. `conditionalAssumption` means the work uses the claim in a narrower model, scenario, proof, or branch with an explicit test, defeater, or reopen condition. Every conditional assumption actually used can function as a premise inside that bounded subargument; not every adopted premise is conditional. Neither posture changes the claim episteme's intrinsic kind.

The same claim can be adopted in one work and conditional in another. It can also change posture within one work through two relation occurrences. Such a transition reopens only results that depended on the changed use; it does not trigger corpus-wide synonym or claim rewriting.

#### A.7.CP:4.4 - Use the cheapest truthful path

1. Name the exact reasoning work and declared use.
2. Cite only the compact IDs that are load-bearing.
3. Record one relation occurrence per exact claim/posture/continuous-use identity.
4. Keep evidence, currentness, source use, kind admission, subject construction, and work method with their direct owners.
5. Stop when the result and its premise uses are recoverable. Do not inspect unused compact entries.

