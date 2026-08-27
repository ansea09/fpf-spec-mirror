---
chunk_kind: "child"
pattern_id: "C.32.MLAO"
pattern_title: "Multilevel Architecture Residual Optimization"
section_id: "C.32.MLAO:8"
section_title: "Common repair cues"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.MLAO/C.32.MLAO__009_common-repair-cues.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.32.MLAO — Multilevel Architecture Residual Optimization"
  - "C.32.MLAO:8 — Common repair cues"
line_start: 64603
line_end: 64616
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
| `ProxyResultAsPreferenceRule` | A residual vector, score, graph, front, dashboard reading, or lens output is used to prefer a candidate before the selected structures and lost structure are recovered. | Recover the selected structures and lost structure, interpret the result as a diagnostic signal or lens output; comparison belongs to `A.19.CPM`, local choice to `C.11`, set-returning selection to `A.19.SelectorMechanism`, and selected-set result declaration to `G.5`. |
| `ParetoFrontAsDecision` | A front is treated as selected architecture. | Use `G.5` for selected-set result declaration, `C.11` for local choice, `A.19.SelectorMechanism` for set-returning selection, and `C.32.PAD` for a project architecture decision. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. |
| `StaticOptimumClaim` | A current residual-reducing candidate is called optimal without an evolution window. | Add evolution window, source-return condition, reopen trigger, and the pattern for the next question result that actually produced the preference. |
| `ArchitectureInfluencePairCollapse` | The influence-source and transformed-side architecture content, changed referent, or actual transformation are treated as one object. | Open `C.32.CONWAY`; recover each exact C.30 architecture side, the typed influence relation, the changed referent, any actual A.3.4 transformation, the residual-bearing locus, candidate alternatives, and any C.29 structural-similarity claim before residual framing. |
| `LevelWordsNoLevels` | Text says level or scope without declared refs. | Use `C.30.STRAT` for stratification-term recovery or `B.2.P` for whole-reidentification wording, then return to residual triage before candidate framing. |
| `OptimizationNoLoss` | Candidates show only gains. | Add new burden, known loss, or bounded exception. |
| `IdealityNoBurden` | A candidate removes a bearer or support function but does not name lost function, coupling, evidence, control, or source-return burden. | Use C.32 and C.31; name function-bearing transfer, characteristic changes, and BLP scale window or waiver if scale advantage is claimed. |
| `FunctionNoBearerAtScope` | A functional change reduces one residual but no admitted bearer can carry it at the affected scope under resource, placement, control, or evidence constraints. | Add or change the bearer, split the function, change placement, resource access, or control relations, reduce the demand, or reject the candidate. Any responsibility claim uses its direct predicate or exact missing governor. |

