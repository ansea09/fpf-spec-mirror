---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:4"
section_title: "Applicability table"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__007_applicability-table.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:4 — Applicability table"
line_start: 60732
line_end: 60748
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SPR"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.F"
  - "A.6.P"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.25"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.2"
  - "E.20"
  - "E.21"
  - "E.24"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.10.ARCH:4 - Applicability table

| Semantic area and ontological neighborhood | First applicable pattern | Trigger family | Required recovery apparatus | Typical recovery product |
| --- | --- | --- | --- | --- |
| Relation construction; primary recoverable use is relation use or relation-bearing claim | `A.6.P` and retained A.6 relation specializations | Relation, endpoint, qualifier, slot, scope, time, viewpoint, evidence-role distinction when an evidence role is current, basedness, service, bridge wording, whole or part, mapping, comparison, dependency, or evaluative ascription when the hidden claim is relation construction. | `RelationKind`, slot discipline, `QualifiedRelationRecord`, endpoint facets, qualifiers, L, A, D, and E hooks, and retained relation specializations named by value. | relation rewrite, relation record, candidate-set note, retained specialization application named by value, or fail-closed Plain disposition. |
| Function-like wording; primary recoverable use is the FPF kind named by value, relation, or claim hidden by `function`, `functional`, `functionality`, `effect`, or similar wording | `A.6.F` first when the FPF kind named by value, relation, or claim is not already recovered; direct governing pattern when it is recovered by value | Functional architecture, required transformation or effect, method, work occurrence or result, role expectation, mathematical function, relation, loss, objective, quality or functionality claim, module allocation, interface or signature relation, or evidence, assurance, gate, or decision overread. | `FunctionUseRepair`, kind and relation recovery, false-kind list, governing-pattern reference, `C.30` or `C.30.ASV` functional-structure boundary, `C.29` mathematical-lens boundary, `C.16` or `C.25` quality boundary, `A.6.M` module-interface relations and A.6 signature or slot applications. | FPF kind or relation named by value assignment, governing-pattern application, `FunctionFlowModuleAlignmentNote`, mathematical-lens application, quality or characteristic application, `A.6.M` module-interface application, ordinary-prose demotion, or stop. |
| Episteme, publication, and source-use; encountered entity or construction may be source span, carrier, face, publication, `PublicationUnit`, EntityOfConcern-like head, old EntityOfConcern-family wording, or text-work evaluation cue | `C.2.P` first; evaluation pattern governing the recovered evaluation claim after recovery when the corresponding claim is being made | Source-expression, episteme or publication wording, FPF-governed wording, `EntityOfConcern` or `describedEntity`-family wording, and `reading`, `read`, or `quality-read` wording when the word could mean source interpretation, publication use, FPF-governed use, or evaluation hidden inside text work. | source-expression clarification, FPF-governed use, claim-bearing episteme, EntityOfConcern, publication, view, face, carrier relation when that relation is being made, `PublicationUnit`, `publicationUnitPrimaryEntityOfConcern` when that publication relation is current, use disposition, project-side kind named by value or reference, sentence role, and evaluation claim or bundle named by value when current. | local rewrite, compact epistemic precision-restoration row, full check, recovered-by-value, reduced-use, blocked-use disposition, neighboring-pattern application, or evaluation-pattern application such as `E.22`, `E.21`, or `E.9.DA`. |
| Admissibility-like, legality-like, authority, validity, readiness, pass-looking, fail-looking, and conformance wording; primary recoverable use is bearer, claim kind, source relation, value frame, bounded use, and governing pattern, not a generic admissibility object | Direct governing pattern when the claim is recoverable by value; `A.19.SPR` only when a hidden state-family bearer and value frame are the problem; `A.6.P` only when relation construction is hidden | `admissible`, `lawful`, `legal`, `legality`, `allowed`, `permitted`, `authorized`, `valid`, `pass`, `fail`, `ready`, `conformant`, `eligible`, and close compounds. | bearer, claim kind, source relation, value frame, admissible use, non-admissible overread, validity window or reopen condition when current, and direct governing pattern for mechanism admissibility predicate, signature applicability, evidence, assurance, gate, work, decision, authority-bearing record, release, temporal validity, or source-use disposition. | direct governing-pattern application; state-family repair note only when hidden state wording is current; recovered gate, evidence, authority, temporal, mechanism, or source-use boundary; quote-only cue; reduced-use cue; blocked-use disposition; or stop. |
| Method, algorithm, program, solver, proof, recipe, workflow, process, procedure, access path, query plan, control strategy, or programming-paradigm wording; primary recoverable use is a slot or use-position in the method-description-work-mechanism chain | `A.3.1` first when method-like wording hides the slot; direct governing pattern after recovery; `C.2.P.DR` first when representation overread is the current problem | algorithm, program, solver, proof, recipe, method, workflow, process, procedure, access path, query plan, control strategy, imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, or similar wording. | current slot or use-position: context-local semantic way of doing (`A.3.1`), episteme describing a method (`A.3.2`), formal-substrate declaration (`A.6.0`) and mathematical-lens use (`C.29`) when current, mechanism declaration or realization (`A.6.1`/`E.20`), planned work (`A.15.2`), dated work (`A.15.1`), evidence relation (`A.10`), source relation, gate relation, result relation, direct governing pattern, or quote-only source wording. If one source label or project-side name points to changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern` rather than to one typed value, use the existing method/work/P2W governing-pattern constellation through `E.10.ARCH:3.1`; then recover linked typed FPF values separately. Do not assign the same typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits such dual typing. Slot-position labels do not create alternate ontology. | `U.Method` statement, `U.MethodDescription` relation, formal-substrate or mathematical-lens application, `U.Mechanism` or MIP application, WorkPlan or Work application, evidence relation, source relation, gate relation, or result relation, direct governing-pattern application, quote-only cue, reduced-use cue, blocked-use disposition, or stop. |
| Declarative representation and imperative-metaphor overread; primary recoverable use is a representation, relation, predicate, graph object, publication face, evidence relation, or pattern relation being treated as action, route, call, dispatch, permission, release, work, or evidence result | `C.2.P.DR` when no direct governing pattern already closes the claim; direct governing pattern when recovered by value | graph path, `PathSlice`, flow valuation, state predicate, checklist predicate, SQL-like query, table, dashboard, publication face, evidence path, pattern relation, representation, route, path, workflow, lifecycle, dispatch, exit, receiver, call, invoke, run, flow, send, move, or `EvidencePath` wording. | encountered representation, representation kind, represented object or claim, source-expression or publication relation when current, tempting imperative overread, recovered governing pattern, admissible use now, non-admissible overread, stop or reopen condition, and graph/evidence/publication/method/work/gate/authority pattern named by value when current. | `DeclarativeRepresentationRepair`, graph/path application under `E.18`, evidence/provenance relation under `A.10`, state-family repair under `A.19.SPR`, publication-face use under `E.17`, mathematical-lens use under `C.29`, method/method-description/work/gate/authority direct application, quote-only cue, reduced-use cue, blocked-use disposition, or stop. |
| Architecture and structure; primary recoverable use is selected structure, `ArchitectureOf@Context` relation, conditional `ArchitectureDescription@Context` use, structural view, or named C.30 subcase | `C.30.P` | Architecture-heavy or structure-heavy wording whose EntityOfConcern under repair, relation, or claim is not yet recoverable. | `A.22` selected structure and structural-view discipline, `C.30` `ArchitectureOf@Context`, `C.30.ASV` structural-view and structure-kind discipline, named C.30 subpattern applications, and `C.30.AD` only when full architecture-description mechanism is current. | architecture-structure repair note, repaired wording, selected-structure naming, architecture question, source-return condition, governing-pattern result, ordinary-prose demotion, or stop. |
| Stratification and source labels; primary recoverable use is hidden behind `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, `gate`, or close engineering source labels | `C.30.STRAT` when the governing pattern is not already recovered; direct governing pattern when it is recovered by value | Engineering, mathematical, publication, project, control, module, neural-network, or architecture prose uses a source label as if it named the FPF kind directly. | Source label, literal source wording, candidate primary EntityOfConcern, recovered FPF kind, recovered relation, recovered claim-use, recovered source-use disposition, governing-pattern selection, admissible use, non-use boundary, and adjacent governing-pattern applications to `C.30.P`, `C.30.LCA`, `A.6.M`, `C.30.TGA-FLOW-REL`, `C.16.P`, `C.29`, `C.2.P`, gate, work, or decision patterns, or ordinary source label. | `StratificationSourceLabelRepairNote`, direct governing-pattern application, ordinary-prose demotion, quote-only, reduced-use, or blocked-use disposition, or stop. |
| Characteristic and scale; primary recoverable use is characteristic, scale, coordinate, score, comparison, indicator role, or characteristic-space construction | `C.16.P` | Characteristic, scale, coordinate, value, score, indicator, threshold, comparison, metric, axis, dimension, feature, property, level, strong, weak, robust, or benchmark wording whose construction is not yet recoverable. | `A.17` Characteristic, `A.18` CSLC, `C.16` measurement, unit, evidence stub, `A.19` `CharacteristicSpace`, `C.25` Q-bundle, `C.29` mathematical-lens boundary, and `E.21` pattern-quality coordinate discipline. | characteristic-scale repair note, declared `Characteristic`, `Scale`, `Coordinate`, `Value`, and `Score` construction, non-comparability, non-measurement, blocked-gate disposition, governing-pattern result, ordinary-prose demotion, or stop. |
| Quality characterization and evaluative characterization; primary recoverable use is quality characterization, Q-bundle use, or pattern-quality coordinate use | `C.16.Q` | Quality or evaluative characterization wording when the hidden claim is not relation construction. | `C.16.P` where bearer or scale construction is hidden, `C.25` Q-bundle, `E.21` pattern-quality coordinates, and characterization or relation applications named by value. | quality-term repair note, quality-bundle or pattern-quality coordinate use, relation or bridge split when current, blocked scalar, gate, or release overread, governing-pattern result, ordinary-prose demotion, or stop. |
| State-family hidden claim; primary recoverable use is a bearer with a state-like value, status, readiness, currentness, or local finite field whose frame is hidden | `A.19.SPR` | State, status, posture, readiness, stance, currentness, validity, stable, accepted, blocked, candidate, admissible, ready, degraded, or close state-family compounds. | bearer kind, state frame or governing pattern, value set or classification source, admissible use, non-admissible overread, validity window or reopen condition, and direct governing-pattern application for source, evidence, assurance, gate, work, decision, temporal, lens-use, pattern-quality, or process cases. | state-family repair note, retained local field with bearer, value set, and admissible use named by value, direct governing-pattern application, quote-only cue, reduced-use cue, blocked use, ordinary-prose demotion, or stop. |
| Neighboring claim or admissible-use boundary already recoverable by value | Evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens, naming, controlled-coarsening, action-invitation, `A.6.M` module-interface, or another governing-pattern application | Any trigger family whose recovered FPF kind, relation, claim-use, source-use disposition, or admissible-use boundary is already recoverable by value. | The governing pattern's own ontology and conformance fields. | Direct governing-pattern application; no detour through a new restoration pattern. |

