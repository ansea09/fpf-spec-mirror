---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:4"
section_title: "Solution (thumbnail)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__006_solution-thumbnail.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:4 — Solution (thumbnail)"
line_start: 35604
line_end: 35650
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
   **Working‑Model relations** (e.g., `ut:ComponentOf`) are **alias patterns** over a general constructional principle. Denote by **`tv:AliasOf`**.

2. **Grounding link (evidence‑level).**
   Each **edge instance** carries **`tv:groundedBy`**:

   * **MANDATORY** for **all structural edges** (sub-properties of `ut:StructPartOf`): the target is a valid **`Γ_m` trace** from **Compose-CAL** (one of `sum`, `set`, `slice`). **Set** `validationMode=axiomatic`; **`postulate` SHALL NOT be used for structural edges**.
   * **Optional** for **epistemic edges** (e.g., `ConstituentOf`, `RepresentationOf`): if no `Γ_m` trace is appropriate, attach an **evidence object** whose admissibility is governed by the declared **`validationMode ∈ {inferential, postulate}`** (assurance rules).

2. **Validation flag (author intent).**
   Every declared edge or aggregation rule carries **`tv:validationMode`** with one of:
   * **`postulate`** — pragmatic working claim backed by observations;
   * **`inferential`** — reasoned consequence (proof outline);
   * **`axiomatic`** — constructive grounding via a `Γ_m.*` composition.

> **F–G–R alignment.**
> **F** (the published *Fact*): `:PumpA ut:ComponentOf :Skid12`.
> **G** (its *Grounding*): `:e123 tv:groundedBy :trace_Γm_sum_456`.
> **R** (declared *Reliability mode*): `tv:validationMode=axiomatic` → inputs B.3.3’s **AssuranceLevel** assessment.

#### B.3.5:4.1 - Typing-Grounding Unfolding Structure Block

When a constructive trace, working-model relation, and target kind or logical representation must be carried together across contexts, use this block or cite an equivalent `A.22.CGUS` specialization. The block is useful when the reader must see the passage from constructional material to a typed or logical claim without treating a readable relation label as proof.

```text
TypingGroundingUnfoldingStructureBlock:
  unfoldingStructureRef: current TypingGroundingUnfoldingStructure record
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

`unfoldingStructureRef` names the current local structure record. `TypingGroundingUnfoldingStructure` is a local `A.22.CGUS` `U.Structure` specialization whose block is governed by B.3.5 for typing-grounding use; the A.22-level relation to that narrower specialization, when needed, is `specializedStructureRef?` on the generic CGUS record. It is not a root U-kind, not proof, not empirical evidence, not a work plan, and not a decision. C.13 contributes constructive-trace loci; C.3 contributes kind intent, extent, subkind, and bridge loci; neither C.13 nor C.3 creates separate authority for this block.

`workingModelOrConstructiveRepresentationRef` names the relation, trace, model, or representation being carried. `targetKindOrLogicalRepresentationRef` names the typed or logical target. `bridgeRef` and `CL_or_CLk` are mandatory when cross-context or kind-level movement is current. `preservedStructure` and `lostOrCollapsedStructure` state what survives the passage and what the published relation no longer carries. Evidence linkage remains with B.3 evidence and assurance governing patterns; proof linkage remains with the proof or mathematical governing pattern that is current. The unfolding block only makes the structure of the passage inspectable.

