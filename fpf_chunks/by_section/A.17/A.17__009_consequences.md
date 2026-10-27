---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
section_id: "A.17:8"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__009_consequences.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
  - "A.17:8 — Consequences"
line_start: 34237
line_end: 34252
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

### A.17:8 - Consequences

The distinctions support the following uses:

- **Recoverable measurement meaning:** a reader can identify the Characteristic to which a reported value belongs.

- **Separate aspect and expression:** the Characteristic names what is measured; the Scale defines its admissible values and structure, with a Unit where applicable.

- **Recoverable participants:** unary and relational Characteristics expose whether a value concerns one bearer or a tuple, such as the distance between two objects.

- **Cross-domain construction:** temperature and a verified-claim proportion can each be described through Characteristic → Scale → Coordinate. Their shared structure supplies no common desirability order. Combining them into a Score requires an explicit ScoringMethod with its preference and applicability conditions under A.19.USCM.

- **Revisable change accounts:** Characteristic meanings and Scales remain explicit as a state model changes. Revising a constraint, input or law can change which states are reachable; adding a Characteristic can supply predictive information that an earlier description omitted.

The cost is identifying disciplinary meanings and revising ambiguous descriptions. A shared term reduces one source of confusion; it does not establish measurement accuracy, evidence quality or a justified scoring model.

