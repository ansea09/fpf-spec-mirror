---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore–Exploit Governor (E/E‑LOG)"
section_id: "C.19:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__006_first-output.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.19 — Explore–Exploit Governor (E/E‑LOG)"
  - "C.19:0.4 — First output"
line_start: 41458
line_end: 41465
dependencies:
  - "B.3"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
  - "sunset line"
  - "widen"
---

### C.19:0.4 - First output

The first useful output is one explicit pool-policy result that names the live pool, the governing lens or policy posture, the current treatment (`widen`, `keep frontier`, `narrow to subset`, `sunset line`, or `reroute`), and the exact event that would justify changing that treatment next.

That result records how the pool will be treated next under the current exploration/exploitation posture; it does not replace one local `C.11` choice record, one `C.24` enactment plan, or one `G.5` published selector result.

If that first output still cannot be written honestly, the current pool-policy result is not finished `C.19` policy yet.

