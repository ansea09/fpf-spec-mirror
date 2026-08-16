---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__013_sota-echoing.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:12 — SoTA-Echoing"
line_start: 3778
line_end: 3788
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
| Capability-based planning in defense and enterprise architecture keeps ability, mission need, activities, Systems, and portfolio planning separate. | The `U.Capability` name governs holder-dependent capability instances with envelope and measures; each instance is not a system-role kind, assignment, Method, Work record, promise, statement, evidence record, or quality bundle. | A capability instance can be compared across candidate Systems without selecting the implementation too early. |
| Analyzable architecture and capability-planning practice separates the system whose ability is claimed from architecture descriptions, requirements, measures, and evidence. | Capability instances name holder, result class, envelope, measures, and qualification window; descriptions, statements, evidence, and currentness assessments remain separate values. | The reader can see which object changed when a requirement, holder, measure, source, or operating condition changes. |
| Current uncertainty and verification work for cyber-physical and autonomous systems treats operating conditions and currentness as first-class modeling concerns. | Qualification windows and lowering triggers are part of the capability instance boundary; evidence, source-use refs, and currentness assessments support or lower reliance without becoming capability. | A stale calibration, changed version, or out-of-envelope input lowers the currentness assessment or capability instance locally. |
| Modern access-control and zero-trust practice separates the acting system, assignment, current assignment-state relation, policy decision, and resource action. | An assignment or assignment-state relation may satisfy an entry condition, but neither grants capability. | “Allowed to act” and “able to achieve the measured result” remain separate checks. |

Source-currentness note: DoDAF and TOGAF are used here as stable capability-planning lineage, not as the full current frontier. Current pressure comes from analyzable architecture, uncertainty-aware engineering, stakeholder-context formalization, and model integration. The NIST zero-trust line is used only for the split between current authorization and measured ability. SysML 2.0 is intentionally excluded as a SoTA authority or lineage for this decision: its model-element vocabulary does not settle the identity of capability holder, system-role kind, assignment, Method, Work, evidence, or capability occurrence, and no claim here depends on it.

