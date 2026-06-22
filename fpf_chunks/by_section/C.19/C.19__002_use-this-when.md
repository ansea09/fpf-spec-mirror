---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__002_use-this-when.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:0 — Use this when"
line_start: 45382
line_end: 45388
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

### C.19:0 - Use this when

- several candidate lines, family regions, or frontier segments remain live under one declared exploration and exploitation policy and the question is now policy over that pool rather than one more local choice result
- the next result should say how the pool will be treated next: `widen`, `keep frontier`, `narrow to subset`, or `sunset line`
- if the question is no longer pool policy, the C.19 use closes by naming the next governing pattern and the reason that pattern now applies
- the governing lens or policy state must be explicit rather than inferred from vague exploration language

