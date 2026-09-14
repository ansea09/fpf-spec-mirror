---
chunk_kind: "child"
pattern_id: "C.16.IR"
pattern_title: "Determine What an Indication Can Resolve"
section_id: "C.16.IR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.IR/C.16.IR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0caf9a10acfc0ee17c32fc71f6173b542393f0a4"
heading_path:
  - "C.16.IR — Determine What an Indication Can Resolve"
  - "C.16.IR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 53042
line_end: 53052
dependencies:
  - "A.3.3.PI"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.16.MR"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### C.16.IR:8 - Common Anti-Patterns and How to Avoid Them

| Failure in the worked situation | Consequence | Repair |
| --- | --- | --- |
| Use the displayed number as the sought value | Loading or clipping changes the answer. | Interpret the reading through the available relation and target conditions. |
| Select one root and discard the rest | A sign or other consequential branch disappears. | Test the admitted domain and retain every branch relevant to the conclusion. |
| Demand every parameter's unique value | Work continues after the requested quantity is determined. | Test agreement on the sought value, as in the zero-voltage case. |
| Treat a wide computational enclosure as realized ambiguity | Approximation slack is mistaken for attainable alternatives. | Construct feasible witnesses or report the unresolved computation. |
| Combine readings without their shared-subject condition | An apparent extra equation relates different unknowns. | Recover the time, initialization and subject correspondence before intersection. |
| Convert repeated readings into a narrower bound by counting them | A common bias or unrestricted bounded error survives repetition. | Supply the error relation that justifies the proposed reduction. |

