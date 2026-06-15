---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__014_relations.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:12 — Relations"
line_start: 82671
line_end: 82677
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

### G.6:12 - Relations

**Builds on:** `G.Core`, `A.10` (evidence anchors/carriers; SCR/RSCR), `B.3` (assurance skeleton), `F.9` (BridgeCard/CL), `G.4` (CAL EvidenceProfiles/ProofLedger), `E.18/A.21` (GateCrossing/CrossingBundle checks), `E.10` (lexical rules), `E.5.*` (notation independence), `F.17` (UTS), `F.15` (RSCR).
**Publishes to:** UTS (Name Cards + PathCards), SCR/RSCR surfaces, downstream selectors/LOG by `PathId` citation, refresh/orchestration as typed triggers (consumed by `G.11` when used).
**Used by:** `G.5` (selector explainability and admissibility justifications), `G.8` (SoS‑LOG bundles), `G.9` (parity harness traces), `G.10` (shipping pins and audit payload), `G.11` (refresh orchestration).
**Constrains:** downstream patterns MUST cite paths when evidence is claimed; they MUST treat edits to pinned evidence/crossing/policy/edition/time bindings as refresh‑relevant causes with canonical trigger ids (governed by `G.Core`).

