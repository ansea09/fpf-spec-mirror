---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
section_id: "A.17:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__004_forces.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
  - "A.17:3 — Forces"
line_start: 34272
line_end: 34285
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.3"
  - "A.3.3"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2"
  - "D.3"
  - "E.10"
  - "F.7"
  - "F.9"
keywords:
  - "attribute"
  - "axis"
  - "characteristic"
  - "dimension"
  - "measurement"
  - "preference"
  - "property"
  - "quantity calculation"
  - "scale order"
  - "scoring"
---

### A.17:3 - Forces

- **F1 — Recoverable measured aspect.** A reported number needs the answer to “value of what?” before it can be interpreted as a measurement.

-   **F2 – Arity clarity.** Some characteristics apply to a single entity (e.g. its mass or length), while others inherently relate multiple entities (e.g. distance between two points, coupling between modules, agreement between judges). If arity isn’t explicit, claims and calculations become corrupted.

- **F3 — Scale integrity.** Scale types constrain meaningful operations. A numerical encoding of ordinal ranks does not by itself justify their arithmetic mean; interval and ratio values retain their applicable unit and transformation rules. A calculation also needs the relation or ScoringMethod that gives its result meaning.

- **F4 - Combining measurements.** A measurement model relates quantities to obtain another quantity; a ScoringMethod combines values into a score for a declared evaluation. Each calculation needs its applicable relation and Scale operations. A common numerical encoding alone supplies neither.

- **F5 — Disciplinary meanings.** The same distinctions can describe a lab temperature, a software-cohesion rating or a judged performance. Each retains its domain definition, bearer, Scale and conditions of assessment.

- **F6 - Revisable state descriptions.** Development can change the Characteristics and state distinctions that matter. The description should support the changes, returns and further questions needed by the practice, including revision of its state space or transition law.

