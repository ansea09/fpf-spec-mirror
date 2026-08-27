---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__001_intro.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:intro — Intro"
line_start: 36732
line_end: 36745
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.29"
  - "E.17"
  - "G.11"
  - "G.6"
keywords:
  - "C.16 measurement work/result episteme"
  - "Scale/Unit"
  - "aggregation work"
  - "allocation/deduplication"
  - "dated work set"
  - "edition-pinned aggregation policy"
  - "provenance"
  - "resource Characteristic"
  - "typed aggregation result"
  - "typed input"
  - "uncertainty"
  - "work parthood/phase/overlap"
  - "work-resource aggregation"
---

## B.1.6 - Work-Resource Aggregation

> **Type:** B-family aggregation pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Use this when.** Use this pattern when the current claim aggregates resources, effort, time, energy, material, information, cost, or another measured resource over exact dated Work occurrences, A.15.1 temporal or operational Work parts, event-bounded episodes, non-Work carrier phases with an established identity and `PhaseOf` relation, boundary partitions, or comparable work-resource ledgers.

**Not this pattern when.** If the current question is the method as a way of doing, use `A.3.1`. If it is a method description, SOP, algorithm text, simulator configuration, or formal expression, use `A.3.2`. If it is a work plan, use `A.15.2`. If it is whether Work occurred or which Work temporal part, episode, operational part, retry, resumption, or later occurrence is current, use `A.15.1`. If it is work-entry readiness, full-kit condition, or resource readiness before work entry, use `A.15.5`. If it is bounded aggregation of already recovered temporal relations without resource accounting, use `B.1.4`. If it is a transformation claim, use `A.3.4`. If apparent resource gain changes whole identity, use `B.2.P` before any B.2-family pattern.

**What goes wrong if missed.** Resource, effort, time, energy, or cost totals are read from methods, plans, dashboards, or phase labels without a dated work occurrence, resource ledger, and overlap policy.

**What this buys.** A replayable chain that keeps the resource Characteristic, measurement work/result episteme, aggregation work/result, exact policy, work parthood/overlap, and provenance separately recoverable while preventing double counting.

