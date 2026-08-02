---
chunk_kind: "child"
pattern_id: "C.30.STRAT"
pattern_title: "Stratification Wording Precision Restoration"
section_id: "C.30.STRAT:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.STRAT/C.30.STRAT__002_use-this-when.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "C.30.STRAT — Stratification Wording Precision Restoration"
  - "C.30.STRAT:0 — Use this when"
line_start: 60926
line_end: 60942
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.5"
  - "G.6"
  - "I.2"
keywords:
---

### C.30.STRAT:0 - Use this when

Use this pattern when stratification or architecture-operation wording is doing FPF-governed work but the selected `ontologicalNeighborhood` and governing pattern for the source-label use are not yet recoverable by value.

Typical source labels:

- `layer`, `level`, `tier`, `stack`, `ladder`, `rung`;
- `block`, `expert`, `cache`, `router`, `gate` when architecture-operation prose uses them as recognition labels before the FPF kind is known.

**What goes wrong if missed.** A source label starts acting as ontology. `Layer` may be taken as a holon level, control layer, publication layer, scale window, or module boundary without saying which ontological neighborhood is being used. `Stack` may become architecture by label. `Block` may become a module. `Expert` may become a role. `Cache` may become a memory relation or state. `Router` may become a decision policy. `Gate` may become a gate decision. None of those interpretations is admissible by word shape alone.

**What this buys.** The practitioner can keep useful source language while recovering the selected `ontologicalNeighborhood` and applying the governing pattern, instead of replacing the source label with another umbrella word.

**First useful move.** Treat the word as a `sourceLabel` and complete the recovery row: source label, bounded text, selected `ontologicalNeighborhood`, primary `EntityOfConcern` kind, relation to that `EntityOfConcern`, recovered kind, relation, or claim-use, governing pattern, admissible use, non-admissible use, and remaining reader use.

**Not this pattern when.** If the governing pattern is already recoverable by value, use it directly. Do not use `C.30.STRAT` merely because a familiar word appears. If the wording is only ordinary source prose with no FPF-governed use, keep ordinary prose or quote-only wording and stop.

