---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:5"
section_title: "Worked Correspondence Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__006_worked-correspondence-cases.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:5 — Worked Correspondence Cases"
line_start: 65701
line_end: 65720
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.19.CPM"
  - "A.2.1"
  - "A.22"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3"
  - "C.11"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ACS"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "E.18.NET"
  - "F.6"
  - "G.5"
  - "U.Structure"
keywords:
---

### C.32.CONWAY:5 - Worked Correspondence Cases

| Grounded working case | Acting and performance facts | Influence-source and architecture-pair facts | Candidate work | Stop or return |
|---|---|---|---|---|
| Product family and manufacturing system | The product referent and bounded A.3.4 transformation are identified independently when actual change is claimed. The admitted manufacturing and certification Systems jointly perform dated architecturing Work, each through its complete A.15.1/F.6 basis; the direct Work-to-change relation remains separate. | One obtaining C.30 `ArchitectureRelation` connects the manufacturing-and-certification holon to its shared batch-line evidence structure; another connects the product-family holon to its current field-module structure. A Plant-A domain declaration defines the influence predicate between those exact occurrences, and current case facts satisfy it. Neither architecture-bearing holon nor architecture relation is inferred to be a performer. | Prepare manufacturing-cell change, product-module split, joint change, and bounded batch exception. | Stop at candidate preparation. Handle product choice or architecture decision under `C.11` or `C.32.PAD`; factory Work authorization through its direct authority or permission relation or an `A.20`/`A.21` gate; and certification evidence or assurance through `A.10` or `B.3`. |
| Organization designing and operating a service platform | Each acting team or organization is used through its admitted `U.System` identity; any actual design or operations Work points to its complete A.15.1/F.6 basis. | Communication, deployment, test, and approval structures influence one service-platform architecture pair through their direct relations. | Prepare a service-boundary, platform-mediation, or bounded-coordination-cost change. If responsibility retargeting is proposed, name the exact responsibility predicate and old and proposed participants; otherwise mark that branch `missing-governor` instead of calling it a team or test role change. | Stop before an organization-redesign decision or authority claim and apply the exact predicate and test for that claim. Use `G.5` for selected-set result declaration and `C.32.PAD` for an architecture decision. When publication is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. |
| Review method influencing authored work products | The method description does not act. When review is performed, point to the review Work's complete A.15.1/F.6 basis and state any Work-to-change relation separately. | The review-method or evidence structure influences the authored-section architecture through its exact method-use, evidence-scope, or project influence relation. | Add a prospective exception-assignment requirement and evidence scope, change the Method step, change the work-product structure, or reject the automation candidate. | Stop before method-governance or publication claims. For method use, apply the direct predicate and the pattern that defines and tests it. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. Use `G.5` only when selected-set result declaration is current. |
| Instructional system changing learner capability | Each instructor or instructional organization is used through its admitted `U.System` identity; any actual teaching Work points to its complete A.15.1/F.6 basis. | Curriculum, feedback, and evidence structures influence the architecture claim about the changed learner-capability referent; they do not become the learner or the performer by influence. | Prepare curriculum, a prospective feedback-assignment requirement, evidence scope, or bounded-cohort candidates. | Stop before educational policy, evidence-sufficiency, or ethical-mediation claims; state them under the exact policy predicate, `A.10`, or `D.4` respectively. |
| AI-agent toolchain changing project work products | An admitted execution System performs any actual tool-call or authoring Work through its complete A.15.1/F.6 basis. | Toolchain control and evidence-refresh structures influence the transformed work-product architecture through exact relations; the toolchain architecture itself does not act. | Add supervision and refresh, change task decomposition, or keep bounded autonomy with source return. | Stop before safety, gate or release, or assurance claims; state them under the exact safety predicate, `A.20`/`A.21`, or `B.3` respectively. |
**Exact positive, distributed-performer, and network-local slice.** In one Plant-A domain framework, `PlantArchitectureInfluenceRelations-v3` defines `BatchEvidenceArchitectureConstrainsModuleArchitecture(sourceArchitectureRelation, transformedArchitectureRelation, evolutionWindow)`. Its first participant is the obtaining C.30 `ArchitectureRelation(ManufacturingCertificationSystem@Plant-A, BatchLineSharedEvidenceStructure@Current)`; its second is the obtaining C.30 `ArchitectureRelation(ProductFamily@Current, FieldModuleBoundaryStructure@Current)`. Both occurrences are explicitly individuated under A.6.REL because this domain predicate uses them as participants. Plant-A facts satisfy that predicate over `ProductFamilyModuleChange@2026Q3`, so `BatchEvidenceConstrainsFieldModules-17` is the exact obtaining influence occurrence and the EntityOfConcern of `BatchEvidence-to-FieldModules-Row-17`. This case-local predicate and occurrence do not mint a universal Conway relation.

The changed referent is independently identified as `ProductFamilyFieldModuleBoundary@2026Q3`. When the same case also claims actual change, A.3.4 independently identifies `FieldModuleBoundaryTransformation-17 : U.Transformation`. `ModuleTransitionArchitecturingWork-17 : U.Work` has the closed extent `2026-07-14T09:00:00+03:00` to `2026-07-16T18:00:00+03:00`, enacts `ModuleTransitionArchitecturingMethod-v3`, and obtains under `executedWithin(ModuleTransitionArchitecturingWork-17, ProductFamilyEngineeringSystem-A)` for admitted `ProductFamilyEngineeringSystem-A : U.System`. Two admitted systems jointly perform that top-level Work. The local `PlantArchitecturingSystemRoleKindDomain` admits `ManufacturingArchitectureSystemRole` and `CertificationArchitectureSystemRole`. `PlantArchitecturingWorkAssignment` is a directly declared two-participant species under `U.SystemRoleAssignment`: its `HolderSystemSlot` admits `U.System`, its declaration-local `AssignedSystemRoleKindSlot` uses that exact local domain, and its predicate says that the holder is selected to supply the denoted architecturing contribution for Plant-A transition Work. `ManufacturingArchitectureAssignment-17 : PlantArchitecturingWorkAssignment` fixes `<ManufacturingArchitectureTeam-A, ManufacturingArchitectureSystemRole>`; `CertificationArchitectureAssignment-17 : PlantArchitecturingWorkAssignment` fixes `<CertificationArchitectureTeam-A, CertificationArchitectureSystemRole>`. Each occurrence continues through its maximal uninterrupted predicate-true interval and covers the full Work extent. F.6 occurrences `performedUnderAssignment(ModuleTransitionArchitecturingWork-17, ManufacturingArchitectureAssignment-17)` and `performedUnderAssignment(ModuleTransitionArchitecturingWork-17, CertificationArchitectureAssignment-17)` obtain, and each separately named performer equals its assignment's `HolderSystemSlot`. The Plant-A domain predicate `ArchitecturingWorkChangesModuleBoundary(ModuleTransitionArchitecturingWork-17, FieldModuleBoundaryTransformation-17)` supplies the separately governed Work-to-change fact. This is the A.15.1 `CC-A15.1-17` joint-performer form; neither a lead assignment nor the architecture pair substitutes for either performer. Taxonomy and scheme epistemes may interpret an assertion but are not assignment participants.

`ProductDevelopmentNetworkRecord-2026Q3` may cite `BatchEvidence-to-FieldModules-Row-17` once in `architectureCorrespondenceRowRefs[]`. That citation contributes one reading of the exact two C.30 architecture-relation occurrences. The pair row remains an episteme, not the `TransformationFlowStructureNetwork`, not one of its members, and not a cross-flow relation. Its optional `networkCrossFlowRelationRowRef` stays absent unless this same influence occurrence is independently grounded at exact member-flow positions and the composite E.18.NET locator resolves exactly one matching row in that same current record edition.

**Network-qualified reading.**
A product-development TFS and a production-system-change TFS participate in one selected E.18.NET-conforming network. A current architecture pair row about manufacturing-architecture influence may be cited by the network record alongside a separately grounded obtaining production or project occurrence. If the pair row also carries `networkCrossFlowRelationRowRef`, that locator names this same exact current record edition and resolves exactly one matching row; it qualifies no citation from another record. The pair row remains one reading of one exact architecture pair. It is neither the network nor proof that the architecture-influence occurrence is the cross-flow occurrence.

**Near miss.** A diagram places a factory architecture beside a product architecture and labels the arrow “shapes”. No direct relation kind and predicate govern that pair and use. The frame may retain the pair as synthesis-local pressure, but the exact row and network cross-flow mapping remain absent with `missing-governor`; the diagram does not create an occurrence.

