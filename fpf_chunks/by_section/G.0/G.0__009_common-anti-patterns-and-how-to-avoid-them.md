---
chunk_kind: "child"
pattern_id: "G.0"
pattern_title: "Frame Standard and Comparability Governance — CG‑Spec"
section_id: "G.0:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.0/G.0__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "G.0 — Frame Standard and Comparability Governance — CG‑Spec"
  - "G.0:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 68167
line_end: 68173
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
  - "edition pins"
  - "legality gate"
  - "Γ-fold"
  - "Φ(CL)"
  - "Φ_plane"
---

### G.0:8 - Common Anti-Patterns and How to Avoid Them

* **Anti-pattern: shadow legality gates in downstream code.** Avoid by requiring downstream to cite `CG‑Spec` segments by id+edition.
* **Anti-pattern: “one number to rule them all”.** Avoid by preserving set-return outputs when only partial orders are lawful; any scalarisation must be explicit, typed, and justified.
* **Anti-pattern: thresholds inside CG‑Spec or CHR.** Avoid by keeping thresholds and acceptance logic in CAL and citing from `CG‑Spec` only via stubs/templates.
* **Anti-pattern: implicit crossings.** Avoid by requiring explicit bridge ids, CL/policy ids, and reference-plane pins.

