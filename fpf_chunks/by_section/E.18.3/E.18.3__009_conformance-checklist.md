---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__009_conformance-checklist.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:7 — Conformance Checklist"
line_start: 78381
line_end: 78391
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.29"
  - "C.30.TFS-REL"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.2"
  - "E.23"
  - "G.11"
keywords:
---

### E.18.3:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-E18.3-1 Transformation substrate.** | Bounded transformations, transformation loci, and transformed concern are named. | Use `A.22.CGUS` or another direct pattern instead of E.18.3. |
| **CC-E18.3-2 Flow structure.** | Transfer or dependency relations, path or path-slice refs, crossings, guards, and optional valuation are recoverable. | Lower to a route card, graph description, or ordinary explanation. |
| **CC-E18.3-3 Adjacent locus boundary.** | Method, work, evidence, gate, architecture, publication, and refresh claims point to direct governing patterns. | Add direct exits or narrow the claim to the transformation-flow structure. |
| **CC-E18.3-4 Preserved and lost structure.** | Preserved and lost or hidden transformation structure are named. | Add them before using the structure for action, comparison, architecture, or publication. |
| **CC-E18.3-5 Stop or return.** | Stop, return, governing-pattern-specific repair, and currentness-refresh conditions are recoverable. | Add the condition or keep the slice as a one-use example. |
| **CC-E18.3-6 Non-chain topology.** | Branches, joins, cycles, partial orders, and guarded alternatives are preserved or explicitly lost when the flow is graph-shaped. | Treat any linear path as a demonstrative slice, not the whole flow structure. |

