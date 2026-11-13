---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__012_sota-echoing.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:11 — SoTA-Echoing"
line_start: 44230
line_end: 44240
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "E.10"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.6"
  - "G.5"
  - "U.Signature"
  - "U.Work"
keywords:
  - "A.6.RCD claim disposition"
  - "assurance hooks"
  - "capability continuity"
  - "composite-Method boundary account"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "methodPartOf"
  - "order-sensitive method"
  - "submethod"
  - "typed join"
  - "work enactment"
---

### B.1.5:11 - SoTA-Echoing

The following published treatments provide bounded comparisons for Method composition. Their models illuminate distinctions; applying those distinctions to FPF Methods uses the construction and identity tests above.

| Published treatment and its contribution | Use in B.1.5 | Applicability limit |
| --- | --- | --- |
| Case and decision models in [CMMN 1.1](https://www.omg.org/spec/CMMN/1.1/About-CMMN) (2016) and [DMN 1.5](https://www.omg.org/spec/DMN/1.5/About-DMN) (2024), object/event records in [OCEL 2.0](https://www.ocel-standard.org/), and traces in [OpenTelemetry 1.58.0](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.58.0/specification/overview.md) describe different objects. These named editions supply historical comparison examples; A.15 and A.15.1 govern the Work claims. | Distinguish a reusable composition account from records about its enactment. Recover the Methods and construction facts, then use the Work or evidence predicates for what happened. | A model or telemetry representation can support a claim without itself being the Method or establishing Method parts. |
| [Bosman et al., “A Calculus for Scoped Effects & Handlers”](https://arxiv.org/abs/2304.09697) (2024) separates syntax from handling semantics and provides explicit forwarding of scoped operations. [Matache et al., “Scoped Effects as Parameterized Algebraic Theories”](https://arxiv.org/abs/2402.03103) (2024) develops equational reasoning for scoped operations. | Use these software examples to examine scope, typed joins, forwarding and boundary behavior. Explain the preconditions, result meanings and failure routes of the proposed Method composition in its domain. | These calculi supply no general Method identity for manufacturing, clinical or organizational work. An FPF boundary change affects identity when it changes the reusable action or admissible boundary under A.3.1. |
| [Gogioso et al., “Constructor Theory as Process Theory”](https://arxiv.org/abs/2401.05364) (2023) connects abstract tasks to physical processes through a compositional formal treatment. A.3.1 develops the Method-side comparison. | Retain the distinction between a specified task and a process that realizes it when examining composition and enactment. | The formal bridge does not by itself identify an FPF Method part or dated Work; use their predicates. |
| [Borgo and Righetti, “Towards Applied Constructional Ontology”](https://journals.sagepub.com/doi/10.3233/FAIA250480) (2025) examines choices and difficulties in applying constructional approaches to foundational ontologies. A.1 develops the construction-sensitive comparison. | State constituents, construction facts and identity choices instead of treating a diagram or label as a constructed whole. | Method composition retains its predicate. Its order is not structural parthood, and the source's exploratory ontology comparison supplies no ready-made Method composition rule. |

