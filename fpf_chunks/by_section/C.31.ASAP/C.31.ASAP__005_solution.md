---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Architecture Scale-Amenability Preference"
section_id: "C.31.ASAP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__005_solution.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.31.ASAP — Architecture Scale-Amenability Preference"
  - "C.31.ASAP:4 — Solution"
line_start: 60981
line_end: 61131
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18.1"
  - "C.19.1"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.31"
  - "C.31.RSA"
  - "C.32"
  - "C.32.ACS"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "RG"
  - "ScaleClaimTriage"
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "platform scale claim"
  - "scale amenability"
  - "scale variable"
  - "scale window"
  - "source-return condition"
  - "waiver reason"
---

### C.31.ASAP:4 - Solution

C.31.ASAP specializes scale-amenability preference for architecture alternatives. It applies when an architecture alternative set, scale variable or scale window, and claimed preference under scale are named.

#### C.31.ASAP:4.1 - Applicability fields

C.31.ASAP applies only when all of the following are present:

1. a declared architecture alternative set, described holon, exact `U.ClaimScope`, and relevant A.2.6 `U.ContextSlice` membership;
2. a declared scale variable or scale window;
3. a claimed preference under scale;
4. slope evidence, scale-probe evidence, or a no-probe reason;
5. an expected stable or improving structure, exception-growth risk, or source-return condition that changes the next architecture move.

If those fields are absent, keep the claim in `C.31` as a temporal or scale-sensitive characteristic cue, in `C.31.RSA` as report-only accounting, in `C.29` as a bounded lens-use output, or in ordinary architecture prose.

#### C.31.ASAP:4.2 - `ScaleClaimTriage`

Use `ScaleClaimTriage` before any heavier scale audit:

```text
ScaleClaimTriage:
  architectureAlternativeSetRef:
  describedHolonRef:
  claimScopeRef:
  selectedContextSliceRefs:
  modelUseStructureRef?:
  architectureClaimRef?:
  scaleVariableRef:
  scaleWindowRef:
  claimedPreferenceUnderScale:
  slopeEvidenceRef?:
  scaleProbeEvidenceRef?:
  noProbeReason?:
  expectedStableOrImprovingStructure:
  exceptionGrowthRisk:
  sourceReturnCondition:
  admissibleUse:
  nonAdmissibleUse:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

The triage is complete enough when it states the next admissible architecture move and the nearest blocked overread. It may stop at local guidance when no comparison, publication, assurance, selected-set, or decision use is being made.

`claimScopeRef` designates one exact `U.ClaimScope`; `selectedContextSliceRefs` records the A.2.6 membership relevant to this use. A scale window is the range of the scale variable for which the preference is claimed, not a substitute for either scope object. `modelUseStructureRef` is optional and is filled only when an independently selected A.1.1 `BoundedModelUseStructure` changes the interpretation of this exact preference use. A generic bounded-context label creates none of those values or relations.

#### C.31.ASAP:4.3 - Architecture scale-preference rule

When architecture alternatives satisfy the same safety boundary, law-domain boundary, and assurance boundary, prefer the alternative whose reusable functional-structure, flow-structure, control-structure, module-interface, work-template, and evidence-package structure and learning-transfer slopes remain stable or improve over the declared scale window, unless an `ArchitectureScaleAuditRecord@Project` records a bounded exception.

This is not a selector result. If an alternative set, shortlist, selected set, local choice, gate, or decision is being claimed, use `G.5`, `G.9`, `C.11`, `A.21`, or the governing pattern. C.31.ASAP governs only the scale-preference claim and its boundary.

A scale-preference claim may inform `C.32` candidate generation or supply one input to an `A.19.CPM` comparison by naming the scale variable, scale window, expected stable or improving structure, exception-growth risk, and source-return condition for candidate alternatives. It does not itself compare, select, declare a selected-set result, publish, authorize, or prove an architecture. Use `C.32` to construct the candidate architecture palette, `A.19.CPM` to compare alternatives, `G.5` to declare a selected-set result, `C.11` to make a final local choice, and `C.32.PAD` to record a project architecture decision. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Apply the relevant evidence, assurance, gate, or release definition and test only when that claim is current.

When the same scale-sensitive pressure must also become a project criterion, `C.32.ACS` creates a separate row for the exact characteristic or Q-Bundle slot, bearer, scale form, and use class. That row may supply declared input to an ASAP preference, but it does not assert that one alternative is preferable under the scale window; conversely, an ASAP preference record is not an ACS row and does not classify the row as an optimization indicator, guardrail, or context-only row.

#### C.31.ASAP:4.4 - Scale variables

Typical architecture scale variables include:

| Scale variable | Reading |
| --- | --- |
| `N_units` | repeated units or instances |
| `N_scopeCount` | aggregation scopes, coarse-graining scopes, or typed LCA control scopes |
| `N_sites` | deployments, sites, markets, or jurisdictions |
| `N_interfaceTypes` | distinct interface grammar variants |
| `N_requiredTransformationKinds` | distinct transformation kinds in the selected functional-structure view |
| `N_flowRelationKinds` | flow-relation or crossing variants in the selected flow-structure view |
| `N_moduleTypes` | module type library size |
| `N_workRepetitions` | delivery, operation, or test repetitions |
| `N_supplierOrVendorClasses` | substitutability or vendor class dimension |
| `N_regulatoryInstances` | approval, safety, or certification repeats |
| `freedomOfAction` | allowed design, search, or control variation |

The scale variable is not enough by name. The claim being made also needs a scale window, expected stable or improving structure, exception-growth risk, and source-return condition.

#### C.31.ASAP:4.5 - Scale audit outputs

Use the heavier audit only when the scale preference changes comparison, publication, selected-set, assurance-input, or decision use:

```text
ArchitectureScaleAuditRecord@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureScaleAuditProjectUseRelationRef?: U.RelationRef governed by the exact audit-use or work-use pattern
  architectureAlternativeSetRef:
  claimScopeRef:
  selectedContextSliceRefs:
  modelUseStructureRef?:
  scaleVariableRefs:
  scaleWindowRef:
  ArchitectureSlopeVector:
  IsoScaleParityNote?:
  ASAPWaiverReason?:
  ArchitectureHeuristicDebt?:
  BespokeResidueRegisterRef?:
  SourceReturnCondition:
  admissibleUse:
  nonAdmissibleUse:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

For `ArchitectureScaleAuditRecord@Project` and `BespokeResidueRegister@Project`, `@Project` is a compatibility and retrieval cue only; it establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. An audit local to one actual project names both the exact composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining direct audit-use relation in `architectureScaleAuditProjectUseRelationRef`; either field alone is insufficient. `BespokeResidueRegister@Project` remains retrieval-only in this edition: `BespokeResidueRegisterRef` may cite the register episteme, but neither that reference nor the audit-use relation asserts the register's own project locality. Assert such locality only after a direct register-to-work relation is governed and cite that exact occurrence; do not borrow the audit relation. Otherwise no audit or residue-register project locality is asserted.

| Output | Meaning |
| --- | --- |
| `ArchitectureSlopeVector` | Slopes for reusable structure, interface variation, flow stability, control stability, work repeatability, bespoke residue, exception growth, and learning transfer. |
| `IsoScaleParityNote` | Comparison under equalized scale budgets where possible; if parity is not possible, the loss is named. |
| `ASAPWaiverReason` | Declared reason for not choosing the scale-amenable alternative. |
| `ArchitectureHeuristicDebt` | Report-only note for knowingly accepting a locally hand-engineered solution with less scale-amenable slope profile under the declared scale window. |
| `BespokeResidueRegister@Project` | Exception inventory with expiry or refactor triggers; not a kernel kind. |
| `ScaleWindow` | Declared range where the preference claim holds. |
| `SourceReturnCondition` | Condition for returning from a compressed, coarse, extracted, indexed, or accounting representation to source-side structural evidence, source records, or a related source or evidence record with higher declared validation boundary. |

`ArchitectureScaleAuditRecord@Project` is a project-side record for triaging an architecture scale-preference claim. It is not an assurance proof, gate record, selected-set result declaration, publication occurrence, local decision, or work plan.

#### C.31.ASAP:4.6 - Waiver discipline

```text
ASAPWaiverReason:
  deontic constraint
  safety or law-domain boundary
  scale-probe overturn
  assurance infeasibility
  context-specific bounded exception
```

Not every non-scale-amenable choice is debt. A deontic constraint, safety boundary, law-domain boundary, mission constraint, assurance infeasibility, or scale-probe overturn can justify a bounded exception without creating `ArchitectureHeuristicDebt`.

`ArchitectureHeuristicDebt` remains report-only unless tied to a decision, risk, work, evidence, assurance, or selected-set record through its governing pattern.

#### C.31.ASAP:4.7 - Scale-refactoring moves

Before scale-preference guidance becomes action-guiding, name at least one possible repair or stop:

| Scale symptom | Possible architecture move | Boundary |
| --- | --- | --- |
| interface variants grow without payoff | reduce interface alphabet or introduce interface grammar | A.6.M governs interface relation repair. |
| product-line or platform variants lack explicit variation points | introduce variability slots or extension rules | Platform label alone is not scale-preference evidence. |
| one aggregation scope hides lower-scope hazards | split the declared aggregation scope or architecture boundary | C.29 supplies lens-use fields only when coarse-graining is mathematical-lens use. |
| repeated work contains reusable structure | replace bespoke work with a method template | Work and method claims go to `A.15`, `A.15.1`, or `A.15.4` when those claims are being made. |
| regulatory or safety residue remains local and repeated | isolate regulatory residue or safety-specific exception register | Evidence, assurance, and gate claims go to `A.10`, `B.3`, `G.6`, or `A.21`. |
| coarse representation loses safety, semantic, or source distinctions | return to lower-scope source-side evidence or narrow the scale window | Source-return condition is mandatory. |

#### C.31.ASAP:4.8 - C.29 lens relation

C.31.ASAP does not prove a scale law and does not perform mathematical-lens recovery. Use `C.29` when the scale preference depends on an RG, coarse-graining, epiplexity, graph, multilevel-learning, or frustration lens.

For architecture use, the C.29 output should name `MLU.Description@RGArchitecture`, `MLU.Description@MultilevelLearningFrustration`, or another local MathLensUse output only when the lens changes the next admissible use. The C.31.ASAP side records the scale variable, scale window, slope or scale-probe evidence, exception-growth risk, and source-return condition. C.29 records candidate mathematical object, mapping mode, preserved structure, lost structure, visible payoff, admissible use, non-admissible use, and stop condition.

