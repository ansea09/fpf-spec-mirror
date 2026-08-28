---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:6"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__009_conformance-checklist.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:6 — Conformance checklist"
line_start: 58878
line_end: 58891
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.3.NAR"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD.BA"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.5"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "candidate-description boundary"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:6 - Conformance checklist

| Check | Condition to establish | Repair if failed |
| --- | --- | --- |
| **CC-C30AD-1 Episteme identity.** | Every architecture description has one exact claim graph, one exact EntityOfConcern—holon, obtaining `ArchitectureRelation` occurrence, or selected structure—and an effective `U.ReferenceScheme`. | Add the missing C.2.1 identity component or use `C.30`/`A.22` until the subject-side object is recoverable. |
| **CC-C30AD-2 Subject and holon recovery.** | The one EntityOfConcern is supplied directly. If it is an architecture-relation occurrence or selected structure, its participant trace recovers the exact holon without copying that holon into description identity; architecture-claim refs remain optional content or trace. | Restore the exact EntityOfConcern and participant trace; remove derived identity from an optional architecture-claim field. |
| **CC-C30AD-2a Traceable multi-view chain.** | The reader can recover the concern, viewpoint, conformance relation, same episteme as `U.View`, EntityOfConcern, selected structure, optional actual architecture relation, set use, and next architecture move. Add allocation, responsibility, source use, representation, publication, correspondence, project use, or stronger-use return only when it is current. Responsibility names its own predicate and participants or the missing governor; assignment and viewpoint establish neither responsibility nor authority. | Add the missing object or relation, narrow the allowed use, or use the pattern that defines how to recover it. |
| **CC-C30AD-3 Viewpoint and structure kind.** | Every asserted architecture structural view identifies the candidate episteme, exact viewpoint episteme, independently obtaining five-part E.17.0 conformance relation, selected structure, and structure kind. | Use `E.17.0` and `C.30.ASV` before relying on the view; a label, query, bundle, diagram, or publication is insufficient. |
| **CC-C30AD-4 Correspondence and source use.** | Cross-view use names a correspondence claim or independently obtaining relation; source-derived or reused use names its source-to-use path; a source-return condition is present only when stronger use opens return to the named source or exact defining or constraining ClaimGraph. | Add the missing claim or direct relation, or narrow the admissible use. |
| **CC-C30AD-5 Representation and publication boundary.** | A diagram, rendering, publication occurrence or form, dashboard, card, file, or carrier is not treated as architecture, selected structure, `U.View`, truth, decision, evidence, assurance, gate passage, Work, authorization, or release. | Use `C.2.P`, `E.17`, `E.24.PUB`, or the pattern for the actual representation, publication, source-use, or other non-description claim. |
| **CC-C30AD-6 Specification-use boundary.** | Specification use names the description episteme or publication. Project locality additionally names one composite `U.Work` and a project-use relation that actually holds; separate non-description claims cite their applicable patterns. | Add the description, Work, and use relation as needed, or keep the use non-project-specific. |
| **CC-C30AD-7 Remaining architecture candidate use.** | Under the declared use boundary, the description still identifies the next architecture move, view repair, source repair, return condition, or pattern needed for a separate claim. | Add that remaining use or reduce the account to source, representation, or publication use. |
| **CC-C30AD-8 Coarse-graining boundary.** | A coarsening claim names the described subject, finer and coarser description structures, their mapping or correspondence, distinctions preserved and lost, and allowed use. It asserts no matching subject levels, parts, or relations without a separate subject-side basis. | Add the missing description facts, narrow the use, or establish the needed subject relation through its own pattern. |

