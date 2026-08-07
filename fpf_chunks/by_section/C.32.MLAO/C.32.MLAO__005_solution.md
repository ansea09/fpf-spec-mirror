---
chunk_kind: "child"
pattern_id: "C.32.MLAO"
pattern_title: "Multilevel Architecture Residual Optimization"
section_id: "C.32.MLAO:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.MLAO/C.32.MLAO__005_solution.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.32.MLAO — Multilevel Architecture Residual Optimization"
  - "C.32.MLAO:4 — Solution"
line_start: 66175
line_end: 66230
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

Build a residual-reducing frame around one recoverable residual. The frame is not a universal optimization target and not a scalar optimization result.

Work in eight steps:

1. Start from a `C.30.ILC`-compatible residual triage.
2. Name the affected declared holon-level refs or declared scope refs and the selected structures that carry the residual.
3. Name the architecture-characteristic criteria rows and any Q-Bundle slots that make the residual worth reducing.
4. Create or reference a C.32 candidate palette.
5. For each candidate, state the residual it reduces, the selected structure changed, and the criteria rows affected.
6. State the new burden, loss, exception, or source-return load created by that candidate.
7. Record the evolution window and whether any NQD, OEE, archive, front, stepping-stone, ideality, or BLP support is only keeping candidate plurality or directionality alive.
8. Stop at the frame, or name the receiving pattern when a later claim is being made: explicit comparison belongs to `A.19.CPM`, set-returning selection to `A.19.SelectorMechanism`, publication of a selected set to `G.5`, local choice to `C.11`, architecture decision to `C.32.PAD`, architecture-description work to `C.30.AD`, publication-face work to `E.17` or `E.24.PUB`, and mathematical-lens use to `C.29`.

Admit a residual-reducing candidate only when it answers the working questions: which declared holon-level ref or declared scope ref is affected, which selected structure changes, which architecture-characteristic row or Q-Bundle slot is at stake, what residual is reduced, what structure is preserved or lost, and what new burden appears.

| Candidate change family | Use when | Repair it provides |
|---|---|---|
| `splitScope` | One scope carries incompatible tempo, functional demand, constraint, or admissibility condition. | Separates the conflict and names coordination cost. |
| `mergeScope` | Mediation creates more burden than separation saves. | Removes unnecessary boundary and names coupling risk. |
| `addMediator` | Direct cross-scope dependency is brittle. | Adds mediation and names mediator failure mode. |
| `addControlStructure` | Rate, feedback, policy, or supervisor conflict persists. | Makes control responsibility explicit and names timing or accountability burden. |
| `addInterfaceGrammar` | Variation grows through unmanaged interface variants. | Names allowed variation, conformance expectation, and exception risk. |
| `repairFunctionBearerGap` | A residual-reducing functional change has no feasible bearer at the affected declared holon-level ref or declared scope ref. | Adds or changes bearer, splits function, changes placement or resource access, changes control responsibility, or rejects the candidate. |
| `addEvidenceScope` | Reusable candidate bearer lacks reusable evidence scope. | Makes evidence maintenance part of the candidate; A.10 evidence-relation validity or sufficiency claims belong to `A.10` when they are current. |
| `addWorkMethodScope` | Repeated work remains bespoke because method structure is missing. | Transfers repeated work into method structure and names review or training burden. |
| `repairArchitectureInfluenceCorrespondence` | The residual is carried by mismatch between one exact typed influence-side architecture source and transformed-side architecture content for the changed referent. | Open `C.32.CONWAY`; keep the changed referent and any actual A.3.4 `U.Transformation` separate, then prepare candidate alternatives that change the influence-source side, change the transformed side, change both, or keep a bounded mismatch. |
| `acceptBoundedException` | Eliminating the residual costs too much now. | Records exception, source-return condition, and reopen trigger. |

**Comparison-input boundary.** C.32.MLAO prepares comparison inputs; it does not run the comparison or choose a candidate. Its output rows are candidate records with residual reduced, new burden, selected structures, preserved structure, lost structure, source-return condition, and optional C.29 lens-output references.

Those references are diagnostic inputs only.

Admitted profiles and a `ComparatorSpec` belong to the receiving explicit-comparison pattern.

If the current claim is explicit comparison, use `A.19.CPM` with admitted profiles and a declared `ComparatorSpec`. If the claim is local choice over an existing option set, use `C.11`. If the claim is set-returning selection, use `A.19.SelectorMechanism`. If the claim is publication of a selected set, use `G.5`.

**Lens-output discipline.** Graphs, fronts, residual vectors, DSMs, RG-like descriptions, and frustration language are C.29 lens outputs, structural descriptions, or diagnostic signals after their architecture use is typed. The real failure is proxy preference: a candidate is preferred because the output looks better while selected structures, lost structure, architecture characteristics, and receiving pattern remain unnamed. The repair is to interpret the output over selected structures and state what residual or loss it exposes; any comparison, selection, or choice claim then belongs to its receiving pattern.

**Method, culture, and episteme discipline.** Method-family, culture/practice-source, and episteme-mediated cases are admitted only when the described holon, bounded context, governing owner pattern, and selected structures are recoverable. If a publication family or publication face is in view, recover whether it is a described holon, a selected structure, an architecture description, or an MVPK face before using it. C.32.MLAO governs only the residual-reducing architecture candidate frame; method, work, publication, evidence, ethical, and decision claims use their governing patterns when current.

**Dynamic candidate discipline.** A preferred or retained candidate is bounded by an evolution window, source conditions, and the receiving pattern that admitted the preference or retention. NQD, OEE, C.18, and C.19 can keep a front, archive, pool, or stepping stone visible; they do not select the architecture and they do not turn a front member into a durable optimum.

**Ideality and BLP discipline.** TRIZ ideality can suggest residual-reducing candidate changes: remove a support bearer, transfer a useful function onto an existing resource, or generalize a bearer so fewer selected structures carry more useful functions. BLP can prefer a more general scale-amenable bearer only inside its declared scale window and audit boundary. Both lines guide candidate generation; neither removes the need to state new burden, lost structure, and receiving pattern.

**Functional-bearer feasibility discipline.** A residual-reducing functional change is not admissible until the function has a bearer under the module, placement, resource, control, information, and evidence constraints declared for the case. If no bearer exists, the residual-reducing candidate must add a bearer, split the function, change placement or resource access, change control responsibility, reduce the demand, or return to C.32 as an unfit candidate.

**Architecture-influence and transformed-side discipline.** When a residual is carried by one independently typed architecture-side source constraining architecture content for a changed referent, use `C.32.CONWAY`. For each actual side, keep the exact C.30 described holon, obtaining `ArchitectureRelation`, and selected `U.Structure` together; keep candidate, required, desired, or expected content in an exact C.30 `ArchitectureClaim`. Keep the changed referent and any actual A.3.4 `U.Transformation` separate. Then prepare residual-reducing candidates that change the influence-source side, the transformed side, both sides, or a bounded mismatch as comparison inputs or downstream candidate alternatives. Influence, transformation, flow, Work, and module-interface claims belong to their exact relation owner, `A.3.4`, `E.18`, `A.15`, or `A.6.M` when current. Structural-similarity claims belong to `C.29` only when they are current.

**Level, stratification-term, and whole-reidentification discipline.** If the case uses `level`, `system level`, `holon level`, `layer`, `tier`, or another stratification term, first use `E.10.ARCH` and `C.30.STRAT` unless the direct governing pattern and recovered neighborhood are already named by value. If the case uses `BOSC`, `MHT`, `MET`, `MFT`, emergence-family, boundary-crossing, or promotion-like wording, first use `E.10` and `B.2.P` to recover the claim kind. Use `B.2` only when a whole-reidentification question remains after the existing-whole explanation check; otherwise use the direct governing pattern for architecture, boundary, capability, function, measurement, publication, work, or lens claims.

**Stop condition.** Stop after the frame names residual, affected declared holon-level refs or declared scope refs, candidate changes, new burdens, preserved and lost structure, source-return conditions, and receiving patterns.

**Lowering condition.** Keep the frame as C.32.MLAO work only while the residual triage, affected level or scope refs, selected structures, criteria rows, evolution window, residual reduced, new burden, and receiving pattern remain current. Lower a candidate to a diagnostic note when the residual is not recoverable, the selected structure is unknown or stale, the architecture characteristic is missing, the new burden is not named, or the receiving pattern cannot use the row. Retire a candidate when its evolution window closes or a stronger residual triage replaces it. Return to `C.30.ILC` when the residual itself is missing, to `C.32.ACS` when criteria rows are missing, to `C.32.ACE` when eval results are needed but not current, to `C.29` when the current claim is a mathematical-lens claim, and to `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, or `C.32.PAD` when the downstream claim is current.

