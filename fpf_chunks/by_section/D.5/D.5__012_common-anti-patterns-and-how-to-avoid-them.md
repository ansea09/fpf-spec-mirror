---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:3.3"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:3.3 — Common Anti-Patterns and How to Avoid Them"
line_start: 63064
line_end: 63071
dependencies:
  - "A.10"
  - "B.3"
  - "C.16"
  - "C.28"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "E.13"
  - "E.17"
  - "E.5.4"
keywords:
---

### D.5:3.3 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Ethics ghetto | Bias or fairness is left in a separate ethics note while the model, metric, release, publication, or work plan keeps operating unchanged. | Put the concern on the audited EntityOfConcern and its intended use, then name the mitigation, constraint, or accepted residual. |
| Checklist charade | A checklist is completed without naming affected people or groups, evidence, current use, or residuals. | Use `BiasRegister@Context` for a light scan or `BiasAuditReport@Context` for deeper review; do not treat a blank checklist as assurance. |
| Bias whack-a-mole | One disparity is patched while proxy, representation, metric, visibility, or language concerns move elsewhere. | Keep REP, ALG, VIS, MET, and LNG concerns visible until the admissible use and accepted residual are explicit. |

