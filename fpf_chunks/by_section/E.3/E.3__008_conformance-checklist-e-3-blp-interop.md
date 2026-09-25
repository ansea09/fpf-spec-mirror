---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
section_id: "E.3:7"
section_title: "Conformance Checklist — E.3 ↔ BLP Interop"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__008_conformance-checklist-e-3-blp-interop.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.3 — Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
  - "E.3:7 — Conformance Checklist — E.3 ↔ BLP Interop"
line_start: 79088
line_end: 79097
dependencies:
  - "E.1"
  - "E.2"
keywords:
  - "ABL"
  - "Arch"
  - "BLP waiver"
  - "Did"
  - "Epist"
  - "Gov"
  - "Prag"
  - "autonomy budget"
  - "conflict resolution"
  - "oversight"
  - "precedence"
  - "principle taxonomy"
  - "profile change"
---

### E.3:7 - **Conformance Checklist — E.3 ↔ BLP Interop**

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑E3.10** | Precedence list includes **BLP** explicitly **below** E/E‑LOG and **above** product tactics; conflicts handled via **BLP‑waiver** discipline. | Makes BLP’s standing auditable. |
| **CC‑E3.11** | A DRR invoking an exception to an applicable BLP/generality policy identifies that exact policy and meets its waiver, evidence and conditional debt requirements. Specialization or a fixed procedure alone creates no exception. | Keeps real overrides visible without manufacturing them. |
| **CC‑E3.12** | Each agentic plan declares an **AutonomyProfileId** (e.g., L0–L4) with explicit budgets. Add `explore_share` and the **E/E‑LOG EmitterPolicyRef** only when the plan uses that live-pool profile under C.24 ATC-4. | Aligns autonomy with assurance. |
| **CC‑E3.13** | L1+ executions emit **CallGraphs** with editioned policy/method ids and budget deltas; L3+ include adaptation status. | Ensures replayability & audit. |
| **CC‑E3.14** | Profile changes follow **promotion/demotion** triggers and publish the profile/policy editions and A.21 decision. E.18 crossing refs and F.9 Bridge refs are present only when their separate predicates obtain. | Keeps autonomy under control. |

