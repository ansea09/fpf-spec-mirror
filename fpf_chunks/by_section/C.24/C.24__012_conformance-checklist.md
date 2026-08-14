---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__012_conformance-checklist.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:7 — Conformance Checklist"
line_start: 53250
line_end: 53265
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
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

1. **CC-ATC-1 - Declared separation.** Every planned call step selects an exact independently admitted `U.Method`; `ATC.CallRouteDescription` is a separate `U.MethodDescription` episteme; `ATC.CallPlan` is a `U.WorkPlan`; each execution is exact dated `U.Work` with actual `enactsMethod`; acceptance is via separate `U.PromiseContent`. No description, service promise, CallGraph row, method-side route logic, or actual burn is smuggled into another object.
2. **CC-ATC-2 - Budgets on record.** Time budget, compute budget, cost ceiling, and risk limit exist ex ante; stop conditions are listed.
3. **CC-ATC-3 - E/E policy.** `EmitterPolicyRef` (or equivalent) and `explore_share` are editioned and logged.
4. **CC-ATC-4 - Assurance tuple.** State the typed claim `Plan admissible under K,S` with `<F,G,R>` and CL penalties traceable in the `CallGraph` SCR. Design-time and run-time never merged.
5. **CC-ATC-5 - BLP waiver discipline.** Any heuristic override against a general method includes expiry and re-evaluation date.
6. **CC-ATC-6 - Provenance minimum.** Every actual call record includes `{WorkRef, MethodDescriptionRef? and edition when cited, PromiseContentRef?, CallPlanRef, EmitterPolicyRef, budget deltas, DescriptorMapRef? (if NQD), DistanceDefRef? (if NQD), Seeds?, Dedup?}`. `WorkRef` names the independently identified `U.Work` occurrence. Its Method, interval, containing System, and every performer's assignment species, obtaining occurrence, and F.6 relation remain recoverable under A.15.1, A.2.1, and F.6. Each ref resolves its direct object; the record creates none of them.
7. **CC-ATC-7 - Notation independence.** No vendor tokens in conceptual text; bindings via Bridges or Profiles only.
8. **CC-ATC-8 - BLP tolerances declared.** `alpha/delta` tolerances are present in `ATC.Policy` or referenced via the active `E/E-LOG` profile.
9. **CC-ATC-9 - `CheckpointReturn` for bounded specialization.** When one route still uses scout or probe discipline on a new task family, it SHALL emit one `CheckpointReturn` with candidate routes, evidence, actual budget spent and remaining, next action, and commit trigger; a successful probe alone never counts as committed rollout.
10. **CC-ATC-10 - Recoverable enactment closure.** When `C.24` returns one enactment-facing call plan or one `CheckpointReturn`, the `CallPlan` SHALL state current objective, ordered exact Method refs, separate route-description refs when current, planned budget envelope, stop or replan condition, and `nextPlannedAction`, while `CheckpointReturn` SHALL state actual budget spent and remaining plus next action and commit trigger.
11. **CC-ATC-11 - Neighboring-pattern boundary.** If the question under repair is still fixed-option choice, pool policy over several live lines, selector-facing result declaration, or publication availability, `C.24` SHALL apply `C.11`, `C.19`, or `G.5` as appropriate; when publication is current, it SHALL apply `E.17` for the face and source return and `E.24.PUB` for the publication occurrence and availability. It SHALL NOT restate those patterns.
12. **CC-ATC-12 - Performer discipline.** User-facing prose and emitted artifacts SHALL identify every admitted System that actually performs planning, revision, call, or observation Work, name the corresponding `U.Work` occurrences, and keep all facts required by A.15.1, A.2.1, and F.6 recoverable. A local system-role kind and a separate System-classification judgment are optional only when independently current. A label, kind, classification judgment, assignment species, or assignment occurrence does not perform the Work.
13. **CC-ATC-13 - Causal action-use spec.** If one `CallPlan` selects observation, intervention, counterfactual-rung evidence collection, counterfactual policy conditioning, or off-policy causal evaluation for a causal purpose, it SHALL carry `CallPlan.causalActionUseSpec?` with `targetCausalityLadderRung`, `causalUseClaimKind: CausalUseClaimKind`, supported use, unsupported use, and a `C.28` causal-use support reference rather than letting call-planning vocabulary certify the causal claim.

