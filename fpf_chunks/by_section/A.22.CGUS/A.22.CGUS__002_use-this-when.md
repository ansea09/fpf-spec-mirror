---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Which Continuations Are Available? — Constraint-Governed Unfolding Structure (CGUS)"
section_id: "A.22.CGUS:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__002_use-this-when.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "A.22.CGUS — Which Continuations Are Available? — Constraint-Governed Unfolding Structure (CGUS)"
  - "A.22.CGUS:0 — Use This When"
line_start: 42357
line_end: 42370
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
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
---

### A.22.CGUS:0 - Use This When

Use this pattern to work out which continuations the conditions of a case allow, including when a diagram shows only one path or no candidates have yet been named. Start with the recipient's question:

> Must I establish that this particular continuation is available, that some continuation exists, or which continuations make up the full set? If I must choose a way to proceed, what will let me identify and use it in time?

Use the required result, the choices open to the actors and the governing constraints to find potential continuations. A named way needs its own conditions. An existence claim can also follow from a rule covering the possible cases. A claim to give all the available ways, or to exclude them all, needs grounds covering the allowed range. Mark a candidate `unknown` when a missing fact or rule prevents deciding it. One established blocking condition can already exclude it. Stop when the answer supplies the requested use.

Open the formal branch when a named use needs the identity and qualification of the unfolding organization as a CGUS. A `ConstraintGovernedUnfoldingStructure` (CGUS) is one A.22 `U.Structure` whose locally named loci, constituents, obtaining relations, and constraints define at least two potential continuations across the cases allowed by those constraints. A separate result says which alternatives are enabled, disabled, unknown, or error for one case and time window.

Do not use CGUS merely because a card, graph, table, narrative, prompt path, or README line looks route-shaped. A single recommendation or displayed sequence is not enough. The structure may branch, join, cycle through subject relations, remain partially ordered, or leave several alternatives live at once. A result with zero or one enabled alternative can still concern that same branching structure.

**What changes in practice.** Practitioners can develop alternatives from the work required or assess alternatives already proposed. Their answer supplies the continuation, existence finding or complete range the recipient needs. They keep potential structure separate from the result for the present case, and they mark an alternative `unknown` when an unresolved fact or rule prevents deciding it. Display order alone neither prescribes nor performs Work.

