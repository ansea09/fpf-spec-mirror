---
chunk_kind: "child"
pattern_id: "F.2"
pattern_title: "Source-Local Term Harvesting & Normalisation"
section_id: "F.2:11"
section_title: "Further recognition cues"
source_path: "FPF-Spec.md"
output_path: "by_section/F.2/F.2__012_further-recognition-cues.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "F.2 — Source-Local Term Harvesting & Normalisation"
  - "F.2:11 — Further recognition cues"
line_start: 103130
line_end: 103154
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

Use the completed PROV-O note as one source-backed input. The BPMN, SOSA/SSN and ITIL cues still need their exact source bases before they can be used as lexical notes. After that recovery, a writer can ask how an SOSA observation result relates to an ITIL service target; the list itself establishes no sameness between BPMN *process* and PROV *activity*.

#### F.2:11.2 - Control and services

* **State-space control source, cited passage and scheme** — `actuation`; Plain **control output**; claim: “A signal applied to influence plant state or output.”
* **IEC 61131-3, cited runtime passage and scheme** — `task`; Plain **scheduled program execution**; claim as above.
* **ITIL 4 (2020), incident-management use** — `incident`; Plain **reported service disruption**; claim: “An unplanned interruption or reduction in service quality.”

This prevents a plant fault from becoming an ITIL incident merely because a writer wants one word for both.

#### F.2:11.3 - Kind, method, and knowledge sources

* **OWL 2 profile source** — `subClassOf`; Plain **class inclusion**; claim: “Every instance of the first class is an instance of the second.”
* **FCA source** — `formal concept`; Plain **extent–intent pair**; claim: “A maximal object–attribute pair under the stated Galois connection.”
* **SPEM 2.0 and ISO 24744 sources** — `method`; Plain **way of doing**; claim recovered from the cited method passage.
* **SOSA/SSN (2017)** — `procedure`; Plain **observation recipe**; claim: “A description of how an observation may be carried out.”

The notes do not turn an FCA concept into a root kind or a procedure description into a Method. Those are separate claims under their direct patterns.

