---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__013_sota-echoing.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:12 — SoTA-Echoing"
line_start: 3129
line_end: 3139
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
  - "E.24.UK"
keywords:
  - "ability envelope"
  - "capability-fit condition"
  - "currentness"
  - "holder-dependent capability instance"
  - "measure set"
  - "qualification window"
---

### A.2.2:12 - SoTA-Echoing

| Current practice or research line | What FPF takes | Practical implication |
|---|---|---|
| Capability-based planning in defense and enterprise architecture keeps ability, mission need, activities, systems, and portfolio planning separate. | The `U.Capability` name governs holder-dependent capability instances with envelope and measures; each instance is not a role, method, work record, promise, statement, evidence record, or quality bundle. | A capability instance can be compared across candidate systems without selecting the implementation too early. |
| Current model-based systems engineering, including SysML v2 work, increases semantic precision and traceability between system model elements, requirements, measures, and stakeholder concerns. | Capability instances name holder, result class, envelope, measures, and qualification window; statements, evidence, and currentness assessments remain separate typed values. | The reader can see which object changed when a requirement, holder, measure, source, or context changes. |
| Current uncertainty and verification work for cyber-physical and autonomous systems treats operating conditions and currentness as first-class modeling concerns. | Qualification windows and lowering triggers are part of the capability instance boundary; evidence, source-use refs, and currentness assessments support or lower reliance without becoming capability. | A stale calibration, changed version, or out-of-envelope input lowers the currentness assessment or capability instance locally. |
| Modern access-control and zero-trust practice separates subject, role relation, current state, policy decision, and resource action. | A role assignment or role state may admit a work attempt, but it does not grant capability. | "Allowed to act" and "able to achieve the measured result" remain separate checks. |

Source-currentness note: DoDAF and TOGAF are used here as stable capability-planning practice lineage, not as the full current frontier. Current pressure comes from SysML v2 and 2025-2026 MBSE work on semantic precision, uncertainty, stakeholder-context formalization, and model integration. The NIST zero-trust line is used only for the split between current authorization and measured ability.

