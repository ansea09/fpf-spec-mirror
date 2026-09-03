---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Cross‑Scale Consistency (C‑3)"
section_id: "A.9:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__007_conformance-checklist.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.9 — Cross‑Scale Consistency (C‑3)"
  - "A.9:6 — Conformance Checklist"
line_start: 22585
line_end: 22594
dependencies:
  - "A.1"
  - "A.8"
  - "A.9"
  - "B.1"
keywords:
  - "aggregation"
  - "composition"
  - "holarchy"
  - "invariants"
  - "roll-up"
---

### A.9:6 - Conformance Checklist

| ID          | Requirement                                                                                                                                                                                      | Purpose (manager‑friendly)                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **CC‑A9‑1** | Every calculus that defines an aggregation operator `Γ` **SHALL** provide a plain‑language note and a formal argument for how `Γ` upholds **all five invariants** (IDEM, COMM, LOC, WLNK, MONO). | Makes the Standard both human‑readable and checkable.     |
| **CC‑A9‑2** | A *singleton fold* (` card (parts) = 1 `) **MUST** return the part unaltered (IDEM). | Locks the recursion base case. |
| **CC‑A9‑3** | Folding two independent sub‑graphs in any order or on any compute site **MUST** yield equal results (COMM + LOC).                                                                                | Enables safe parallel work and reproducible analytics.    |
| **CC‑A9‑4** | No aggregate metric **MAY** exceed the minimum of that metric across parts unless an **MHT** is declared (WLNK).                                                                                 | Prevents stealth inflation of reliability or truth.       |
| **CC‑A9‑6** | A declared **Meta‑Holon Transition** **SHALL**: (a) name the new supervisory holon; (b) cite the data triggering the transition; (c) restate how the quintet holds at the new scale.             | Ensures emergence is captured explicitly, not hand‑waved. |

