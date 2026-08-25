---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__002_use-this-when.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:0 — Use This When"
line_start: 34171
line_end: 34184
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
---

### A.22.CGUS:0 - Use This When

Use this pattern when a diagram or explanation shows several possible next actions, but readers may mistake one displayed path for the required work sequence. Start with one ordinary question:

> Which alternatives are available now, and what condition blocks each one?

Name the decision, the visible alternatives, the condition for each alternative, and the facts available now. If a needed fact or rule is missing, mark that alternative `unknown` and stop when this answers the practical question. A useful explanation need not first become a formal record or an admitted structure.

Open the formal branch only when the team must qualify, persist, compare, publish, or rely more strongly on the structure. A `ConstraintGovernedUnfoldingStructure` (CGUS) is one A.22 `U.Structure` whose locally named loci, constituents, obtaining relations, and constraints define at least two potential continuations across the cases allowed by those constraints. A separate result says which alternatives are enabled, disabled, or unknown for one case and time window.

Do not use CGUS merely because a card, graph, table, narrative, prompt path, or README line looks route-shaped. A single recommendation or displayed sequence is not enough. The structure may branch, join, cycle through subject relations, remain partially ordered, or leave several alternatives live at once. A result with zero or one enabled alternative can still concern that same branching structure.

**What changes in practice.** Practitioners correct the visible alternatives and their conditions before completing formal fields. They keep potential structure separate from the result for the present case, and they stop at the first unresolved fact instead of inventing a continuation. Display order alone neither prescribes nor performs Work.

