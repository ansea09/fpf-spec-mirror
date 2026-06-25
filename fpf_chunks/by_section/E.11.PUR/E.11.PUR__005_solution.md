---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Recommendation and Pattern-Use Sequence"
section_id: "E.11.PUR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__005_solution.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "E.11.PUR — Pattern-Use Recommendation and Pattern-Use Sequence"
  - "E.11.PUR:4 — Solution"
line_start: 69058
line_end: 69133
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.5"
  - "A.16"
  - "A.21"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "E.8"
keywords:
---

### E.11.PUR:4 - Solution

Use three registers deliberately.

In engineer-facing speech, phrases such as "first useful move", "working move", "professional move", "SoTA move", "strong move", "admissible move", and "next move" may stay when they help a team ask what to do next.

In didactic pattern-language speech, the same idea can be explained as building a useful FPF phrase from pattern words: one pattern may frame the problem, another preserve variants, another recommend an architecture question, another carry the decision toward work, and another update SoTA or wording.

In the precise FPF layer, do not create a `Move` kind from either metaphor. Recover `PatternUseRecommendation@Context` for the recommended use of one pattern, `PatternUseSequence@Context` for several pattern uses, and the direct governing pattern for work, plan, gate, decision, publication, architecture, source, or transformation claims.

#### E.11.PUR:4.1 - PatternUseRecommendation@Context

`PatternUseRecommendation@Context` is a dependent durable pattern-use relation value. It says which FPF pattern use is recommended now for one current concern.

E.24.UK settlement: this pattern does not introduce a root `U.PatternUseRecommendation`, a root `U.Move`, or an independent pattern-use ontic. The governed value is a context relation over existing values: project concern, bounded context, candidate pattern uses, governing pattern, applicability finding, recommended pattern use, expected practical result, and neighboring governing-pattern refs. `PatternUseSequence@Context` is the sequence form of the same relation discipline, not a workflow, lifecycle, route, WorkPlan, or performed work.

```text
PatternUseRecommendation@Context:
  ProjectConcernRef
  BoundedContextRef
  PatternUserOrAgentRef?
  GoverningPatternRef
  CurrentEntityOfConcernRef?
  CurrentClaimOrRelationKindRef?
  RecognitionCueRef?
  CandidatePatternUseSet?
  ApplicablePatternUseSet?
  ApplicabilityFinding
  RecommendedPatternUse
  ReasonForRecommendation
  ExpectedPracticalGain?
  OutputRefOrOutputShape
  AdmissibleUse
  BlockedStrongerUse
  StopCondition
  NextGoverningPatternRef?
  ReturnOrReopenCondition?
```

`RecommendedPatternUse` is stronger than an applicability finding. It means: this pattern use is selected as useful for the current concern, given the available candidate pattern uses and the expected practical result. If a project actor then plans or performs work, that resulting object is governed by `U.WorkPlan`, A.21, or `U.Work`, not by this pattern-use relation.

#### E.11.PUR:4.2 - PatternUseSequence@Context

Use `PatternUseSequence@Context` when several recommended or applied pattern uses must be kept together:

```text
PatternUseSequence@Context:
  ProjectConcernRef
  BoundedContextRef
  SequencePurpose
  PatternUseRefs
  OrderingReason?
  OutputChain
  DirectGoverningPatternForEachUse
  BlockedWorkflowOverread
  StopCondition
  ReturnOrReopenCondition?
```

The sequence is not a work plan, route, workflow, lifecycle, or performed work. It is only a relation among pattern uses unless a neighboring pattern makes work planning, call planning, transformation-flow structure, gate decision, or performed work current.

#### E.11.PUR:4.3 - Boundary Table

| Current claim | Use |
| --- | --- |
| Which FPF pattern use is recommended now? | `PatternUseRecommendation@Context`. |
| Which several FPF pattern uses belong together for this concern? | `PatternUseSequence@Context`. |
| Accepted problem-side material is carried toward a next FPF value. | `E.18.1`. |
| Work is intended, scheduled, or prepared. | `A.15.2`, `A.15.3`, or `A.15.5`. |
| Work actually occurred. | `A.15.1`. |
| A gate admits, degrades, blocks, or abstains. | `A.21`. |
| An AI agent is planning tool calls. | `C.24`. |
| Architecture candidate material is current. | `C.30` or the direct architecture child pattern. |
| Language-state transition is current. | `A.16`. |
| Publication expression makes the pattern use visible. | `E.8`, `E.11`, `E.17`, or the direct publication pattern. |

