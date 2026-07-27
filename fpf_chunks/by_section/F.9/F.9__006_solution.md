---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__006_solution.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:4 — Solution"
line_start: 89728
line_end: 89793
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "different <ReferenceScheme"
  - "exact F.17 SchemeSenseCell endpoints"
  - "inverse/composition checks"
  - "obtaining Bridge"
  - "optional CL evidence-strength shorthand"
  - "optional card"
  - "quantum/coarsening exit"
  - "relation-semantic profile"
  - "separate C.2.1 bounded-use claim"
---

### F.9:4 - Solution

Start with the two exact local senses, not with a context object, mapping table, or card. Resolve each endpoint as an F.17 `SchemeSenseCell` coordinate:

```text
<ReferenceScheme by value, LocalExpression, LocalSenseClaim>
```

For F.9, **semantic context** is Plain shorthand for the bounded interpretation basis recovered from one cell's `<ReferenceScheme, LocalSenseClaim>` projection. It is not a `U.Entity`, `U.BoundedContext`, selected model-use structure, project, scope, viewpoint, description, designator, or reference. Two expressions under the same projection are a designation question first. Different projections make a Bridge question possible but do not make a Bridge obtain.

When the two cells are from different semantic contexts, declare one relation-semantic `BridgePredicateProfile` and test it against their current meanings. Shared spelling, different schemes, a mapping implementation, a card, a registry entry, evidence, an assessment score, or publication establishes none of those facts by itself.

#### F.9:4.1 - Direct Bridge relation

`Bridge` is a direct species of `U.Relation`. Its reusable `RelationSignature` has exactly two participant meanings:

| SlotKind | ValueKind | refMode | Participant meaning |
| --- | --- | --- | --- |
| `SourceSenseCellSlot` | F.17 `SchemeSenseCell` coordinate | `SenseCellAddressRef` | The exact source local sense, resolving its by-value reference scheme, local expression, and local-sense claim. |
| `ReceivingSenseCellSlot` | F.17 `SchemeSenseCell` coordinate | `SenseCellAddressRef` | The exact receiving local sense used by the claimed semantic relation. |

No context, proposed use, use direction, correspondence rule for that use, permitted-loss tolerance, assertion, evidence item, policy, time value, card, publication, registry id, or carrier is a third participant.

An F.9-local `BridgePredicateProfile` is a by-value predicate declaration, not a U-kind, participant, card, claim, or evaluation result. Its identity-bearing content is only:

1. the `BridgeKind` and its kind-defined symmetry or endpoint orientation;
2. the exact source and receiving endpoint-sense readings, including their `senseFamily` readings where material;
3. the relation-kind-specific correspondence or difference condition;
4. the applicability and as-of basis for testing that condition;
5. the Boolean truth condition; and
6. every stop dependency whose absence prevents a truthful result.

The profile contains no receiving-use role, use direction, use-specific correspondence rule, permitted-loss tolerance, bounded-use proposition, assertion polarity, evidence-reliance classification, assurance claim, authorization, or receiving object.

`Bridge(SourceSenseCell, ReceivingSenseCell; BridgePredicateProfile)` obtains exactly when:

- both endpoint references resolve to exact F.17 `SchemeSenseCell` values;
- their semantic-context projections differ;
- the profile applies to those endpoint readings at its stated as-of basis;
- the current endpoint meanings satisfy its kind-specific correspondence or difference condition and Boolean truth condition; and
- every required dependency is present.

If an endpoint is unresolved, the projections are the same, a dependency is missing, or the predicate is false or unresolved, assert no positive occurrence and state the exact exit: ordinary designation, `unresolved SenseCell endpoint`, `same semantic context`, `missing Bridge dependency`, `Bridge predicate false`, or `Bridge predicate unresolved`.

The occurrence is identified by the exact endpoint cells together with the exact profile. For an asymmetric kind, the ordered source-to-receiving relation tuple is identity-bearing and an inverse claim requires another profile and occurrence. For a symmetric kind, swapping only the readable presentation of the same canonical endpoint pair does not create another occurrence. A changed endpoint or changed relation-semantic profile identifies another occurrence candidate. A changed proposed use, use direction, rule, tolerance, evidence path, reliance disposition, assurance claim, card, registry entry, publication, form, or carrier does not reidentify the fixed Bridge.

#### F.9:4.2 - Judge a bounded use separately

Once exact Bridge `b` obtains, state the proposed use in ordinary language before introducing FPF terms. Name:

- `u`: what the reader proposes to compare, substitute, translate, publish, or otherwise do;
- `d`: the exact source-to-receiving direction for that use;
- `r`: the use-specific correspondence rule;
- `t`: the semantic-loss tolerance for that use; and
- whether the claim is affirmative or negative.

The resulting C.2.1 claim asks whether `b` is suitable for `<u,d,r,t>`. Its exact EntityOfConcern is `b`; its ClaimGraph designates `u`, `d`, `r`, `t`, and polarity; its effective ReferenceScheme makes those designations interpretable. That C.2.1 triple identifies the claim episteme. Changing `u`, `d`, `r`, or `t` changes the claim, not the Bridge.

An affirmative claim is one premise for the proposed use. It is not a permission, authorization, evidence-provenance relation, reliance classification, assurance claim, decision, or occurrence of that use. A negative claim says that the Bridge is not suitable for the named use; it does not make the Bridge cease to obtain.

For ordinary evidence reliance below B.3's material-reliance threshold and with no assurance claim, recover the exact A.10 evidence-provenance graph relation by value and state its local `RelianceDisposition` for the same bounded use. Only `RelianceDisposition=pass` supports reliance on the affirmative claim for that exact use; `degrade` supports only its named narrower use, while `abstain`, `reopen`, `evidence-needed`, `blocked-current-use`, or `safety-case-required` supplies no passing classification for the attempted use.

Enter B.3 when the receiver makes an assurance claim or the proposed use meets B.3's material-reliance threshold. Decide first whether a current assurance claim exists. A met threshold requires the minimum reliance safety assurance record and contest boundary but creates no positive claim. Use a positive current B.3 assurance claim only when it exists, its record is sufficient, and it carries the same bounded assurance use. Otherwise state the exact no-assurance, insufficient-record, narrowed, rejected, withdrawn, abstaining, or blocked disposition and stop or narrow the use accordingly.

Neither an A.10 passing disposition nor a positive B.3 assurance claim is legal, policy, or deontic authorization. If authorization is needed, recover it under its direct governor. If a later claim says the use happened, recover the actual Work, assertion episteme, publication occurrence, direct relation, operation application, or other object under its own pattern; the role `u` in the bounded-use claim is not that occurrence.

