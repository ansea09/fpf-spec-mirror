---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
section_id: "A.6.7:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__013_relations.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.6.7 — MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
  - "A.6.7:12 — Relations"
line_start: 24304
line_end: 24311
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

### A.6.7:12 - Relations

* **Relates to A.6.1:** suite members are `U.Mechanism`; the suite does not replace the mechanism definition.
* **Relates to A.6.5:** member operation declarations retain A.6.1 argument/result meanings, ValueKinds and binding rules. A.6.5 applies only where a cited `RelationSignature` independently declares participant SlotSpecs; there SlotKind stability, correct refMode and non-semantic SlotIndex remain required.
* **Relates to E.18 / P2W:** suite protocols describe intended composition; use E.18 for the selected transformation-flow structure and its crossings, and E.18.1 for P2W carry-through.
* **Suite conformance:** use §7 for the applicable requirements. Resolve required references and check the content and facts those requirements consume; a pin's presence alone does not establish conformance.
* **Relates to G.10:** suites are not packs; G.10 handles shipping of Part-G outputs as a SoTA pack, while E.17 publishes reader-facing forms of an already accepted engineering account.

