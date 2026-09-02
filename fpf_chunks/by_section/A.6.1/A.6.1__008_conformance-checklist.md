---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Reusable Law-Governed Operation Declaration"
section_id: "A.6.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__008_conformance-checklist.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.6.1 — U.Mechanism - Reusable Law-Governed Operation Declaration"
  - "A.6.1:7 — Conformance Checklist"
line_start: 13377
line_end: 13400
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "E.24.PUB"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "LawSet"
  - "OperationAlgebra"
  - "U.Mechanism"
  - "application binding"
  - "operation application"
  - "operation declaration"
  - "realization"
---

### A.6.1:7 - Conformance Checklist

1. **Exact episteme.** One `U.Mechanism` episteme and its exact `EntityOfConcernRef` are recoverable.
2. **Identity.** Content, EntityOfConcern, and effective `U.ReferenceScheme` remain recoverable.
3. **Signature dependence and family-level anchors.** The mechanism uses A.6.0 signature content and adds operation and admission semantics without becoming a second root beside `U.Episteme`. One truthful family-level `SubjectKind` and `RangedValueKind` pair is connected to the exact argument or result meanings that realize those declarations; optional `ResultKind` is present only for one distinct family-level result kind. Additional operation-local ValueKinds remain local. If no common pair exists, split the declaration or stop instead of using a union or generic input or output list.
4. **Typed operation declarations.** Every reused operation has declaration-local argument and result meanings, exact ValueKinds, binding designation rules, and semantic cardinalities when needed. None is an A.6.5 SlotSpec.
5. **Application semantics.** Every claimed particular application has an exact application predicate, identity rule, extent rule, and recoverable occurrence boundary.
6. **Actual bindings.** Every claimed actual argument or returned result has an obtaining declaration-local binding with the exact application and bound value; type compatibility, description, plan, record, or token match is insufficient.
7. **Binding identity.** The application, exact mechanism episteme, operation designator, argument or result designator, bound value, and maximal continuous binding extent distinguish the binding occurrence.
8. **Recognition result.** A recognition-evaluation declaration uses `true | false | unknown` with the A.1 meanings; `unknown` is not false, a candidate state, evidence status, currentness, or receiving disposition.
9. **Law and admission split.** Reusable laws, proposed-application admission predicates, and the operation's own returned value remain distinct.
10. **Exact applicability.** `U.ClaimScope`, time, selected `CHR:ReferencePlane` when current, and mechanism-specific conditions replace generic context wording.
11. **Optional structure.** A model-use structure is cited only when its selected relations delimit or change the receiving mechanism use; it does not replace the effective reference scheme or claim scope.
12. **Dependency truth.** SignatureManifest content names actual imports and provided names only when dependency replay matters.
13. **Realization relation.** A realizer keeps its direct kind; the direct relation declares its participants, obtaining predicate, and maximal-continuous-interval identity rule.
14. **Evaluation and evidence boundary.** Evidence availability can change evaluation or warrant without changing world-side satisfaction; an argument binding establishes use, not truth or warrant.
15. **Method and work boundary.** Method, method description, work plan, dated work, actual application, and binding remain separately identifiable. A.6.1 defines neither dated-work identity nor work mereology.
16. **Result boundary.** A result binding neither produces nor constitutes its bound entity and does not materialize a C.2.1 result episteme.
17. **Mechanism comparison claims.** Every refinement, conservative-extension, or equivalence claim names exact endpoint mechanism epistemes, reference schemes, scope, predicate, and preserved and changed content. Historical continuation is stated only through a separately obtaining C.2.1 `EpistemeEditionRelation`; a comparison or shared label supplies none. The claim uses an already admitted direct relation, the applicable A.6.RCD branch, or the exact missing-governor stop. Generic mechanism `transport` is absent; exact cross-context `SchemeSenseCell` correspondence requires F.9.
18. **Mathematical-lens boundary.** Quotient, product, morphism, operand order, and tuple claims use C.29 when mathematical structure preservation is current.
19. **Progressive explicitness.** One-off direct use is not forced into a mechanism declaration or application-binding apparatus.
20. **CGUS boundary.** Mnemonic imperatives are not called an executable sequence; condition-governed continuation uses A.22.CGUS.
21. **Changed object.** Declaration, application, binding, realization, evaluation, evidence, work, representation, and publication changes return to the object that actually changed.

