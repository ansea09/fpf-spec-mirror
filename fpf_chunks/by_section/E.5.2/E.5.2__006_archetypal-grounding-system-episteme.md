---
chunk_kind: "child"
pattern_id: "E.5.2"
pattern_title: "Notational Independence"
section_id: "E.5.2:5"
section_title: "Archetypal Grounding (System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2/E.5.2__006_archetypal-grounding-system-episteme.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "E.5.2 — Notational Independence"
  - "E.5.2:5 — Archetypal Grounding (System / Episteme)"
line_start: 102724
line_end: 102741
dependencies:
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
  - "C.2.8"
  - "C.37"
  - "E.5"
keywords:
---

### E.5.2:5 - Archetypal Grounding (System / Episteme)

A pattern describes a pump boundary by specifying which components belong to the pump. A table records each component's membership. A diagram places the same components inside or outside a closed line. The line denotes the selected boundary, with no claim about physical distance or drawing scale.

The table's reading convention assigns membership through a field value. The diagram's convention assigns it through enclosure. The table and diagram are the two expressions being compared. Their semantic mapping relates entries to labelled components and membership values to placement relative to the line. Both expressions preserve the membership claims.

The diagram can help the user examine connections across the boundary. That operation depends on the represented connections and their interpretation. The boundary's meaning remains available if the table, or another notation that preserves the membership claims, replaces the diagram.

In the episteme case, F-G-R assurance components can be described in prose and represented in a diagram. Explain which elements denote the assurance components and which relations denote their connections. A triple-store serialization stores this content using tooling conventions. Its storage names do not define the components.

An R-score table can also be rendered as a heatmap. State which score or interval each colour denotes and how the review threshold treats equality. For a cell that represents several scores, apply the review rule to every score still possible. If all would be flagged, flag the cell. If all would pass, the cell passes this threshold check. If some would be flagged and others would pass, consult the values or other available evidence for that decision. For an order requiring the numeric table itself, deliver the table even if the heatmap settles every flag.

A project instruction permits a motor to start only while both the clamp-closed and pressure-present signals are true. A local sketch replaces this with `clamp closes -> pressure arrives -> motor starts`, where each arrow means only that one event precedes the next.

The sketch shows an event order but omits the required overlap: it does not rule out the clamp reopening before pressure arrives.

Compare the source condition with the sketch's timing relations. Show that motor start falls within the overlap of the two true signals, or limit the sketch to showing a proposed event order and use the source instruction to decide whether starting is permitted. This comparison is needed because the sketch is used in place of the instruction.

