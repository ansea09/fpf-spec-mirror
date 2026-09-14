---
chunk_kind: "child"
pattern_id: "A.3.3.CC"
pattern_title: "Construct a Configuration Description under Constraints"
section_id: "A.3.3.CC:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.CC/A.3.3.CC__002_problem-frame.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "A.3.3.CC — Construct a Configuration Description under Constraints"
  - "A.3.3.CC:1 — Problem frame"
line_start: 9614
line_end: 9623
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5.FM"
  - "B.5.MPC"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.CC:1 - Problem frame

Use this pattern when you need to describe how participants can be arranged, but choosing values for them separately admits combinations that the modeled situation excludes. A linkage joins its endpoints at a fixed distance; buffers share a fixed stock; a body must fit inside a container. The next calculation needs a description that preserves those connections.

**First useful move.** Name the participants, the question and one condition joining their values. For two buffers containing three jobs altogether, begin with “q1 and q2 are nonnegative integer job counts, and q1 + q2 = 3.” You can now recover the second count from the first and reject a proposed pair whose sum differs from three. Add buffer capacities when the question concerns which distributions fit.

The Method constructs an interpretable description of configurations: the retained arrangement or combination of participant values, expressed through variables and constraints. It can return an equation, a parametrization, a finite set or another usable representation. The arrangement being modeled and its description remain distinct. The examples assume elementary algebra and, for the linkage, the ordinary meaning of sine and cosine; the Solution explains the representation choices.

The practical gain is a basis for finding, comparing or rejecting configurations and for constructing a later model of change. If an available description already supplies the combinations and distinctions the question needs, use it directly. A prediction additionally needs the state information and law addressed by A.3.3.

