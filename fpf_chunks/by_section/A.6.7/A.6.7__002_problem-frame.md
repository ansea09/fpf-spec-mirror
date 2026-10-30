---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
section_id: "A.6.7:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__002_problem-frame.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.6.7 — MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
  - "A.6.7:1 — Problem frame"
line_start: 24031
line_end: 24038
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "G.10"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "CG-Spec"
  - "CN-Spec"
  - "P2W"
  - "crossing visibility"
  - "distinct mechanisms"
  - "mechanism suite"
  - "planned baseline"
  - "spec pins"
  - "suite obligations"
---

### A.6.7:1 - Problem frame

An A.6.1 `U.Mechanism` declares its operations, arguments, results, laws, guards and any transport or audit conditions. Some architectures need several distinct declarations to be used together under shared conditions: for example, a characterization chain or an admissibility-gated selection protocol. The suite description states those joint conditions without redefining the member operations.

FPF already has `MechFamilyDescription`, but its meaning is: **many realizations of one and the same `U.Mechanism`**. That construct cannot correctly represent a bundle of different mechanisms (different declarations), and trying to overload it creates a level error.

Additionally, FPF reserves “Pack” for publication/shipping bundling (e.g., G.10); using “Pack” to mean “container of mechanisms” creates ontological collisions and downstream confusion.

