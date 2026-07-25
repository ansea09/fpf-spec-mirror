---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Architecture Scale-Amenability Preference"
section_id: "C.31.ASAP:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__008_conformance-checklist.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.31.ASAP — Architecture Scale-Amenability Preference"
  - "C.31.ASAP:7 — Conformance Checklist"
line_start: 62818
line_end: 62832
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18.1"
  - "C.19.1"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.31"
  - "C.31.RSA"
  - "C.32"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "RG"
  - "ScaleClaimTriage"
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "platform scale claim"
  - "scale amenability"
  - "scale variable"
  - "scale window"
  - "source-return condition"
  - "waiver reason"
---

### C.31.ASAP:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| `CC-C31.ASAP-1` | A C.31.ASAP use being made names architecture alternative set, scale variable or scale window, and claimed preference under scale. | Prevents generic "scales better" wording. |
| `CC-C31.ASAP-2` | `ScaleClaimTriage` names slope evidence, scale-probe evidence, or a no-probe reason. | Prevents preference claims without declared evidence or no-probe reason. |
| `CC-C31.ASAP-3` | Expected stable or improving structure and exception-growth risk are stated. | Keeps the pattern about architecture structure rather than scale vocabulary. |
| `CC-C31.ASAP-4` | Source-return condition is present when any compressed, coarse, extracted, indexed, or accounting representation drops source-side distinctions. | Prevents unsafe coarse descriptions. |
| `CC-C31.ASAP-5` | Waiver reason is one of deontic constraint, safety or law-domain boundary, scale-probe overturn, assurance infeasibility, or context-specific bounded exception. | Prevents false debt labels. |
| `CC-C31.ASAP-6` | `ArchitectureHeuristicDebt` remains report-only unless a decision, risk, work, evidence, assurance, or selected-set record is being used under its governing pattern. | Prevents shadow project authority. |
| `CC-C31.ASAP-7` | Platform, product-line, modularity, reuse, open-interface, RG, and coarse-graining labels do not establish scale preference by themselves. | Blocks source-label overread. |
| `CC-C31.ASAP-8` | Mathematical-lens claims name C.29 output fields; C.31.ASAP governs only the architecture scale-preference side. | Keeps C.29 and C.31.ASAP distinct. |
| `CC-C31.ASAP-9` | Comparison, selected-set, local choice, evidence, assurance, gate, work, or release claims name the governing pattern. | Prevents scale preference from becoming selection or assurance. |
| `CC-C31.ASAP-10` | SoTA rows mutate at least one solution line, checklist item, boundary, relation, or worked slice. | Keeps source use non-decorative. |

