---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack: Classify and Place Boundary Claims"
section_id: "A.6:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__011_rationale.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.6 — Signature Stack: Classify and Place Boundary Claims"
  - "A.6:10 — Rationale"
line_start: 14071
line_end: 14083
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.8.PER"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
keywords:
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "Work versus non-Work effect"
  - "acceptance"
  - "actual occurrence"
  - "and evidence"
  - "atomic L/A/D/E claims"
  - "delivery"
  - "in invariants"
  - "publication face"
  - "reference predicates by ID or canonical location from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:10 - Rationale

A boundary account can contain different claims, including:

* definitions and laws about operations or other mathematical objects;
* admissibility conditions for the selected operation;
* prescriptions, commitments or grants under their governing rules; and
* **actual occurrences and evidence** (effects may arise through Work, natural or spontaneous transformation, formal change, or another directly governed interaction, and evidence supports but does not create them).

Mixing these claims makes it harder to distinguish a semantic boundary change from an implementation change, and to test each claim against its own rule and evidence.

Reusable declarations constrain their realizations, while observations and evaluated results can expose a reason to revise those declarations. Keep the dependence and the reason for revision distinct. The classification follows what each claim says rather than its visible word, such as “must”, “guarantee”, “valid” or “allowed”.

