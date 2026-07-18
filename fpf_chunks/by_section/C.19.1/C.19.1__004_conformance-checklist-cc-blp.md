---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:3"
section_title: "Conformance Checklist (CC‑BLP)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__004_conformance-checklist-cc-blp.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:3 — Conformance Checklist (CC‑BLP)"
line_start: 47380
line_end: 47392
dependencies:
  - "A.0"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "E.23"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "BLP‑waiver"
  - "Scale‑Audit"
  - "alpha and delta tolerances"
  - "general-solution preference"
  - "iso‑scale parity"
  - "scale‑amenability"
  - "slope vector"
---

### C.19.1:3 - Conformance Checklist (CC‑BLP)

1. **Alpha and delta tolerances** declared in DRR or via policy profile, with CI level stated.
2. DRR includes a **Scale‑Audit** (BLP‑1a through BLP‑1g) with slopes, confidence intervals, edition pins, policy pins, and Resrc‑CAL.
3. Selection cites **BLP‑2** and precedence checks.
4. Any heuristic that meets the BLP‑4 trigger is recorded as a `BLP.HeuristicDebtEntry` with scope, responsible role, expiry or review window, and de‑hardening plan; ordinary local bounded tactics do not create a debt entry.
5. Authoring defaults to **rules‑as‑prohibitions**; deviations are DRR‑justified and safety-bounded.
6. **Resrc‑CAL** accounts and assurance deltas reported.
7. **Replicate counts, seed records, and confidence intervals** recorded for slope estimates; heteroscedasticity handling disclosed.
8. Audit artefacts exported to **G.11** with **BLP.Policy@Context** id.

9. When a narrower specialist bearer is selected or returned for one declared task family, the record names the task family, work target, holon structure under comparison when current, and the Scale‑Audit, waiver, or override ground that keeps the choice BLP‑compatible.

