---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:4"
section_title: "Solution — Discipline Health Characterisation (DHC)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__006_solution-discipline-health-characterisation-dhc.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:4 — Solution — Discipline Health Characterisation (DHC)"
line_start: 49276
line_end: 49355
dependencies:
  - "A.10"
  - "A.17"
  - "A.17-A.18"
  - "A.18"
  - "A.19"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.2.1"
  - "C.20"
  - "C.I"
  - "E.24.PUB"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "alignment"
  - "discipline"
  - "disruption"
  - "field health"
  - "reproducibility"
  - "standardisation"
---

### C.21:4 - Solution — Discipline Health Characterisation (DHC)

#### C.21:4.0 - The objects used by DHC

“DHC” names this vocabulary and method of use. It does not admit `U.DHCPack`, `U.DHCMethodSpec`, or `U.DHCSeries` as public kinds.

| Object | What it is | What it is not |
| --- | --- | --- |
| DHC Characteristic and Scale declarations | Exact A.17 Characteristic and A.18 Scale definitions, with Unit and polarity when applicable. | A dashboard field or a health verdict. |
| `DHCDefinitionSet` when a reusable selection is needed | One C.2.1 episteme about the already identified discipline. Its ClaimGraph states the intended use and selects exact Characteristic, Scale, Unit, and measurement-definition editions. | A slot-set kind, the discipline, or a publication. Ordinary one-coordinate use needs no such episteme. |
| `DHCMethodRef.edition` | The existing C.16 measurement-definition value for one Characteristic and Scale. It resolves the exact `U.Method`, any `U.MethodDescription` edition, model, calibration basis, uncertainty treatment, construction, and time or population policy used by the reading. | The Method, MethodDescription, measurement Work, or result. |
| DHC coordinate result | A C.16 measurement result and, when persisted as a claim, one C.2.1 result episteme about the discipline. | A time-series publication, dashboard row, or acceptance decision. |
| `DHCSeries` when repeated use needs one | One C.2.1 episteme whose EntityOfConcern is the discipline and whose ClaimGraph orders exact coordinate-result episteme refs by window under one intended use, ClaimScope, comparison basis, and definition basis. Content change creates another episteme edition under the applicable edition rule. | A publication occurrence, form, carrier, table, or the Work that assembled it. |
| dashboard row or slice | A C.29 or G.12 representation over exact result or series refs. | The result, evidence, series episteme, publication, or discipline. |
| publication occurrence | An obtaining E.24.PUB availability relation among one selected episteme edition, audience declaration, bounded-use declaration, form, carrier, and availability interval. | Rendering, upload, release, measurement, or series-assembly Work. |

Rendering, measuring, assembling a series, uploading, and maintaining availability may each be Work when actually performed. A work record or carrier does not make that Work occur.

#### C.21:4.0a - One replay basis for every persisted coordinate

Every persisted, compared, aggregated, or published coordinate makes the following values recoverable. This is a field group, not another public kind:

`DHCReplayBasis := <DisciplineRef, IntendedUse, ClaimScopeRef, ComparisonBasis, CharacteristicRef.edition, ScaleRef.edition, UnitRef.edition?, DHCMethodRef.edition, MethodRef, MethodDescriptionRef.edition?, MeasurementModelRef.edition?, CalibrationBasisRef?, TimeOrPopulationBasis, DHCDefinitionSetRef.edition?, TargetSliceRef?, DistanceDefRef.edition?>`

- `DHCMethodRef.edition` resolves the same Characteristic, Scale, Method, MethodDescription, model, calibration, and uncertainty semantics named by the active fields. A mismatch is not repaired by choosing one field as “primary.”
- `DHCDefinitionSetRef.edition` appears only when a named reusable definition selection exists.
- `TargetSliceRef` appears only when the named computation or publication actually consumes an A.2.6 selection. Every selected slice must be shown to belong to, or otherwise be covered by, the authoritative `ClaimScope`; the slice never substitutes for that scope.
- `DistanceDefRef.edition` appears only when the Scale comparison or target-distance rule uses a separately declared distance.
- Evidence paths, lane tags, currentness, assurance, acceptance, public names, and publication refs are added only when the receiving use consumes those separate results.

#### C.21:4.1 - Portable Characteristics

Each bullet below names one exact Characteristic and Scale family. A DHC use selects only the coordinates needed by its question.

1. **ReproducibilityRate** — ratio in `[0,1]`; Unit `replicated_claims/tested_claims`; polarity higher-is-more-reproducible, not “healthier in every respect.” Declare the tested claim or benchmark population, independent-team condition, protocol, corpus or cohort, and time window.

2. **FormalRecognitionStatus** — nominal by default. Values such as `none`, `draft`, `approved`, `withdrawn`, or another lifecycle vocabulary belong to one named standards body and exact status scheme. Use an ordinal only when that scheme itself supplies a lawful order. There is no general `de facto < de jure` ladder and no default health polarity.

3. **PracticeAdoptionRate** — ratio in `[0,1]`; Unit `adopting_units/eligible_units`. Declare the population, adoption criterion, observation window, and treatment of partial adoption. Higher means wider observed adoption, not automatically better health or SoTA.

4. **AlignmentDensity** — ratio; Unit `obtaining_relations/100_compared_cells`. Count only exact obtaining F.9 relations in the declared F.17 cell set. Each counted relation has direction, admitted use, and loss. A higher value means denser declared alignment for that set; any health band belongs to G.4.

5. **DisruptionBalance** — interval reading over one exact disruption/consolidation method and corpus. Polarity is target-is-best, using an explicit target-band distance rule; the band belongs to G.4 Acceptance.

6. **EvidenceUnitResolution** — ordinal, compare-only, under one exact segmentation scheme whose levels are nested, for example `artifact < section < claim < subclaim`. Higher means a finer addressable unit under that scheme. It does not say how many claims an artifact contains or how densely claims are supported.

7. **ClaimsPerArtifact** — ratio; Unit `claims/artifact`, with exact claim segmentation and artifact population. It measures claim breadth or packing, not support density. Declare a target band when the use needs one; no universal monotone health polarity applies.

8. **SupportAnchorsPerClaim** — ratio; Unit `anchors/claim`, with exact anchor admissibility and claim segmentation. It measures support-anchor density, not claim size. It has no universal monotone health polarity.

9. **TraditionShareEntropy** — one exact entropy Characteristic and Scale, with log base, normalization, category set, and population fixed. Higher entropy means greater dispersion on that scale. Any desired band is separate.

10. **TraditionShareConcentration** — HHI or another exact concentration Characteristic, normally ratio in `[0,1]`; higher HHI means greater concentration and therefore lower dispersion. Do not place it in the entropy field. `1 - HHI` may be introduced only as an explicit transformation to a separately declared receiving Scale. Comparing that result with normalized entropy still requires an explicit common comparison rule.

#### C.21:4.1a - Engineering-grade extension Characteristics

A discipline-health use may add these coordinates when its question needs them. They do not become evidence, assurance, gate, release, Work, or project-authority results.

11. **EngineeringClaimJustificationRecoverability** — ordinal, polarity higher-is-more-recoverable. It asks whether the exact construction, source, model, lens, or relation carrying an engineering claim's force can be recovered for the intended use. The reading cites the direct pattern and rule that define or constrain that force.

12. **SemioSubstitutionPressure** — ordinal or ratio as separately declared, polarity lower-is-less-substitution-pressure. It asks how often a representation, fluent wording, record, dashboard, view, or source chain is mistaken for its engineering subject, relation, or claim.

When either extension is active, add a short explanation naming the current claim kind or use boundary, the direct pattern and rule, admissible use, prohibited overread, and stop or reopen condition. The explanation is claim content, not a new evidence or assurance object.

#### C.21:4.2 - Comparison and legality rules

1. **Direct same-semantics comparison.** Compare readings directly when C.16's conservative conditions hold: the same measurement definition, Characteristic, Scale and Unit semantics, compatible model and calibration regime, and compatible time or population basis. Record the admitted comparison basis. Different source labels or editions alone require no Bridge.
2. **Cross-local comparison.** When the use actually relates distinct F.17 local senses, additionally cite the exact obtaining F.9 relation, direction, admitted use, and loss. Any justified consequence affects R only. The relation supplies none of ClaimScope, measurement, comparison, or acceptance semantics.
3. **Reference-plane crossing.** When a reading is used across distinct world, concept, or episteme planes, cite the exact crossing basis. Any assurance consequence affects R only. A dashboard row or source label does not establish the crossing.
4. **Cross-scale transformation.** A conversion, normalization, distance, or aggregate names its exact Method, Scale, legal operation, and loss or uncertainty. No common scale is inferred from similar labels.
5. **Freshness.** A persisted or reused coordinate carries its observation window and applicable currentness rule. Staleness leads to the receiving pattern's degrade, abstain, or reopen result; it does not rewrite the historical measurement.
6. **Target bands.** “Target-is-best” is not “higher-is-better.” A comparison to a band uses an explicit distance-to-band rule and leaves the G.4 threshold separate.
| Scale family | Lawful ordinary operations | Prohibited shortcut |
| --- | --- | --- |
| nominal status | equality, membership, mode when justified | lifecycle ranking or arithmetic without an ordered scheme |
| ordinal resolution | order, median or mode where meaningful | mean, ratio, or affine arithmetic |
| ratio rate or density | operations allowed by its exact Scale and Unit | unit mixing or comparison across changed construction |
| interval balance | differences and target distance under its exact rule | ratios or silent target-band polarity |
| entropy and concentration | operations under their own definitions | treating entropy and HHI as interchangeable or equally directed |

