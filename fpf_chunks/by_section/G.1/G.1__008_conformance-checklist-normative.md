---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "CG‑Frame‑Ready Generator"
section_id: "G.1:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__008_conformance-checklist-normative.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "G.1 — CG‑Frame‑Ready Generator"
  - "G.1:7 — Conformance Checklist (normative)"
line_start: 101940
line_end: 101953
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.19"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.Core"
keywords:
  - "CGFrameLibraryId"
  - "CGKitId manifest"
  - "RSCR linkage surfaces"
  - "RefreshReadinessCardId"
  - "ShortlistId"
  - "SoTA_SetId"
  - "UTS/Name Cards"
  - "VariantPoolId"
  - "and set-result scaffold"
  - "edition pins"
  - "generator"
  - "generator chassis"
  - "selector"
  - "set-result outcome"
  - "set-return selection"
  - "shipping and refresh boundaries"
  - "six-card kit (M1-M6)"
---

### G.1:7 - Conformance Checklist (normative)

| ConformanceId     | Statement   |
| ----------------- | ----------- |
| **CC‑G1‑CoreRef** | The pattern MUST satisfy the **effective** `CoreConformanceIds` implied by `G.1:4.1` (`GCoreConformanceProfileId` expansion + deltas), per `G.Core` expansion rules.   |
| CC‑G1‑01          | The reusable CG-Frame kit MUST include all six cards `M1…M6` with stable ids **and** a versioned kit manifest `CGKitId`, including at minimum: `{CGKitId, CG‑FrameContext, SoTAPaletteDescriptionId, SoTA_SetId, VariantPoolId, ShortlistId, CGFrameLibraryId, RefreshReadinessCardId}`.  |
| CC‑G1‑02          | `M1` MUST bind the kit to a single `CG‑FrameContext` and MUST expose the required pins from `GCorePinSetId.PartG.AuthoringMinimal` (including `entityOfConcern` and `CNSpecRef/CGSpecRef` editions). `M1` MUST also expose (or explicitly cite) a `ReferenceMap` surface and MUST NOT restate its semantics (cite `G.0:CG‑Spec.ReferenceMap`).  |
| CC‑G1‑03          | `M2` MUST be wired to `G.2` (or explicitly cite the `G.2` artefacts governed by cited patterns) and MUST be reconstructible as a scoped set, including `SoTAPaletteDescriptionId` + `SoTA_SetId` (not free‑floating prose). Provenance MUST be anchored via `A.10` for the emitted set.  |
| CC‑G1‑04          | `M3` MUST record emitter provenance as a wiring surface, including `EmitterPolicyRef` (policy‑id/ref), edition pins, and provenance anchors (via `A.10`). Any method‑specific fields MUST be introduced only via `GPatternExtension` blocks.   |
| CC‑G1‑05          | `M4` MUST be wired to `G.5` (or explicitly cite `G.5` artefacts governed by cited patterns) and MUST preserve set-result outcomes. `SCRId` MUST be present (or explicitly cited to the governing definition surface) so assurance is id‑addressable; `DRRId` SHOULD be present when a decision‑rationale artefact is minted.   |
| CC‑G1‑06          | `M5` MUST publish a library/index surface that points to referenced CHR/CAL/LOG artefacts and to any minted public ids (`UTSRowId[]`, Name Cards) via the canonical governing definitions (Part F), without introducing shadow specs (delegation target: `CC‑GCORE‑CN‑CG‑1` via `CC‑G1‑CoreRef`).    |
| CC‑G1‑07          | `M6` MUST publish `CGKitId` and expose refresh‑readiness wiring: canonical `RSCRTriggerKindId[]` applicability + minimal payload pins (including `SlotFillingsPlanItemRef[]` when applicable) and RSCR test ids; orchestration semantics MUST be cited to `G.11`.  |
| CC‑G1‑08          | Any method/discipline/generator specificity in `G.1` MUST be located in `G.1:4.4` as `GPatternExtension` blocks with `PatternScopeId`, `GPatternExtensionKind`, and `GoverningPatternId` (or `governing pattern not yet selected` only for Phase-3 seeds). If QD/illumination or Open‑Ended generator families are declared, the corresponding extension blocks MUST be present and MUST carry the edition and policy pins required by the governing pattern. |

