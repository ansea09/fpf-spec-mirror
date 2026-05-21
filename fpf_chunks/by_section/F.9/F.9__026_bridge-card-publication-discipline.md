---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:24"
section_title: "Bridge Card Publication Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__026_bridge-card-publication-discipline.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:24 — Bridge Card Publication Discipline"
line_start: 63690
line_end: 63710
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "A.6.Q"
  - "B.3"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
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

### F.9:24 - Bridge Card Publication Discipline

#### F.9:24.1 - Minimal bridge-card declaration
A usable Bridge Card should make visible:

- the two typed SenseCells,
- the bridge kind,
- direction where direction matters,
- declared `senseFamily`,
- `CL`,
- explicit Loss Notes,
- and the Bridge-supported use or row consequence.

If any of these fields is absent, later readers are forced back into inference by prose similarity, which is exactly what `F.9` is supposed to block.

#### F.9:24.2 - One-pair default rule
The default declaration discipline is one primary Bridge per cell pair per relevant `senseFamily`, with richer Loss Notes rather than many near-duplicate cards. Local exceptions are admissible only when the cards genuinely differ in bridge kind, direction, or admissible use.

#### F.9:24.3 - Revision over silent drift
If later evidence changes bridge `CL`, direction, or loss, the Bridge Card should be revised explicitly. It should not be left in place while surrounding prose quietly changes the practical scope.

