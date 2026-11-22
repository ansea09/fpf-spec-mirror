---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:5"
section_title: "Aggregation Rules"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__008_aggregation-rules.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:5 — Aggregation Rules"
line_start: 45094
line_end: 45127
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.29"
  - "E.17"
  - "G.11"
  - "G.6"
keywords:
---

### B.1.6:5 - Aggregation Rules

**Typed resource basis.** Aggregate only values whose resource Characteristic, Scale, applicable Unit, subject and accounting boundary are compatible under the operative rule. Joules, hours, kilograms, currency, bytes and attention do not become one scalar by co-location.

**Measurement before aggregation.** Each measured input points to C.16 measurement work and one measurement-result episteme. Raw meter output, indication, resource stock, attributed value, aggregation input, and later efficiency verdict remain distinct.

**Included accounting subjects.** Establish which subjects the account covers, individually or through a rule that covers the whole requested scope. Identify an individual Work occurrence or phase when its resource use, identity or part relation is used in the inference or requested as a result. Parent–child, `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work` and other admitted Work-part relations must already obtain between independently admitted Work participants under A.15.1 or their subject patterns. A non-Work phase keeps its carrier's identity and `PhaseOf` grounds. For temporal overlap, recover the participants, temporal reference and interval facts under C.27.TA; establish resource-use or stock overlap under its accounting rule. A Method, plan, epoch or phase label, invoice period or dashboard grouping does not establish these subjects or relations.

**Operative policy.** State inclusion and output kind, and the conversion, normalization, weighting, missing-value, boundary-allocation, uncertainty and overlap/deduplication rules needed to interpret or justify the result. Identify the edition when the result or use depends on it. A policy declaration remains distinct from its application and result.

**Overlap and shared stocks.** For an exact total, establish disjoint contributions or justify how any overlap is handled. For a bound, establish the direction in which overlap can affect the requested quantity. For example, the sum of the hours in two complete groups is an upper bound on the hours in their union if repeated contributions have nonnegative values and are measured on the same basis. That bound can settle a ceiling without identifying every shared contribution. For allocation among works, use the assignment rule for the resources in question. Reuse of one person, tool or meter across distinct resource contributions does not by itself duplicate those contributions.

**Aggregation result and any asserted Work.** For a requested application, return the typed total, vector, interval or bounded estimate warranted by the input values, included subjects and rule, with its qualifications. A design for a class of jobs identifies how to select those inputs in each permitted case and why the rule will answer the receiving question. An ordinary statement or table can convey that result. When a claim-bearing result episteme is needed, identify it through C.2.1 as in §2, retaining the distinction between resource value, claim content and expression.

When a dated aggregation occurrence is asserted or required, use A.13 to identify the performer and A.15.1 to admit that Work independently. Add F.6 when assignment-bound attribution is needed. The Method, bindings, resources and time retain their separate grounds.

**Uncertainty and provenance.** Propagate measurement, model and conversion uncertainty under the operative rule where it affects the result or use. Keep the necessary sources and derivations recoverable. Use A.10 for needed replayable source-to-use reliance and G.6 for a needed stable address of that chain, preserving any Work, measurement, policy-application and transformation facts the use requires.

**Estimates, plans and performed use.** An estimated or derived resource value retains its source values, model and conditions; a planned amount retains its planning basis. The same value may serve both uses. Keep resource readiness under A.15.5. Use A.15.1 and the measurement or aggregation predicates for performed Work and measured results.

**Efficiency and yield.** A ratio or yield claim names its input resource results, output or domain result, attribution bases and applicable comparison rule. Any asserted dated aggregation Work retains its independent grounds. Explain a claimed gain through the measurement, accounting and domain-result grounds on which it depends; use B.2 when whole identity remains the question.

#### B.1.6:5.1 - Aggregation obligations

| Obligation | What must be named |
| --- | --- |
| Resource input | Characteristic, Scale, applicable Unit, subject, time basis, attribution grounds and uncertainty relevant to the use. A claimed performed measurement retains its C.16 Work/result; an estimate or derived value retains its sources, model and conditions. |
| Included subjects | Grounded coverage of the accounting subjects, and the identity of every individual occurrence whose attribution the conclusion uses or supplies; every Work-part, temporal-overlap, resource-use or stock relation used by this aggregation; and the identity and `PhaseOf` grounds for any included non-Work carrier phase. |
| Policy | Inclusion and output kind; every conversion, weighting, missing-value, allocation, uncertainty or overlap rule needed for the result or use; and an edition when either depends on it. |
| Dated aggregation Work, when asserted or required | Performer identified through A.13; dated `U.Work` independently admitted through A.15.1; a separate F.6 check when assignment-bound attribution is needed; separate Method, resources and direct/A.6.1 bindings. |
| Aggregation result | For an application, the typed result, included subjects, rule, boundary, time basis and qualifications. For a design, the input selection and rule that will supply the required output under the stated conditions. When the receiving claim or use needs a result episteme, identify it through C.2.1 as in §2. |
| Source basis and currentness | Recoverable sources and derivations; A.10 when source-to-use reliance must be replayable, G.6 when that chain needs a stable address, and G.11 when currentness affects use. |
| Later use | The receiving claim, action or judgement and any premise, reference, argument or decision-use relation it requires. |

