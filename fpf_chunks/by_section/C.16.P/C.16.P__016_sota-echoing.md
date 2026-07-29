---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Characteristic and Scale Precision Restoration"
section_id: "C.16.P:12.2"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__016_sota-echoing.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "C.16.P — Characteristic and Scale Precision Restoration"
  - "C.16.P:12.2 — SoTA-Echoing"
line_start: 47810
line_end: 47823
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

### C.16.P:12.2 - SoTA-Echoing

Current measurement, quality, proxy-risk, and comparison practice distinguishes characteristics, scales, measures, scores, indicators, thresholds, comparability, proxy status, and decision use. FPF adopts this line only where it changes examples, non-comparability boundaries, indicator and proxy boundaries, scale and scoring method fields, gate and comparison exits, or conformance checks.

| Practice source | Source-use relation and currentness | What `C.16.P` adopts or adapts | FPF import boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 15939:2017 systems and software measurement process. | Current-standard reference for measurement-process discipline. | Disciplines `CharacteristicScaleRepairNote` fields for measure, scale, indicator, measurement use, and information need; informs `CC-C16P-1` and direct exits to `C.16`, `A.17`, and `A.18`. | Does not make "metric" a recovered kind, evidence relation, gate, or decision by itself. |
| ISO/IEC 25010:2023 product quality model. | Current-standard reference for quality-characteristic families. | Disciplines quality and scalar-quality cases: a quality word needs characteristic and scale construction or quality-pattern use named by value before comparison, score, or gate use. | Does not import ISO quality characteristics as the FPF quality ontology; quality-term or evaluative characterization still exits to `C.16.Q`, `C.25`, or `E.21` when live. |
| ISO/IEC 80000 quantities and units practice and VIM-style metrology vocabulary. | Current reference for quantities, units, and measurement vocabulary. | Disciplines unit, value, scale, and scoring-method fields; blocks number-without-scale and unitless comparison overreads. | Does not impose physical-quantity metrology on qualitative, ordinal, or pattern-quality characteristic spaces. |
| NIST AI RMF 1.0 metric and risk-management practice, including measurement, monitoring, validity, and risk-tolerance framing. | Current practice reference for proxy and indicator risk. | Disciplines `indicatorRole`, `proxyDistortionRisk`, threshold rule or reference, and non-admissible use; informs the indicator and proxy and score-as-gate anti-patterns. | Does not let a risk metric, dashboard, or benchmark become assurance, release permission, or decision authority. |
| Current FPF internal characterization stack: `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, and `E.21`. | Current FPF governing-source relation; primary authority for FPF characteristic and scale recovery. | Selects the governing pattern after repair and prevents `C.16.P` from becoming a CHR super-pattern. | Does not copy local trigger lists into governing patterns or replace characteristic named by value-space, quality, mathematical-lens, benchmark, gate, or decision patterns. |

This row blocks scalar verdicts without declared scale and admissible use. It does not import metric lists, maturity-status schemes, or external scoring traditions as FPF ontology.

