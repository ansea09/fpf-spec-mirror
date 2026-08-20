---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__011_rationale.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:10 — Rationale"
line_start: 80228
line_end: 80231
dependencies:
  - "A.16.0"
  - "A.22"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.13"
  - "C.2.1"
  - "C.2.2a"
  - "C.29"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "E.7"
  - "F.9"
  - "F.9.1"
keywords:
---

### E.17.1:10 - Rationale

`MultiViewDescribing` already assumes that viewpoint plurality exists. `E.17.1` supplies packaging and provenance discipline for that plurality, including cases where viewpoints are used to re-express positions in `U.LanguageStateSpace` or trajectories in `U.LanguageStateMoveTrajectory`. Without it, every domain can only improvise locally and member provenance becomes fragile. Semantic correspondence is a separate result: same-scheme comparison states its exact predicate and participants, while cross-context comparison uses F.9 and a bounded-use reliance path.

