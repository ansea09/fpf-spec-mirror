---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 69589
line_end: 69597
dependencies:
  - "C.32.ADR"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| ADR as decision | A publication projection is treated as the decision relation. | Fill `PrincipleFrameworkArchitectureDecision@Context`, then project it through `C.32.ADR` if useful. |
| Template-led selection | Headings decide what evidence is gathered. | Start from the architecture question, source basis, alternatives, selected structures, and consequences. |
| PFAD overgrowth | The pattern repeats generic decision practice. | Demote to `E.9` plus `C.32.PAD` and keep only a relation row if no framework-specific slot is active. |
| Hidden Core change | A domain or local decision silently changes FPF Core meaning. | Record framework family and dependency direction under `E.4` and `E.5.3`. |

