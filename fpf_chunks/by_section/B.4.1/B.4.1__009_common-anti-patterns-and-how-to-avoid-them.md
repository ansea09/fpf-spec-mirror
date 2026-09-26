---
chunk_kind: "child"
pattern_id: "B.4.1"
pattern_title: "Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
section_id: "B.4.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4.1/B.4.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "B.4.1 — Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
  - "B.4.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 43084
line_end: 43089
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.6.A"
  - "A.6.P"
  - "B.4"
  - "B.5.2"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.22.1"
  - "F.9.1"
keywords:
---

### B.4.1:8 - Common Anti-Patterns and How to Avoid Them
- **Anomaly inflation.** Treat every early cue as already an anomaly statement.
- **Cue-pack route smuggling.** Hide route decision or route rationale upstream in `PreArticulationCuePack`.
- **False single-route certainty.** Pretend one route is obvious when multiple candidate routes are still live.
- **Projection capture.** Treat a typed downstream projection publication or its MVPK face as if it already governed the endpoint family.

