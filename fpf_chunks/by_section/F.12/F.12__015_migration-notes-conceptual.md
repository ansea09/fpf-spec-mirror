---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:14"
section_title: "Migration notes (conceptual)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__015_migration-notes-conceptual.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:14 — Migration notes (conceptual)"
line_start: 65790
line_end: 65799
dependencies:
  - "A.2.3"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
  - "U.PromiseContent"
keywords:
  - "Service Level Agreement (SLA)"
  - "Service Level Objective (SLO)"
  - "acceptance criteria"
  - "binding"
  - "observation"
---

### F.12:14 - Migration notes (conceptual)

1. **Clause revisions.** Introduce a **new ClauseCell**; keep old verdicts intact (Non‑retroactivity).
2. **Monitor changes.** Update or replace **Bridges** (kind/CL/Loss). Future verdicts use the new Bridge; past ones are annotated, not rewritten.
3. **Scope corrections.** If evidence was about the wrong **Work**, retire the verdict and restate the quadruple; do **not** patch by redefining the Clause.
4. **Unit harmonisation.** When scales/units change, apply **KD‑CAL** conversions inside the Measure’s Context; if Cross‑context mapping is needed, declare a **Bridge**.
5. **Population refinement.** If a Clause’s quantifier is refined (e.g., per‑region → per‑AZ), treat each as a new ClauseCell or a new Window partition; avoid hidden re‑baselining.
6. **Proxy retirement.** When direct Observations become available, prefer them; keep earlier proxy‑based verdicts with their CL/Loss notes.


