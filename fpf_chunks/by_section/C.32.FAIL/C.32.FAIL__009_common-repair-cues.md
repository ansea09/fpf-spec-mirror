---
chunk_kind: "child"
pattern_id: "C.32.FAIL"
pattern_title: "Architecture Failure Recognition and Repair"
section_id: "C.32.FAIL:8"
section_title: "Common repair cues"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.FAIL/C.32.FAIL__009_common-repair-cues.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.32.FAIL — Architecture Failure Recognition and Repair"
  - "C.32.FAIL:8 — Common repair cues"
line_start: 66832
line_end: 66847
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.27"
  - "C.29"
  - "C.3"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.P"
  - "C.31"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "E.18"
  - "E.18.NET"
  - "E.24.PUB"
  - "F.6"
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
| `WarningNameOnly` | A memorable warning name does not change the next repair action. | Add the architecture object, blocked overread, subject pattern, and repair action, or remove the row. |
| `EverythingIsFailureCue` | Any architecture worry is admitted as a C.32.FAIL cue. | Admit only recurring failures that change the first architecture repair action. |
| `AuditPromptAsPattern` | The row says to measure, review, or audit. | Demote it unless it names the architecture object and repair action first. |
| `EvidenceAsRepair` | More evidence is treated as the repair. | Name the architecture repair first; evidence may follow under its own pattern. |
| `DecisionInsideRepairCue` | The cue says which architecture to choose. | Local choice belongs to `C.11`; project architecture decision belongs to `C.32.PAD` after the candidate repair is available. |
| `DescriptionCarrierAsRepair` | A diagram, report, dashboard, or publication face is treated as the repair. | Use `C.30.AD` for description use, `E.17` for a source-backed publication face and source return, and `E.24.PUB` for the publication occurrence and audience availability. Keep dashboard, report, or generated-carrier use under its source-use or publication relation. Keep C.32.FAIL only if an architecture object under stress and repair action are named. |
| `FunctionAsQuality` | A function such as teach, compute, certify, or regulate is treated as the architecture characteristic. | Recover the function under `A.6.F` and name the separate architecture characteristic or quality bundle. |
| `FunctionalGraphNoBearer` | A functional graph, workflow, or method structure names a required function that no admitted bearer can perform under the module, placement, resource, control, or evidence constraints declared for the case. | Use C.32; add or change bearer, split function, change placement or resource access, change control responsibility, reduce demand, or reject the candidate. |
| `IdealityAsAdequacyShortcut` | The phrase ideal architecture, no modules, or fewer parts is used as architecture adequacy by itself. | Convert it into a C.32 candidate and name function bearing, lost structure, new burden, architecture characteristics, and pattern for the next question. |
| `UniversalBearerAsAdequacyClaim` | A universal module, general substrate, or existing resource is used as better architecture because it can carry more functions. | Use `C.19.1` only when scale advantage is claimed. Otherwise recover module-interface, coupling, evidence, control, safety, admissibility, and source-return effects before stating an explicit comparison under `A.19.CPM`, local choice under `C.11`, set-returning selection under `A.19.SelectorMechanism`, or selected-set result declaration under `G.5`. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the occurrence and audience availability. |
| `ConwayNameAsRepair` | A warning row says Conway, mirroring, or inverse Conway but gives no architecture repair. | Open `C.32.CONWAY`; name the changed referent, the exact influence-source-side and transformed-side C.30 architecture relations or modal claims, the direct influence kind/predicate/occurrence or truthful stop, affected characteristics, candidate form, gain, loss, and pattern for the next question. Keep actors, assignments, Work, actual transformation, and any E.18.NET network or cross-flow occurrence with their subject patterns. |

