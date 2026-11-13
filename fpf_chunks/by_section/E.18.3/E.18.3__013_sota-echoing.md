---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__013_sota-echoing.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:11 — SoTA-Echoing"
line_start: 119209
line_end: 119222
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.PROD"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "G.11"
  - "G.5"
keywords:
---

### E.18.3:11 - SoTA-Echoing

| Exact source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| OMG, *Case Management Model and Notation (CMMN) Version 1.1*, December 2016 | Use as lineage for weakly structured case-work slices whose positions and relations are constrained without one fixed work order. | CMMN is not treated as current best-known process practice. E.18.3 does not import its notation or make a case-management method. |
| Aaron Küsters and Wil M.P. van der Aalst, "OCPQ: Object-Centric Process Querying & Constraints", arXiv:2506.11541, 2025 | Use the object-centric account of how typed objects and their relations jointly determine constraint queries. This reinforces multi-object flow positions, joins, many-to-many dependencies, exact relation preservation, and explicit reconsideration conditions. | OCPQ governs event-data queries and constraint checking. E.18.3 does not import event-log, query-language, or process-mining ontology, and an OCPQ result does not become transformation-flow structure. |
| Chiariello, Fionda, Ielo, and Ricca, "Direct Encoding of Declare Constraints in ASP", arXiv:2412.10152, 2024; Burattin, Maggi, and Sperduti, "Conformance Checking Based on Multi-Perspective Declarative Process Models", arXiv:1503.04957, 2015 | Use as declarative-process lineage for exact guards, crossings, and admissible path slices under several typed perspectives. | E.18.3 does not import Declare, MP-Declare, ASP, or conformance-checking ontology. |
| Hildebrandt and Mukkamala, "Declarative Event-Based Workflow as Distributed Dynamic Condition Response Graphs", EPTCS 69, 2011; Bagheri Hariri et al., "Verification of Semantically-Enhanced Artifact Systems", arXiv:1308.6292, 2013 | Use as DCR and artifact-centric lineage for distinct relation, condition, response, milestone, and artifact-state positions. | No DCR, GSM, database, or verification-method semantics are adopted as FPF ontology. |
| JuliaHub, [Dyad changelog](https://help.juliahub.com/dyad/stable/manual/changelog.html), [component syntax](https://help.juliahub.com/dyad/stable/manual/syntax.html), and [analysis documentation](https://help.juliahub.com/dyad/stable/analyses/udes.html), 2026. Bounded relation-first multi-domain modeling comparison using the cited component and analysis documentation. [Modelica 3.7](https://specification.modelica.org/) is retained only as historical acausal-modeling lineage, not as the SoTA basis. | Dyad keeps reusable component models and their relations distinct from analysis definitions, model compilation, solver or simulation work, and analysis results. E.18.3 adopts that separation for model-related transformation-flow slices: keep each value’s identity and exact connecting relation. The slice does not put all those values into one calculation or execution order. The separation helps distinguish a model from the work that computes and interprets its results; Modelica supplies historical lineage only. | E.18.3 governs only the selected transformation-flow slice that prepares, checks, or uses model-related structure. It does not govern the physical model, compiler or solver semantics, analysis result, performed simulation, or agent edit. |
| Ma, Gowda, Anantharaman, Laughman, Shah, and Rackauckas, "ModelingToolkit: A Composable Graph Transformation System For Equation-Based Modeling", arXiv:2103.05244; Rackauckas et al., "Composing Modeling and Simulation with Machine Learning in Julia", arXiv:2105.05946; Functional Mock-up Interface standard | Use these model-toolchain sources to keep symbolic model structure, graph transformations, calibration analyses, surrogate components, exchange packages, and result publications as independently identified values connected through already-obtaining transformation-flow relations; any claim about them keeps its own criterion and current basis. | E.18.3 does not prove mathematical adequacy, domain validity, evidence readiness, source currentness, or publication truth. Those claims use `C.29`, domain DPF patterns, evidence patterns, `G.11`, or publication patterns as applicable. |
| Current FPF `E.18`, `E.23`, `C.18`, `C.19`, and `G.11` practice | Use local path slices, feedback relations, candidate-population stewardship, and currentness values as independently identified neighboring values or claims shown to obtain under their own criteria rather than one master process. | Architecture, work, evidence, improvement, archive, front, pool, E.18 slice-local refresh, and G.11 currentness claims keep applicable definitions, constraints, predicates, tests, evidence rules, and assurance rules distinct from the current facts or evidence that satisfy them. A Method contributes a reusable way of doing and applicability or bounds; it is not thereby a criterion for those claims. |

In the 7 August 2026 comparison, OCPQ was the research comparator for typed multi-object constraint structure, and the cited Dyad documentation supplied a bounded engineering comparison of relation-first models kept separate from analysis definitions, compilation, execution, and results. Modelica 3.7 supplies historical acausal-modeling lineage only; the older CMMN, Declare, DCR, and artifact-centric rows also supply lineage. Reopen the adoptions when object-centric constraint methods change object-relation treatment, model languages change model-analysis separation, or use evidence shows that these distinctions no longer prevent workflow, query-result, or execution-artifact overread.

