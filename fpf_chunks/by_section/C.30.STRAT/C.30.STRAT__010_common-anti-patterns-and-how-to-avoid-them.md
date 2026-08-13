---
chunk_kind: "child"
pattern_id: "C.30.STRAT"
pattern_title: "Stratification Wording Precision Restoration"
section_id: "C.30.STRAT:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.STRAT/C.30.STRAT__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.30.STRAT — Stratification Wording Precision Restoration"
  - "C.30.STRAT:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 61671
line_end: 61680
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.5"
  - "G.6"
  - "I.2"
keywords:
---

### C.30.STRAT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Source label as ontology | `layer`, `block`, `expert`, `cache`, or `gate` is treated as a kind by label. | Complete the `StratificationSourceLabelRepairNote` and select the subject pattern from the recovered neighborhood. |
| C.30 takeover | Any structure-like word is treated as governed by C.30 because it sounds architectural. | Choose by selected `ontologicalNeighborhood`; non-source-label claims are governed by the patterns named in `C.30.STRAT:4.2`. |
| Local trigger fanout | `A.6.M`, `C.30.LCA`, `C.31`, or another subject pattern copies a growing label table. | Keep one thin pointer to `C.30.STRAT` and keep the subject pattern to its own invariant. |
| Expert-as-role false positive | `expert` in MoE prose becomes a system-role kind, assignment, Work-attribution claim, or responsibility claim by word alone. | Treat it as a source label for submodel, transformation, path selection, candidate selection, or ordinary non-use. If unresolved claim-bearing *role* remains, use `E.10.ROLE` and recover only the independent branches that obtain: local system-role kind; separate System-classification judgment; exact assignment species and occurrence; complete actual-Work basis; responsibility or authority under its direct predicate or exact A.6.RCD missing governor; or another direct relation. No conjunction is required and no branch implies another. |
| Gate-as-gate-decision false positive | A gating function, UI label, or source word becomes gate passage. | Use `A.20` or `A.21` only for actual constraint-validity or gate-decision claims; otherwise use the function, flow, publication, or ordinary-label disposition named by value. |

