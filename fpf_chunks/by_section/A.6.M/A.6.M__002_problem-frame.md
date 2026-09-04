---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__002_problem-frame.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:1 — Problem frame"
line_start: 18813
line_end: 18859
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.B"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.RSA"
  - "E.18"
  - "E.20"
  - "G.5"
keywords:
  - "are used only for pattern users"
  - "claims"
  - "component"
  - "conformance items"
  - "evidence records"
  - "interface"
  - "interface specification"
  - "layer"
  - "module relation"
  - "open architecture"
  - "or assurance records. Modeled modules and interfaces are not written as agents with duties"
  - "or publication records"
  - "platform"
  - "port"
  - "records"
  - "stack"
  - "substitutability"
---

### A.6.M:1 - Problem frame

Use this pattern when an architecture or engineering text says "module", "component", "interface", "port", "platform", or "open architecture", and the phrase is doing more than ordinary orientation. If a stratification or architecture-operation source label covered by `C.30.STRAT` is doing the work, apply `C.30.STRAT` first; use A.6.M only when that repair recovers module-interface claim content. Use A.6.M when the question under repair is whether one holon is being claimed as a replaceable, reusable, or separately changed structural unit of a larger holon under the exact `VP.ModuleInterface` viewpoint episteme. The note or claim does not make a direct module relation obtain.

The first useful output is `ModuleRelationRepairNote`, a claim-repair note rather than a relation occurrence:

```text
ModuleRelationRepairNote:
  wholeHolonRef:
  candidateModuleHolonRef:
  effectiveReferenceScheme: U.ReferenceScheme, byValue
  claimScope?: U.ClaimScope, byValue
  modelUseStructureRef?: only when one selected model-use structure changes module meaning
  moduleInterfaceViewpointRef?: VP.ModuleInterface
  selectedDependencyStructureRef?: U.StructureRef
  boundaryRef:
  interfaceSpecificationRef?: U.EpistemeRef constrained to InterfaceSpecification
  interfaceSpecificationGap?: exact missing-specification result
  admissibilityConditions:
  substitutabilityPolicyRef?:
  changePolicyRef?:
  directModuleRelationDisposition:
    noDirectRelationClaimed | admittedRelationAndOccurrence | missingGovernor
  admittedRelationKindOrDeclarationRef?:
  obtainingRelationOccurrenceRef?: U.RelationRef
  missingRelationParticipantRefs?:
  proposedPredicate?:
  affectedUse?:
  futureDefinitionNeed?:
  definingPatternLocator?: PatternID used only as a locator
  claimBoundary:
  notAModuleBecause:
  governedNonModuleClaimPatternRefs:
  stopCondition:
```
Exactly one of `interfaceSpecificationRef` and `interfaceSpecificationGap` is current. `noDirectRelationClaimed` leaves every direct-relation field empty. `admittedRelationAndOccurrence` requires an exact admitted relation kind or defining declaration plus one separately obtaining occurrence. `missingGovernor` names the actual participants, proposed predicate, affected use, and missing definition or declaration; a PatternID may locate an applicable rule but cannot fill any of those positions.

Ordinary use stops when the whole, candidate module, boundary, interface specification, admissibility conditions, substitutability policy, change policy, blocked false interpretation, relation disposition, and neighboring work, procedural, role, or enactor subject-pattern choice are clear enough to choose the next architecture move. Use the fuller `ModuleInterfaceClaim` record only when substitutability, conformance, publication, evidence, assurance, change policy, repeated reuse, or cross-team coordination requires durable claim content.

What goes wrong if A.6.M is missed: a functional link becomes a module interface; a signature becomes an implemented interface; a port label becomes proof of integration; "open" becomes a decoration; a platform label hides the actual extension rules; a stratification or architecture-operation source label bypasses `C.30.STRAT` and mints a false local kind; autonomy-like wording is confused with separate module change policy; and a module diagram starts being used for claims governed elsewhere.

What A.6.M buys in practice: the practitioner can repair one module or interface phrase into usable claim content, distinguish it from an independently admitted direct relation occurrence, see which FPF pattern defines or constrains any remaining non-module claim, and stop before full measurement, evidence, or mechanism-suite records are needed.

Not this pattern when the question under repair is the general architecture claim, selected architecture structure kind, structural view, stratification wording or source-label recovery, function wording, procedural or work-package wording, role or enactor wording, autonomous operation, independent acting, unsupervised decision or action, measurement, modularity characterization, or reusable-structure residue. Use `C.30`, `C.30.ASV`, `C.30.STRAT`, `A.6.F`, `A.15`, `A.2`, `E.16`, `C.31`, `C.16`, or `C.31.RSA` as appropriate. For any other claim being made, apply the governing FPF pattern and keep A.6.M only for the module-relation and interface-specification portion.

**E.10.ARCH relation.** A.6.M is the precision-restoration pattern for module-interface relation wording, interface-specification wording, platform-grammar wording, substitutability wording, change-policy wording, and open-architecture module-interface claims. `E.10`, `E.10.ARCH`, or `C.30.STRAT` applies A.6.M only after the recovered result is a module-interface relation, interface specification, platform grammar, substitutability policy, change policy, or open-architecture module-interface claim. If the source wording is still a stratification or architecture-operation source label covered by `C.30.STRAT`, apply `C.30.STRAT` first. If the claim being made is non-module work, role, evidence, assurance, gate, decision, characteristic, flow, autonomy, component, mechanism, or mathematical-lens use, apply the subject pattern named in `A.6.M:12` and keep A.6.M only for the module-interface slice when that module-interface relation remains the claim being made.

