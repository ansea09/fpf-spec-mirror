---
chunk_kind: "child"
pattern_id: "C.11.CRC"
pattern_title: "Configuration-Relative Contribution Comparison"
section_id: "C.11.CRC:8"
section_title: "Common Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11.CRC/C.11.CRC__010_common-anti-patterns-and-repairs.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "C.11.CRC — Configuration-Relative Contribution Comparison"
  - "C.11.CRC:8 — Common Anti-Patterns and Repairs"
line_start: 46286
line_end: 46297
dependencies:
  - "A.10"
  - "A.15"
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

### C.11.CRC:8 - Common Anti-Patterns and Repairs

| Anti-pattern | Repair |
| --- | --- |
| Candidate value is constant across configurations | Name `S0`, interactions, horizon, and affected Systems. |
| Average benefit chooses the next element | Preserve result/resource vectors and return the comparison to `C.11`. |
| Derivative times step equals finite contribution | State smoothness region and remainder or perform the finite comparison. |
| Shadow price equals asset value | Keep the local active-constraint result and model the finite intervention separately. |
| Functional stationarity proves physical optimality | Use `C.29`, physical/domain evidence, sufficiency checks, and validation. |
| Variational inference is calculus of variations or “learning” | Recover the target distribution, approximation family, objective, returned approximation, and diagnostics. |
| More information is already more capability or value | Treat information as a decision input and test the target result separately. |

