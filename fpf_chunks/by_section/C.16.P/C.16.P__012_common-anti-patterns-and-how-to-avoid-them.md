---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Restore Precision to Characteristic and Scale Wording"
section_id: "C.16.P:11"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "C.16.P — Restore Precision to Characteristic and Scale Wording"
  - "C.16.P:11 — Common Anti-Patterns and How to Avoid Them"
line_start: 59048
line_end: 59057
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

### C.16.P:11 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Metric-as-evidence | A metric is used to assert evidence, proof, gate passage or decision authority without the conditions that establish that relation. | Recover characteristic and scale construction, then apply `A.10` or evidence named by value, gate, or decision pattern if that claim is being made. |
| Score-as-gate | A score is treated as gate passage, readiness, release, or decision. | Recover scale, threshold rule or reference, comparison reference or comparator set, and exact gate, decision, or release pattern. |
| Axis-as-ontology | Axis or dimension is treated as if it already named a characteristic or factor. | Recover `Characteristic`, coordinate, latent factor, mathematical lens, structural aspect, or ordinary prose. |
| Strong-without-scale | Strong or weak asserts a degree of a characteristic without its scale or comparison reference or comparator set. | State the Characteristic and Scale used by the claim, or replace the unsupported degree with a supported narrower statement. |
| Indicator-as-indicated-characteristic | Indicator wording hides the indicated characteristic or proxy relation. | Name the indicated characteristic or claim, exact direct relation, and proxy-distortion risk when a proxy is used; return `missing-governor` only when no governing rule can state or test that claim. Keep missing facts and failed positive tests distinct under `A.6.RCD:0.1`. |

