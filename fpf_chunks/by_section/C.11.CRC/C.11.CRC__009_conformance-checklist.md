---
chunk_kind: "child"
pattern_id: "C.11.CRC"
pattern_title: "Configuration-Relative Contribution Comparison"
section_id: "C.11.CRC:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11.CRC/C.11.CRC__009_conformance-checklist.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.11.CRC — Configuration-Relative Contribution Comparison"
  - "C.11.CRC:7 — Conformance Checklist"
line_start: 47727
line_end: 47740
dependencies:
  - "A.1.CSD"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
keywords:
  - "candidate configuration S1"
  - "constraints"
  - "current configuration S0"
  - "finite change"
  - "interactions"
  - "marginal contribution"
  - "option effects"
  - "result and resource vectors"
  - "transition"
  - "uncertainty"
---

### C.11.CRC:7 - Conformance Checklist

1. Is one receiving decision named?
2. Are `S0`, finite `Δ`, and realizable `S1` explicit?
3. Are system boundary, affected Systems, horizon, scenarios, and evidence window compatible—and, when a missing bearer could change the comparison, was `A.1.CSD` used before freezing this coordinate?
4. Are result and resource coordinates explicit, with protected coordinates not silently scalarized?
5. Are implementation capability, planned transition work, reversibility, and excluded variants recoverable?
6. Are constraints, interactions, overlap, thresholds, congestion, and downstream effects considered where material?
7. Are future option effects distinguished from realized results?
8. Are evidence, uncertainty, sensitivity/robustness, transfer limits, and unsupported overreads visible?
9. Is each derivative, sensitivity, shadow-price, functional-variation, variational-inference, or evolutionary-variation result used only for its exact question?
10. Does the output remain a comparison claim, with `C.11` retaining the `ChoiceResult`?
11. Is the smallest reopen condition stated?

