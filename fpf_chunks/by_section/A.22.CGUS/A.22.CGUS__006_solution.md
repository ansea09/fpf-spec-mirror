---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__006_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:4 — Solution"
line_start: 31281
line_end: 31484
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "B.3.5"
  - "B.5.2"
  - "C.13"
  - "C.2.P.DR"
  - "C.3"
  - "C.32.P2S"
  - "C.35"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.23"
  - "E.9"
  - "E.9.DA"
  - "G.11"
keywords:
---

### A.22.CGUS:4 - Solution

Select `ConstraintGovernedUnfoldingStructure@Context <: U.Structure` as a thin A.22 specialization of `U.Structure` for constraint-governed unfolding across named loci.

A constraint-governed unfolding structure is a `U.Structure` whose relation signatures, constraints, invariants, guarded transitions, preserved and lost structure, and governing-pattern exits make several loci jointly constrain admissible next forms. It states how admitted starting records and already-current structures can participate in that structure. It does not state that real work must occur in the displayed order, and it does not require one starting record, one starting structure, or one resulting record.

Do not read "unfolding" as a chain by default. The unfolding structure may be branching, merging, cyclic, partially ordered, or graph-shaped, and it may leave several alternative next forms live at once. A linear chain, cycle drawn as "back to the start", seminar order, prompt path, or happy path is usually a `DemonstrativeUnfoldingSlice@Context`: one declared traversal or presentation of a wider structure.

#### A.22.CGUS:4.1 - Ontic Field Block

```text
ConstraintGovernedUnfoldingStructure@Context:
  kind: U.Structure
  unfoldingStructureId:
  boundedContextRef:
  declaredStructureSubstrateRef:
  entityOfConcernRef:
  acceptedStartingRecordRefs[]:
  acceptedStartingStructureRefs[]:
  promotedCoreFamilyCueRefs[]?:
    UF.P2W |
    UF.P2S |
    UF.ABD |
    UF.NAR |
    UF.IMP |
    UF.GND |
    UF.SEL |
    UF.REFRESH |
    UF.CALL |
    otherDeclared
  localFamilyCueRefs[]?:
  unfoldingFamilyClass?:
    transformationFlow |
    methodWork |
    reasoningSearch |
    narrativeOrdering |
    improvementLoop |
    typingGrounding |
    architectureSelection |
    selectionOrPortfolio |
    referenceCurrentness |
    toolUsePlanning |
    otherDeclared
  specializedStructureRef?:
  relationSignatureRefs[]:
  unfoldingLoci[]:
  constraintRefs[]:
  invariantRefs[]:
  guardedTransitionRefs[]:
  preservedStructure:
  lostOrHiddenStructure:
  admissibleNextFormKindRefs[]:
  defaultDemonstrativeSliceRecipeRefs[]:
  admissibleUse:
  nonAdmissibleUse:
  structureUseReturnCondition:
  stopCondition:
  reopenOrRefreshTriggers[]:
```

`acceptedStartingRecordRefs[]` names already admitted project records that the unfolding structure may use at the start of the current use: problem cards, `G.2` source packs, candidate-set records, evaluation results, cue publications, or other governed records. Each record must keep its own direct governing pattern and admitted use. The field does not make raw source prose, attractive distinctions, prompts, model output, or a visible route into an admitted starting record by itself.

`acceptedStartingStructureRefs[]` names already-current `U.Structure` refs that the unfolding structure may use at the start of the current use. This slot is intentionally separate from `acceptedStartingRecordRefs[]`: a record may describe, publish, or evaluate a structure, but it is not that structure.

`declaredStructureSubstrateRef` names the structure substrate whose loci and relations are being unfolded, such as transformation-flow structure, architecture-facing structure use, narrative ordering, abductive search, improvement loop, typing-grounding passage, refresh situation, or option-selection structure. `entityOfConcernRef` names the entity or concern whose unfolding is being organized. `unfoldingLoci[]` names the governed positions inside the structure. The accepted-starting slots are therefore not duplicates of substrate, EntityOfConcern, or loci: they record which admitted records and current structures are available at the start of the current unfolding use.

`promotedCoreFamilyCueRefs[]?` may name short FPF-core cues such as `UF.P2S` or `UF.REFRESH` when they help readers recognize a familiar core family. These cues are optional examples, not a maintained list, not a conformance vocabulary, and not a DPF index. A DPF or project-local package may use `localFamilyCueRefs[]?`, local cue examples, or no family cue at all; its authoritative route is the local governing-pattern map plus the relevant FPF and DPF pattern bodies. `unfoldingFamilyClass?` is optional broad retrieval and review shorthand; it is not the governing vocabulary.

`specializedStructureRef` is used only when a narrower `U.Structure` specialization is current, such as `E.18.3` for transformation-flow unfolding, `C.32.P2S` for architecture-facing P2S, `B.5.2` for abductive search, `A.6.3.NAR` for narrative ordering, `E.23` for improvement loops, or typing-grounding patterns for constructive-to-logical grounding.

#### A.22.CGUS:4.1a - Field Glosses

These fields are ordinary structure slots, not a second method, work, evidence, architecture, or publication record.

| Field | What this slot names | Not this | Direct exit when stronger claim is current |
| --- | --- | --- | --- |
| `relationSignatureRefs[]` | references to relation signatures that make the unfolding positions connectable | not proof that the relations hold in the world | `A.6.0`, `A.6.5`, or the pattern governing the relation |
| `constraintRefs[]` | constraints that restrict admissible continuations | not a gate result or work authorization | `A.20`, `A.21`, A.15 family, or the domain pattern |
| `invariantRefs[]` | structure that must survive admissible unfolding | not a measurement or evidence result | `C.16`, `C.25`, `A.10`, or `B.3` when those claims are current |
| `guardedTransitionRefs[]` | guarded changes between loci or admissible next positions | not a performed work occurrence | `A.3.4`, A.15 family, `A.20`, or `A.21` |
| `preservedStructure` | selected structure kept by this unfolding use | not a claim that every selected starting structure or source-described structure is preserved | `C.33`, `C.34`, or the direct governing pattern for the preservation claim |
| `lostOrHiddenStructure` | selected or expected structure not carried by the unfolding use | not a defect by itself | structure-use return condition, `C.33`, `C.34`, or the direct governing pattern named by the use |
| `admissibleNextFormKindRefs[]` | kinds of records or uses that may be written next | not a required sequence and not execution | receiving governing pattern for each next form |
| `defaultDemonstrativeSliceRecipeRefs[]` | teaching or planning slice recipes over the structure | not the structure and not work order | `DemonstrativeUnfoldingSlice@Context`, `E.17`, or A.15 family as current |
| `admissibleUse` | what this CGUS may safely support | not blanket permission for all uses | direct governing pattern for the supported claim |
| `nonAdmissibleUse` | blocked overread for this CGUS use | not a negative catalogue of every possible mistake | direct governing pattern that would be needed for the blocked claim |
| `structureUseReturnCondition` | condition that names the selected structure or expected structure at issue, the lost or hidden distinction, and the receiving governing pattern; when current it also names the exact source description, publication, source-use relation, lens result, extraction, or probe locus whose use must be repaired | not a `G.11` refresh unless currentness or decay is the claim | receiving governing pattern named by value |
| `stopCondition` | condition for keeping the current record, description, or demonstrative slice at reduced use | not failure of the admitted starting record, source pack, or description by itself | A.16, E.11, E.17, or the direct governing pattern as applicable |
| `reopenOrRefreshTriggers[]` | changed facts, currentness, or use conditions that reopen the smallest affected claim | not a new reopen and refresh ontology | `G.11` for currentness or decay; `E.18` for slice-local refresh; the direct governing pattern for repair |

#### A.22.CGUS:4.2 - Admission Test

Use CGUS only when all of these are recoverable enough for the next use:

| Coordinate | Required recovery | If missing |
| --- | --- | --- |
| Several logical loci | More than one governed position is live: problem-side record, current structure, candidate set, method relation, work-planning locus, evidence locus, reader route, evaluation row, refresh trigger, or another declared position. | Keep the candidate wording as a note, cue, recommendation, or description. |
| Cross-locus constraints | Loci constrain each other through relations, guards, boundaries, preserved or lost structure, stop rules, or return conditions. | Treat a list of steps or pattern IDs as an index until constraints are recoverable. |
| `U.Structure` specialization | The object is a `U.Structure` under A.22 or a narrower `U.Structure` specialization governed elsewhere. | Treat a card, graph, narrative, publication, README line, or method description as a description or seed. |
| Admissible next forms | One or more next forms are named: pattern-use recommendations, candidate sets, narrative orderings, work-plan seeds, method-selection frames, evaluation repair frames, architecture inputs, return requests, refresh actions, or demonstrative slices. | Do not sell the structure as user-facing solution structure. |
| Direct governing-pattern exits | Any locus that makes a stronger claim points to the pattern that governs that claim. | The unfolding structure is overreading itself as method, work, evidence, gate, decision, architecture, or publication authority. |
| Non-workflow boundary | The actual project sequence remains allowed to be nonlinear, iterative, partial, or interrupted. | Lower the artifact to a work plan or method description only if the direct pattern governs that claim. |
| Non-chain topology | Branches, joins, cycles, partial orders, many-to-many constraints, or alternative live next forms remain visible when they matter. | Treat a linear chain as a demonstrative slice until the wider structure is recoverable. |
| Stop, split, return, refresh | Conditions for stopping, splitting, returning to a governing pattern, or refreshing after changed evidence, currentness, or context are named. | The structure becomes a one-way story that cannot localize repair. |

#### A.22.CGUS:4.3 - Descriptions And Demonstrative Slices

Keep the structure separate from descriptions and teaching slices.

```text
ConstraintGovernedUnfoldingStructureDescription@Context:
  kind: U.Episteme
  entityOfConcernRef: ConstraintGovernedUnfoldingStructure@Context
  representationSchemeRef:
  viewpointRef?:
  preservedStructure:
  lostOrCoarsenedStructure:
  declaredUse:
  descriptionUseReturnCondition:
  publicationRefs[]?:
```

```text
DemonstrativeUnfoldingSlice@Context:
  kind: U.Episteme
  entityOfConcernRef: ConstraintGovernedUnfoldingStructure@Context
  demonstrationUseKind:
    happyPath |
    workedSlice |
    firstUseExample |
    promptExample |
    actualCaseReplay |
    variantComparison |
    otherDeclared
  traversalOrOrderingRuleRef:
  includedLocusRefs[]:
  omittedBranchRefs[]:
  loopCompressionPolicyRef?:
  alternativeSliceRefs[]?:
  presentationFormKind:
    orderedList |
    chainDiagram |
    flowCard |
    table |
    narrativePath |
    slideSequence |
    promptBlock |
    graphSlice |
    otherDeclared
  admissibleUse:
  nonAdmissibleUse:
  sliceUseReturnCondition:
```

`DemonstrativeUnfoldingSlice@Context` is the right place for a happy path, P2W chain, P2S chain, cycle steps, prompt example, case replay, or seminar sequence. The slice shows one admissible traversal of the unfolding structure for a declared use. It is not a chain in the world and not a performed-work order.

When a graph-shaped or workflow-shaped description is used for teaching, record which branches, joins, cycles, or alternatives are included, omitted, compressed, or represented by a "return to start" arrow. The slice may be a chain because the reader needs one path; the governed unfolding structure need not be a chain.

A demonstrative slice may also be used before execution as a slot-filling scaffold. The presentation chain holds attention on visible positions such as "first record", "candidate repair", "evaluation row", "gate condition", or "return". Each visible position asks which CGUS field or direct governing pattern must be filled: admitted starting record, starting structure, locus, constraint, invariant, guard, preserved structure, lost structure, admissible next form, stop condition, return condition, method or work link, evidence link, architecture use, or publication use. The chain helps the team plan the structure by filling or rejecting these slots; it does not make the slot filled and does not authorize the work.

Use the scaffold in small passes. First name the visible positions. Then attach each position to `unfoldingLoci[]` or to a direct governing pattern. Then fill constraints, invariants, guards, preserved and lost structure, admissible next forms, and stop or return conditions. If a position cannot be attached to a locus or governing pattern, keep the chain as a seed description or demonstrative slice and do not admit the full unfolding structure yet.

For example, "draft -> evaluate -> repair -> re-evaluate" is a useful presentation chain for an improvement cycle only after the object version, evaluation frame, candidate repair loci, expected evaluation movement, loop-decision locus, and stop or continue condition are recoverable. Before those slots are filled, the chain is a planning scaffold, not an improvement loop and not performed work.

#### A.22.CGUS:4.4 - Direct Governing Pattern Exits

CGUS carries the unfolding structure. It does not absorb stronger claims.

| Stronger claim being made | Direct governing pattern or family |
| --- | --- |
| Atomic bounded change | `A.3.4` |
| Method or method description | `A.3.1`, `A.3.2`, and method-composition patterns |
| Work plan, work entry, or performed work | `A.15.2`, `A.15.5`, `A.15.1`, and neighboring work patterns |
| Evidence, assurance, or gate | `A.10`, `B.3`, `A.20`, `A.21`, `G.6` as current |
| Architecture use, architecture decision, or architecture description | `C.30`, `C.30.ASV`, `C.32.P2S`, `C.32.PAD`, `C.32.ADR`, `C.30.AD` |
| Narrative rendering or publication use | `A.6.3.NAR`, `E.17`, `E.17.0` |
| Improvement of an object version | `E.23`, with evaluation patterns for the declared object |
| Source currentness, decay, edition shift, or refresh orchestration | `G.11` |
| Mathematical lens or formal modeling | `C.29`, `A.6.0`, `A.6.1` |

Use the word `refresh` only when a currentness, telemetry, edition, decay, or slice-local refresh claim is actually current. Otherwise use plain return, stop, split, or repair wording and name the direct governing pattern.

#### A.22.CGUS:4.4a - Direct Governing-Pattern Dependent Records

Some CGUS uses need dependent records that keep adjacent method, work, evidence, architecture, description, or publication claims inspectable. A.22.CGUS does not define those record schemas. It only requires that a CGUS field name the direct governing pattern before a stronger claim is relied on.

For method and work linkage, use the A.15-owned `MethodWorkUnfoldingLinkage@Context` only when the relation among method, method description, role assignment, capability-fit condition, work plan, readiness, performed work, evidence, assurance, or gate must stay inspectable as a relation. If only one method, work-plan, readiness, performed-work, evidence, assurance, or gate claim is current, use that direct governing record instead.

For architecture use, use the C.32.P2S-owned `ArchitectureUnfoldingStructureUse@Project` only when a named unfolding structure is being used as architecture-relevant structure in problem-to-structure architecturing. If the current claim is only grounded architecture, structural view, architecture description, decision, ADR-like projection, measurement, eval, or performed realization work, use the direct pattern for that claim.

This keeps A.22.CGUS thin: it governs the constraint-governed unfolding structure and its safe next-use boundary, while A.15, C.30, C.32, evidence, gate, publication, and domain patterns govern the adjacent records that carry stronger claims.

#### A.22.CGUS:4.5 - Promoted Core Family Cue Examples

The FPF core may promote a few short family cues when a cue helps readers recover a familiar governing pattern and a common blocked overread. This is an example device, not a maintained list of all CGUS families.

For example, `UF.P2S` can be useful when an architecture-facing question moves from problem pressure to candidate, selected, expected, or actual structures. The cue points the reader toward `C.32.P2S` and warns that a P2S card is not itself the architecture decision, architecture description, ADR, or realization work.

For example, `UF.IMP` can be useful when an object version, evaluation frame, candidate repairs, and re-evaluation are current. The cue points toward `E.23` and warns that a retry loop or prompt loop is not quality improvement by shape.

For example, `UF.REFRESH` can be useful when a `G.11` source-currentness relation, telemetry, evidence decay, or edition shift is current. The cue points toward `G.11` and warns that a stale reference set is not current authority.

If no promoted cue helps, omit the cue. Do not invent a core `UF.*` cue merely to make a CGUS use look governed. DPFs and project-local frameworks may carry their own local cue examples when useful, but the governing claim still comes from the local governing-pattern map and the relevant pattern bodies.

