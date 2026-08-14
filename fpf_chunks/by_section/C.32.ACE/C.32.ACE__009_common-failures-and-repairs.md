---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:8"
section_title: "Common failures and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__009_common-failures-and-repairs.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:8 — Common failures and repairs"
line_start: 65675
line_end: 65687
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.32"
  - "C.32.ACS"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "architecture-characteristic eval program"
  - "comparison input"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:8 - Common failures and repairs

| Failure | Symptom | Repair |
|---|---|---|
| `SourceFitnessTermAsFPFObject` | "Fitness function" is written as the object under work. | Rewrite as `ArchitectureCharacteristicEvalProgram@Project` and name evaluated rows, candidates, parity frame, eval operations, and receiving use. |
| `EvalAsCriterion` | A benchmark, monitor, or test is named as the architecture characteristic. | Return to ACS; name the criterion, bearer, scale, proxy risk, and protected counter-characteristics before writing the eval. |
| `TestModeAsEvalWhole` | The team only asks whether one candidate passes while the work question is variant comparison. | Keep the test for the hard constraint, then add eval result forms that compare candidates or expose the trade-off front. |
| `UnfairComparison` | Candidates are compared under different budgets, evidence windows, environments, or missing-data rules. | Rebuild the parity frame or record the result as unusable for selection. |
| `ResultAsDecision` | A rank, score, pass, or dashboard reading selects the architecture. | Treat the result as source material for an A.10 evidence relation when an evidence claim is current, or as comparison input when comparison is current. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, `G.5` for selected-set result declaration, and `C.32.PAD` for a project architecture decision. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. |
| `SingleIndicatorGoodhart` | Work improves one optimized indicator while an unmeasured architecture concern worsens. | Limit optimized indicators, add protected counter-characteristics, and open `E.13` when proxy-to-value drift appears. |
| `LosingVariantAsError` | A candidate that lost a planned eval is recorded as a mistake. | Record it as a variant result unless an expectation caused unplanned rework; keep useful learning in the variant archive. |
| `ProgramAsRunOrResult` | The ACE record is said to execute, measure, evaluate, or produce the result, or one generic `resultRef` hides the result kind. | Name the evaluation's `U.Work` occurrence and keep all facts required by A.15.1, A.2.1, and F.6 recoverable. Add an operation application only when it independently obtains, and identify the typed result under the applicable pattern; keep the ACE record as the evaluation framing record. |

