---
chunk_kind: "child"
pattern_id: "C.32.FAIL"
pattern_title: "Architecture Failure Recognition and Repair"
section_id: "C.32.FAIL:8"
section_title: "Common repair cues"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.FAIL/C.32.FAIL__009_common-repair-cues.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "C.32.FAIL — Architecture Failure Recognition and Repair"
  - "C.32.FAIL:8 — Common repair cues"
line_start: 60235
line_end: 60250
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.P"
  - "C.31"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.24.PUB"
  - "G.5"
keywords:
  - "architecture failure cue"
  - "architecture repair cue"
  - "candidate repair"
  - "repair-entry family"
  - "selected-structure relation"
  - "source overread"
  - "stressed architecture object"
---

### C.32.FAIL:8 - Common repair cues

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `WarningNameOnly` | A memorable warning name does not change the next repair action. | Add the architecture object, blocked overread, governing pattern, and repair action, or remove the row. |
| `EverythingIsFailureCue` | Any architecture worry is admitted as a C.32.FAIL cue. | Admit only recurring failures that change the first architecture repair action. |
| `AuditPromptAsPattern` | The row says to measure, review, or audit. | Demote it unless it names the architecture object and repair action first. |
| `EvidenceAsRepair` | More evidence is treated as the repair. | Name the architecture repair first; evidence may follow under its own pattern. |
| `DecisionInsideRepairCue` | The cue says which architecture to choose. | Local choice belongs to `C.11`; project architecture decision belongs to the project-selected architecture-decision pattern after the candidate repair is available. |
| `DescriptionCarrierAsRepair` | A diagram, report, dashboard, or publication face is treated as the repair. | Description use belongs to `C.30.AD`; publication-face use belongs to `E.17` or `E.24.PUB`; dashboard, report, or generated carrier use must stay under source-use or publication governance. Keep C.32.FAIL only if an architecture object under stress and repair action are named. |
| `FunctionAsQuality` | A function such as teach, compute, certify, or regulate is treated as the architecture characteristic. | Recover the function under `A.6.F` and name the separate architecture characteristic or quality bundle. |
| `FunctionalGraphNoBearer` | A functional graph, workflow, or method structure names a required function that no admitted bearer can perform under the module, placement, resource, control, or evidence constraints declared for the case. | Return to C.32; add or change bearer, split function, change placement or resource access, change control responsibility, reduce demand, or reject the candidate. |
| `IdealityAsAdequacyShortcut` | The phrase ideal architecture, no modules, or fewer parts is used as architecture adequacy by itself. | Convert it into a C.32 candidate and name function bearing, lost structure, new burden, architecture characteristics, and receiving pattern. |
| `UniversalBearerAsAdequacyClaim` | A universal module, general substrate, or existing resource is used as better architecture because it can carry more functions. | Use `C.19.1` only when scale advantage is claimed; otherwise recover module-interface, coupling, evidence, control, safety, admissibility, and source-return effects before explicit comparison belongs to `A.19.CPM`, local choice to `C.11`, set-returning selection to `A.19.SelectorMechanism`, or publication of a selected set to `G.5`. |
| `ConwayNameAsRepair` | A warning row says Conway, mirroring, or inverse Conway but gives no architecture repair. | Open `C.32.CONWAY`; name the transformer and transformed holons, selected structures on both sides, changing relation, affected characteristics, candidate repair, loss, and stop condition. |

