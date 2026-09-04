---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:6"
section_title: "Bias annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__008_bias-annotation.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:6 — Bias annotation"
line_start: 35372
line_end: 35378
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:6 - Bias annotation

- **Green-display bias.** A display can look like a decision. Recover the gate result and applicable profile.
- **Neutral-value bias.** An algebraic neutral can hide an unknown or unrun check. Preserve applicability and evaluation state before mapping.
- **Profile-label bias.** A profile name can look authoritative. Require its applicable rule and any separate authority relation.
- **Infrastructure bias.** Publication and replay fields can look like the gate itself. Keep the decision result primary and add infrastructure only for its triggered use.

