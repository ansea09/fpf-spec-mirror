---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__001_intro.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:intro — Intro"
line_start: 31275
line_end: 31288
dependencies:
  - "A.1.1"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.6"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

## B.1.4 - Contextual and Temporal Aggregation

> **Type:** B-family aggregation pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Use this when.** Use this pattern when the current claim aggregates relations across a bounded context, ordered situation, phase set, or time window, and the question is not just ordinary part-whole construction. Typical cues are ordered steps, order-sensitive argument chains, version histories, asset histories, phases of one carrier, rolling windows, context-scoped roll-ups, or time-sliced evidence.

**Not this pattern when.** If the question is ordinary part-whole or collection admission, use `B.1`, `A.14`, and `C.13`. If the question is the method as such, method description, work plan, or dated work occurrence, use `A.3.1`, `A.3.2`, `A.15.2`, or `A.15.1`. If the question is work-resource accounting, use `B.1.6`. If the question is changed identity, use `A.3.4`; if a new whole must be reidentified, use `B.2` through `B.2.P`. If the question is temporal adequacy of a claim, use `C.27`.

**What goes wrong if missed.** Order, phase, context, or time-window wording becomes ordinary parthood, method order, performed work, evidence currentness, or whole reidentification by label.

**What this buys.** The practitioner can aggregate context-sensitive and temporal material while returning method, work, transformation, work-resource, temporal-adequacy, and MHT claims to their direct owners.

