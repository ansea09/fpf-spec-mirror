---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__007_bias-annotation.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:6 — Bias-Annotation"
line_start: 61845
line_end: 61858
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
---

### C.30.ASV:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: architecture structural-view claims over holons.

| Bias risk | Mitigation |
| --- | --- |
| Module-view bias | Make module-interface one structure kind, not the default meaning of architecture. |
| Viewpoint-kind conflation | Keep selected structure kind, exact viewpoint episteme P, catalogue L, local family declaration, exact `U.ViewpointRef`, candidate description E, and conformance relation separate. |
| TEVB mutation bias | Reuse only exact references from a materialized project-local TEVB declaration when their resolved P rules fit; do not treat E.17.2's template or a `VF.TEVB.ENG` spelling as a current family value. |
| Check-only bias | Every failed conformance check gives a repair action or use of an applicable pattern. |
| Didactic-thinning risk | The pattern starts with triage and action, not taxonomy alone. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, description, direct conformance relation, or repair guidance above.

