---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__007_worked-cases.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:5 — Worked cases"
line_start: 35338
line_end: 35353
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:5 - Worked cases

#### A.21:5.1 - Ordinary local pass

The workshop case at the entry uses two required checks. Each application names its subject and criterion: `CalibrationCertificate-44` for `TorqueWrench-12` is current under `CalibrationRule-E3`, and `WorkshopEnclosure-2` is closed under `EnclosureRule-E2`. `WorkshopEntryProfile-E5` maps both satisfied results to `pass`. Worst-result aggregation gives `pass`; the short rationale names both results, and the bounded action is “start `CalibrationCycle-17` before 16:00”. No publication or replay record is required.

#### A.21:5.2 - Unknown and failed checks

If the state of `WorkshopEnclosure-2` cannot be established, that application is `unknown`; it does not disappear as `abstain`. The profile maps it to `block`, so the action is “hold the cycle and inspect the enclosure”. If `CalibrationCertificate-44` is expired while the enclosure check passes, the certificate application maps to `block`; the passing enclosure result remains available for repair and need not be rerun unless its own recheck condition is met.

If inspection was not performed after the block was already known, record that check as `notRun`. It remains in the required set and cannot support `pass`.

#### A.21:5.3 - Conditional high-consequence extension

`RegulatedReleaseProfile-E9` adds `RegulatedConformance(Regulator-X, Rule-E9)` and evidence-completeness applications for `ReleaseLot-27`. Unknown regulator conformance maps to `block`. The profile cites Regulator X, Rule E9, the evidence tolerance, the refusal consequence, and the window. If the decision is published or reused, add the E.17 publication and an audit or equivalence record; ordinary gates do not inherit that apparatus.

