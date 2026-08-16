---
chunk_kind: "child"
pattern_id: "G.2"
pattern_title: "SoTA Harvester & Synthesis"
section_id: "G.2:7"
section_title: "Conformance Checklist (normative) — CC‑G2"
source_path: "FPF-Spec.md"
output_path: "by_section/G.2/G.2__008_conformance-checklist-normative-cc-g2.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "G.2 — SoTA Harvester & Synthesis"
  - "G.2:7 — Conformance Checklist (normative) — CC‑G2"
line_start: 99590
line_end: 99620
dependencies:
  - "A.10"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.19"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.13"
  - "G.3-G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "BridgeMatrix"
  - "DeclaredSubstrateAtlasView"
  - "FlowRecord"
  - "GammaEpistSynthId"
  - "SoTA Synthesis Pack@CG-Frame"
  - "SoTA harvest"
  - "SoTAPaletteDescription"
  - "Tradition"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "palette-first"
  - "synthesis"
---

### G.2:7 - Conformance Checklist (normative) — **CC‑G2**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                                                                                        | Purpose / Notes                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **CC‑G2‑CoreRef**         | A conforming `G.2` artefact **MUST** satisfy the **effective** core obligations declared by the `GCoreLinkageManifest` in `G.2:4.1` (per `G.Core` Expansion rule).                                                                                                                                                                                 | Phase‑2 bridge clause: ensures universal invariants are not redefined inside `G.2`. |
| **CC-G2-Pluralism-1** | A conforming pack MUST include at least two `Tradition` lineages and at least three materially distinct entries, each identified by its source edition and claim region, with its EntityOfConcern, evidence norm, and comparison limits visible. | Prevents a single lineage or one renamed source cut from masquerading as synthesis. |
| **CC‑G2‑Ledger‑1**        | A conforming pack **MUST** include `G.2a CorpusLedger` with inclusion/triage status and explicit rationale hooks per entry.                                                                                                                                                                                                                        | Makes discovery/triage auditable.                                                   |
| **CC‑G2‑FlowRecord‑1**    | A conforming pack **MUST** include `G.2h FlowRecord` that traces identification → screening → eligibility → included at a minimum granularity sufficient to reproduce the corpus boundary.                                                                                                                                                         | Prevents “mystery inclusion” and supports refresh.                                  |
| **CC-G2-ClaimSheets-1** | For each included `Tradition`, the pack MUST include a `ClaimSheetId` naming exact sources and editions, claim regions, effective schemes where meaning matters, EntitiesOfConcern, comparison bases, evidence anchors, freshness notes, and intended use; it MUST NOT fuse cross-`Tradition` claims by default. | Keeps plurality and provenance explicit without a Context container. |
| **CC‑G2‑Palette‑1**       | A conforming pack **MUST** export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as citable views (via `SoTA_SetId`, `SoTAPaletteDescriptionId`) and ensure both are reconstructible from pack components by id (no hidden extra structure).                                                                                                      | Prevents downstream scraping of prose; keeps “M2 output” explicit.                  |
| **CC‑G2‑Palette‑2**       | If the pack exports one derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep `SoTAPaletteDescription` explicit as the default base palette, keep that derivation recoverable, and cite the declared `Q` or reachability/coverage rule that disciplined that view. Derived tradition views **MUST NOT** silently replace the palette's default meaning. | Keeps non-default tradition views recoverable without redefining palette-first semantics. |
| **CC‑G2‑AtlasInterpretation‑1**  | If the pack exports `TraditionAtlasView`, it **MUST** satisfy the same interpretive-view declaration required by `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`: keep the base palette and active source set or active set result recoverable, name `TypedSetViews` when several declared set views are held together, cite any active `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space refs, cite any active `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, or `BridgeDistortionNote` only when they do real explanatory work, state why thinner `DeclaredSubstrateInterpretiveView` is insufficient here, and **MUST NOT** use atlas form when palette-first or thinner `DeclaredSubstrateInterpretiveView` is sufficient. | Keeps the `G.2` specialization at least as constraining as the general `DeclaredSubstrateAtlasView` declaration and preserves space-role recoverability. |
| **CC‑G2‑entityOfConcernMap‑1** | A conforming pack **MUST** include `G.2g entityOfConcern Map`, mapping (at minimum) each load‑bearing claim family and each minted/evolved public id to `entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩`, and citing the relevant `ClaimSheetId` and evidence anchors (A.10 and/or G.6 paths when used).                                         | Keeps plane/holon boundaries explicit and citable.                                  |
| **CC‑G2‑Alignment‑1**     | Any cross‑`Tradition` consolidation **SHALL** be presented as either (i) disjoint parallel claims with explicit divergence, or (ii) an explicitly justified alignment proof; any reuse across `Tradition` boundaries **MUST** use explicit crossing bundles per `CC‑GCORE‑CROSS‑1` (delegation).                                                  | Prevents silent semantic leakage.                                                   |
| **CC‑G2‑GammaSynth‑1**    | If the pack asserts **fusion or substitution** across sources or across `Tradition` records (not merely “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records satisfying `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit alignment refs + assurance tuple refs). If no fusion or substitution is asserted, the pack **SHALL** state so explicitly. | Restores the load‑bearing synthesis artefact (alias: `G.2‑F`) without shadow specs. |
| **CC‑G2‑Inventory‑1**     | A conforming pack **MUST** include `G.2c OperatorAndObjectInventory`, sufficient for downstream CHR/CAL authoring to begin without re‑harvesting terms.                                                                                                                                                                                            | Ensures the pack is actionable.                                                     |
| **CC‑G2‑Inventory‑2**     | `G.2c OperatorAndObjectInventory` entries **MUST** be treated as **stubs** for downstream authoring: they **MUST NOT** embed acceptance thresholds or claim legality decisions locally. If an entry is not a citation of an already governed CHR/CAL artefact, it **MUST** be explicitly marked as `stub` (typing/lawfulness `TBD`) and **MUST NOT** be used as if lawful. Legality/threshold semantics are governed by `G.3` for CHR and `G.4` for CAL via explicit ids/pins. | Prevents “shadow CHR/CAL” and preserves lawfulness discipline without redefining it locally. |
| **CC‑G2‑MeasurementLawful‑1** | If any inventory entry is presented as **non‑stub** (i.e., already lawful/typed), the pack **MUST** cite the governing lawfulness discipline (e.g., `A.17–A.19/C.16` as applicable) and provide the minimal evidence anchors needed to justify that typing claim.                                                                                      | Prevents “quietly lawful” measurement claims inside the harvester pack.             |
| **CC-G2-MicroExamples-1** | For every load-bearing claim family, a conforming pack MUST include at least two worked micro-examples on heterogeneous substrates. Each names the source and edition, claim region, EntityOfConcern, comparison basis, and intended use; cites its A.10 carrier or evidence path; and gives an applicable assurance tag. | Makes the synthesis teachable and inspectable; the example form supplies no meaning or authority. |
| **CC‑G2‑UTS‑1**           | If the pack proposes or evolves any public ids, it **MUST** publish UTS proposals *(Name Cards + MDS where applicable)* and cite them via `UTSRowId[]`, satisfying `CC‑GCORE‑UTS‑1` (delegation).                                                                                                                                               | Keeps naming and evolution disciplined.                                             |
| **CC‑G2‑Families‑1**      | SoS indicators and candidate evaluation constructs **SHALL** be represented as **families/variants** (windows/constraints/assumptions) **with explicit Acceptance branch structure per variant** (branch ids/labels only), not as single unqualified scalars; any scalar summary **MAY** be included only as report‑only unless explicitly promoted by governing patterns. *(Set-return discipline is delegated to `CC‑GCORE‑SET‑1`.)* | Prevents covert scalarization and keeps acceptance governed by downstream patterns.                |
| **CC‑G2‑HandOff‑1**       | A conforming pack **MUST** emit hand‑off manifests to `G.3`, `G.4`, and `G.5` that cite pack components by id and identify which families/operators are intended for downstream formalisation or registry entry.                                                                                                                                   | Prevents downstream re‑authoring and drift.                                         |
| **CC‑G2‑CoverageGate‑1**  | The pack **MUST** declare `FamilyCoverageFloorK` and enforce it as a harvesting gate. It **MUST** either (i) specify `k` explicitly in an explicit `HarvestPolicyRef`, or (ii) use the pattern‑local default rule governed by `CC‑G2‑CoverageGate‑1`. *Default rule (pattern-local):* `k=3`. If the gate fails, the pack **MUST** (a) record the repair iteration in `FlowRecord`, and (b) broaden the search radius (new venues/corpora/contexts/traditions) rather than silently weakening the gate; if an exploration policy is used for this broadening, it **MUST** be pinned as a policy id/ref. | Makes “coverage floor” explicit and prevents “silent narrowing” under failure.      |
| **CC‑G2‑DistanceGate‑1**  | If a diversity‑by‑distance gate is used, the pack **MUST** pin `DistanceDefRef.edition` and the declared threshold (δ), and treat edits as RSCR‑relevant per `CC‑GCORE‑TRIG‑*` (delegation). If no such gate is used, the pack **SHALL** explicitly state that it is not used.                                                                     | Avoids implicit distance defaults and improves refreshability.                      |
| **CC‑G2‑RSCR‑1**          | A conforming pack **MUST** emit canonical `RSCRTriggerKindId` causes (not free text) for edits to evidence surfaces, name/tokenization surfaces (e.g., UTS proposals/aliases), crossings, planes, edition pins, and harvesting policy pins (`HarvestPolicyRef`), per `CC‑GCORE‑TRIG‑1…TRIG‑4` (delegation).                                                                                      | Keeps refresh reason codes stable and typed.                                        |
| **CC‑G2‑Ext‑GammaEpist‑1** | If `G.2:Ext.GammaEpistSynthesis` is used (i.e., any fusion/substitution is asserted), the pack **SHALL** expose the required pins listed in that extension and **SHALL NOT** redefine `Γ‑fold/Φ/penalty` semantics locally (cite governing definitions by delegation).                                                                                       | Keeps synthesis auditable without creating shadow specs.                            |
| **CC‑G2‑Ext‑HarvestProtocols‑1** | If `G.2:Ext.HarvestProtocols` is used, the pack **SHALL** expose the required pins/criteria ids listed in that extension and **SHALL NOT** redefine evidence/quality semantics outside the declared protocol profile.                                                                                                                            | Keeps protocol variation explicit and separately citable.                           |
| **CC-G2-Ext-DHC-1** | If `G.2:Ext.DHCAlignmentHooks` is used, the pack SHALL expose the DHC method edition, exact F.17 cell comparison set, exact F.9 relation refs actually counted, evidence paths, and C.21 unit and constraint pins such as `bridges_per_100_cells` and `CL_min=2`, without redefining them locally. | Keeps DHC counts tied to named cells and obtaining relations. |
| **CC‑G2‑Ext‑NQD‑1**       | If `G.2:Ext.NQDAnnex` is used, the pack **SHALL** expose the required pins/editions/policies listed in that extension and **SHALL NOT** redefine QD semantics locally.                                                                                                                                                                             | Keeps QD/OEE extension pins replayable and non‑shadowing.                          |
| **CC‑G2‑Ext‑Interop‑1**   | If `G.2:Ext.InteropForms` is used, the pack **SHALL** expose the required interop pins and **SHALL NOT** introduce alternative legality/acceptance semantics.                                                                                                                                                                                      | Prevents “foreign gate” shadowing.                                                  |

