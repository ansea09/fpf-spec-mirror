---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:10"
section_title: "Selector Fields And Evidence Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__012_selector-fields-and-evidence-relations.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:10 — Selector Fields And Evidence Relations"
line_start: 47568
line_end: 47573
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "C.32.P2S"
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

### C.22:10 - Selector Fields And Evidence Relations

*Inputs.* `ProblemProfile` (...Description), CG-Spec ids, Evidence Graph Ref (A.10), D.CTX; CharacteristicSpaceRef, ArchiveConfig, and EmitterPolicyRef configs when QD is live; GeneratorIntent when OEE is live.
*Produces.* `TaskSignature` under a declared `Context` field (S2) with provenance; **SCR-visible** fields; UTS Name Cards for any minted traits; archive, `PortfolioMode` semantics, and telemetry hooks declared when QD is current. Do not introduce `TaskSignature@Context` as a separate kind.
*Used by.* **G.5** (Eligibility and Selection kernel), **G.4** (Acceptance and Evidence), **C.23** (admit, degrade, and abstain rules and method-family maturity checks).

