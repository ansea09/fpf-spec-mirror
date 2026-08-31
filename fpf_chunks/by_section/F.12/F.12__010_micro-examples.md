---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:9"
section_title: "Micro-examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__010_micro-examples.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:9 — Micro-examples"
line_start: 96334
line_end: 96351
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.RCD"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.2"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.9"
  - "U.PromiseContent"
keywords:
  - "EvidenceStatus"
  - "PromiseContent"
  - "RequirementStatus"
  - "declared result scale"
  - "delivery Work"
  - "evaluation Work"
  - "indicator recovery"
  - "measured value"
  - "observation"
  - "operation result binding"
---

### F.12:9 - Micro-examples

#### F.12:9.1 - SaaS uptime

* **Promise content:** availability ≥ 99.9% for the named service scope in June.
* **Delivery Work population:** the in-scope service-delivery occurrences during June, connected to the promise through the applicable A.2.3 relations.
* **Evidence:** synthetic-probe observations, with regions and outage-detection coverage stated. If their measurement model directly concerns the promised availability characteristic, no proxy is added; otherwise the distinct probe-to-user indicator relation needs a defining or testing pattern.
* **Evaluation:** a System performs evaluation Work; the exact application binds observed good time and total in-scope time and returns a value on the declared result scale.
* **Status or summary:** map the result to `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only when that F.10 rule applies. If the evidence basis is inadequate, use `EvidenceStatus=Inconclusive` and `RequirementStatus=Pending`, or the exact locally declared result. Plainly: met, not met, or cannot judge.

#### F.12:9.2 - Furnace temperature band

The promise content states `[720,740] °C` during the soak phase. The delivery Work is the actual batch soak occurrence. Calibrated thermocouple observations either measure the product characteristic directly or use a separately defined sensor-location indicator relation. Evaluation Work applies the band rule and binds its result. An out-of-band result can support `RequirementStatus=Violated`; insufficient spatial evidence supports `EvidenceStatus=Inconclusive` and leaves the requirement pending unless the declared acceptance scale specifies another local result.

#### F.12:9.3 - Incident MTTR

The promise content states restoration within 60 minutes per in-scope incident. Each incident-handling Work has observed start and restoration events. A separate evaluation Work occurrence applies the declared event and subtraction rule; its application binds those timestamps and returns the result. A playbook may be the selected evaluation MethodDescription when its edition changes that rule, but it is not the Work or proof of the duration.

