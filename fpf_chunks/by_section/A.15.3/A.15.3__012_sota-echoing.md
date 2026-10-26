---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem: Plan a Value for an Existing Declaration Member"
section_id: "A.15.3:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__012_sota-echoing.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem: Plan a Value for an Existing Declaration Member"
  - "A.15.3:11 — SoTA-Echoing"
line_start: 30089
line_end: 30096
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

| Source contribution | Adoption in A.15.3 | Rejected shortcut |
| --- | --- | --- |
| ISO/IEC/IEEE 12207:2017 and ISO/IEC/IEEE 15288:2023 distinguish process descriptions, planning, execution, and information items while allowing local life-cycle adaptation. | Keep the declaration, intended plan content, and performed work separate. | Treating a process-tooling layout or checklist field as an FPF declaration. |
| [SLSA v1.2 build provenance](https://slsa.dev/spec/v1.2/build-provenance) separates build definition, including resolved dependencies, from run details; [in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) separates subjects from the typed predicate content. | Cite declaration and edition only when replay depends on them; keep run, provenance, result, and evidence claims separate. | Importing a supply-chain record schema as a universal slot or result ontology. |
| Nix flake-lock practice makes selected dependency revisions explicit for reproducibility. | Pin the selected declaration or value episteme when another resolution could change the planned meaning. | Saying *latest* when a later comparison needs one edition. |

