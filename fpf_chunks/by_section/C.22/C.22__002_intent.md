---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__002_intent.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:1 — Intent"
line_start: 41332
line_end: 41343
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

### C.22:1 - Intent

Operationalise No‑Free‑Lunch discipline in selection by ensuring every run‑time decision sees a **typed TaskSignature (S2)**, not a paragraph, and that **“problem”** (method unknown) is cleanly separated from **“task”** (method known; signature bound). The signature is the **smallest CHR‑typed set** sufficient to drive **Eligibility → Acceptance → policy‑governed selection** without illegal arithmetic or silent coercions; crossings are auditable (Bridge+CL → **R_eff only**).

#### C.22:1.1 - Term split used in this pattern

- `TaskSignature` attachment means attaching one typed problem record to one declared task family or work target; it does **not** pre-bind a method.
- `ScopeSlice(G)` means the claim-bounding scope cut over `describedEntity/scope`; it is not an evidence-path slice and not a baseline-set slice.
- `threshold` is not one undifferentiated family here:
  - articulation and closure thresholds stay with cue or prompt governing patterns such as `B.4.1` and `B.5.2.0`
  - acceptance-gate thresholds stay with `G.4`
  - the work-measure threshold target used in specialization claims is only the declared success mark for the current task family or work target
