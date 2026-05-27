---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__002_problem-frame.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:1 — Problem frame"
line_start: 52297
line_end: 52322
dependencies:
  - "A.10"
  - "A.22"
  - "A.6.F"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "D.3"
  - "D.4"
  - "G.5"
  - "G.6"
keywords:
  - "cross-scope residual"
  - "declared scope"
  - "frustration"
  - "interlevel conflict"
  - "local repair"
  - "source return"
  - "structure kind"
---

### C.30.ILC:1 - Problem frame

Use this pattern when architecture work is triggered by statements such as:

```text
"Optimization at the component scope breaks the wider system."
"We added modularity, but integration exceptions grew."
"Local agent autonomy conflicts with the control or policy scope."
"At one scale window the architecture is stable; at the next, bespoke bridges appear."
"The team optimizes latency, but the evidence or assurance scope becomes unrepairable."
"We may need a declared system level, control layer, mediator, interface grammar, or work/evidence scope, but it is not clear which architecture move is admissible."
```

The first useful move is `CrossScopeArchitectureResidualTriage@Context`: name the affected declared scopes, structure kinds, residual carrier, local repair already attempted, why local repair is insufficient, and the first admissible architecture move or exact governing pattern application.

Entry condition: if declared scopes, at least one architecture structure kind, and one first admissible architecture move cannot be named in one sentence, keep the phrase as an ordinary source cue or `ProblemCard@Context`, not as `CrossScopeArchitectureResidualTriage@Context`.


What goes wrong if C.30.ILC is missed: a local improvement, control layer, scale label, interface grammar, or evidence reuse is treated as whole-architecture adequacy while the residual moves into another declared scope.

What C.30.ILC buys in practice: the practitioner can keep the useful conflict or frustration wording as a Plain source cue, recover the affected scopes and structure kinds, and stop at one admissible architecture move or exact governing pattern application.

`Interlevel conflict` and `frustration` may stay as ordinary source cues, but the conforming record recovers them through declared scopes, structure kinds, and residual carrier. The pattern does not create a generic level scale or `U.Frustration`. It asks which declared system level, aggregation scope, control layer, organizational scope, work/evidence scope, system/environment scope, scale window, interface grammar, allocation boundary, or source-return condition is carrying the residual.

Not this pattern when the live issue is stakeholder negotiation, ethics, measurement, scale/coarse-graining, candidate generation, final selection, causal outcome, evidence, assurance, or mathematical-lens validation. Use `D.3`/`D.4`, `C.16` or an admitted characteristic/measurement receiving pattern, `C.29` or an admitted scale/coarse-graining receiving pattern when that lens is live, `G.5` or an admitted candidate-generation receiving pattern, `C.11`, `C.28`, `A.10`/`B.3`/`G.6`, or `C.29` respectively.

