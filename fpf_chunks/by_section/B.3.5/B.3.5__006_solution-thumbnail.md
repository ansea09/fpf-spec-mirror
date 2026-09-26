---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:4"
section_title: "Solution (thumbnail)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__006_solution-thumbnail.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:4 — Solution (thumbnail)"
line_start: 42456
line_end: 42507
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:4 - Solution (thumbnail)

CT2R‑LOG introduces a **two‑link discipline** and a **validation flag** around each canonical edge:

1. **Alias link (concept‑level).**
   **Working-Model relations** (e.g., `ut:ComponentOf`) are the public names for their exact direct relation principles. **`tv:AliasOf`** may point from the public relation kind to that principle for comparison and reuse; the alias defines neither an occurrence nor a whole.

2. **Grounding link (assurance level).**
   Each relation assertion covered by this elected profile carries `tv:groundedBy` according to its direct relation kind:

   * **Structural parthood** (`ComponentOf`, `PortionOf`, or `AspectOf`) requires one current C.2.1 construction-trace episteme in the applicable `sum` or `slice` form and `validationMode=axiomatic`. `postulate` is not available for this branch.
   * **Collection belonging under the collection's own rule** requires one current C.2.1 `C.13 set` trace and `validationMode=axiomatic`. The trace reports the collection, the entity, the already established relation, the rule for belonging, and the identity conditions. It does not make the entity a constructive part, make belonging obtain, or prove that separately grounded parthood is impossible.
   * **Other epistemic or constitutive edges** may use an admissible evidence object or logical argument under `validationMode ∈ {inferential, postulate}` when no constructive trace is appropriate.

3. **Validation flag (author intent).**
   Every relation or aggregation rule covered by this profile carries `tv:validationMode` with one of:
   * **`postulate`** — pragmatic working claim backed by observations;
   * **`inferential`** — reasoned consequence with a followable argument; or
   * **`axiomatic`** — one inspectable construction account is the declared assurance basis.

The direct branch above selects which modes and grounding targets are allowed. The flag is an assurance posture, not a species of world-side relation and not an identity or timelessness guarantee.

> **F–G–R alignment.**
> **F** (the published relation claim): `:PumpA ut:ComponentOf :Skid12`.
> **G** (its inspectable grounding account): the assertion links to `:trace_Γm_sum_456`, a C.2.1 episteme about the exact direct construction facts.
> **Assurance posture:** `tv:validationMode=axiomatic` is the author's declaration. B.3.3 assesses the actual grounding for the receiving claim and use; a level is published only through an applicable justified profile. The declaration does not alter formality or establish empirical adequacy.

#### B.3.5:4.1 - Structural CT2R Typing-Grounding Unfolding Structure Block

When a constructive trace, working-model relation, and target kind or logical representation must be carried together across contexts, use this block or cite an equivalent `A.22.CGUS` specialization. The block is useful when the reader must see the passage from constructional material to a typed or logical claim without treating a readable relation label as proof.

```text
StructuralCT2RTypingGroundingUnfoldingStructureBlock:
  unfoldingStructureRef: exact independently selected A.22 structure, when needed
  workingModelOrConstructiveRepresentationRef:
  targetKindOrLogicalRepresentationRef:
  bridgeRef?:
  constructiveTraceRef?:
  preservedStructure:
  lostOrCollapsedStructure:
  CL_or_CLk?:
  admissibleReuse:
  blockedSubstitution:
  evidenceOrProofLinkageRef?:
```

`unfoldingStructureRef` names an independently selected A.22 structure; this block is a record describing its use. Recover the exact constituents, obtaining relations, applied constraints and named selection/use frame. `StructuralCT2RTypingGroundingUnfoldingStructure` is a local designator for the selected structure used to inspect this construction-to-typed/logical projection. Any A.22.CGUS qualification is tested separately under its potential-continuation rule; a local name or record does not establish it. C.13 supplies constructive-trace content and C.3 the kind intent, extent and subkind content actually used. The record creates no proof, empirical evidence, Work plan or decision.

When an inadequate working account requires general diagnostic recovery of the exact subject construction, use `A.7.1`. That return may stop at a direct relation, system-role assignment, state or capability, Work occurrence, holon recognition, or the pattern for another subject without opening this structural CT2R specialization.

`workingModelOrConstructiveRepresentationRef` names the relation, trace, model, or representation being carried. `targetKindOrLogicalRepresentationRef` names the typed or logical target. `bridgeRef` is required when this use actually claims or consumes an obtaining semantic Bridge under F.9 or a kind correspondence under C.3.3. `CL_or_CLk` is required when the consumed assurance/calibration account requires that value. Entity, scheme, plane or notation changes alone establish no crossing; a same-sense unit conversion requires neither invented endpoints nor a Bridge. CL does not by itself authorize use. `preservedStructure` and `lostOrCollapsedStructure` state what survives the passage and what the published relation no longer carries. Evidence linkage remains with B.3 evidence and assurance subject patterns; proof linkage remains with the proof or mathematical subject pattern that is current. The unfolding block only makes the structure of the passage inspectable.

