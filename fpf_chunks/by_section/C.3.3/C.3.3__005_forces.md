---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:4"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__005_forces.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:4 — Forces"
line_start: 36896
line_end: 36905
dependencies:
  - "A.2.6"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
keywords:
  - "CL^k"
  - "KindBridge"
  - "R penalty"
  - "cross-context mapping"
  - "type-congruence"
---

### C.3.3:4 - Forces

| Force                                    | Tension to resolve                                                                              |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Minimal disclosure vs precision**      | Bridges must be light to write yet precise enough to avoid semantic drift.                      |
| **Local autonomy vs global reuse**       | Each target‑context keeps its vocabulary; reuse requires explicit, reviewable mappings.                   |
| **Typed safety vs agility**              | We need typed compatibility checks without blocking exploratory reuse.                          |
| **Separate channels vs operator workload** | Two channels (Scope & Kind) must be explicit, but guard writers shouldn’t drown in boilerplate. |


