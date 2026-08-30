---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Unified Normalization Mechanism (UNM)"
section_id: "A.19.UNM:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__012_rationale.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.19.UNM — Unified Normalization Mechanism (UNM)"
  - "A.19.UNM:10 — Rationale"
line_start: 32876
line_end: 32885
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:10 - Rationale

UNM is designed as a **minimal canonical semantic surface**:
- Enough structure to prevent illegal comparisons and hidden transformations.
- Explicit routing in CN-frame so normalization is governance, not an algorithmic trick.
- Evidence/calibration are delegated to MM‑CHR to avoid redefining measurement meaning.
- Exact bearer, basis, scope/window and intended-use checks prevent accidental global normalization; actual Bridge, kind, and plane relations are cited only when a conclusion relies on them.

This balances evolvability (methods evolve) with didactic usability (one place to read what UNM is).

