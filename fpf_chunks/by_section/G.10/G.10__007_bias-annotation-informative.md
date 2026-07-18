---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:6"
section_title: "Bias‑Annotation (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__007_bias-annotation-informative.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:6 — Bias‑Annotation (informative)"
line_start: 96153
line_end: 96165
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

### G.10:6 - Bias‑Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Format bias (Arch/Prag).** A popular export format is tempting to treat as “the pack”.
  *Mitigation:* keep Core surfaces conceptual (E.5.2); move serialisation recipes to Annex/Interop; keep conformance on semantics.
* **Centralisation bias (Gov).** A single pattern governing shipping semantics can become a bottleneck.
  *Mitigation:* keep shipping as one explicit governing-pattern responsibility, but push mode/method specifics into explicit `G.10:Ext.*` extension blocks and cite governing patterns.
* **Telemetry→dominance bias (Onto/Prag).** Shipping pipelines often “promote” telemetry proxies (illumination/coverage) into ranking.
  *Mitigation:* preserve the telemetry/order separation and require explicit CAL policy‑id for any promotion; record the policy‑id in audit pins/telemetry.
* **Interop authority bias (Onto/Epist).** External indexes can silently override local legality/typing.
  *Mitigation:* `G.10‑6` ingests interop only as cited notes (editions + mapping policy refs), never as a replacement governing spec ref.

