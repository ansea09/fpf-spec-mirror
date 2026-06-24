---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:9"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__013_bias-annotation.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:9 — Bias-Annotation"
line_start: 43073
line_end: 43080
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

### C.16:9 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Number-as-fact bias | A displayed value is treated as meaningful without subject, characteristic, scale, unit, polarity, and evidence basis. | Rebuild the value as a `U.Measure` against one `U.DHCMethodRef`. |
| Scale-upgrade bias | Ordinal labels, ranks, or ratings are averaged or ratio-compared as if they were interval or ratio values. | Return to A.18 scale admissibility and declare a scoring method only when the governing pattern admits it. |
| Dashboard authority bias | A dashboard tile, benchmark, or score is reused as assurance, causal support, or admission basis. | Keep the measurement in C.16 and cite `B.3`, `C.28`, `A.21`, or the governing pattern for the wider use. |

