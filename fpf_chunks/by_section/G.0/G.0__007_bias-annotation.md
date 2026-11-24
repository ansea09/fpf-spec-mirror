---
chunk_kind: "child"
pattern_id: "G.0"
pattern_title: "Define Admissible Comparison and Aggregation for a Frame (CG-Spec)"
section_id: "G.0:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/G.0/G.0__007_bias-annotation.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "G.0 — Define Admissible Comparison and Aggregation for a Frame (CG-Spec)"
  - "G.0:6 — Bias-Annotation"
line_start: 136529
line_end: 136537
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CN"
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
  - "admissible comparison and aggregation"
  - "edition pins"
  - "evidence requirements"
  - "Γ-fold"
  - "Φ(CL)"
  - "Φ_plane"
---

### G.0:6 - Bias-Annotation

`CG‑Spec` can encode (and therefore amplify) biases if authored carelessly:

* **Tradition favoritism.** Comparator choices may privilege a tradition’s evidence style; mitigation: declare evidence minima and any justified crossing loss, and require grounds for cross-tradition aggregation.
* **Metric gaming and Goodhart effects.** A single score can conceal trade-offs. Preserve the comparator’s declared relations and the selector’s actual outcome. State the authority and basis for a scalar ranking used in a decision.
* **Hidden thresholds and opaque safety policy.** Embedding acceptance thresholds in prose or code hides value judgments; mitigation: keep thresholds in CAL acceptance clauses and pin policy ids.
* **Scope creep.** A comparison may be reused for a different entityOfConcern or reference plane. Retain `entityOfConcern` and `ReferencePlane` pins, and apply the governing rule for any plane relation the comparison uses. Include E.18/A.21 crossing or gate pins when that use applies.

