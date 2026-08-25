---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 61639
line_end: 61670
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
  - "C.32.MWA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
  - "U.Structure"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "selected-structure contribution rows"
  - "trade-off front"
---

### C.32:8 - Common Anti-Patterns and How to Avoid Them

#### C.32:8.1 - Architecture trade-off failures

| Anti-pattern | Repair |
|---|---|
| **Local structure win hides other-scope loss.** A module split, control placement, evidence scope, or direct responsibility-relation change helps one concern while worsening another architecture characteristic. | Rebuild the selected-structure contribution rows and record the gained and lost characteristics before comparison; do not infer responsibility from a team label or assignment. |
| **Function and architecture characteristic collapse.** The candidate is argued from user-visible function while evolvability, coupling, cohesion, latency, evidence burden, or another architecture characteristic remains unnamed. | Recover the function through `A.6.F` or the structural-view pattern, then name the architecture characteristic separately. |
| **Function without feasible bearer.** A functional architecture, workflow, Method step, or searched graph asks for a function but A.6.F identifies no bearer that satisfies the functional predicate under the relevant module, resource, placement, control, evidence, local-kind, classification, or assignment constraints. | Repair the bearer claim before admitting the candidate. |
| **No real trade-off.** Only one configuration is visible, or alternatives differ only by description. | Generate structurally different candidates, or state why the project work is not architecture synthesis and use the subject pattern. |
| **Description artifact stands in for candidate content.** A diagram, ADR, view, dashboard, benchmark output, or digital-twin view is the visible work product, but the selected structures and architecture-characteristic trade-off are still missing. | Keep the visible work product with its description-use, C.29 mathematical-lens, benchmark, publication, or source-use pattern and recover candidate content before C.32 use. |
| **Front member treated as durable optimum.** A front member, local winner, or benchmark leader is used as if the evolution window will stay fixed. | Record evolution window, source-return condition, and retained alternatives under the exact C.18 or C.19 predicates; use G.5 only to declare a selected-set result from those alternatives. If the result is published, use E.17 for a source-backed face and source return and E.24.PUB for the publication occurrence and audience availability. |
| **Software-source overfit.** A software architecture source supplies a useful architecture-change idea, but the described holon is not a software system. | Translate only the change over selected structures and characteristics; do not import the software ontology. |
| **Architecture-influence source omitted.** The candidate architecture for a changed referent cannot be built, tested, deployed, certified, or evolved under the current architecture, Work, communication, method, tool, deployment, evidence, selected-structure, or other source, but that source's exact kind and influence status are hidden. | Open `C.32.CONWAY`; recover the source kind and either its exact obtaining direct relation or the precise provisional disposition, keep the acting System, any local system-role kind or assignment, Work, changed referent, and any actual transformation distinct, and prepare influence-source-side change, transformed-side change, joint change, and bounded mismatch as candidate alternatives or comparison inputs. |
| **Method-defined dimensions lose their semantics.** A BIM, digital-twin, or view-method dimension already carries method-defined structure, constraint, cost, schedule, use-phase, or maintenance semantics, but the synthesis text keeps only the dimension name or dimension count. | Preserve the method semantics and map them to selected structures, constraints, characteristics, and source-return conditions. |
| **Ideality shortcut.** Fewer bearers, fewer modules, or one universal module is only a candidate direction until functions, architecture characteristics, scale window, safety, admissibility, and losses are named. | Keep it as one candidate and expose those missing tests before comparison. |

#### C.32:8.2 - More repair cues

| Repair cue | Symptom | First repair |
|---|---|---|
| `SingleStructureSynthesis` | One structure is optimized and the result is called the architecture. | Write the selected-structure contribution rows and name the architecture characteristics before admitting the candidate as C.32 work. |
| `UserFunctionAsArchitectureCharacteristic` | The user-visible function is treated as the architecture quality being optimized. | Recover the functional demand through `A.6.F` or `C.30.ASV`; then name the architecture characteristic or quality bundle separately. |
| `FunctionNoFeasibleBearer` | A functional architecture names a required function, but no bearer satisfies the A.6.F predicate under the relevant System, module, Method, resource, placement, control, evidence, local-kind, classification, or assignment constraints. | Repair with `functionBearerFeasibilityRepair`: add or change the bearer, split the function, change placement or resource access, change control relations, reduce the demand, or reject the candidate. A kind or assignment never becomes the bearer by form, and any responsibility claim remains a separate direct predicate or exact missing governor. |
| `DescriptionFormAsArchitecture` | An architecture-description artifact is treated as the architecture because it is the most visible representation. | Keep the visible work product under `C.30.AD`, `C.30.ASV`, `E.17`, `E.24.PUB`, `C.29`, or source-use governance as applicable; recover described holon, selected structures, candidate architecture change, and characteristic bundle before admitting any C.32 candidate. |
| `BenchmarkWinnerAsArchitecture` | A comparison result is treated as architecture selection. | Treat the result as comparison input or as source material for an A.10 evidence relation when that claim is current; admit a C.32 candidate only after selected structure, architecture-change kind, gain, loss, and pattern for the next question are recovered. |
| `MethodDimensionSemanticsLost` | A BIM, digital-twin, or architecture-view method supplies dimensions, but C.32 use keeps only the dimension name or dimension count and loses the method's structure, constraint, schedule, cost, use-phase, or maintenance semantics. | Preserve the source method semantics, then map each method-declared dimension to selected structures, constraints, preserved and lost structure, architecture characteristics, and source-return condition. |
| `ArchitectureInfluenceMismatch` | One independently typed source is incompatible with transformed-side architecture content needed for the changed referent, or the source's influence status is still provisional. | Open `C.32.CONWAY`; recover the changed referent, each source's exact kind and obtaining relation or precise provisional disposition, both exact C.30 architecture sides or modal claims, and any separately grounded acting, Work, method-side or direct method-use relation, A.3.4 transformation, or E.18 flow facts through their subject patterns; generate candidates that change the influence-source side, the transformed side, both sides, or a bounded mismatch. Use `C.29` only if structural similarity is claimed. |
| `ShortlistByName` | A set is called shortlist before the result fields required by `G.5` exist. | Keep it as a local palette or open `G.5`. |
| `UniversalBearerAsArchitecture` | A universal module, general substrate, or existing resource is treated as better architecture by name. | Create a C.32 candidate that names functions transferred to the bearer, bearer count change, coupling change, evidence burden, control burden, safety and admissibility boundary, and BLP scale window or waiver if scale advantage is claimed. |
| `SourceCompressionNoReturn` | A candidate hides source distinctions. | Add a source-return condition or demote the item to a source cue. |

