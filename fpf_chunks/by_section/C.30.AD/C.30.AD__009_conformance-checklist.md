---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:6"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__009_conformance-checklist.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:6 — Conformance checklist"
line_start: 55766
line_end: 55778
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD.BA"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.5"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "candidate-description boundary"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:6 - Conformance checklist

| Check | Requirement | Repair if failed |
| --- | --- | --- |
| **CC-C30AD-1 EntityOfConcern.** | The architecture description's `DescriptionContext.EntityOfConcernRef` points to one `ArchitectureOf@Context` claim record. | Add `architectureClaimRef` or use `C.30` until the architecture claim is recoverable. |
| **CC-C30AD-2 Described holon recovery.** | The described holon is recovered through `ArchitectureOf@Context.describedHolonRef`, not by replacing the description EntityOfConcern with the holon. | Restore the strict description boundary and copy only the recoverable holon ref. |
| **CC-C30AD-2a Traceable multi-view chain.** | The description use recovers the chain from working concern or A.15 allocation-responsibility family being used through viewpoint, selected structure or structure kind, architecture claim, ASV view, architecture description, source or publication use when source or publication use is being made, correspondence when used or source return when needed, and remaining admissible architecture move. | Add the missing reference, reduce the admissible use, or apply the governing pattern that can recover the missing relation. |
| **CC-C30AD-3 Viewpoint and structure kind.** | Every architecture structural view names viewpoint and selected structure or structure kind. | Use `C.30.ASV` before relying on the view. |
| **CC-C30AD-4 Correspondence and source return.** | Cross-view, generated-view, source-derived, reused, regulated, or comparison use names correspondence or source-return condition. | Add correspondence and source-return fields or reduce the admissible use. |
| **CC-C30AD-5 Publication boundary.** | Publication face, publication form, diagram, dashboard, card, file, or rendering is not treated as architecture, decision claim, evidence, assurance, gate passage, performed work, work authorization, or release authorization. | Assign publication or source use to `C.2.P` or `E.17` and the non-architecture claim to the direct pattern governing that claim. |
| **CC-C30AD-6 Specification-use boundary.** | Specification use is declared as use over a Description episteme or publication, with direct governing-pattern applications when it carries a non-description claim. | Add `ArchitectureDescriptionSpecificationUse@Project` or demote to ordinary description. |
| **CC-C30AD-7 Remaining architecture candidate use.** | The bounded description still tells the practitioner what architecture move, view normalization, source return, or governing-pattern application remains. | Add the remaining architecture candidate use or reduce the text to source or publication use. |

