---
chunk_kind: "child"
pattern_id: "C.11.CRC"
pattern_title: "Configuration-Relative Contribution Comparison"
section_id: "C.11.CRC:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11.CRC/C.11.CRC__002_use-this-when.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "C.11.CRC — Configuration-Relative Contribution Comparison"
  - "C.11.CRC:0 — Use This When"
line_start: 60144
line_end: 60153
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
  - "C.43"
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

Use this pattern when a proposed finite change is being justified by “what it adds,” but its contribution has not been compared with the current configuration under the conditions that matter to the receiving decision. The change may add, replace or remove something; it may also acquire information before a later commitment.

**First useful result.** Tell the decision maker what would change with the proposal over the period they care about, compared with continuing without it. Include who gains or loses, the resources needed and any later choice it opens or closes. State which findings are estimates and what would change the comparison. This account is a `C.2.1` episteme. It supplies a premise for a choice (C.11), for planning later actions (C.43), or for the receiving design Method.

**Cheap exit.** If an existing domain calculation or `A.19`/`C.11` account already states the same finite baseline and change with the material comparison conditions and reopen condition, use it directly.

**Not this pattern when.** Do not use it for a source-only comparison with no realizable configuration change; for a purely causal question under `C.28`; for a mathematical-lens question already answered by `C.29` and a field Method; for an archive/front relation under `C.18`; or as a substitute for field-specific finance, optimization, operations, engineering, experimental-design, or capability-development calculation.

