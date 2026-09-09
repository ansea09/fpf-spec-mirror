---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:4"
section_title: "Solution - Structured abductive micro-cycle"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__005_solution-structured-abductive-micro-cycle.md"
commit_sha: "aa10af7e8221518114822d00bb9cf11e6c41f6b2"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:4 — Solution - Structured abductive micro-cycle"
line_start: 41098
line_end: 41154
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
keywords:
  - "abduction"
  - "candidate hypotheses"
  - "explanatory prompt"
  - "origin trace"
  - "plausibility filters"
  - "route-to-hypothesis"
---

### B.5.2:4 - Solution - Structured abductive micro-cycle

`B.5.2` begins from an admissible `U.AbductivePrompt`, expands a candidate set, compares it under explicit plausibility criteria, and publishes the selected conjecture as a hypothesis-bearing `U.Episteme`. Preserve the supports, rivals, limitations and allowed downstream use. Abduction alone assigns no `AssuranceLevel`.

#### B.5.2:4.1 - Nature of abduction in FPF

In FPF, abduction proposes a presently most plausible candidate explanation, model or conjecture under a declared prompt. Its plausibility can justify keeping or using that conjecture for a bounded purpose, but does not establish its causal mechanism or a stronger empirical claim. Deduction, evidence synthesis and action choice keep their own questions.

#### B.5.2:4.2 - Four-step micro-cycle

| Step | Core activity | Required publication outcome |
|---|---|---|
| **1. Frame the prompt** | State the initiating `U.AbductivePrompt` precisely enough that the unexplained contrast, opportunity, or probe pressure is explicit. | A prompt record with open question, scope notes, and provenance. |
| **2. Generate candidate hypotheses** | Produce multiple candidate conjectures that could resolve the prompt. | A visible candidate set, even if lightweight. |
| **3. Apply plausibility filters** | Compare candidates against explicit plausibility criteria. | A short rationale that records why some candidates remain live and others are rejected. |
| **4. Select and publish the prime hypothesis** | Choose the presently preferred conjecture where the comparison warrants one. | A hypothesis-bearing `U.Episteme` with its prompt, selection rationale, live rivals, supports, fragilities and allowed use. No universal level or mandatory next experiment follows. |

The loop is intentionally iterable. A selected prime hypothesis may later be replaced, narrowed, or reopened if deduction, probe work, or evidence reveals a better rival.

#### B.5.2:4.3 - Entry discipline via `U.AbductivePrompt`

`AnomalyStatement` remains a canonical prompt species, but it is not the only one. `B.5.2` also accepts the broader prompt species governed by `B.5.2.0`, such as `ProblemCuePrompt`, `OpportunityCuePrompt`, and `ProbeCuePrompt`. This broadens entry without dissolving type discipline.

#### B.5.2:4.4 - Plausibility filters

The filtering step is local and context-sensitive, but the criteria used **SHALL** be explicit. Typical filters include:

- **Parsimony.** Does the candidate introduce only the additional structure that the prompt requires?
- **Explanatory reach.** How much of the prompt does the candidate actually account for?
- **Consistency with established constraints.** Does the candidate avoid collision with already trusted pillars, mechanisms, or scope declarations?
- **Falsifiability / probeability.** What implication, deduction or possible observation could discriminate the candidate from its rivals? Keep that question separate from whether a check is obtainable and worth performing now.
- **Scope fit.** Is the candidate framed for the declared prompt scope rather than for an inflated or shifted target?

No one filter is universally decisive. The pattern only requires that at least two filters be declared when a prime hypothesis is selected.

#### B.5.2:4.5 - Abductive Unfolding Structure Block

When the abductive run must be reused as more than a one-off hypothesis note, add an unfolding block. It shows how the prompt becomes rival hypotheses and downstream tests without treating the creative passage as evidence.

```text
AbductiveUnfoldingStructureBlock:
  unfoldingStructureRef: current AbductiveSearchUnfoldingStructure record
  abductivePromptRef:
  cueSetWithDownstreamPatternAlternativesRef:
  rivalHypothesisSetRef:
  hypothesisGenerationLoci[]:
  plausibilityConstraintRefs[]:
  evidenceReturnLoci[]:
  languageStateMoveRefs[]:
  poolPolicyOrSelectionRef?:
  blockedOverread: not inspiration event, not linear ideation workflow, not evidence by itself
```

Use `unfoldingStructureRef` for the current local structure record; use A.22.CGUS `specializedStructureRef?` only when the generic CGUS record must point to this narrower specialization. Use `cueSetWithDownstreamPatternAlternativesRef` when the prompt still carries several possible patterns for the next question. Use `rivalHypothesisSetRef` before selecting a prime hypothesis. Use `evidenceReturnLoci[]` to say where later evidence, deduction, probe design, or assurance work can return; do not use those loci as evidence. If the live claim becomes candidate retention, pool policy, selected-set result declaration, or comparison, apply `C.18`, `C.19`, `G.5`, or the pattern that defines the required comparison instead of making abduction a selector.

`AbductiveSearchUnfoldingStructure` is a local `A.22.CGUS` `U.Structure` specialization used for abductive search. It is not a root U-kind, ideation workflow, evidence, or selection decision. Use `B.5.2` to state the abductive prompt, cue set with alternative next patterns, rival hypotheses, plausibility constraints, and evidence-return loci. Use the patterns that define or test evidence, deduction, probe design, assurance, selected-set result declaration, pool policy, and comparison when those claims become current.

