---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__002_problem-frame.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:1 — Problem frame"
line_start: 59513
line_end: 59549
dependencies:
  - "A.10"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.TFS-REL"
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

**First-minute use slice.** A robotics team says a local controller upgrade made each arm faster, but cell-level stoppages and audit exceptions grew. Before drawing another architecture view, C.30.ILC records: described holon = assembly cell; declared levels and scopes = arm controller, cell control, evidence scope; level-bearing selected structure = control and evidence-reuse structure; residual-bearing locus = control-rate conflict plus evidence-reuse failure; local repair already attempted = retuned each arm controller; first architecture move = add or change mediator relation or control-layer relation and apply `C.30.ASV` for the selected structural view.

The first useful move is `CrossScopeArchitectureResidualTriageRecord@Context`: name the affected declared holon levels or declared scopes, the selected structure in which those levels or scopes are recoverable, residual-bearing locus, local repair already attempted, why local repair is insufficient, and the first admissible architecture move or subject-pattern application.

The primary `EntityOfConcern` is the cross-scope or interlevel architecture residual in the described holon or holon family for a named architecture concern and intended use. The described holon may be an admitted system, organization-as-system, episteme, work occurrence, discipline, or another admitted holon kind. Publication-family material uses the episteme and publication patterns. A MethodDescription is an episteme; a Method uses `A.3.1` and the relations claimed for it. A phrase in a description, a diagram label, or a mathematical-lens output may make the residual visible, but it is not the residual itself and does not become the center of this pattern.

`InterlevelConflict@Context` applies when two or more declared holon levels, declared scopes, or level-bearing structure relations of the same described holon or holon family impose incompatible or tensioned constraints, objectives, admissibility conditions, tempos, resource allocations, information-transfer relations, or assurance requirements. Examples include declared system levels, declared episteme levels, aggregation scopes, typed control layers, declared organizational scopes, work scopes, evidence scopes, system scopes, environment scopes, description-use scopes, publication-use scopes, or other declared scopes. A selected structure matters here only when it carries, separates, or relates the declared levels or scopes. A conflict between structures belongs in C.30.ILC only when those structures are assigned to different declared holon levels, declared scopes, scale windows, or coarse-graining steps; a same-level, same-scope, or unassigned conflict between structures belongs elsewhere until a level, scope, scale-window, or coarse-graining assignment is recovered.

`FrustrationResidual` applies when a persistent cross-scope or interlevel residual remains after local repairs have been attempted or deemed insufficient: local optimization in one declared holon level or declared scope improves local fit while degrading, blocking, or destabilizing another declared holon level, declared scope, or level-bearing structure relation.

`ComplexityGrowthPressure` is admitted only as conditional architecture pressure: reducing an interlevel residual may require adding, splitting, mediating, or stabilizing a declared holon level, declared scope, aggregation scope, interface grammar, control loop, evidence scope, work-method scope, abstraction scope, source-return scope, or declared system level when that special case is being claimed. It is not a claim that complexity is good or that complexity necessarily grows.

Entry condition: if declared holon levels or declared scopes, the selected structure or architecture structure kind that carries them, one residual-bearing locus, and one first admissible architecture move cannot be named for the described holon in context, keep the issue at ordinary problem framing or `ProblemCard@Context`; do not claim `CrossScopeArchitectureResidualTriageRecord@Context` yet.

What goes wrong if C.30.ILC is missed: a local improvement, control layer, scale label, interface grammar, or evidence reuse is treated as whole-holon architecture adequacy while the residual moves into another declared holon level or declared scope.

What this buys: the practitioner can name the residual-bearing locus, the declared levels or scopes, the local repair already attempted, and one first architecture move without turning multilevel frustration, scale, ethics, evidence, or mathematical-lens use into this pattern's object.

What C.30.ILC buys in practice: the practitioner can keep useful conflict or frustration language as an entry label while governing the architecture residual itself: affected holon levels or scopes, the selected structure that carries them, residual-bearing locus, and one admissible architecture move or subject-pattern application.

`Interlevel conflict` and `frustration` may appear in ordinary project descriptions, but the conforming record governs the residual through declared holon levels or declared scopes, the selected structure that carries them, and a residual-bearing locus. The pattern does not create a generic level scale or `U.Frustration`. It asks which declared holon level, declared scope, aggregation scope, control layer, organizational scope, work scope, evidence scope, system scope, environment scope, scale window, interface grammar, allocation boundary, publication section, or source-return condition bears the residual. A system level or episteme level is a special case of a declared holon level.

Not this pattern when the issue under repair is only ethical value framing, interlevel ethical conflict structure, ethical mediation or decision use, measurement, scale relation, coarse-graining relation, mathematical-lens validation, candidate generation, residual-reducing candidate-set work, final selection, causal outcome, evidence, or assurance. Use the subject pattern and keep C.30.ILC only to the architecture residual-bearing locus.

