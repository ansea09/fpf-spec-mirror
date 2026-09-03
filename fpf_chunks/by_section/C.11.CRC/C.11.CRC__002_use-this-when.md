---
chunk_kind: "child"
pattern_id: "C.11.CRC"
pattern_title: "Configuration-Relative Contribution Comparison"
section_id: "C.11.CRC:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11.CRC/C.11.CRC__002_use-this-when.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.11.CRC — Configuration-Relative Contribution Comparison"
  - "C.11.CRC:0 — Use This When"
line_start: 47620
line_end: 47629
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

### C.11.CRC:0 - Use This When

Use this pattern when a bounded addition, replacement, removal, intervention, experiment, information/computation acquisition, capability-development element, project, or component is being justified by “what it adds,” but the current configuration, interactions, resources, horizon, uncertainty, and receiving decision are not yet part of the comparison.

**First useful result.** Return one ordinary `C.2.1` episteme that compares a realizable finite changed configuration with the current configuration under a declared basis. State the result coordinates and resource coordinates, interactions, uncertainty, option effects, unsupported overreads, and the `C.11` decision that can consume the claim. The comparison does not choose the option.

**Cheap exit.** If a current `A.19`/`C.11` account already states the same finite baseline, change, horizon, result and resource coordinates, interactions, uncertainty, and reopen condition, use that account directly.

**Not this pattern when.** Do not use it for a source-only comparison with no realizable configuration change; for a purely causal question under `C.28`; for a mathematical-lens question already answered by `C.29` and a field Method; for an archive/front relation under `C.18`; or as a substitute for field-specific finance, optimization, operations, engineering, experimental-design, or capability-development calculation.

