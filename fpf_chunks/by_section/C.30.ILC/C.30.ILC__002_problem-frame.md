---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__002_problem-frame.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:1 — Problem frame"
line_start: 78180
line_end: 78234
dependencies:
  - "A.10"
  - "A.22"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "D.3"
  - "D.4"
  - "G.5"
  - "G.6"
keywords:
  - "cross-scope residual"
  - "declared scope"
  - "first architecture move"
  - "frustration"
  - "interlevel conflict"
  - "local repair"
  - "residual-bearing locus"
  - "structure kind"
---

### C.30.ILC:1 - Problem frame

Use this pattern when a project situation contains a cross-scope architecture residual for a described holon, often described in project speech as:

```text
"Optimization at the component scope breaks the wider holon."
"We added modularity, but integration exceptions grew."
"Local agent autonomy conflicts with the control or policy scope."
"At one scale window the architecture is stable; at the next, bespoke bridges appear."
"The team optimizes latency, but the evidence or assurance scope becomes unrepairable."
"We may need to add, split, or mediate a declared holon level, declared scope, control layer, interface grammar, work scope, or evidence scope, but it is not clear which architecture move is admissible."
```

**First-minute use slice.** After an assembly team retunes its arm controllers, individual arms finish faster. The team also reports more cell stoppages and more audit exceptions. The engineer takes the assembly cell as the holon of interest and separates the two decisions.

- For the stoppages, compare the time required for an arm to acknowledge a request with the interval the cell controller allows. Use the active configuration and the recorded reason for a stop to distinguish a timeout from a shortage of material. To explain an increase across jobs, also check which jobs and operating conditions were compared.
- For the audit exceptions, compare the records the retuned controllers supply with the information the audit now requires. Changed audit criteria can produce more exceptions even if the controllers supply the same records.

A documented timing incompatibility rules out timely acknowledgement through that interface. If timely acknowledgement is required, the specified exchange cannot meet that requirement. Carry this finding into redesign when a different arrangement is commissioned. If timeout with a fallback is permitted, check whether that alternative meets the cell’s need. Evidence that the interface caused a particular stop warrants addressing that occurrence. The aggregate counts alone leave both diagnoses open. A mediator or changed control layer becomes a candidate when the diagnosed coupling calls for it. Use C.30.ASV when its structural view is needed.

The first result names the affected holon levels or scopes, the structure that carries them, the residual-bearing locus, any attempted local repair or reason for its insufficiency, and the first warranted architecture move. An adequate ordinary explanation can finish the question. `CrossScopeArchitectureResidualTriageRecord@Context` can organize the result when its fields help the receiving use.

The primary `EntityOfConcern` is the cross-scope or interlevel architecture residual in the described holon or holon family for a named architecture concern and intended use. The described holon may be an admitted system, organization-as-system, episteme, work occurrence, discipline, or another admitted holon kind. Publication-family material uses the episteme and publication patterns. A MethodDescription is an episteme; a Method uses `A.3.1` and the relations claimed for it.

A phrase in a description, a diagram label, or a mathematical-lens output may make the residual visible, but it is not the residual itself and does not become the center of this pattern.

`InterlevelConflict@Context` applies when two or more declared holon levels, declared scopes, or level-bearing structure relations of the same described holon or holon family impose incompatible or tensioned constraints, objectives, admissibility conditions, tempos, resource allocations, information-transfer relations, or assurance requirements.

Examples include declared system levels, declared episteme levels, aggregation scopes, typed control layers, declared organizational scopes, work scopes, evidence scopes, system scopes, environment scopes, description-use scopes, publication-use scopes, or other declared scopes.

A selected structure matters here only when it carries, separates, or relates the declared levels or scopes. A conflict between structures belongs in C.30.ILC only when those structures are assigned to different declared holon levels, declared scopes, scale windows, or coarse-graining steps; a conflict confined to the same level and scope, or one whose relevant assignment remains unknown, belongs elsewhere until that cross-level or cross-scope basis is recovered.

`FrustrationResidual` applies when a persistent cross-scope or interlevel residual remains after local repairs have been attempted or deemed insufficient: local optimization in one declared holon level or declared scope improves local fit while degrading, blocking, or destabilizing another declared holon level, declared scope, or level-bearing structure relation.

`ComplexityGrowthPressure` is admitted only as conditional architecture pressure: reducing an interlevel residual may require adding, splitting, mediating, or stabilizing a declared holon level, declared scope, aggregation scope, interface grammar, control loop, evidence scope, work-method scope, abstraction scope, source-return scope, or declared system level when that special case is being claimed. It is not a claim that complexity is good or that complexity necessarily grows.

**Entry condition.** For the described holon in context, name:

- declared holon levels or declared scopes;
- the selected structure or architecture structure kind that carries them;
- one residual-bearing locus;
- one first admissible architecture move or a supported `noArchitectureMove` result.

If any cannot be named, keep the issue at ordinary problem framing or `ProblemCard@Context`; do not claim `CrossScopeArchitectureResidualTriageRecord@Context` yet.

What goes wrong if C.30.ILC is missed: a local improvement, control layer, scale label, interface grammar, or evidence reuse is treated as whole-holon architecture adequacy while the residual moves into another declared holon level or declared scope.

What this buys: the practitioner can keep conflict or frustration language as an entry label while naming the residual-bearing locus, the affected declared holon levels or scopes, the selected structure that carries them, any local repair or reason for its insufficiency, and one first architecture move or sufficient `noArchitectureMove` result.

`Interlevel conflict` and `frustration` may appear in ordinary project descriptions, but the conforming record describes the residual through declared holon levels or declared scopes, the selected structure that carries them, and a residual-bearing locus. The pattern does not create a generic level scale or `U.Frustration`.

It asks which declared holon level, declared scope, aggregation scope, control layer, organizational scope, work scope, evidence scope, system scope, environment scope, scale window, interface grammar, allocation boundary, publication section, or source-return condition bears the residual. When a level concerns holon composition, identify the kind of whole involved, its constituents and the relation the residual depends on. A system, a body of knowledge or an occurrence of Work can each have relevant constituents. Comparing a service model with a less detailed model of the same service raises a different question. Which relevant distinctions does the second model still carry? Use B.5.MR if the comparison is one of refinement.

Use the subject pattern when the issue under repair is only ethical value framing, interlevel ethical conflict structure, ethical mediation or decision use, measurement, scale relation, coarse-graining relation, mathematical-lens validation, candidate generation, residual-reducing candidate-set work, final selection, causal outcome, evidence, or assurance. Use C.30.ILC only for the architecture residual-bearing locus.

