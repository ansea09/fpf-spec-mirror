---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__013_sota-echoing.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:11 — SoTA-Echoing"
line_start: 31568
line_end: 31580
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "B.3.5"
  - "B.5.2"
  - "C.13"
  - "C.2.P.DR"
  - "C.3"
  - "C.32.P2S"
  - "C.35"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.23"
  - "E.9"
  - "E.9.DA"
  - "G.11"
keywords:
---

### A.22.CGUS:11 - SoTA-Echoing

| Exact source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| Object Management Group, *Case Management Model and Notation (CMMN) Version 1.1*, December 2016 | Adopt the weakly structured case-work pressure: possible work items and constraints may be visible without selecting one performed-work order. | Do not import CMMN notation or treat CGUS as a case-management method. |
| Chiariello, Fionda, Ielo, and Ricca, "Direct Encoding of Declare Constraints in ASP", arXiv:2412.10152, 2024; Burattin, Maggi, and Sperduti, "Conformance Checking Based on Multi-Perspective Declarative Process Models", arXiv:1503.04957, 2015 | Adopt declarative constraints and multi-perspective loci as pressure for admissible traces without first selecting one imperative sequence. | FPF does not import Declare, MP-Declare, ASP, or conformance-checking ontology. |
| Hildebrandt and Mukkamala, "Declarative Event-Based Workflow as Distributed Dynamic Condition Response Graphs", EPTCS 69, 2011 | Use DCR relation pressure for condition, response, include, exclude, role, and distribution-like loci. | Do not import DCR graph semantics as FPF workflow ontology. |
| Bagheri Hariri, Calvanese, Montali, Santoso, and Solomakhin, "Verification of Semantically-Enhanced Artifact Systems", arXiv:1308.6292, 2013, with artifact-centric and GSM lineage | Adapt attention to object/lifecycle state, stages, milestones, guards, and artifact state as pressure for named loci and guarded transitions. | CGUS does not become an artifact lifecycle method, database schema, or verification method. |
| ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise - Architecture description* | Use architecture-description separation as pressure to keep structure, description, viewpoint, view, correspondence, and publication apart. | Architecture-specific claims remain with `C.30` and `C.32`. |
| Modelica Association, *Modelica Language Specification* 3.6 (2023) and 3.7 (2026); JuliaHub, Dyad product page and Dyad documentation v3.0.0 | Adopt only the relation-first pattern: model components expose relations, connection constraints, units, conservation relations, and modes before one causal direction, calculation order, compiler output, solver run, or simulation trace is selected. | FPF does not import DAE, Modelica, Dyad, solver, compiler, or AI-agent ontology. A solver run, compiler output, or AI-assisted edit is a use over a model structure, not the CGUS itself. |
| Ma, Gowda, Anantharaman, Laughman, Shah, and Rackauckas, "ModelingToolkit: A Composable Graph Transformation System For Equation-Based Modeling", arXiv:2103.05244; Rackauckas et al., "Composing Modeling and Simulation with Machine Learning in Julia", arXiv:2105.05946; Functional Mock-up Interface standard | Use the model-toolchain separation to keep reusable symbolic model structure, structural transformations, analysis records, calibration records, model-discovery records, surrogate-substitution relations, model-exchange packages, and result publications as different loci or direct governing-pattern records. | FPF does not import FMI, digital-twin, ML-surrogate, calibration, or co-simulation ontology. Mathematical model claims use `C.29`; currentness, evaluation, evidence, publication, and domain-validity claims exit to their direct governing patterns. |
| FPF pattern-language practice | Use demonstrative slices and entry seeds for learnability while keeping pattern bodies as governing authority. | A first-entry route, example, or public card is not the specification. |

