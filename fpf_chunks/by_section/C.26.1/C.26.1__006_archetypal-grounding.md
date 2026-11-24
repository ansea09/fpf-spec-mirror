---
chunk_kind: "child"
pattern_id: "C.26.1"
pattern_title: "Probe-Coupled Boundary Interaction"
section_id: "C.26.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.1/C.26.1__006_archetypal-grounding.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "C.26.1 — Probe-Coupled Boundary Interaction"
  - "C.26.1:5 — Archetypal Grounding"
line_start: 69639
line_end: 69646
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.6"
  - "A.6.B"
  - "A.6.P"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.26"
  - "C.26.2"
  - "C.26.3"
  - "F.9"
keywords:
  - "API read"
  - "bridge result"
  - "dashboard as instrument"
  - "evidence window"
  - "export loss"
  - "passive read"
  - "probe-coupled boundary"
  - "survey"
  - "workshop as state-changing interaction"
---

### C.26.1:5 - Archetypal Grounding

A team runs a service-boundary workshop after a series of incidents. The first map says “Payments is separate from Checkout.” During the meeting, participants agree that failure to update a customer's payment status will enter checkout incident triage. The signed decision records the new triage rule. The next week's incident log cites it when two such incidents are redirected.

The meeting record establishes the new agreement. The later log shows two applications. To decide whether earlier incidents of the same kind already went to checkout triage, examine earlier routing records for failures to update payment status. Payments can be a separate service while Checkout handles those incidents. Establish the service boundary from the relevant interfaces and responsibilities if the decision requires it. The records leave open whether a different question order would have changed the agreement.

Use the recorded rule for the handoff it governs. If another team will apply it, compare which incidents each team calls a failure to update payment status and whether a difference changes routing. Use `F.9` for a cross-context correspondence when needed.

