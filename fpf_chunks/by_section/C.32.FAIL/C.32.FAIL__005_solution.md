---
chunk_kind: "child"
pattern_id: "C.32.FAIL"
pattern_title: "Architecture Failure Recognition and Repair"
section_id: "C.32.FAIL:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.FAIL/C.32.FAIL__005_solution.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "C.32.FAIL — Architecture Failure Recognition and Repair"
  - "C.32.FAIL:4 — Solution"
line_start: 60849
line_end: 60885
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.P"
  - "C.31"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.24.PUB"
  - "G.5"
keywords:
  - "architecture failure cue"
  - "architecture repair cue"
  - "candidate repair"
  - "repair-entry family"
  - "selected-structure relation"
  - "source overread"
  - "stressed architecture object"
---

### C.32.FAIL:4 - Solution

Convert the warning cue into an `ArchitectureRepairCue@Project`. Work in six steps:

1. State the symptom in ordinary practitioner language.
2. Name the described holon, bounded context, and architecture object under stress.
3. State the blocked overread that would lead the team astray.
4. Name the first governing pattern for the architecture object or lens relation.
5. Propose the smallest repair action that changes architecture handling.
6. State where to stop, or which neighboring pattern governs the next claim if another claim is already current.

Core repair families for first-draft use:

| Repair family | Symptom | Architecture object under stress | First repair action | Stop or receiving pattern |
|---|---|---|---|---|
| Weak module-interface | A source-side bearer is called a module because it has a convenient boundary. | Candidate module-interface relation and selected structure boundary. | Recover interface behavior, admissible-use boundary, change policy, and interface-conformance witness. | Stop at repaired interface cue; module-interface structure claims belong to `A.6.M`, `C.30.ASV`, or `C.31` when current. |
| False platform | A reusable-structure promise hides variation pressure and local exceptions. | Variation structure, substitution policy, evidence scope, and exception boundary. | Recover variation slots, substitution rules, substitution-conformance checks, and exception-growth trigger. | Cross-scope residual work belongs to `C.32.MLAO` when current. |
| Hidden single winner | A comparison or generation result is treated as selected architecture. | Candidate palette and retained alternatives. | Rebuild the C.32 palette with candidate gain, loss, preserved structure, hidden structure, and source-return condition. | Explicit comparison belongs to `A.19.CPM`, set-returning selection to `A.19.SelectorMechanism`, publication of a selected set to `G.5`, local choice to `C.11`, and project architecture decision to `C.32.PAD`. |
| Proxy result or description as authority | A score, graph, residual vector, generated output, architecture-description artifact, or MVPK publication face is used to accept or prefer an architecture candidate before the selected structure and receiving pattern are named. | Candidate architecture claim and selected-structure relation hidden behind the proxy, description, or visible result. | Recover the selected structure, source-side referent, view relation, or lens-output relation first. Use `C.29` for lens output, `C.30.ASV` or `C.30.AD` for view or description use, `A.19.CPM` for comparison, `C.11` for local choice, `A.19.SelectorMechanism` for set-returning selection, and `G.5` for publication of a selected set. | Stop when the visible work product only orients repair; evidence claims belong to `A.10` and assurance claims belong to `B.3`. |
| Coordination cost displaced by responsibility change | A team, work, or responsibility change improves local flow while pushing coordination into module interfaces, shared test, evidence, approval, or deployment structures. | Correspondence among role-enactor structure, work structure, coordination relation, module-interface structure, and evidence or deployment structure. | Recover the shifted coordination cost, then decide whether the repair belongs to `C.32.CONWAY`, `A.6.M`, `C.32.MLAO`, or a work and role pattern. | Role and work claims belong to the A.15 family; use architecture only for selected structures and architecture characteristics. |
| Temporal or control coupling | Named parts need brittle timing or control coordination. | Temporal relation, control relation, and affected work or evidence relation. | Recover the timing or control constraint and ask whether a candidate architecture change affects the selected structure. | Temporal adequacy claims belong to `C.27`, control or mechanism placement claims belong to the governing mechanism pattern, and flow-structure claims belong to `E.18` when current. |
| Evidence jump | The team asks for more evidence before naming the architecture repair. | Architecture object whose evidence relation may be stale, misplaced, or bearer-dependent. | Name the architecture repair first, then record the A.10 evidence relation, source-currentness relation, bearer, scope, and decision-use boundary. | Evidence relations belong to `A.10`, assurance to `B.3`, and gate or release claims to `A.20` or `A.21` when those patterns are current. |
| Generated output as authority | A generated architecture-looking output is treated as carrying an authority relation for architecture adequacy. | Source cue, generated description, candidate selected structure, and evaluation boundary. | Treat the output as a source cue; recover source-side referent, selected structure, architecture-change kind, gain, loss, and human review boundary. | Candidate generation belongs to `C.32`; generated-description use belongs to `C.30.AD`; publication-face use belongs to `E.17` or `E.24.PUB` when current. |
| Single-structure synthesis | One selected structure is improved and called the architecture synthesis. | Synthesis structure map and architecture characteristic bundle. | Return to C.32; name the other selected structures that must be coordinated and the architecture characteristics that make the trade-off real. | Stop at repaired C.32 palette, or open `C.32.MLAO` if the failure crosses scopes. |
| User function as architecture characteristic | A user-visible function is treated as the architecture quality being optimized. | Functional demand, architecture characteristic, and quality bundle boundary. | Recover the function through `A.6.F` or `C.30.ASV`; then name the architecture characteristic or `C.25` quality bundle separately. | Stop before comparison until function and characteristic occupy distinct fields. |
| Function with no feasible bearer | A function graph, workflow, use case, method step, or neural cell graph names a required function that no admitted bearer can perform under the current constraints. | Functional demand, candidate bearer set, module-interface relation, placement or deployment relation, resource access, control relation, and evidence burden. | Return to `C.32`; add or change bearer, split function, change placement or resource access, change control responsibility, reduce demand, or reject the candidate. | Stop before comparison, G.5 publication, assurance, or decision claims. |
| Static optimum | A front member or local winner is treated as durable optimum. | Evolution window, receiving pattern result, front or archive relation, and reopen trigger. | Add evolution window, source-return condition, and receiving pattern; keep C.18 and C.19 as retention or pool policy only. | Comparison belongs to `A.19.CPM`, set-returning selection to `A.19.SelectorMechanism`, local choice to `C.11`, publication of a selected set to `G.5`, and architecture decision to `C.32.PAD` when the decision claim is being made. |
| Ideality shortcut | Fewer bearers or fewer modules is treated as architecture improvement by itself. | Function-bearing allocation, selected structure count, and architecture characteristic bundle. | Recover the function-bearing transfer; name the removed or generalized bearer, the functions still carried, the new burden, and lost structure. | Return to `C.32`; use `C.31`, `A.6.F`, `A.6.M`, and `C.19.1` when their claims are current. |
| Universal bearer as adequacy shortcut | A universal module or general substrate is treated as architecture adequacy or scale adequacy by itself. | Scale-amenability claim, module-interface relation, evidence burden, control burden, and safety or admissibility boundary. | Treat universality as a candidate; require BLP scale window or waiver when scale advantage is claimed and record coupling, evidence, control, and source-return effects. | Stop before G.5 publication, assurance, release, or decision claims unless receiving patterns are current. |
| Transformer and transformed architecture mismatch | The architecture of a holon that changes another holon is collapsed with the changed holon's architecture, or the changed architecture is desired without a feasible changing holon. | Transformer-side selected structures, transformed-side selected structures, and the changing relation. | Open `C.32.CONWAY`; recover the changing relation through `A.3.4`, `E.18`, work, or method patterns; generate candidate repairs that change the transformer side, the transformed side, both sides, or a bounded mismatch. | Use `A.6.M` only for module-interface repair and `C.29` only when structural similarity is claimed. |

Admit a new repair family only when its row tells the practitioner what to repair first. A suspicious name alone is not enough; the row must name the architecture object under stress, the first repair action, and the stop or receiving pattern.

**Stop condition.** Stop after the repair action, receiving pattern, and source-return condition are named. Do not grow the cue into a risk register, evidence case, release argument, or final architecture choice.

**Lowering condition.** Keep the row as a C.32.FAIL repair cue only while the symptom, described holon, architecture object under stress, blocked overread, first governing pattern, repair action, stop condition, and escalation condition remain current. Lower the row to an observation when the architecture object is unknown, the repair action is missing, the first governing pattern is not named, or the symptom belongs only to evidence, assurance, release, description, publication, comparison, selection, choice, or decision work. Retire the cue when the repair action has been applied or the stressed architecture object is no longer current. Return to `A.6.P` or `E.10` when the case is only source-expression recovery, to `C.32` when candidate repair is current, to `C.32.MLAO` or `C.32.CONWAY` when their residual or correspondence repair is current, and to the named receiving pattern when a stronger downstream claim is current.

