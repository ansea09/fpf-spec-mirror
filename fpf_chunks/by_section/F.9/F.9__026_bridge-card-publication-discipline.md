---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:25"
section_title: "Bridge Card publication discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__026_bridge-card-publication-discipline.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:25 — Bridge Card publication discipline"
line_start: 90035
line_end: 90059
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

### F.9:25 - Bridge Card publication discipline

#### F.9:25.1 - Minimal declaration

A usable Bridge Card makes visible:

* the two typed `SenseCells`,
* bridge kind,
* direction when direction matters,
* declared `senseFamily` for each cell,
* `CL`,
* Loss Notes,
* counter-example or invariant evidence,
* admitted use and non-admitted use.

If any of these fields is absent, readers are forced back into inference by prose similarity, which F.9 blocks.

#### F.9:25.2 - One-pair default rule

The default declaration discipline is one primary Bridge per cell pair per relevant `senseFamily`, with richer Loss Notes rather than many near-duplicate cards. Local exceptions are admissible only when the cards genuinely differ in bridge kind, direction, `CL`, or admitted use.

#### F.9:25.3 - Revision over silent drift

If evidence changes bridge `CL`, direction, loss, or admitted use, revise the Bridge Card explicitly. Do not leave the Bridge in place while surrounding prose quietly changes its practical scope.

