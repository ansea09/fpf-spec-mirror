---
chunk_kind: "child"
pattern_id: "F.3"
pattern_title: "Source-Local Sense Clustering"
section_id: "F.3:12"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.3/F.3__013_worked-examples.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "F.3 — Source-Local Sense Clustering"
  - "F.3:12 — Worked examples"
line_start: 91705
line_end: 91738
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

### F.3:12 - Worked examples

#### F.3:12.1 - BPMN 2.0

**Process (workflow graph).** Claim: a graph of flow nodes and sequence flows that specifies orchestration among participants. Supporting expressions may include *process*, *process model*, and *business process* where the cited passages use them for the diagram. Counterexample: “this process took five minutes” describes an occurrence, not this design claim.

**Event (node).** Claim: a typed diagram node marking starts, ends, or intermediates. Counterexample: “the outage event happened at 13:05” describes an occurrence.

#### F.3:12.2 - PROV-O

**Activity.** Claim: a time-bounded occurrence that uses or generates entities and may be associated with agents. Counterexample: a sorting algorithm as a reusable way of doing is not an occurrence.

**Agent.** Claim: an entity that bears responsibility for an activity’s effects under the PROV scheme. Counterexample: an RBAC permission role is not thereby a PROV agent.

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

