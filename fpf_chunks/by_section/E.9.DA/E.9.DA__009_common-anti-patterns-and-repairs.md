---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:8"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__009_common-anti-patterns-and-repairs.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:8 — Common anti-patterns and repairs"
line_start: 57748
line_end: 57758
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
keywords:
---

### E.9.DA:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Heading-complete DRR.** Headings exist but authors cannot tell what to write. | Lower selected-answer, receiving-locus, and drafting-action coordinates. |
| **Source packet in DRR clothing.** Sources are preserved but FPF decisions are absent. | State selected payload, rejected payload, and receiving obligations. |
| **Address completion without architecture.** Every locus is named but the split or merge is wrong. | Repair `FPFContentArchitectureSelectionAdequacy`. |
| **Watch item as decision.** Drafting is expected to choose the answer later. | Select, narrow, split, or hold. |
| **Review-state proxy.** Review acceptance or landing is treated as adequacy. | Use decision-content evidence only. |
| **Adequacy table without evidence loci.** Values are listed without exact `DRR` or source loci. | Re-run the evaluation with `Coordinate | Value | ShortRationale | EvidenceLocus`; lower any coordinate whose evidence cannot be named. |

