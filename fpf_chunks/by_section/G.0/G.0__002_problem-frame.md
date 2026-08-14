---
chunk_kind: "child"
pattern_id: "G.0"
pattern_title: "Frame Standard and Comparability Governance — CG‑Spec"
section_id: "G.0:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.0/G.0__002_problem-frame.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "G.0 — Frame Standard and Comparability Governance — CG‑Spec"
  - "G.0:1 — Problem frame"
line_start: 99314
line_end: 99326
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.5"
  - "E.5.2"
  - "F.9"
  - "G.1"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "CG-Frame"
  - "CG-Spec"
  - "CL-routing"
  - "ComparatorSet"
  - "MinimalEvidence"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "ScaleComplianceProfile (SCP)"
  - "admissibility gate"
  - "edition pins"
  - "Γ-fold"
  - "Φ(CL)"
  - "Φ_plane"
---

### G.0:1 - Problem frame

A team defines or evolves a `CG‑Frame` (e.g., a frame for creativity measurement, decision quality, architecture trade‑offs, or selected-set publication). Downstream mechanisms (G.1–G.5 and beyond) must compare, aggregate, and publish CHR‑typed observations in ways that are:

* lawful with respect to measurement admissibility (scale/unit/polarity constraints),
* auditable with explicit evidence minima and provenance,
* reproducible via pinned editions and explicit policy ids,
* portable only via explicit crossings (bridges and reference-plane moves), never via implicit semantic leakage.

`CG‑Spec` is the single design-time object that fixes *what comparisons and aggregations are lawful in this frame*, under which pinned assumptions and minimal evidence requirements, so that run-time selection and publication can be audited without inventing new “local legality gates”.

Didactic subtitle: **Design-time rules for safe, auditable comparison.**

