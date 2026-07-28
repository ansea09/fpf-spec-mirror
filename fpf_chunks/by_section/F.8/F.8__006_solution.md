---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__006_solution.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:4 — Solution"
line_start: 90125
line_end: 90214
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

Treat mint-or-reuse as a typed decision over a recovered candidate, not as a vote on wording. Use this compact relation:

```text
MintReuseDecision:
  CandidateExpressionSlot:
  BoundedContextSlot:
  RecoveredKindOrRelationSlot:
  LocalSenseRefSlot:
  ProposedUseSlot:
  ReuseCandidateRefSlot:
  DecisionKindSlot:
  DirectPatternRefs:
  NameDisciplineRefs:
  NonAdmissibleOverreadSlot:
  ReopenConditionSlot:
```

`DecisionKindSlot` is a local field for the result of this pattern. It does not create a new `U.*` kind.

Admissible decision kinds:

- `localPhraseOnly`;
- `reuseLocalSenseLabel`;
- `aliasOnly`;
- `reuseConceptSetRow`;
- `nameRoleDescription`;
- `nameDirectPatternValue`;
- `introducePolicyId`;
- `proposeConceptSetRow`;
- `proposeUKindCandidate`;
- `blockOrLowerUse`.

#### F.8:4.1 - Decision Targets

| If the candidate expression names... | F.8 decision | Direct governing pattern |
| --- | --- | --- |
| A one-off phrase after local repair | `localPhraseOnly` | `E.10` or direct governing pattern |
| An existing local sense inside one bounded context | `reuseLocalSenseLabel` | `F.1`, `F.2`, `F.3`, `F.5` |
| A wording variant for the same recovered meaning | `aliasOnly` | `F.5`, `F.13`, `F.18` |
| A cross-context reading already admitted by bridges | `reuseConceptSetRow` | `F.7`, `F.9` |
| A label for a role-description episteme describing one `U.Role` | `nameRoleDescription` | `F.4`, `F.5`, `F.18` |
| A status, evidence, source, requirement, publication, assurance, gate, decision, method, work, relation-position, characteristic, or architecture value | `nameDirectPatternValue` only after the direct pattern recovers the value | Direct governing pattern, then `F.5` or `F.18` if durable naming is current |
| A policy identifier | `introducePolicyId` or reuse with resolvable refs | `F.8:8.1`, plus the pattern governing the policy use |
| A recurring cross-context row not yet present | `proposeConceptSetRow` | `F.7`, `F.9` |
| A missing cross-family primitive | `proposeUKindCandidate` | `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, `F.18` |

#### F.8:4.2 - Decision Sequence

Use this order. Stop at the first result that fits the recovered kind and use.

1. **Recover the current claim.** Name the bounded context, local sense if known, and the kind or relation being claimed.
2. **Split mixed candidates.** If one expression covers role, status, evidence, work, method, measurement, or structure at once, split it before deciding.
3. **Check local reuse.** If one bounded context already has the needed local sense, reuse its label inside that context.
4. **Check role expression.** If the candidate describes one work-facing `U.Role`, use `F.4` and `F.5`. If it asserts assignment or performed work, use `A.2.1`, `F.6`, or `A.15.1`. If it is evidence, status, access, requirement, source, publication, assurance, gate, decision, or relation-position use, use the direct pattern.
5. **Check cross-context reuse.** If more than one context is current, use `F.9` bridge discipline and `F.7` Concept-Set row discipline. Reuse a row only for the row's admitted use.
6. **Check alias.** If the meaning is the same and only wording changes, use alias discipline. Do not let an alias change kind or scope.
7. **Check policy id.** If the candidate is a policy identifier, require `PolicyIdRef` discipline in `F.8:8.1`.
8. **Propose new row.** If the need recurs across contexts and bridges admit the intended use but no row exists, propose a small Concept-Set row.
9. **Propose new U-kind only rarely.** Use this only when the candidate is cross-family, irreducible to existing FPF values, governed by `E.24.UK`, and then accepted under the relevant A.8, A.11, C.3, E.9, and F.18 law.
10. **Block or lower.** If none of the above is true, keep the expression local, quote it as source wording, or lower the claim.

#### F.8:4.3 - Role Expression Boundary

A role expression becomes a durable role name only when it names one work-facing `U.Role` or the role-description episteme for that role in one bounded context.

| Source expression | Recovered case | F.8 result |
| --- | --- | --- |
| `ReviewerRole` in a review method | Work-facing role value needs a description and label | `nameRoleDescription`; use `F.4`, `F.5`, `F.18` when public |
| `Alice as reviewer` | Holder assigned to role for a window | Not a name decision until `A.2.1` recovers the assignment |
| `review happened` | Performed work | Use `A.15.1`; durable naming only if the work-kind name itself is current |
| `EvidenceRole` | Episteme used as evidence | Use evidence-use patterns; only then name the evidence-use relation if durable |
| `AccessRole` | Permission or policy grouping | Use access, policy, status, or deontic pattern; do not mint a `U.Role` by suffix |
| `ProviderRole` in a signature | Relation position | Use `A.6.5` SlotSpec discipline; name a slot if needed |
| `RoleEnactment` in source prose | Source wording around assignment plus work occurrence | Use `F.6`; do not mint `U.RoleEnactment` |

#### F.8:4.4 - Row Scope Consumption

F.8 consumes row scope; it does not define bridge strength. `F.9` declares bridges and `F.7` declares Concept-Set rows. F.8 asks whether the row's declared use is enough for the proposed name.

| Row use | F.8 admissible naming use | Non-admissible overread |
| --- | --- | --- |
| Naming-only | Shared prose label, glossary text, teaching label | assignment, performed work, structural inference, measurement equivalence |
| Role-description naming | RoleDescription label can cite the row as a comparison aid when one local `U.Role` remains primary | cross-context role assignment by row alone |
| Measurement naming | Shared measurement label where units and procedure constraints remain visible | procedure interchange without the measurement pattern |
| Type-structure naming | Name for an admitted structural relation under the row's invariants | universal U-kind without `E.24.UK` and direct decision-pattern admission |

If the row does not admit the intended use, lower the name's use or open the direct bridge or row repair. Do not strengthen a name because the wording is attractive.

