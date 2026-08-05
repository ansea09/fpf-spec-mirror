---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__009_conformance-checklist.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:7 — Conformance Checklist"
line_start: 35192
line_end: 35207
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "B.3.5"
  - "B.5.2"
  - "C.13"
  - "C.18"
  - "C.19"
  - "C.2.P.DR"
  - "C.3"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.18.NET-conforming"
  - "E.23"
  - "F.17"
  - "G.11"
  - "G.5"
keywords:
---

### A.22.CGUS:7 - Conformance Checklist

| ID | Passing condition | Failed-check repair |
| --- | --- | --- |
| **CC-CGUS-1 A.22 identity.** | The current object is one selected `U.Structure` with exact independently identified constituents, exact selected obtaining relation occurrences, exact applied constraints, and one named selection-use frame; the `ConstraintGovernedUnfoldingStructure` profile adds no ambient context discriminator. | Recover the missing A.22 discriminator, or lower to the current note, record, graph, table, or description. |
| **CC-CGUS-2 Typed positions and cross-position constraints.** | More than one filled `CGUSPositionLocator` resolves an independently established selected constituent, and exact already-obtaining relations or applied constraints among those constituents change admissible continuations. | Recover the missing constituent, SlotSpec, relation occurrence, or constraint; an empty row remains provisional. |
| **CC-CGUS-3 Episteme separation.** | A pre-admission presentation is a C.2.1 episteme about the actual question or proposed continuation set; a whole-structure description and one demonstrative slice are distinct C.2.1 epistemes whose exact EntityOfConcern is the admitted CGUS. None is the selected structure. | Keep the presentation provisional until admission, then identify each needed episteme by its own ClaimContent, EntityOfConcern, and effective ReferenceScheme. |
| **CC-CGUS-3a Transformation-flow locator exclusivity.** | A one-TFS slice has the complete top-level E.18 triple and no network locator; a network slice has one network locator and none of the three top-level E.18 fields; a generic slice may have neither family. No partial or mixed family is present. | Restore one complete family, or remove transformation-flow provenance and keep the slice generic. |
| **CC-CGUS-3b Network locator admission reuse.** | Every position ref agrees with the exact network, recursive member path, and leaf position and resolves the same admitted `CGUSPositionLocator` already used by the slice and E.18.3 structure. Every selected cross-flow row resolves exactly one row in the current record and cites an exact already-admitted relation-reference episteme. Member-local TFS locators retain boundaries, Work, transformations, valuations, path slices, and tags; the network has no global copy. | Return the mismatched network, path, leaf, record, position, relation, or binding. Remove copied position lists and global state. |
| **CC-CGUS-3c Flow/subflow/network discriminator.** | Several valuations retain one TFS identity; one internal portion remains one parent-relative `SubflowRef`; independent flows or nested networks plus exact cross-boundary occurrences use E.18.NET. Membership is acyclic while directly governed feedback may cycle. | Use E.18 or E.18.NET; remove the valuation-created flow, detail-created member, giant flattened flow, or cyclic membership. |
| **CC-CGUS-4 Concrete stronger claims and method-description threshold.** | Every stronger method, MethodDescription, plan, Work, transformation, production, evidence, gate, decision, architecture, publication, source-use, currentness, or mathematical claim is explicit and names the concrete definition, constraint, test, method, evidence rule, or assurance rule it uses. A pattern reference, intended realization, ordering claim, recommendation, or imperative grammar admits no `U.MethodDescription` or Work. | State the concrete contribution, apply A.3.2 only to an already identified episteme about one admitted Method, or narrow the claim. |
| **CC-CGUS-5 Non-workflow boundary.** | The structure does not prescribe performed-work order by itself. | Move work-order claims to a work plan or method description if justified. |
| **CC-CGUS-6 Admissible next form.** | At least one admissible next-form kind is named for the admitted structure. | Keep the artifact as a provisional description until a next use and next-form kind are recoverable. |
| **CC-CGUS-7 Stop, reconsideration, and currentness reference.** | Stop and reconsideration boundaries name the condition, affected structure, and next unresolved question; any currentness claim is an exact referenced relation under `G.11`. | Add the boundary, question, or referenced currentness relation, or lower the structure to a one-use explanation. |
| **CC-CGUS-8 Graph-shaped structure coverage.** | If the admitted starting record set, starting structure set, or visible expression is graph-shaped, case-like, or workflow-shaped, branching, joining, cyclic, partial-order, and alternative-live-next-form structure is preserved or explicitly lost. | Do not collapse the object to a chain. Keep the chain provisional before admission, or make it an admitted slice afterward and name the omitted graph structure. |

