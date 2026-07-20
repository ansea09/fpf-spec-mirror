---
chunk_kind: "child"
pattern_id: "A.7.2"
pattern_title: "FPF Ontology-Premise Reconciliation"
section_id: "A.7.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.2/A.7.2__006_solution.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.7.2 — FPF Ontology-Premise Reconciliation"
  - "A.7.2:4 — Solution"
line_start: 21323
line_end: 21419
dependencies:
  - "A.10"
  - "A.7.1"
  - "A.7.2"
  - "A.7.CP"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "G.11"
keywords:
  - "incompatible FPF consequences"
  - "optional convergence"
  - "premise reconciliation"
  - "same receiving claim and scope"
  - "source-use conflict"
---

### A.7.2:4 - Solution

#### A.7.2:4.1 - Recover the exact conflict

1. Name the smallest disputed receiving ontology claim and its current edition.
2. State the material practical consequence produced by each FPF method or source use.
3. Recover the exact FPF claim epistemes, direct kinds and relations, `A.7.CP` reasoning-basis occurrences, source-use occurrences, scope, and currentness.
4. Test whether the outputs concern the same receiving claim or the same practical consequence in the same scope. If not, return `noConflictStop` or `contextSplit`.
5. Compare exact source content through direct evidence, formal-semantics, domain, scope, and currentness owners. Do not rank source labels.
6. Translate candidate distinctions into FPF objects and constructive consequences. Test them against subject evidence and only the `A7CP-*` claims used by the reconciliation work.
7. Reopen the smallest FPF decision set, preserve unaffected direct-owner decisions, and repair the methods or clauses that produce the conflict rather than merely rewriting a premise list.
8. Return one declared result with affected use, stop, and reopen condition.

#### A.7.2:4.2 - Use one closed reconciliation result set

The result episteme uses exactly one local disposition:

- `reconciledCompatibility` — repaired methods now support compatible use for the named claim and scope;
- `contextSplit` — the claims or constructions are valid only in different named contexts or scopes;
- `doNotCompose` — both may remain current, but their outputs must not be combined for the named use;
- `unresolvedEscalation` — evidence or decision authority is insufficient, with the exact blocked use and receiving owner named;
- `noConflictStop` — the apparent conflict disappears after claim, consequence, or scope recovery.

These are reconciliation-result dispositions, not new U-kinds. Compatible co-use is demonstrated only when warranted. A current conflict does not have to end in one winner.

#### A.7.2:4.3 - Record claim-relative source use

`OntologyClaimSourceUseRelation@Context` records how one dated ontology-decision or reconciliation work occurrence actually consumes one source episteme for one receiving ontology claim. It is local to this use and does not create a universal source-authority relation.

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
  sourceContentBundleRef: U.EpistemeRef
  sourceContentKindRef: U.KindRef
  boundedContextRef: U.BoundedContextRef
  sourceUseScope: U.ClaimScope
  useFunction: OntologySourceUseFunctionValue
  useInterval: QualificationWindowPolicy
  sourceCurrentnessRef: U.EntityRef
  receivingClaimCurrentnessRef: U.EntityRef
  landedFPFDecisionRef?: U.EpistemeRef
  evidenceUseRelationRefs[]?: U.EntityRef
  disposition: OntologySourceUseDispositionValue
  blockedOverreadRef: U.EpistemeRef
  receivingClaimChangeDisposition: ReceivingClaimChangeDispositionValue
```

The source participant is the exact source episteme and edition consumed. The receiving participant is the exact ontology-claim episteme and edition being formulated, constrained, tested, interpreted, compared, or traced. The work participant is the dated ontology-decision work; its `performedBy` role assignment supplies the admitted system.

The relation obtains during the maximal interval in which the named work actually consumes `sourceContentBundleRef` for the declared function, scope, context, and receiving claim. Citation, access, bibliography membership, prestige, publication status, or co-location alone is insufficient. A change of source edition/content bundle, receiving-claim edition, work occurrence, context, scope, function, or maximal use interval creates another occurrence.

`sourceCurrentnessRef` and `receivingClaimCurrentnessRef` resolve to results under `G.11` or the exact direct owner. `landedFPFDecisionRef` appears only when current work consumes a landed decision as internal basis; it is not a prestige weight. `evidenceUseRelationRefs` point to exact `A.10` occurrences only when evidential use is current. `unresolved` pairs with `undeterminedPendingResolution` unless independent evidence establishes `unchanged`; it never silently means `changed`.

#### A.7.2:4.4 - Identify source-use conflict without ranking traditions

`OntologySourceUseConflictFinding@Context <: U.Episteme` cites two or more exact source-use occurrences and states a conflict only when their content bears on the same receiving claim or same practical consequence in the same scope and their conclusions cannot jointly hold.

Different use functions are neither automatically comparable nor automatically insulated. Compare their exact content through direct evidence, formal-semantics, domain, scope, and currentness owners. A finding can support adoption, adaptation, rejection, context split, non-composition, or unresolved return only with the exact counterexample, contradiction, proof consequence, or evidence relation that warrants it. “Stronger source” without claim-specific grounds is not a resolution.

#### A.7.2:4.5 - Stop and reopen

Stop with `noConflictStop` when the shared claim or consequence disappears after recovery. Stop with `contextSplit` or `doNotCompose` when that boundary truthfully protects the use. Stop unresolved only with the exact missing evidence or decision owner and blocked use.

Reopen when a source or receiving-claim edition changes, currentness changes, new domain or formal evidence bears on the same claim, a blocked overread becomes relevant, a landed decision changes, or repaired methods again produce incompatible same-scope consequences. Reopen only affected source-use and receiving decisions.

