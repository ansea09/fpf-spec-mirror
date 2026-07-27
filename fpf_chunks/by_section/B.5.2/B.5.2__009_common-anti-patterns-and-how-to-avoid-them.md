---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 39896
line_end: 39904
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
keywords:
  - "abduction"
  - "candidate hypotheses"
  - "explanatory prompt"
  - "origin trace"
  - "plausibility filters"
  - "route-to-hypothesis"
---

### B.5.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Authority candidate** | One favored conjecture is advanced immediately, with no rival set and no explicit filtering. | `CC-B.5.2-2` and `CC-B.5.2-3` require candidate plurality and visible plausibility grounds. |
| **Untestable grand conjecture** | The candidate sounds deep or comprehensive, but it creates no admissible next step for checking, probing, or deduction. | `CC-B.5.2-6` rejects prime hypotheses that cannot open a downstream checking, probing, deduction, or evidence-acquisition relation. |
| **Prompt amnesia** | A later reader can see the conjecture but not the initiating anomaly, opportunity, or probe pressure. | `CC-B.5.2-1` and `CC-B.5.2-5` keep prompt provenance attached. |
| **Symptom patching** | The selected candidate only redescribes a visible symptom and leaves the actual prompt unresolved. | The explicit plausibility filter for explanatory reach forces the candidate to be compared against the whole prompt. |

