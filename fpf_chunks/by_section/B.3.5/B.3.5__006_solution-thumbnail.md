---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:4"
section_title: "Solution (thumbnail)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__006_solution-thumbnail.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:4 — Solution (thumbnail)"
line_start: 38617
line_end: 38668
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:4 - Solution (thumbnail)

CT2R‑LOG introduces a **two‑link discipline** around each canonical edge:

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
> **R** (the author's declared assurance posture): `tv:validationMode=axiomatic` → one input to B.3.3's **AssuranceLevel** assessment; it does not alter F.

#### B.3.5:4.1 - Structural CT2R Typing-Grounding Unfolding Structure Block

When a constructive trace, working-model relation, and target kind or logical representation must be carried together across contexts, use this block or cite an equivalent `A.22.CGUS` specialization. The block is useful when the reader must see the passage from constructional material to a typed or logical claim without treating a readable relation label as proof.

```text
StructuralCT2RTypingGroundingUnfoldingStructureBlock:
  unfoldingStructureRef: current StructuralCT2RTypingGroundingUnfoldingStructure record
  workingModelOrConstructiveRepresentationRef:
  targetKindOrLogicalRepresentationRef:
  bridgeRef?:
  constructiveTraceRef?:
  preservedStructure:
  lostOrCollapsedStructure:
  CL_or_CLk:
  admissibleReuse:
  blockedSubstitution:
  evidenceOrProofLinkageRef?:
```

`unfoldingStructureRef` names the current local structure record. `StructuralCT2RTypingGroundingUnfoldingStructure` is a local `A.22.CGUS` `U.Structure` specialization whose block is governed by B.3.5 only for structural construction-to-typed/logical projection; the A.22-level relation to that narrower specialization, when needed, is `specializedStructureRef?` on the generic CGUS record. It is not a root U-kind, proof, empirical evidence, work plan, decision, or general ontology-return structure. `C.13` contributes constructive-trace loci; `C.3` contributes kind intent, extent, subkind, and bridge loci; neither creates separate authority for this block.

When an inadequate working account requires general diagnostic recovery of the exact subject construction, use `A.7.1`. That return may stop at a direct relation, system-role assignment, state or capability, Work occurrence, holon recognition, or the pattern for another subject without opening this structural CT2R specialization.

`workingModelOrConstructiveRepresentationRef` names the relation, trace, model, or representation being carried. `targetKindOrLogicalRepresentationRef` names the typed or logical target. `bridgeRef` and `CL_or_CLk` are mandatory when cross-context or kind-level movement is current. `preservedStructure` and `lostOrCollapsedStructure` state what survives the passage and what the published relation no longer carries. Evidence linkage remains with B.3 evidence and assurance subject patterns; proof linkage remains with the proof or mathematical subject pattern that is current. The unfolding block only makes the structure of the passage inspectable.

