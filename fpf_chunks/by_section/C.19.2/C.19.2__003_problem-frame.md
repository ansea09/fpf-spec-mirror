---
chunk_kind: "child"
pattern_id: "C.19.2"
pattern_title: "Use-Bounded Apparatus Application"
section_id: "C.19.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.2/C.19.2__003_problem-frame.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.19.2 — Use-Bounded Apparatus Application"
  - "C.19.2:1 — Problem frame"
line_start: 49393
line_end: 49398
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.7.1"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.31.ASAP"
  - "E.23"
keywords:
  - "configuration or adaptation work"
  - "declared result and guarantee"
  - "one selected apparatus"
  - "reuse horizon"
  - "setup cost"
  - "use-bounded apparatus application"
---

### C.19.2:1 - Problem frame

A team can have a rich apparatus and still lack an economical way to use it. A maintenance group may need only one typed relation distinction for a one-off repair, an architecture team may need a carefully configured model across hundreds of handoffs, and an assurance team may need a formal technique only after the required guarantee becomes stronger. In each case, displaying more apparatus is easier than proving that its setup work changes the result.

The governed concern is one bounded apparatus application for one declared use and horizon. The apparatus retains its direct kind; this pattern does not introduce a generic `U.Apparatus` kind. The application question is distinct from candidate generation, local choice, planning, performed work, and the domain result.

