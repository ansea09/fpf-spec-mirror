---
chunk_kind: "child"
pattern_id: "C.32.MLAO"
pattern_title: "Architecture Candidates to Reduce Cross-Scope Residuals"
section_id: "C.32.MLAO:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.MLAO/C.32.MLAO__005_solution.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.32.MLAO — Architecture Candidates to Reduce Cross-Scope Residuals"
  - "C.32.MLAO:4 — Solution"
line_start: 77785
line_end: 77840
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.6.M"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.29"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "G.5"
keywords:
  - "Pareto front"
  - "declared level"
  - "declared scope"
  - "ideality pressure"
  - "multilevel architecture residual optimization"
  - "residual-reducing candidate frame"
  - "scale amenability"
  - "stepping stone"
---

### C.32.MLAO:4 - Solution

Develop candidate changes around one recoverable residual; record them in the form needed for their use.

Work in eight steps:

1. Start from a `C.30.ILC`-compatible residual triage.
2. Name the affected levels or scopes and the selected structures that carry the residual. Supply declared refs when the receiving use requires them.
3. Explain why reducing the residual matters. Reuse adequate architecture-characteristic criteria and Q-Bundle slots; develop missing criteria through `C.32.ACS` when needed for the proposed use.
4. Develop or reuse a C.32 candidate palette. Investigation of a candidate may expose structure or criteria not yet understood.
5. For each candidate, state the residual it is expected to reduce, the selected structure changed, and the characteristics or criteria affected.
6. Assess the new burden, loss, exception, or source-return load that the candidate could create within the declared evolution window. State what is expected and unresolved; if none is identified, say which affected structures, scopes, and criteria were inspected.
7. Record the evolution window and any support that only keeps candidate plurality or directionality alive, such as NQD, OEE, an archive or front, stepping-stone retention, ideality, or BLP.
8. Stop at the frame, or name the pattern for the next question when a later claim is current: use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `G.5` for selected-set result declaration, `C.11` for local choice, `C.32.PAD` for an architecture decision, `C.30.AD` for architecture-description work, and `C.29` for mathematical-lens use. For publication, use `E.24.PUB` for the actual occurrence, form, carrier, audience, bounded use and availability; add `E.17` when a source-backed face and return to source are needed.

Before relying on a candidate for residual reduction, answer the working questions: which scope and selected structure change, which architecture characteristic or Q-Bundle slot is at stake, what residual is expected to decrease, what structure is preserved or lost, and what new burden is expected or why none is currently identified. A provisional candidate can retain unanswered questions; it cannot supply the conclusions those answers would support.

| Candidate change family | Use when | Repair it provides |
|---|---|---|
| `splitScope` | One scope carries incompatible tempo, functional demand, constraint, or admissibility condition. | Separates the conflict and names coordination cost. |
| `mergeScope` | Mediation creates more burden than separation saves. | Removes unnecessary boundary and names coupling risk. |
| `addMediator` | Direct cross-scope dependency is brittle. | Adds mediation and names mediator failure mode. |
| `addControlStructure` | Rate, feedback, policy, or supervisor conflict persists. | Adds or changes control relations, states timing burden, and names any direct control-responsibility predicate with actual participants; if none is admitted, records the exact missing governor instead of inferring responsibility from the control structure. |
| `addInterfaceGrammar` | Variation grows through unmanaged interface variants. | Names allowed variation, conformance expectation, and exception risk. |
| `repairFunctionBearerGap` | A residual-reducing functional change has no feasible bearer at the affected declared holon-level ref or scope ref. | Proposes or changes a feasible bearer, splits the function, changes placement, resource access, or control relations, or rejects the candidate. Any responsibility change uses its direct domain predicate or exact missing governor. |
| `addEvidenceScope` | Reusable candidate bearer lacks reusable evidence scope. | Makes evidence maintenance part of the candidate. For a current evidence use, apply `A.10` for source recovery and bounded reliance, and the applicable subject rule to judge whether the evidence supports the named claim or meets the named requirement. |
| `addWorkMethodScope` | Repeated work remains bespoke because method structure is missing. | Proposes reusable method structure for the repeated work and names review or training burden. |
| `repairArchitectureInfluenceCorrespondence` | The residual is carried by mismatch between one exact typed influence-side architecture source and transformed-side architecture content for the changed referent. | Open `C.32.CONWAY`; keep the changed referent and any actual A.3.4 `U.Transformation` separate, then prepare candidate alternatives that change the influence-source side, change the transformed side, change both, or keep a bounded mismatch. |
| `acceptBoundedException` | Eliminating the residual costs too much now. | Records the exception and reopen trigger, including source return when needed to recover a consequential distinction. |

**Comparison-input boundary.** C.32.MLAO prepares comparison inputs; it does not run the comparison or choose a candidate. Its comparison inputs state expected residual reduction, possible new burden, selected structures and relevant preservation or loss. Include source-return conditions when a later use needs omitted distinctions, and C.29 lens-output references when used.

Those references are diagnostic inputs only.

Admitted profiles and a `ComparatorSpec` belong to the receiving explicit-comparison pattern.

If the current claim is explicit comparison, use `A.19.CPM` with admitted profiles and a declared `ComparatorSpec`. If the claim is local choice over an existing option set, use `C.11`. If the claim is set-returning selection, use `A.19.SelectorMechanism`. If the claim is selected-set result declaration, use `G.5`. For publication, use `E.24.PUB` for the occurrence and audience availability, with `E.17` when a source-backed face and source return are needed.

**Lens-output discipline.** Graphs, fronts, residual vectors, DSMs, RG-like descriptions, and frustration language are C.29 lens outputs, structural descriptions, or diagnostic signals after their architecture use is typed. The real failure is proxy preference: a candidate is preferred because the output looks better while selected structures, lost structure, architecture characteristics, and pattern for the next question remain unnamed. The repair is to interpret the output over selected structures and state what residual or loss it exposes; any comparison, selection, or choice claim then belongs to its pattern for the next question.

**Method, culture, and episteme discipline.** For a Method-family, culture, practice, or episteme case, first name the described holon, optimization question and use, selected structures, and the pattern that defines or constrains each load-bearing claim. If a publication family or publication face is in view, decide whether it is the described holon, a selected structure, an architecture description, or an MVPK face before using it. C.32.MLAO defines only the residual-reducing architecture candidate frame; use the applicable patterns for Method, Work, publication, evidence, ethical, and decision claims.

**Dynamic candidate discipline.** A preferred or retained candidate is bounded by an evolution window, source conditions, and the pattern for the next question that admitted the preference or retention. NQD, OEE, C.18, and C.19 can keep a front, archive, pool, or stepping stone visible; they do not select the architecture and they do not turn a front member into a durable optimum.

**Ideality and BLP discipline.** TRIZ ideality can suggest residual-reducing candidate changes: remove a support bearer, transfer a useful function onto an existing resource, or generalize a bearer so fewer selected structures carry more useful functions. BLP can prefer a more general scale-amenable bearer only inside its declared scale window and audit boundary. Both lines guide candidate generation. When removing a bearer, inspect transferred functions and possible coupling, evidence, control and source-return burdens; retain the applicable scale boundary and receiving comparison or choice rules.

**Functional-bearer feasibility discipline.** Before a candidate can support a feasibility or residual-reduction claim, name a bearer that could perform the function under the applicable module, placement, resource, control, information and evidence constraints. This is a design-time feasibility claim, not proof that the System, assignment, or Work already exists. An assignment supplies neither capability, functioning, function bearing, nor performance. If feasibility is unknown, investigate the consequential uncertainty. If no feasible bearer can be proposed, add or change a candidate bearer, split the function, change placement, resource access, or control relations, reduce the demand, or mark the candidate unfit for that use. It may remain useful as an exploratory alternative or counterexample. Responsibility still needs an admitted direct predicate or the exact missing governor.

**Architecture-influence and transformed-side discipline.** When a residual is carried by one independently typed architecture-side source constraining architecture content for a changed referent, use `C.32.CONWAY`. For each actual side, keep the exact C.30 described holon, obtaining `ArchitectureRelation`, and selected `U.Structure` together; keep candidate, required, desired, or expected content in an exact C.30 `ArchitectureClaim`. Keep the changed referent and any actual A.3.4 `U.Transformation` separate. Then prepare residual-reducing candidates that change the influence-source side, the transformed side, both sides, or a bounded mismatch as comparison inputs or downstream candidate alternatives. Influence, transformation, flow, Work, and module-interface claims belong to their exact relation pattern, `A.3.4`, `E.18`, `A.15`, or `A.6.M` when current. Use `C.29` when a mathematical structural-similarity claim is current.

**Level, stratification-term, and whole-reidentification discipline.** When stratification wording leaves the relevant object or relation unclear, use `E.10.ARCH` and `C.30.STRAT`. When `BOSC`, `MHT`, `MET`, `MFT`, emergence, boundary-crossing or promotion wording leaves the claim kind unclear, use `E.10` and `B.2.P`. Use the recovered subject pattern directly when the meaning is already clear. Use `B.2` only when a whole-reidentification question remains after the existing-whole explanation check; otherwise use the subject pattern for architecture, boundary, capability, function, measurement, publication, work, or lens claims.

**Stop condition.** Stop when the needed candidate account explains the residual, affected scopes and structures, proposed changes and possible new burdens. Preserve the distinctions, loss and source-return conditions needed by its receiving use. An exploratory account may finish with unresolved questions; comparison or decision inputs must meet their receiving rules.

**Reconsideration condition.** A changed residual, structure, criterion or evolution window reopens the affected candidate claims. Preserve any still-supported account and useful provisional questions. A missing binding blocks the use that needs it; it does not erase independent information. Retain a candidate for a new window only when its premises still hold, and revise or retire the affected claim when they do not. Use `C.30.ILC` when the residual itself is missing, `C.32.ACS` when criteria rows are missing, `C.32.ACE` when eval results are needed but not current, `C.29` when the current claim is a mathematical-lens claim, and `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, or `C.32.PAD` when the downstream claim is current.

