---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:9"
section_title: "Worked Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__010_worked-examples.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:9 — Worked Examples"
line_start: 60528
line_end: 60546
dependencies:
  - "A.4"
  - "A.7"
  - "E.10.U1"
  - "E.10.U2"
  - "E.10.U4"
  - "E.10.U7"
  - "E.10.U9"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.9"
keywords:
  - "U.BoundedContext"
  - "anchor"
  - "context"
  - "domain"
  - "frame"
---

### E.10.D1:9 - Worked Examples

#### E.10.D1:9.1 Enactment — process vs activity (two context of meaning).

* Use `BPMN_2_0:process` and `PROV_O_2013:activity` as **SenseCell**s.
* In a Concept‑Set row, code the provisional relation `⋈` (overlap), not an equality.
* Role Descriptions later reference **the specific SenseCell**, not “an anchor”.

#### E.10.D1:9.2 Roles — behavioural mask vs access status.

* `BPMN_2_0:participant` vs `NIST_RBAC_2004:role`.
* Mark `⟂` (incompatible) in the Concept‑Set row to prevent conflation.
* Any cross‑use requires E.10.U9 with explicit loss policy.

#### E.10.D1:9.3 Services & evidence.

* `ITIL4_2020:service` / `ITIL4_2020:service‑level‑objective` with KD‑CAL cells `SOSA_SSN_2017:observation`.
* References in acceptance patterns point to **SenseCell**s; provenance stays within the PROV Context.

