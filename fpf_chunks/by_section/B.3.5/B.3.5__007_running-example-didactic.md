---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:6"
section_title: "Running example (didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__007_running-example-didactic.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:6 — Running example (didactic)"
line_start: 31251
line_end: 31268
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

### B.3.5:6 - Running example (didactic)

> **Story.** A refinery team publishes `:PumpA ut:ComponentOf :Skid12`.

* **Publication — Working-Model surface.**
  They mint one edge with the **Working-Model** relation **ComponentOf** and **declare the surface’s `U.Formality`** (typically **F≈F3**, controlled narrative). Only the publication surface is visible to readers.

* **Constructive grounding (Γₘ).**
  In the background, the edge node records `tv:groundedBy :trace_Γₘ_sum_456`. That trace is a **Compose-CAL** “sum” that lists the parts aggregated into the skid. Any auditor can **replay** the trace to prove extensional identity. *(Grounding does not change the surface’s F; it sets `validationMode=axiomatic` and contributes to **R** in the **VA** lane.)*

* **Assurance stance & R-lane.**
 Because the edge is construction-backed, authors set `tv:validationMode=axiomatic`. B.3.3 reads the flag and assigns an **AssuranceLevel** in the appropriate **R** lane (scale defined in B.3.3). **F**, **G**, and **R** remain **orthogonal**: this move raises assurance without changing claim scope (**G**) or the surface’s formality (**F**).

* **Contrast (epistemic).**
When the same team asserts `:MassFlowRepresentation RepresentationOf :FlowModel`, they declare `validationMode=postulate` and attach a calibration dataset (Empirical Validation) instead of a **Γₘ** trace. The edge remains publishable, but reviewers record a lower-confidence stance, and B.3.4’s **evidence ageing** policy will decay its trust over time.

Result: **one** visible relation for engineers, **two** hidden anchors for assurance.

