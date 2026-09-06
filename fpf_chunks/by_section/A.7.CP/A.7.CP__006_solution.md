---
chunk_kind: "child"
pattern_id: "A.7.CP"
pattern_title: "Constructive-Premise Compact and Reasoning-Basis Use"
section_id: "A.7.CP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.CP/A.7.CP__006_solution.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "A.7.CP — Constructive-Premise Compact and Reasoning-Basis Use"
  - "A.7.CP:4 — Solution"
line_start: 22261
line_end: 22342
dependencies:
  - "A.7"
  - "A.7.1"
  - "A.7.2"
keywords:
  - "ClaimUsedAsReasoningBasisRelation@Context"
  - "adopted premise or conditional assumption"
  - "constructive-premise claim"
  - "dated reasoning Work"
  - "exact receiving claim or result"
  - "selective reopen"
---

### A.7.CP:4 - Solution

#### A.7.CP:4.1 - Publish the compact once

The compact carries these stable claim contents:

1. **`A7CP-01 Existence and obtaining`.** World-side obtaining is not created by a claim, database row, predicate, or publication merely representing it.
2. **`A7CP-02 Constructive settlement`.** When identity, constitution, dependence, or obtaining changes a consequence, name the construction or direct governing relation that grounds it; a reconstructible trace is not itself the world construction.
3. **`A7CP-03 Constitution and social objects`.** Constituting acts, admitted systems, and the relations they institute remain distinct from descriptions of those acts and relations.
4. **`A7CP-04 Epistemic openness and fallibility`.** Evidence and reliance may remain unresolved without turning unresolved evidence into a third world-side obtaining mode.
5. **`A7CP-05 Representation boundary`.** Descriptions, logical forms, database rows, graphs, and publications represent or carry claims under exact relations; their form does not prove the represented ontic.
6. **`A7CP-06 Agency and work attribution`.** A `U.MethodDescription` episteme describes an admitted `U.Method`; for a precise performed-Work claim, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated `U.Work`. Only when the claim or its receiving use expressly consumes precise assignment-bound attribution does F.6 separately relate that Work to the same obtaining A.13 assignment; F.6 identifies neither the assignment nor the performer, neither the system-role kind nor the assignment acts, and missing or failed F.6 leaves the Work intact. A result follows only through its own separately established relation—for example, a production, operation-result, measurement, evaluation, decision, delivery, or acceptance relation—not from Work in general.
7. **`A7CP-07 Kind discipline`.** Use direct existing kinds and local admission before proposing a universal kind, root relation, or role-like surrogate.
8. **`A7CP-08 Scoped pluralism`.** Different source traditions or apparatuses may be useful for different receiving claims; compatibility is tested by consequences, not achieved through prestige hierarchy.
9. **`A7CP-09 Structure and wholeness`.** A description of structure is not the structure; not every construction is mereology, and `C.13` alone defines constructional mereology.
10. **`A7CP-10 Time, identity, and currentness`.** World-side temporal qualification, occurrence identity, claim/publication currentness, and source supersession are separate questions.
11. **`A7CP-11 Subject-pattern separation`.** Capability, state, architecture, role, method, work, evidence, permission, and relation families retain their subject patterns even when an ontology method diagnoses a conflict among them.
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
  ReceivingReasoningResultSlot:
    SlotKind: ReceivingReasoningResultSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef

semanticDirection: BasisClaimSlot -> ReceivingReasoningResultSlot
  through the named ReasoningWorkSlot
ReasoningBasisPostureValue ::= adoptedPremise | conditionalAssumption

RelationOccurrenceQualifiers:
  basisClaimAddress: ClaimAddress
  posture: ReasoningBasisPostureValue
  reasoningUseScope?: U.ClaimScope
  modelUseStructureRef?: U.StructureRef

OccurrenceIdentity:
  <exact basis-claim edition and claim ID,
   exact reasoning-work occurrence,
   exact receiving-result edition,
   posture,
   reasoningUseScope when present,
   maximalContinuousRelianceInterval>
```

`BasisClaimSlot` is the exact claim-bearing episteme used, and `basisClaimAddress` is a `C.2.1 ClaimAddress` selecting the exact claim inside that same edition by its intrinsic ClaimGraph identity. `ReasoningWorkSlot` is the dated reasoning, choice, ontology-analysis, or reconciliation `U.Work` that relies on it. `ReceivingReasoningResultSlot` is the claim, comparison, decision, or other claim-bearing result episteme whose content that Work forms or revises using the basis claim. If the practical result is world-side, use the direct result claim that bears on it; the world-side object retains its subject pattern. An admitted `U.System` performs the Work. If the case relies on an assignment, recover one actual occurrence of a separately declared `U.SystemRoleAssignment` species and the obtaining F.6 attribution for that exact Work-assignment pair; its holder must be the same System. The assignment's existence, holder, or interval does not establish that attribution, and the assignment neither supplies the System nor performs the Work. Claim episteme, described Method when one is used, Work occurrence, assignment occurrence, attribution, use posture, receiving result, and any world-side result remain distinct. The words “premise” and “assumption” are not relation participants.

The relation obtains during the maximal continuous interval in which the named work actually relies on the exact basis claim to form or revise the exact receiving result. Access, citation, publication, co-location, or use of the claim elsewhere in the same work is insufficient. `reasoningUseScope` appears only when this premise use is narrower than or otherwise differs from the receiving result's declared claim scope; `modelUseStructureRef` appears only when an independently selected `BoundedModelUseStructure` changes interpretation. Source currentness, evidence, publication, work method, and the receiving result's own governance remain with their subject patterns.

One occurrence is identified by the exact basis-claim edition and ID, reasoning-work occurrence, receiving-result edition, posture, optional narrower use scope, and maximal continuous reliance interval. If one work uses the same basis claim for two independent results, record two relation occurrences that share the work participant but name different receiving results; do not duplicate the work. A change to any identity value ends or splits only the affected result-specific occurrence.

#### A.7.CP:4.3 - Keep posture and transition explicit

`adoptedPremise` means the named work presently uses the basis claim as accepted support for the exact receiving result. `conditionalAssumption` means the work uses it for that result only in a narrower model, scenario, proof, or branch with an explicit test, defeater, or reopen condition. Every conditional assumption actually used can function as a premise inside that bounded subargument; not every adopted premise is conditional. Neither posture changes the basis-claim episteme's intrinsic kind.

The same claim can have different postures in different work or for different receiving results of one work. A posture transition creates a later occurrence only for the exact receiving result on that relation edge. Reopen that result and its dependents; another result of the same work remains closed when its separate premise-use occurrence and posture did not change.

#### A.7.CP:4.4 - Use the cheapest truthful path

1. Name the exact reasoning work and each exact receiving claim, decision, comparison, or other claim-bearing result it is forming.
2. For each receiving result, cite only the compact IDs that are load-bearing.
3. Record one relation occurrence per exact basis claim, receiving result, posture, and continuous reliance interval; reuse the same work reference across independent results.
4. Name a narrower `U.ClaimScope` or selected `BoundedModelUseStructure` only when it changes this premise use.
5. Keep evidence, currentness, source use, kind admission, subject construction, work method, and result governance with their subject patterns.
6. Stop when every load-bearing receiving result points to its exact premise-use occurrences. Do not inspect unused compact entries.

