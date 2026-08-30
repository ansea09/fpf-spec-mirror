---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Description of a set of distinct mechanisms"
section_id: "A.6.7:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__013_relations.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.6.7 — MechSuiteDescription — Description of a set of distinct mechanisms"
  - "A.6.7:12 — Relations"
line_start: 20423
line_end: 20430
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.18"
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
* **Relates to E.18 / P2W:** suite protocols describe intended composition; actual composition and crossings are expressed in E.18 subgraphs and P2W flow.
* **Relates to E.19:** suite-level conformance is a conceptual review checklist; suites require pins/anchors rather than procedural validation.
* **Relates to G.10:** suites are not packs; publication/shipping is handled via G.10 and MVPK faces.

