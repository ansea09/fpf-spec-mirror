---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:16"
section_title: "Revision law"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__020_revision-law.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:16 — Revision law"
line_start: 80505
line_end: 80513
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:16 - Revision law

1. **Edition shift in a context.** Re-evaluate affected cells; if sense moved, split the Bridge or lower `CL`.
2. **New mismatch evidence.** Add a counter-example; decrease `CL` or change kind.
3. **Convergence.** Raise `CL` only when invariants demonstrably match and counter-examples no longer apply.
4. **senseFamily correction.** If a cell's `senseFamily` was mistyped, fix the cell first in F.3, then revisit Bridges.
5. **Row overreach.** If a row's use exceeds the weakest Bridge, split the row or lower its admitted use.
6. **Bridge sprawl.** Consolidate near-duplicates into one Bridge with richer Loss Notes.

