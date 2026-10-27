---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set"
section_id: "C.32.ACS:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__002_problem-frame.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set"
  - "C.32.ACS:1 — Problem frame"
line_start: 76560
line_end: 76649
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.30"
  - "C.30.P"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.HCS"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "Q-Bundle"
  - "architecture criteria"
  - "attainable observation"
  - "protected qualities"
  - "proxy risk"
  - "required result"
  - "structural alternatives"
---

### C.32.ACS:1 - Problem frame

Use this pattern when a project must turn architecture-characteristic pressure into a small project criteria set for architecture improvement, candidate synthesis, residual optimization, and later eval work.

Primary working reader: an architect or architecture-responsible practitioner turning broad quality names into project criteria rows for the next improvement cycle.

Typical entry phrases:

```text
"Maintainability matters, but which bearer and scale make it an architecture criterion here?"
"We can optimize only a few rows; which characteristics drive optimization and which guard against loss?"
"Architecture around a Method, local system-role kind, separate System-classification judgment, assignment, AI workflow, or built asset has trustworthiness or teachability pressure; what is the exact characteristic bearer and which Q-Bundle slot or ACS row is current?"
```

**First-minute use slice.** A product-family architect has HCS starter heads and source catalogue names for maintainability, substitutability, evidence reuse, safety, availability, latency, and scale amenability. Using C.32.ACS, the practitioner builds project rows and gives each admitted row its bearer, exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective reference scheme and plane, qualification or evaluation window, scale form, relevant proxy risk and protected losses, and a source-return condition when that use needs one. Maintainability, substitutability, and evidence reuse become optimization indicators; safety and availability remain monitored guardrails. The source phrase "scale amenability" remains only a starter cue until ACS admits a concrete characteristic row, such as exception growth or interface-grammar variation, with its bearer and scale form; a claim that one alternative is preferable under a declared scale window remains a separate `C.31.ASAP` object. C.32 can now synthesize candidates against declared criteria instead of a loose list of quality words.

This pattern constructs a project architecture-characteristic criteria set for the receiving improvement or evaluation question. The optional records below can keep its bindings recoverable. Its rows can supply C.32 synthesis, C.32.MLAO residual work, C.32.ACE eval programs, and later patterns for the next questions. The named set and row records are C.32.ACS-local forms, not new `U.*` kinds; starter packs, `U.Characteristic` values, Q-Bundles, measurement methods and results, eval programs and results, candidate palettes, comparison rules, selection results, G.5 result declarations, actual publications, local choices, and architecture decisions remain separate objects.

Ordinary working move: make one row per project architecture characteristic, bind its bearer and scale, mark whether it drives optimization, guards against loss, or only gives context, and record what eval reading can reopen synthesis.

The first useful result is a set of criteria with their meanings, use classes and necessary bindings. Use `ArchitectureCharacteristicCriteriaSet@Project` when a record helps:

For a first pass, identify the described holon, architecture use, a small set of draft criteria and their possible bearers. Keep missing bindings as explicit questions. Before admitting a criterion for its receiving use, establish its bearer or selected structure, claim scope and relevant context slices, reference scheme and applicable plane, qualification or evaluation window, scale form, use class, protected losses and reopen condition. An incomplete draft does not yet support that use. Add readings, target bands, and eval-program references only when the current receiving use needs them; add a selected `BoundedModelUseStructure` only when it independently changes interpretation of the row use.

```text
ArchitectureCharacteristicCriteriaSet@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureCriteriaProjectUseRelationRef?: U.RelationRef governed by the exact criteria-use or work-use pattern
  describedHolonRef:
  architectureUseRef:
  holonFamilyStarterPackRef?:
  sourceCatalogueRefs?:
  draftProjectCriteriaRows:
    - architectureCharacteristicRef:
      sourceHeadOrStarterPackRef?:
      bearerOrSelectedStructureRefs:
      rowClaimScopeRef: U.EntityRef referencing one U.ClaimScope
      selectedContextSliceRefs:
      modelUseStructureRef?:
      effectiveReferenceScheme:
      referencePlane?:
      qualificationOrEvaluationWindow:
      endpointShape: singleCharacteristic | qBundle | qBundleSlot | sourceVocabularyOnly
      qBundleRef?:
      architectureQuestion:
      scaleFormRef:
      polarity:
      useClass: optimizationIndicator | monitoredGuardrail | contextOnly
      currentReadingRef?:
      targetBandOrStopCondition?:
      readingMethodRefOrNoReadingReason:
      evalProgramRefs?:
      proxyRisk: relevant risk, unresolved risk, or reason no material proxy risk was identified
      protectedCounterCharacteristicRefs?: when a loss needs protection
      receivingUseRef:
      sourceReturnCondition?: when source return can change the receiving use
  optimizationIndicatorRowRefs:
  monitoredGuardrailRowRefs:
  contextOnlyRowRefs?:
  improvementCycleRef?:
  reopenCondition:
```

For `ArchitectureCharacteristicCriteriaSet@Project` and `ArchitectureCharacteristicImprovementRow@Project`, `@Project` is a compatibility and retrieval cue only; it establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. A criteria set or improvement row local to one actual project names both the exact composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining direct use relation for that exact record in `architectureCriteriaProjectUseRelationRef`; either field alone is insufficient, and a relation occurrence about the set is not silently reused for a distinct row. Otherwise the record remains retrieval-only and no project locality is asserted.

If precise Work is asserted, recover each actual performer System's A.13 core, then independently admit the dated occurrence under A.15.1 from its performance history, Method actually followed, temporal extent and required containing-System relation. Add F.6 only when the receiving use consumes precise assignment-bound attribution through the same obtaining A.13 assignment and its declared species. F.6 identifies neither assignment nor performer; missing or failed F.6 attribution alone leaves the Work intact while its independent A.13/A.15.1 grounds still hold.

`draftProjectCriteriaRows` are draft project criteria rows. They are not candidate architectures, selected architectures, or a selected set returned by `A.19.SelectorMechanism`.

What goes wrong if C.32.ACS is missed: the team says that the architecture should be more maintainable, scalable, modular, safe, or evolvable, but no one can say which selected structures carry the characteristic, which few rows are criteria for the next optimization, which rows only guard against loss, which C.25 Q-Bundle is involved, or which eval result can reopen synthesis.

The practitioner can narrow catalogue or starter material to criteria that change the next action, with optimization indicators distinguished from binding constraints and safeguards against proxy loss.

Adoption test: after using C.32.ACS, the project can name the few rows that drive optimization, the guardrail rows that protect against loss, and the bearer, scale, proxy risk, receiving use, and reopen condition for each live row.

Not this pattern when the current work is choosing the holon-family starter pack, modeling a Q-Bundle, validating a measurement method, designing an eval program, synthesizing candidates, comparing or selecting candidates, choosing locally, declaring a selected-set result, publishing it to an audience, or deciding the project architecture.

Common exits by claim kind:

- `C.32.HCS` for holon-family starter packs.
- `C.25` for Q-Bundles and composite quality families.
- `C.16` for measurement templates, readings, units, thresholds, or comparability claims.
- `C.32.ACE` for eval-program framing and typed-result classification over declared rows; obtain each actual result separately under the pattern that defines and tests its kind and exact predicate or constraint.
- `E.13` when an indicator, score, or dashboard starts replacing the declared architecture concern.
- `E.22` and `E.23` for improvement-question framing and repeated improvement method.
- `C.32` for candidate synthesis and `C.32.MLAO` for residual-reducing candidates.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for selected-set result declaration. For publication, use `E.24.PUB` for the publication occurrence and audience availability, and E.17 when a source-backed face and source return are needed.
- `A.10` for source recovery and bounded reliance, `G.6` when an addressable provenance path is needed, and `B.3` for an actual named assurance claim; use the direct pattern that defines or tests any additional evidence or validity claim.
- `C.32.PAD` for project decision.

