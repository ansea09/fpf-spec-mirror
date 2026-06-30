---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:3"
section_title: "Shared recovery algorithm"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__009_shared-recovery-algorithm.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:3 — Shared recovery algorithm"
line_start: 69541
line_end: 69571
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
  - "A.3.4"
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
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.2"
  - "E.20"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.10.ARCH:3 - Shared recovery algorithm

#### E.10.ARCH:3.1 - Method, work, and P2W governing-pattern constellation in wording restoration

Use this branch when one source label, project handle, or project concern points to changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern` rather than to one typed FPF value.

Do not name a new recovery object. Recover the project concern first only to find the linked relation positions. Then recover the typed FPF values separately through their governing patterns. Typical filled values include `U.Method`, `U.MethodDescription`, `U.Mechanism`, formal-substrate declaration, mathematical-lens use, `U.WorkPlan`, dated `U.Work`, evidence relation, source relation, gate relation, result relation, publication relation, and temporal relation when current.

When the recovered project concern is not one method but a relation among methods or method families, recover `MethodRelationStructure@BoundedContext`: serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, selector relation, fallback relation, or another method-side relation. Govern it through `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current. Treat algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation as `C.29` mathematical-lens use or method-description representation, not as `U.MethodAlgebra`.

This branch selects relation positions among already governed typed values. It publishes no new recovery object or super-kind; it only keeps the project concern, relation positions, and separately recovered FPF values from being collapsed into one umbrella value.

A compact local restoration note records how wording restoration found those typed values: affected entity, bounded context, change or maintained-condition statement, state or delta predicates when current, and references to the governing method, description, mechanism, work, evidence, source, gate, result, publication, or temporal patterns. If a project needs a project record, evidence record, gate record, method, work plan, work occurrence, or ontic, use that direct governing pattern instead of treating the restoration note as the project value.

Each filled reference remains governed by its own pattern. `A.15` carries the role-method-plan-work alignment part; `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.10`, gate, source, result, publication, temporal, and evidence patterns carry their own typed values. Do not assign one typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits that dual typing. Ontic-slot labels and relation-position labels do not create alternate ontology.

If a current `U.*` name in the constellation looks like only an ontic-slot label or relation-position label, apply `E.24`: retain the `U.*` name only when an existing governing pattern gives it standalone `EntityOfConcern` identity, stable identity criterion, and action-facing gain. If not, demote that use to a SlotKind or relation label rather than keeping the U-kind by inertia. If repeated method, work, and process material actually needs a durable ontic, open an E.24 ontic-introduction decision and write the governing head pattern before citing that ontic as current FPF ontology.
Use this recovery order for FPF-relevant wording-use restoration cases. Each realization pattern may publish a compact local form, but the order stays shared.

1. **Trigger and bounded text.** Name the bounded text span or publication unit, trigger span, local sentence function, register classification, and whether the text is conformant FPF, project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims, or source text being unpacked for possible FPF use.
2. **Cheap local closure.** Check whether the wording has no FPF-governed use or only a small local head, register, or morphology repair. If yes, repair locally under `E.10`, state the remaining reader use, and stop.
3. **Head kind and candidate ontology.** Recover the head kind, register classification, EntityOfConcern and Description-episteme boundary, specification-use gate when specification use is current, candidate referents, candidate EntityOfConcern values, relation records named by value, claim records, candidate relations, candidate ontic slots, candidate relation positions, candidate use relations, candidate carriers or publications, and scope, time, viewpoint, or context facets. Include literal and intended candidates when metonymy or compression is plausible.
4. **Semantic area, ontological neighborhood, and governing-pattern selection.** State `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`; then select the `ontologicalNeighborhood` and first applicable governing pattern by primary `EntityOfConcern` kind and admissible adjacent FPF kinds, references, or relations: relation construction, function-like kind and relation recovery, episteme, publication, source-use, selected structure or architecture description, characteristic or scale construction, quality characterization, evidence, assurance, gate, work, decision, causal-use, naming, controlled coarsening, or another governing FPF pattern.
5. **Formal apparatus or stable substrate.** State the stable apparatus that makes the repair checkable: relation or signature slots under `A.6.0`, `A.6.5`, and `A.6.P`; publication relation set; source-use disposition; selected structure; architecture question; characteristic or scale construction; quality bundle; mathematical lens under `C.29`; evidence or provenance relation; gate record; work occurrence; decision record; assurance argument; causal-use record; or governing-pattern field set. When the same object is used in several relation, signature, or lens positions, record the object kind and current ontic slot, relation position, or use relation separately and cite the governing pattern; `E.10.ARCH` selects the restoration architecture rather than duplicating that pattern's ontology.
6. **Normalized ontology and lexical projection.** Produce the repaired wording, compact repair note, record-shaped value, governing-pattern application, or non-use disposition. Do not replace one umbrella word with another. The replacement candidate is itself a bounded wording use until it passes the `E.10` trigger scan or is demoted to ordinary wording, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite.
7. **Admissible use and remaining reader use.** State the admissible use, non-admissible claim escalation or adjacent use, and one useful reader use. If the wording is type-correct but inert, the repair is incomplete.

Perform a terminology-source audit only when the wording imports a source ontology that can change the recovered object, kind, relation, current ontic slot, relation position, use relation, admissible use, or governing pattern. For slot-shaped material, use `E.24` slot-language unless a governing boundary or interface pattern makes interface meaning current. Do not turn stable ordinary prose into type annotation merely because the repair can name its ontology.

The sequence is shared; each wording-use restoration case differs by `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, primary `EntityOfConcern` use fields, current ontic slot, relation position, and use-relation field set, `ontologicalNeighborhood`, governing pattern, substrate, and result.

