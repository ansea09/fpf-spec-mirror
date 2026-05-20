---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__003_problem-frame.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:2 — Problem frame"
line_start: 55777
line_end: 55785
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "E.10"
  - "E.10.D2"
  - "E.10.SEMIO"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicViewing"
  - "U.MultiViewDescribing"
keywords:
---

### E.17:2 - Problem frame

* Teams routinely need several **faces** of the *same* arrow: a **`TechCard`** for the catalog, an **`InteropCard`** for machine exchange, a **`PlainView`** for narrative, and an **`AssuranceLane`** for evidence.
* Informal “renderings” quietly **drift semantics**; **composite arrows** are often published piecemeal, breaking traceability; **evidence** forgets unit, scale, and edition pins.
* “View” and “viewpoint” are **blurred** in practice; authors conflate **publication** with **mechanism**.
* L‑SURF requires **`SurfaceKind` token discipline**; Core allows only **PublicationSurface** or **InteropSurface**; faces are named **...View**, **...Card**, or **...Lane** (no ad‑hoc `...Surface` kinds).

**MVPK** fixes this by making publication a typed projection from existing source epistemes or episteme-lane views via species of `U.EpistemicViewing` subject to explicit viewpoint specs and pinning guards. In the morphism profile, this projection is the functorial D and S episteme publication discipline described below. **Part E is conceptual:** no machine-exchange formats are specified here.

