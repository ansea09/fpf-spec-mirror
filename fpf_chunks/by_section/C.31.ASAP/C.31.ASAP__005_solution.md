---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Which Architecture Is Preferable Under Scale? (Scale Amenability)"
section_id: "C.31.ASAP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__005_solution.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "C.31.ASAP — Which Architecture Is Preferable Under Scale? (Scale Amenability)"
  - "C.31.ASAP:4 — Solution"
line_start: 79793
line_end: 79969
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
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
  - "C.32.PAD"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "exception growth"
  - "scale amenability"
  - "scale probe"
  - "scale variable"
  - "scale window"
  - "waiver"
---

### C.31.ASAP:4 - Solution

C.31.ASAP specializes scale-amenability preference for architecture alternatives. It applies when an architecture alternative set, scale variable with its window, and claimed preference under scale are named.

#### C.31.ASAP:4.1 - Applicability fields

C.31.ASAP applies only when all of the following are present:

1. a declared architecture alternative set, described holon, `U.ClaimScope`, and relevant A.2.6 `U.ContextSlice` membership;
2. a declared scale variable and its window;
3. a claimed preference under scale;
4. the observed scale behavior, a derivation from applicable conditions, evidence from a scale probe, or a reason why the claim remains hypothetical;
5. the grounds relating the architecture alternatives to that comparison. These may include an applicable quotation for the required service, or differences in structure and local exceptions where those affect the claimed advantage.

If those fields are absent, keep the claim in `C.31` as a temporal or scale-sensitive characteristic cue, in `C.31.RSA` as report-only accounting, in `C.29` as a bounded lens-use output, or in ordinary architecture prose.

#### C.31.ASAP:4.2 - `ScaleClaimTriage`

Recover the following content before a heavier scale audit. Reuse an adequate account; the triage form is optional:

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
  comparisonBasisRef?:
  noProbeReason?:
  expectedStableOrImprovingStructure?:
  exceptionGrowthRisk?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

The account is complete enough when it answers the scale-preference question or identifies the next warranted inquiry or architecture move.

Include `nonAdmissibleUse?` only for an independently grounded alternative that is plausible here and whose rejection changes understanding or action; `groundedScaleShortcut?` is an alias for that optional value.

Retaining or publishing the bounded answer preserves its limits. A stronger comparison, assurance, selected-set or decision claim needs its own grounds.

`claimScopeRef` designates one `U.ClaimScope`; `selectedContextSliceRefs` records the A.2.6 membership relevant to this use. A scale window is the range of the scale variable for which the preference is claimed, not a substitute for either scope object.

`modelUseStructureRef` is optional and is filled only when an independently selected A.1.1 `BoundedModelUseStructure` changes the interpretation of this preference use.

#### C.31.ASAP:4.3 - Architecture scale-preference rule

When architecture alternatives satisfy the same safety, law-domain and assurance boundaries, prefer the alternative whose relevant reusable structure remains stable or improves over the declared scale window, unless a stated bounded exception justifies another choice. Select the functional, flow, control, interface, work-template or evidence structure and any learning-transfer characteristic on which this architecture question depends.

Define the advantage that would change the recommendation. Compare both alternatives for the same deliveries under the conditions that affect that advantage. Separate a one-time investment from work repeated at each installation or each new interface type. When deciding whether to commission a shared design, count the preparation it requires. When deciding whether to keep using one already built, compare future costs and commitments that the choice can still change. The original expense remains part of the investment history. More deployments at an established site may require none of the qualification work that a first deployment in a new jurisdiction requires. Check where the two alternatives tie or change order. When different admissible mixes of sites give different recommendations, state which mix supports each and what is known about the proposed rollout.

Observations can support a comparison for the conditions examined. A binding rate, an engineering bound or a supported construction can also establish an answer for the entire stated range under its assumptions. Record the observations or the applicable derivation and its assumptions. A quotation or bound that orders the alternatives throughout a window can be cited in `comparisonBasisRef` even when neither slope is known. An advantage in price throughout a window establishes which quote is cheaper. To claim its price grows more slowly, compare the changes in price. When an untested premise could reverse the preference, state what depends on it. A reason for skipping a probe supplies no evidence about its outcome. An applicable derivation can already settle the question. Conflicting characteristics need the preference or decision rule for the work in question.

C.31.ASAP defines the scale-preference claim and its boundary. Use `G.9` for a parity claim and `A.21` for a gate claim; the candidate, comparison, set-declaration, and choice uses are distinguished below.

A scale-preference claim may inform `C.32` candidate generation or supply one input to an `A.19.CPM` comparison by naming the scale variable and window, the grounds for ordering the alternatives, and any structural uncertainty or exception that could reverse that order.

Use:

- `C.32` to construct the candidate architecture palette;
- `A.19.CPM` to compare alternatives;
- `G.5` to declare a selected-set result;
- `C.11` to make a final local choice; and
- `C.32.PAD` to record a project architecture decision.

For audience availability, use `E.24.PUB` for the publication occurrence, form, carrier, audience and bounded use; use `E.17` when a source-backed face and return are needed.

Apply the relevant evidence, assurance, gate, or release definition and test only when that claim is current.

When the same scale-sensitive pressure must also become a project criterion, `C.32.ACS` creates a separate row for the characteristic or Q-Bundle slot, bearer, scale form, and use class. That row may supply declared input to an ASAP preference. Use C.31.ASAP to state which alternative is preferable under the scale window; use C.32.ACS to admit and classify the criterion row as an optimization indicator, guardrail, or context-only row. Keep the preference record and criterion row separately referenced.

#### C.31.ASAP:4.4 - Scale variables

Typical architecture scale variables include:

| Scale variable | Reading |
| --- | --- |
| `N_units` | repeated units or instances |
| `N_scopeCount` | aggregation scopes, coarse-graining scopes, or typed LCA control scopes |
| `N_sites` | Distinct deployment sites. Deployment events, markets and jurisdictions can have different counts and costs. Name and count the one that drives the work in question. |
| `N_interfaceTypes` | distinct interface grammar variants |
| `N_requiredTransformationKinds` | distinct transformation kinds in the selected functional-structure view |
| `N_flowRelationKinds` | flow-relation or crossing variants in the selected flow-structure view |
| `N_moduleTypes` | module type library size |
| `N_workRepetitions` | delivery, operation, or test repetitions |
| `N_supplierOrVendorClasses` | substitutability or vendor class dimension |
| `N_regulatoryInstances` | approval, safety, or certification repeats |
| `freedomOfAction` | allowed design, search, or control variation |

Name the scale variable, its window and the characteristic whose behavior matters to the comparison. Add a source-return condition when omitted distinctions could change the receiving action. Increasing the number of sites changes a quantity in the model. Abstracting the model can leave the jurisdiction of a site open. The same disciplinary model can compare five and forty sites. Use B.5.MR:4.2 when asking which conclusions still follow after leaving a distinction open.

#### C.31.ASAP:4.5 - Scale audit outputs

Use a fuller audit when unresolved behavior, exceptions or comparison grounds could change the receiving use. An existing adequate account can carry the necessary content:

```text
ArchitectureScaleAuditRecord@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureScaleAuditProjectUseRelationRef?: U.RelationRef governed by the audit-use or work-use pattern
  architectureAlternativeSetRef:
  claimScopeRef:
  selectedContextSliceRefs:
  modelUseStructureRef?:
  scaleVariableRefs:
  scaleWindowRef:
  ArchitectureSlopeVector?:
  comparisonBasisRef?:
  IsoScaleParityNote?:
  ASAPWaiverReason?:
  ArchitectureHeuristicDebt?:
  BespokeResidueRegisterRef?:
  SourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

For `ArchitectureScaleAuditRecord@Project` and `BespokeResidueRegister@Project`, `@Project` is a compatibility and retrieval cue.

An audit local to one project names both the composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining direct audit-use relation in `architectureScaleAuditProjectUseRelationRef`. `BespokeResidueRegisterRef` may cite the register episteme. Assert that register's project locality only after a separate direct register-to-work relation is governed, and cite that occurrence; the audit-use relation remains about the audit. Otherwise retain only retrieval use and make no audit or residue-register project-locality claim.

| Output | Meaning |
| --- | --- |
| `ArchitectureSlopeVector` | Slopes for the selected characteristics, such as reusable structure, interface variation, flow or control stability, work repeatability, residue, exception growth or learning transfer. Keep missing estimates, uncertainty and incomparable dimensions visible. |
| `IsoScaleParityNote` | Comparison under equalized scale budgets where possible; if parity is not possible, the loss is named. |
| `ASAPWaiverReason` | Declared reason for not choosing the scale-amenable alternative. |
| `ArchitectureHeuristicDebt` | Report-only note for knowingly accepting a locally hand-engineered solution with less scale-amenable slope profile under the declared scale window. |
| `BespokeResidueRegister@Project` | Pattern-local exception inventory with expiry or refactor triggers. |
| `ScaleWindow` | Declared range where the preference claim holds. |
| `SourceReturnCondition` | Condition for returning from a compressed, coarse, extracted, indexed, or accounting representation to source-side structural evidence, source records, or a related source or evidence record with higher declared validation boundary. |

`ArchitectureScaleAuditRecord@Project` records the triage of an architecture scale-preference claim. An assurance proof, gate record, selected-set result declaration, publication occurrence, local decision, or work plan remains a separate result under its own pattern; use A.15.2 for the work plan.

#### C.31.ASAP:4.6 - Waiver discipline

```text
ASAPWaiverReason:
  deontic constraint
  safety or law-domain boundary
  scale-probe overturn
  assurance infeasibility
  context-specific bounded exception
```

A deontic constraint, safety boundary, law-domain boundary, mission constraint, assurance infeasibility, or scale-probe overturn can justify a bounded exception without creating `ArchitectureHeuristicDebt`.

`ArchitectureHeuristicDebt` remains report-only unless tied to a decision, risk, work, evidence, assurance, or selected-set record through its governing pattern.

#### C.31.ASAP:4.7 - Scale-refactoring moves

Name at least one possible repair or stop before using the scale preference to guide action:

| Scale symptom | Possible architecture move | Boundary |
| --- | --- | --- |
| interface variants grow without payoff | reduce interface alphabet or introduce interface grammar | A.6.M governs interface relation repair. |
| product-line or platform variants lack explicit variation points | introduce variability slots or extension rules | Platform label alone is not scale-preference evidence. |
| one aggregation scope hides lower-scope hazards | split the declared aggregation scope or architecture boundary | Recover the consequential distinction. Use C.29 when the mathematical representation, transfer or limits of reliance remain unresolved. |
| repeated work contains reusable structure | reuse a method template for subsequent work | Use `A.3.1` for a Method claim and `A.15` for Method–Work alignment. For a dated Work, recover A.13 and independent A.15.1 admission, with F.6 only for precise assignment-bound attribution. Use `A.15.4` only while appearance hides a work-relevant prerequisite. |
| regulatory or safety residue remains local and repeated | isolate regulatory residue or safety-specific exception register | Establish the relied-on source grounds; use `A.10` for a needed replayable source-to-use account, `G.6` for needed addressable provenance, `B.3` when a named assurance claim is current, and `A.21` for a gate claim. |
| coarse representation loses action-changing safety, semantic or source distinctions | return to source-side evidence or narrow the scale window | Preserve the return condition needed by this reliance. |

#### C.31.ASAP:4.8 - C.29 lens relation

A scale preference may use an RG, coarse-graining, epiplexity, graph, multilevel-learning or frustration model. Establish the assumptions and correspondence needed by that inference; an adequate domain treatment can suffice. Use `C.29` when choosing or transferring the representation, or relying on its result, leaves an unresolved question. Keep the architecture scale-preference claim in C.31.ASAP and use C.18.1 for a scale-law claim.

The account retains its scale variable, window and the basis for the comparison, including any variation in exceptions that can change the answer. State where to recover an omitted fact when the answer depends on it. When a C.29 account is needed, it can use `MLU.Description@RGArchitecture`, `MLU.Description@MultilevelLearningFrustration` or another local account to explain the representation, correspondence, preserved and lost distinctions, payoff and limits. A separately named output is needed only when the receiving use requires it.

