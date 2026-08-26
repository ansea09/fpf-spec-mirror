---
chunk_kind: "child"
pattern_id: "F.11"
pattern_title: "Method Quartet Harmonisation"
section_id: "F.11:11"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.11/F.11__012_worked-examples.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "F.11 — Method Quartet Harmonisation"
  - "F.11:11 — Worked examples"
line_start: 94357
line_end: 94387
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

### F.11:11 - Worked examples

#### F.11:11.1 - ML service rollout

* **Method:** canary deployment strategy.
* **MethodDescription:** the versioned canary plan with traffic slices and rollback rules.
* **Work:** two dated canary deployment occurrences.
* **Outputs:** traffic-shifting commands, if material to the claim.
* **Agency:** name the deploying System, its exact local system-role kind and assignment, and performed-Work attribution only if responsibility is part of the example.
* **Evidence:** latency and error-rate observations about the Work; the plan’s approval is separate.

The example does not infer SLO satisfaction from the plan. F.12 evaluates the promise from Work outcomes in the stated window.

#### F.11:11.2 - Industrial furnace control

* **Method:** PID with feed-forward.
* **MethodDescription:** controller tuning sheet and program description.
* **Work:** the actual PLC task cycles in the stated interval.
* **Outputs:** setpoints and valve-duty values produced during those cycles.
* **Evidence:** temperature observations and their scale and unit basis.

If the IEC task expression and a PROV Activity expression are related for reporting, state that exact F.9 relation and loss. It does not create the Work-to-output or evidence relations.

#### F.11:11.3 - Clinical assay

The Method is ELISA; the MethodDescription is kit IFU v7; the Work is batch B217; robot commands are optional output detail; absorbance observations support the quality verdict. Any deviation from the IFU is an explicit description-use or conformance claim, not a property inferred from the four-question layout.

#### F.11:11.4 - Incident response

The Method is triage-first incident handling; the MethodDescription is the playbook and diagram; the Work is the handling of INC-3421 from 09:10 to 10:02. MTTR is computed from observations of that Work. Command invocations are included only if a direct control or transformation claim needs them.

