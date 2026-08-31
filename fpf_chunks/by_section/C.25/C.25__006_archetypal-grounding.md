---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__006_archetypal-grounding.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:5 — Archetypal Grounding"
line_start: 53520
line_end: 53527
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

### C.25:5 - Archetypal Grounding

**Tell.** A quality family is not automatically one metric. Use one Characteristic when one measure and Scale carry the claim; use a Q-Bundle only when several differently typed contributors are jointly load-bearing.

**Minimal completed availability case.** Under `ServiceQualityScheme-v4`, the claim says: *CheckoutAPI maintained at least 99.9% availability for customer-facing request handling over the rolling 30-day window.* Its exact bearer is the independently identified `CheckoutAPI` System. Its Q-Bundle content has `Name: Availability`, `ClaimScope: customer-facing request handling`, `Measures: AvailabilityRatio[%] >= 99.9`, and `QualificationWindow: rolling 30 days`. `WorkScope`, `Mechanisms`, `Status`, and `Evidence` are omitted because this drafting use does not rely on them. If evidence reliance, a failover prerequisite, or a gate later becomes current, add only the direct relation or slot that question needs.

**Escalation examples.** A resilience or security claim often needs several measures, scenario or attack-class scope, mechanisms or control statuses, and a qualification window. Those contributors belong in the bundle only when they are part of that claim's truth conditions; treating the family as one scalar score would erase which contributor failed.

