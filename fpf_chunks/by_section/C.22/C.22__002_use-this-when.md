---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__002_use-this-when.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:0 — Use This When"
line_start: 46235
line_end: 46242
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

### C.22:0 - Use This When

Use this pattern when a stabilized problem-side representation must become a selector-facing typed attachment record for eligibility, acceptance, or policy-governed selection. Typical cases include solver choice, method-family eligibility, QD archive selection, open-ended generator selection, or specialization claims that need a declared task family or work target.

**What goes wrong if missed.** A problem remains a paragraph: selector inputs drift, ordinals and units get mixed, unknowns are coerced, acceptance thresholds leak into CHR fields, and cross-context reuse happens by name instead of Bridge+CL.

**What this buys.** The downstream selection question gets one minimal `TaskSignature` with typed fields, unknown handling, evidence relations, scope, freshness, and crossing conditions visible before any method family is admitted or compared.

