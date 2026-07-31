---
chunk_kind: "child"
pattern_id: "A.15.6"
pattern_title: "Project, Process, and Case Recovery through Work, Method, and Transformation"
section_id: "A.15.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.6/A.15.6__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.15.6 — Project, Process, and Case Recovery through Work, Method, and Transformation"
  - "A.15.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 26419
line_end: 26437
dependencies:
  - "A.1"
  - "A.1.STM"
  - "A.12"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.22"
  - "A.3.1"
  - "A.3.4"
  - "A.6.1"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.18"
  - "E.18.NET"
  - "E.24.PUB"
keywords:
---

### A.15.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Charter-created project occurrence | Authorization or funding is counted as performed project work. | Keep the `U.WorkPlan` and decision relations; admit actual project work only after the complete `A.15.1` occurrence basis obtains. |
| Interval-made work part | An occurrence is called part of project Work because its timestamp lies inside the chosen project interval. | Admit the occurrence and composite Work independently, then state the exact obtaining work-part relation. Otherwise retain only the temporal relation. |
| Team-is-project | The temporary organization and the work it performs share one identity. | Identify the organization as `U.System`, the project as composite `U.Work`, and connect them through participation relations. |
| Occurrence-is-process | One successful or failed execution is treated as the repeatable method, or a local structure label is treated as an admitted process object. | Select `U.Method`, an exact A.22 `U.Structure`, or `TransformationFlowStructure` according to the claim. Fill all four A.22 discriminators before locally calling the structure `MethodRelationStructure`; otherwise keep direct relations unbundled. Use Work as a method-enactment observation only through exact `enactsMethod`, or as an operation-application observation through an exact A.6.1 declaration and binding. |
| Case-file or changed-entity substitution | A record replaces the subject, or every case is forced into one continuing affected entity. | Read the closure claim, select its exact EntityOfConcern, preserve episteme-edition, characteristic/measurement, relation, decision, result, and continuing-referent identity laws, and keep the case file as a separate episteme. |
| Three-view collapse | Project, process, and case topics assign subjects to descriptions and accounts with different subjects are published as one multi-view description. | Recover each EntityOfConcern from actual claim content; split independent subjects into separate epistemes and add correspondence relations where useful. |
| Suffix-provided locality | `@Project` or `@BoundedContext` is expected to establish identity, authority, or a selected structure. | Name the exact relation and typed reference. For a method-side structure, fill A.22's four discriminators; no suffix contributes locality or identity. |
| Role-by-label | A system is said to hold `SystemOfInterestRole` because someone called it the project system-of-interest. | Keep project designation Plain, or name the role value, taxonomy episteme, effective scheme, and concrete enactment-facing participation under A.2. Only then, if assignment identity matters, recover the holder, obtaining A.2.1 assignment, and uninterrupted extent. |
| Role proves project selection | An obtaining role assignment is treated as proof that one project selected its holder. | Keep the plan or decision designation and obtaining work, change, and use facts separate. Assert one compound selection claim only after its constructor substrate is selected; otherwise return the section 4.1a missing-substrate result. |
| Future-system backdating | A planned controller or plant is treated as an admitted system and role holder before it exists. | Keep the designator and expected use in plan content; after identity inception, test selection and assignment separately. |
| Project-result field | Entities, values, conditions, choices, measurements, verdicts, decisions, relation occurrences, changed referents, and claim-bearing epistemes are grouped as one intrinsic result of the project. | Ask what the result is and what it is a result of or for. Keep that subject in the kind or claim already established for it, then choose one WMR outcome. If no positive assertion is available, return one non-assertability result marked `factually unsupported`, `missing-information`, or `missing-governor`; only the last is an ontology blocker. |
| Network-is-project | A network of transformation-flow structures is treated as the project, workflow actor, or work-breakdown structure. | Keep the `E.18.NET` structure non-agentive and include Work in the project only through exact `A.15.1` work-parthood. |
| Probe-is-constructor | The `A.6.RCD:4.2` conjunction row or a reference scheme is treated as if it supplied a constructor substrate. | Keep every direct fact and return `missing-substrate[project-selection-conjunction]` until one substrate and edition defines the conjunction's inputs, output claim, applicability, and truth semantics. |
| Actor invented or suppressed | Every Transformation is forced to have a Work performer, or project Work, a TFS/network, Method, record, or changed subject is silently put in an acting position. | Ground the A.3.4 change first. Add a causal or interaction participant only under its direct owner. For a Work-realized change, name performer system, covering assignment, Work, changed referent, and direct governor; otherwise invent no actor, assignment, Method, or Work. |

