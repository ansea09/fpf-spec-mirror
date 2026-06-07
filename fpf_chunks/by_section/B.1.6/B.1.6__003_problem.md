---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__003_problem.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:2 — Problem"
line_start: 30318
line_end: 30326
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "B.1"
  - "B.1.2"
  - "B.1.4"
  - "B.1.5"
  - "C.5"
keywords:
  - "Resrc-CAL"
  - "cost"
  - "energy consumption"
  - "resource aggregation"
  - "work"
---

### B.1.6:2 - Problem

Without a dedicated algebra for spent resources, models drift into four errors:

1. **Process–Work conflation:** Time‑ordered steps and resource spending are mixed, producing ambiguous or double‑counted totals.
2. **Conservation violations:** Totals appear that exceed inputs or create “free” resource, contradicting physical and informational conservation.
3. **Boundary blindness:** Spending is reported without specifying the boundary across which it is measured, making numbers non‑comparable.
4. **Category errors in mereology:** Collection membership (MemberOf) is misused as if it were parthood for resource stocks, polluting Γ proofs (B.1).

