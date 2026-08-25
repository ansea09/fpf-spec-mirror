---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
section_id: "A.2.5:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__015_sota-echoing.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.2.5 — SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
  - "A.2.5:12 — SoTA-Echoing"
line_start: 4984
line_end: 4996
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.21"
  - "A.6.5"
  - "A.6.REL"
  - "C.3"
keywords:
  - "Work admission"
  - "assignment-state predicate"
  - "assignment-state relation"
  - "evidence boundary"
  - "state condition"
  - "time window"
---

### A.2.5:12 - SoTA-Echoing

| Current or mature line | What it contributes | Concrete mutation in A.2.5 |
|---|---|---|
| [W3C SCXML 1.0](https://www.w3.org/TR/scxml/), a mature 2015 Recommendation rather than current competitive SoTA | Explicit states, parallel regions, guarded transitions, events, and executable state-machine semantics. | Keep statecharts available when the subject-domain model needs them, but type them as mathematical or description lenses rather than the world-side relation occurrence or universal Method order. |
| Esparza and Fischer, [Runtime Verification for LTL in Stochastic Systems](https://arxiv.org/abs/2508.07963), 2025 | Runtime monitoring distinguishes true, false, and inconclusive results; finite observations do not settle every temporal property. | Treat incomplete evidence as unresolved for the relying use, preserve the predicate's temporal reading, and do not close an occurrence merely because a finite evidence path is silent. |
| [Cedar Policy Language current reference](https://docs.cedarpolicy.com/policies/syntax-policy.html) | Fine-grained decisions evaluate a concrete principal, action, resource, current attributes, and request-time conditions rather than a system-role label alone. | Require the system performing consumer decision Work to combine current assignment, exact predicate, state window, and action-specific relations. Keep this as an implementable software specialization rather than the ontology of every assignment state. |
| Zuvic, [Capability Gates Are Not Authorization](https://arxiv.org/abs/2606.28679), 2026 preprint | A current agent-framework audit distinguishes exposed capability from per-call, value-sensitive authorization and reports fail-closed enforcement experiments. | Keep capability in A.2.2 and require the consumer to evaluate the concrete state and action claim before side effects; do not infer authorization from tool exposure. The empirical scope remains the audited software frameworks. |
| Liu et al., [A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469), 2026 preprint | Task alignment, action alignment, source authorization, and data isolation require runtime checks over the current task and action. | In agentic cases, require the consumer's governing claim to name the current task and action relations; A.2.5 supplies only the exact state relation and assertion form, while A.10 supplies only the evidence-use relation; the applicable evaluation or assurance pattern separately establishes any reliance posture. |
| `A.6.REL`, `A.2.1`, `A.19`, `A.2.4`, and `A.10` | FPF already separates relation obtaining, occurrence identity, assignment episodes, characteristic-space predicates, assertions, and evidence use. | Give A.2.5 an occurrence identity rule, preserve the lightweight assertion path, and keep evidence outside generic state identity. |

These sources do not turn A.2.5 into an IT access-control pattern. Their transferable contribution is narrower: current action decisions need exact participants and predicates; temporal monitoring can remain unresolved; capability and action admission differ; and state-machine notation is optional modeling machinery.

