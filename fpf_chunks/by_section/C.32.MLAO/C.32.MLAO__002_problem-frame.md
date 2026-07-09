---
chunk_kind: "child"
pattern_id: "C.32.MLAO"
pattern_title: "Multilevel Architecture Residual Optimization"
section_id: "C.32.MLAO:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.MLAO/C.32.MLAO__002_problem-frame.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "C.32.MLAO — Multilevel Architecture Residual Optimization"
  - "C.32.MLAO:1 — Problem frame"
line_start: 61304
line_end: 61388
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.6.M"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.29"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "G.5"
keywords:
  - "Pareto front"
  - "declared level"
  - "declared scope"
  - "ideality pressure"
  - "multilevel architecture residual optimization"
  - "residual-reducing candidate frame"
  - "scale amenability"
  - "stepping stone"
---

### C.32.MLAO:1 - Problem frame

Use this pattern when a practitioner has a recoverable cross-scope or interlevel architecture residual and needs candidate architecture changes that reduce that residual under a declared evolution window.

Primary working reader: an architect or architecture-responsible practitioner who has already recovered a residual and must prepare candidate changes without calling a local improvement a whole-holon optimum.

Typical entry phrases:

```text
"The local architecture improvement made another scope worse."
"The platform helps product teams but grows evidence exceptions."
"Local agent autonomy conflicts with the control or policy scope."
"The method template speeds authoring and slows review."
"A graph, residual vector, or Pareto front can inform comparison only after selected structures, residuals, losses, and the receiving pattern are declared; it is not the architecture."
```

**First-minute use slice.** A regulated product-family team has used `C.30.ILC` to name a residual: local product variants are quicker to ship, but certification evidence grows at the family scope. Using C.32.MLAO, the practitioner frames three residual-reducing candidate changes: add evidence scope, narrow interface grammar, or accept a bounded exception with a reopen trigger. Each candidate states the residual it reduces and the new burden it creates. The team now has explicit inputs for `A.19.CPM`, `C.11`, `A.19.SelectorMechanism`, or `G.5` when comparison, local choice, selection, or publication of a selected set is current.

The primary `EntityOfConcern` is a residual-reducing candidate frame for one grounded architecture question. In plain working terms, the frame asks where a local architecture improvement moved the cost and which candidate can reduce that moved cost without hiding its new burden. The described holon can be a system, organization-as-system, discipline, AI-agent setup, built asset, episteme, work occurrence, or another admitted holon kind. Source labels such as practice, culture, tradition, style, method, or role are admitted only after recovery into an admitted holon, method-side structure, role-side structure, work structure, episteme, bounded context, or C.36 cultural-evolution relation. A method family or role-side concern may appear as a selected method-side or role-side structure around that described holon, but it is not admitted as a holon by label. A publication family may appear only when it is the described holon or selected structure under its own governing pattern; publication-face use stays with `E.17` or `E.24.PUB`. C.32.MLAO is not a universal optimizer, adequacy claim, selector, decision, assurance argument, publication pattern, or software-system-only pattern.

What goes wrong if C.32.MLAO is missed: local success is called whole-holon architecture success, or an optimization phrase hides the residual that shifted to another declared holon-level ref or declared scope ref.

What C.32.MLAO buys in practice: the practitioner can prepare residual-reducing architecture candidates for later comparison by naming residual reduced, new burden created, affected scope, preserved structure, lost structure, and source-return condition.

Ordinary working move: name where the local improvement moved the cost, name the selected structure and scope that now carry the residual, then prepare candidate changes that reduce that residual while making the new burden explicit.

Adoption test: after using C.32.MLAO, a reader can see the residual reduced, the new burden, the affected scope, the preserved structure, the lost structure, and the evolution-window stop condition for each candidate.

Use C.32.MLAO only after residual triage. Do not use it to recover the residual itself, justify a mathematical lens, compare or select candidates, choose locally, publish a selected set, or decide the project architecture.

Common exits by claim kind:

- `C.30.ILC` when the residual is not recoverable yet.
- `C.32.ACS` when architecture-characteristic criteria rows are missing.
- `C.32.ACE` when eval programs or eval results are the current claim.
- `C.29` when mathematical-lens use is being claimed.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for publication of a selected set.
- `C.18` and `C.19` for archive, front, pool treatment, or stepping-stone retention.
- `C.30.AD`, `E.17`, and `E.24.PUB` for architecture-description or publication-face work.
- `C.32.PAD` for project decision.

The first useful output is `MultilevelArchitectureResidualOptimizationFrame@Project`. The frame is the project working record for residual-reducing candidate framing. It records residual movement and candidate burdens; it is not a universal optimizer, scalar optimum, C.29 lens result, or architecture decision:

For a first pass, fill only the described holon, bounded context, residual-triage ref, affected level or scope refs, selected structures, residual-bearing loci, criteria rows, evolution window, residual-reducing candidates with residual reduced and new burden, receiving pattern, and stop condition. Add front, archive, NQD, OEE, C.29 lens, ideality, scale-amenability, function-bearer, and transformer-transformed refs only when that support is current for the candidate being framed.

```text
MultilevelArchitectureResidualOptimizationFrame@Project:
  describedHolonRef:
  boundedContextRef:
  residualTriageRef:
  declaredHolonLevelRefs?:
  declaredScopeRefs:
  selectedStructureRefs:
  residualBearingLoci:
  candidatePaletteRef:
  architectureCharacteristicCriteriaSetRef?:
  architectureCharacteristicCriteriaRowRefs:
  qBundleRefs?:
  evolutionWindowRef:
  dynamicFrontOrArchiveRef?:
  nqdOrOeeSupportRef?:
  steppingStoneRefs?:
  architectureIdealityPressureRef?:
  scaleAmenabilityPolicyRef?:
  functionBearerFeasibilityRef?:
  transformerTransformedCorrespondenceRef?:
  residualReducingCandidates:
    - candidateRef:
      selectedStructureChanged:
      affectedLevelOrScope:
      affectedArchitectureCharacteristicRefs:
      affectedCriteriaRowRefs?:
      architectureCharacteristicEvalResultRefs?:
      residualReduced:
      newBurden:
      preservedStructure:
      lostOrHiddenStructure:
      sourceReturnCondition:
  comparisonInputRefs?:
  receivingOperationPatternRef?:
  c29LensOutputRef?:
  metaHolonTransitionRef?:
  stopCondition:
```

