---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__005_solution.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:4 — Solution"
line_start: 63569
line_end: 63660
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
  - "C.32.MWA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
  - "U.Structure"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "selected-structure contribution rows"
  - "trade-off front"
---

### C.32:4 - Solution

Create an `ArchitectureSynthesisFrame@Project` when the selected structures and characteristics are not yet visible enough. The frame is a temporary visibility aid for C.32 use; the palette remains the first useful output. Then create a `CandidateArchitecturePalette@Project`. Treat the palette as a small constructive object over selected structures of a described holon, not as a checklist, not as a decision, not as a selected-set result declared under `G.5`, and not as a publication occurrence.

Work in seven steps:

1. Anchor the palette to one described holon or holon family, synthesis question, and intended next use. Name any current C.30 architecture relations and selected structures that can change that question.
2. Write the smallest useful set of selected-structure contribution rows. Start with the functional demand and candidate bearer recovered with `A.6.F`, constructive module or manufacture structure, and placement or deployment structure when they shape the question; add control, transformation-flow, Method, Work, local-kind relation or classification, assignment, information, evidence, scale, or other selected structures only when they change the synthesis question. Send unresolved claim-bearing “role” wording through `E.10.ROLE`. For each required function, name at least one admissible bearer under the declared constraints.
3. Reference the architecture-characteristic criteria rows and any Q-Bundle slots that make the trade-off real. Separate functional demand, architecture characteristics, criteria rows, eval results, and decisions.
4. Generate candidate architecture configurations. A candidate claim may propose, for example, changed decomposition, allocation, A.6.F function bearing, bearer count, placement, interface grammar, a control or transformation-flow relation, Method use, future assignment conditions, an independently established responsibility relation, evidence scope, information structure, or a bounded exception. Modal candidate wording creates no assignment occurrence and proves no Work occurred. Use a WorkPlan, policy, commitment, permission, decision, or other truthful prospective object when one applies. For actual precise Work, recover each exact actual performer System through A.13 and let A.15.1 independently admit the dated Work and enacted Method; add an assignment occurrence, its declared species, and F.6 only when the candidate account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. F.6 identifies neither assignment nor performer, missing or failed F.6 leaves the Work intact, and an assignment never carries responsibility by itself.
5. For each candidate, state selected structure changes, expected architecture gain, known architecture loss, constraint fit, preserved structure, lost or hidden structure, and source-return condition.
6. When a front, archive, search result, or pool-treatment policy is being used, cite `C.18`, `C.19`, or NQD and OEE support as generation or retention support only. Keep the C.32 candidate content separate from archive work, front membership, pool treatment, selected-set result declaration, actual publication, and local choice.
7. Stop when the palette contains the fields required by the pattern for the next question, such as comparison, C.18 or C.19 front-policy use, selected-set result declaration, actual publication, local choice, decision, or repair.

These contribution rows are not an audit checklist. Together they name only the structures that actually change the candidate configuration.

**Architecture-characteristic improvement loop.** C.32 is one turn in a continuing improvement cycle over architecture characteristics, not a one-shot search for final form. The practitioner starts with characteristic pressure or criteria rows from `C.32.ACS`, `C.31`, `C.25`, `C.16`, `C.16.P`, `C.31.ASAP`, or a local Q-Bundle; synthesizes candidate selected-structure changes; and records which criteria rows are expected to improve and which protected rows may worsen.

`ArchitectureCharacteristicImprovementLoop@Project` is a local feedback record for reopening C.32 synthesis when characteristic pressure changes. It is not an E.23 method, an ACE eval program, a comparison rule, a selection result, or a decision.

Keep each receiving claim with its subject pattern.
Criteria rows stay with `C.32.ACS`; Q-Bundles with `C.25`; scale preference with `C.31.ASAP`; measurement with `C.16`; eval programs and eval results with `C.32.ACE`.
Improvement-question framing and repeated-improvement method stay with `E.22` or `E.23`.
Use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for set-returning selection, `G.5` for selected-set result declaration, `C.11` for local choice, and `C.32.PAD` for a project architecture decision. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.
For this loop, bring only the changed characteristic pressure into C.32 and return the next candidate palette.
Open the next synthesis question from the resulting eval result, front relation, retained alternative, rejected candidate, or source-return trigger.

An eval result that cohesion improved, evidence reuse decayed, coupling changed, latency worsened, or exception growth changed does not choose an architecture. A practitioner may use it as feedback only after the bearer, criteria row, scale or qualitative reading frame, selected structures, parity frame, and pattern for the next question are recoverable.

```text
ArchitectureCharacteristicImprovementLoop@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureSynthesisProjectUseRelationRef?: U.RelationRef resolving to the exact synthesis-feedback or work-use relation
  describedHolonRef:
  currentArchitectureCharacteristicPressureRefs:
  architectureCharacteristicCriteriaSetRef?:
  architectureCharacteristicCriteriaRowRefs?:
  synthesisQuestion:
  candidatePaletteRef:
  architectureCharacteristicEvalResultRefs?:
  changedSelectedStructureRefs:
  improvementClaimPatternLocator: C.32.ACS | C.32.ACE | C.31 | C.25 | C.16 | C.16.P | C.31.ASAP | other pattern for the next question
  nextSynthesisQuestion?:
  sourceReturnCondition:
```

| Synthesis position | Typical selected structure | What it contributes | First pattern for the next question |
|---|---|---|---|
| Functional demand | `FunctionalStructure` | A.6.F-recovered functional demands, dependencies, constraints, and candidate bearer pressure. | `C.30.ASV`, `A.6.F`, `C.30.TFS-REL` when flow relation is current. |
| Constructive bearer | `ModuleInterfaceStructure`, material, manufacturing, or component relation. | Candidate modules, interface grammar, substitutability, variation slots, and fabrication burden. | `A.6.M`, `C.31`, `C.30.ASV`. |
| Placement and locality | `PlacementDeploymentStructure` or `MaterialSpatialStructure`. | Location, latency, access, environment, maintenance, and source-return burden. | `C.30.ASV`, domain pattern when current. |
| Control and flow | `ControlStructure` and `TransformationFlowStructure`. | Feedback, supervisor relation, rate, flow relation, crossing, and transformation relation. | `C.30.LCA`, `E.18`, `C.30.TFS-REL`, `C.27` when timing is current. |
| Method, Work, local-kind or assignment, information, and evidence | Method and Work structures; relations among local system-role kinds, classifications, or assignment structures; direct allocation or responsibility relations; information and evidence structures. | Prospective enactment burden, independently established responsibility, data custody, evidence reuse, assurance pressure, and source return. | `E.10.ROLE` for unresolved wording; A.2 and A.2.1 for recovered kind, classification, or assignment; A.15 and F.6 only for actual Work; the admitted direct domain predicate or exact missing governor for responsibility; `A.10`, `B.3`, `C.25`, and `C.31` when those claims are current. |

Candidate architecture changes are local C.32 entries for candidate configurations. They are not FPF work occurrences, method steps, or receiving-pattern claims. A change is admissible only when the selected structure being changed is named.

| Architecture-change kind | Constructive use | Minimum repair against overread |
|---|---|---|
| `configurationSynthesis` | Coordinate several selected structures into one candidate architecture configuration. | State the selected-structure contribution rows and architecture characteristics before claiming improvement. |
| `functionalAllocationChange` | Change the candidate A.6.F bearer or the module, Method, Work, local kind, separate System-classification judgment, assignment, control, or other structures that constrain its functioning. | Keep the functional predicate and bearer distinct from every neighboring structure; unresolved “role” wording goes through `E.10.ROLE`. |
| `functionBearerFeasibilityRepair` | Repair a candidate whose functional structure names a required function that no admitted bearer can bear under module, placement, resource, control, or evidence constraints. | Add or change an A.6.F bearer, split the function, change placement or resource access, change the direct control or responsibility relation, reduce the functional demand, or reject the candidate. |
| `functionBearerConsolidation` | Transfer a required function onto an existing selected structure, remove a support bearer, or propose one more general bearer for several functions. | State the functions transferred, the bearer removed or generalized, the affected architecture characteristics, the lost options, and the BLP scale window or waiver when scale advantage is claimed. |
| `structuralSubstitution` | Replace one selected structure with another candidate structure. | State what is preserved and what is lost. |
| `relationRetargeting` | Change an affected relation endpoint, direct responsibility relation, system-role assignment, dependency relation, admissible-use boundary, or source-return relation. | Name the relation kind and its actual predicate before using the change in a candidate; if a needed responsibility predicate is absent, record the exact missing governor. |
| `architectureInfluenceCorrespondenceSynthesis` | Coordinate candidate structures when an independently typed architecture or other source constrains transformed-side architecture content for a changed referent. | Open `C.32.CONWAY`; name the changed referent and any independently grounded A.3.4 transformation separately; name each typed influence source by kind and its exact direct relation when an influence occurrence is asserted, otherwise keep the pressure synthesis-local with its `missing-governor`, unresolved-grounding, or false-predicate disposition; for each actual architecture side keep the exact C.30 holon, obtaining `ArchitectureRelation`, and selected `U.Structure` visible, and keep modal content in `ArchitectureClaim`; then prepare influence-source-side, transformed-side, joint, or bounded-mismatch candidates with affected architecture characteristics, expected gain, known loss, source-return condition, and pattern for the next question. |
| `decompositionOrAllocationChange` | Propose reallocation of a module, future assignment condition, Work boundary, evidence relation, data custody, control relation, or variation slot across structures; retarget responsibility only through its direct domain predicate. | State the proposed boundary, participant conditions, prospective object, and migration burden. Do not create an assignment or Work occurrence from candidate wording; return the exact missing governor when the needed responsibility relation has no current predicate. |
| `placementOrDeploymentChange` | Change locality, deployment, material placement, installation, or maintenance access. | Name the affected structure and the latency, access, source-return, or environment burden. |
| `flowOrControlVariant` | Change transformation flow, control depth, rate band, feedback boundary, or mediator relation. | State the timing, control, observability, or accountability burden created by the change. |
| `interfaceGrammarChange` | Narrow, split, widen, or stabilize an interaction boundary. | Apply `A.6.M` when module-interface relation repair is current. |
| `declaredScopeOrHolonLevelChange` | Split, merge, add, or remove a declared holon-level reference, declared scope, evidence scope, work-method scope, or aggregation scope. | Name the affected reference, use `C.30.STRAT` when the wording is only a stratification term, and use `B.2` only when whole reidentification is current. |
| `boundedException` | Keep a residual because removing it costs more than it buys now. | State the exception, reopen trigger, and next subject pattern if later source use or decision use expands. |

**Didactic mini-slices.** Use these as examples of the kind of work C.32 expects, not as domain-specific templates.

| Situation | First C.32 step | Candidate repair |
|---|---|---|
| A sterilization function is placed in a shared field module, but the field placement has no power and no certified evidence relation for that heat cycle. | Keep the functional demand separate from the module and placement structures. | Add a local certified bearer, split the function into pre-field and field steps, change placement, or reject the shared-module candidate. |
| An ML functional graph includes retrieval, planning, and action, but no module-interface relation or direct domain predicate carries evidence-refresh responsibility or admissible-use control. | Treat the graph as functional structure and recover module-interface, evidence, control, admitted-System, and responsibility relations separately. | Add a retrieval service and an admitted evidence-refresh responsibility relation with actual participants, add a supervisor relation, narrow model-interface behavior, return the exact missing governor, or reject the candidate. |
| A Method family says the review function is automated, but A.6.F identifies no bearer and no direct responsibility predicate identifies who is responsible for exceptions. | Recover the Method structure and A.6.F function bearer first. Keep any admitted Systems, local kinds, separate System-classification judgments, assignments, actual Work with its F.6 attribution, responsibility relation, and evidence structure separate. | Propose an assignment condition only in truthful plan or candidate content; cite a direct exception-responsibility relation or exact missing governor; split the Method step, change evidence scope, or keep the automation as source cue. Use a full Work chain only after performance. |

When one independently typed architecture-side or other source constrains transformed-side architecture content for a changed referent, use `C.32.CONWAY` before using Conway, mirroring, or inverse-Conway language in candidate synthesis. The practitioner names the changed referent and any actual A.3.4 transformation separately, each influence source by exact kind and its direct relation only when that occurrence is asserted, and, for each actual architecture side, the exact C.30 described holon, obtaining `ArchitectureRelation`, and selected `U.Structure`; modal architecture content stays in an exact `ArchitectureClaim`. Without an admitted and satisfied direct influence predicate, the pressure stays synthesis-local in the C.32.CONWAY frame with its `missing-governor`, unresolved-grounding, or false-predicate disposition and no exact pair row. Candidate work then names influence-source-side, transformed-side, joint, or bounded-mismatch changes, architecture characteristics under pressure, expected gains, known losses, and source-return conditions.

Keep the candidate palette as the C.32 result. `C.32.CONWAY` carries the architecture-influence correspondence frame or one exact reusable pair-row episteme. Influence alone supplies no acting System, local system-role kind, System-classification judgment, assignment, Work, changed-referent identity, or transformation participation. Transformation, acting and Work attribution, exact influence, transformation-flow, and module-interface claims belong to `A.3.4`, `A.12`, `A.2.1`, `A.15.1`, `F.6`, the direct influence pattern, `E.18`, `C.30.TFS-REL`, or `A.6.M` when current. Structural-similarity or preservation claims belong to `C.29` when they are current.

A richer dossier is optional. Open it only when one candidate must carry source views, relation notes, measurements, C.29 lens outputs, evidence notes, or failure repairs that affect the next architecture use. Ordinary C.32 use should remain one row per candidate configuration.

**Downstream use.** The C.32 result is architecture-specific candidate content. Use `G.5` to declare a selected-set result, `C.11` for a fixed local choice, and `C.32.PAD` for a project architecture decision. Use `C.18` or `C.19` for archive, front, pool-treatment, or generation policy when that claim is current. Use `C.30.AD` for architecture-description work. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.

**Stop condition.** Stop C.32 when the palette can support the next use without hiding the selected structures, architecture-change kind, architecture gain, architecture loss, constraint fit, source-return condition, or pattern for the next question.

**Lowering condition.** Lower the record out of C.32 use when the needed architecture claim is not grounded, the item is only a source artifact, only one configuration is visible, the candidate lacks selected-structure change, the functional demand has no feasible bearer, the architecture gain or loss is unnamed, or the next use is already comparison, selection, selected-set result declaration, actual publication, local choice, decision, evidence, or assurance. Use `C.30` for grounding, the source or description pattern for source artifacts, `C.32.FAIL` for candidate repair, and the named pattern for the next question when the downstream claim is current. Reopen C.32 when a criteria row, eval result, retained alternative, front relation, source-return trigger, or source-currentness change alters the selected structures under pressure or the acceptable loss profile.

