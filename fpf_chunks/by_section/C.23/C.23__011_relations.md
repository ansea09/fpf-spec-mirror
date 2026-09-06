---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:10"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__011_relations.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:10 — Relations"
line_start: 53349
line_end: 53355
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
  - "admit"
  - "degrade"
  - "evidence"
  - "maturity"
  - "selector"
---

### C.23:10 - Relations

**Builds on:** **G.5** (selector consumes these rules), **G.4** (Acceptance & EvidenceProfiles), **C.22** (S2 typing), **C.18 NQD‑CAL**, **C.19 E/E‑LOG**, **B.3** (named assurance claims and declared aggregation, including WLNK only when applicable).
**Publishes to:** **UTS** (MaturityCards, rule ids), **SCR/RSCR** (branch coverage; parity hooks).
**Constrains:** **G.8** (LOG Bundling must cite MaturityCards), **G.9** (parity harness draws baselines per rung), **G.11** (refresh windows per rung & decay), **G.5** (Open‑Ended Family mode for GeneratorFamily).
**Outcome.** **Admissibility logic** for MethodFamilies combines LOG shells, the maturity poset, degrade modes, and publication requirements with CG‑Spec legality rules, CHR guard‑macros, and CAL acceptance mechanics.

