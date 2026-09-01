---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:8.0"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__010_bias-annotation.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:8.0 — Bias-Annotation"
line_start: 95075
line_end: 95109
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RCD"
  - "A.7"
  - "A.8"
  - "C.11"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "admission before naming"
  - "alias"
  - "designation"
  - "durable naming"
  - "governed value or relation"
  - "local phrase"
  - "proposed naming use"
  - "row use"
  - "subject before name"
---

### F.8:8.0 - Bias-Annotation

F.8 counters two shortcuts: a familiar word is treated as proof that a stronger name is needed, or a record is treated as the subject or decision it describes. Recover the four starting facts, choose the lightest disposition, and add a Structure, decision result, NameCard, row, or publication object only when its own receiving use requires it.

#### F.8:8.1 - Policy-Identifier Mint-or-Reuse Discipline

FPF treats policy identifiers such as `Phi(CL)`, `Phi_plane`, `Psi(CL^k)`, `Aut-Guard`, `EmitterPolicyRef`, insertion-policy identifiers, and acceptance-clause identifiers as versioned references whose meaning must be recoverable. They are not "just strings", system-role-kind names, gate decisions, permissions, or policy specifications.

```text
PolicyIdentifierReference:
  PolicyIdentifier:
  PolicySpecificationRef:
  MintDecisionOrChoiceOccurrenceRef?: required only for cited, replayed, normative, cross-local reuse, or accountable mint history
  MintDecisionSubjectPatternLocator?: paired with MintDecisionOrChoiceOccurrenceRef
  MintDecisionPredicateRef?: paired with MintDecisionOrChoiceOccurrenceRef
  MintDecisionParticipantRefs?: [actual participants with their meanings]
  MintDecisionApplicability?:
  MintDecisionOccurrenceIdentityBasis?:
  MintDecisionMakingWorkRef?: [separate A.15.1 Work only when current]
  MintDecisionOrChoiceResultRef?: [separate result, such as a C.11 ChoiceResult, only when current]
  MintDecisionResultEpistemeRef?:
  ScopeOrNamespaceRef:
```
`PolicyIdentifier` is the selected designator. `PolicySpecificationRef` resolves to the separate policy-definition episteme and pins an edition or equivalent digest when needed. A local non-accountable introduction can stop there with explicit local scope. The conditional mint-occurrence fields are required when the use cites, replays, makes normative, reuses across the local boundary, or assigns accountability to the mint history; together they resolve one admitted decision or choice occurrence and the pattern, predicate, actual participants, applicability, and identity rule that establish it. If that stronger use is requested and those facts are absent, return `missing-governor` for it rather than inventing an occurrence. A C.11 `ChoiceResult` and any dated decision-making Work remain separate. `MintDecisionResultEpistemeRef`, when current, resolves to a C.2.1 episteme or accepted record describing the occurrence; the record does not perform the decision.

For FPF normative policy identifiers, the durable result episteme is usually an accepted `E.9` decision record, but only after the decision or choice pattern has admitted the occurrence that record describes. A local non-exported and non-accountable identifier needs only its separately recoverable specification and explicit scope; it need not create a decision or result episteme. In every branch, the policy specification, identifier, any decision or choice occurrence, any C.11 result, any decision-making Work, and any record remain distinct.

Rules:

1. **No silent policy-identifier introduction.** Every new identifier resolves the separate `PolicySpecificationRef` and states its scope. A local non-accountable introduction stops there. A cited, replayed, normative, cross-local, or accountable mint history additionally resolves the decision or choice occurrence plus the pattern, predicate, participants, applicability, and identity rule that establish it; without that basis, return `missing-governor` for the stronger branch and do not claim it.
2. **Reuse is reference use.** Reusing an existing identifier resolves the same identifier and policy specification. Resolve the original mint occurrence only when the current reuse consumes or asserts that history; it does not restate policy semantics, turn a record into the occurrence, or silently create another decision.
3. **Gate checkability.** A gate, crossing, Bridge, assurance, or publication claim that depends on a policy identifier includes `PolicyIdentifierReference` or an equivalent resolvable structure admitted by its subject pattern.
4. **Policy authority stays with the subject pattern.** F.8 selects introduction or reuse of the identifier; it does not decide whether the policy permits Work, passes a gate, makes a relation obtain, or provides evidence.
5. **The identifier grants nothing by itself.** Name, namespace, suffix, source prestige, specification publication, or decision record grants no permission, status, equivalence, or authority beyond the policy claim defined by its subject pattern.

