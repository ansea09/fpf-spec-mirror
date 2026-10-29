---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:8"
section_title: "Common failures and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__009_common-failures-and-repairs.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:8 — Common failures and repairs"
line_start: 77250
line_end: 77262
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
  - "architecture fitness-function source wording"
  - "architecture-characteristic eval program"
  - "comparison input"
  - "current-architecture evaluation"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "monitoring"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:8 - Common failures and repairs

| Failure | Symptom | Repair |
|---|---|---|
| `SourceFitnessTermAsFPFObject` | The source label "fitness function" hides which operation, rule or expression is meant. | Recover that source meaning. Frame the needed architecture evaluation through ACE while retaining the actual function, test or monitor as its own contribution; an ordinary source-local label may remain. |
| `EvalAsCriterion` | A benchmark, monitor, or test is named as the architecture characteristic. | Return to ACS; name the criterion, bearer, scale, proxy risk, and protected counter-characteristics before writing the eval. |
| `TestModeAsEvalWhole` | The team only asks whether one candidate passes while the work question is variant comparison. | Keep the test for the hard constraint, then add eval result forms that compare candidates or expose the trade-off front. |
| `UnfairComparison` | Candidates are compared under different budgets, evidence windows, environments, or missing-data rules. | Establish the comparison's required parity or withhold the unsupported comparative inference. Retain readings that remain usable under their own conditions. |
| `ResultAsDecision` | A rank, score, pass, or dashboard reading selects the architecture. | Treat the result as source material for an A.10 evidence-provenance account when an evidence claim is current, or as comparison input when comparison is current. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, `G.5` for selected-set result declaration, and `C.32.PAD` for a project architecture decision. For publication, use E.24.PUB for the occurrence and audience availability, and E.17 when a source-backed face and source return are needed. |
| `SingleIndicatorGoodhart` | Work improves one optimized indicator while an unmeasured architecture concern worsens. | Limit optimized indicators, add protected counter-characteristics, and open `E.13` when proxy-to-value drift appears. |
| `LosingVariantAsError` | A candidate that lost a planned eval is recorded as a mistake. | Record it as a variant result unless an expectation caused unplanned rework; keep useful learning in the variant archive. |
| `ProgramAsRunOrResult` | The ACE record is said to execute, measure, evaluate, or produce the result, or one generic `resultRef` hides the result kind. | Recover each exact evaluator through A.13 and let A.15.1 independently admit the evaluation `U.Work`. Add an attribution ref only when the record expressly represents precise assignment-bound attribution; missing or failed F.6 attribution alone leaves the Work intact while its independent A.13/A.15.1 grounds still hold. Add an operation application only when it independently obtains, and identify the typed result under the applicable pattern; keep the ACE record as the evaluation framing record. |

