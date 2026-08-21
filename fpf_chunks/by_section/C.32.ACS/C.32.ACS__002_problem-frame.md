---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set for Improvement Cycles"
section_id: "C.32.ACS:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__002_problem-frame.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set for Improvement Cycles"
  - "C.32.ACS:1 — Problem frame"
line_start: 62061
line_end: 62148
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
  - "anti-Goodhart guard"
  - "architecture characteristic criteria set"
  - "criteria row"
  - "improvement cycle"
  - "protected counter-characteristic"
  - "proxy risk"
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

**First-minute use slice.** A product-family architect has HCS starter heads and source catalogue names for maintainability, substitutability, evidence reuse, safety, availability, latency, and scale amenability. Using C.32.ACS, the practitioner builds project rows and gives each row its bearer, exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective reference scheme and plane, qualification or evaluation window, scale form, proxy risk, protected losses, and source-return condition. Maintainability, substitutability, and evidence reuse become optimization indicators; safety and availability remain monitored guardrails. The source phrase "scale amenability" remains only a starter cue until ACS admits a concrete characteristic row, such as exception growth or interface-grammar variation, with its bearer and scale form; a claim that one alternative is preferable under a declared scale window remains a separate `C.31.ASAP` object. C.32 can now synthesize candidates against declared criteria instead of a loose list of quality words.

This pattern concerns one project architecture-characteristic criteria-set record for improvement cycles. Its rows can supply C.32 synthesis, C.32.MLAO residual work, C.32.ACE eval programs, and later patterns for the next questions. The set and its rows are C.32.ACS-local record forms, not new `U.*` kinds; starter packs, `U.Characteristic` values, Q-Bundles, measurement methods and results, eval programs and results, candidate palettes, comparison rules, selection results, G.5 result declarations, actual publications, local choices, and architecture decisions remain separate objects.

Ordinary working move: make one row per project architecture characteristic, bind its bearer and scale, mark whether it drives optimization, guards against loss, or only gives context, and record what eval reading can reopen synthesis.

The first useful output is `ArchitectureCharacteristicCriteriaSet@Project`:

For a first pass, fill the described holon, architecture use, three to five draft row names, and for every row the bearer or selected structure, exact claim scope and selected context slices, reference scheme and plane, qualification or evaluation window, scale form, use class, protected losses, receiving use, and reopen condition. Add readings, target bands, and eval-program references only when the current receiving use needs them; add a selected `BoundedModelUseStructure` only when it independently changes interpretation of the row use.

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
      proxyRisk:
      protectedCounterCharacteristicRefs:
      receivingUseRef:
      sourceReturnCondition:
  optimizationIndicatorRowRefs:
  monitoredGuardrailRowRefs:
  contextOnlyRowRefs?:
  improvementCycleRef?:
  reopenCondition:
```

For `ArchitectureCharacteristicCriteriaSet@Project` and `ArchitectureCharacteristicImprovementRow@Project`, `@Project` is a compatibility and retrieval cue only; it establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. A criteria set or improvement row local to one actual project names both the exact composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining direct use relation for that exact record in `architectureCriteriaProjectUseRelationRef`; either field alone is insufficient, and a relation occurrence about the set is not silently reused for a distinct row. Otherwise the record remains retrieval-only and no project locality is asserted.

`draftProjectCriteriaRows` are draft project criteria rows. They are not candidate architectures, selected architectures, or a selected set returned by `A.19.SelectorMechanism`.

What goes wrong if C.32.ACS is missed: the team says that the architecture should be more maintainable, scalable, modular, safe, or evolvable, but no one can say which selected structures carry the characteristic, which few rows are criteria for the next optimization, which rows only guard against loss, which C.25 Q-Bundle is involved, or which eval result can reopen synthesis.

What C.32.ACS buys in practice: the practitioner can reduce broad catalogue and starter-pack material to draft project criteria rows, then to three to five optimization indicators, while keeping other important characteristics as monitored guardrails against Goodhart-style proxy loss.

Adoption test: after using C.32.ACS, the project can name the few rows that drive optimization, the guardrail rows that protect against loss, and the bearer, scale, proxy risk, receiving use, and reopen condition for each live row.

Not this pattern when the current work is choosing the holon-family starter pack, modeling a Q-Bundle, validating a measurement method, designing an eval program, synthesizing candidates, comparing or selecting candidates, choosing locally, declaring a selected-set result, publishing it to an audience, or deciding the project architecture.

Common exits by claim kind:

- `C.32.HCS` for holon-family starter packs.
- `C.25` for Q-Bundles and composite quality families.
- `C.16` for measurement templates, readings, units, thresholds, or comparability claims.
- `C.32.ACE` for eval-program framing and typed-result classification over declared rows; each actual result is a separate subject assertion under its exact predicate or constraint.
- `E.13` when an indicator, score, or dashboard starts replacing the declared architecture concern.
- `E.22` and `E.23` for improvement-question framing and repeated improvement method.
- `C.32` for candidate synthesis and `C.32.MLAO` for residual-reducing candidates.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for selected-set result declaration. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.
- `A.10` and `B.3` when evidence or assurance claims are being made.
- `C.32.PAD` for project decision.

