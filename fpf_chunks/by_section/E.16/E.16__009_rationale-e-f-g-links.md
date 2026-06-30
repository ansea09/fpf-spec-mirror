---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:8"
section_title: "Rationale & E‑/F‑/G‑links"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__009_rationale-e-f-g-links.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:8 — Rationale & E‑/F‑/G‑links"
line_start: 71869
line_end: 71876
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.24"
  - "C.9"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.17"
  - "F.4"
  - "F.6"
  - "F.8"
  - "G.10"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "autonomy budget"
  - "autonomy ledger"
  - "guarded enactment"
  - "override speech act"
  - "scout/probe/commit checkpoint"
---

### E.16:8 - Rationale & E‑/F‑/G‑links

* **E.8** — follows the pattern template (Context → Problem → Forces → Solution → Grounding → CC → Consequences).
* **E.10** — uses LEX‑BUNDLE: Scope via **ClaimScope (G)**, time via **Γ_time**, no “validity/process/actor/agent‑as‑noun” language; new lexical rule **L‑AUTO** added in edits below.
* **Mint/reuse authority (policy-ids).** Mint/reuse authority is expressed via **F.8:8.1** (`PolicyIdRef`: `PolicySpecRef` + `MintDecisionRef?`) and explicit **GateCrossing** checks (**E.18**) evaluated by the active **GateProfile/GateFit** (**A.21**); no tier ladder is required.
* **Part F** — integrates with **F.4** Role Description (RCS includes *AgencyLevel*; RSG gates), **F.6** Role Assignment & Enactment (Green‑Gate), **F.15** SCR/RSCR (harness includes depletion/override tests), **F.17** UTS (columns, incl. optional ScaleLens fields).
* **Part G** — **G.4/G.5**: method authors must declare budgets & guards; **G.9** parity includes autonomy consumption & violations; **G.10** shipping requires UTS autonomy fields.

