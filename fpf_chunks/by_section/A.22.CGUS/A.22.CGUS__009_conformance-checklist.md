---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__009_conformance-checklist.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:7 — Conformance Checklist"
line_start: 31530
line_end: 31542
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "B.3.5"
  - "B.5.2"
  - "C.13"
  - "C.2.P.DR"
  - "C.3"
  - "C.32.P2S"
  - "C.35"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.23"
  - "E.9"
  - "E.9.DA"
  - "G.11"
keywords:
---

### A.22.CGUS:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-CGUS-1 Structure kind.** | The object is `ConstraintGovernedUnfoldingStructure@Context <: U.Structure` or a named narrower `U.Structure` specialization. | Lower to note, seed, description, route card, method description, or governing-pattern record. |
| **CC-CGUS-2 Loci and constraints.** | Several loci and cross-locus constraints are named. | Add loci and constraints or stop using CGUS. |
| **CC-CGUS-3 Description separation.** | Descriptions, views, diagrams, tables, graph expressions, narratives, slides, and README entries do not become the structure. | Recast them as `ConstraintGovernedUnfoldingStructureDescription` or `DemonstrativeUnfoldingSlice` with declared use. |
| **CC-CGUS-4 Direct governing patterns.** | Method, work, evidence, gate, decision, architecture, publication, refresh, and mathematical claims point to direct governing patterns. | Add governing-pattern exits or narrow the claim. |
| **CC-CGUS-5 Non-workflow boundary.** | The structure does not prescribe performed-work order by itself. | Move work-order claims to a work plan or method description if justified. |
| **CC-CGUS-6 Admissible next form.** | At least one admissible next form or demonstrative slice is named. | Keep the artifact internal until a next use is recoverable. |
| **CC-CGUS-7 Stop and return.** | Stop, split, return, and currentness-refresh conditions are recoverable where relevant. | Add the condition or lower the structure to a one-use explanation. |
| **CC-CGUS-8 Graph-shaped structure coverage.** | If the admitted starting record set, starting structure set, or visible expression is graph-shaped, case-like, or workflow-shaped, branching, joining, cyclic, partial-order, and alternative-live-next-form structure is preserved or explicitly lost. | Do not collapse the object to a chain. Make the chain a demonstrative slice and name the omitted graph structure. |

