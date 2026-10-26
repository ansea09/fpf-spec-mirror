---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
section_id: "A.6.7:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__003_problem.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.6.7 — MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
  - "A.6.7:2 — Problem"
line_start: 23909
line_end: 23922
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

### A.6.7:2 - Problem

The suite user needs one description that can:

1. represent a **set of distinct mechanisms** (distinct `U.Mechanism`),
2. declare **shared obligations** that must hold across the set (e.g., crossing visibility, admissibility-citation discipline, guard decision format, penalty routing),
3. provide **shared spec pins** (e.g., “this suite is governed by CN-Spec and CG-Spec”), without duplicating those spec contents,
4. constrain **allowed protocols** of use (allowed pipelines / permitted ordering), without turning the suite into a mechanism, and
5. preserve strict distinction among:

   * a description of several distinct mechanism contracts (`MechSuiteDescription`),
   * a description of realizations of one contract (`MechFamilyDescription`),
   * a publication bundle (`Pack`, e.g., G.10).

