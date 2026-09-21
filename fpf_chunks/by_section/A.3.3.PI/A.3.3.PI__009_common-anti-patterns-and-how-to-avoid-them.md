---
chunk_kind: "child"
pattern_id: "A.3.3.PI"
pattern_title: "Retain the Information Needed for Prediction"
section_id: "A.3.3.PI:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.PI/A.3.3.PI__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "31f4cb0b7f8000e0115098b50b44f80c8c36a671"
heading_path:
  - "A.3.3.PI — Retain the Information Needed for Prediction"
  - "A.3.3.PI:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 10270
line_end: 10280
dependencies:
  - "A.3.3"
  - "A.3.3.CC"
  - "A.3.3.TR"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.29.1"
keywords:
---

### A.3.3.PI:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Why it matters | Repair |
| --- | --- | --- |
| Use an aggregate as a predictive state without comparing its merged cases | Components or hidden modes can produce different continuations. | Compare those cases and retain their relevant distinction or output range. |
| Substitute a long-run average for a history-conditioned forecast | A decision about the next event can depend on recent observations. | Condition on the available history or retain its predictive distribution. |
| Turn a recovered value into a measurement without carrying its assumptions | Algebraic reconstruction can amplify errors and depends on the supplied law. | Propagate the reading uncertainty and inspect the admitted domain. |
| Repeat a one-step predictor beyond its supported use | Prediction error can accumulate, or the retained output may lack its own update. | Construct an adequate state update or a predictor for the required horizon. |
| Keep a longer history without the intervening inputs | Similar observations can follow different actions and call for different forecasts. | Retain the actions that enter the transition account. |
| Obtain a full hidden-state estimate after a bound has settled the question | The extra work adds cost without changing the present choice. | Use the bound and reopen the distinction when another question needs it. |

