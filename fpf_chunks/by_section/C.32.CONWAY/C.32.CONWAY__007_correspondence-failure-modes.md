---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:6"
section_title: "Correspondence Failure Modes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__007_correspondence-failure-modes.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:6 — Correspondence Failure Modes"
line_start: 65370
line_end: 65388
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.19.CPM"
  - "A.22"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3"
  - "C.11"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ACS"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "E.18.NET"
  - "G.5"
keywords:
---

### C.32.CONWAY:6 - Correspondence Failure Modes

| Failure mode | C.32.CONWAY repair action |
|---|---|
| **Architecture-as-actor** | Replace the acting architecture with the exact `U.System`, role assignment, dated Work, and actor-side or work-to-change relation; keep architecture as a separately related influence source. |
| **Influence-as-performance** | Remove role, Work, performer, or transformation-participation inferences that came only from influence. Establish those facts independently or leave them absent. |
| **Changed referent omitted** | Identify the exact referent and changing relation before deciding which architecture is transformed. |
| **Performer without Work basis** | When performance is claimed, add exact dated Work, `performedUnderAssignment(W, RA)`, holder-system equality, and required direct relations; use A.15.1 multiple-performer forms when needed. |
| **Influence source without governor** | Apply the direct relation owner. With no kind/predicate, keep the correspondence synthesis-local and return `missing-governor`; with unresolved facts, name the grounding boundary; with a false predicate, remove the influence occurrence. |
| **Architecture-bearer equality with an actor inferred** | Keep the influence-source holon and acting system unequal unless independent actor and architecture-bearer facts establish equality. |
| **Transformed-side-only inverse Conway** | If the text says inverse Conway but changes only the transformed architecture, name the exact influence-source selected structure that must change or stop using the inverse-Conway claim. |
| **Source-side change without transformed pressure** | If an organization, method, line, or toolchain is reorganized without one transformed architecture and characteristic under pressure, return to the direct Work or organization-design use. |
| **One-sided optimization** | Prepare source-side change, transformed-side change, joint change, and bounded mismatch candidates before claiming the correspondence has been constructively handled. |
| **Pair treated as network** | Keep the exact pair row as one qualified reading; use E.18.NET for network identity, members, and exact cross-flow relations. |
| **Network citation treated as relation admission** | Ground the exact relation participants in member-flow positions and make the E.18.NET composite locator name that same citing current record and exactly one cross-flow row; otherwise remove `networkCrossFlowRelationRowRef`. A locator for one record does not qualify another record's citation. |
| **Mirroring treated as adequacy** | Keep the statement as candidate pressure or use C.29 when structural similarity or preservation is claimed. |
| **Software-practice overfit** | When the changed referent is a product family, manufacturing system, school, hospital, or another admitted non-software holon, transfer only the selected-structure correspondence and affected characteristics; do not import software-service or team ontology. A method-family or method-description label alone does not make the named object a `U.Holon`; if the case uses a method-related holon, identify that exact holon and admit it independently under its direct kind owner. |
| **Static correspondence** | Reopen when either architecture, selected structure, relation occurrence, changed referent, or evolution window changes. |

