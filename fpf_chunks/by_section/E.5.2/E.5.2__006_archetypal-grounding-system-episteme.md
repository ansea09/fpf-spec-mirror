---
chunk_kind: "child"
pattern_id: "E.5.2"
pattern_title: "Notational Independence"
section_id: "E.5.2:5"
section_title: "Archetypal Grounding (System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2/E.5.2__006_archetypal-grounding-system-episteme.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "E.5.2 — Notational Independence"
  - "E.5.2:5 — Archetypal Grounding (System / Episteme)"
line_start: 75841
line_end: 75852
dependencies:
  - "A.6.3.RT"
  - "C.2.8"
  - "C.37"
  - "E.5"
keywords:
  - "BPMN"
  - "UML"
  - "diagram"
  - "notation"
  - "semantics"
  - "syntax"
  - "tool-agnostic"
---

### E.5.2:5 - Archetypal Grounding (System / Episteme)

A pattern describes a pump boundary by specifying which components belong to the pump. A table records each component's membership; a diagram places the same components inside or outside a closed line. The line denotes the selected boundary, with no claim about physical distance or drawing scale.

The table's reading convention assigns membership through a field value; the diagram's convention assigns it through enclosure. The table and diagram are the two expressions being compared. Their semantic mapping relates entries to labelled components and membership values to placement relative to the line. Both expressions preserve the membership claims. The diagram can help the user examine connections across the boundary; that operation depends on the represented connections and their interpretation. The boundary's meaning remains available if the table or another notation replaces the diagram.

For an episteme example, F-G-R assurance components can be described in prose and represented in a diagram. Explain which element and relation denotes each component and connection. A triple-store serialization stores this content using tooling conventions; its storage names do not define the components.

An R-score table can also be rendered as a heatmap. State which score or interval each colour denotes. If several scores share a colour, retain the values or limit the equivalence claim to the displayed intervals.

A project instruction permits a motor to start only while both the clamp-closed and pressure-present signals are true. A local sketch replaces this with `clamp closes -> pressure arrives -> motor starts`, where each arrow means only that one event precedes the next. The sketch shows an event order but omits the required overlap: it does not rule out the clamp reopening before pressure arrives. Compare the source condition with the sketch's timing relations. Show that motor start falls within the overlap of the two true signals, or limit the sketch to showing a proposed event order and use the source instruction to decide whether starting is permitted. This comparison is needed because the sketch is used in place of the instruction.

