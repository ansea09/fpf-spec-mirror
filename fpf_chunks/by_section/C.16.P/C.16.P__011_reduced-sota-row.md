---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Characteristic and Scale Precision Restoration"
section_id: "C.16.P:8"
section_title: "Reduced SoTA row"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__011_reduced-sota-row.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.16.P — Characteristic and Scale Precision Restoration"
  - "C.16.P:8 — Reduced SoTA row"
line_start: 40862
line_end: 40874
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.20"
  - "A.21"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.25"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.21"
  - "F.18"
  - "G.0"
  - "G.5"
  - "G.9"
keywords:
---

### C.16.P:8 - Reduced SoTA row

Current measurement, quality, proxy-risk, and comparison practice distinguishes characteristics, scales, measures, scores, indicators, thresholds, comparability, proxy status, and decision use. FPF adopts this line only where it changes examples, non-comparability boundaries, indicator/proxy boundaries, scale and scoring method fields, gate/comparison exits, or conformance checks.

| Practice basis | Source posture | What `C.16.P` adopts or adapts | FPF import boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 15939:2017 systems and software measurement process. | Current-standard/reference support for measurement-process discipline. | Disciplines `CharacteristicScaleRepairNote` fields for measure, scale, indicator, measurement use, and information need; supports `CC-C16P-1` and direct exits to `C.16`, `A.17`, and `A.18`. | Does not make "metric" a recovered kind, evidence path, gate, or decision by itself. |
| ISO/IEC 25010:2023 product quality model. | Current-standard/reference support for quality-characteristic families. | Disciplines quality and scalar-quality cases: a quality word needs characteristic/scale or exact quality pattern use before comparison, score, or gate use. | Does not import ISO quality characteristics as the FPF quality ontology; quality/evaluative characterization still exits to `C.16.Q`, `C.25`, or `E.21` when live. |
| ISO/IEC 80000 quantities/units practice and VIM-style metrology vocabulary. | Current reference support for quantities, units, and measurement vocabulary. | Disciplines unit, value, scale, and scoring-method fields; blocks number-without-scale and unitless comparison overreads. | Does not force physical-quantity metrology onto qualitative, ordinal, or pattern-quality characteristic spaces. |
| NIST AI RMF 1.0 metric/risk-management practice, including measurement, monitoring, validity, and risk-tolerance framing. | Current practice/reference support for proxy and indicator risk. | Disciplines `indicatorRole`, `proxyDistortionRisk`, threshold basis, and non-admissible use; supports the indicator/proxy and score-as-gate anti-patterns. | Does not let a risk metric, dashboard, or benchmark become assurance, release permission, or decision authority. |
| Current FPF internal characterization stack: `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, and `E.21`. | Current FPF governing-source support; primary authority for FPF characteristic and scale recovery. | Selects the exact receiving pattern after repair and prevents `C.16.P` from becoming a CHR super-pattern. | Does not copy local trigger lists into receiving patterns or replace exact characteristic-space, quality, mathematical-lens, benchmark, gate, or decision patterns. |

This row blocks scalar verdicts without declared scale and admissible use. It does not import metric lists, maturity-status schemes, or external scoring traditions as FPF ontology.
