---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:9"
section_title: "Micro‑examples (didactic, multi‑domain)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__010_micro-examples-didactic-multi-domain.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:9 — Micro‑examples (didactic, multi‑domain)"
line_start: 74067
line_end: 74098
dependencies:
  - "A.2.3"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
  - "U.PromiseContent"
keywords:
  - "Service Level Agreement (SLA)"
  - "Service Level Objective (SLO)"
  - "acceptance criteria"
  - "binding"
  - "observation"
---

### F.12:9 - Micro‑examples (didactic, multi‑domain)

#### F.12:9.1 - SaaS uptime (services + sensing)

* **Contexts:** *ITIL 4* (Clause), *PROV‑O* (Work), *SOSA/SSN* (Measure).
* **ClauseCell:** *availability ≥ 99.9% monthly*.
* **WorkCell:** *service delivery work* Activities during June.
* **MeasureCell:** *uptime observation* from synthetic probes.
* **Predicate:** share‑of‑time ≥ 0.999.
* **Bridge:** probe result → user availability (**kind:** proxy; **CL:** 2; **Loss:** regional gaps).
* **Verdict:** *Satisfied (June)* if the ratio holds; **attaches to Clause\@June about those Works**.

#### F.12:9.2 - Furnace band (industrial control)

* **Contexts:** *quality/deontics canon* (Clause), *IEC 61131‑3/PROV* (Work), *KD‑CAL* (Measure).
* **ClauseCell:** *product temperature within \[720,740] °C during soak*.
* **WorkCell:** *soak phase* Work interval.
* **MeasureCell:** thermocouple Observations (KD‑CAL).
* **Predicate:** band conformance.
* **Bridge:** IEC task interval → PROV Activity (**Interpretation**, CL=2).
* **Verdict:** *Violated* if any measured value exits the band.

#### F.12:9.3 - Incident MTTR (services + enactment)

* **Contexts:** *ITIL 4* (Clause), *PROV‑O* (Work).
* **ClauseCell:** *MTTR ≤ 60 min per incident*.
* **WorkCell:** each incident’s handling Activity.
* **MeasureCell:** timestamps (Observed facts) of start‑fix and restore events.
* **Predicate:** duration ≤ 60 min.
* **Bridge:** BPMN steps → PROV Activity (**Interpretation**, CL=2).
* **Verdict:** *Satisfied* if the measured interval meets the target.

