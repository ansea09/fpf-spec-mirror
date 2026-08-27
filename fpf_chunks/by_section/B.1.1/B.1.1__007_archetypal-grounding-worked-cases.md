---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Structure and Relation Grounding"
section_id: "B.1.1:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__007_archetypal-grounding-worked-cases.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "B.1.1 — Dependency Structure and Relation Grounding"
  - "B.1.1:5 — Archetypal Grounding (Worked Cases)"
line_start: 35750
line_end: 35769
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.22"
  - "A.6.5"
  - "B.1"
  - "B.1.4"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
keywords:
---

### B.1.1:5 - Archetypal Grounding (Worked Cases)

#### B.1.1:5.1 - Plant Supplier

Source graph: `PowerGrid -> Plant`.

If the edge means electricity supply, recover a boundary-crossing or supply relation. The power grid is not a plant part. Use part-whole relations only for admitted plant internals.

#### B.1.1:5.2 - Digital Twin

Source graph: `DigitalTwin -> Turbine`.

If the edge means representation, recover the architecture-description, publication, source-use, evidence, or digital-twin relation. The digital twin is not a turbine component by graph adjacency.

#### B.1.1:5.3 - Work Plan And Work Occurrence

Source graph: `Prep -> Weld -> Paint`.

If the graph describes a method or process view, use the patterns that define the method, description, and order claims. If it describes performed Work, use A.15.1 with occurrence identity, timing, evidence, and the exact Work relation. Do not let the same graph do both jobs.

