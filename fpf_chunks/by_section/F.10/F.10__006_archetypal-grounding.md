---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__006_archetypal-grounding.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:5 — Archetypal Grounding"
line_start: 80975
line_end: 80994
dependencies:
  - "A.2.4"
  - "B.3"
  - "F.1"
  - "F.18"
  - "F.3"
  - "F.9"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:5 - Archetypal Grounding

#### F.10:5.1 - Service Acceptance from Run-Time Evidence

A service dashboard reports uptime for July. In the monitoring context, the measurement episteme gives `EvidenceStatus = Measured` for the claim "uptime was 99.95 percent in July." In the service-management context, the SLO clause has `RequirementStatus = Satisfied` only if the service pattern's evaluation rule says that the measured uptime meets the clause.

F.10 records two status-use statements and an interpretation bridge. It does not infer requirement satisfaction from the word "measured" alone.

#### F.10:5.2 - Approved Method Description

A safety controller method description is `StandardStatus = Approved` in one standard profile and edition. That approval makes the method description admissible under that profile. It does not prove that a particular controller run met response-time obligations. A run-time log can be assigned `EvidenceStatus = Corroborated` for a response-time claim; a separate requirement-use statement can then evaluate the duty clause.

#### F.10:5.3 - Model Card and Fairness Requirement

A model card says a model is "validated" because cross-validation AUC is high. In F.10 this becomes an `EvidenceStatus` statement for a predictive-performance claim inside the validation context. It does not decide the policy requirement "demographic parity delta <= 0.1" unless production-window fairness evidence and the policy evaluation rule are present.

#### F.10:5.4 - Status Display Cue

A release dashboard cell shows `Ready`. The cell is a cue. A status-use statement is available only when the source, target, value, scope, window, and provenance constraint are recoverable. If the status is consumed for a gate, release, assurance, or admission use, the direct governing pattern for that use must also admit it.

