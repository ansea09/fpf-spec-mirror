---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:2"
section_title: "Problem — Failures of reuse, legality and refresh"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__003_problem-failures-of-reuse-legality-and-refresh.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:2 — Problem — Failures of reuse, legality and refresh"
line_start: 129520
line_end: 129530
dependencies:
  - "A.10"
  - "A.15.3"
  - "C.18"
  - "C.21"
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

### G.10:2 - Problem — Failures of reuse, legality and refresh

Shipping fails when:

1. **Format-as-governing-spec.** A concrete export format is treated as “the pack,” turning a tool choice into a governing pack definition.
2. **Editionless hand‑offs.** Shipped artefacts omit the edition/policy pins required to replay or compare outcomes, so parity and RSCR become non‑actionable.
3. **Shipping changes the rules.** The pack adds local rules (hidden scalarisation, competing defaults, private gate decisions), fragmenting the governing spec ref.
4. **Invisible crossings.** An actual correspondence, flow crossing or gate lacks the grounds, bundle anchors or policy pins required for its receiving use.
5. **No method‑of‑obtaining‑output disclosure.** Consumers receive outcomes without a minimal, citable trail of *which methods, mechanisms, and policies were used, at which editions, to obtain them*.
6. **Refresh orphaning.** Telemetry and decay signals exist, but the shipped artefact provides no stable scope keys (`PathId` / `PathSliceId`) and no payload pins for RSCR triggers.

