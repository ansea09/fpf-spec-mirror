---
chunk_kind: "child"
pattern_id: "A.3.4.P"
pattern_title: "Transformation Wording Repair: Recover Objects and Claims"
section_id: "A.3.4.P:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4.P/A.3.4.P__006_archetypal-grounding.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "A.3.4.P — Transformation Wording Repair: Recover Objects and Claims"
  - "A.3.4.P:5 — Archetypal Grounding"
line_start: 13971
line_end: 14013
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30.ASV"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.20"
  - "E.24"
  - "E.8"
  - "F.19"
keywords:
  - "actual subject facts"
  - "and continuity rule"
  - "and other neighboring claims through exact governors"
  - "and routing flow structure"
  - "boundary"
  - "distinguishing performed-work or other direct actor-side claims from differently typed influence sources"
  - "evidence"
  - "method"
  - "publication"
  - "representation"
  - "transformation ontic precision restoration. Repairs change-situation wording by grounding any actual U.Transformation in its changed referent"
  - "work"
---

### A.3.4.P:5 - Archetypal Grounding

#### A.3.4.P:5.1 - Refrigerator functional diagram

A design reader wants to trace the connections on a single-stage vapour-compression schematic. Its arrows show the refrigerant path. Its caption says, “The refrigeration circuit moves heat through the cycle.” An operator may read the same words while asking whether heat actually left the compartment during a particular interval.

For the design reader, identify the compressor, condenser, expansion and evaporator loci and their connections in the selected `TransformationFlowStructure`. The same schematic can describe a unit that stood idle throughout the operator’s interval. For the operating question, establish the relevant heat transfer over that interval from the operating conditions and evidence that can distinguish the answer. Where the use of the caption is unknown, retain those readings until the surrounding account or the recipient identifies the intended claim.

#### A.3.4.P:5.2 - Neural-network block

Source wording says: "The attention block transforms activations in the model pipeline."

Repair: the block may be an architecture locus or module allocation. For a claimed action, apply the dated-Work or non-Work test in 4.4 and establish any Work-to-activation relation required by the use. A design organization, Method, toolchain or communication System that influenced the block keeps its own kind and influence relation. Activation and tensor-shape claims use their participant, port, operation-application or signature relations. An episteme describing an admitted attention Method may be a MethodDescription under A.3.2; C.29 governs a mathematical-representation use when one is made. The pipeline may be a transformation-flow structure. Use the applicable evidence or evaluation pattern when relying on a benchmark or ablation result.

#### A.3.4.P:5.3 - CRISPR editing workflow

Source wording says: "The guide-selection workflow changes the target gene."

Repair: the target-gene edit is only a candidate `U.Transformation` until the biological referent, edit boundary, boundary conditions, actual sequence and direct-relation facts, and reidentification rule establish one occurrence. Guide selection may be method, method description, work plan, evidence-facing table, or performed lab work according to the current claim.

#### A.3.4.P:5.4 - Evidence path near a plant change

Source wording says: "The evidence path lets the valve-change flow proceed."

Repair: identify the action meant by *proceed* and the condition the evidence is claimed to satisfy. Apply the governing rule to the available facts, and use `A.22.CGUS` if availability or ordering remains unclear. Preserve any established `A.10` provenance relation for the named claim. Use `A.3.4` only if an actual valve-change occurrence is also asserted.

#### A.3.4.P:5.5 - Filled minimal repair note

```text
TransformationWordingRepair:
  EncounteredWording: "the refrigeration circuit moves heat through the cycle"
  WorkingConcern: the design reader needs to locate the four stages in the supplied schematic and follow their connections.
  RecoveredEntityOfConcern: `RefrigeratorHeatTransferFlowStructure-1`, the selected `TransformationFlowStructure` over the compressor, condenser, expansion, and evaporator transformation loci.
  ActualTransformationDisposition: no actual occurrence claim is made; the current object is the selected `RefrigeratorHeatTransferFlowStructure-1`.
  NeighboringClaimAndExactRelation: the arrows in the supplied schematic connect the four named loci in refrigerant-flow order. The operator’s question also requires evidence about the interval of operation.
  GoverningPattern: `E.18` governs `RefrigeratorHeatTransferFlowStructure-1`; use `A.3.4` when a claim about an actual component occurrence needs its basis established.
  RetainedUse: "circuit" may remain ordinary domain wording for `RefrigeratorHeatTransferFlowStructure-1`; the source's heat-transfer claim remains unresolved.
  StopOrReturnCondition: use the selected structure for the recovered structural question; if the receiving use needs the heat-transfer claim, recover its participants and relation under the relevant subject rules. A later actual-occurrence claim still needs the A.3.4 occurrence basis.
  RemainingReaderUse: use `E.18` for `RefrigeratorHeatTransferFlowStructure-1`; open the applicable subject pattern when an additional claim is needed.
```

For the designer, the repaired caption reads “Follow the refrigerant from the compressor to the condenser, through the expansion device to the evaporator, and back to the compressor.” If the supplied drawing shows only the four positions, identify them and obtain the connections before claiming a path. To determine whether heat left the compartment during the operator’s interval, use evidence of operation during that interval.

