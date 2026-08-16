---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__002_problem-frame.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:1 — Problem Frame"
line_start: 3500
line_end: 3518
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
  - "E.24.UK"
keywords:
  - "ability envelope"
  - "capability-fit condition"
  - "currentness"
  - "holder-dependent capability instance"
  - "measure set"
  - "qualification window"
---

### A.2.2:1 - Problem Frame

In ordinary work, the same sentence often carries several typed values:

- "The welding robot is the welder on this line."
- "The welding robot can weld seam type W at 12 seams per minute."
- "The welding procedure says how to weld seam type W."
- "The robot welded batch B at 10:20."
- "The supplier promises 12 seams per minute."

Only the second sentence can support a `U.Capability` instance when the holder, Work family, envelope, measures, and currentness conditions are recoverable. The sentence itself is a statement about the capability instance. The others may state a local system-role assignment, MethodDescription, performed Work, or promise content. When FPF collapses them, project reasoning becomes brittle:

1. **System-role assignment becomes fake ability.** “Assigned as verifier” is treated as “able to verify”.
2. **Method description becomes fake ability.** A recipe or algorithm is treated as if it can execute itself.
3. **Past work becomes fake ability.** One successful work occurrence is treated as stable capacity.
4. **Promise content becomes fake ability.** A service promise hides the real system envelope and measured bounds.
5. **Description becomes fake holder.** A standard, report, model card, or dashboard is said to "have capability" because it is useful in a capability argument.
6. **Unbounded ability becomes unreviewable.** "Can machine titanium" does not name conditions, measures, version, calibration, or currentness.

