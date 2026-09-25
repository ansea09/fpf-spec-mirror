---
chunk_kind: "child"
pattern_id: "A.4"
pattern_title: "Compare a System's Intended Design with Its Operating Conditions"
section_id: "A.4:9"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.4/A.4__010_sota-echoing.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.4 — Compare a System's Intended Design with Its Operating Conditions"
  - "A.4:9 — SoTA-Echoing"
line_start: 11036
line_end: 11049
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.3.4"
  - "B.4"
  - "C.2.1"
  - "C.27"
keywords:
  - "comparison criterion"
  - "conformance"
  - "design account"
  - "discrepancy"
  - "missing basis"
  - "operating facts"
---

### A.4:9 - SoTA-Echoing

**Practice question.** How can an operating observation answer a design question while preserving the selected requirement, comparable conditions and a separate decision about what to change?

The selected line first identifies what the comparison is meant to establish, then applies an explicit decision rule. **Adopt** the distinction in the NASA *Systems Engineering Handbook*, Rev. 2, NASA/SP-2016-6105, [§2.4](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/): compliance with specified requirements and suitability for intended use in the intended environment answer different questions. This supports §4 steps 1–3: a passed flow requirement is not by itself proof of operational suitability. NASA's wider life-cycle process is outside this bounded method; its source role here is the substantive separation of comparison purposes.

For a quantitative requirement near a measurement limit, the competing answers are simple acceptance and guarded acceptance. [JCGM 106:2012, §§8.2–8.3](https://www.bipm.org/en/doi/10.59161/jcgm106-2012), supplies both: simple acceptance compares the measured value directly with the tolerance; guarded acceptance narrows the acceptance region to reduce false acceptance. The former is a serious, inexpensive choice when the parties accept its risk and the measurement uncertainty is adequate for their purpose. The latter can cost more false rejections. Neither changes the specified tolerance itself.

**Adapt** that comparison in §4 steps 2–4: retain the applicable rule and its uncertainty basis instead of silently treating every point estimate as decisive. Where the receiving use requires protection against false acceptance, guarded acceptance is the better answer at comparable effort when the uncertainty estimate is already available. Where that extra protection is unnecessary, reuse a sufficient simple comparison. **Reject** automatically tightening the rule or weakening the requirement merely because the result is inconvenient.

The exact-value pump comparison in §5.1 needs no extra uncertainty calculation. In a separate constructed variant, the available estimate is `105 L/min`, its justified coverage interval is `97–113 L/min`, and the minimum requirement remains `100 L/min`. Simple acceptance accepts the point value. A selected rule requiring the entire interval to satisfy the minimum withholds acceptance because `97 < 100`. Both use the same observation; the second result does not establish that the pump actually delivers less than 100. This is why step 4 distinguishes an evidential limit from an established discrepancy, and step 5 leaves any response to its own authority.

Reopen the chosen rule if the uncertainty or condition-translation basis changes, or the receiving use changes the tolerated decision risk. If the selected account instead contains a descriptive prediction, return to step 2 and recover its prediction-comparison rule; a conformity-assessment source does not authorize recalibrating the prediction or revising a requirement.

