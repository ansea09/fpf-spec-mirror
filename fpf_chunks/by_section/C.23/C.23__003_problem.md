---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__003_problem.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:2 — Problem"
line_start: 67123
line_end: 67133
dependencies:
  - "A.10"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "E.10"
  - "E.18"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
keywords:
  - "MethodFamily"
  - "SoS-LOG"
  - "abstain"
  - "admission rules"
  - "admit"
  - "degrade"
  - "evidence"
  - "maturity"
  - "selector"
---

### C.23:2 - Problem

Unstructured “readiness” stories and undisciplined evidence lead to:

* (i) **Illicit scalarisation** across mixed scale types,
* (ii) ambiguous gating conditions that a dispatcher cannot apply,
* (iii) reuse after the family, evidence profile, claim scope, qualification window, or comparison basis changed, or reliance on an unstated source-local, kind, or plane relation, and
* (iv) Immature families entering production.

We need a **notation‑independent LOG layer** whose **executable rules** use **TaskSignature (S2)** + **EvidenceProfiles** to return *admit / degrade / abstain*, retaining relation losses and any justified assurance consequences under R4.

