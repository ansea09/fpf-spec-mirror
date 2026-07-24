---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:3"
section_title: "Shared recovery algorithm"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__009_shared-recovery-algorithm.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:3 — Shared recovery algorithm"
line_start: 74100
line_end: 74135
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
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
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
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

Do not name a new recovery object. Recover the project concern first to find the linked direct relations and independently governed entities. Then recover the typed FPF values separately through their governing patterns. Typical values include `U.Method`, `U.MethodDescription`, `U.Mechanism`, formal-substrate declaration, mathematical-lens use, `U.WorkPlan`, a dated Work occurrence admitted under `U.Work`, evidence relation, source relation, gate relation, exact direct subject relation for a changed referent, measurement-result episteme, evaluation result, `C.11` `ChoiceResult` or decision record, publication relation, and temporal relation when current.

When the recovered project concern is not one method but a relation among methods or method families, recover `MethodRelationStructure@BoundedContext`: serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, selector relation, fallback relation, or another method-side relation. Govern it through `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current. Treat algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation as `C.29` mathematical-lens use or method-description representation, not as `U.MethodAlgebra`.

This branch recovers direct relations among already governed typed values. It publishes no new recovery object or super-kind; it keeps the project concern, actual relation participants, their direct relations, and the separately recovered FPF values from collapsing into one umbrella value.

A compact local restoration note records how wording restoration found those typed values: affected entity, bounded context, change or maintained-condition statement, state or delta predicates when current, and references to the governing method, description, mechanism, work, evidence, source-relation, gate, measurement, evaluation, choice, decision, publication, or temporal patterns. If a project needs a project record, evidence record, gate record, method, work plan, work occurrence, measurement-result episteme, evaluation result, `C.11` `ChoiceResult` or decision record, or ontic, use that direct governing pattern instead of treating the restoration note as the project value.

Each filled reference remains governed by its own pattern. `A.15` carries the role-method-plan-work alignment part; `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.10`, gate, source-relation, measurement, evaluation, decision, publication, temporal, and evidence patterns carry their own typed values. Do not assign one typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits that dual typing. Declaration-local SlotKind labels and relation-participant labels create no alternate ontology.

When `input`, `raw material`, epistemic `source data` or `source material`, `output`, `result`, `outcome`, `deliverable`, `handoff`, or work-name wording still hides one relation to method, plan, dated work, transformation, evaluation, delivery, transfer, or receiving use, apply `A.6.P.WMR` after generic relation recovery. Use `C.2.P` first for the epistemic source expression, episteme or publication, and source-to-use relation; keep physical raw material under its direct physical governor.

The WMR branch first recovers claim subject, modality and exact temporal extent, polarity, and recovery/support state independently, then closes with exactly one family: exact direct subject-relation claim, positive or governed negative; exact `A.6.1` operation-application binding; exact local `A.15.PROD` or `A.6.RCD` claim; or exact non-assertability result. Its reason is separately `factually unsupported`, `missing-information`, or `missing-governor`: the failed known `EpistemeUsedByReviewWorkAsReference` predicate uses the first; the unavailable ETL receiving-use fact under a known governor uses the second; and the absent `Patient_8472` / `HE-8472` health-effect relation kind and owner uses the third. Only `missing-governor` names the affected receiving use and future owner. Classification, a generic `result relation`, a `U.MethodDescription` field, a planned filling, an actual-slot-looking reference, or an inferred opposite polarity does not close the row.

If a current `U.*` name only duplicates a declaration-local SlotKind or relation-participant label, apply `E.24.UK` inside the E.24 ontic-introduction decision. Retain the `U.*` name only when a direct governing pattern supplies the durable-kind membership condition and the E.24 decision supplies stable ontic identity and action-facing gain. Otherwise keep the SlotKind declaration-local or keep the participant meaning as relation prose. If repeated method, work, and process material needs a durable ontic, write its E.24 decision and governing head pattern before citing it as current FPF ontology.

Use this recovery order for FPF-relevant wording-use restoration cases. Each realization pattern may publish a compact local form, but the order stays shared.

1. **Trigger and bounded text.** Name the bounded text span or publication unit, trigger span, local sentence function, register classification, and whether the text is conformant FPF, project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims, or source text being unpacked for possible FPF use.
2. **Cheap local closure.** Check whether the wording has no FPF-governed use or only a small local head, register, or morphology repair. If yes, repair locally under `E.10`, state the remaining reader use, and stop.
3. **Head kind and candidate ontology.** Recover the head kind, register classification, EntityOfConcern and Description-episteme boundary, specification-use gate when current, candidate referents, candidate EntityOfConcern values, direct relation kinds and actual participants, reusable `RelationSignature` and `SlotSpec` declarations when current, claim-bearing epistemes and participant designations when current, candidate carriers or publications, and scope, time, viewpoint, or context facets. Include literal and intended candidates when metonymy or compression is plausible.
4. **Semantic area, ontological neighborhood, and governing-pattern selection.** State `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`; then select the `ontologicalNeighborhood` and first applicable governing pattern by primary `EntityOfConcern` kind and admissible adjacent FPF fields. The alternatives in this sentence are governing-pattern neighborhoods, not one hidden kind: relation construction, function-like kind and relation recovery, episteme, publication, source relation, selected structure or architecture description, characteristic or scale construction, quality characterization, evidence, assurance, gate, work, decision, causal-use, naming, controlled coarsening, or another governing FPF pattern.
5. **Formal apparatus or stable substrate.** State the stable apparatus that makes the repair checkable. The alternatives are governed apparatus families, not one object type: direct relation predicate and occurrence-identity rule; reusable `RelationSignature` SlotSpecs; publication relations; source-relation disposition; selected structure; architecture question; characteristic or scale construction; quality bundle; mathematical lens under `C.29`; evidence or provenance relation; work occurrence; decision, assurance, gate, or causal-use object under its direct pattern; or another governing-pattern field set. When the same entity participates in several direct relations, is designated by several assertion epistemes, or corresponds to several representation elements, keep those uses distinct and cite each governing pattern. `E.10.ARCH` selects the restoration architecture rather than duplicating those ontologies.
6. **Normalized ontology and lexical projection.** Produce repaired wording, a compact repair note, a claim-bearing episteme, a direct governing-pattern application, or a non-use disposition according to the recovered object. Do not replace one umbrella word with another. The replacement candidate is itself a bounded wording use until it passes the `E.10` trigger scan or is demoted to ordinary wording, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite.
7. **Admissible use and remaining reader use.** State the admissible use, non-admissible claim escalation or adjacent use, and one useful reader use. If the wording is type-correct but inert, the repair is incomplete.

Perform a terminology-source audit only when source ontology can change the recovered governed object, direct relation kind, relation-participant meaning, actual participant kind, declaration-local SlotSpec, assertion-side participant designation, exact use, admissible use, or governing-pattern selection. For relation-shaped material, apply the relation-use recovery rule above and `A.6.5` only when reusable typed declaration is current. Do not turn stable ordinary prose into type annotation merely because the repair can name its ontology.

The sequence is shared; each wording-use restoration case differs by `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, primary `EntityOfConcern` use fields, current governed object, any exact direct relation use, `ontologicalNeighborhood`, governing pattern, substrate, and result.

