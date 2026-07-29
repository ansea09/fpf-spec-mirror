---
chunk_kind: "child"
pattern_id: "A.15.6"
pattern_title: "Project, Process, and Case Recovery through Work, Method, and Transformation"
section_id: "A.15.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.6/A.15.6__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.15.6 — Project, Process, and Case Recovery through Work, Method, and Transformation"
  - "A.15.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 26477
line_end: 26495
dependencies:
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
  - "A.22-selected U.Structure"
  - "SystemOfInterestRole"
  - "TransformationFlowStructure"
  - "U.RoleAssignment"
  - "actual composite project U.Work"
  - "actual versus intended system"
  - "affected case referent and change history"
  - "evaluation non-claim"
  - "missing constructor substrate"
  - "project designation and selection claim"
  - "project/process/case wording"
  - "result U.Episteme"
  - "reusable U.Method"
---

### A.15.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Charter-created project occurrence | Authorization or funding is counted as performed project work. | Keep the `U.WorkPlan` and decision relations; admit actual project work only after the complete `A.15.1` occurrence basis obtains. |
| Interval-made work part | An occurrence is called part of project Work because its timestamp lies inside the chosen project interval. | Admit the occurrence and composite Work independently, then state the exact obtaining work-part relation. Otherwise retain only the temporal relation. |
| Team-is-project | The temporary organization and the work it performs share one identity. | Identify the organization as `U.System`, the project as composite `U.Work`, and connect them through participation relations. |
| Occurrence-is-process | One successful or failed execution is treated as the repeatable method, or a local structure label is treated as an admitted process object. | Select `U.Method`, an exact A.22 `U.Structure`, or `TransformationFlowStructure` according to the claim. Fill all four A.22 discriminators before locally calling the structure `MethodRelationStructure`; otherwise keep direct relations unbundled. Use Work as a method-enactment observation only through exact `enactsMethod`, or as an operation-application observation through an exact A.6.1 declaration and binding. |
| Case-file substitution | A record replaces the patient, claim, asset, or other changing referent. | Read the claim content, select its exact EntityOfConcern, and keep the case file as a separate description episteme. |
| Three-view collapse | Project, process, and case topics assign subjects to descriptions and accounts with different subjects are published as one multi-view description. | Recover each EntityOfConcern from actual claim content; split independent subjects into separate epistemes and add correspondence relations where useful. |
| Suffix-provided locality | `@Project` or `@BoundedContext` is expected to establish identity, authority, or a selected structure. | Name the exact relation and typed reference. For a method-side structure, fill A.22's four discriminators; no suffix contributes locality or identity. |
| Role-by-label | A system is said to hold `SystemOfInterestRole` because someone called it the system of interest. | Keep the phrase Plain, or name the role value, taxonomy episteme, effective scheme, and concrete enactment-facing participation under A.2. Only then, if assignment identity matters, recover the actual holder, obtaining A.2.1 assignment, and uninterrupted extent. |
| Role proves project selection | An obtaining role assignment is treated as proof that one project selected its holder. | Keep the plan or decision designation and obtaining work, change, and use facts separate. Assert one compound selection claim only after its constructor substrate is selected; otherwise return the section 4.1a missing-substrate result. |
| Future-system backdating | A planned controller or plant is treated as an admitted system and role holder before it exists. | Keep the designator and expected use in plan content; after identity inception, test selection and assignment separately. |
| Project-result field | Entities, values, conditions, choices, measurements, verdicts, decisions, relation occurrences, changed referents, and claim-bearing epistemes are grouped as one intrinsic result of the project. | Ask what the result is and what it is a result of or for. Keep that subject in the kind or claim already established for it, then choose one WMR outcome. If no positive assertion is available, return one non-assertability result marked `factually unsupported`, `missing-information`, or `missing-governor`; only the last is an ontology blocker. |
| Network-is-project | A network of transformation-flow structures is treated as the project, workflow actor, or work-breakdown structure. | Keep the `E.18.NET` structure non-agentive and include Work in the project only through exact `A.15.1` work-parthood. |
| Probe-is-constructor | The `A.6.RCD:4.2` conjunction row or a reference scheme is treated as if it supplied a constructor substrate. | Keep every direct fact and return `missing-substrate[project-selection-conjunction]` until one substrate and edition defines the conjunction's inputs, output claim, applicability, and truth semantics. |
| Change-without-actor | Project Work, a flow structure, or the changed system is silently put in the acting position. | Name the distinct acting system and changed holon for every relied-on actual transformation; add a role assignment only when its own `A.2` and `A.2.1` facts obtain. |

