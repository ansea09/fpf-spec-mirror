---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__016_relations.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:12 — Relations"
line_start: 51538
line_end: 51550
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.19.1"
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
---

### C.24:12 - Relations

- `A.3.1` supplies admitted Method identity; `C.11` supplies the fixed choice consumed through `upstreamChoiceResultRef`.
- `C.18` supplies generated candidate or front material, and `C.19` supplies `PoolPolicyResult` or `EmitterPolicy` only when live-pool treatment still constrains the plan. Neither admits a Method.
- `C.19.1` supplies the scale-claim probe, any selected comparison or Scale-Audit result, and any separate local policy or `BLP-waiver`; C.24 invents none of them.
- `A.15`, `A.15.1`, `A.15.2`, `A.2.1`, and `F.6` keep Method, description, plan, Work, performer, and attribution distinct.
- `G.6` supplies the trace representation cited by `ATC.CallGraphRef`.
- `B.3` supplies one bounded assurance result only when a named assurance use is current.
- `C.28` supplies causal-use support when the plan is used for causal evidence, intervention, policy, fairness, or counterfactual work.
- `C.27` evaluates temporal claims about speed, narrowing, recovery, or stop/replan rate. More calls or faster narrowing is not success by itself.
- `E.23` may use C.24 plans and checkpoints inside improvement Work; C.24 does not restate the improvement loop.
- `E.10.MOVE`, `E.11.PUR`, and `A.15.5` recover project moves, pattern-use recommendations, and work-entry readiness when those questions are not plan-local.

