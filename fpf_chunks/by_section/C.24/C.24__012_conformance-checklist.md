---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__012_conformance-checklist.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:7 — Conformance Checklist"
line_start: 52781
line_end: 52796
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.5"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.28"
  - "C.5"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.23"
  - "E.3"
  - "E.5"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
  - "U.WorkPlan"
keywords:
---

### C.24:7 - Conformance Checklist

1. **CC-ATC-1 - Declared separation.** `ATC.CallRouteDescription` is a `MethodDescription`; `ATC.CallPlan` is a `U.WorkPlan` that cites route descriptions; execution is `Work`; acceptance is via `U.PromiseContent`. No method-side route logic or actual burn is smuggled into the `U.WorkPlan` field set.
2. **CC-ATC-2 - Budgets on record.** Time budget, compute budget, cost ceiling, and risk limit exist ex ante; stop conditions are listed.
3. **CC-ATC-3 - E/E policy.** `EmitterPolicyRef` (or equivalent) and `explore_share` are editioned and logged.
4. **CC-ATC-4 - Assurance tuple.** Publish the typed claim `Plan admissible under K,S` with `<F,G,R>` and CL penalties traceable in the `CallGraph` SCR. Design-time and run-time never merged.
5. **CC-ATC-5 - BLP waiver discipline.** Any heuristic override against a general method includes expiry and re-evaluation date.
6. **CC-ATC-6 - Provenance minimum.** Record `{PromiseContentRef, CallPlanRef, MethodDesc.edition, EmitterPolicyRef, DescriptorMapRef? (if NQD), DistanceDefRef? (if NQD), TimeWindow, Seeds?, Dedup?}`.
7. **CC-ATC-7 - Notation independence.** No vendor tokens in conceptual text; bindings via Bridges or Profiles only.
8. **CC-ATC-8 - BLP tolerances declared.** `alpha/delta` tolerances are present in `ATC.Policy` or referenced via the active `E/E-LOG` profile.
9. **CC-ATC-9 - `CheckpointReturn` for bounded specialization.** When one route still uses scout/probe discipline on a new task family, it SHALL publish one `CheckpointReturn` with candidate routes, evidence, burned/residual actual budget, next action, and commit trigger; a successful probe alone never counts as committed rollout.
10. **CC-ATC-10 - Recoverable enactment closure.** When `C.24` returns one enactment-facing call plan or one `CheckpointReturn`, the `CallPlan` SHALL state current objective, route refs in order, planned budget envelope, stop or replan condition, and `nextPlannedAction`, while `CheckpointReturn` SHALL state burned/residual actual budget plus next action and commit trigger.
11. **CC-ATC-11 - Neighboring-pattern boundary.** If the question under repair is still fixed-option choice, pool policy over several live lines, or selector-facing publication, `C.24` SHALL apply `C.11`, `C.19`, or `G.5` rather than restating those patterns.
12. **CC-ATC-12 - Role discipline.** User-facing prose and emitted artifacts SHALL speak about systems in agential roles or equivalent typed performers, not one generic `agent` head, when that generic head would blur the holder kind.
13. **CC-ATC-13 - Causal action-use spec.** If one `CallPlan` selects observation, intervention, counterfactual-rung evidence collection, counterfactual policy conditioning, or off-policy causal evaluation for a causal purpose, it SHALL carry `CallPlan.causalActionUseSpec?` with `targetCausalityLadderRung`, `causalUseClaimKind: CausalUseClaimKind`, supported use, unsupported use, and a `C.28` causal-use support reference rather than letting call-planning vocabulary certify the causal claim.

