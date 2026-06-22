---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__012_sota-echoing.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:11 — SoTA-Echoing"
line_start: 22375
line_end: 22383
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.7"
  - "B.3"
  - "C.27.TA"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.20"
  - "E.24"
  - "G.11"
  - "G.6"
  - "U.RelationSlotDiscipline"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

### A.15.3:11 - SoTA-Echoing

| Current practice line | Adoption in A.15.3 | Rejected shortcut |
| --- | --- | --- |
| ISO/IEC/IEEE 12207:2017 and ISO/IEC/IEEE 15288:2023 keep life-cycle processes adaptable and distinguish process descriptions, planning, execution, and information items without prescribing one method or documentation form. | Adopt the process-information separation: A.15.3 is one planned-baseline information item inside work planning, not the work and not one universal process model. | Treating a process-tooling layout, stage model, or checklist as the FPF baseline ontology. |
| SLSA v1.2 provenance and in-toto Statement v1 separate build definition, run details, subjects, predicates, and resolved dependencies for software-supply-chain replay. | Use this only as an analogy for reproducibility and provenance separation: planned fillers and refs are recorded before work, while performed work, provenance, evidence, subject claims, and output claims remain separate FPF relations. | Importing supply-chain ontology as FPF ontology, or treating provenance, evidence, or an attestation record as the planned baseline itself. |
| Nix flakes and `flake.lock` practice show current dependency pinning: unlocked inputs are resolved to locked revisions and content hashes for reproducibility. | Adopt explicit pinning discipline for planned fillers, edition pins, and time rules when replay depends on them. | Saying "latest" or relying on a generated view when a bounded plan needs pinned planned rows. |
| Contemporary reproducible-build and supply-chain practice favors small attributable deltas and stable refs over mutable hidden defaults. | A.15.3 keeps planned rows stable, then lets performed work record variance, substitution, and crossing witnesses. | Editing the plan after execution so that no variance remains. |

