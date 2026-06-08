---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__001_intro.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:intro — Intro"
line_start: 79321
line_end: 79328
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.5"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G6"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

## G.6 - Evidence Graph & Provenance Ledger

**Tag.** Architectural pattern
**Stage.** design‑time (assembly) + run‑time (telemetry ingestion)
**Primary output.** A notation‑independent `EvidenceGraph` + a stable `PathId` / `PathSliceId` citation surface + an SCR projection (“Assurance SCR”) suitable for audit, selection explainability, and refresh/RSCR wiring.
**Primary hooks.** A.10 (evidence anchors/carriers; SCR/RSCR anchoring), B.3 (assurance lanes and `F/G/R` skeleton), F.9 (BridgeCard/CL), G.4 (CAL `EvidenceProfiles` + `ProofLedger` linkage), `G.Core` (Part‑G invariants, RSCR trigger catalogue, default-governing-definition index), E.18/A.21 (GateCrossing + CrossingBundle checks), F.17 (UTS publication), F.15 (RSCR), E.10 (LEX), E.5.* (notation‑independence discipline).
**Non‑duplication note.** Universal Part‑G invariants (no shadow specs; Bridge‑only crossings; tri‑state discipline; penalties→`R_eff` only; P2W split; typed/id‑based RSCR causes; defaults with one governing definition; Δ‑discipline) are governed by `G.Core` and are *cited* via `CC‑GCORE‑*`. This pattern defines only the *EvidenceGraph kit* and its path‑addressable provenance surfaces.

