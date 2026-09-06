---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 9651
line_end: 9664
dependencies:
  - "A.1"
  - "A.10"
  - "A.11"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.22"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.32.P2S"
  - "E.18"
  - "E.18.1"
  - "E.24"
  - "E.24.UK"
  - "F.18"
  - "G.11"
keywords:
  - "actual bounded change"
  - "actual subject facts"
  - "changed referent"
  - "continuity and reidentification"
  - "occurrence boundary"
  - "transformation composition"
---

### A.3.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Method name as change | "This method transforms X" is treated as an actual occurrence. | Name the continuing changed subject, boundary, and before/during/after facts; keep the method under A.3.1. |
| Process diagram as work | A workflow diagram is treated as enacted work. | Use `E.18` or `A.3.2` for the diagram; use `A.15.1` for dated work. |
| Dynamics model as permission | A transition law is used to approve action. | Keep `A.3.3` for the model; use evidence, gate, decision, and assurance patterns for use authority. |
| Temporal trend as intervention | A rate or rhythm trend is treated as proof of changed behavior under an intervention. | Use `C.27.TA` and `C.27`, then identify the continuing changed subject and its before/during/after facts separately. |
| Formal construction as work | A morphism or proof construction is treated as work performed in a project-world object. | Use `C.29` or the direct formal pattern for the mathematical relation; name realization and work separately. |
| Publication as transformation | A dashboard or report is treated as the changed state. | Use publication or source patterns for that artifact; identify the changed subject separately. |
| Sliced trajectory as composition | Samples, subintervals, method steps, work parts, concurrent changes, or flow nodes are declared components of one transformation by containment or proximity. | Independently identify each actual transformation. If the use needs a positive composition claim, return the parked blocker in 4.2.1; this edition does not choose its future architecture. Sampling or subdivision likewise supplies no evidence of indivisibility. |
| Resolution-level identification as partlessness | A change identified as one occurrence at the resolution chosen for the task is treated as necessarily atomic, indivisible, or partless, or as automatically composite and holonic. | Keep the independently identified `U.Transformation`; infer neither presence nor absence of finer parts. Do not make a positive composition or A.1 claim until a future accepted architecture supplies its basis. |
| Work-caused change as production | A change that follows `U.Work` is called a produced entity or completed production. | First close the named work/transformation connection through `4.2.4` or keep its blocker; then separately test production-work participation, first existence of the subject, and the applicable production-completion criterion under `A.15.PROD`. |

