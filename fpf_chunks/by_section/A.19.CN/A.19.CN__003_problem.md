---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN‑frame (comparability & normalization)"
section_id: "A.19.CN:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__003_problem.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.19.CN — CN‑frame (comparability & normalization)"
  - "A.19.CN:2 — Problem"
line_start: 29737
line_end: 29745
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CL/loss notes"
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "bridges"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "normalization refs"
  - "registry"
  - "Γ-fold governance"
---

### A.19.CN:2 - Problem

Absent a governance layer, four failure modes recur:

1. **Chartless numbers.** Measures move between teams without units, reference states, or declared normalization → **illusory comparability**.
2. **Hidden normalization flips.** Re‑parameterisations (e.g., normalising by batch size) silently alter meaning; trend lines lie.
3. **CN‑frame sprawl.** Every initiative mints a new “dashboard dimension”; semantics diverge; assurance collapses.
4. **Un‑bridgeable reports.** Cross‑team roll‑ups average **incongruent** CN‑frames, violating the **weakest‑link (WLNK)** discipline from Γ and B.3.

