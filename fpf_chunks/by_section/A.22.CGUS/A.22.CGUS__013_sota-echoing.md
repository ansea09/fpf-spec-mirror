---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__013_sota-echoing.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:11 — SoTA-Echoing"
line_start: 35148
line_end: 35162
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "B.3.5"
  - "B.5.2"
  - "C.13"
  - "C.18"
  - "C.19"
  - "C.2.P.DR"
  - "C.3"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.18.NET-conforming"
  - "E.23"
  - "E.24.PUB"
  - "F.17"
  - "G.11"
  - "G.5"
keywords:
---

### A.22.CGUS:11 - SoTA-Echoing

| Exact source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| Object Management Group, *Case Management Model and Notation (CMMN) Version 1.1*, December 2016 | Use as lineage for the weakly structured case-work pressure: possible work items and constraints may be visible without selecting one performed-work order. | CMMN is not treated as current best-known process practice. Do not import its notation or treat CGUS as a case-management method. |
| Esser and Fahland, "OCPQ: Object-Centric Process Querying & Constraints", arXiv:2506.11541, 2025 | Adopt the current object-centric pressure that several typed objects and their relations can jointly determine a constraint query. This reinforces graph-shaped starts, joins, many-to-many dependencies, and relation-preserving continuation without reducing the case to one trace. | OCPQ governs event-data querying and constraint checking. CGUS does not import event-log, query-language, or process-mining ontology, and a query result does not become the unfolding structure. |
| Chiariello, Fionda, Ielo, and Ricca, "Direct Encoding of Declare Constraints in ASP", arXiv:2412.10152, 2024; Burattin, Maggi, and Sperduti, "Conformance Checking Based on Multi-Perspective Declarative Process Models", arXiv:1503.04957, 2015 | Use as declarative-process lineage for constraints and multiple typed perspectives that admit traces without first selecting one imperative sequence. | FPF does not import Declare, MP-Declare, ASP, or conformance-checking ontology. |
| Hildebrandt and Mukkamala, "Declarative Event-Based Workflow as Distributed Dynamic Condition Response Graphs", EPTCS 69, 2011 | Use as DCR lineage for keeping conditions, responses, inclusions, exclusions, role assignments, and distribution relations distinct. | Do not import DCR graph semantics as FPF workflow ontology. |
| Bagheri Hariri, Calvanese, Montali, Santoso, and Solomakhin, "Verification of Semantically-Enhanced Artifact Systems", arXiv:1308.6292, 2013, with artifact-centric and GSM lineage | Use as artifact-centric lineage for object state, stages, milestones, guards, and state transitions as pressure for typed positions and guarded relation changes. | CGUS does not become an artifact lifecycle method, database schema, or verification method. |
| JuliaHub, Dyad 3.2 component and analysis documentation (2026); Modelica Association, *Modelica Language Specification* 3.7 (2026) | Adopt Dyad 3.2 as the current engineering comparator: reusable components expose relation-first structure and constraints, while separately selected analyses run on a model and produce solution objects and artifacts. Retain Modelica 3.7 as historical lineage for acausal declarative modeling. | FPF imports neither Dyad nor Modelica ontology. A model structure, analysis description, performed analysis, solution object, artifact, compiler output, solver run, or AI-assisted edit remains a distinct object or use; none is the CGUS merely by adjacency. |
| Ma, Gowda, Anantharaman, Laughman, Shah, and Rackauckas, "ModelingToolkit: A Composable Graph Transformation System For Equation-Based Modeling", arXiv:2103.05244; Rackauckas et al., "Composing Modeling and Simulation with Machine Learning in Julia", arXiv:2105.05946; Functional Mock-up Interface standard | Use the model-toolchain separation to preserve the distinct kinds and relations of reusable symbolic model structures, structural transformations, analysis records, calibration records, model-discovery records, surrogate-substitution relations, model-exchange packages, and result publications. | FPF does not import FMI, digital-twin, ML-surrogate, calibration, or co-simulation ontology. Mathematical model claims use `C.29`; currentness uses `G.11`; evaluation, evidence, publication, and domain-validity claims use the exact applicable patterns. |
| FPF pattern-language practice | Use provisional demonstrations before structure admission and demonstrative slices afterward, while keeping exact rule content in pattern bodies as the defining source. | A first-entry route, example, or public card is neither admission evidence by itself nor the specification. |

As of 2026-08-04, OCPQ supplies the current research comparator for typed multi-object constraint queries, while Dyad 3.2 supplies the current engineering comparator for reusable relation-first components separated from analyses and their produced solution objects and artifacts. Modelica 3.7 remains historical lineage for acausal declarative modeling. The older CMMN, Declare, DCR, and artifact-centric rows likewise provide lineage and known distinctions, not present-day authority by age or official status. These sources changed `4.2` by requiring graph-shaped and many-to-many recovery, `4.3` by separating a demonstration from the wider structure, and the physical-modeling slice by separating reusable relations from analysis and execution. Reopen these adoptions when a newer object-centric constraint method changes the treatment of objects or relations, when the modeling languages change component-relation or analysis separation, or when use evidence shows that the imported distinction no longer prevents chain or execution-artifact overread.

