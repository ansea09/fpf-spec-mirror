---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem: Plan a Value for an Existing Declaration Member"
section_id: "A.15.3:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__012_sota-echoing.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem: Plan a Value for an Existing Declaration Member"
  - "A.15.3:11 — SoTA-Echoing"
line_start: 30229
line_end: 30236
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
| [ISO/IEC/IEEE 12207:2017](https://www.iso.org/standard/63712.html) describes software life-cycle processes, activities and tasks; it is retained as a historical anchor, withdrawn on 29 April 2026 and superseded by [12207:2026](https://www.iso.org/standard/90219.html). [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) provides system life-cycle process descriptions without prescribing a specific life-cycle model and refers detailed information-item content to ISO/IEC/IEEE 15289. | Keep the declaration, intended plan content, and performed work separate. | Treating a process-tooling layout or checklist field as an FPF declaration. |
| [SLSA v1.2 build provenance](https://slsa.dev/spec/v1.2/build-provenance) separates build definition, including resolved dependencies, from run details; [in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) separates subjects from the typed predicate content. | Cite declaration and edition only when replay depends on them; keep run, provenance, result, and evidence claims separate. | Importing a supply-chain record schema as a universal slot or result ontology. |
| The [Nix 2.26 manual’s lock-file mechanism](https://nix.dev/manual/nix/2.26/command-ref/new-cli/nix3-flake.html#lock-files) records resolved dependency inputs in `flake.lock`, including revisions where applicable and content hashes. An existing, up-to-date lock file preserves the selected direct and transitive dependencies for repeatable input resolution. | Pin the selected declaration or value episteme when another resolution could change the planned meaning. | Saying *latest* when a later comparison needs one edition. |

