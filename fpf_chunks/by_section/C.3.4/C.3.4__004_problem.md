---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__004_problem.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:3 — Problem"
line_start: 38251
line_end: 38257
dependencies:
  - "C.3.1"
  - "C.3.2"
keywords:
  - "RoleMask"
  - "constraints"
  - "context-local adaptation"
  - "subkind promotion"
---

### C.3.4:3 - Problem

1. **Kind sprawl.** Teams mint near‑duplicate kinds (“Account\_PCI”, “Account\_Ledger”), and alignment decays.
2. **Hidden constraints.** Informal “we only accept …” statements leak into prose; guards can’t check them deterministically.
3. **Scope conflation.** Contextual requirements (jurisdiction, API version) get smuggled into “type” talk, blurring Scope vs Kind.
4. **Cross‑context fragility.** Masks don’t travel unless their constraints are mapped; teams reuse names and hope.

