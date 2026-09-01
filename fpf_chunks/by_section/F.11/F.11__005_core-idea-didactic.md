---
chunk_kind: "child"
pattern_id: "F.11"
pattern_title: "Method Quartet Harmonisation"
section_id: "F.11:4"
section_title: "Core idea (didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.11/F.11__005_core-idea-didactic.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "F.11 — Method Quartet Harmonisation"
  - "F.11:4 — Core idea (didactic)"
line_start: 96338
line_end: 96350
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "B.1.5"
  - "C.2.1"
  - "E.10.D1"
  - "F.0.1"
  - "F.10"
  - "F.17"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Work"
keywords:
  - "Method"
  - "MethodDescription"
  - "control or transformation output"
  - "dated Work"
  - "description use"
  - "enactment"
  - "performed-Work attribution"
---

### F.11:4 - Core idea (didactic)

Use four questions, then state only the relations that actually obtain:

* **Method — the way.** An algorithm, test method, clinical pathway, or welding technique is a way of doing under A.3 and A.3.1.
* **MethodDescription — the description episteme.** An SOP, program text, BPMN or SPEM model, or other episteme is a `U.MethodDescription` only when A.3.2 finds one admitted Method as its exact `EntityOfConcern` and at least one substantive claim about that Method as a way of doing.
* **Work — the occurrence.** A dated performance, run, batch, or service episode is `U.Work` under A.15 and A.15.1. Work is the occurrence itself, not a record of the occurrence; a record or report is a separate episteme or carrier.
* **Control or transformation output — if present.** A setpoint, command, duty-cycle value, signal, or changed output is identified under its direct pattern and related to the Work only when that relation obtains.

F.11 allows the plain sentence “this MethodDescription describes the Method” as shorthand for that A.3.2 constitution and membership judgement. It does not add a binary description relation. Several epistemes may each have the same Method as their exact `EntityOfConcern`; one episteme may concern one admitted composite Method; and one document or publication may present several separately identified epistemes. One MethodDescription episteme cannot have several Methods as its `EntityOfConcern`.

Work may enact a Method when the exact enactment relation and evidence are stated. A System may perform Work under an obtaining system-role assignment when A.15.1 and F.6 support that attribution. A claim that a System or Work used, followed, deviated from, conformed to, or relied on a particular MethodDescription edition is separate. Cite the pattern that defines or tests that claim; use A.10 or B.3 for evidence reliance, and return A.6.RCD `missing-governor` when no current pattern supplies the needed relation after its participants and sentence are explicit.

