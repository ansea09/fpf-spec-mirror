---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__001_intro.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:intro — Intro"
line_start: 43103
line_end: 43116
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
  - "B.2"
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
---

## B.1.6 - Work-Resource Aggregation

> **Type:** B-family aggregation pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Use this when.** Use this pattern when the current claim aggregates measured or estimated resource use, such as effort, time, energy, material, information or cost, across identified accounting subjects. These may include dated Work occurrences, A.15.1 temporal or operational Work parts, event-bounded episodes, non-Work carrier phases with an established identity and `PhaseOf` relation, or boundary partitions with the relations needed for their resource account.

**Not this pattern when.** If the current question is the Method as a way of doing, use `A.3.1`. If it concerns whether an episteme is a MethodDescription, or the use of its claims about a Method as a way of doing, use `A.3.2`. If it is a work plan, use `A.15.2`. If it is whether Work occurred or which Work temporal part, episode, operational part, retry, resumption, or later occurrence is current, use `A.15.1`. If it is work-entry readiness, full-kit condition, or resource readiness before work entry, use `A.15.5`. If it is bounded aggregation of already recovered temporal relations without resource accounting, use `B.1.4`. If it is a transformation claim, use `A.3.4`. If resource gain leaves whole identity in question, use `B.2`; use `B.2.P` only when emergence-family wording is unresolved.

**What goes wrong if missed.** A convenient resource total is taken from a method description, plan, dashboard or phase label without warranted input values, identified accounting subjects and a combination rule that handles any overlap.

**What this buys.** The practitioner can justify a typed total, vector, interval or bounded estimate from its input values, included subjects, accounting scope, time basis and operative rules, and check whether the same resource contribution has been counted more than once.

