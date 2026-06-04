---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__003_problem-frame.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:2 — Problem frame"
line_start: 72177
line_end: 72188
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:2 - Problem frame

Cross-context work fails in predictable ways:

1. **String-equals fallacy.** Identical spellings (“process”, “role”, “accuracy”) taken as identical meaning.
2. **Scope creep.** A naming convenience is stretched to assignment or structural claims.
3. **DesignRunTag jumping.** Design artefacts are substituted for run-time occurrences (or vice-versa).
4. **Direction amnesia.** Narrower/broader relations treated as symmetric.
5. **Loss blindness.** Differences (units, granularity, preconditions) are left unstated, contaminating downstream reasoning.

Bridges cure these by **making relation, direction, loss, and `CL` explicit**.

