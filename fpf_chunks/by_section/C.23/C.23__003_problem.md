---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__003_problem.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:2 — Problem"
line_start: 53174
line_end: 53183
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
  - "admit"
  - "degrade"
  - "evidence"
  - "maturity"
  - "selector"
---

### C.23:2 - Problem

Unstructured “readiness” stories and undisciplined evidence lead to:

* (i) **Illicit scalarisation** across mixed scale types,
* (ii) **Prose‑only** gating that a dispatcher cannot execute,
* (iii) reuse after the family, evidence profile, claim scope, qualification window, or comparison basis changed, or reliance on an unstated source-local, kind, or plane relation, and
* (iv) Immature families leaking into production.
  We need a **notation‑independent LOG layer** that turns **TaskSignature (S2)** + **EvidenceProfiles** into **executable rules** for *admit / degrade / abstain*, **routing any CL penalties to `R_eff` only** (never mutating **F/G**).

