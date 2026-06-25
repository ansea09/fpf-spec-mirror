---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:4"
section_title: "Separation From Neighboring Values"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__005_separation-from-neighboring-values.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:4 — Separation From Neighboring Values"
line_start: 2691
line_end: 2702
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

### A.2.2:4 - Separation From Neighboring Values

| Source wording | Recovered FPF values |
|---|---|
| "Engineer role can approve the design." | `U.Role` and `U.RoleAssignment` for who may act; `U.Capability` only if the holder's ability to approve is being measured or qualified. |
| "The robot is assigned as welder." | `U.RoleAssignment`; add `U.Capability` only if the claim also says the robot can meet a welding envelope and measures. |
| "The solver has the scheduling algorithm." | `U.MethodDescription` or deployed software-system relation; `U.Capability` only for the deployed system's ability to produce schedules within bounds. |
| "The report has evidence capability." | Evidence-use relation around an episteme; no capability holder unless a system can perform evidential work. |
| "The team did one successful run." | `U.Work` occurrence; capability only after a separate ability claim with envelope, measures, and currentness. |
| "We promise five-day close." | Promise content and commitment; capability is the internal holder ability that makes the promise credible. |
| "The architecture provides resilience capability." | Architecture or structure claim plus capability claim for the relevant system or composite, with measured resilience characteristics. |

