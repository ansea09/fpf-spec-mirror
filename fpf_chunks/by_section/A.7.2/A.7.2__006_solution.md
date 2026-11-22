---
chunk_kind: "child"
pattern_id: "A.7.2"
pattern_title: "FPF Ontology-Premise Reconciliation"
section_id: "A.7.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.2/A.7.2__006_solution.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "A.7.2 — FPF Ontology-Premise Reconciliation"
  - "A.7.2:4 — Solution"
line_start: 27072
line_end: 27186
dependencies:
  - "A.10"
  - "A.7.1"
  - "A.7.2"
  - "A.7.CP"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "G.11"
keywords:
  - "actual source-use relations"
  - "context split"
  - "dated FPF applications"
  - "exact used clauses and premises"
  - "optional convergence"
  - "result claims or decisions"
  - "same receiving claim or consequence"
---

### A.7.2:4 - Solution

#### A.7.2:4.1 - Recover the conflict

1. Name the disputed receiving claim or decision. Recover the wording, edition, scope and intended force of each clause. Are they alternatives under consideration, or must they govern the same decision together?
2. To compare rules, choose a situation in their common scope that the shared background conditions allow. Follow each clause under the same facts and interpretation to what it requires, permits, rules out or leaves open. One admissible case that would require incompatible answers establishes a conflict for joint use over the proposed range. Agreement in one case settles only that case unless the reason for agreement covers the range.
3. When the question concerns actual applications, recover the result claim or decision, the facts, the clause or premise applied and the practical consequence for each. Recover dated Work and source-use occurrences to the extent the historical claim needs them. Use A.7.CP reasoning-basis occurrences for claims actually used.
4. Compare the consequences for the same receiving use. One clause can leave a choice open that the other settles. Check whether both can be honored, including any right each would grant. Where differing scopes remove the conflict, explain the split. A decision that both clauses support in one case can be returned for that case even if their consequences differ elsewhere. A conclusion about compatibility across their shared domain needs grounds covering that domain.
5. Compare source content through direct evidence, formal-semantics, domain, scope, and currentness patterns. Do not rank source labels.
6. Translate candidate distinctions into FPF objects and constructive consequences. Test them against subject evidence and only the `A7CP-*` claims used by the reconciliation work.
7. When the comparison establishes a defective clause or subject-pattern decision, repair the smallest affected decision set. Follow the changed rule through the disputed case and check its consequences over the range for which compatible use is claimed. Re-evaluate the affected recorded conclusions under the repaired clauses when the receiving decision relies on them. Where the grounds warrant neither correction, use the appropriate `doNotCompose` or `unresolvedEscalation` result under §4.2.
8. Return one declared result with affected use, stop, and reopen condition.

#### A.7.2:4.2 - Use one closed reconciliation result set

The result episteme uses exactly one local disposition:

- `reconciledCompatibility` — the repaired clauses support compatible use for the named claim and scope, with checked application results when those results are at issue;
- `contextSplit` — the apparent incompatibility disappears under the recovered contexts or scopes; each claim retains its separate subject-matter warrant;
- `doNotCompose` — both may remain current, but their outputs must not be combined for the named use;
- `unresolvedEscalation` — evidence or decision authority is insufficient, with the blocked use and receiving subject pattern named;
- `noConflictStop` — the apparent conflict disappears after claim, consequence, or scope recovery.

These are reconciliation-result dispositions, not new U-kinds. Compatible co-use is demonstrated only when warranted. A conflict does not have to end in one winner.

#### A.7.2:4.3 - Record claim-relative source use

Use this relation when the question is which source a particular decision or reconciliation actually used. A comparison of proposed clauses can instead give the conditions and implications that follow from their text. A claim that someone used either clause in earlier work has its own historical grounds.

`OntologyClaimSourceUseRelation@Context` relates one source episteme, one receiving ontology claim, and the dated ontology-decision or reconciliation work occurrence that consumes that source for that claim. It is local to this use and does not create a universal source-authority relation.

```text
OntologySourceUseFunctionValue ::=
  formulateReceivingClaim
  | constrainReceivingClaim
  | testOrStressReceivingClaim
  | interpretFormalOrImplementationSemantics
  | compareReceivingAlternatives
  | traceLineage

OntologySourceUseDispositionValue ::=
  adopt | adapt | reject | comparatorOnly | lineageOnly | unresolved

ReceivingClaimChangeDispositionValue ::=
  changed | unchanged | undeterminedPendingResolution

OntologyClaimSourceUseRelation@Context <: U.Relation

RelationSignature:
  SourceEpistemeSlot:
    SlotKind: SourceEpistemeSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef
  ReceivingOntologyClaimSlot:
    SlotKind: ReceivingOntologyClaimSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef
  OntologyDecisionWorkSlot:
    SlotKind: OntologyDecisionWorkSlot
    ValueKind: U.Work
    refMode: WorkRef

semanticDirection: SourceEpistemeSlot -> ReceivingOntologyClaimSlot
  through the named OntologyDecisionWorkSlot

RelationOccurrenceQualifiers:
  sourceUseScope: U.ClaimScope
  useFunction: OntologySourceUseFunctionValue
  sourceContentSliceRef?: U.EpistemeRef
  sourceContentKindRef?: U.KindRef
  modelUseStructureRef?: SelectedStructureReference
  sourceCurrentnessResultRef?: U.EpistemeRef
  receivingClaimCurrentnessResultRef?: U.EpistemeRef
  landedFPFDecisionRef?: U.EpistemeRef
  evidenceUseRelationRefs[]?: U.EntityRef
  disposition?: OntologySourceUseDispositionValue
  blockedOverreadRef?: U.EpistemeRef
  receivingClaimChangeDisposition?: ReceivingClaimChangeDispositionValue

OccurrenceIdentity:
  <source-episteme edition,
   receiving-claim edition,
   ontology-decision work occurrence,
   useFunction,
   sourceUseScope,
   maximalContinuousUseInterval>
```
The source participant is the source episteme and edition consumed. The receiving participant is the ontology-claim episteme and edition being formulated, constrained, tested, interpreted, compared, or traced.

For the Work participant, use A.13 to identify the performer and A.15.1 to admit the dated ontology-decision `U.Work` independently. If the case must also identify the assignment under which that Work was performed, F.6 checks the assignment used by A.13 and compares its holder with the already identified performer. The assignment relates the independently identified System to its assigned-kind value; that System performs the Work.

The minimal occurrence needs only those three participants, `useFunction`, `sourceUseScope`, and the maximal continuous interval during which the named Work consumes content from that source episteme for that receiving claim. Citation, access, bibliography membership, prestige, publication status, or co-location alone is insufficient.

If the Work consumes a separately identified claim or content episteme within the source, `sourceContentSliceRef` names that slice.

A different consumed source or receiving-claim edition, Work occurrence, function, scope, or maximal continuous use episode identifies another occurrence. Correcting knowledge of the same actual episode changes the assertion, not that occurrence. A changed optional qualifier identifies another occurrence only when it changes the direct use predicate; a later review record alone does not.

Add `modelUseStructureRef` only when one independently selected `BoundedModelUseStructure` changes interpretation of this use. Add source-content kind, currentness-result, published-decision, evidence-use, disposition or receiving-claim-change references only when the reconciliation asserts or consumes that item under its subject rule.

A `blockedOverreadRef` additionally requires F.19's independent local ground, plausible intended-reader error and effect on truth, understanding or use; state only the smallest needed correction. A recorded `unresolved` disposition needs no fabricated blocked-overread episteme.

Record `unchanged` only when the Work reaches that result; an absent change disposition makes no claim.

#### A.7.2:4.4 - Identify source-use conflict without ranking traditions

`OntologySourceUseConflictFinding@Context <: U.Episteme` cites two or more source-use occurrences and states a conflict only when their content bears on the same receiving claim or same practical consequence in the same scope and their conclusions cannot jointly hold.

Different use functions are neither automatically comparable nor automatically insulated. Compare their content through direct evidence, formal-semantics, domain, scope, and currentness patterns. A finding can support adoption, adaptation, rejection, context split, non-composition, or unresolved return only with the counterexample, contradiction, proof consequence, or evidence relation that warrants it. “Stronger source” without claim-specific grounds is not a resolution.

#### A.7.2:4.5 - Stop and reopen

Stop with `noConflictStop` when the shared claim or consequence disappears after recovery. Stop with `contextSplit` or `doNotCompose` when that boundary truthfully protects the use. Stop unresolved only with the missing evidence basis or decision predicate and source and blocked use.

Reconsider affected uses when a source or receiving-claim edition changes, needed currentness changes, new domain or formal evidence bears on the same claim, a grounded blocked-overread issue becomes relevant, the consumed FPF decision changes, or later applications of repaired clauses yield incompatible same-scope consequences. Reopen only dependent source-use, application-result and receiving decisions; preserve results whose grounds remain unchanged.

