---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__003_problem-frame.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:1 — Problem frame"
line_start: 60694
line_end: 60705
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "E.10.LRN"
  - "E.17"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "audience availability"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "publication face"
  - "publication occurrence"
  - "selector-facing declaration"
  - "sunset line"
  - "widen"
---

### C.19:1 - Problem frame
C.19 describes policies and lenses for treating an identified live pool. Use the applicable C.18 generation, archive or front account when the treatment depends on it; the existence of a record is not an entry condition.

C.11 concerns local choice among a fixed `OptionSet`; C.19 concerns treatment of several still-live candidate lines, family regions or frontier segments. Either question can arise without first completing the other.

Immediate failure indicators for this pattern:
- the current pool-policy result cannot name the still-live candidate pool whose treatment it states
- the governing lens or policy state is missing
- the next pool-side treatment exists only as one vague promise to continue exploration later

If the live question is not treatment of a still-live pool, use the exact exit in `C.19:4.4`. C.19 begins or continues only while the pool-policy question is current.

