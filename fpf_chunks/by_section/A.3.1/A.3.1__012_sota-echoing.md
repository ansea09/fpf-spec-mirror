---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__012_sota-echoing.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:11 — SoTA-Echoing"
line_start: 7031
line_end: 7043
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.22"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.REL"
  - "B.1.5"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.20"
  - "C.29"
  - "C.36"
  - "C.36.P"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "F.9"
  - "G.11"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
---

### A.3.1:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Constructor-theory and process-theory bridge, with a current time treatment | Gogioso, Wang-Mascianica, Waseem, Scandolo, and Coecke, ["Constructor Theory as Process Theory"](https://arxiv.org/abs/2401.05364), EPTCS 397, 2023; Deutsch and Marletto, ["Constructor theory of time"](https://arxiv.org/abs/2505.08692), arXiv v3, revised 2026-06-05. | Adopt the separation between a transformation specified as possible or impossible and a concrete process that realizes it. Adapt it beyond physical tasks: an FPF method is identified through the bounded way of transforming or preserving its governed entity or structure; a concrete realizer is connected to a mechanism declaration by a separate realization relation; dated enactment belongs to work. The 2023 paper is a formal bridge and the 2026 paper is a current extension, not evidence that constructor theory alone supplies a universal method ontology. | The pattern starts from transformation or enactment kind and separates method, mechanism, mechanism realization, description, plan, and work. The manufacturing case no longer lets equipment equations or one tool run define the reusable method. |
| Scoped effects, handlers, and current semantic non-uniqueness | Bosman, van den Berg, Tang, and Schrijvers, ["A Calculus for Scoped Effects & Handlers"](https://arxiv.org/abs/2304.09697), LMCS 20(4), 2024; Matache, Lindley, Moss, Staton, Wu, and Yang, ["Scoped Effects as Parameterized Algebraic Theories"](https://arxiv.org/abs/2402.03103), ESOP 2024 extended version; Kura, ["On Complete Categorical Semantics for Effect Handlers"](https://arxiv.org/abs/2602.03275), current 2026 preprint. | Adopt the separation among operation syntax, handling semantics, scope, resources, equations, and type-and-effect information. Kura's result strengthens the guard: even a sound formal account need not be the only semantic model of the same handling constructs. Adapt only as a software-derived stress test; these calculi do not define methods in manufacturing, medicine, or organizational work. | The pattern refuses to repair `algorithm`, `program`, `function`, handler syntax, or one semantic model to `U.Method` merely by programming-paradigm label. The proof and optimization cases ask for the bounded way of doing before admitting a method identity. |
| Current graph, binding, and persistent-equivalence representations | Tiurin, Barrett, Ghica, and Hu, ["Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs"](https://arxiv.org/abs/2406.15882), revised 2025-05-20; Tiurin, Ghica, and Hu, ["Categorical E-Graphs for Lambda Calculi"](https://arxiv.org/abs/2505.00807), revised 2026-06-25; Merckx et al., ["E-Graphs as a Persistent Compiler Abstraction"](https://arxiv.org/abs/2602.16707), current 2026 preprint. | Adapt the demonstrated distinction between represented equivalence or rewriting structure and an ordered instruction sequence. Binding-aware hierarchical hypergraphs and equivalence state preserved across several intermediate-representation levels show why neither graph layout nor one representation level establishes the semantic method or dated work order. These sources are compiler and formal-representation results, not a general ontology of project methods. | Graph paths, queries, tables, rewrite graphs, and persistent compiler structures remain descriptions or formal lenses until a direct method, method-relation, work, evidence, or gate claim is recovered. The graph-overread case and `C.2.P.DR` exit carry this safeguard. |
| Historical declarative versus imperative programming contrasts | Codd 1970; Kowalski 1979; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004; Deutsch 2013; Deutsch and Marletto 2015. | Reject as current SoTA; retain only as lineage and regression contrast. | Older slogans such as "declarative versus imperative" are used only as recognition cues; the repair recovers the exact FPF governed object and claim. |

Review a project's current `U.Method` identification when its bounded context, transformation or enactment kind, transformed entity or structure, preconditions, effects, bounds, or work-facing acceptance relation changes. Review only the linked description, work, mechanism, representation, or evidence relation when that neighboring value changes without changing a method-identity basis. Review the method family or selector under `G.5` only when the available family no longer separates the methods or variants needed for the current use.

When a receiving use relies on the currentness, edition, freshness, telemetry, or decay status of a cited method description or SoTA source, use `G.11` for that currentness relation. A new paper, source edition, implementation, or run is a reason to inspect the affected relation; it does not change the method merely by being newer. Reconsider the A.3.1 distinction itself only when stronger work on constructor theory, process theory, effect systems, process modeling, practice theory, cultural evolution, graph or equivalence representation, or FPF's direct method neighbors overturns a distinction on which the project relies.

