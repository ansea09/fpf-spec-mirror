---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "SCR/RSCR Harness for Unification"
section_id: "F.15:17"
section_title: "Acceptance summary (“Harness green”)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__018_acceptance-summary-harness-green.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "F.15 — SCR/RSCR Harness for Unification"
  - "F.15:17 — Acceptance summary (“Harness green”)"
line_start: 77341
line_end: 77349
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.1-F.14"
  - "F.14"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:17 - Acceptance summary (“Harness green”)

A unification slice is **publish‑ready** when:

1. **All SCR (S‑Local & S‑Cross) hold** for the current snapshot (Contexts, Local‑Senses, SenseCells, rows, Role Descriptions, Bridges, windows).
2. **All RSCR (R‑Evo) hold** against the previous snapshot: no silent replacements; rows either unchanged or retired+reborn; Bridges re‑validated with CL non‑inflated without witnesses; windows adjusted only for real variance; SoD intact.
3. **One micro‑witness per moving part** exists in the text (tiny example showing the check in action).
4. **Memory rule still holds**: the active Context set for the line fits in a careful mind without external aids (F.1).

