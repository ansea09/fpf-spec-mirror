---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__006_solution.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:4 — Solution"
line_start: 91849
line_end: 91961
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "A.8"
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
  - "F.7"
  - "F.9"
keywords:
  - "decision lattice"
  - "minting new U-kinds"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:4 - Solution

Treat mint-or-reuse as a typed disposition over an already recovered candidate, never as a vote on wording. Keep the following objects distinct:

- the exact governed value or relation and its direct pattern;
- the candidate expression, any selected designation, and any alias;
- the effective naming `U.ReferenceScheme`, exact local-sense claim, optional `SchemeSenseCell`, and any actual two-participant `LocalSenseBasisRelation`;
- the mint-or-reuse decision occurrence;
- any C.2.1 decision-result episteme and any record or carrier that designates it;
- any F.18 NameCard, F.17 row, policy specification, policy identifier, publication occurrence, form, or carrier; and
- an independently selected bounded-model-use Structure only when its organization changes interpretation for this exact naming use.

Ordinary use may stop with a readable disposition and no durable decision object. Materialize a decision occurrence reference or result episteme only when a receiving claim needs citation, replay, or accountability. When a C.2.1 result episteme is current, use this compact readable projection of its claim graph:

```text
MintReuseDecisionResultEpisteme:
  DecisionResultEpistemeId:
  EntityOfConcernRef: [the separately identified mint-or-reuse decision occurrence]
  CandidateExpression:
  GovernedValueOrRelationRef:
  GovernedKindOrRelationKindRef:
  DirectGoverningPatternRef:
  ProposedNamingUse:
  EffectiveNamingReferenceScheme: [U.ReferenceScheme carried by value]
  LocalSenseClaim:
  LocalSenseCellRef?: [only when an independently current SchemeSenseCell is needed]
  LocalSenseBasisRelationRef?: [only when the exact cell-to-basis-episteme relation obtains]
  SelectedModelUseStructureRef?: [only when an independently selected Structure changes this use]
  ReuseCandidateRefs?:
  SelectedDisposition:
  ResultingNamingRefs?: [only objects independently current after the disposition]
  NonAdmissibleOverread:
  ReopenCondition:
```

The block describes the result episteme; it is not the decision occurrence. `EntityOfConcernRef` resolves to that occurrence, while the remaining fields designate claims in the episteme's `U.ClaimGraph`. A record identifier, completed field set, NameCard, row, or publication creates neither the decision occurrence nor the governed value. If no result episteme is needed, apply the same distinctions in prose without creating a record.

Admissible dispositions are:

- `localPhraseOnly`;
- `reuseExistingDesignation`;
- `aliasOnly`;
- `reuseDirectPatternName`;
- `reuseAdmittedTermRow`;
- `nameRoleDescription`;
- `openDurableNamingSettlement`;
- `proposePublicTermRow`;
- `introducePolicyIdentifier`;
- `proposeUKindCandidate`; and
- `blockOrLowerUse`.

These are F.8 result labels, not new `U.*` kinds. A stronger result opens its direct owner; it does not itself mint the corresponding card, row, identifier, policy specification, relation occurrence, or U-kind.

#### F.8:4.1 - Decision Targets

| If the candidate expression designates... | Smallest F.8 disposition | Direct governing pattern |
| --- | --- | --- |
| A one-off phrase after local repair | `localPhraseOnly` | `E.10` or the direct governing pattern |
| An existing selected designation for the exact governed value and use | `reuseExistingDesignation` | The direct pattern, with `F.1`, `F.2`, and `F.3` for local-sense discovery and `F.5` or `F.18` only if naming settlement work is separately current |
| A wording variant for the same exact value, kind, scope, occurrence identity, and use | `aliasOnly` | `F.5`, `F.13`, `F.18` |
| An adequate name already supplied by the direct subject pattern | `reuseDirectPatternName` | The direct governing pattern |
| A cross-local or public reading already admitted by one exact F.17 row | `reuseAdmittedTermRow` only for its declared use | `F.17`; `F.9` only when an actual Bridge between exact cells is relied on |
| A label for a RoleDescription episteme describing one independently governed work-facing `U.Role` | `nameRoleDescription` | `A.2`, `F.4`, `F.5`; `F.18` if durable naming is current |
| A status, evidence, source, requirement, publication, assurance, gate, decision, method, Work, relation-position, characteristic, architecture, access, or policy value | `reuseDirectPatternName`, or `openDurableNamingSettlement` only after that value is recovered | Direct governing pattern, then `F.5` or `F.18` when needed |
| A recurring durable naming settlement not served by lighter dispositions | `openDurableNamingSettlement` | `F.14`, then `F.18`; a NameCard is optional until its own enduring-use gate passes |
| A public, Core-facing, durable, or cross-local term not covered by a current row | `proposePublicTermRow` | `F.17` after the exact F.18 inputs and row threshold are current |
| A policy identifier | reuse the current identifier or `introducePolicyIdentifier` with separately resolvable objects | `F.8:8.1`, plus the pattern governing the policy use |
| A missing cross-family primitive | `proposeUKindCandidate` | `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, `F.18` |

#### F.8:4.2 - Decision Sequence

Use this order and stop at the first disposition that supports the exact proposed use without hiding a governed distinction.

1. **Recover the four starting facts.** Name one candidate expression, one exact already-governed value or relation, its direct pattern, and one proposed use. If the value or obtaining relation is not independently current, stop and return to the direct pattern; F.8 cannot establish it.
2. **Split mixed candidates.** If one expression covers role, status, evidence, Work, method, measurement, policy, source, publication, or structure at once, split it into separate `<governed value, proposed use>` decisions.
3. **State exact semantic locality.** Carry the effective naming `U.ReferenceScheme` by value and state the local-sense claim. Cite a `SchemeSenseCell` and its exact `LocalSenseBasisRelation` only when those independently governed objects are current. Cite a selected bounded-model-use Structure only when its organization changes interpretation for this use.
4. **Apply F.14 and try a local phrase.** If ordinary local wording supports the use, choose `localPhraseOnly` and stop.
5. **Try an existing designation.** Reuse it only when exact value, kind, scope, occurrence identity, local-sense claim, and proposed use match.
6. **Try an alias.** Use `aliasOnly` when the governed meaning is unchanged and lineage can expose the wording variation. An alias may not change kind, scope, occurrence identity, use, or authority.
7. **Try the direct-pattern name.** Use the name already supplied by the exact role, status, evidence, policy, method, Work, relation, or other subject owner. Route work-facing role labels through `A.2`, `F.4`, and `F.5`; route assignment or performed Work through `A.2.1`, `F.6`, and `A.15.1` rather than naming.
8. **Try one admitted F.17 row.** Reuse only the row's declared `AdmissibleUse`. Local-sense reuse does not imply cross-local sameness; a row and equal spelling create no F.9 Bridge.
9. **Open only the next naming object that pays for itself.** A stable local address may justify a cell; an enduring naming settlement may justify a NameCard; a public/Core/durable/cross-local need may justify an F.17 row. None implies the next object.
10. **Introduce a policy identifier only for a recovered policy specification.** Keep the identifier, specification, mint decision occurrence, and result episteme or record distinct.
11. **Propose a new U-kind only rarely.** Require cross-family recurrence, irreducibility to existing FPF values or relations, `E.24.UK`, and the relevant A.8, A.11, C.3, E.9, and F.18 admission basis. F.8 only routes the proposal.
12. **Block or lower.** If no disposition is justified, keep the expression local, quote it as source wording, or lower the claim.

#### F.8:4.3 - Role Expression Boundary

A role expression becomes a durable role name only when the direct role owner has independently recovered one work-facing `U.Role`, or F.4 has constituted the RoleDescription episteme for that role. The naming ReferenceScheme interprets the expression; it neither supplies a role value nor assigns a holder.

| Source expression | Recovered case | F.8 result |
| --- | --- | --- |
| `ReviewerRole` in a review method | Work-facing role value needs a description and label | `nameRoleDescription`; use `A.2`, `F.4`, `F.5`, and `F.18` only when durable/public use is current |
| `Alice as reviewer` | Holder assigned to a role for a window | Not a name decision until `A.2.1` recovers the assignment |
| `review happened` | Dated performed Work | Use `A.15.1`; durable naming only if the Work-kind designation itself is current |
| `EvidenceRole` | Episteme used as evidence | Use evidence-use patterns; only then consider a name for the exact governed value or relation |
| `AccessRole` | Permission or policy grouping | Use access, policy, status, or deontic pattern; do not mint a `U.Role` by suffix |
| `ProviderRole` in a signature | Relation position | Use `A.6.5` SlotSpec discipline; name a slot only if needed |
| `RoleEnactment` in source prose | Source wording around assignment plus Work occurrence | Use `F.6`; do not mint `U.RoleEnactment` |

#### F.8:4.4 - F.17 Row-Scope Consumption

F.8 consumes one exact F.17 row and its declared use; it does not constitute the row or define Bridge strength. F.17 keeps the row episteme, governed value, designations, cell, basis relation, any F.9 Bridge, edition relation, and publication package distinct. F.8 asks only whether the row's `AdmissibleUse` covers the proposed naming use.

| Declared row use | F.8 admissible naming use | Non-admissible overread |
| --- | --- | --- |
| Naming-only | Shared prose label, glossary text, teaching label | equivalence, assignment, performed Work, structural inference, measurement equivalence |
| Role-description naming | RoleDescription label may cite the row as a comparison aid while one local `U.Role` remains primary | cross-local role identity or assignment by row alone |
| Measurement naming | Shared measurement label where units and procedure constraints remain visible | procedure interchange without the measurement pattern |
| Type-structure naming | Name for an admitted structural relation under the row's invariants | universal U-kind without `E.24.UK` and direct admission |

If the row does not admit the proposed use, lower the name's use or repair the exact F.17 row and any required F.9 relation. Do not strengthen a name because the wording is attractive, and do not infer cross-local sameness from local-sense reuse.

