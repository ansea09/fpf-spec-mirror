---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__005_solution.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:4 — Solution"
line_start: 58798
line_end: 58887
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "synthesis structure map"
  - "trade-off front"
---

### C.32:4 - Solution

Create an `ArchitectureSynthesisFrame@Project` when the selected structures and characteristics are not yet visible enough. The frame is a temporary visibility aid for C.32 use; the palette remains the first useful output. Then create a `CandidateArchitecturePalette@Project`. Treat the palette as a small constructive object over selected structures of a described holon, not as a checklist, not as a decision, and not as a published selected set under `G.5`.

Work in seven steps:

1. Anchor the palette to one described holon or holon family, bounded context, and synthesis question.
2. Build the smallest useful synthesis structure map. Start with the declared functional demand, constructive module or manufacture structure, and placement or deployment structure when they shape the question; add control, transformation-flow, work, role, information, evidence, scale, or other selected structures only when they change the synthesis question. For each required function, name at least one admissible bearer under the declared constraints.
3. Reference the architecture-characteristic criteria rows and any Q-Bundle slots that make the trade-off real. Separate functional demand, architecture characteristics, criteria rows, eval results, and decisions.
4. Generate candidate architecture configurations. Each candidate may change decomposition, allocation, function bearing, bearer count, placement, interface grammar, control relation, transformation-flow relation, work method, role responsibility, evidence scope, information structure, or bounded exception.
5. For each candidate, state selected structure changes, expected architecture gain, known architecture loss, constraint fit, preserved structure, lost or hidden structure, and source-return condition.
6. When a front, archive, search result, or pool-treatment policy is being used, cite `C.18`, `C.19`, or NQD and OEE support as generation or retention support only. Keep the C.32 candidate content separate from archive work, front membership, pool treatment, publication of a selected set, and local choice.
7. Stop when the palette contains the fields required by the receiving pattern for comparison, C.18 or C.19 front-policy use, publication of a selected set, local choice, decision, or repair.

The synthesis structure map is not an audit checklist. It is the small set of structures that actually changes the candidate configuration.

**Architecture-characteristic improvement loop.** C.32 is one turn in a continuing improvement cycle over architecture characteristics, not a one-shot search for final form. The practitioner starts with characteristic pressure or criteria rows from `C.32.ACS`, `C.31`, `C.25`, `C.16`, `C.16.P`, `C.31.ASAP`, or a local Q-Bundle; synthesizes candidate selected-structure changes; and records which criteria rows are expected to improve and which protected rows may worsen.

`ArchitectureCharacteristicImprovementLoop@Project` is a local feedback record for reopening C.32 synthesis when characteristic pressure changes. It is not an E.23 method, an ACE eval program, a comparison rule, a selection result, or a decision.

Keep each receiving claim with its own pattern.
Criteria rows stay with `C.32.ACS`; Q-Bundles with `C.25`; scale preference with `C.31.ASAP`; measurement with `C.16`; eval programs and eval results with `C.32.ACE`.
Improvement-question framing and repeated-improvement method stay with `E.22` or `E.23`.
Comparison, set-returning selection, selected-set publication, local choice, and project architecture decision stay with `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `C.11`, and `C.32.PAD`.
C.32 only consumes the changed characteristic pressure and produces the next candidate palette.
Open the next synthesis question from the resulting eval result, front relation, retained alternative, rejected candidate, or source-return trigger.

An eval result that cohesion improved, evidence reuse decayed, coupling changed, latency worsened, or exception growth changed does not choose an architecture. C.32 can use it as feedback only after the bearer, criteria row, scale or qualitative reading frame, selected structures, parity frame, and receiving pattern use are recoverable.

```text
ArchitectureCharacteristicImprovementLoop@Project:
  describedHolonRef:
  currentArchitectureCharacteristicPressureRefs:
  architectureCharacteristicCriteriaSetRef?:
  architectureCharacteristicCriteriaRowRefs?:
  synthesisQuestion:
  candidatePaletteRef:
  architectureCharacteristicEvalResultRefs?:
  changedSelectedStructureRefs:
  improvementClaimGoverningPatternRef: C.32.ACS | C.32.ACE | C.31 | C.25 | C.16 | C.16.P | C.31.ASAP | other receiving pattern
  nextSynthesisQuestion?:
  sourceReturnCondition:
```

| Synthesis role | Typical selected structure | What it contributes | First receiving pattern |
|---|---|---|---|
| Functional demand | `FunctionalStructure` | A.6.F-recovered functional demands, dependencies, constraints, and candidate bearer pressure. | `C.30.ASV`, `A.6.F`, `C.30.TFS-REL` when flow relation is current. |
| Constructive bearer | `ModuleInterfaceStructure`, material, manufacturing, or component relation. | Candidate modules, interface grammar, substitutability, variation slots, and fabrication burden. | `A.6.M`, `C.31`, `C.30.ASV`. |
| Placement and locality | `PlacementDeploymentStructure` or `MaterialSpatialStructure`. | Location, latency, access, environment, maintenance, and source-return burden. | `C.30.ASV`, domain pattern when current. |
| Control and flow | `ControlStructure` and `TransformationFlowStructure`. | Feedback, supervisor relation, rate, flow relation, crossing, and transformation relation. | `C.30.LCA`, `E.18`, `C.30.TFS-REL`, `C.27` when timing is current. |
| Work, role, information, and evidence | Work-method, allocation-responsibility, information, and evidence structures. | Enactment burden, responsibility, data custody, evidence reuse, assurance pressure, and source return. | A.15 family, `A.10`, `B.3`, `C.25`, `C.31` when those claims are current. |

Candidate architecture changes are local C.32 entries for candidate configurations. They are not FPF work occurrences, method steps, or receiving-pattern claims. A change is admissible only when the selected structure being changed is named.

| Architecture-change kind | Constructive use | Minimum repair against overread |
|---|---|---|
| `configurationSynthesis` | Coordinate several selected structures into one candidate architecture configuration. | State the synthesis structure map and architecture characteristics before claiming improvement. |
| `functionalAllocationChange` | Change which candidate bearer, module, role, method, or work structure carries a required functional demand. | Keep functional demand, bearer, module, role, and work as distinct relations. |
| `functionBearerFeasibilityRepair` | Repair a candidate whose functional structure names a required function that no admitted bearer can perform under module, placement, resource, control, or evidence constraints. | Add or change a bearer, split the function, change placement or resource access, change control responsibility, reduce the functional demand, or reject the candidate. |
| `functionBearerConsolidation` | Transfer a required function onto an existing selected structure, remove a support bearer, or propose one more general bearer for several functions. | State the functions transferred, the bearer removed or generalized, the affected architecture characteristics, the lost options, and the BLP scale window or waiver when scale advantage is claimed. |
| `structuralSubstitution` | Replace one selected structure with another candidate structure. | State what is preserved and what is lost. |
| `relationRetargeting` | Change an affected relation endpoint, responsibility relation, role relation, dependency relation, admissible-use boundary, or source-return relation. | Name the relation kind or boundary before using the change in a candidate. |
| `transformerTransformedCorrespondenceSynthesis` | Coordinate candidate structures when a holon that changes another holon constrains the changed holon's architecture. | Open `C.32.CONWAY`; name the changing relation, transformer-side selected structure, transformed-side selected structure, affected architecture characteristics, expected gain, known loss, and receiving pattern. |
| `decompositionOrAllocationChange` | Reallocate module, role, work, evidence responsibility, data custody, control responsibility, or variation slot across structures. | State the new boundary and migration burden. |
| `placementOrDeploymentChange` | Change locality, deployment, material placement, installation, or maintenance access. | Name the affected structure and the latency, access, source-return, or environment burden. |
| `flowOrControlVariant` | Change transformation flow, control depth, rate band, feedback boundary, or mediator relation. | State the timing, control, observability, or accountability burden created by the change. |
| `interfaceGrammarChange` | Narrow, split, widen, or stabilize an interaction boundary. | Apply `A.6.M` when module-interface relation repair is current. |
| `declaredScopeOrHolonLevelChange` | Split, merge, add, or remove a declared holon-level reference, declared scope, evidence scope, work-method scope, or aggregation scope. | Name the affected reference, use `C.30.STRAT` when the wording is only a stratification term, and use `B.2` only when whole reidentification is current. |
| `boundedException` | Keep a residual because removing it costs more than it buys now. | State the exception, reopen trigger, and next governing pattern if later source use or decision use expands. |

**Didactic mini-slices.** Use these as examples of the kind of work C.32 expects, not as domain-specific templates.

| Situation | First C.32 step | Candidate repair |
|---|---|---|
| A sterilization function is placed in a shared field module, but the field placement has no power and no certified evidence relation for that heat cycle. | Keep the functional demand separate from the module and placement structures. | Add a local certified bearer, split the function into pre-field and field steps, change placement, or reject the shared-module candidate. |
| An ML functional graph includes retrieval, planning, and action, but no module-interface relation or role relation carries evidence-refresh responsibility or admissible-use control. | Treat the graph as functional structure and recover module-interface, evidence, and control structures. | Add a retrieval service with explicit evidence-refresh responsibility, add a supervisor relation, narrow model-interface behavior, or reject the candidate. |
| A method family says the review function is automated, but no role or method structure can carry accountability for exceptions. | Recover method structure, role-enactor structure, and evidence structure separately. | Add an exception role, split the method step, change evidence scope, or keep the automation as source cue only. |

When the architecture being synthesized belongs to a holon that changes another holon, use `C.32.CONWAY` before using Conway, mirroring, or inverse-Conway language in candidate synthesis. The practitioner names the changing relation, the transformer holon, the transformed holon, selected structures on both sides, architecture characteristics under pressure, candidate changes, expected gains, known losses, and source-return conditions.

The C.32 side keeps the candidate palette. `C.32.CONWAY` carries the correspondence frame. Transformation, work, transformation-flow, and module-interface claims belong to `A.3.4`, `E.18`, `A.15`, `C.30.TFS-REL`, or `A.6.M` when current. Structural-similarity or preservation claims belong to `C.29` when they are current.

A richer dossier is optional. Open it only when one candidate must carry source views, relation notes, measurements, C.29 lens outputs, evidence notes, or failure repairs that affect the next architecture use. Ordinary C.32 use should remain one row per candidate configuration.

**Downstream use.** C.32 prepares architecture-specific candidate content. Publishing a selected set belongs to `G.5`. A fixed local choice belongs to `C.11`. A project architecture decision belongs to `C.32.PAD`. Archive, front, pool-treatment, or generation policy belongs to `C.18` or `C.19` when that claim is being made. Architecture-description or publication-face work belongs to `C.30.AD`, `E.17`, or `E.24.PUB`.

**Stop condition.** Stop C.32 when the palette can support the next use without hiding the selected structures, architecture-change kind, architecture gain, architecture loss, constraint fit, source-return condition, or receiving pattern.

**Lowering condition.** Lower the record out of C.32 use when the needed architecture claim is not grounded, the item is only a source artifact, only one configuration is visible, the candidate lacks selected-structure change, the functional demand has no feasible bearer, the architecture gain or loss is unnamed, or the next use is already comparison, selection, publication of a selected set, local choice, decision, evidence, or assurance. Return to `C.30` for grounding, to the source or description pattern for source artifacts, to `C.32.FAIL` for candidate repair, and to the named receiving pattern when the downstream claim is current. Reopen C.32 when a criteria row, eval result, retained alternative, front relation, source-return trigger, or source-currentness change alters the selected structures under pressure or the acceptable loss profile.

