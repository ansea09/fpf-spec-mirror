---
chunk_kind: "child"
pattern_id: "C.32.MLAO"
pattern_title: "Multilevel Architecture Residual Optimization"
section_id: "C.32.MLAO:8"
section_title: "Common repair cues"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.MLAO/C.32.MLAO__009_common-repair-cues.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.32.MLAO — Multilevel Architecture Residual Optimization"
  - "C.32.MLAO:8 — Common repair cues"
line_start: 64552
line_end: 64565
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.6.M"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.29"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "G.5"
keywords:
  - "Pareto front"
  - "declared level"
  - "declared scope"
  - "ideality pressure"
  - "multilevel architecture residual optimization"
  - "residual-reducing candidate frame"
  - "scale amenability"
  - "stepping stone"
---

### C.32.MLAO:8 - Common repair cues

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `LocalEvalAsWholeArchitecture` | One scope improves or one eval result is better, and the whole architecture is called better. | Return to residual triage; name improved and harmed scopes, selected structures, criteria rows, and residual-bearing locus before framing residual-reducing candidates. |
| `ProxyResultAsPreferenceRule` | A residual vector, score, graph, front, dashboard reading, or lens output is used to prefer a candidate before the selected structures and lost structure are recovered. | Recover the selected structures and lost structure, interpret the result as a diagnostic signal or lens output; comparison belongs to `A.19.CPM`, local choice to `C.11`, set-returning selection to `A.19.SelectorMechanism`, and publication of a selected set to `G.5`. |
| `ParetoFrontAsDecision` | A front is treated as selected architecture. | Publication of a selected set belongs to `G.5`, local choice to `C.11`, set-returning selection to `A.19.SelectorMechanism`, and project architecture decision to `C.32.PAD`. |
| `StaticOptimumClaim` | A current residual-reducing candidate is called optimal without an evolution window. | Add evolution window, source-return condition, reopen trigger, and the receiving pattern result that actually produced the preference. |
| `TransformerTransformedCollapse` | The architecture of the changing holon and the changed holon are treated as one structure. | Open `C.32.CONWAY`; recover the changing relation, selected structures on both sides, residual-bearing locus, candidate alternatives, and any C.29 structural-similarity claim before residual framing. |
| `LevelWordsNoLevels` | Text says level or scope without declared refs. | Use `C.30.STRAT` for stratification-term recovery or `B.2.P` for whole-reidentification wording, then return to residual triage before candidate framing. |
| `OptimizationNoLoss` | Candidates show only gains. | Add new burden, known loss, or bounded exception. |
| `IdealityNoBurden` | A candidate removes a bearer or support function but does not name lost function, coupling, evidence, control, or source-return burden. | Return to C.32 and C.31; name function-bearing transfer, characteristic changes, and BLP scale window or waiver if scale advantage is claimed. |
| `FunctionNoBearerAtScope` | A functional change reduces one residual but no bearer can carry it at the affected scope under resource, placement, control, or evidence constraints. | Add or change bearer, split function, change placement or resource access, change control responsibility, reduce the demand, or reject the candidate. |

