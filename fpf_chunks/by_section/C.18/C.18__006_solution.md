---
chunk_kind: "child"
pattern_id: "C.18"
pattern_title: "Open-Ended Search Archive and Front Stewardship"
section_id: "C.18:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18/C.18__006_solution.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.18 — Open-Ended Search Archive and Front Stewardship"
  - "C.18:4 — Solution"
line_start: 48534
line_end: 48641
dependencies:
  - "A.15"
  - "A.17-A.19"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.5.2.1"
  - "C.16"
  - "C.17"
  - "C.19"
  - "C.2"
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
  - "G.6"
  - "G.9"
keywords:
  - "CandidateSet"
  - "DescriptorMapRef"
  - "DistanceDefRef"
  - "EmitterPolicyRef"
  - "Front vs ExplorationArchive"
  - "IlluminationSummary report-only telemetry"
  - "InsertionPolicyRef"
  - "NQD-CAL"
  - "NQDArchive"
  - "provenance editions"
  - "Γ_nqd.generate"
  - "Γ_nqd.illuminate"
  - "Γ_nqd.selectFront"
  - "Γ_nqd.updateArchive"
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
  nextGoverningRelation: C.30 architecture candidate treatment or G.5 selected-set publication
```

#### C.18:4.3 - Generation And Downstream-Use Record
When loop-engineering practice generates many agent prompts, harness variants, workflow variants, or framework seeds, `C.18` records generation, archive, front, descriptors, telemetry, retained exploration value, lineage, and next governing relation. It does not say that the loop improved. Use `E.23` only when a retained object version is changed and re-evaluated; use `G.9` for parity between variants and `G.5` when a selected set must be published.

```text
OpenEndedVariantGenerationRecord@Project:
  problemCardRef?:
  generationMethodOrFamilyRef:
  variantSetRef:
  descriptorMapRef:
  characteristicOrDescriptorSetRef:
  archiveOrFrontRef?:
  architectureCandidateRefs?:
  culturalVariantRefs?:
  telemetryRefs?:
  workPlanOrMeasurementRef?:
  refreshRef?:
  nextGoverningRelation:
```

Use this record when generation is current. `architectureCandidateRefs` become architecture moves only through `C.30`, `C.30.ASV`, or `C.30.AD`. `culturalVariantRefs` become cultural-evolution cases only through `C.36`. Work planning, performed work, effect measurement, and refresh use the A.15 family and `G.11`. P2W carry-through uses `E.18.1` when an accepted problem-side distinction must be preserved into the next relation.

#### C.18:4.4 - Front And Archive Are Different Returns

- Start from one declared candidate or eligibility set.
- Return the non-dominated front over the declared comparator, dominance set, or relation-token set.
- Return the exploration archive separately when retained exploration value, coverage, novelty, diversity, stepping-stone value, or future reachability is current.
- Keep tie-breakers and telemetry explicit so diversity, illumination, or popularity signals do not rewrite front semantics.
- Use `RetentionIntent=steppingStone` when retention exists for frontier expansion or later curriculum value rather than current dominance.
- If one source line keeps both returns, say that the front answers current non-domination while the archive answers retained exploration value.

#### C.18:4.5 - Cultural And Architecture Variant Boundaries

For architecture-candidate generation, C.18 records generation, archive, front, descriptor, telemetry, and retained exploration value. C.30 governs the architecture claim: `ArchitectureOf@Context`, selected structure or structure kind, affected characteristic, and next architecture move.

For cultural variants, C.18 records the generated or retained variant set and its descriptors, lineage, telemetry, and archive or front relation. C.36 governs the cultural-evolution case when collective-holon or discipline-facing method, work, role, canon, memory, recognition, selection, mediation, style, tradition, or intervention relations are current. F.17, F.18, and F.9 govern durable term and bridge work for labels such as style, tradition, genre, scene, school, and technique.

