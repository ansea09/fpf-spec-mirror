---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "FPF Pattern Publication Form for Evaluation Guidance"
section_id: "E.8.ECSPF:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__008_conformance-checklist.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "E.8.ECSPF — FPF Pattern Publication Form for Evaluation Guidance"
  - "E.8.ECSPF:7 — Conformance Checklist"
line_start: 73963
line_end: 73982
dependencies:
  - "A.19.ECS"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.8.ECSPF:7 - Conformance Checklist

| Check | Requirement | Why |
|---|---|---|
| `CC-E8ECSPF-1` | The pattern SHALL carry every required value from the accepted `EvaluationCharacteristicSpaceSpec` and every optional value whose trigger holds, including reader scope, qualification window, neighbouring exits, and the applicable `E.22` and `E.23` conditions. A citation or field-name list alone does not satisfy this requirement. | Prevents loss between the accepted specification and practitioner-facing content. |
| `CC-E8ECSPF-2` | Recognition text SHALL state evaluated object kind, declared use, working reader, qualification window, first evaluation use, FPF-publication boundary, and object-kind boundary before dense coordinate tables. | Keeps the pattern usable before it becomes reviewable. |
| `CC-E8ECSPF-3` | The `Solution` SHALL carry the accepted specification's values rather than leaving them only in conformance rows, SoTA rows, or examples. | Prevents checklist substitution. |
| `CC-E8ECSPF-4` | Worked cases SHALL include passing, below-floor, and outside-declared-object-kind boundary outcomes. | Tests evaluated-object-kind discrimination. |
| `CC-E8ECSPF-5` | Each coordinate SHALL state value meanings, polarity or no-simple-direction value rule, missingness rule, and protected trade-off when applicable to the declared evaluation use. | Makes evaluation uses repeatable and bounded. |
| `CC-E8ECSPF-5a` | The publication form SHALL prohibit an undeclared total or average over ordinal coordinates. Any admitted scalarization SHALL name its method, declared use, information loss, applicability, and stop or return condition. | Prevents a convenient number from replacing the evaluation. |
| `CC-E8ECSPF-5b` | When one visible value improves, the evaluation use SHALL check whether an intended value or protected trade-off worsened and SHALL stop or reopen when the evaluation would reward that loss. | Blocks proxy improvement and Goodhart-style degradation. |
| `CC-E8ECSPF-6` | When the publication form makes an outside claim, `Relations` SHALL cite the applicable `PatternID` and state its concrete contribution in ordinary language. The contribution is not limited to a fixed verb list. A pattern citation SHALL NOT be retyped as a Method or MethodDescription. Simple relations stay free of phrase apparatus, and architecture-placement reasoning stays out of publication-form evaluation prose. | Prevents a second ontology or apparatus-overwrapped publication form. |
| `CC-E8ECSPF-6a` | Wording, naming, or precision-restoration repairs SHALL follow `F.19`. When a repair can change an FPF-governed meaning, it SHALL check the evaluated object and its kind, relation or claim kind, live ontic slot, relation position, use relation, admissible use, and scope before and after the repair, as applicable to the changed claim. For a claim outside this pattern, cite the applicable pattern id and state its concrete contribution. Require a particular assertion, episteme edition, `ClaimGraph`, `U.Method`, qualifying `U.MethodDescription`, or Method use only when its admission test passes and the receiving claim depends on that identity. | Prevents evaluation patterns from inheriting lexical cleanup as ontology drift or locator use as formal identity. |
| `CC-E8ECSPF-7` | If the authored publication form is under improvement, `E.21` SHALL evaluate FPF pattern-version quality separately from the evaluation's evaluated object result. | Keeps pattern quality distinct from evaluated object quality. |
| `CC-E8ECSPF-8` | An author SHALL not turn a local, temporary, or one-project evaluation specification into an FPF pattern unless its reuse scope is durable and the patterns used for outside claims are named with their concrete contributions. | Blocks needless pattern growth. |
| `CC-E8ECSPF-9` | The publication form SHALL state what would lower, reopen, or retire the accepted specification or the guidance that carries it: changed object kind or object version, changed use, reader, or qualification window, changed use of a cited source, changed source adoption, adaptation, or rejection decision, missing contrast case, coordinate-value drift, missingness or comparison-rule change, or a correction to an exit or outside claim. | Makes maintenance of the pattern testable. |
| `CC-E8ECSPF-10` | The publication form SHALL state the required result row shape and evidence basis. If values need external, comparator, projection, worked-case, or currentness evidence, the result form SHALL require that evidence by value or lower the coordinate. | Prevents the pattern from accepting prose impressions or two-column value lists as evaluation results. |
| `CC-E8ECSPF-11` | A reusable pattern that teaches an evaluation SHALL publish calibration points for common adjacent-value disagreements and any coordinate-specific evidence payload needed to reach floor or exceptional values. | Makes the same evaluation guidance usable by more than one evaluator. |
| `CC-E8ECSPF-12` | The publication form SHALL keep `E.21` values, `PatternQualityStatus`, corpus-projection evidence, README, ToC, E.11, and I.2 alignment, card or retrieval evidence, cold-reader evidence, monolith parity, landing evidence, Developer, Reviewer, and Executor correspondence, and other quality-carrier facts out of the pattern. These facts belong in the `E.21` result, `E.19` run record, README, ToC, E.11, or I.2, card, retrieval, or projection carrier, or release or landing evidence carrier unless the content-use test shows that the pattern's own `EntityOfConcern` and user-facing action are that evaluation or projection work. | Prevents quality of the authored pattern from replacing the evaluation guidance it must teach. |

