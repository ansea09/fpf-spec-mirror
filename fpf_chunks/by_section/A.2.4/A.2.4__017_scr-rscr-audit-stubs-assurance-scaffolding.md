---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "U.EvidenceRole"
section_id: "A.2.4:16"
section_title: "SCR/RSCR audit stubs (assurance scaffolding)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__017_scr-rscr-audit-stubs-assurance-scaffolding.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.2.4 — U.EvidenceRole"
  - "A.2.4:16 — SCR/RSCR audit stubs (assurance scaffolding)"
line_start: 3339
line_end: 3358
dependencies:
  - "A.10"
  - "A.2"
  - "B.3"
keywords:
  - "claim"
  - "episteme"
  - "evidence"
  - "justification"
  - "support"
---

### A.2.4:16 - SCR/RSCR audit stubs (assurance scaffolding)

These stubs allow concept-level validation of evidence-role assignments, without implying any specific tooling.

**SCR-A2.4-E1 (Assignment integrity)**
Assert: `holder` is `U.Episteme`; `context` present; `claimRef` resolves; `timespan` non-empty; provenance anchored to EPV.

**SCR-A2.4-E2 (Weight discipline)**
Assert: if `weight.score` present → `weight.modelRef` present and all required inputs provided; recompute to check.

**SCR-A2.4-E3 (Traceability)**
For empirical evidence-role assignments: assignment → `fromWorkSet` → each `U.Work` has performer `U.RoleAssignment` and timestamps; no missing hops.

**RSCR-A2.4-R1 (Regression on version bump)**
When `claimRef` or holder episteme versions change, ensure **new** bindings are created; no in-place mutation.

**RSCR-A2.4-R2 (Decay check)**
Bindings past `timespan.to` or with expired `decayClass` are flagged for review per context policy.


