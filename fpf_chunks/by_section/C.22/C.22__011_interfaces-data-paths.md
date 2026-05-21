---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:10"
section_title: "Interfaces & Data Paths"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__011_interfaces-data-paths.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:10 — Interfaces & Data Paths"
line_start: 41499
line_end: 41504
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
  - "Problem‑CHR"
  - "ScopeSlice(G)"
  - "TaskKind"
  - "TaskSignature"
  - "specialization anchor"
  - "unknown handling"
---

### C.22:10 - Interfaces & Data Paths

*Inputs.* `ProblemProfile` (…Description), CG-Spec ids, Evidence Graph Ref (A.10), D.CTX; (if QD) CharacteristicSpaceRef/ArchiveConfig/EmitterPolicyRef configs; (if OEE) GeneratorIntent.
 *Produces.* `TaskSignature@Context` (S2) with provenance; **SCR-visible** fields; UTS Name Cards for any minted traits; (if QD/OEE) archive / `PortfolioMode` semantics and telemetry hooks declared.
 *Consumed by.* **G.5** (Eligibility/Selection kernel), **G.4** (Acceptance/Evidence), **C.23** (admit/degrade/abstain rules; maturity ladder).

