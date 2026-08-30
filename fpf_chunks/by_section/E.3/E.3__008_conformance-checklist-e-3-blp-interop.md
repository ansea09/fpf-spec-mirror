---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy & Precedence Model"
section_id: "E.3:7"
section_title: "Conformance Checklist — E.3 ↔ BLP Interop"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__008_conformance-checklist-e-3-blp-interop.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "E.3 — Principle Taxonomy & Precedence Model"
  - "E.3:7 — Conformance Checklist — E.3 ↔ BLP Interop"
line_start: 69765
line_end: 69774
dependencies:
  - "E.2"
keywords:
  - "Arch"
  - "Did"
  - "Epist"
  - "Gov"
  - "Prag"
  - "classification"
  - "conflict resolution"
  - "hierarchy"
  - "precedence"
  - "principles"
  - "taxonomy"
---

### E.3:7 - **Conformance Checklist — E.3 ↔ BLP Interop**

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑E3.10** | Precedence list includes **BLP** explicitly **below** E/E‑LOG and **above** product tactics; conflicts handled via **BLP‑waiver** discipline. | Makes BLP’s standing auditable. |
| **CC‑E3.11** | Every DRR that overrides BLP **MUST** include a **Scale‑Audit** (E.2 **BLP‑1**) and a **Heuristic‑Debt** entry (E.2 **BLP‑4**). | Prevents silent heuristic drift. |
| **CC‑E3.12** | Each agentic plan declares an **AutonomyProfileId** (e.g., L0–L4) with explicit budgets, `explore_share`, and **E/E‑LOG EmitterPolicyRef**. | Aligns autonomy with assurance. |
| **CC‑E3.13** | L1+ executions emit **CallGraphs** with editioned policy/method ids and budget deltas; L3+ include adaptation status. | Ensures replayability & audit. |
| **CC‑E3.14** | Profile changes follow **promotion/demotion** triggers and are published as GateCrossings with edition pins in the SCR. | Keeps autonomy under control. |

