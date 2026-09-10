---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Description of a set of distinct mechanisms"
section_id: "A.6.7:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__013_relations.md"
commit_sha: "ce6fcc3b99b10e42f4b258f84091355b2ee5ab24"
heading_path:
  - "A.6.7 — MechSuiteDescription — Description of a set of distinct mechanisms"
  - "A.6.7:12 — Relations"
line_start: 20498
line_end: 20505
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
  - "U.Mechanism.Intension"
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

### A.6.7:12 - Relations

* **Relates to A.6.1:** suite members are `U.Mechanism.Intension`; the suite does not replace the mechanism definition.
* **Relates to A.6.5:** suites must not weaken slot/ref discipline; any suite protocol assumes member mechanisms follow A.6.5 invariants (SlotKind stability, correct refMode, no semantic meaning in SlotIndex).
* **Relates to E.18 / P2W:** suite protocols describe intended composition; use E.18 for the selected transformation-flow structure and its crossings, and E.18.1 for P2W carry-through.
* **Relates to E.19:** E.19 governs admission or refresh review of this pattern edition. Suite-level conformance uses the conceptual checklist in §7; suites require pins/anchors rather than procedural validation.
* **Relates to G.10:** suites are not packs; G.10 handles shipping of Part-G outputs as a SoTA pack, while E.17 publishes reader-facing forms of an already accepted engineering account.

