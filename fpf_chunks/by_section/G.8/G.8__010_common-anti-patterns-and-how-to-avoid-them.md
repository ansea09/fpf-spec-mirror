---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
section_id: "G.8:9"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "G.8 — Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
  - "G.8:9 — Common Anti‑Patterns and How to Avoid Them"
line_start: 129434
line_end: 129450
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.23"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.17"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "SoS-LOG"
  - "admissibility ledger"
  - "rule ids"
  - "tri-state {pass"
---

### G.8:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern:** Embedding thresholds inside SoS‑LOG rules or ladder rungs.
  **Avoid:** thresholds live in `G.4` Acceptance; bundle only cites clause ids.

* **Anti‑pattern:** Treating illumination/QD telemetry as a hidden scalar score that changes dominance.
  **Avoid:** keep telemetry report‑only unless explicitly promoted by a governing-pattern policy pin.

* **Anti‑pattern:** Publishing a bundle that implies a correspondence or receiving-use conclusion without its required grounds, or omits CL/Φ pins required by the actual calibration or named assurance use.
  **Avoid:** retain the actual channel and receiving-use grounds under G.Core:4.2.3, using `G.8:Ext.BridgeReuseWiring` for F.9 reuse. Missing required grounds block the dependent use.

* **Anti‑pattern:** Re‑defining `PortfolioMode`/`DominanceRegime` defaults in the bundle text.
  **Avoid:** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex`.

* **Anti‑pattern:** Recording RSCR “reasons” as prose labels only.
  **Avoid:** emit canonical `RSCRTriggerKindId` values per `G.Core`.

