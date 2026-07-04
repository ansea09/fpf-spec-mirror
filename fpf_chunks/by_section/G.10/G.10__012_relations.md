---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:9"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__012_relations.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:9 — Relations"
line_start: 92941
line_end: 92946
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

### G.10:9 - Relations

**Builds on:** `G.Core`; consumes/cites artefacts governed by cited patterns from `G.2` (harvest pack), `G.3` (CHR pack), `G.4` (CAL pack), `G.6` (EvidenceGraph), `G.7` (bridge calibration), `G.8` (SoS‑LOG bundle), `G.9` (parity report), optional `G.12` (dashboard slice), optional `G.13` (interop surface).
**Publishes to / used by:** UTS (pack identity), selector‑facing consumers (via `G.5`), audit and assurance publications (SCR/RSCR), refresh orchestration (`G.11`).
**Constrains:** tooling exports are downstream; serialisation and repository integration are explicitly non‑normative here.

