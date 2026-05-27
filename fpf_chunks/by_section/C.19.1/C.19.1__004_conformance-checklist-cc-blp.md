---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:3"
section_title: "Conformance Checklist (CC‑BLP)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__004_conformance-checklist-cc-blp.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:3 — Conformance Checklist (CC‑BLP)"
line_start: 42513
line_end: 42525
dependencies:
  - "A.0"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "BLP-waiver"
  - "BLP‑waiver"
  - "Bitter Lesson"
  - "Scale‑Audit"
  - "general‑method preference"
  - "iso‑scale parity"
  - "scale-audit"
  - "scale‑amenability"
  - "slope vector"
  - "task-family specialization"
  - "α/δ tolerances"
---

### C.19.1:3 - Conformance Checklist (CC‑BLP)

1. **α/δ tolerances** declared in DRR or via policy profile (and CI level stated).
2. DRR includes a **Scale‑Audit** (BLP‑1a–g) with slopes, **CI**, edition/policy pins, and Resrc‑CAL.
3. Selection cites **BLP‑2** and precedence checks.
4. Any heuristic that meets the BLP‑4 trigger is recorded as a `BLP.HeuristicDebtEntry` with scope, responsible role, expiry or review window, and de‑hardening plan; ordinary local bounded tactics do not create a debt entry.
5. Authoring defaults to **rules‑as‑prohibitions**; deviations are DRR‑justified and safety‑anchored.
6. **Resrc‑CAL** accounts and assurance deltas reported.
7. **Replicate counts/seeds** and **confidence intervals** recorded for slope estimates; heteroscedasticity handling disclosed.
8. Audit artefacts exported to **G.11** with **BLP.Policy@Context** id.

9. When a narrower specialist method is selected or returned for one declared task family, the record names the task family/work target and the Scale‑Audit, waiver, or override ground that keeps the choice BLP‑compatible.

