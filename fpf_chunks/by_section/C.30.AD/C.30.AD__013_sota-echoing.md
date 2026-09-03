---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__013_sota-echoing.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:10 — SoTA-Echoing"
line_start: 59761
line_end: 59772
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
  - "A.6.3.NAR"
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
  - "E.10.D2"
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

### C.30.AD:10 - SoTA-Echoing

**Deliberate exclusion.** SysML v2 is not used here as SoTA or useful lineage. Search prominence, a systems-oriented name, and long-standing promotion do not show that it improves the practitioner questions above, and this pattern has no project evidence that it does. For C.30.AD it is a historical dead end. Reopen this boundary only if concrete project results change a rule, worked case, or practitioner action in this pattern.

| Practice or source line | Source-use relation and currentness | C.30.AD adoption | Action consequence | Boundary |
| --- | --- | --- | --- | --- |
| FPF `C.2.1`, `A.22`, `E.17.0`, `C.30`, and `C.30.ASV` separate episteme identity, selected structures, direct architecture relations, architecture claims, and structural-view adequacy. | Current internal definitions for the objects used by this pattern. | Reuse these objects instead of importing a second architecture-description ontology. | Disciplines `C.30.AD:4.1`, `C.30.AD:4.1a`, `C.30.AD:4.2`, `CC-C30AD-1`, `CC-C30AD-3`, and `CC-C30AD-4`: every description has one exact EntityOfConcern and scheme; every asserted view has exact viewpoint conformance; correspondence and source use are explicit. | A description or view remains an episteme and does not become architecture, proof, decision, or release authority. |
| Views-and-Beyond and related architecture documentation practice treats views as stakeholder-relevant projections over architecture. | Mature reference and lineage source for view-based architecture documentation; not used as a mandatory current catalog. | Adopt view usefulness while requiring exact E.17.0 viewpoint conformance and structure-kind recovery through `C.30.ASV`; description-set use remains claim content or a separate relation that actually holds. | Disciplines `C.30.AD:4.1a`, `C.30.AD:4.2`, and the multi-view worked case: a view remains useful for a working concern without becoming the selected structure or a `U.View` by label. | No mandatory view catalog or local membership relation is imported, and view adequacy remains in `E.17.0` and `C.30.ASV`. |
| `E.17.0` and MVPK publication machinery in current FPF. | Current internal FPF definitions and publication practices for views, viewpoints, publication occurrences, forms, carriers, and publication separation. | Reuse generic view and publication machinery instead of minting architecture-local copies. | Disciplines `C.30.AD:4.1a`, `C.30.AD:4.5`, `CC-C30AD-5`, and `CC-C30AD-6`: architecture-description identity and composition remain separate from representation, publication occurrence, form, carrier, and publication-currentness. | C.30.AD specializes architecture-description use; it does not replace E.17.0, E.17.1, E.17.2, E.17, E.24.PUB, or C.2.P. |
| C4, arc42, ADR, model-card, and system-card practice makes architecture communication practical. | Current practitioner-source family for familiar architecture publication and documentation forms. | Admit these as possible source publications, view publications, decision-description publications, transparency publications, or specification-use records. | Disciplines `C.30.AD:4.5`, worked cases, and anti-patterns: practitioners can use familiar forms while keeping source, representation, publication, description, architecture, evidence, gate, decision, work authorization, release authorization, and other non-description claims separate. | Template, card, graph, or diagram quality is not architecture adequacy by itself. |
| Tool-generated architecture relation graphs and code-agent architecture probing expose useful but partial structure. | Emerging practitioner practice for recovering architecture-relevant relations from code, models, and generated analyses; currentness depends on the analyzed edition and tool run. | Treat generated graphs as representations or source-derived descriptions with observed, inferred, and unknown relation boundaries. | Disciplines `C.30.AD:4.3`, `C.30.AD:5`, and `CC-C30AD-4`: a generated output can guide structure recovery and next architecture moves only through a named source-to-use path; stronger use activates the declared source-return condition. | Generated relation coverage does not become an obtaining subject relation, `U.View`, proof, gate passage, safety assurance, or complete architecture. |

