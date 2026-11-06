---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Generate and Compare Candidate Explanations (Abductive Loop)"
section_id: "B.5.2:4"
section_title: "Solution - Structured abductive micro-cycle"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__005_solution-structured-abductive-micro-cycle.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "B.5.2 — Generate and Compare Candidate Explanations (Abductive Loop)"
  - "B.5.2:4 — Solution - Structured abductive micro-cycle"
line_start: 49633
line_end: 49690
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
  - "C.28.CM"
keywords:
---

### B.5.2:4 - Solution - Structured abductive micro-cycle

`B.5.2` begins from an account that meets `B.5.2.0`'s `U.AbductivePrompt` entry conditions, develops candidate explanations and compares them under explicit plausibility criteria. Return a qualified conjecture when the grounds support it, or an abort, defer or split outcome under §14.2. Preserve the prompt, candidates considered, supports, limitations and allowed downstream use. Abduction alone assigns no `AssuranceLevel`.

#### B.5.2:4.1 - Nature of abduction in FPF

Abduction develops candidate explanations, models or conjectures for a declared explanatory prompt and compares their plausibility. Prefer a candidate only to the extent that the comparison warrants that preference. A conjecture's plausibility may justify keeping or using it for a bounded purpose; it does not establish its causal mechanism or a stronger empirical claim. Deduction, evidence synthesis and action choice keep their own questions.

#### B.5.2:4.2 - Four-step micro-cycle

| Step | Core activity | Required publication outcome |
|---|---|---|
| **1. Frame the prompt** | State the initiating explanatory question precisely enough that the unexplained contrast, opportunity, or probe pressure is explicit. | A prompt account with its open question, species, scope and motivating grounds under `B.5.2.0`; reuse an adequate existing account. |
| **2. Generate candidate hypotheses** | Develop candidates that could explain the prompt and look for serious rivals. | The candidates actually considered, including any limit from not identifying a serious rival. |
| **3. Apply plausibility filters** | Compare candidates against explicit plausibility criteria. | A short rationale stating why each considered candidate remains live, is deferred or is rejected, and what comparison those grounds support. |
| **4. Return the supported result** | Select a conjecture when the comparison warrants it; otherwise return the applicable outcome in §14.2. | A hypothesis-bearing `U.Episteme` with its prompt, selection rationale, any live rivals, supports, fragilities and allowed use when a conjecture is selected; otherwise the justified abort, defer or split outcome. |

The loop is intentionally iterable. A selected prime hypothesis may later be replaced, narrowed, or reopened if deduction, probe work, or evidence reveals a better rival.

#### B.5.2:4.3 - Entry discipline via `U.AbductivePrompt`

`AnomalyStatement` remains a canonical prompt species, but it is not the only one. `B.5.2` also accepts the broader prompt species governed by `B.5.2.0`, such as `ProblemCuePrompt`, `OpportunityCuePrompt`, and `ProbeCuePrompt`.

#### B.5.2:4.4 - Plausibility filters

The filtering step is local and context-sensitive, but the criteria used **SHALL** be explicit. Typical filters include:

- **Parsimony.** Does the candidate introduce only the additional structure that the prompt requires?
- **Explanatory reach.** How much of the prompt does the candidate actually account for?
- **Consistency with established constraints.** Does the candidate avoid collision with already trusted pillars, mechanisms, or scope declarations?
- **Falsifiability / probeability.** What implication, deduction or possible observation could discriminate the candidate from its rivals? Keep that question separate from whether a check is obtainable and worth performing now.
- **Scope fit.** Is the candidate framed for the declared prompt scope rather than for an inflated or shifted target?

Select the filters needed to judge explanatory adequacy and preference for this prompt and intended use. Make their grounds, any decisive comparison and unresolved trade-offs explicit.

When a causal hypothesis cannot yet yield a discriminating implication because its mechanisms and rival accounts are unspecified, use C.28.CM to construct comparable causal models. Return their conditional consequences and unresolved premises to these plausibility filters. A useful hypothesis whose present question is already answered needs no additional model merely to remain a candidate.

#### B.5.2:4.5 - Abductive Unfolding Structure Block

When the question concerns possible continuations of abductive work and their conditions, use A.22.CGUS's ordinary branch. Open its formal branch only when the receiving use depends on the unfolding organization's CGUS identity or membership; reuse of a hypothesis note alone does not require that branch.

```text
AbductiveUnfoldingStructureBlock:
  unfoldingStructureRef: one independently identified A.22.CGUS structure
  abductivePromptRef:
  cueSetWithDownstreamPatternAlternativesRef:
  rivalHypothesisSetRef:
  hypothesisGenerationLoci[]:
  plausibilityConstraintRefs[]:
  evidenceReturnLoci[]:
  languageStateMoveRefs[]:
  poolPolicyOrSelectionRef?:
```

Use `unfoldingStructureRef` to designate the selected structure. Recover its constituents, obtaining relation occurrences, applied constraints and selection-use frame under A.22; qualify its loci and potential continuations under A.22.CGUS. Keep the describing record separate from that identity. Use `cueSetWithDownstreamPatternAlternativesRef` when the prompt still carries several possible patterns for the next question. Use `rivalHypothesisSetRef` for the candidates actually compared and preserve the comparison limit when no serious rival was identified. Use `evidenceReturnLoci[]` to say where later evidence, deduction, probe design, or assurance work can return; do not use those loci as evidence. Abductive plausibility comparison remains here. Use C.18 for archive or front claims, C.19 for live-pool policy, G.5 for a selector's selected-set declaration, or the direct comparison method when that distinct result is needed.

`AbductiveSearchUnfoldingStructure` is a local designation for an A.22.CGUS structure selected for an abductive-search question; it supplies no additional identity rule.

