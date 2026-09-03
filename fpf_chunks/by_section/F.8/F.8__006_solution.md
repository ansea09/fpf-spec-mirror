---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__006_solution.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:4 — Solution"
line_start: 95191
line_end: 95335
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
  - "F.19"
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

### F.8:4 - Solution

Treat mint-or-reuse as a decision about an already recovered subject, not a vote on wording. Start with four facts:

1. the candidate expression;
2. the governed value or relation;
3. the subject pattern that defines or tests that value or relation; and
4. the proposed naming use.

If any fact is missing, stop at the subject-recovery route; naming cannot supply it. Otherwise try the dispositions in this order and stop at the first one that supports the proposed use:

1. keep a local phrase;
2. reuse an existing designation;
3. use an alias without changing the governed meaning;
4. reuse the subject pattern's name;
5. reuse an admitted F.17 row within its stated use;
6. name a separately justified `SystemRoleKindDescription` when that is the governed object;
7. open a durable naming settlement;
8. propose a public row;
9. introduce a policy identifier for an already recovered policy specification; or
10. block or lower the naming use.

The smallest result is one readable sentence, not a mandatory record: state the governed subject, proposed naming use, selected disposition, resulting name when any, and the change that would reopen the decision. Add a non-use boundary only when `F.19`'s grounded-contribution test admits it. For example, when no lighter disposition supports a needed durable local designation: “Under `PatternReviewReferenceScheme-2026`, use `ReviewerRole` as the Plain designation of `ReviewerSystemRole` for local review-method prose; select `openDurableNamingSettlement` and revisit the decision if the naming use becomes public or cross-local.”

The corresponding F.8 result labels are `localPhraseOnly`, `reuseExistingDesignation`, `aliasOnly`, `reuseDirectPatternName`, `reuseAdmittedTermRow`, `nameSystemRoleKindDescription`, `openDurableNamingSettlement`, `proposePublicTermRow`, `introducePolicyIdentifier`, and `blockOrLowerUse`. They are not new `U.*` kinds. A stronger result opens its subject pattern; it does not itself create a card, row, identifier, policy specification, or relation occurrence.

#### F.8:4.1 - Decision Targets

| If the candidate expression designates... | Smallest F.8 disposition | Subject pattern |
| --- | --- | --- |
| A one-off phrase after local repair | `localPhraseOnly` | `E.10` or the subject pattern |
| An existing selected designation for the governed value and use | `reuseExistingDesignation` | The subject pattern, with `F.1`, `F.2`, and `F.3` for local-sense discovery; use `F.5` or `F.18` only when naming work is separately needed |
| A wording variant for the same value, kind, scope, occurrence identity, and use | `aliasOnly` | `F.5`, `F.13`, and `F.18` |
| An adequate name already supplied by the subject pattern | `reuseDirectPatternName` | The subject pattern |
| A cross-local or public reading admitted by one F.17 row | `reuseAdmittedTermRow` only for its declared use | `F.17`; `F.9` only when an obtaining Bridge between the named cells is used |
| A new designation for a recovered local system-role kind | `localPhraseOnly` when local wording is enough; otherwise `openDurableNamingSettlement` when durable reuse is needed | `A.2` and `C.3` for the kind, then `F.5`; `F.18` only for a durable settlement |
| A label for a separately justified `SystemRoleKindDescription` episteme about that kind | `nameSystemRoleKindDescription` | `F.4` for the description, then `F.5`; `F.18` only when the description's own name must be durable |
| Any other governed subject—for example, a status, evidence use, source use, requirement, assurance use, gate, decision, access value, policy, Method, Work, publication use, characteristic, architecture value, or relation position | `reuseDirectPatternName`, or `openDurableNamingSettlement` only after that subject is recovered | Its subject pattern, then `F.5` or `F.18` when needed |
| A recurring durable naming settlement not served by lighter dispositions | `openDurableNamingSettlement` | `F.14`, then `F.18`; a NameCard is optional until its own enduring-use gate passes |
| A public, Core-facing, durable, or cross-local term not covered by an admitted row | `proposePublicTermRow` | `F.17` after the F.18 inputs and row threshold are met |
| A policy identifier | reuse the existing identifier, or select `introducePolicyIdentifier` for a recovered policy specification; add a mint-occurrence basis only for the stronger history uses in §8.1 | `F.8:8.1` and the subject pattern for the policy use |
| An expression offered as a new cross-family primitive before its admission disposition is stable | `blockOrLowerUse`; no naming disposition is available yet | `E.24.CD` when the governed object is still unclear; if a U-kind proposal remains, `E.24.UK` decides admission. Return only after the governed object is recovered or one stable `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject` result is available. |

#### F.8:4.2 - Decision Sequence

Use this order and stop at the first disposition that supports the proposed use without hiding a governed distinction.

1. **Recover the four starting facts.** Name the expression, governed value or relation, its subject pattern, and the proposed use. If the value or relation is not available, stop and use its subject-recovery route; F.8 cannot establish it.
2. **Split mixed candidates.** If one expression covers more than one governed subject or use—for example, a kind, assignment, evidence use, policy, Method, or Work—make separate naming decisions.
3. **State the naming locality.** Carry the naming `U.ReferenceScheme` by value and state the local-sense claim. Cite a `SchemeSenseCell`, an obtaining `LocalSenseBasisRelation`, or a selected bounded-model-use Structure only when the naming use needs that object.
4. **Apply F.14 and try a local phrase.** If ordinary local wording supports the use, choose `localPhraseOnly` and stop.
5. **Try an existing designation.** Reuse it only when the value, kind, scope, occurrence identity, local sense, and proposed use match.
6. **Try an alias.** Use `aliasOnly` when the governed meaning is unchanged and lineage can expose the wording variation. An alias may not change kind, scope, occurrence identity, use, or authority.
7. **Try the subject's existing name.** Use the name supplied for the governed subject. A.2 and C.3 govern a local system-role kind and F.5 governs its designation; use F.18 only for a durable settlement and F.4 only for a separately needed `SystemRoleKindDescription`. A.2.1 continues to govern any assignment. For precise performed Work, A.13 first recovers each exact actual performer and A.15.1 independently admits the occurrence; F.6 follows only when the naming case or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment.
8. **Try one admitted F.17 row.** Reuse only the row's declared `AdmissibleUse`. Local-sense reuse does not imply cross-local sameness; a row and equal spelling create no F.9 Bridge.
9. **Open only the next naming object that pays for itself.** A stable local address may justify a cell; an enduring naming settlement may justify a NameCard; a public/Core/durable/cross-local need may justify an F.17 row. None implies the next object.
10. **Introduce a policy identifier only for a recovered policy specification.** A local identifier can stop with that specification and its scope. If the mint history is cited, replayed, normative, cross-local, or accountable, recover its decision or choice occurrence through the subject pattern; otherwise return `missing-governor` for that stronger history claim. Keep any C.11 result, decision-making Work, result episteme, and record separate.
11. **Stop before naming an unsettled U-kind proposal.** Select `blockOrLowerUse`. If the governed object is still unclear, use E.24.CD; otherwise send the recovered proposal episteme or source construct to E.24.UK. F.8 does not test or admit the candidate. After E.24.UK returns a stable `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject` disposition, re-enter F.8 only if the admitted or reused kind, local kind, or recovered non-kind object needs a designation.
12. **Block or lower.** If no disposition is justified, keep the expression local, quote it as source wording, or lower the claim.

#### F.8:4.3 - Role Expression Boundary

A role expression is not enough to choose the object. For a system-role naming case, keep these four objects distinct:

| Symbol | Object |
| --- | --- |
| `L` | The candidate or selected designation, interpreted under the effective naming ReferenceScheme. |
| `K` | The local system-role kind recovered through A.2 and C.3, with its work-facing contribution distinction and `KindSignature`. |
| `D` | An optional F.4 `SystemRoleKindDescription` episteme whose EntityOfConcern is `K`. |
| `A` | An optional A.2.1 assignment occurrence in which an admitted system is assigned under `K`. |

Under the effective naming scheme, `L` designates `K`. Needing `L` does not create or require `D`; `D` may receive its own designation when a separate description is justified. Naming either object creates no `A`. The naming ReferenceScheme interprets the expression; it neither defines the kind nor assigns a system.

After A.2 and C.3 have recovered `K`, apply the naming ladder. Keep a one-off expression local when that is enough, and reuse an existing designation when it fits. If the kind needs a durable designation, select `openDurableNamingSettlement`, use F.5 to name `K`, and use F.18 for the durable settlement. Use `nameSystemRoleKindDescription` and F.4 only when the governed object is a separately justified description episteme `D`.

| Source expression | Recovered case | F.8 result |
| --- | --- | --- |
| `ReviewerRole` in a review method | A recovered review-system-role kind needs a durable designation; that naming need requires no description episteme | `openDurableNamingSettlement`; A.2 and C.3 govern the kind, F.5 its designation, and F.18 the durable settlement; use F.4 only for a separately needed description |
| `Alice as reviewer` | A system is assigned to a local system-role kind for an interval | Not a name decision until `A.2.1` recovers the `U.SystemRoleAssignment` occurrence |
| `review happened` | Dated performed Work | Use `A.15.1`; open naming only if a Work-kind designation is needed |
| `EvidenceRole` | An episteme used as evidence | Use the evidence-use pattern; only then consider a name for the governed relation |
| `AccessRole` | Permission or policy grouping | Use access, policy, status, or deontic pattern; do not mint a local system-role kind by suffix |
| `ProviderRole` in a signature | Relation position | Use `A.6.5` SlotSpec discipline; name a slot only if needed |
| `RoleEnactment` in source prose | Source wording around a `U.SystemRoleAssignment` plus a Work occurrence | Recover the exact actual performer through A.13 and let A.15.1 independently admit the Work; use F.6 only when the naming case expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment, and do not mint `U.RoleEnactment` |

#### F.8:4.4 - F.17 Row-Scope Consumption

F.8 consumes one named F.17 row and its declared use; it neither constitutes the row nor defines Bridge strength. F.17 keeps the row episteme, governed value, designations, cell, basis relation, any F.9 Bridge, edition relation, and publication package distinct. F.8 asks only whether `AdmissibleUse` covers the proposed naming use.

| Declared row use | F.8 admissible naming use | Other claims return to |
| --- | --- | --- |
| Naming-only | Shared prose label, glossary text, teaching label | The direct subject pattern for the claim actually needed—for example equivalence, assignment, performed Work, structural inference, or measurement equivalence. |
| System-role-kind designation naming | A designation may cite the row as a comparison aid after the local kind is recovered | The direct result for kind admission, cross-local kind identity, classification, or assignment. |
| System-role-kind-description naming | A label for a separately justified `SystemRoleKindDescription` may cite the row as a comparison aid | The direct result for kind identity, cross-local kind identity, or assignment; the separately justified description remains the object being named. |
| Measurement naming | Shared measurement label where units and procedure constraints remain visible | The measurement pattern for any claim of procedure interchange. |
| Type-structure naming | Name for an admitted structural relation under the row's invariants | `E.24.UK` for U-kind admission. |

If the row does not admit the proposed use, lower the name's use or repair the F.17 row and any needed F.9 relation. Attractive wording supplies neither a stronger use nor cross-local sameness.

#### F.8:4.5 - Accountable Decision Branch

Open this branch only when a receiving claim needs to cite, replay, or assign accountability to the mint-or-reuse decision occurrence itself. First recover that occurrence through the decision or choice pattern that admits it. The ordinary naming result remains valid without this branch.

Keep these objects distinct in the accountable branch:

- the governed value or relation and its subject pattern;
- the candidate expression, selected designation, and any alias;
- the effective naming `U.ReferenceScheme`, local-sense claim, optional `SchemeSenseCell`, and any obtaining two-participant `LocalSenseBasisRelation`;
- the decision or choice occurrence and the pattern that admits it;
- any C.2.1 decision-result episteme and the record or carrier that designates it;
- any F.18 NameCard, F.17 row, policy specification, policy identifier, publication occurrence, form, or carrier; and
- a selected bounded-model-use Structure only when its organization changes interpretation for this naming use.

When a result episteme is needed, use the full projection below:

```text
MintReuseDecisionResultEpisteme:
  DecisionResultEpistemeId:
  EntityOfConcernRef: [decision or choice occurrence already admitted by its direct pattern]
  DecisionGovernorLocator:
  DecisionPredicateRef:
  DecisionParticipantRefs: [actual participants with their meanings]
  DecisionApplicability:
  DecisionOccurrenceIdentityBasis:
  DecisionMakingWorkRef?: [separate A.15.1 Work only when current]
  DecisionOrChoiceResultRef?: [separate result, such as a C.11 ChoiceResult, only when current]
  CandidateExpression:
  GovernedValueOrRelationRef:
  GovernedKindOrRelationKindRef:
  GovernedValueSubjectPatternLocator:
  ProposedNamingUse:
  EffectiveNamingReferenceScheme: [U.ReferenceScheme carried by value]
  LocalSenseClaim:
  LocalSenseCellRef?: [only when a current SchemeSenseCell is needed]
  LocalSenseBasisRelationRef?: [only when the cell-to-basis-episteme relation obtains]
  SelectedModelUseStructureRef?: [only when a selected Structure changes this use]
  ReuseCandidateRefs?:
  SelectedDisposition:
  ResultingNamingRefs?: [only objects current after the disposition]
  NonAdmissibleOverread?: [only when admitted by `F.19`'s grounded-contribution test]
  ReopenCondition:
```

The block describes the result episteme. `EntityOfConcernRef` resolves to the decision or choice occurrence admitted through `DecisionGovernorLocator`; the predicate, participants, applicability, and identity basis show why that occurrence exists. `GovernedValueSubjectPatternLocator` identifies the pattern for the value being named. `NonAdmissibleOverread` is included only when admitted by `F.19`'s grounded-contribution test. A C.11 `ChoiceResult` and dated decision-making Work keep their direct identities and relations. If the occurrence and its governor cannot be recovered, do not instantiate the block: return the A.6.RCD `missing-governor` result. If no result episteme is needed, state the ordinary result and stop.

