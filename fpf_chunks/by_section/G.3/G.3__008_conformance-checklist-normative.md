---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__008_conformance-checklist-normative.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:7 — Conformance Checklist (normative)"
line_start: 136643
line_end: 136666
dependencies:
  - "A.10"
  - "A.15.2"
  - "A.15.3"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CHR"
  - "B.3"
  - "B.3.4"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "E.10"
  - "E.5.1"
  - "E.5.3"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.Core"
keywords:
  - "CHR Pack@CG-Frame"
  - "CHR authoring"
  - "CSLC lawfulness"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "characteristics"
  - "coordinates"
  - "edition pins"
  - "levels"
  - "scales"
  - "typed measurement"
  - "Φ/CL policy pins"
---

### G.3:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G3‑CoreRef** | `G.3` is conformant only if the applicable `G.Core` obligations declared in `G.3:4.1` are satisfied (effective expansion of profiles/sets + deltas; explicit pins; typed RSCR triggers; defaults with one governing definition).                       |
| CC‑G3‑01          | `CHR Pack@CG‑Frame` is published as a notation‑independent kit payload with the minimum exported objects listed in `G.3:4.2`.                                                                                                         |
| CC-G3-02 | Every `CHR.Characteristic` names its exact characteristic and scale editions, its bearer as the `entityOfConcern`, claim scope and applicable slices, any applicable qualification and evaluation windows, `ReferencePlane`, method or model edition when it affects interpretation, evidence refs, intended downstream use, and a filled `ObservableOf` field (instrument or determination protocol, uncertainty treatment when it affects interpretation or use, and any temporal basis consumed by the definition or receiving use). |
| CC‑G3‑03          | Every `CHR.Characteristic` declares its `ScaleRef`, `Polarity`, and `UnitSet` (or an explicit “unitless” declaration), plus bounds/zero semantics where applicable.                                                                   |
| CC‑G3‑04          | Missingness is typed in the CHR artefacts such that downstream tri‑state handling is possible without silent coercion. *(Tri‑state semantics are governed by `G.Core`; the typing obligation is CHR‑local.)*                              |
| CC‑G3‑05          | `CHR.Scale` / `CHR.Level` artefacts encode the scale type and admissible transforms, and make illicit arithmetic checkable by downstream consumers.                                                                                   |
| CC‑G3‑06          | Any published `CHR.Coordinate` includes a `CoordinatePolicy` that states preserved invariants and explicit non‑entitlements; coordinates do not silently upgrade measurement structure.                                               |
| CC‑G3‑07          | `CHR.LegalityMatrix` and `CHR.Guards` exist and are referenced by downstream operator authoring; semantics are governed by cited definitions (MM‑CHR and `G.Core`), not duplicated locally.                                                        |
| CC‑G3‑08          | `CHR.AggregationSpecs` are typed and legality‑constrained; where Γ‑fold is required and no explicit override is pinned, cite `DefaultId.GammaFoldForR_eff` through `G.Core.DefaultGoverningDefinitionIndex`. |
| CC‑G3‑09          | If any characteristic is intended for promotion into `CG‑Spec`, the linkage is explicit and edition‑pinned (no shadow ids). *(Governing definition: `G.0`; wiring via `G.3:Ext.CGSpecPromotionWiring`.)*                                             |
| CC‑G3‑10          | UTS Name Cards exist for public ids minted or evolved by the CHR pack (designations under F.17/F.18 plus public-id continuity notes). *(Delegation target: `CC‑GCORE‑UTS‑1` via `CC‑G3‑CoreRef`.)*                                                                      |
| CC‑G3‑11 | Worked examples and RSCR tests retain their source, proof or measurement basis, with G.6 path citations when used or required. They cover illegal-operation refusal, unit and scale constraints, polarity invariants and coordinate non-entitlements. |
| CC‑G3‑12          | Thresholds/guard‑bands are not embedded in CHR artefacts; they remain governed by CAL acceptance clauses (`G.4`).                                                                                                                        |
| CC‑G3‑13          | When method‑role declarations are present (via `RoleDecls` and/or `QD.Role` alias), each declaration is **docked** to its governing pattern via a corresponding `G.3:Ext.*` module, and the edition and policy pins required by the governing pattern are surfaced to make downstream interpretation reproducible. *(QD/OEE governing patterns: `C.18` and `C.19`; wiring via `G.3:Ext.QD_OEE_Wiring`.)* |
| CC‑G3‑14 | **Evidence wired.** Each `CHR.Characteristic` cites the grounds of its legality and guard claims through A.10 source/carrier references, or G.6 paths when shared path citation or a receiving contract requires them. The chosen representation preserves the actual claim and support relations. |
| CC‑G3‑15          | An `Archetypal Grounding` section exists with at least two domain‑distinct examples that demonstrate lawful CHR typing/legality and the CHR↔CAL separation (notably: no thresholds in CHR).                                          |
| CC‑G3‑16 | If `EvidenceLanes` are used, declare their tags with the selected regime’s definitions and pin any lane-dependent tolerances/proof requirements. Cross-lane comparison or aggregation requires both a governing policy that permits the use (typically `G.4`) and grounds for the operation on these measurements. Cite both, with G.6 paths when used or required. |
| CC‑G3‑17          | When CHR outputs are bound into a planned baseline, identify the `A.15.2` WorkPlan and its local baseline locator. If the plan fills an independently declared operation argument or relation position under `A.15.3`, also use `CHRMechanismSuiteSlotFillingsPlanItem` with its governing declaration reference, member designator and plan-local filling-row locator, as governed by `A.19.CHR:4.1.2` (wiring via `G.3:Ext.SuiteBoundaryLinkage`). |
| CC‑G3‑18 | **Use-qualified currentness.** A claim whose receiving use depends on currentness retains its B.3.4 basis and any applicable validity window or decay policy. Named models/policies are pinned through `G.3:Ext.DecayWiring`. Changes to relied-on windows, policies or other support conditions participate in RSCR under `G.3:4.1`. |

