---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__001_intro.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:intro — Intro"
line_start: 46367
line_end: 46377
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

## C.16 - Measurement & Metrics Characterization (MM‑CHR)

> **Status:** Stable
> **Type:** Pattern

**Use this pattern when.** Use C.16 when a value, score, rating, metric label, QL probe output, dashboard reading, or comparison is being treated as meaningful without a visible characteristic, scale, unit, polarity, comparability basis, or evidence pointer.

**What goes wrong if missed.** Convenient numbers become free-floating facts: dashboards imply unsupported comparison, scores hide scale changes, ordinal labels are averaged as interval quantities, and measurement outputs are reused as causal, assurance, or admission claims without the pattern that governs those uses.

**What this buys.** A measurement reading that a reader can interpret, compare, and reuse only within its declared measurement basis: subject, characteristic, scale, coordinate or level, unit, polarity, evidence stub, and any governing comparability or scoring basis.

