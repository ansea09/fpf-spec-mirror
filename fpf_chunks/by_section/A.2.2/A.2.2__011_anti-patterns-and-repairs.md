---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:10"
section_title: "Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__011_anti-patterns-and-repairs.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:10 — Anti-Patterns and Repairs"
line_start: 2811
line_end: 2823
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
keywords:
  - "ability"
  - "action"
  - "measures"
  - "performance"
  - "skill"
  - "work scope"
---

### A.2.2:10 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Role-as-capability | "The inspector role can detect this defect." | Keep the role value and role assignment; state capability for the holder system if measured detection ability is current. |
| Assignment-as-capability | "Assigned, therefore able." | Use A.2.1 for assignment and A.2.2 for the ability claim. |
| Method-description-as-capability | "The procedure has capability." | Use `U.MethodDescription` for the episteme; use `U.Capability` for the system that can enact the method within bounds. |
| Work-as-capability | "We did it once, so we can." | Keep the work occurrence; add a separate capability claim only when envelope, measures, and currentness are justified. |
| Promise-as-capability | "The SLA is our capability." | Use promise content or commitment for what is offered; capability is the internal measured ability that makes the promise credible. |
| Episteme-as-holder | "The report has assessment capability." | Use evidence, source, status, or assessment relation for the episteme; capability holder remains a system. |
| Unbounded capability | "The tool can machine titanium." | Add material grade, tolerances, feed range, environment, version, qualification window, and measurement evidence. |
| Capability threshold in role name | `HighPrecisionWelderRole` hides a measured threshold. | Keep role name clean; put precision threshold in method requirement and holder capability. |

