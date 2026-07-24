---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__006_first-output.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:0.4 — First output"
line_start: 49185
line_end: 49193
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "G.11"
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
For loop-engineering practice, use this first output only when the live question is pool policy over still-live loop, harness, workflow, method-family, or framework-seed candidates. `C.19` may decide to widen, keep, narrow, or sunset the pool under a declared lens. It does not improve one object version, publish the selected set, or authorize work; those exits go to `E.23`, `G.5`, or the `A.15` family.

The first useful output is one explicit pool-policy result that names the live pool, the governing lens or policy state, the current treatment (`widen`, `keep frontier`, `narrow to subset`, or `sunset line`), and the exact event that would justify changing that treatment next. If the current question has become local choice, enactment planning, selected-set publication, or refresh, the first output names `C.11`, `C.24`, `G.5`, or `G.11` as the next governing pattern instead of filling `currentTreatment`.

That result records how the pool will be treated next under the current exploration and exploitation policy; it does not replace one local `C.11` choice record, one `C.24` enactment plan, or one `G.5` published selector result.

If that first output still cannot be written honestly, the current pool-policy result is not finished `C.19` policy yet.

