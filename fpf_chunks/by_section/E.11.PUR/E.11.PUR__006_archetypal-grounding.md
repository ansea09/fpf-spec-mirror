---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__006_archetypal-grounding.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:5 — Archetypal Grounding"
line_start: 74831
line_end: 74870
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
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

A team considering a high-cost pump test has candidate uses of `C.28` causal triage and `A.21` gate discipline. Both may be applicable. The immediate uncertainty is whether a causal model output may support intervention, so `C.28` offers the more useful first result.

Recommend `C.28` without claiming that the test is authorized. The later gate use remains a separate candidate whose applicability can be reconsidered after the causal-use result exists.

Because this local recommendation is reversible and no later use relies on five separate findings, the team records `recommendationSupportProfile=ordinaryCompact`, the applicability result, and one compact rationale over all five aspects. If a later gate review needs to replay each aspect independently, that review may create current fit findings and a current applicability finding from the then-current basis. It does not claim that those addressable findings existed when the earlier compact recommendation was made; the original compact rationale remains its historical basis.

#### E.11.PUR:5.2 - Unordered complementary uses

A clinical team needs both a terminology repair and an evidence-basis review before revising a protocol. Neither result is a prerequisite for the other in the current context.

Use one coordination relation with `orderingMode=unordered`. The team may perform the uses in either order or in parallel. Their coexistence does not create a lifecycle or WorkPlan.

#### E.11.PUR:5.3 - Result-based precedence

A design team's architecture-candidate comparison begins only after its evaluation coordinates are defined. One candidate use of `A.19.ECS` expects an `EvaluationCharacteristicSpaceSpec`; the dependent comparison use consumes that exact result.

Use `precedenceBasis=prerequisiteResult` and point to the ECS candidate's existing expectation. Do not copy `EvaluationCharacteristicSpaceSpec` and its signature into new ordering fields. After the result is grounded, the dependent use can begin under its own Solution.

#### E.11.PUR:5.4 - Method precondition is not a result dependency

A machining pattern assumes an admitted material-kind classification. The classification is a method precondition already current in the bounded context, not the result of another candidate pattern use.

If coordination is still useful, use `methodPrecondition` and leave the result-expectation position absent. Do not invent a prerequisite result merely to make the relation look uniform.

#### E.11.PUR:5.5 - Repair a stale copied prerequisite locally

An older architecture coordination copied `EvaluationCharacteristicSpaceSpec` and its signature into an ordering record. The ECS candidate's current expectation later changed, leaving the copy stale while both candidates, their applicability findings, the coordination question, and `partialOrder` mode remained sound.

Repair only the ordering relation: remove the copied result description, set `precedenceBasis=prerequisiteResult`, and reference the ECS candidate's current expectation. The dependent use returns until that expected result is grounded. Candidate inspection, applicability, coordination membership, and direct Solutions do not restart.

#### E.11.PUR:5.6 - A higher recommendation score can reduce useful fit

An assistant ranks candidate pattern uses by historical recommendation acceptance. The familiar `A.21` gate candidate receives a higher score and is recommended first more often for causal-use uncertainty. Recommendation acceptance rises, but wrong-turn returns also rise because the needed `C.28` causal-use result is still absent.

The score improved while first-result fit and receiving-use value worsened. Keep the historical score as telemetry, apply `E.13` to the substitution, and base recommendation on current applicability, expected result, receiving use, and live alternatives. A higher score is not another fit finding.

