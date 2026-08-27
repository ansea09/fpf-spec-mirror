---
chunk_kind: "child"
pattern_id: "C.11.CRC"
pattern_title: "Configuration-Relative Contribution Comparison"
section_id: "C.11.CRC:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11.CRC/C.11.CRC__004_problem.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.11.CRC — Configuration-Relative Contribution Comparison"
  - "C.11.CRC:2 — Problem"
line_start: 46728
line_end: 46740
dependencies:
  - "A.1.CSD"
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

### C.11.CRC:2 - Problem

Without an explicit configuration-relative comparison, practitioners make at least six transfers:

- a finite change is approximated by a derivative outside its valid region;
- a shadow price for one active constraint is multiplied into the value of an asset that changes several constraints;
- a candidate is compared with an empty system instead of the actual current configuration;
- several result and resource coordinates are hidden inside one scalar;
- interaction and common-cause overlap are counted as independent contribution; and
- information, option value, or reversibility is treated as realized benefit.

`A.19` provides comparison mechanisms and characteristic spaces, `C.29` governs mathematical lenses, and `C.11` makes the choice. The remaining recurring practitioner action is to construct the finite comparison claim that those patterns can consume.

