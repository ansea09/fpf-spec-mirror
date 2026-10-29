---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Clarify Architecture and Structure Wording (Precision Restoration)"
section_id: "C.30.P:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__002_use-this-when.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "C.30.P — Clarify Architecture and Structure Wording (Precision Restoration)"
  - "C.30.P:0 — Use this when"
line_start: 72099
line_end: 72122
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.8"
  - "G.5"
keywords:
  - "architecture description"
  - "architecture wording"
  - "diagram"
  - "model"
  - "precision restoration"
  - "structural view"
  - "structure wording"
---

### C.30.P:0 - Use this when

Use this pattern when architecture or structure wording hides which use is being made.

Typical triggers:

- `architecture`, `architecture description`, `architecture model`, `architecture diagram`, `architecture map`, `architecture dashboard`, `architecture score`;
- `structure`, `structural view`, `structural model`, `module layout`, `component structure`, `interface structure`, or stratification wording or source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` whose technical meaning must be recovered through `C.30.STRAT` before local architecture or structure assignment;
- `graph`, `flow`, `transformation-flow graph expression`, `control sketch`, `LCA diagram`, `ADR`, `dashboard`, `benchmark`, `source`, or `view` being treated as architecture or structure by wording alone;
- a function, module, interface, signature, flow, control, quality, score, evidence, assurance, gate, work, decision, causal-use, or release claim being smuggled under architecture or structure wording.

**What goes wrong if missed.** A diagram becomes the architecture, a graph becomes proof, a view becomes the selected structure, a source document becomes an architecture decision, a score becomes architecture adequacy, or a function, module, or interface claim becomes architecture by default.

**What this buys.** The reader can state the intended claim, retain its useful content, and use the pattern that addresses the remaining question. Clear ordinary wording needs no repair record.

**First useful move.** Recover what the sentence says and what the reader needs to do with it. Keep adequate ordinary wording. Otherwise rewrite the ambiguous claim, then use its subject pattern for any remaining substantive question. A repair note is optional when the repair needs to remain inspectable.

**Not this pattern when.**

- If the use under repair is already a selected structure, use `A.22` directly.
- For an already recoverable `ArchitectureRelation` or bounded `ArchitectureClaim`, use `C.30` directly. For architecture-description identity, correspondence or use, use `C.30.AD`; use `C.30` for the initial description question tied to one architecture move.
- If the use under repair is already an architecture structural view, use `C.30.ASV` or a named `C.30.*` view pattern directly.
- If the claim being made is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens use, characteristic and scale construction, quality characterization, source-use, or relation construction, use the subject pattern for that claim after any architecture or structure wording is demoted or assigned.

