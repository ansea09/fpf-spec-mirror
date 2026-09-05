---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__006_solution.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:4 — Solution"
line_start: 95673
line_end: 95744
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "C.3"
  - "E.10.ROLE"
  - "E.17.ID.CR"
  - "E.24.PUB"
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

For F.9, **semantic bounded context** is a Plain practice name for the local interpretation basis recovered from one exact cell's `<ReferenceScheme, LocalSenseClaim>` projection. It is not an entity, relation participant, selected model-use structure, project situation, scope, viewpoint, description, designator, or reference. Two expressions under the same projection remain with ordinary designation and scope operations. Different projections make a Bridge question possible but do not make a Bridge obtain.

When the two cells are from different semantic contexts, declare one relation-semantic `BridgePredicateProfile` and test it against their current meanings. Shared spelling, different schemes, a mapping implementation, a card, a registry entry, evidence, an assessment score, or publication establishes none of those facts by itself.

#### F.9:4.1 - Direct Bridge relation

`Bridge` is a direct species of `U.Relation`. Its reusable `RelationSignature` has exactly two participant meanings:

| SlotKind | ValueKind | refMode | Participant meaning |
| --- | --- | --- | --- |
| `SourceSenseCellSlot` | F.17 `SchemeSenseCell` coordinate | `SenseCellAddressRef` | The exact source local sense, resolving its by-value reference scheme, local expression, and local-sense claim. |
| `ReceivingSenseCellSlot` | F.17 `SchemeSenseCell` coordinate | `SenseCellAddressRef` | The exact receiving local sense used by the claimed semantic relation. |

Only the two endpoint meanings are RelationSignature participants. `CL`, Loss Notes, `U.ClaimScope`, an admitted-use qualifier, evidence, counterexamples, policy, time or as-of values, `BoundedModelUseStructure`, description, Card, publication, registry identifier, form, and carrier are qualifiers or neighboring objects. No proposed-use field, use direction, use-specific rule, permitted-loss tolerance, assertion, or reliance result is a third participant.

The reusable Bridge declaration is one independently constituted C.2.1 episteme whose exact EntityOfConcern is the direct `Bridge` relation kind. The same declaration episteme is used relation-facing as the compatible `RelationSignature`; its two SlotSpecs declare participant meanings but create neither endpoint nor occurrence. The relation kind, declaration episteme, RelationSignature use, SlotSpecs, actual cells, obtaining occurrence, assertion, occurrence-description episteme, Card, and publication remain distinct.

An F.9-local `BridgePredicateProfile` is a by-value predicate declaration, not a U-kind, participant, card, claim, or evaluation result. Direction is stated in the Bridge kind and endpoint orientation when the predicate is asymmetric. Its identity-bearing content is only:

1. the `BridgeKind` and its kind-defined symmetry or endpoint orientation;
2. the exact source and receiving endpoint-sense readings, including their `senseFamily` readings where material;
3. the relation-kind-specific congruence, difference, or loss condition, distinct from observed Loss Notes and a proposed use's permitted-loss tolerance;
4. the applicability and as-of basis for testing that condition;
5. the Boolean truth condition; and
6. every stop dependency whose absence prevents a truthful result.

The profile contains no proposed-use field, use direction, use-specific correspondence rule, permitted-loss tolerance, bounded-use proposition, assertion polarity, evidence-reliance classification, assurance claim, authorization, or receiving object.

`Bridge(SourceSenseCell, ReceivingSenseCell; BridgePredicateProfile)` obtains exactly when:

- both endpoint references resolve to exact F.17 `SchemeSenseCell` values;
- their semantic-context projections differ;
- the profile applies to those endpoint readings at its stated as-of basis;
- the current endpoint meanings satisfy its kind-specific correspondence or difference condition and Boolean truth condition; and
- every required dependency is present.

If an endpoint is unresolved, the projections are the same, a dependency is missing, or the predicate is false or unresolved, assert no positive occurrence and state the exact exit: ordinary designation, `unresolved SenseCell endpoint`, `same semantic context`, `missing Bridge dependency`, `Bridge predicate false`, or `Bridge predicate unresolved`.

**Admitted-use qualifier.** The Bridge declaration admits this relation only as the semantic-correspondence or semantic-difference premise for a comparison, explanation, translation, naming, or other bounded-use claim. Its nearest non-use is equally explicit: the Bridge alone licenses no substitution and creates no scope result, model-use crossing, local system-role kind, assignment occurrence, Work, evidence authority, status transfer, U-kind admission, publication, or other subject relation. This readable use boundary is a declaration or description qualifier; it is neither a participant nor profile identity and grants no specific use.

**Non-optional occurrence identity and recurrence rule.** `BridgeOccurrenceIdentityRule` identifies the occurrence by the exact endpoint cells together with the exact profile. For an asymmetric kind, the ordered source-to-receiving tuple is identity-bearing and an inverse relation requires another profile and directed occurrence. For a symmetric kind, swapping only the readable presentation of the same canonical endpoint pair does not create another occurrence. A changed endpoint or changed relation-semantic profile identifies another candidate.

A Bridge is non-recurrent for one fixed canonical endpoint tuple and exact profile: at most one occurrence has that identity. Repeated tests, assertions, descriptions, Cards, registry rows, or publications neither split nor repeat it. A later applicability or as-of basis changes the profile and therefore opens another occurrence candidate. If a claimed lapse and resumption cannot be represented by an endpoint or profile change, stop at `missing Bridge recurrence basis` rather than inventing two occurrences with one identity. Changed proposed use, direction, rule, tolerance, evidence path, reliance disposition, assurance claim, Card, registry entry, publication, form, or carrier never reidentifies or recurs the fixed Bridge.

#### F.9:4.2 - Judge a bounded use separately

Once exact Bridge `b` obtains, state the proposed use in ordinary language before introducing FPF terms. Name:

- `u`: what the reader proposes to compare, substitute, translate, publish, or otherwise do;
- `d`: the exact source-to-receiving direction for that use;
- `r`: the use-specific correspondence rule;
- `t`: the semantic-loss tolerance for that use; and
- whether the claim is affirmative or negative.

The resulting C.2.1 claim asks whether `b` is suitable for `<u,d,r,t>`. Its exact EntityOfConcern is `b`; its ClaimGraph designates `u`, `d`, `r`, `t`, and polarity; its effective ReferenceScheme makes those designations interpretable. That C.2.1 triple identifies the claim episteme. Changing `u`, `d`, `r`, or `t` changes the claim, not the Bridge.

An affirmative claim is one premise for the proposed use. It is not a permission, authorization, evidence-provenance relation, reliance classification, assurance claim, decision, or occurrence of that use. A negative claim says that the Bridge is not suitable for the named use; it does not make the Bridge cease to obtain.

For ordinary evidence reliance, recover the exact A.10 evidence-provenance relation and local `RelianceDisposition` for the same bounded use. Only `pass` supports reliance on the affirmative claim for that use; `degrade` supports only its named narrower use, while `abstain`, `reopen`, `evidence-needed`, `assurance-needed`, or `blocked-current-use` supplies no passing classification.

Use B.3 only when an actual named assurance claim about the proposed use is current. Require its result for the same bounded assurance use; a non-positive disposition stops or narrows that use. A direct domain rule may require the claim, but the Bridge, display, consequence, or A.10 disposition does not create it.

Neither an A.10 passing disposition nor a B.3 `AssuranceResult` with `disposition=supported-for-use` is legal, policy, or deontic authorization. If authorization is needed, recover it under its direct pattern. If a later claim says the use happened, recover the actual Work, assertion episteme, publication occurrence, direct relation, operation application, or other object under its own pattern; the `u` designation in the ClaimGraph names the proposed use and is not that occurrence.

