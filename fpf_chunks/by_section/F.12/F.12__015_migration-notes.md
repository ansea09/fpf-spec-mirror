---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:14"
section_title: "Migration notes"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__015_migration-notes.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:14 — Migration notes"
line_start: 94166
line_end: 94174
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.RCD"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.2"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.9"
  - "U.PromiseContent"
keywords:
  - "EvidenceStatus"
  - "PromiseContent"
  - "RequirementStatus"
  - "declared result scale"
  - "delivery Work"
  - "evaluation Work"
  - "indicator recovery"
  - "measured value"
  - "observation"
  - "operation result binding"
---

### F.12:14 - Migration notes

1. **Promise revision.** Keep the old promise-content identity, evaluation results, and status assertions; evaluate the new claim separately.
2. **Monitor change.** State whether the new observation model directly measures the promised characteristic or needs a separately defined indicator relation; preserve past evidence identity.
3. **Scope correction.** Retire a result or status assertion about the wrong Work or population and issue a corrected evaluation rather than redefining the promise.
4. **Scale and unit change.** Apply the direct conversion and measurement relations; use F.9 only when local meanings also differ.
5. **Population refinement.** Treat per-region, per-zone, or per-episode changes as explicit promise or evaluation changes.
6. **Indicator retirement.** Prefer direct measurement when available; keep prior indicator-dependent results, status assertions, and evidence uses with their original limits.

