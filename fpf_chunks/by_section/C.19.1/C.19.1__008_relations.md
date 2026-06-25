---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:7"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__008_relations.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:7 — Relations"
line_start: 45806
line_end: 45819
dependencies:
  - "A.0"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "E.23"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "BLP‑waiver"
  - "Scale‑Audit"
  - "general‑method preference"
  - "iso‑scale parity"
  - "scale‑amenability"
  - "slope vector"
  - "α/δ tolerances"
---

### C.19.1:7 - Relations

**Depends on:** **G.5/G.9** (selector/parity), **G.11** (refresh telemetry), **C.5** (Resrc‑CAL), **C.18** (NQD‑CAL), **C.19** (E/E‑LOG), **F.7/F.9** (Bridges, CL/Φ/Ψ). **Constrained by:** **E.5** Guard‑Rails and **E.3** precedence.

#### C.19.1:7.1 - C.29 mathematical-lens use relation

When a mathematical lens is chosen over a general, scale-amenable method because it is elegant, specialized, or theoretically prestigious, `C.19.1` governs the scale-advantage and method-preference claim. A `C.29` application may state `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensUseAdmissibilityValue`, `admissibleUse`, `nonAdmissibleUse`, and `StopCondition`; it does not supply BLP compatibility, scale dominance, or waiver evidence.

If scale advantage is live, cite a `Scale-Audit` or `BLP-waiver`. If scale advantage is not live, keep the mathematical lens local and bounded by its `C.29` stop condition.

> *Memory hook.* **Prefer what scales; explain when you don’t.**

When `E.23` selects between a Ralph-like general adaptive loop, a specialized object-family cycle, or a mixed operation-family set, `C.19.1` governs the BLP comparison and waiver discipline. The local `E.23` cost and risk prompt `token_or_compute_cost + tool_cost + adaptation_attempt_cost + human_supervision_cost + rework_cost - avoided_loss_value` is not a scalar quality score; it is a practical accepted-work cost account for deciding whether the next pass, added operation, or method-family switch is BLP-compatible. Repeated automation alone does not satisfy BLP; the record must still name the object under improvement, object-under-improvement evaluation, protected trade-offs, bounded cost and risk posture, and stop or switch condition.

