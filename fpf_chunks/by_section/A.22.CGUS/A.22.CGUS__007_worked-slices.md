---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:5"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__007_worked-slices.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:5 — Worked Slices"
line_start: 31485
line_end: 31519
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

### A.22.CGUS:5 - Worked Slices

**Architecture P2S slice.** A team starts with architecture-relevant problem pressure. The unfolding structure may organize problem pressure, unknown structures, candidate structures, architecture characteristics, decision locus, realization work linkage, actual structure feedback, and return conditions. The P2S flow card can describe that organization, but the architecture decision remains governed by `C.32.PAD`, architecture descriptions by `C.30.AD`, and performed work by the A.15 family.

**Abductive search slice.** An inquiry starts from an abductive prompt and a cue set selected for the search. The unfolding structure may organize rival hypotheses, plausibility constraints, hypothesis-generation loci, evidence-return loci, and downstream tests. The structure is not evidence; evidence appears only when an evidence pattern governs the claim.

**Improvement-loop slice.** A pattern version has an evaluation frame and current evaluation result. The unfolding structure may organize candidate repairs, protected tradeoffs, expected evaluation movement, loop-decision locus, and re-evaluation. The loop is not improvement by shape; `E.23` governs improvement only after the object version and evaluation relation are recoverable.

**First-entry seed slice.** A README entry says "develop or review architecture." That line may seed an entry unfolding among problem-side records, candidate first governed records, likely governing-pattern returns, and next readable outputs. The README line is a seed description, not the project's unfolding structure and not a universal FPF route.

**Field-filled scaffold slice.** A team has a visible card sequence "problem pressure -> candidate options -> eval -> repair." At first this is only a demonstrative slice. It becomes a CGUS record only after fields are recoverable:

```text
acceptedStartingRecordRefs[]: ProblemCard@Cooling-v2; EvaluationResult@thermal-margin-v1
acceptedStartingStructureRefs[]: current module-placement structure
declaredStructureSubstrateRef: architecture-facing candidate synthesis and improvement-loop structure
unfoldingLoci[]: pressure locus; candidate-set locus; eval-result locus; repair-choice locus; return locus
constraintRefs[]: thermal margin threshold; service-access constraint; accepted-loss boundary
invariantRefs[]: cooling path must remain maintainable
guardedTransitionRefs[]: candidate enters repair only after eval-result relation is named
preservedStructure: candidate alternatives plus repair-locality relation
lostOrHiddenStructure: rejected-candidate details not shown in the teaching chain
admissibleNextFormKindRefs[]: C.32 candidate palette update; E.23 improvement input; C.32.PAD decision only later
structureUseReturnCondition: return to C.32 when a new candidate structure appears; return to E.23 when the changed object version is evaluated
stopCondition: keep as DemonstrativeUnfoldingSlice until candidate-set and eval relations are named
```

The same visible chain helps planning because each position asks for a slot. It does not make the project follow that order and does not authorize work.

**Reference-currentness slice.** A SoTA pack relies on telemetry and admitted reference-publication editions that may decay. CGUS may organize the current reference set, edition-shift loci, decay triggers, possible deprecation or reship, and return condition. The structure is not the currentness decision; `G.11` governs freshness, telemetry, decay, deprecation, reship, and no-change claims.

**Physical-modeling slice.** A team models a physical system or another governed EntityOfConcern whose behavior depends on component relations, conservation-like constraints, operating modes, calibration data, and analysis goals. CGUS may organize the model structure, admitted measured data, mode-change loci, compiler boundary, solver boundary, surrogate-substitution boundary, and return to calibration or model-discovery work. In a digital-twin case, the physical entity, digital model, measured-data history, simulation outputs, services, and bidirectional correspondence links remain different loci or records and relations governed by their direct patterns. The simulation run, generated code, exchange package, AI-assisted model edit, calibration result, and digital-twin publication are also separate produced carriers, work outputs, calibration records, or publications. Acausal modeling is useful here because it shows that relations and constraints can be stated before a calculation direction is chosen; `C.29`, `G.11`, `E.23`, evidence patterns, and domain DPF patterns govern stronger mathematical, currentness, evaluation, evidence, or domain-validity claims.

**Method/work linkage slice.** A method description is admitted because it may realize a governed structure change or change set. CGUS may organize the method relation, work-plan seed, readiness condition, expected structure effect, evidence or gate linkage, and stop condition. It does not authorize work. The method, plan, work-entry readiness, performed work, evidence, assurance, and gate claims remain with A.3, A.15, A.10, B.3, A.20, and A.21.

