---
chunk_kind: "child"
pattern_id: "B.5.MPC"
pattern_title: "Connect Physical, Mathematical and Computational Reasoning"
section_id: "B.5.MPC:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MPC/B.5.MPC__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "B.5.MPC — Connect Physical, Mathematical and Computational Reasoning"
  - "B.5.MPC:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 41706
line_end: 41718
dependencies:
  - "A.15.9"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.3"
  - "B.3.3"
  - "B.5"
  - "B.5.4"
  - "C.11.DUA"
  - "C.16"
  - "C.29"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
  - "C.39"
  - "C.40"
  - "U.Dynamics"
keywords:
---

### B.5.MPC:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Failure visible in the worked cases | Repair |
| --- | --- | --- |
| Substitute the right number into the wrong command | A count of relative motor increments is treated as an absolute wheel-position target. | Recover the interface's counted participant, unit and initial-state use; construct the input it actually accepts. |
| Check only the middle calculation | The robot arithmetic is correct while rolling or successful completion remains unsupported for an actual-travel claim. | Add the physical and observation contributions consumed by that stronger claim, or return the conditional design. |
| Treat a sufficient abstraction as complete physical design | A gear colouring is taken to establish torque or mechanical compatibility. | State the bounded direction consequence and obtain the missing mechanical account when the decision requires it. |
| Repair the drawing while leaving the arrangement unchanged | An odd-cycle edge is deleted from the contact graph but the gears remain meshed. | Change the actual contact or revise the contact rule with its physical basis, then reconstruct the graph consequence. |
| Count reservations as occupants | Three cards outside the free pool are reported as three visitors inside during handover. | Retain Reserved and Awaiting-return states, or report the resulting occupancy bound. |
| Preserve local rules while duplicating a shared resource | Each entrance has its own three-card stock and both are used for one room. | Use one total stock or a partition of it; transfer existing free cards when balancing entrances. |
| Traverse every contribution before using a sufficient result | A proof already excludes a design, yet simulation and implementation continue as compulsory stages. | Return the proved physical obstruction under its assumptions and choose a revised design question. |
| Ask a contributor for an unexplained answer | The receiver gets a count, proof or program whose needed meaning cannot be recovered. | Request the particular interpretation, decisive argument or operating condition required by the next use. |

