---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__006_archetypal-grounding.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:5 — Archetypal Grounding"
line_start: 80373
line_end: 80418
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
  - "C.22.PFR"
  - "C.24"
  - "C.30"
  - "E.10.MOVE"
  - "E.11"
  - "E.11.PUA"
  - "E.18"
  - "E.18.1"
  - "G.11"
keywords:
---

### E.11.PUR:5 - Archetypal Grounding

#### E.11.PUR:5.1 - Applicable but not recommended

A team considering a high-cost pump test has candidate uses of `C.28` causal triage and `A.21` gate discipline. Both may be applicable. The immediate uncertainty is whether a causal model output may support intervention, so `C.28` offers the more useful first result. That uncertainty and the recommendation are epistemic; neither asserts an actual C.22.PFR Problem.

Recommend `C.28` without claiming that the test is authorized. The later gate use remains a separate candidate whose applicability can be reconsidered after the causal-use result exists.

Because this local recommendation is reversible and no named later use relies on it, the team states the applicability result and one compact rationale over all five aspects in the working conversation; it materializes no recommendation episteme or support profile. If a later gate review needs to replay each aspect independently, that review may create current fit findings and a current applicability finding from the then-current basis. It does not backdate those addressable findings; if the original readable rationale was retained, it remains the earlier recommendation's historical basis.

#### E.11.PUR:5.1.1 - An earlier result still answers the concern

The same team already has a C.28 causal-use result for the same pump model, intervention question, declared use, sources, assumptions, and qualification window. The team uses C.28 to compare that result episteme and edition with the present concern. Every comparison value still matches, so the team cites the result and stops instead of performing the C.28 use again.

If the team uses the result as a premise in a project discussion and the source-to-use account is still implicit, it uses A.10 to make the source → result → claim connection explicit for that bounded use. If the later gate Work relies on that result, its A.10 evidence-provenance path names the result and bounded use. If new operating conditions change the causal-use assumptions or qualification window, the team reopens that affected C.28 question rather than treating the old result as current or restarting every coordinated pattern use.

#### E.11.PUR:5.2 - Unordered complementary uses

A clinical team needs both a terminology repair and an evidence-basis review before revising a protocol. Neither result is a prerequisite for the other in the current context.

State an unordered coordination: the team may use either pattern first or use them in parallel. No coordination episteme or ordering relation is required for that local judgement. If the later protocol revision becomes a named reliance that needs the coordination replayable, materialize one `PatternUseCoordination@Context` with `orderingMode=unordered` and no ordering relations. Their coexistence does not create a lifecycle or WorkPlan.

#### E.11.PUR:5.3 - Result-based precedence

A design team's architecture-candidate comparison begins only after its evaluation coordinates are defined. One candidate use of `A.19.ECS` expects an `EvaluationCharacteristicSpaceSpec`; the dependent comparison use consumes that exact result.

Use `precedenceBasis=prerequisiteResult`, point to the ECS candidate's existing expectation, and cite its current E.11.PUA result-closure finding. The closure must identify the exact `EvaluationCharacteristicSpaceSpec`, its defining or constraining `ClaimGraph` and pattern locator, the evaluation or Method use relative to which it is this result, and the direct relation, A.6.1 binding, or local-claim basis with its exact predicate. Do not copy the spec or its signature into ordering fields. Until that basis is current, no precedence occurrence is established and the dependent use stays at its return boundary.

#### E.11.PUR:5.4 - Method precondition is not a result dependency

A machining pattern assumes an admitted material-kind classification. The classification is a method precondition already current for that exact machining use, not the result of another candidate pattern use.

If coordination is still useful, use `methodPrecondition` and leave both result-reference positions absent. Do not invent a prerequisite result merely to make the relation look uniform.

#### E.11.PUR:5.5 - Repair a stale copied prerequisite locally

An older architecture coordination copied `EvaluationCharacteristicSpaceSpec` and its signature into an ordering record. The ECS candidate's current expectation later changed, leaving the copy stale while both candidates, their applicability findings, the coordination question, and `partialOrder` mode remained sound.

Repair only the ordering relation: remove the copied result description, set `precedenceBasis=prerequisiteResult`, and reference the ECS candidate's current expectation and current E.11.PUA result-closure finding. If the exact result, relative object, direct basis, predicate, or defining `ClaimGraph` cannot be recovered, keep the precedence relation non-obtaining and the dependent use at its return boundary. Candidate inspection, applicability, coordination membership, and direct `Solution` content do not restart.

#### E.11.PUR:5.6 - A higher recommendation score can reduce useful fit

An assistant ranks candidate pattern uses by historical recommendation acceptance. The familiar `A.21` gate candidate receives a higher score and is recommended first more often for causal-use uncertainty. Recommendation acceptance rises, but wrong-turn returns also rise because the needed `C.28` causal-use result is still absent.

The score improved while first-result fit and receiving-use value worsened. Keep the historical score as telemetry, apply `E.13` to the substitution, and base the recommendation on current applicability, expected result, any current receiving use, and the other candidates still under consideration. A higher score is not another fit finding.

