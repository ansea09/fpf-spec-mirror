---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Restore Precision to Characteristic and Scale Wording"
section_id: "C.16.P:7"
section_title: "Archetypal Grounding - Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__009_archetypal-grounding-worked-cases.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "C.16.P — Restore Precision to Characteristic and Scale Wording"
  - "C.16.P:7 — Archetypal Grounding - Worked cases"
line_start: 62450
line_end: 62464
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
| "Latent axis explains behavior." | Recover whether `axis` is a latent coordinate, factor, mathematical lens, characteristic, or ordinary source-local word. Use `C.29` when choosing, transferring or relying on the mathematical representation leaves an unresolved question. |
| "The benchmark proves the method is better." | Recover benchmark harness, characteristic space, comparison set, scale, statistical or evidential claim, and decision use. Use the patterns governing the evidence, decision and work claims as needed. |

**Worked comparison.** A report calls a new implementation “stronger.” The receiving question is how typical response time changed across four specified, matched workloads. The agreed summary is the median, here the mean of the two middle ordered times. Response time is elapsed duration on a ratio Scale. The earlier times are 80, 100, 120 and 140 ms. The corresponding new times are 70, 90, 110 and 130 ms. For these four cases, median response time fell from 110 to 100 ms.

If the requirement is a median of at most 105 ms on these cases, the new result meets it. If **each** case must finish within 105 ms, the 110 and 130 ms cases violate it, even though every paired case was 10 ms faster. The same records settle both questions. They provide no comparison for other workloads without grounds for transfer. A change in the tested workload mix would also require grounds for comparing the two editions.

