---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Express a Quality Claim as One Characteristic or a Structured Bundle"
section_id: "C.25:14"
section_title: "Slot Interaction Law"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__015_slot-interaction-law.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.25 — Q-Bundle: Express a Quality Claim as One Characteristic or a Structured Bundle"
  - "C.25:14 — Slot Interaction Law"
line_start: 68108
line_end: 68129
dependencies:
  - "A.15"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.Q"
  - "C.26.3"
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

`C.25` names the slots and defines how they interact.

#### C.25:14.1 - Scope and measure remain orthogonal

`ClaimScope` answers **where** or **under what contextual slice** the quality claim holds; `WorkScope` answers where the capability's deliverability claim may be evaluated. `Measures[CHR]` answer **how** a measurable aspect behaves. A broader scope is not a larger measurement value; a narrower scope is not a penalty value. Scope is governed by set inclusion and coverage, not by scalar order.

#### C.25:14.2 - Mechanism and status are gating slots

Mechanisms and statuses may be load-bearing for admissibility, but they do not become measurements merely because they matter. A redundancy mechanism may be required for claiming a resilience bundle, and a certification status may be required for external publication, yet neither slot is itself the `Measures[CHR]` head.

This matters because many quality arguments fail by turning mechanism presence into an implicit score.

#### C.25:14.3 - Declare windows that affect the claim

A quality claim that depends on rolling windows, observation periods, maintenance intervals, or disruption horizons must publish that temporal qualifier explicitly. If the truth of the quality claim changes when the window changes, then the window is part of the declared bundle record rather than optional commentary.

#### C.25:14.4 - Report-only summary proxies

A publisher may compute a report-only summary proxy, such as a compact quality summary value. Identify the source quality-claim episteme or exact `ClaimAddress`, and state which Q-Bundle slots the proxy summarizes and omits. The proxy is a separate Characteristic or claim under its direct pattern; it does not replace that source in a norm, gate, comparison, endpoint classification or cross-context use.

