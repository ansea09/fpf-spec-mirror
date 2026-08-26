---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:9"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__010_conformance-checklist-normative.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:9 — Conformance Checklist (normative)"
line_start: 50470
line_end: 50494
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:9 - Conformance Checklist (normative)

0. **Minimal A.6.0 declaration.** `TaskSignature` exposes exact `EntityOfConcernRef`, effective `U.ReferenceScheme`, `SubjectKind`, `RangedValueKind`, optional `ResultKind`, `SliceSet`, and `ExtentRule`, plus Vocabulary, Laws, and Applicability. Add `SignatureManifest` only when dependency replay needs actual imports and provided names; it does not supply signature identity.
1. **Signature and assignment present.** Every exported selector-facing case names one TaskSignature identity and edition plus one `TaskSignatureAssignmentRelation` whose exact problem-side episteme, TaskSignature, receiving-use episteme, obtaining conditions, and occurrence extent are recoverable. No setting, carrier, or organization is added as a fourth participant. Current characteristic bindings are CHR-typed; a live unknown preserves `unknown`, while a non-current optional vocabulary item remains absent.
   1a. **Publication and designators do not define identity.** Two E.17 publications or serialized records that resolve to the same `<declaration content, EntityOfConcernRef, effectiveReferenceScheme>` identify the same TaskSignature episteme. Carrier, layout, serialization, `SignatureId`, or edition label alone does not create a new identity component.
2. **CHR admissibility proven.** Any numeric comparison or aggregation **cites CG-Spec** by **Characteristic id** and proves **CSLC admissibility**; **no mean on ordinals; no unit mixing**.
3. **Unknowns remain typed.** A live unknown remains `unknown`, cites the direct downstream policy, and is not coerced. The acceptance, eligibility, or selector pattern records its own governed result.
4. **Evidence and assurance are conditional.** When the receiving use relies on evidence or provenance, cite the exact A.10 relation and only the source edition, currentness, and freshness conditions that reliance needs. When an assurance claim or material-reliance threshold is current, cite its separate B.3 result, applicable assurance lanes, and declared fold. Otherwise the TaskSignature needs neither an evidence dossier nor an assurance fold.
5. **Cross-semantic use is separated.** Declare `ReferencePlane` for a value or objective head when its interpretation or comparison needs it. A scheme or plane difference alone creates neither a Bridge nor a penalty. Resolve two exact F.17 local senses, test the F.9 predicate, and state any proposed use separately.
6. **Acceptance thresholds live in CAL.** No acceptance-gate thresholds in CHR or code paths; only in **G.4 AcceptanceClauses**.
7. **Selector-use support.** The TaskSignature exposes the scales, units, polarities, and admitted order relations needed by `G.5`; it carries no mixed-scale scalarization or local selector verdict. `G.5` governs any Pareto-set result when its admissible relation remains partial.
8. **Bridge and use claims remain distinct.** For current cross-semantic reuse, cite the two exact local senses and an actual F.9 Bridge only when its predicate is true. State the action, direction, correspondence rule, tolerated loss, and polarity in a separate bounded-use claim; if the predicate is false, keep the local values separate.
9. **Packaging is conditional.** Create an F.9 card, terminology row, Name Card, or reusable package only when a named receiving pattern independently needs that artifact. Packaging describes an already tested relation and separate use claim; it establishes neither.
10. **Structure and gates are conditional.** Apply E.18 crossing checks only when a selected transformation-flow structure and exact `GateCrossing` are current. Apply A.21 only when a named gate decision is current. Each pattern supplies its own result; neither a structure nor a gate makes F.9 obtain, and C.22 requires no crossing or gate package otherwise.
11. **QD fields (when QD is in scope).** A `TaskSignature` with `PortfolioMode=Archive` or QD heads is complete only when it carries CHR-typed **CharacteristicSpaceRef** (d>=2), **ArchiveConfig** (topology, resolution, K, `InsertionPolicyRef`, `DistanceDefRef.edition`), and **EmitterPolicyRef** fields; every characteristic declares its **ReferencePlane**.
12. **DominanceRegime default.** `DominanceRegime` defaults to `ParetoOnly`. Illumination enters dominance only through a cited **CAL.Acceptance policy** enabling that relation; the SCR records the policy id.
13. **Telemetry.** The telemetry record carries **PathSliceId** when an E.18 path slice is current, the applicable **decay and refresh policy ids**, and edition counters for **CharacteristicSpaceRef**, **DistanceDefRef**, and **EmitterPolicyRef**. An illumination increase is traceable to the policy id that admitted it.
14. **GeneratorIntent (when OEE is in scope).** A TaskSignature supports the claimed OEE generator-family use only when `GeneratorIntent` cites **`EnvironmentValidityRegion`** and **`TransferRulesRef`** with ids resolvable in G.5 and C.23. Any downstream abstention is their result, not a C.22 output.
15. **Budgets.** When `Budgeting` is live, its evaluation, time, and batch values carry declared units and the applicable E/E-LOG exploration-budget id.
16. **Archive-comparison support.** A TaskSignature supports the claimed archive comparison only when `DistanceDefRef.edition` and the applied novelty measures are CSLC-admissible and editioned. The archive or selector pattern defines or constrains any downstream abstention or returned-set result.
17. **Planes.** QD heads and characteristics declare a `ReferencePlane` when their meaning or comparison depends on it. A plane difference alone creates neither correspondence nor an assurance adjustment. Use item 8 for a current cross-semantic claim and item 4 for any separately current B.3 assurance result.
18. **Unknown QD values.** A live unknown QD field remains `unknown`, cites the policy governing its downstream use, and is not coerced or mapped by C.22 itself.

19. **Specialization claims referenced.** A declared specialization on this TaskSignature is complete when it names the task family and work target, work-measure threshold target, adaptation budget, freshness or provenance basis for reuse, and the exact TaskSignature edition and assignment relation needed for the same claim to remain admissible in `C.22.1`, `G.5`, and `G.9` use.

