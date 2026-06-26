---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Context-Defined Way of Doing"
section_id: "A.3.1:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__012_sota-echoing.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "A.3.1 — U.Method: Context-Defined Way of Doing"
  - "A.3.1:11 — SoTA-Echoing"
line_start: 6472
line_end: 6482
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "B.1.5"
  - "C.2.P.DR"
  - "C.29"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "G.5"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.RoleAssignment"
keywords:
  - "abstract process"
  - "how-to"
  - "procedure"
  - "recipe"
---

### A.3.1:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current constructor-theory and process-theory work | Gogioso, Wang-Mascianica, Waseem, Scandolo, and Coecke, "Constructor Theory as Process Theory", EPTCS 397, 2023, arXiv:2401.05364; Deutsch and Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Adopt and adapt: method claims are interpreted through possible or intended transformations and their realization, not through software notation first. | The pattern starts from transformation or enactment kind and separates method, mechanism, description, plan, and work. |
| Current scoped-effects and handlers work | Bosman, van den Berg, Tang, and Schrijvers, "A Calculus for Scoped Effects & Handlers", LMCS 20(4), 2024, arXiv:2304.09697; Matache, Lindley, Moss, Staton, Wu, and Yang, "Scoped Effects as Parameterized Algebraic Theories", ESOP 2024 extended version, arXiv:2402.03103. | Adopt: operation syntax, semantic handling, scope, resources, equations, and type information plus effect information are separate concerns. | The pattern refuses to repair `algorithm`, `program`, or `function` to `method` merely by programming-paradigm label. |
| Current graph and equivalence representation work | Tiurin, Barrett, Ghica, and Hu, "Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs", arXiv:2406.15882, v2 revised 2025-05-20. | Adapt: graph, query, equivalence, and rewrite structures can be representations without being ordered instructions. | Graph path, query, and table overreads are repaired with `C.2.P.DR` unless a direct graph, method, work, evidence, or gate claim is recovered. |
| Historical declarative versus imperative programming contrasts | Codd 1970; Kowalski 1979; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004; Deutsch 2013; Deutsch and Marletto 2015. | Reject as current SoTA; retain only as lineage and regression contrast. | Older slogans such as "declarative versus imperative" are used only as recognition cues; the repair recovers FPF kind and slot. |

Refresh this pattern when current work on constructor theory, process theory, effect systems, process modeling, graph and equivalence representations, or FPF's own method, work, and mechanism patterns changes the governing distinction among method, method description, formal substrate, mechanism, work plan, dated work, and evidence.

