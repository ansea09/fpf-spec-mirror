---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:6"
section_title: "Archetypal Grounding - Running example"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__008_archetypal-grounding-running-example.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:6 — Archetypal Grounding - Running example"
line_start: 39150
line_end: 39167
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

### B.3.5:6 - Archetypal Grounding - Running example

> **Story.** A refinery team publishes `:PumpA ut:ComponentOf :Skid12`.

* **Publication — Working-Model relation layer.**
  They mint one edge with the **Working-Model** relation **ComponentOf** and declare the published edge's `U.Formality` (typically **F≈F3**, controlled narrative). Only the Working-Model relation is visible to readers.

* **Constructive grounding (Γₘ).**
  In the background, the published assertion links to `:trace_Γₘ_sum_456`, a C.2.1 episteme that names the exact pump and skid, the direct fastening, coupling, enclosure, terminal, flange, and seal occurrences that obtain, the applicable skid assembly rule, and the skid reidentification rule. An auditor replays that account to inspect the assertion's basis. The same listed parts under a different assembly can form another whole, while a permitted pump replacement can preserve Skid12; the direct relations and reidentification rule, not the trace or input list, decide.

* **Assurance stance & R-lane.**
 Because the assertion is linked to an inspectable construction account, authors set `tv:validationMode=axiomatic`. This records their assurance posture; it does not strengthen the direct relation, fix identity, or make either timeless. B.3.3 reads the flag together with the actual grounding, warrants, evidence, and their currentness to assess the appropriate **R** lane. **F**, **G**, and **R** remain orthogonal.

* **Contrast (epistemic).**
When the same team asserts `:MassFlowRepresentation RepresentationOf :FlowModel`, they declare `validationMode=postulate` and attach a calibration dataset (Empirical Validation) instead of a **Γₘ** trace. The edge remains publishable, but reviewers record a lower-confidence stance, and B.3.4’s **evidence ageing** policy will decay its trust over time.

Result: **one** visible relation for engineers, **two** assurance references for reviewers.

