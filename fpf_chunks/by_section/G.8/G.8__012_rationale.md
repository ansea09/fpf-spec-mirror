---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "SoS‑LOG Bundles & Maturity Ladders"
section_id: "G.8:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__012_rationale.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "G.8 — SoS‑LOG Bundles & Maturity Ladders"
  - "G.8:11 — Rationale"
line_start: 72747
line_end: 72750
dependencies:
  - "A.10"
  - "A.21"
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

### G.8:11 - Rationale

`C.23` governs **rule semantics**, `G.4` governs **thresholding/acceptance**, `G.6` governs **path‑addressable provenance**, and `G.5` governs **selection/registry semantics**. Without a dedicated packaging kit, projects either (i) duplicate semantics inside ad‑hoc “decision bundles” (creating shadow specs), or (ii) leave dispatch un‑auditable. `G.8` keeps these boundaries strict while providing a single, consumable surface.

