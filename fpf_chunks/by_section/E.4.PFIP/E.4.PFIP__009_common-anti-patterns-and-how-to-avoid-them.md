---
chunk_kind: "child"
pattern_id: "E.4.PFIP"
pattern_title: "Principle-Framework Publication Integration and Preservation"
section_id: "E.4.PFIP:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFIP/E.4.PFIP__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "E.4.PFIP — Principle-Framework Publication Integration and Preservation"
  - "E.4.PFIP:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 69702
line_end: 69715
dependencies:
  - "C.2.1"
  - "C.33"
  - "C.34"
  - "E.11"
  - "E.17"
  - "E.24.PUB"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFIP"
  - "E.8"
keywords:
---

### E.4.PFIP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Source parity proves preservation | Accepted additions are present, but unrelated predecessor content may be gone. | Run the predecessor-to-candidate comparison independently. |
| Green build proves preservation | Syntax and assembly succeed while meaning or selected structure disappears. | Select the form-appropriate inventory and inspect semantic outcomes. |
| Same use means same form | Two different forms serving orientation are paired as versions. | Require retained form identity or an accepted one-to-one continuity decision. |
| Text diff for every form | Diagram relations, card fields, or retrieval cues have no meaningful shared spans. | Use the FPF pattern that defines or constrains the form, `C.33`, or `C.34` to select content or structure. |
| Retired form, retired content | A split or merge decision silently authorizes every old omission. | Run the allocation comparison over the complete predecessor inventory. |
| Collective-publication shortcut | Several forms or carriers are renamed as one bundle so one comparison seems sufficient. | Keep named expressions separate and use them as inputs to the allocation comparison. |
| Carrier continuity as content continuity | An unchanged file or address is treated as proof that the selected edition and expression still obtain. | Apply `E.24.PUB` and compare the selected expression, not the storage proxy. |
| Positive preservation ledger | Every unchanged sentence or field receives a report row. | Keep completeness checkable and report losses, accepted differences, unexpected additions, blockers, and unresolved correspondences or content-change questions. |
| Fabricated predecessor | A first publication is forced through a predecessor comparison. | Use accepted-source incorporation, complete candidate inventory, and package evaluation only. |

