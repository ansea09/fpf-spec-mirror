---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Express a Quality Claim as One Characteristic or a Structured Bundle"
section_id: "C.25:15"
section_title: "Worked Quality Families"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__016_worked-quality-families.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "C.25 — Q-Bundle: Express a Quality Claim as One Characteristic or a Structured Bundle"
  - "C.25:15 — Worked Quality Families"
line_start: 65197
line_end: 65237
dependencies:
  - "A.10"
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

### C.25:15 - Worked Quality Families

#### C.25:15.1 - Availability family

A narrow service commitment may use `AvailabilityRatio[%]` as one characteristic. A broader availability family usually still needs a bundle because the claim depends on:

- declared service and time scope,
- observation and qualification window,
- one or more mechanism slots such as failover or redundancy,
- and evidence tying the measurement to declared observation conditions.

The bundle form makes it possible to distinguish "the measurement fell short" from "the measurement is fine but the declared mechanism prerequisite was absent".

#### C.25:15.2 - Resilience family

Resilience is almost never one scalar. It commonly binds together:

- disruption scenario scope,
- observed restoration measures, such as mean time to restore under a declared observation protocol, and the recovered data point,
- recovery mechanisms and preparedness states,
- and scenario-specific evidence about drills, restorations, or incident traces.

Keep the observations distinct from their objectives: [RTO](https://csrc.nist.gov/glossary/term/Recovery_Time_Objective) bounds permissible recovery duration, while [RPO](https://csrc.nist.gov/glossary/term/recovery_point_objective) specifies the required data-recovery point. Neither is an observed recovery result. Compare the observations with the applicable objectives under the declared rule.

Trying to compress this into a single resilience value can hide the difference between fast recovery in one scenario and structural fragility in another.

#### C.25:15.3 - Security family

Security claims routinely combine:

- trust-zone or attack-class scope,
- measurable characteristics such as patch latency, control coverage, or response interval,
- control-set and certification slots,
- and evidence from audit, observation, or incident review.

`C.25` therefore treats broad security-family claims as bundle-shaped unless the claim has already been narrowed to one admissible CHR characteristic.

#### C.25:15.4 - Maintainability and evolvability

For maintainability or evolvability, recover the particular claim and the contributors on which it depends. These may include the system or change-class scope; measures such as change lead time, defect reintroduction rate, restoration interval or review load; enabling mechanisms such as modularity rules or a test harness; and the observation window or other support actually used. Keep measures distinct from mechanism and scope claims. A narrow claim carried by one Characteristic can stop there; a broader claim retains every load-bearing contributor, not every example in this list.

