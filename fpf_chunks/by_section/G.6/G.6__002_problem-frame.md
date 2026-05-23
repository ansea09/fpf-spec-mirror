---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__002_problem-frame.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:1 — Problem frame"
line_start: 71678
line_end: 71691
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

### G.6:1 - Problem frame

SoTA claims, operators, and method families are admitted (or gated) using assurance signals derived from diverse artefacts and anchors. FPF already mandates **Evidence Graph Referring** (A.10), lane discipline, and the assurance skeleton (B.3). What is often still missing in practice is a *first‑class, citable* object that makes the provenance of an admission/decision **addressable**:

* *exactly which* anchors and bindings were used,
* *under which* `ReferencePlane` and `BoundedContext`,
* *with which* explicit crossings and penalty policies,
* *for which* time window (freshness/decay),
* in a way that selectors, audits, and maturity transitions can cite without copying tables or re‑telling a story.

This pattern introduces the missing kit: a typed, lane‑aware `EvidenceGraph` plus stable `PathId` / `PathSliceId` addresses that downstream LOG, UTS, parity, and refresh can cite.

**Why here (not in G.4)?** G.4 governs CAL artefacts (EvidenceProfiles, ProofLedger, acceptance policies). G.6 packages *cross‑artefact provenance* as a graph and mints *path identities* that downstream surfaces can cite without duplicating CAL tables or re‑inventing legality rules.

