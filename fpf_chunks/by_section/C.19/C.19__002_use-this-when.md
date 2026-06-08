---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore–Exploit Governor (E/E‑LOG)"
section_id: "C.19:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__002_use-this-when.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "C.19 — Explore–Exploit Governor (E/E‑LOG)"
  - "C.19:0 — Use this when"
line_start: 43185
line_end: 43190
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

### C.19:0 - Use this when

- several candidate lines, family regions, or frontier segments remain live under one declared exploration/exploitation policy and the question is now policy over that pool rather than one more local choice result
- the next result should say how the pool will be treated next: `widen`, `keep frontier`, `narrow to subset`, `sunset line`, or `reroute`
- the governing lens or policy state must be explicit rather than inferred from vague exploration language

