---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__004_forces.md"
commit_sha: "e230eef4f6955116bf697ca9ba5e79247af1843e"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:3 — Forces"
line_start: 67293
line_end: 67299
dependencies:
  - "A.10"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "E.10"
  - "E.18"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
keywords:
  - "MethodFamily"
  - "SoS-LOG"
  - "abstain"
  - "admission rules"
  - "admit"
  - "degrade"
  - "evidence"
  - "maturity"
  - "selector"
---

### C.23:3 - Forces

* **Pluralism vs. dispatchability.** Competing Traditions expose different invariants; selection must compare **without semantic flattening**.
* **Maturity vs. opportunity.** Open‑ended exploration (E/E‑LOG) must coexist with **run‑safe** exploitation; *immature ≠ forbidden* → provide safe **degrade** paths.
* **Unknowns (tri‑state).** Missing or `unknown` values in live S2 fields must propagate to *Degrade(mode)* (including *sandbox*) or *Abstain*; no silent coercions.
* **Meaning and implementation.** Keep the family, its description, rule and evaluation result distinct. A particular notation or software implementation must preserve the same admission conditions.

