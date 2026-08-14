---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:14"
section_title: "Slot Interaction Law"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__015_slot-interaction-law.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:14 — Slot Interaction Law"
line_start: 53493
line_end: 53520
dependencies:
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:14 - Slot Interaction Law

The practical payoff of `C.25` is not just that it names the slots. It also stabilizes how those slots interact.

#### C.25:14.1 - Scope and measure remain orthogonal

`ClaimScope` and `WorkScope` answer **where** or **under what contextual slice** the quality claim holds. `Measures[CHR]` answer **how** a measurable aspect behaves. A broader scope is not a larger measurement value; a narrower scope is not a penalty value. Scope is governed by set inclusion and coverage, not by scalar order.

#### C.25:14.2 - Mechanism and status are gating slots

Mechanisms and statuses may be load-bearing for admissibility, but they do not become measurements merely because they matter. A redundancy mechanism may be required for claiming a resilience bundle, and a certification status may be required for external publication, yet neither slot is itself the `Measures[CHR]` head.

This matters because many quality arguments fail by turning mechanism presence into an implicit hidden score.

#### C.25:14.3 - Qualification windows are not decorative

A quality claim that depends on rolling windows, observation periods, maintenance intervals, or disruption horizons must publish that temporal qualifier explicitly. If the truth of the quality claim changes when the window changes, then the window is part of the declared bundle record rather than optional commentary.

#### C.25:14.4 - Report-only summary proxies

A publisher may compute a report-only summary proxy for convenience, for example a compact quality summary proxy value or an oversight-facing composite score. Such a proxy is admissible only if:

- it is explicitly declared as a **report-only proxy**,
- the underlying bundle slots remain visible,
- and no norm, gate, or bridge silently substitutes the proxy for the bundle itself.

This prevents a convenience summary from becoming a covert replacement for the typed quality claim.

