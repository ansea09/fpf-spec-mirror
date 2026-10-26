---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Restore Precision to Characteristic and Scale Wording"
section_id: "C.16.P:7"
section_title: "Archetypal Grounding - Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__009_archetypal-grounding-worked-cases.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.16.P — Restore Precision to Characteristic and Scale Wording"
  - "C.16.P:7 — Archetypal Grounding - Worked cases"
line_start: 58697
line_end: 58711
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

### C.16.P:7 - Archetypal Grounding - Worked cases

| Wording | Repair |
| --- | --- |
| "This pattern is stronger." | Recover which claim is meant, including any characteristic and scale it uses. If the sentence means pattern-quality evaluation, use `E.21`; if it means relation strength, use `A.6.P`; if the claimed degree has no basis, state the supported narrower gain or leave that degree unresolved. |
| "Architecture score improved." | Recover whether this is a score on a declared scale, pattern-quality coordinate, grounded architecture adequacy value, selected-structure characteristic value, Q-bundle value, benchmark result, gate threshold, or ordinary comparison. Repair the wording only while the intended comparison remains unclear; use the recovered score construction directly. |
| "The metric supports launch." | Recover measure, characteristic, scale, scoring method, threshold predicate or reference, and gate or decision pattern. A measurement may support a named launch criterion; establish that evidence use and any further launch conditions under their governing rules. |
| "The model has robust quality." | Recover robustness perturbation and scale, quality-term or evaluative characterization under `C.16.Q`, Q-bundle under `C.25`, or mathematical-lens use under `C.29`. |
| "Latent axis explains behavior." | Recover whether `axis` is a latent coordinate, factor, mathematical lens, characteristic, or ordinary source-local word. Use `C.29` when a mathematical-lens use is being claimed. |
| "The benchmark proves the method is better." | Recover benchmark harness, characteristic space, comparison set, scale, statistical or evidential claim, and decision use. Use evidence named by value, decision, and work patterns as needed. |

**Worked comparison.** A report calls a new implementation “stronger.” Its supplied observations concern response time in four matched workload cases under the same conditions. Response time is elapsed duration on a ratio Scale, expressed in milliseconds. The earlier times are 80, 100, 120 and 140 ms; the new times are 70, 90, 110 and 130 ms. Both comparisons use the median, defined here as the mean of the two middle ordered values. The respective medians are 110 and 100 ms.

The supported rewrite is: “For these four matched workload cases, median response time fell by 10 ms, from 110 to 100 ms.” It names the Characteristic, Unit, comparison set and scoring operation and can finish the wording repair. It supplies no comparison for other workloads. If a receiving criterion requires median response time at most 105 ms on these cases, the new value satisfies that numerical condition. Any other release conditions remain separate. If the new trials used different workload cases, the original comparison would need an account of their comparability before supporting the same claim.

