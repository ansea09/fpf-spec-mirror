---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:4"
section_title: "Solution (thumbnail)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__006_solution-thumbnail.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:4 — Solution (thumbnail)"
line_start: 39391
line_end: 39439
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

### B.3.5:4 - Solution (thumbnail)

CT2R‑LOG introduces a **two‑link discipline** around each canonical edge:

1. **Alias link (concept‑level).**
   **Working-Model relations** (e.g., `ut:ComponentOf`) are the public names for their exact direct relation principles. **`tv:AliasOf`** may point from the public relation kind to that principle for comparison and reuse; the alias defines neither an occurrence nor a whole.

2. **Grounding link (evidence‑level).**
   Each **edge instance** carries **`tv:groundedBy`**:

   * **MANDATORY** for **all published structural edges** (sub-properties of `ut:StructPartOf`): the target is one current C.2.1 construction-trace episteme in the `sum`, `set`, or `slice` form. It names the exact participants, direct relation occurrences, applicable construction rule, and identity or reidentification conditions already grounded under their direct patterns. **Set** `validationMode=axiomatic`; **`postulate` SHALL NOT be used for structural edges**. Neither the link nor the mode makes those facts obtain.
   * **Optional** for **epistemic edges** (e.g., `ConstituentOf`, `RepresentationOf`): if no `Γ_m` trace is appropriate, attach an **evidence object** whose admissibility is governed by the declared **`validationMode ∈ {inferential, postulate}`** (assurance rules).

2. **Validation flag (author intent).**
   Every declared edge or aggregation rule carries **`tv:validationMode`** with one of:
   * **`postulate`** — pragmatic working claim backed by observations;
   * **`inferential`** — reasoned consequence (proof outline);
   * **`axiomatic`** — the author declares that one inspectable construction account is the assurance basis for the assertion. This is an assurance posture, not a species of world-side relation and not an identity or timelessness guarantee.

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

When an inadequate working account requires a general diagnostic return to the exact subject construction, use `A.7.1`. That return may stop at a direct relation, role assignment, state/capability, work occurrence, holon recognition, or another subject owner without opening this structural CT2R specialization.

`workingModelOrConstructiveRepresentationRef` names the relation, trace, model, or representation being carried. `targetKindOrLogicalRepresentationRef` names the typed or logical target. `bridgeRef` and `CL_or_CLk` are mandatory when cross-context or kind-level movement is current. `preservedStructure` and `lostOrCollapsedStructure` state what survives the passage and what the published relation no longer carries. Evidence linkage remains with B.3 evidence and assurance governing patterns; proof linkage remains with the proof or mathematical governing pattern that is current. The unfolding block only makes the structure of the passage inspectable.

