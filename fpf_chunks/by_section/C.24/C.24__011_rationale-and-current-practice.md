---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
section_id: "C.24:10"
section_title: "Rationale and current practice"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__011_rationale-and-current-practice.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.24 — Plan Tool or Service Calls for a Fixed Action (C.Agent-Tools-CAL)"
  - "C.24:10 — Rationale and current practice"
line_start: 64114
line_end: 64128
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.7"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.2.1"
  - "C.28"
  - "C.5"
  - "E.17"
  - "E.23"
  - "E.24.PUB"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
keywords:
  - "agentic tool-use"
  - "call planning"
  - "route probe"
  - "service calls"
---

### C.24:10 - Rationale and current practice

**Qualification window.** This comparison uses the source set as of 2026-08-21. Reopen it when a later result changes the relative value of explicit planning, route grounding, active information gathering, checkpoint use and replanning, multidimensional evaluation, or long-horizon budget and dependency handling for the declared use.

| Contribution | Adopted, adapted, or rejected move | Boundary and trade-off |
| --- | --- | --- |
| ToolPlanner, EMNLP 2024, [ToolPlanner: A Tool Augmented LLM for Multi Granularity Instructions with Path Planning and Feedback](https://aclanthology.org/2024.emnlp-main.1018/) | **Adopt:** keep path planning, feedback, and replanning explicit instead of hiding them inside one call loop. | The gain is replayable route revision; the cost is a plan object. The LLM benchmark does not define universal FPF objects. |
| PlanningArena, ACL 2025, [PlanningArena: A Modular Benchmark for Multidimensional Evaluation of Planning and Tool Learning](https://aclanthology.org/2025.acl-long.1499/) | **Adapt:** check tool selection, reasoning, user-input interpretation, and execution-relevant constraints separately instead of treating one aggregate score as plan quality. | Its scenarios do not set universal weights or safety limits. C.24 keeps only the dimensions that change this plan or checkpoint. |
| IBM Research, ECAI 2025, [From Grounding to Planning: Benchmarking Bottlenecks in Web Agents](https://research.ibm.com/publications/from-grounding-to-planning-benchmarking-bottlenecks-in-web-agents) | **Retain with a rejected overread:** keep route grounding distinct from plan quality, but reject the claim that planning is always the dominant bottleneck. | This preserves a cheap diagnostic split without hard-coding a web-agent bottleneck order. |
| Aghzal et al., 2026 preprint, [Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective](https://arxiv.org/abs/2603.14248) | **Adopt:** separate high-level planning, low-level execution, and replanning; a sound plan does not excuse failed grounding or adaptive control. | The result makes the IBM split conditional. It does not make every web-agent layer mandatory in a known fixed route. |
| DeepPlanning, ACL 2026, [DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints](https://aclanthology.org/2026.acl-long.335/) | **Adapt:** retain global budgets, dependencies, or safe parallelism when material, and use the bounded scout and checkpoint cycle for information needed before commitment. | Long-horizon benchmarks expose degradation and efficiency trade-offs, but their task schemas do not belong in every ordinary call plan. |
| `C.19.1` current scale-comparison sources and method | **Adopt conditionally:** use Bitter-Lesson pressure only with the actual probe and a named bearer, scale window, evidence, cost, safety, and uncertainty. | Generality is not a winner by label; local policy and waiver stay separate from empirical comparison. |

These contributions distinguish route grounding, plan quality, execution and replanning. Keep only fields that change the route, stop, reliance or replay. Reconsider the plan when new knowledge changes one of those decisions; another benchmark alone need not change an adequate plan.

