---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Restore Precision to Characteristic and Scale Wording"
section_id: "C.16.P:8"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__010_bias-annotation.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.16.P — Restore Precision to Characteristic and Scale Wording"
  - "C.16.P:8 — Bias-Annotation"
line_start: 58787
line_end: 58794
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.16.Q"
  - "C.25"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.21"
  - "F.18"
keywords:
---

### C.16.P:8 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Scalar verdict bias | `strong`, `weak`, `robust`, or `high` is used as a verdict without characteristic, scale, and comparison reference. | Recover the intended construction and its basis, state a supported narrower gain, or leave the characterization unresolved. |
| Proxy promotion bias | An indicator, metric, score, or benchmark result is treated as the thing indicated. | Name the direct indicator relation, any proxy relation and distortion risk used by the claim, admissible use, and subject pattern for any wider claim. |
| Gate-by-number bias | A threshold or score is treated as release, readiness, proof, or decision authority. | Recover the threshold rule and cite the gate, assurance, decision, or release pattern that actually governs the use. |

