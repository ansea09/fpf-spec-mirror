---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping (Evidence • Standard • Requirement)"
section_id: "F.10:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__003_problem-frame.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "F.10 — Status Families Mapping (Evidence • Standard • Requirement)"
  - "F.10:2 — Problem frame"
line_start: 63957
line_end: 63966
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:2 - Problem frame

Without a modality‑aware mapping of statuses:

* **Homonym traps.** *Validated* in metrology ≠ *validated* in software QA; *approved* in a standard ≠ *compliant* to a requirement.
* **DesignRunTag bleed.** Design‑time “approved method” is used as if it proved run‑time “meets SLO”.
* **False substitution.** *Observed availability 99.95%* is silently treated as *SLO satisfied* without declaring the translation.
* **Name inflation.** New U.Types minted to stabilise drifting status words instead of fixing Contexts and Bridges.


