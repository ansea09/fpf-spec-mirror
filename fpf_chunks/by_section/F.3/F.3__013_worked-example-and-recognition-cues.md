---
chunk_kind: "child"
pattern_id: "F.3"
pattern_title: "Source-Local Sense Clustering"
section_id: "F.3:12"
section_title: "Worked example and recognition cues"
source_path: "FPF-Spec.md"
output_path: "by_section/F.3/F.3__013_worked-example-and-recognition-cues.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "F.3 — Source-Local Sense Clustering"
  - "F.3:12 — Worked example and recognition cues"
line_start: 103365
line_end: 103406
dependencies:
  - "A.11"
  - "A.7"
  - "E.10.D1"
  - "F.1"
  - "F.17"
  - "F.2"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "LocalSenseClaim"
  - "alias consolidation"
  - "counterexample"
  - "effective ReferenceScheme"
  - "optional SchemeSenseCell"
  - "source expression"
---

### F.3:12 - Worked example and recognition cues

Section 12.2 supplies one source-grounded clustering case. The other entries are recognition cues for possible clusters and boundaries; recover their exact editions, passages and interpretation bases before treating them as completed LocalSenseClaims.

#### F.3:12.1 - BPMN 2.0

**Process (workflow graph).** Claim: a graph of flow nodes and sequence flows that specifies orchestration among participants. Supporting expressions may include *process*, *process model*, and *business process* where the cited passages use them for the diagram. Counterexample: “this process took five minutes” describes an occurrence, not this design claim.

**Event (node).** Claim: a typed diagram node marking starts, ends, or intermediates. Counterexample: “the outage event happened at 13:05” describes an occurrence.

#### F.3:12.2 - PROV-O

**Receiving question.** Which of `prov:Activity`, `http://www.w3.org/ns/prov#Activity` and `prov:Agent` can share one local meaning?

**Source basis.** [W3C PROV-O Recommendation, 30 April 2013](https://www.w3.org/TR/2013/REC-prov-o-20130430/), §1.3 fixes the `prov` namespace; §3.1 states the class meanings; §4.1 gives the class IRIs. The effective scheme is that edition's PROV-O vocabulary.

**Activity.** Consolidate the prefixed name and its full IRI: both address the class whose Tech label is **activity (PROV-O)** and Plain label is **occurrence that acts on or with entities**. LocalSenseClaim: an occurrence over an interval that acts on or with entities. A sorting algorithm as a reusable way of doing is not thereby such an occurrence.

**Agent.** Keep a separate local meaning. Tech **agent (PROV-O)**; Plain **responsible participant**. LocalSenseClaim: something responsible for an activity, an entity's existence or another agent's activity. An RBAC permission role is not thereby a PROV agent.

The namespace expansion supports the alias consolidation; the temporal-occurrence and responsibility meanings remain separate. These two local claims answer the receiving question; an F.17 address is added only for a later recurring use.

#### F.3:12.3 - ITIL 4

**Service-level objective and SLO.** One claim may consolidate the full form and abbreviation when the cited edition uses them interchangeably: a target value or range for a service characteristic. Counterexample: an observed availability value is evidence, not the target.

**Incident.** Claim: an unplanned interruption or reduction in service quality. Counterexample: a plant sensor fault is not an ITIL incident unless another relation is separately established.

#### F.3:12.4 - SOSA/SSN

**Observation.** Claim: an act applying a procedure to a feature of interest to obtain a result. Counterexample: “20 °C” is a result value, not the observation act.

#### F.3:12.5 - OWL 2

**SubClassOf.** Claim: every instance of one class is an instance of another. Counterexample: `rdf:type` relates an individual to a class.

**EquivalentClasses.** Claim: two class expressions have the same instances under the OWL semantics. Counterexample: `owl:sameAs` is individual identity.

#### F.3:12.6 - IEC 61131-3

**Task.** Claim: a cyclic or event-driven runtime unit that invokes programs. Counterexample: a control algorithm or program description is not the task occurrence.

