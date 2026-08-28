---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:8"
section_title: "Conformance Checklist (CC‑G13; applies when G.13 surfaces are used)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__009_conformance-checklist-cc-g13-applies-when-g-13-surfaces-are-used.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:8 — Conformance Checklist (CC‑G13; applies when G.13 surfaces are used)"
line_start: 105527
line_end: 105559
dependencies:
  - "A.18"
  - "A.19"
  - "E.10"
  - "E.18"
  - "E.5.2"
  - "F.17"
  - "G.0"
  - "G.12"
  - "G.13"
  - "G.2"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CHR-typed SoS features"
  - "ClaimMapperCard@Context"
  - "ExternalIndexCard@Context"
  - "InteropSurface@Context"
  - "RSCRTriggerKindId"
  - "UTS twins"
  - "claim mapper"
  - "edition pins"
  - "embedding spec"
  - "external index"
  - "interop"
  - "mapping policy"
  - "plane map"
  - "telemetry pin"
---

### G.13:8 - Conformance Checklist (CC‑G13; applies when G.13 surfaces are used)

1. **CC‑G13‑CoreRef.** *(normative)* `G.13` implementations **MUST** satisfy the *effective* `G.Core` obligations declared by `G.13:4.1` (`GCoreLinkageManifest`), including trigger typing, Default Governing Definition Index citation, and crossing‑visibility pin discipline.

2. **CC‑G13‑InteropIsNotASpecRefSurface.** *(delegated)* Interop surfaces **MUST NOT** introduce shadow legality/comparability gates; they cite `CN‑Spec`/`CG‑Spec`/CHR/CAL governing definitions and publish pins instead.
   → delegate to `CC‑GCORE‑CN‑CG‑1`.

3. **CC‑G13‑CrossingsAreExplicitWhenInteropTouchesPlanesOrContexts.** *(delegated)* Any cross‑plane/context reuse implied by alignment **MUST** be made explicit through the crossing visibility discipline.
   → delegate to `CC‑GCORE‑CROSS‑1`.

4. **CC-G13-PlanePenaltyPoliciesArePinned.** *(local; governing-definition citing)* If `PlaneMapRef` is used (or alignment implies plane‑level penalties), interop surfaces **MUST** publish the relevant policy‑id pins via the crossing‑visibility discipline, and any such policies **MUST** satisfy the constraints governed by `CG‑Spec` (cite `CC‑G0‑Φ`). Interop surfaces **MUST NOT** define interop‑local penalty functions.

5. **CC‑G13‑SetReturnPreserved.** *(delegated)* Interop **MUST NOT** introduce hidden scalarisation or forced single‑winner selection.
   → delegate to `CC‑GCORE‑SET‑1`.

6. **CC‑G13‑DefaultClaimsAreCitationsOnly.** *(delegated)* Any mention of defaults (e.g., dominance regime, `PortfolioMode`) is a **citation** to the default's governing definition through `G.Core.DefaultGoverningDefinitionIndex`, not a local default statement.
   → delegate to `CC‑GCORE‑DEF‑1`.

7. **CC‑G13‑EditionDisciplineForInteropCards.** *(local)* `ExternalIndexCard@Context` and `ClaimMapperCard@Context` **MUST** expose edition pins (`ExternalIndexRef.edition`, `ClaimMapperRef.edition`). Any interop surface published to UTS **MUST** cite the relevant `…Ref.edition` values (incl. `PlaneMapRef.edition?`, `ScaleEmbeddingSpecRef.edition?`) when present.
   FPF edition keys **MUST** appear only on `…Ref.edition` pins when a reference is present. Provider snapshot labels (e.g., `ExternalEdition` on `ExternalIndexCard@Context`) may exist on the source card, but **MUST NOT** be copied into downstream artefacts as free‑floating “edition fields”; downstream artefacts cite the corresponding `…Ref.edition` pins instead.
   In particular, interop transforms **MUST NOT** perform illicit arithmetic on ordinal/compare‑only scales (e.g., averaging or subtraction); any aggregation must be via lawful CAL operators with explicit scale legality (cite `A.18` / `CC‑G0‑CSLC`).

8. **CC‑G13‑SoSFeaturesAreCHRTypedAndLegal.** *(local; governing-definition citing)* If `SoSFeatureTransform@Context` is used, produced SoS features **MUST** be CHR‑typed via `FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}` (governed by `G.3`) and any legality/units obligations must be satisfied via CSLC/CG governing definitions (cite `A.18` / `G.0` / `G.4`; do not invent interop‑local legality gates).

9. **CC‑G13‑TelemetryEmitsCanonicalTriggerKinds.** *(delegated)* Interop‑driven changes (external edition bumps, mapping policy changes, plane‑map edits, embedding‑spec edits) **MUST** emit canonical `RSCRTriggerKindId` causes with explicit scope and payload pins.
   → delegate to `CC‑GCORE‑TRIG‑1`, `CC‑GCORE‑TRIG‑2`, `CC‑GCORE‑TRIG‑3`, `CC‑GCORE‑TRIG‑4`.

10. **CC‑G13‑IDContinuityForExternallySourcedIdentifiers.** *(delegated)* Interop publication **MUST** follow Δ‑discipline: no “renaming by meaning”; use aliases/deprecations as required.
    → delegate to `CC‑GCORE‑ID‑1`, `CC‑GCORE‑ID‑2`.

11. **CC‑G13‑NotationIndependence.** *(local)* Conformance is judged on the conceptual objects in `G.13:4.2`. Any serialisation is non‑normative and must not redefine semantics.
   *(Cites `E.5.2` for notation independence.)*

