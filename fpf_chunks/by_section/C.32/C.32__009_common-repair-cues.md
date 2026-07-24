---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:8"
section_title: "Common Repair Cues"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__009_common-repair-cues.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:8 — Common Repair Cues"
line_start: 63336
line_end: 63350
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "synthesis structure map"
  - "trade-off front"
---

### C.32:8 - Common Repair Cues

| Repair cue | Symptom | First repair |
|---|---|---|
| `SingleStructureSynthesis` | One structure is optimized and the result is called the architecture. | Build the synthesis structure map and name the architecture characteristics before admitting the candidate as C.32 work. |
| `UserFunctionAsArchitectureCharacteristic` | The user-visible function is treated as the architecture quality being optimized. | Recover the functional demand through `A.6.F` or `C.30.ASV`; then name the architecture characteristic or quality bundle separately. |
| `FunctionNoFeasibleBearer` | A functional architecture names a required function, but no admitted module, role, method, resource, placement, control relation, or evidence structure can carry it. | Repair with `functionBearerFeasibilityRepair`: add or change a bearer, split the function, change placement or resource access, change control responsibility, reduce the demand, or reject the candidate. |
| `DescriptionFormAsArchitecture` | An architecture-description artifact is treated as the architecture because it is the most visible representation. | Keep the visible work product under `C.30.AD`, `C.30.ASV`, `E.17`, `E.24.PUB`, `C.29`, or source-use governance as applicable; recover described holon, selected structures, candidate architecture change, and characteristic bundle before admitting any C.32 candidate. |
| `BenchmarkWinnerAsArchitecture` | A comparison result is treated as architecture selection. | Treat the result as comparison input or as source material for an A.10 evidence relation when that claim is current; admit a C.32 candidate only after selected structure, architecture-change kind, gain, loss, and receiving pattern are recovered. |
| `MethodDimensionSemanticsLost` | A BIM, digital-twin, or architecture-view method supplies dimensions, but C.32 use keeps only the dimension name or dimension count and loses the method's structure, constraint, schedule, cost, use-phase, or maintenance semantics. | Preserve the source method semantics, then map each method-declared dimension to selected structures, constraints, preserved and lost structure, architecture characteristics, and source-return condition. |
| `TransformerTransformedMismatch` | The architecture of the holon doing the changing cannot produce, test, maintain, evolve, or certify the architecture desired for the changed holon. | Open `C.32.CONWAY`; recover the changing relation through `A.3.4`, `E.18`, work, or method patterns; generate candidates that change the transformer side, the transformed side, both sides, or a bounded mismatch. Use `C.29` only if structural similarity is claimed. |
| `ShortlistByName` | A set is called shortlist before the fields required by `G.5` publication exist. | Keep it as a local palette or open `G.5`. |
| `UniversalBearerAsArchitecture` | A universal module, general substrate, or existing resource is treated as better architecture by name. | Create a C.32 candidate that names functions transferred to the bearer, bearer count change, coupling change, evidence burden, control burden, safety and admissibility boundary, and BLP scale window or waiver if scale advantage is claimed. |
| `SourceCompressionNoReturn` | A candidate hides source distinctions. | Add a source-return condition or demote the item to a source cue. |

