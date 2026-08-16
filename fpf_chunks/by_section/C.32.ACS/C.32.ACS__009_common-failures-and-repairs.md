---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set for Improvement Cycles"
section_id: "C.32.ACS:8"
section_title: "Common failures and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__009_common-failures-and-repairs.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set for Improvement Cycles"
  - "C.32.ACS:8 — Common failures and repairs"
line_start: 65137
line_end: 65150
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.30"
  - "C.30.P"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.HCS"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "Q-Bundle"
  - "anti-Goodhart guard"
  - "architecture characteristic criteria set"
  - "criteria row"
  - "improvement cycle"
  - "protected counter-characteristic"
  - "proxy risk"
---

### C.32.ACS:8 - Common failures and repairs

| Failure | Working symptom | Repair |
|---|---|---|
| `CatalogueCopyAsCriteriaSet` | A project imports a long list of ilities and treats the list as architecture guidance. | Use HCS for starter heads, then build ACS rows, mark optimization indicators, and keep guardrails and context-only rows separate. |
| `TooManyOptimizationIndicators` | Dozens of rows drive optimization at once. | Keep the few rows that change the next synthesis step; demote the rest to monitored guardrails or context-only rows. |
| `FunctionGoalAsArchitectureCriterion` | A user-visible function is used as the architecture optimization criterion. | Recover the function through `A.6.F`; then name the architecture characteristic that makes the function sustainable. |
| `QBundleDuplicatedAsScaleSet` | Maintainability, availability, security, teachability, or trustworthiness is treated as one ACS row when the truth depends on several typed slots. | Open `C.25`, construct or reference the Q-Bundle, then select only the relevant slot for ACS use. Keep any report-only proxy outside the criteria row unless its bearer, scale, proxy risk, and receiving use are declared. |
| `EvalProgramAsCriterion` | A test, monitor, source-side fitness function, benchmark, dashboard, or eval result is named as the criterion. | Name the characteristic row first; eval-program construction belongs to `C.32.ACE` and measurement claims belong to `C.16`. |
| `BearerCarryoverWithoutRebinding` | An engineered-system row is copied to architecture around a Method, local system-role kind, separate System-classification judgment, assignment, or cultural-evolution case without changing the exact bearer, predicate, scale, or admissible use. | Return to HCS only if the described holon family changed. Otherwise stay in ACS and rebind the row to the actual bearer and selected structure; a Method, kind, or assignment is not forced into a holon family. |
| `LocalGainHidesCounterLoss` | A candidate improves one row while worsening evidence burden, control burden, source-return cost, or functional adequacy. | Add monitored guardrail rows and open `E.13` when proxy-to-value drift appears before comparison or next synthesis. |
| `ReadingAsDecision` | A better reading is treated as the selected architecture. | Keep the reading as feedback. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, `G.5` for selected-set result declaration, and `C.32.PAD` for a project architecture decision. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. |
| `ContextLabelAsRowScope` | A domain, team, project, or bounded-context label is used as if it delimited every criterion row. | Bind each row's exact `U.ClaimScope`, selected A.2.6 context slices, scheme and plane, and window; add a selected model-use structure only when it changes interpretation. |

