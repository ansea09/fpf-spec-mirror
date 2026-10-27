---
chunk_kind: "child"
pattern_id: "A.7.2"
pattern_title: "FPF Ontology-Premise Reconciliation"
section_id: "A.7.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.2/A.7.2__006_solution.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.7.2 — FPF Ontology-Premise Reconciliation"
  - "A.7.2:4 — Solution"
line_start: 25868
line_end: 25970
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

#### A.7.2:4.1 - Recover the exact conflict

1. Name the smallest disputed receiving ontology claim and its current edition.
2. For each dated application, name its resulting ontology-claim or decision episteme, the practical consequence the receiving use would take from it, and the exact method clause, premise, or source-use occurrence on which the work relied.
3. Recover the FPF claim epistemes, dated application Work, direct kinds and relations, and source-use occurrences needed for this comparison. Include A.7.CP reasoning-basis occurrences only for claims actually used; recover scope and currentness where they affect the result.
4. Test whether the result claims support incompatible answers to the same receiving claim or practical consequence in the same scope. If not, return `noConflictStop` or `contextSplit`.
5. Compare exact source content through direct evidence, formal-semantics, domain, scope, and currentness patterns. Do not rank source labels.
6. Translate candidate distinctions into FPF objects and constructive consequences. Test them against subject evidence and only the `A7CP-*` claims used by the reconciliation work.
7. Reopen the smallest FPF decision set, preserve unaffected subject-pattern decisions, and repair the method clause or subject-pattern decision that caused the dated applications to yield incompatible results. Run enough of the affected application again to obtain a checked result; do not stop at rewriting a premise list.
8. Return one declared result with affected use, stop, and reopen condition.

#### A.7.2:4.2 - Use one closed reconciliation result set

The result episteme uses exactly one local disposition:

- `reconciledCompatibility` — repaired clauses and checked application results now support compatible use for the named claim and scope;
- `contextSplit` — the apparent incompatibility disappears under the recovered contexts or scopes; each claim retains its separate subject-matter warrant;
- `doNotCompose` — both may remain current, but their outputs must not be combined for the named use;
- `unresolvedEscalation` — evidence or decision authority is insufficient, with the exact blocked use and receiving subject pattern named;
- `noConflictStop` — the apparent conflict disappears after claim, consequence, or scope recovery.

These are reconciliation-result dispositions, not new U-kinds. Compatible co-use is demonstrated only when warranted. A current conflict does not have to end in one winner.

#### A.7.2:4.3 - Record claim-relative source use

`OntologyClaimSourceUseRelation@Context` relates one source episteme, one receiving ontology claim, and the dated ontology-decision or reconciliation work occurrence that actually consumes that source for that claim. It is local to this use and does not create a universal source-authority relation.

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
  modelUseStructureRef?: U.StructureRef
  sourceCurrentnessResultRef?: U.EpistemeRef
  receivingClaimCurrentnessResultRef?: U.EpistemeRef
  landedFPFDecisionRef?: U.EpistemeRef
  evidenceUseRelationRefs[]?: U.EntityRef
  disposition?: OntologySourceUseDispositionValue
  blockedOverreadRef?: U.EpistemeRef
  receivingClaimChangeDisposition?: ReceivingClaimChangeDispositionValue

OccurrenceIdentity:
  <exact source-episteme edition,
   exact receiving-claim edition,
   exact ontology-decision work occurrence,
   useFunction,
   sourceUseScope,
   maximalContinuousUseInterval>
```
The source participant is the source episteme and edition consumed. The receiving participant is the ontology-claim episteme and edition being formulated, constrained, tested, interpreted, compared, or traced. For the Work participant, use A.13 to identify the actual performer and A.15.1 to admit the dated ontology-decision `U.Work` independently. If the case must also identify the assignment under which that Work was performed, F.6 checks the assignment used by A.13 and compares its holder with the already identified performer. The assignment relates the independently identified System to its assigned-kind value; that System performs the Work.

The minimal occurrence needs only those three exact participants, `useFunction`, `sourceUseScope`, and the maximal continuous interval during which the named Work actually consumes content from that source episteme for that receiving claim. Citation, access, bibliography membership, prestige, publication status, or co-location alone is insufficient. If the Work consumes a separately identified claim or content episteme within the source, `sourceContentSliceRef` names that slice. A different consumed source or receiving-claim edition, Work occurrence, function, scope, or maximal continuous use episode identifies another occurrence. Correcting knowledge of the same actual episode changes the assertion, not that occurrence. A changed optional qualifier identifies another occurrence only when it changes the direct use predicate; a later review record alone does not.

Add `modelUseStructureRef` only when one independently selected `BoundedModelUseStructure` changes interpretation of this use. Add source-content kind, currentness-result, published-decision, evidence-use, disposition or receiving-claim-change references only when the reconciliation actually asserts or consumes that item under its subject rule. A `blockedOverreadRef` additionally requires F.19's independent local ground, plausible intended-reader error and effect on truth, understanding or use; state only the smallest needed correction. A recorded `unresolved` disposition needs no fabricated blocked-overread episteme. Record `unchanged` only when the Work reaches that result; an absent change disposition makes no claim.

#### A.7.2:4.4 - Identify source-use conflict without ranking traditions

`OntologySourceUseConflictFinding@Context <: U.Episteme` cites two or more exact source-use occurrences and states a conflict only when their content bears on the same receiving claim or same practical consequence in the same scope and their conclusions cannot jointly hold.

Different use functions are neither automatically comparable nor automatically insulated. Compare their exact content through direct evidence, formal-semantics, domain, scope, and currentness patterns. A finding can support adoption, adaptation, rejection, context split, non-composition, or unresolved return only with the exact counterexample, contradiction, proof consequence, or evidence relation that warrants it. “Stronger source” without claim-specific grounds is not a resolution.

#### A.7.2:4.5 - Stop and reopen

Stop with `noConflictStop` when the shared claim or consequence disappears after recovery. Stop with `contextSplit` or `doNotCompose` when that boundary truthfully protects the use. Stop unresolved only with the exact missing evidence basis or decision predicate and source and blocked use.

Reconsider affected uses when a source or receiving-claim edition changes, needed currentness changes, new domain or formal evidence bears on the same claim, a grounded blocked-overread issue becomes relevant, the consumed FPF decision changes, or later applications of repaired clauses yield incompatible same-scope consequences. Reopen only dependent source-use, application-result and receiving decisions; preserve results whose grounds remain unchanged.

