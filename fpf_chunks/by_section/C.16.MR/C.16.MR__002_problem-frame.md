---
chunk_kind: "child"
pattern_id: "C.16.MR"
pattern_title: "Construct a Measurement Relation"
section_id: "C.16.MR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.MR/C.16.MR__002_problem-frame.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "C.16.MR — Construct a Measurement Relation"
  - "C.16.MR:1 — Problem frame"
line_start: 52653
line_end: 52664
dependencies:
  - "A.3.3"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "B.5.RC"
  - "C.11.DUA"
  - "C.16"
  - "C.29.2"
keywords:
---

### C.16.MR:1 - Problem frame

Use this pattern when you have an indication or a proposed measurement procedure, but the relation between that indication and the property you want to determine is missing or unsuitable. A connected voltmeter can change the voltage. A test response can depend on both capability and the assistance offered. A counter can report the remainder after a wrap rather than the total number of events.

**First useful move.** Follow one indication back through the procedure that produces it. Name the sought property, the conditions under which it is sought, and one interaction or transformation that can make the indication differ from it. Express the relation supplied by that interaction. For an ideal source with open-circuit voltage E and series resistance Rs, a voltmeter of resistance Rm reads V=E*Rm/(Rs+Rm). This already shows why the indication alone need not determine E.

The Method constructs a measurement relation: how sought values, the measuring arrangement and relevant influences produce an indication, or how those contributions jointly constrain the sought value. The relation may use laws, an applicable calibration, an empirical response model or their combination. It can be used to plan a measurement or interpret an obtained indication.

The worked constructions concern quantities and event counts; they require elementary algebra and, in the assessment case, conditional probabilities. Subject Methods supply the physical laws, instrument response, assessment meaning or computational operations. C.16 supplies the Characteristic, Scale and performed-measurement account. This construction can return a conditional relation before any measurement is performed.

When a usable relation already supplies the needed answer under the current procedure and conditions, use it. If the relation is available but several sought values fit the indication, the next work is to determine what that indication can resolve. If an existing measurement disagrees with a prediction, compare possible changes to the models and arrangements.

