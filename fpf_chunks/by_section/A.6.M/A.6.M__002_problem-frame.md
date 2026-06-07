---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__002_problem-frame.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:1 — Problem frame"
line_start: 13754
line_end: 13785
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
  - "C.30.TGA-FLOW-REL"
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

Use this pattern when an architecture or engineering text says "module", "component", "interface", "port", "platform", or "open architecture", and the phrase is doing more than ordinary orientation. If a source label such as "layer" or "stack" is doing the work, apply `C.30.STRAT` first; A.6.M receives the case only when the recovered result is a module-interface relation. Open A.6.M when the live question is whether one holon is being treated as a replaceable, reusable, or separately changed structural unit of a larger holon under a declared module-interface viewpoint.

The first useful move is `ModuleRelationRepairNote`:

```text
ModuleRelationRepairNote:
  wholeHolonRef:
  candidateModuleHolonRef:
  boundedContextRef:
  moduleInterfaceViewpointRef: VP.ModuleInterface
  boundaryRef:
  interfaceSpecificationRef or interfaceSpecificationGap:
  admissibilityConditions:
  substitutionOrChangePolicyRef:
  liveClaimBoundary:
  notAModuleBecause:
  nextGoverningPatternRef:
  stopCondition:
```

Ordinary use stops when the whole, candidate module, boundary, interface specification, admissibility conditions, substitution or change policy, blocked false interpretation, and neighboring work, procedural, role, or enactor exit are clear enough to choose the next architecture move. Open the fuller `moduleIn(...)` relation record only when substitutability, conformance, publication, evidence, assurance, change policy, repeated reuse, or cross-team coordination is live.

What goes wrong if A.6.M is missed: a functional link becomes a module interface; a signature becomes an implemented interface; a port label becomes proof of integration; "open" becomes a decoration; a platform label hides the actual extension rules; a source word such as "layer" or "stack" bypasses `C.30.STRAT` and mints a false local kind; autonomy-like wording is confused with separate module change policy; and a module diagram starts carrying claims that belong elsewhere.

What A.6.M buys in practice: the practitioner can repair one module or interface phrase into a module-relation record, see which exact FPF governing pattern carries any remaining non-module claim, and stop before opening full measurement, evidence, or mechanism-suite records.

Not this pattern when the live question is the general architecture claim, selected architecture structure kind, structural view, stratification wording or source-label recovery, function wording, procedural or work-package wording, role or enactor wording, autonomous operation, independent acting, unsupervised decision or action, measurement, modularity characterization, or reusable-structure residue. Use `C.30`, `C.30.ASV`, `C.30.STRAT`, `A.6.F`, `A.15`, `A.2`, `E.16`, `C.31`, `C.16`, or `C.31.RSA` as appropriate. For any other live claim, apply the exact FPF governing pattern and keep A.6.M only for the module-relation and interface-specification portion.

**E.10.ARCH relation.** A.6.M is the receiving precision-restoration pattern for module-interface relation wording, interface-specification wording, platform-grammar wording, substitutability wording, and open-architecture module-interface claims. `E.10`, `E.10.ARCH`, or `C.30.STRAT` sends wording here only after the recovered result is a module-interface relation, interface specification, platform grammar, substitution or change policy, or open-architecture module-interface claim. If the source wording is still a structure-source label such as `block`, `layer`, `stack`, `expert`, `router`, or `cache`, apply `C.30.STRAT` first. If the live claim is functional architecture, TGA flow, component relation, work, role or enactor relation, autonomy, characteristic, evidence, assurance, gate, decision, or mathematical correspondence, use the exact governing pattern and keep A.6.M only for the module-interface slice when that slice remains live.

