---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 78129
line_end: 78141
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

### G.6:8 - Common Anti-Patterns and How to Avoid Them

* **Narrative‑only provenance (“because story”).**
  **Avoid:** mint `PathId/PathSliceId` and require citation for any decision that claims evidence‑based justification (CC‑G6‑9).
* **Implicit crossings (“same entity, different context”).**
  **Avoid:** represent crossings only via explicit crossing artefacts/pins; treat edition/plane/context changes as explicit crossing‑relevant edits and trigger RSCR (governed by G.Core crossing discipline).
* **Smuggling legality rules into EvidenceGraph prose.**
  **Avoid:** cite/pin legality surfaces (`CG‑Spec` and CAL artefacts); do not introduce local “mini‑CG” rules in G.6 (cite `CC‑GCORE‑CN‑CG‑1`).
* **Unpinned editions/policies (“it’s obvious which version”).**
  **Avoid:** require explicit edition/policy pins on citable paths; treat changes as typed triggers.
* **Alias‑only RSCR causes (“H3: something changed”).**
  **Avoid:** record canonical `RSCRTriggerKindId` as the cause; aliases are labels only and must dock via `G.Core.TriggerAliasMap.G6`.

