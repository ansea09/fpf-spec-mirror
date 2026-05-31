---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__002_use-this-when.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:0 — Use this when"
line_start: 51936
line_end: 51960
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.8"
  - "J.4"
keywords:
---

### C.30.P:0 - Use this when

Use this pattern when architecture or structure wording hides which object is live.

Typical triggers:

- `architecture`, `architecture description`, `architecture model`, `architecture diagram`, `architecture map`, `architecture dashboard`, `architecture score`;
- `structure`, `structural view`, `structural model`, `layer`, `module layout`, `block`, `component structure`, `interface structure`;
- `graph`, `flow`, `TGA graph`, `control sketch`, `LCA diagram`, `ADR`, `dashboard`, `benchmark`, `source`, or `view` being treated as architecture or structure by wording alone;
- a function, module, interface, signature, flow, control, quality, score, evidence, assurance, gate, work, decision, causal-use, or release claim being smuggled under architecture/structure wording.

**What goes wrong if missed.** A diagram becomes the architecture, a graph becomes proof, a view becomes the selected structure, a source document becomes an architecture decision, a score becomes architecture adequacy, or a function/module/interface claim becomes architecture by default.

**What this buys.** The reader can recover the live object, block the overread, and move to the exact pattern: selected structure under `A.22`, architecture description under `C.30`, architecture structural view under `C.30.ASV`, TGA-flow relation under `C.30.TGA-FLOW-REL`, control-structure view under `C.30.LCA`, mathematical lens under `C.29`, characteristic/scale repair under `C.16.P`, or a project-side evidence, assurance, gate, work, decision, causal-use, release, or publication pattern.

**First useful move.** Ask what object the architecture or structure wording is actually naming, then either apply the exact architecture/structure pattern directly or use one `architecture-structure repair note` to assign the claim elsewhere.


**Not this pattern when.**

- If the live object is already a selected structure, use `A.22` directly.
- If the live object is already `ArchitectureOf@Context` or `ArchitectureDescription@Context`, use `C.30` directly.
- If the live object is already an architecture structural view, use `C.30.ASV` or an exact `C.30.*` view pattern directly.
- If the live claim is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens adequacy, characteristic/scale construction, quality characterization, source-transfer, or relation construction, use the exact pattern for that claim after any architecture/structure wording is demoted or assigned.

