---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:2"
section_title: "Problem — Why naive shipping breaks reuse, legality, and refresh"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__003_problem-why-naive-shipping-breaks-reuse-legality-and-refresh.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:2 — Problem — Why naive shipping breaks reuse, legality, and refresh"
line_start: 81082
line_end: 81092
dependencies:
  - "A.10"
  - "A.15.3"
  - "C.18"
  - "E.18"
  - "E.5.2"
  - "F.17-F.18"
  - "G.11"
  - "G.12"
  - "G.12-G.13"
  - "G.13"
  - "G.2"
  - "G.2-G.9"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "AuditPins"
  - "CrossingBundle"
  - "MOOManifest"
  - "PathId/PathSliceId"
  - "PortfolioRosterId"
  - "RSCR wiring"
  - "SoTA-Pack(Core)"
  - "UTS publication"
  - "edition pins"
  - "no semantic respecification"
  - "notation-independent pack"
  - "pack-boundary governing definition"
  - "parity pins"
  - "selector-ready publication surface"
  - "shipping"
  - "telemetry pins"
---

### G.10:2 - Problem — Why naive shipping breaks reuse, legality, and refresh

Naive shipping fails (conceptually) when any of the following occurs:

1. **Format-as-governing-spec.** A concrete export format is treated as “the pack,” turning a tool choice into a governing pack definition.
2. **Editionless hand‑offs.** Shipped artefacts omit the edition/policy pins required to replay or compare outcomes, so parity and RSCR become non‑actionable.
3. **Pack smuggles semantics.** Shipping reintroduces “convenience” rules (hidden scalarisation, competing defaults, private gate decisions), fragmenting the governing spec ref.
4. **Invisible crossings.** Cross-context or cross-plane reuse is present, but the pack does not expose the crossing bundles and penalty policy pins needed for audit and refresh planning.
5. **No method‑of‑obtaining‑output disclosure.** Consumers receive outcomes without a minimal, citable trail of *which mechanisms/policies/editions produced them*.
6. **Refresh orphaning.** Telemetry and decay signals exist, but the shipped artefact provides no stable scope keys (`PathId` / `PathSliceId`) and no payload pins for RSCR triggers.

