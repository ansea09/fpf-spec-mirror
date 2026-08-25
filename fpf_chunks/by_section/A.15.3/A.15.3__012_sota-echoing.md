---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__012_sota-echoing.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:11 — SoTA-Echoing"
line_start: 25017
line_end: 25024
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "U.WorkPlan"
keywords:
  - "WorkPlan claim content"
  - "actual-use predicate"
  - "baseline replay"
  - "concrete RefKind and policy"
  - "direct owner"
  - "edition pin"
  - "exact declaration member"
  - "intended-performance designator"
  - "no actuality by plan"
  - "open-world omission"
  - "participant/argument/result meaning"
  - "positive planned designation"
  - "semantic cardinality"
---

### A.15.3:11 - SoTA-Echoing

| Current practice line | Adoption in A.15.3 | Rejected shortcut |
| --- | --- | --- |
| ISO/IEC/IEEE 12207:2017 and ISO/IEC/IEEE 15288:2023 distinguish process descriptions, planning, execution, and information items while allowing local life-cycle adaptation. | Keep the declaration, intended plan content, and performed work separate. | Treating a process-tooling layout or checklist field as an FPF declaration. |
| SLSA v1.2 provenance and in-toto Statement v1 separate build definition, run details, subjects, predicates, and resolved dependencies. | Cite declaration and edition only when replay depends on them; keep run, provenance, result, and evidence claims separate. | Importing a supply-chain record schema as a universal slot or result ontology. |
| Nix flake-lock practice makes selected dependency revisions explicit for reproducibility. | Pin a declaration or value edition only when resolving another edition could change the planned meaning. | Saying *latest* when a later comparison needs one edition. |

