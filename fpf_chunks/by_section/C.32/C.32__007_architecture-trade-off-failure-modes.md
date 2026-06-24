---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:6"
section_title: "Architecture Trade-Off Failure Modes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__007_architecture-trade-off-failure-modes.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:6 — Architecture Trade-Off Failure Modes"
line_start: 58782
line_end: 58796
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

### C.32:6 - Architecture Trade-Off Failure Modes

| Failure mode | C.32 repair action |
|---|---|
| **Local structure win hides other-scope loss** | A module split, control placement, evidence scope, or team responsibility change helps one concern while worsening another architecture characteristic. Rebuild the synthesis structure map and record the gained and lost characteristics before comparison. |
| **Function and architecture characteristic collapse** | The candidate is argued from user-visible function while evolvability, coupling, cohesion, latency, evidence burden, or another architecture characteristic remains unnamed. Recover the function through `A.6.F` or the structural-view pattern, then name the architecture characteristic separately. |
| **Function without feasible bearer** | A functional architecture, workflow, method step, or searched graph asks for a function that no admitted module, role, resource, placement, control relation, or evidence structure can carry. Repair the bearer set before admitting the candidate. |
| **No real trade-off** | Only one configuration is visible, or alternatives differ only by description. Generate structurally different candidates, or state why the project work is not architecture synthesis and return to the direct governing pattern. |
| **Description artifact stands in for candidate content** | A diagram, ADR, view, dashboard, benchmark output, or digital-twin view is the visible work product, but the selected structures and architecture-characteristic trade-off are still missing. Keep the visible work product under description-use, C.29 mathematical-lens use, benchmark, publication, or source-use governance and recover candidate content before C.32 use. |
| **Front member treated as durable optimum** | A front member, local winner, or benchmark leader is used as if the evolution window will stay fixed. Record evolution window, source-return condition, and retained alternatives through C.18 or C.19; use G.5 only when publishing a selected set after the receiving pattern has made that set available. |
| **Software-source overfit** | A software architecture source supplies a useful architecture-change idea, but the described holon is not a software system. Translate only the change over selected structures and characteristics; do not import the software ontology. |
| **Transformer-side architecture omitted** | The candidate architecture for a changed holon cannot be built, tested, deployed, certified, or evolved by the declared changing holon. Open `C.32.CONWAY` and prepare transformer-side change, transformed-side change, joint change, and bounded mismatch as candidate alternatives or comparison inputs. |
| **Method-defined dimensions lose their semantics** | A BIM, digital-twin, or view-method dimension already carries method-defined structure, constraint, cost, schedule, use-phase, or maintenance semantics, but the synthesis text keeps only the dimension name or dimension count. Preserve the method semantics and map them to selected structures, constraints, characteristics, and source-return conditions. |
| **Ideality shortcut** | Fewer bearers, fewer modules, or one universal module is only a candidate direction until functions, architecture characteristics, scale window, safety, admissibility, and losses are named. |

