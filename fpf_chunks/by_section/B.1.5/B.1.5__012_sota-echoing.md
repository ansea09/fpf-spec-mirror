---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__012_sota-echoing.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:11 — SoTA-Echoing"
line_start: 37565
line_end: 37577
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
  - "A.6.1"
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
  - "C.29"
  - "E.10"
  - "E.20"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.6"
  - "G.5"
  - "U.MethodDescription"
  - "U.PresentationCarrier"
  - "U.Signature"
  - "U.Structure"
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

These rows answer the B.1.5 practice question: how to decide and expose order-sensitive Method composition without mistaking descriptions, Work, event records, or construction diagrams for the composite Method.

| Current practice answer | Published source basis | B.1.5 adoption | Rejected shortcut |
| --- | --- | --- | --- |
| Current workflow, case, decision, process-mining, and object-centric event-log practice separates process models from event logs, telemetry, and resource records. | `A.15:11` — OMG CMMN 1.1 (2016) and OMG DMN 1.5 (2024); `A.15.1:13.1` — OCEL 2.0 Specification (2024) and OpenTelemetry Specification 1.58.0. | **Adopt and adapt.** Adopt the model, decision, occurrence, log, and telemetry separations; adapt them by requiring exact candidate and part Methods, `methodPartOf`, and separately grounded Work because a review must distinguish modeled composition from what happened. | **Reject.** A workflow notation, event log, trace, or telemetry span is neither the composite Method nor proof of Method parts or dated Work. |
| Typed functional, scoped-effect, protocol, and workflow-composition practice treats composition as constrained by interfaces, preconditions, intended results, handlers, scope, and admissible order. | `A.3.1:11` — Gogioso et al., “Constructor Theory as Process Theory” (2023); Bosman et al., “A Calculus for Scoped Effects & Handlers” (2024); Matache et al., “Scoped Effects as Parameterized Algebraic Theories” (2024). | **Adapt.** Use preconditions, intended-result meanings, scope, order, typed joins, adapters, and failure routes as concrete tests of the whole-forming claim because a composition label alone cannot show that one reusable whole action works. Use A.6.RCD's lightest sufficient disposition for each resulting claim. | **Reject.** A type signature, handler calculus, process-theory description, edge label, or source-material description alone does not identify a Method part, admit a relation kind, or ground dated Work. |
| Scoped software semantics makes operation declarations, handler scope, and boundary behavior explicit without supplying a general Method-identity rule. | `A.3.1:11` — Bosman et al., “A Calculus for Scoped Effects & Handlers” (2024), and Matache et al., “Scoped Effects as Parameterized Algebraic Theories” (2024), cited above. | **Adapt and delimit.** Use that boundary visibility to state exposed, forwarded, and encapsulated interactions. The rule that a boundary decision affects Method identity when it changes the reusable action or admissible boundary is an FPF decision; a named receiver triggers explicit statement or publication because callers and substituting-method uses need a stable boundary account. | **Reject.** Handler syntax, planner Work, publication layout, carrier choice, or diagram position does not decide whether an interaction is exposed, forwarded, or encapsulated. |
| Current constructional-ontology practice requires explicit constituents, constructive relations, dependence, and identity choices rather than inferring a whole from a diagram or label. | `A.1:11` — Florio and Linnebo, *Introduction to Constructional Ontology* (2024), and Borgo and Righetti, “Towards Applied Constructional Ontology” (2025). | **Adapt.** Require exact part Methods, obtaining `methodPartOf` occurrences, other whole-forming claims at their A.6.RCD dispositions, a reusable whole action, and a reidentification rule because constituent names alone do not construct a Method whole. | **Reject.** Method-composition order is not A.14 structural parthood, and neither a C.13 notation nor one shared label creates the Method or a relation kind. |

**Currentness and reopen.** These four decisions are qualified by the exact source selections cited above. Reopen only the affected row when a cited source or edition is superseded, or when newer practice changes the relied-on model/occurrence separation, order or join condition, interface or substitution boundary, or construction and reidentification test. Recheck that row's B.1.5 adoption, refusal, and affected Solution, worked-case, checklist, and Relations loci; leave unaffected rows closed.

