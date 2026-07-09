---
chunk_kind: "child"
pattern_id: "E.10.MOVE"
pattern_title: "Move and Readiness Wording Precision Restoration"
section_id: "E.10.MOVE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.MOVE/E.10.MOVE__005_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.10.MOVE — Move and Readiness Wording Precision Restoration"
  - "E.10.MOVE:4 — Solution"
line_start: 70052
line_end: 70136
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.16"
  - "A.16.0"
  - "A.21"
  - "A.3.4.P"
  - "B.1.6"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.11.PUR"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "G.6"
keywords:
---

### E.10.MOVE:4 - Solution

Apply this recovery order:

1. Name `GovernedTextSpan`: the exact text span whose move-like or readiness-like wording is being repaired.
2. Name `ClaimBeingMade` and `ObjectUnderWordingRepair`: what claim, relation, object, change situation, intended result, or remaining reader use made the wording matter?
3. Classify borrowed or ordinary wording: seminar pattern-use language, TameFlow `MOVE` wording, work-entry readiness, local move locus, ordinary prose, or quote-only wording.
4. Decide `DirectFPFTarget`: `PatternUseRecommendation@Context`, E.18.1 P2W, `U.WorkPlan`, PlanItem, `SlotFillingsPlanItem`, `WorkEntryReadiness@Context`, A.21 `GateDecision`, performed `U.Work`, `U.Transformation`, `U.Method`, `U.MethodDescription`, A.16 language-state move, C.24 call planning, C.30 architecture candidate move, selected set, publication expression, source relation, or ordinary prose.
5. If several values are current, split them and name the direct governing pattern for each.
6. Preserve `RemainingReaderUse`. The repair fails if the text becomes formally clean but no longer tells the practitioner what can be done now.
7. Use `A.3.4.P` for the change-situation branch and return to `E.10.MOVE` only for pattern-use, direct-object, or work-entry readiness wording left after the transformation branch is recovered.

#### E.10.MOVE:4.1 - MoveAndReadinessWordingRepair note

```text
MoveAndReadinessWordingRepair:
  EncounteredWording:
  GovernedTextSpan:
  ClaimBeingMade:
  ObjectUnderWordingRepair:
  EncounteredWordingClass: seminarPatternUse | tameFlowMoveWording | workEntryReadiness | localMoveLocus | ordinaryProse | quoteOnly
  DirectFPFTarget:
  RecoveredRelations:
  DirectGoverningPatterns:
  RetainedPlainWording:
  BlockedOverread:
  RequiredSplit?:
  FinalWordingOrBlocker:
  RemainingReaderUse:
```

The note is a temporary wording-use restoration aid. It does not create project records, gate decisions, WorkPlans, or work occurrences.

#### E.10.MOVE:4.2 - Short Cue Set

Trigger this pattern only when the wording has FPF-governed use:

- move, first useful move, working move, professional move, SoTA move, strong move, admissible move, next move;
- step, action, application, solution, next action, work item, work entry;
- full kit, full-kitting, readiness, ready, committed, launch-ready;
- TameFlow `MOVE` or source MOVE;
- route, workflow, and process when the wording hides pattern-use, direct-object, or readiness relation rather than a transformation-situation claim.
- unfolding, path, loop, flow, diffusion, graph, chain, route, workflow, and process when the wording hides a selected structure, description, demonstrative slice, method, work, evidence, gate, publication, decision, architecture use, or currentness/refresh claim governed by `G.11` or slice-local refresh governed by `E.18`.

The list is not a replacement vocabulary. It is a recognition aid for the recovery order.

#### E.10.MOVE:4.2a - Step And Action Synonym-Substitution Repair

Do not close a move-like repair by replacing `move` with `step`, `action`, `application`, `solution`, `work item`, or `next action`. Those words are still triggers when they carry FPF-governed use. A conforming repair first names the object under wording repair, then the direct FPF target: pattern-use recommendation, P2W carry-through, `U.WorkPlan`, `SlotFillingsPlanItem`, `WorkEntryReadiness@Context`, `GateDecision`, performed `U.Work`, transformation, method, publication, source relation, local language-state move, call-planning action, architecture candidate record, ordinary prose, or quote-only wording. The final wording may keep `step` or `action` only when the direct governing pattern and remaining reader use are explicit.

#### E.10.MOVE:4.3 - Source-Wording Classes

| EncounteredWordingClass | Typical recovery |
| --- | --- |
| `seminarPatternUse` | `PatternUseRecommendation@Context`, `PatternUseSequence@Context`, publication phrase, or direct neighboring pattern. |
| `tameFlowMoveWording` | WorkPlan, PlanItem, full-kit preparation, `WorkEntryReadiness@Context`, A.21 when gate decision is current, preparation `U.Work`, target `U.Work`, resource relation, or result relation. |
| `workEntryReadiness` | `WorkEntryReadiness@Context`, `FullKitCondition`, A.15.2, A.15.3, A.15.1, A.21, B.1.6, or A.15.4. |
| `localMoveLocus` | A.16 language-state move, C.24 call-planning action, C.30 architecture candidate move, or another accepted local locus. |
| `unfoldingStructureWording` | `A.22.CGUS` only when several loci, cross-locus constraints, preserved and lost structure, admissible next forms, and stop or return conditions are recoverable; otherwise select the direct governing pattern for description, demonstrative slice, method, work, evidence, gate, decision, architecture, publication, or currentness/refresh, or record a no-restoration ordinary-prose disposition when no FPF object is being claimed. |
| `ordinaryProse` | Keep or lightly rewrite without FPF restoration. |
| `quoteOnly` | Keep as source wording and block stronger use. |

#### E.10.MOVE:4.4 - Relation to A.3.4.P

Use `A.3.4.P` first when the wording is mainly about change in the world or a transformation-flow structure:

- process, workflow, path, pipeline, operation, flow, transformation, change, circuit, network, and route-like wording;
- graph path, path slice, flow valuation, or transformation-flow structure claims;
- method, mechanism, work, or publication-description confusion caused by change-situation wording.

Use `E.10.MOVE` when the remaining question is: which object under wording repair, pattern use, work-entry readiness relation, or local move locus should the reader use next? If both are current, split the text and apply both patterns to their own current objects.

#### E.10.MOVE:4.5 - Durable Name Repair

Durable field and record names must name the direct FPF target they recover. Examples:

| Dirty durable name | Prefer |
| --- | --- |
| `FirstMoveRecord@Context` | `FirstApplicationRecord@Context` when the object is the first application record. |
| `RelationMoveNow` | `CurrentRelationGovernedUse` when the object is the local `A.15.4` relation-governed use. |
| `NextMoveHypothesis` | `RecommendedPatternUse` or another direct candidate, selected set, work, gate, or architecture object. |
| `Pattern-Use Sequence` | `PatternUseSequence@Context` when the durable relation is meant. |

Do not run these as mechanical global replacements. Recover the governed object first.

