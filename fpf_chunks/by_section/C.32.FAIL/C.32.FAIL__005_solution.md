---
chunk_kind: "child"
pattern_id: "C.32.FAIL"
pattern_title: "Architecture Failure Recognition and Repair"
section_id: "C.32.FAIL:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.FAIL/C.32.FAIL__005_solution.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.32.FAIL — Architecture Failure Recognition and Repair"
  - "C.32.FAIL:4 — Solution"
line_start: 78866
line_end: 78902
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.27"
  - "C.29"
  - "C.3"
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
  - "E.10.ROLE"
  - "E.17"
  - "E.18"
  - "E.18.NET"
  - "E.24.PUB"
  - "F.6"
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

Develop the first repair action from the warning cue. The following six moves guide that work:

1. State the symptom in ordinary practitioner language.
2. Name the affected architecture object, described holon, concern and intended repair use. Preserve available observations and unresolved questions; add an architecture claim, scope or qualification window when material.
3. If a mistaken inference explains the failure, state it and the distinction needed to correct it.
4. Use the subject pattern for the architecture object or lens relation when its definition or test is needed; cite it when the next user needs that route.
5. Propose the smallest action that can resolve the architecture difficulty. If a consequential premise is unknown, first recover the observation or subject result that can settle it.
6. State where to stop, or which neighboring pattern defines or constrains the next claim if another claim is already current.

Core repair families for a first repair-cue draft:

| Repair family | Symptom | Architecture object under stress | First repair action | Stop or pattern for the next question |
|---|---|---|---|---|
| Weak module-interface | A source-side bearer is called a module because it has a convenient boundary. | Candidate module-interface relation and selected structure boundary. | Recover interface behavior, admissible-use boundary, change policy, and interface-conformance witness. | Stop at repaired interface cue; module-interface structure claims belong to `A.6.M`, `C.30.ASV`, or `C.31` when current. |
| False platform | A reusable-structure promise hides variation pressure and local exceptions. | Variation structure, substitution policy, evidence scope, and exception boundary. | Recover variation slots, substitution rules, substitution-conformance checks, and exception-growth trigger. | Cross-scope residual work belongs to `C.32.MLAO` when current. |
| Hidden single winner | A comparison or generation result is treated as selected architecture. | Candidate palette and retained alternatives. | Recover the C.32 alternatives, expected gains and losses, including source-return conditions when needed. Reuse an adequate palette; develop missing alternatives when they can change the choice. | State explicit comparison under the A.19.CPM predicate, set-returning selection under A.19.SelectorMechanism, selected-set result declaration under G.5, local choice under C.11, and a project architecture decision under C.32.PAD. For publication, state the E.24.PUB occurrence and audience availability, with E.17 source-backed face and source return when needed. |
| Proxy result or description as authority | A score, graph, residual vector, generated output, architecture-description artifact, or MVPK publication face is used to accept or prefer an architecture candidate before the selected structure and pattern for the next question are named. | Candidate architecture claim and selected-structure relation hidden behind the proxy, description, or visible result. | Recover the selected structure, source-side referent, view relation, or lens-output relation first. Use `C.29` for mathematical-lens output, `C.30.ASV` or `C.30.AD` for view or description use, `A.19.CPM` for comparison, `C.11` for local choice, `A.19.SelectorMechanism` for set-returning selection, and `G.5` for selected-set result declaration. For publication, use `E.24.PUB` for the occurrence and audience availability; add `E.17` when a source-backed face and source return are needed. | Stop when the visible work product only orients repair; evidence claims belong to `A.10` and assurance claims belong to `B.3`. |
| Coordination cost displaced by responsibility change | A change in ordinary work organization or a responsibility relation improves local flow while pushing coordination into module interfaces, shared test, evidence, approval, or deployment structures. | Team or organization System and its relations; coordination relation; module-interface, evidence, deployment, Method or plan structure; and, only when current, local kind, separate System-classification judgment, assignment, enactor relation, and actual Work network. | Recover the shifted coordination cost and the structure under stress. If responsibility retargeting is claimed, name its direct predicate, old and proposed participants, and occurrence identity or return `missing-governor`; then decide whether the architecture repair belongs to `C.32.CONWAY`, `A.6.M`, or `C.32.MLAO`. | Route unresolved role wording through `E.10.ROLE`. Keep ordinary work organization, Method or plan structure, local kind, separate System-classification judgment, assignment, enactor relation, dated Work, and responsibility as separate branches under their subject patterns. |
| Temporal or control coupling | Named parts need brittle timing or control coordination. | Temporal relation, control relation, and affected work or evidence relation. | Recover the timing or control constraint and ask whether a candidate architecture change affects the selected structure. | Temporal adequacy claims belong to `C.27`, control or mechanism placement claims belong to the governing mechanism pattern, and flow-structure claims belong to `E.18` when current. |
| Evidence jump | The team asks for more evidence without naming the architecture uncertainty it would settle. | Architecture object whose evidence relation may be stale, misplaced, or bearer-dependent. | Name the affected architecture object and the uncertainty the evidence must settle. Reuse available evidence or obtain the needed result under `A.10` and the subject rule; then choose the justified repair. | Evidence relations belong to `A.10`, assurance to `B.3`, internal-constraint validity to `A.20`, and a named gate decision to `A.21` under an applicable profile. Release requirements remain with the patterns that define them. |
| Generated output as authority | A generated architecture-looking output is treated as carrying an authority relation for architecture adequacy. | Source cue, generated description, candidate selected structure, and evaluation boundary. | Treat the output as a source cue; recover source-side referent, selected structure, architecture-change kind, gain, loss, and the review needed for the intended reliance. | Use `C.32` for candidate generation and `C.30.AD` for generated-description use. For publication, use `E.24.PUB` for the occurrence and audience availability; add `E.17` when a source-backed face and source return are needed. |
| Single-structure synthesis | One selected structure is improved and called the architecture synthesis. | Synthesis structure map and architecture characteristic bundle. | Use C.32; name the other selected structures that must be coordinated and the architecture characteristics that make the trade-off real. | Stop at repaired C.32 palette, or open `C.32.MLAO` if the failure crosses scopes. |
| User function as architecture characteristic | A user-visible function is treated as the architecture quality being optimized. | Functional demand, architecture characteristic, and quality bundle boundary. | Recover the function through `A.6.F` or `C.30.ASV`; then name the architecture characteristic or `C.25` quality bundle separately. | Keep function and characteristic distinct in the explanation before relying on their comparison. |
| Function with no feasible bearer | A function graph, workflow, use case, method step, or neural cell graph names a required function whose feasible bearer is missing or unresolved under the current constraints. | Functional demand, candidate bearer set, module-interface relation, placement or deployment relation, resource access, control relation, and evidence burden. | Use `C.32`. Possible first repairs include adding or changing a bearer, splitting the function, changing placement or resource access, changing control responsibility, reducing demand, or rejecting the candidate. | Keep feasibility unresolved or reject the candidate for the affected use. Comparison can retain a provisional or infeasible alternative with that status; stronger conclusions require their own premises. |
| Static optimum | A front member or local winner is treated as durable optimum. | Evolution window, pattern for the next question result, front or archive relation, and reopen trigger. | Recover the preference's evolution window and grounds, with source-return conditions where needed; use C.18 and C.19 for retention or pool policy. | Use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, `G.5` for selected-set result declaration, and `C.32.PAD` for an architecture decision. For publication, use `E.24.PUB` for the occurrence and audience availability; add `E.17` when a source-backed face and source return are needed. |
| Ideality shortcut | Having fewer bearers or fewer modules is treated as architecture improvement by itself. | Function-bearing allocation, selected structure count, and architecture characteristic bundle. | Recover the function-bearing transfer; name the removed or generalized bearer, the functions still carried, the new burden, and lost structure. | Use `C.32`; use `C.31`, `A.6.F`, `A.6.M`, and `C.19.1` when their claims are current. |
| Universal bearer as adequacy shortcut | A universal module or general substrate is treated as architecture adequacy or scale adequacy by itself. | Scale-amenability claim, module-interface relation, evidence burden, control burden, and safety or admissibility boundary. | Treat the proposed universal module or general substrate as a candidate bearer; require BLP scale window or waiver when scale advantage is claimed and record coupling, evidence, control, and source-return effects. | Stop before G.5 selected-set result declaration, actual publication, assurance, release, or decision claims unless patterns for the next questions are current. |
| Mismatch between architecture influence and transformed-side structure | An influence-source architecture is collapsed with transformed-side architecture content, a desired transformed-side structure is paired with no compatible influence-source arrangement, or an architecture or selected structure is treated as the changing actor. | The exact changed referent; each influence-source-side and transformed-side obtaining C.30 `ArchitectureRelation` or modal `ArchitectureClaim`; and the direct architecture-influence or correspondence occurrence only when independently governed and obtaining. | Open `C.32.CONWAY`; recover the two exact architecture sides, the direct influence kind and predicate or `missing-governor`, and then prepare influence-source-side, transformed-side, joint, or bounded-mismatch candidates. Add acting systems, assignments, Work, and actual transformation only through their subject patterns when those claims are current. | Use `A.6.M` only for module-interface repair, `C.29` only when mathematical structural similarity is claimed, and E.18.NET only for an independently selected network; a C.32.CONWAY frame or exact pair row is neither an actor, network, nor cross-flow occurrence. |

Admit a new repair family only when its row tells the practitioner what to repair first. A suspicious name alone is not enough; the row must name the architecture object under stress, the first repair action, and the stop or pattern for the next question.

**Stop condition.** Stop when the affected object and justified next action are clear. Carry a source-return condition or another pattern when the next use needs it. A precise unresolved question can be the useful return; the cue itself supplies no evidence, assurance or decision verdict.

**Reconsideration condition.** Keep the symptom, affected object, supported observations and justified action current. If the object or repair remains unknown, retain the observation and the question needed to recover it. Missing documentation alone does not invalidate a known action. After a repair, examine whether it resolved the failure before retiring the active cue; preserve useful history. A changed object reopens the affected use. Use `A.6.P` or `E.10` when the case is only source-expression recovery, `C.32` when candidate repair is current, `C.32.MLAO` or `C.32.CONWAY` when their residual or correspondence repair is current, and the named pattern for the next question when a stronger downstream claim is current.

