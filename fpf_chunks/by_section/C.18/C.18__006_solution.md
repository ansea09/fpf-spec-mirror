---
chunk_kind: "child"
pattern_id: "C.18"
pattern_title: "Open-Ended Search Archive and Front Stewardship"
section_id: "C.18:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18/C.18__006_solution.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.18 — Open-Ended Search Archive and Front Stewardship"
  - "C.18:4 — Solution"
line_start: 49300
line_end: 49452
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "C.16"
  - "C.19"
  - "C.30"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "C.36"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "currentness"
  - "descriptors"
  - "exploration archive"
  - "generation"
  - "lineage"
  - "non-dominated front"
  - "open-ended search"
  - "refresh"
  - "retained exploration value"
  - "telemetry"
---

### C.18:4 - Solution

Keep archive, front, telemetry, generation, and downstream relations as separate records.

#### C.18:4.1 - Archive Record

```text
ExplorationArchiveRecord@Context:
  archiveRef:
  variantSetRef:
  descriptorMapRef:
  characteristicSpaceRef:
  distanceDefinitionRef?:
  retentionPolicyRef:
  retainedExplorationValue:
  steppingStoneUse?:
  lineageOrEditionPins:
  telemetryRefs?:
  currentnessAsOf:
  currentStatus:
  stopOrRefreshReason:
  nextGoverningRelation:
```

Use this record when the current question is retained exploration value, coverage, novelty, diversity, stepping-stone value, future reachability, curriculum expansion, lineage, or archive policy. Do not use the archive record as a selected-set publication or work permission.

#### C.18:4.2 - Front Record

```text
FrontRecord@Context:
  frontRef:
  candidateSetRef:
  comparatorOrDominanceSetRef:
  admissibilityRef:
  descriptorMapRef?:
  characteristicSpaceRef?:
  relationTokenSetRef:
  excludedTelemetryRefs?:
  selectedSetPublicationRef?:
  currentnessAsOf:
  currentStatus:
  stopOrRefreshReason:
  nextGoverningRelation:
```

Use this record when the current question is non-domination, Pareto relation, Q-front membership, comparator currentness, admissibility, or partial-order preservation. The front may feed `G.5`, but it is not itself a selected-set publication unless `G.5` makes that publication.

#### C.18:4.2a - Filled Archive And Front Micro-Records

```text
ExplorationArchiveRecord@Context:
  archiveRef: dance-lab-variant-archive-2026
  variantSetRef: choreography variants generated during a festival lab
  descriptorMapRef: timing, body vocabulary, risk, teachability, audience recognizability
  characteristicSpaceRef: festival style-engineering characteristic space
  distanceDefinitionRef: difference in timing and body-vocabulary descriptors
  retentionPolicyRef: keep rare but teachable variants and variants that open later combination work
  retainedExplorationValue: stepping stones for teaching and later style intervention
  steppingStoneUse: candidate material for C.36 cultural-evolution case work
  lineageOrEditionPins: lab session, teacher edit, platform-publication edition
  telemetryRefs: replay counts, class adoption counts, jury notes
  currentnessAsOf: lab records and platform-publication edition reviewed through 2026-07-31
  currentStatus: active for retained exploration and teaching use
  stopOrRefreshReason: reopen if the teaching-use judgement, retention policy, lineage, or platform edition changes
  nextGoverningRelation: C.36 case card or G.11 refresh, depending on the current question
```

```text
FrontRecord@Context:
  frontRef: cooling-module-maintainability-energy-front
  candidateSetRef: retained cooling-module architecture candidates
  comparatorOrDominanceSetRef: energy-use and maintainability comparator
  admissibilityRef: safety and manufacturing constraints already admitted by project policy
  descriptorMapRef: thermal performance, service access, part count, manufacturing tolerance
  characteristicSpaceRef: product-family architecture characteristic space
  relationTokenSetRef: non-dominated candidates under current comparator
  excludedTelemetryRefs: tests outside the current temperature envelope
  selectedSetPublicationRef: empty until G.5 publishes the selected set
  currentnessAsOf: comparator, safety constraints, and test evidence reviewed through 2026-07-31
  currentStatus: active non-dominated front for the declared comparator
  stopOrRefreshReason: reopen if eligibility, comparator, dominance grounds, or evidence edition changes
  nextGoverningRelation: C.30 architecture candidate treatment, G.5 selected-set publication, or G.11 refresh
```

#### C.18:4.3 - Generation And Downstream-Use Record

When loop-engineering practice generates many agent prompts, harness variants, workflow variants, or framework seeds, `C.18` records generation, archive, front, descriptors, telemetry, retained exploration value, lineage, and the next governing relation. It does not say that the loop improved. Use `E.23` only when one retained object version is changed and re-evaluated; use `G.9` for parity between variants and `G.5` when a selected set must be published.

```text
OpenEndedVariantGenerationRecord@Project:
  problemCardRef?:
  generationMethodOrFamilyRef:
  sourceRefs?:
  evaluatorOrComparatorRef?:
  emitterPolicyRef?:
  insertionPolicyRef?:
  dedupThreshold?:
  deduplicationBasisRef?:
  deduplicationUnit?:
  variantSetRef:
  descriptorMapRef:
  characteristicOrDescriptorSetRef:
  archiveOrFrontRef?:
  architectureCandidateRefs?:
  culturalVariantRefs?:
  telemetryRefs?:
  projectLocality?:
    generationWorkOccurrenceRef:
    compositeProjectWorkOccurrenceRef:
    governingRelationPatternRef:
    exactGenerationToProjectRelationRef:
  workPlanOrMeasurementRef?:
  refreshRef?:
  currentnessAsOf:
  currentStatus:
  stopOrRefreshReason:
  nextGoverningRelation:
```

Across the archive, front, and generation records, `currentnessAsOf` names the replay date or window together with the relevant pinned editions; `currentStatus` states whether the recorded archive/front/generation relation is active, held, closed, or stale for its declared use; and `stopOrRefreshReason` names the condition that ended it or the exact trigger that would reopen its currentness. These fields record the boundary but do not perform refresh. When source, descriptor, comparator, policy, evidence, or edition currentness becomes the live question, `nextGoverningRelation` points to `G.11` and `refreshRef?` may cite the separately governed refresh record.

Here `@Project` is a compatibility and retrieval cue, not a project kind or relation assertion. Fill `projectLocality?` only after both Work occurrences have been admitted independently and the cited relation actually obtains under its direct governor. `generationWorkOccurrenceRef` names the exact dated generation `U.Work`; `compositeProjectWorkOccurrenceRef` names the selected composite project `U.Work`; and `exactGenerationToProjectRelationRef` cites, rather than creates, the exact work-part, containing-work, decision-use, source-use, or other governed relation. Use work parthood only when the complete `A.15.1` basis holds. Otherwise omit `projectLocality?`: the `@Project` suffix remains retrieval-only and establishes no project Work, parthood, authority, context, or viewpoint.

For example, a completed harness-generation run may state:

```text
projectLocality:
  generationWorkOccurrenceRef: HarnessVariantGenerationRun-2026-07-31 : U.Work
  compositeProjectWorkOccurrenceRef: AgentHarnessProjectWork-2026 : U.Work
  governingRelationPatternRef: A.15.1
  exactGenerationToProjectRelationRef: OperationalPartOf_work(HarnessVariantGenerationRun-2026-07-31, AgentHarnessProjectWork-2026)
```

Every optional field whose name ends in `Ref?` points to a separately governed object, claim, policy profile, or measurement basis. `dedupThreshold?` is not a reference: it carries one declared scalar threshold value. `deduplicationUnit?` carries its unit literal. Fill `emitterPolicyRef?` and `insertionPolicyRef?` only when the cited C.19 profile or insertion policy actually governs the current pool treatment. When a threshold is inherited, the cited profile supplies `dedupThreshold`, `deduplicationBasisRef`, and `deduplicationUnit`; when it is not inherited, carry the scalar in `dedupThreshold?` and its basis and unit in `deduplicationBasisRef?` and `deduplicationUnit?`. These references and scalars do not give C.19 a generation operator or move archive/front ownership out of C.18. In particular, `problemCardRef?` may cite a C.22.2 problem-side episteme but creates neither an actual Problem nor a `ProblematicForRelation` under `C.22.PFR`. A generated variant, archive entry, front membership, telemetry value, or retained-exploration claim is neither an improvement-result nor a work-result identity and creates no relation from generation Work to a result. `nextGoverningRelation` names the next owner; it does not itself make a choice, publish a selected set, authorize work, perform refresh, or make any relation obtain.

Use this record when generation is current. `architectureCandidateRefs` become architecture moves only through `C.30`, `C.30.ASV`, or `C.30.AD`. `culturalVariantRefs` become cultural-evolution cases only through `C.36`. Local choice uses `C.11`; work planning and performed work use the A.15 family; effect measurement uses its direct measurement and evaluation owners; refresh uses `G.11`. P2W carry-through uses `E.18.1` when an accepted problem-side distinction must be preserved into the next relation.

#### C.18:4.4 - Front And Archive Are Different Returns

- Start from one declared candidate or eligibility set.
- Return the non-dominated front over the declared comparator, dominance set, or relation-token set.
- Return the exploration archive separately when retained exploration value, coverage, novelty, diversity, stepping-stone value, or future reachability is current.
- Keep tie-breakers and telemetry explicit so diversity, illumination, or popularity signals do not rewrite front semantics.
- Before promoting telemetry or a popularity-like signal into the comparator, dominance set, or selected-set criteria, state which intended archive/front use or value becomes worse when that signal improves and cite the policy or decision authority that admits the trade-off. If either answer is missing, keep the signal as telemetry or an explicitly bounded tie-breaker rather than silently promoting it.
- Use `RetentionIntent=steppingStone` when retention exists for frontier expansion or later curriculum value rather than current dominance.
- If one source line keeps both returns, say that the front answers current non-domination while the archive answers retained exploration value.

#### C.18:4.5 - Cultural And Architecture Variant Boundaries

For architecture-candidate generation, C.18 records generation, archive, front, descriptor, telemetry, and retained exploration value. C.30 governs the architecture claim: `ArchitectureOf@Context`, selected structure or structure kind, affected characteristic, and next architecture move.

For cultural variants, C.18 records the generated or retained variant set and its descriptors, lineage, telemetry, and archive or front relation. C.36 governs the cultural-evolution case when collective-holon or discipline-facing method, work, role, canon, memory, recognition, selection, mediation, style, tradition, or intervention relations are current. F.17, F.18, and F.9 govern durable term and bridge work for labels such as style, tradition, genre, scene, school, and technique.

