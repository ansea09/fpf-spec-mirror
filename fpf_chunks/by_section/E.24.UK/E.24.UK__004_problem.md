---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__004_problem.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:2 — Problem"
line_start: 86268
line_end: 86278
dependencies:
  - "A.11"
  - "A.3.2"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.17.0"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "U.MethodDescription"
  - "U.View"
  - "U.Viewpoint"
keywords:
---

### E.24.UK:2 - Problem

Without this pattern:

1. **`U.*` spelling substitutes for admission.** A public name is retained because it looks like a kind.
2. **Unsettled type and kind wording competes with U-kind admission rules.** Type, kind, subkind, Concept-Set rows, U-kind names, and E.24 ontics become overlapping ontologies.
3. **A dependent distinction becomes an independent root.** A kind whose individuals retain root identity or depend on one root-kind individual is treated as if it had an independent root settlement.
4. **Structural names over-admit.** Titles, filenames, headings, and ToC rows advertise kindhood more strongly than the pattern body establishes.
5. **Declaration and representation elements become U-kinds.** A participant meaning in a direct relation, a SlotKind in its reusable declaration, an assertion field, or a `C.29` representation element receives a `U.*` spelling even though its governing object is already known.
6. **Naming patterns are asked to do ontology.** F.5, F.8, F.18, or F.17 is used before the governed object has been recovered.

