---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__002_problem-frame.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:1 — Problem frame"
line_start: 13520
line_end: 13536
dependencies:
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:1 - Problem frame

FPF repeatedly needs to relate one exact episteme to another, often alongside a separately described operation that produced the receiving episteme:

* turning an informal method description into a more formal specification;
* projecting a large system description into a smaller “for‑safety‑officer” view;
* re‑expressing the same behavioural model in a different calculus or notation;
* relating an analysis about one subsystem to an analysis about another, with a separate claim about invariant, visible loss, bounded use, conditions, support, and polarity.

All of these can be described by **episteme-to-episteme mathematical arrows**. The arrow relates exact epistemes and states its laws; it does not itself change an episteme, measure, execute, or actuate. Any operation application and Work remain separate.

Without one reusable local discipline for such arrows:

* every family (KD‑CAL, E.18, MVPK, discipline packs) reinvent their own notion of “projection”, “reinterpretation”, or “refinement”;
* laws about which parts of the source and receiving epistemes may differ, and which grounding or reference-plane facts their rules read and compare, fragment across the spec;
* cross‑family reasoning (e.g. “this E.18 structural reinterpretation is a retargeting, not a view”) becomes brittle and ad‑hoc.

