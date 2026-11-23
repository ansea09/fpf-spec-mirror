---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__006_solution.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:4 — Solution"
line_start: 47501
line_end: 47570
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:4 - Solution

The Working-Model and Assurance layers name E.14's presentation order: the claim first, its needed support accessible underneath. When two models are being compared for abstraction or refinement, use B.5.MR's comparison of their admitted answers.

To choose the relations, ask which changes could leave your statement true while altering the reader’s decision. Holding an item’s registration fixed, it can move from a warehouse into an assembly. Holding the assembly fixed, responsibility for maintaining it can pass to another operator. Follow the part relations of the system, the constituent operations of a Method or the parts of performed Work as far as their arrangement affects the requested answer. Establish links between these accounts by the facts they assert, such as who performed the installation and which installed equipment the record describes. A direct fact about one relation can already settle a request confined to that relation.

Choose the distinctions to publish from the same question. Can the reader reach the required decision, with its grounds, in all the arrangements the model describes alike? Keep a missing distinction in the statement or in a grounding account accessible when it is needed. If the commissioned conclusion uses several assertions together, establish their compatibility for the items, times and uses it covers.

CT2R-LOG distinguishes an optional link between relation designations from the grounding link and validation flag required for each covered assertion:

1. **Alias link (lexical).**
   **`tv:AliasOf`** may link a local relation designation to the accepted Tech designation of the same relation in that use. The definition in :5 fixes both endpoints and the conditions for using this alternative label. Cite the relation pattern to recover the relation’s meaning.

2. **Grounding link (assurance).**
   Each relation assertion covered by this elected profile carries `tv:groundedBy` according to its relation kind:

   * **ComponentOf, PortionOf, or AspectOf** requires one current C.2.1 construction-trace episteme in the applicable `sum` or `slice` form and `validationMode=axiomatic`. PortionOf uses the measured-portion profile in `C.13:4.1.1`; AspectOf uses the facet profile. This requirement follows the asserted relation, including measured text portions, and does not make those two profiles interchangeable.
   * **Collection belonging under the collection's own rule** requires one current C.2.1 `C.13 set` trace and `validationMode=axiomatic`. The trace reports the collection, the entity, the already established relation, the rule for belonging, and the identity conditions. It does not make the entity a constructive part, make belonging obtain, or prove that separately grounded parthood is impossible.
   * **Other epistemic or constitutive edges** use the support appropriate to their claim: an admissible evidence object for `postulate`, a followable argument for `inferential`, or a qualifying C.13 construction account for `axiomatic`. Constructive grounding is optional in this branch; select the mode from the basis used for this assertion.

3. **Validation flag (author intent).**
   Every relation or aggregation rule covered by this profile carries `tv:validationMode` with one of:
   * **`postulate`** — pragmatic working claim backed by observations;
   * **`inferential`** — reasoned consequence with a followable argument; or
   * **`axiomatic`** — one inspectable construction account is the declared assurance basis.

The applicable branch above selects the allowed modes and grounding targets. The mode declares the author's justification posture; B.3.3 judges what that support establishes for the receiving use.

> **Relation, grounding, and assurance.**
> **Published relation claim:** `:PumpA ut:ComponentOf :Skid12`. Assess its expression properties under C.2.3 when that assessment matters to the use.
> **Grounding account:** the assertion links to `:trace_Γm_sum_456`, a C.2.1 episteme about the construction facts.
> **Assurance posture:** `tv:validationMode=axiomatic` is the author's declaration. B.3.3 assesses the grounding for the receiving claim and use; a level is published only through an applicable justified profile. The declaration does not alter formality or establish empirical adequacy.

#### B.3.5:4.1 - Inspect correspondence to a target kind or logical representation

When a constructive trace, Working-Model relation and target kind or logical representation must be used together, state the question and the direction of the inference. Consider the permitted source arrangements that a target description can represent. If it describes two different arrangements alike, see whether that difference could change the required answer. A dated entry certifying the installation of a pump of an approved class can establish that class for the installation. If it omits the unit identifier, several individual pumps may still fit the entry. For a claim about that unit, find its binding to the installation or give the narrower conclusion. A difference lost in the mapping can be immaterial to another question. An argument covering the relevant arrangements settles whether the inference holds.

The optional block records the correspondence and its limits. Use `A.22.CGUS` for a remaining question about potential continuations and their conditions.

```text
StructuralCT2RTypingGroundingUnfoldingStructureBlock:
  unfoldingStructureRef: independently selected A.22 structure, when needed
  workingModelOrConstructiveRepresentationRef:
  targetKindOrLogicalRepresentationRef:
  bridgeRef?:
  constructiveTraceRef?:
  preservedStructure:
  lostOrCollapsedStructure:
  CL_or_CLk?:
  admissibleReuse:
  blockedSubstitution?:
  evidenceOrProofLinkageRef?:
```

When the receiving use needs a selected A.22 structure, `unfoldingStructureRef` names it. Recover its constituents, obtaining relations, applied constraints and named selection/use frame under A.22.

`StructuralCT2RTypingGroundingUnfoldingStructure` is a local designator for that selected structure used to inspect this construction-to-typed/logical projection.

Any A.22.CGUS qualification is tested separately under its potential-continuation rule; a local name or record does not establish it. C.13 supplies constructive-trace content and C.3 the kind intent, extent and subkind content used.

When an inadequate working account requires general diagnostic recovery of the subject construction, use `A.7.1`. That return may stop at a relation, system-role assignment, state or capability, Work occurrence, holon recognition, or the pattern for another subject without opening this structural CT2R specialization.

`workingModelOrConstructiveRepresentationRef` names the relation, trace, model, or representation being carried. `targetKindOrLogicalRepresentationRef` names the typed or logical target. `bridgeRef` is required when this use claims or consumes an obtaining semantic Bridge under F.9 or a kind correspondence under C.3.3.

`CL_or_CLk` is required when the consumed assurance/calibration account requires that value. Entity, scheme, plane or notation changes alone establish no crossing; a same-sense unit conversion requires neither invented endpoints nor a Bridge. CL does not by itself authorize use.

`preservedStructure` and `lostOrCollapsedStructure` state what survives the passage and what the published relation no longer carries.

Evidence linkage remains with B.3 evidence and assurance subject patterns; proof linkage remains with the proof or mathematical subject pattern. The unfolding block only makes the structure of the passage inspectable.

