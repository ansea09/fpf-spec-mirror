---
chunk_kind: "child"
pattern_id: "C.19.2"
pattern_title: "Use-Bounded Apparatus Application"
section_id: "C.19.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.2/C.19.2__007_archetypal-grounding.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.19.2 — Use-Bounded Apparatus Application"
  - "C.19.2:5 — Archetypal Grounding"
line_start: 61348
line_end: 61367
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.7.1"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.31.ASAP"
  - "C.39"
  - "C.40"
  - "E.23"
keywords:
  - "configuration or adaptation work"
  - "declared result and guarantee"
  - "one selected apparatus"
  - "reuse horizon"
  - "setup cost"
  - "use-bounded apparatus application"
---

### C.19.2:5 - Archetypal Grounding

**Repeated audited handoffs.** A fleet has 400 maintenance handoffs each year. The required result is an audited maintenance-decision episteme with a fixed safety and interoperability guarantee. Candidate generation is complete: an ontology-backed Method and a lighter local decision Method are eligible; their descriptions are available. A spreadsheet macro is excluded because it cannot preserve required relation-occurrence identity.

In this constructed planning account, both eligible Methods satisfy the same guarantee and material non-time conditions. The complete expected setup and per-handoff effort are comparable person-hours, including the required learning, review and integration. Forty setup hours are available. The ontology-backed Method needs 40 hours initially and 6 minutes per handoff; the lighter Method needs 2 hours initially and 14 minutes per handoff.

| Horizon | Ontology-backed Method | Lighter Method |
| --- | --- | --- |
| 400 handoffs | 40 + 400 × 6/60 = 80 hours | 2 + 400 × 14/60 = 95 hours 20 minutes |
| 100 handoffs | 40 + 100 × 6/60 = 50 hours | 2 + 100 × 14/60 = 25 hours 20 minutes |

The setup difference is 38 hours and the per-handoff saving is 8 minutes: the methods tie at 285 handoffs. At the declared 400-handoff horizon, C.11 returns `choose now` for the ontology-backed Method on the supplied equal-guarantee basis, saving an expected 15 hours 20 minutes. If the feasible horizon falls to 100, the same basis favors the lighter Method. These are conditional estimates, not observed maintenance results; changed costs or guarantees reopen their respective questions.

An admitted maintenance-information System performs the dated configuration and application Work using the selected ontology-backed Method. The account recovers the System's A.13 core and independently admits the Work under A.15.1. Because the current question is whether setup cost is repaid across the handoffs and consumes no exact assignment-bound attribution, this short example does not open F.6 or expose assignment identity, species, participants, or attribution detail. A later attribution-bearing claim adds F.6 through the same obtaining A.13 assignment.

A separately admitted maintenance-decision System then performs decision Work using the selected Method. Its A.13 core and independent A.15.1 Work admission are recoverable; this setup-cost example consumes no exact assignment-bound attribution, so F.6 remains unopened. Under `A.6.1`, application `MaintenanceDecisionApplication-1` of operation `DecideMaintenance`, declared by `MaintenanceDecisionMechanism-E1`, returns `AuditedMaintenanceDecision-1` under result declaration `DecisionResult`; no Work-to-result or production claim is made. If repair or audit cost does not fall after the declared sample, reopen the apparatus application.
**One-off naming repair.** A team already has the direct typed-relation method for one local, reversible naming decision. No rival is live and the current method has a credible small path, so no option set or choice result is created. The team performs the minimal wording and typing work and returns a scoped terminology decision. Recurrence, integration, a failed result, or a stronger guarantee may later open candidate generation and choice.

**Non-use.** If the blocked result comes from missing telemetry while the method, state kinds, and action distinctions are already clear, return to measurement and evidence work. Apparatus selection cannot manufacture the missing observation.

