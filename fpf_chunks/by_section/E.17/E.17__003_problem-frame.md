---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__003_problem-frame.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:2 — Problem frame"
line_start: 80196
line_end: 80204
dependencies:
  - "A.15.4"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.View"
keywords:
---

### E.17:2 - Problem frame

* Teams routinely need several **faces** of the *same* arrow: a **`TechCard`** for the catalog, an **`InteropCard`** for machine exchange, a **`PlainView`** for narrative, and an **`AssuranceLane`** for evidence.
* Informal “renderings” quietly **drift semantics**; **composite arrows** are often published piecemeal, breaking traceability; **evidence** forgets unit, scale, and edition pins.
* “View” and “viewpoint” are **blurred** in practice; authors conflate **publication** with **mechanism**.
* publication-face-kind discipline requires **`publication-face kind` token discipline**; Core allows only literal values **publication face/form** or **interop publication form**; faces are named **...View**, **...Card**, or **...Lane** with no ad-hoc face-kind names outside the literal set.

**MVPK** fixes this by selecting one exact episteme edition, one exact publication viewpoint, one publication form, one bounded use, and any required pins. A.6.3 viewing is an optional construction route when another episteme is actually constructed from the source; E.24.PUB governs publication availability. In the morphism profile, the construction and publication rules preserve the declared functorial discipline for Description epistemes, including Description epistemes admitted for specification use. **Part E is conceptual:** no machine-exchange formats are specified here.

