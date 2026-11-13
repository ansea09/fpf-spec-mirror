---
chunk_kind: "child"
pattern_id: "F.2"
pattern_title: "Source-Local Term Harvesting & Normalisation"
section_id: "F.2:11"
section_title: "Further recognition cues"
source_path: "FPF-Spec.md"
output_path: "by_section/F.2/F.2__012_further-recognition-cues.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "F.2 — Source-Local Term Harvesting & Normalisation"
  - "F.2:11 — Further recognition cues"
line_start: 126768
line_end: 126792
dependencies:
  - "A.11"
  - "A.7"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.3"
  - "F.4"
  - "F.9"
keywords:
  - "LNF"
  - "LocalExpression"
  - "LocalSenseClaim"
  - "effective ReferenceScheme"
  - "exact source and edition"
  - "optional SchemeSenseCell"
---

### F.2:11 - Further recognition cues

The entries in this section are possible readings to inspect, not completed lexical notes. Recover each exact source basis before relying on the proposed gloss.

#### F.2:11.1 - Enactment and sensing

Use the completed PROV-O note as one source-backed input. The BPMN, SOSA/SSN and ITIL cues still need their exact source bases before they can be used as lexical notes. After that recovery, a writer can ask how an SOSA observation result relates to an ITIL service target; listing the expressions together does not establish sameness between BPMN *process* and PROV *activity*.

#### F.2:11.2 - Control and services

* **State-space control source, cited passage and scheme** — `actuation`; Plain **control output**; claim: “A signal applied to influence plant state or output.”
* **IEC 61131-3, cited runtime passage and scheme** — `task`; Plain **scheduled program execution**; claim as above.
* **ITIL 4 (2020), incident-management use** — `incident`; Plain **reported service disruption**; claim: “An unplanned interruption or reduction in service quality.”

Use the source's service-disruption criteria to decide whether a reported plant fault also qualifies as an ITIL incident.

#### F.2:11.3 - Kind, method, and knowledge sources

* **OWL 2 profile source** — `subClassOf`; Plain **class inclusion**; claim: “Every instance of the first class is an instance of the second.”
* **FCA source** — `formal concept`; Plain **extent–intent pair**; claim: “A maximal object–attribute pair under the stated Galois connection.”
* **SPEM 2.0 and ISO 24744 sources** — `method`; Plain **way of doing**; claim recovered from the cited method passage.
* **SOSA/SSN (2017)** — `procedure`; Plain **observation recipe**; claim: “A description of how an observation may be carried out.”

Classifying an FCA concept as a root kind or identifying a Method from a procedure description requires a separate claim under the relevant pattern. Once recovered, the source meanings can inform those judgements.

