---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:6"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__009_worked-cases.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:6 — Worked cases"
line_start: 52368
line_end: 52379
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.8"
  - "J.4"
keywords:
---

### C.30.P:6 - Worked cases

| Wording | Repair |
| --- | --- |
| "The architecture is the diagram." | The diagram is a publication, carrier, source cue, architecture description rendering, or structural view. It is not the architecture itself. Apply `C.2.P` if a source-publication relation set is live, then `C.30` or `C.30.ASV` only if the architecture claim or structural view is recovered. |
| "`ArchitectureOf@PlantOps` is defined over structures S1 and S2 under context C." | Direct `C.30`; no `C.30.P` unless another selected structure, architecture-description use, structural-view use, source-return relation, or exact C.30 subcase remains hidden. |
| "This ADR changed the architecture." | Recover whether the ADR is a publication, decision record, document with named source-use role, architecture-description update, work plan, or ordinary source. Use `C.2.P`, `C.11`, `A.15`, or `C.30` as live. |
| "The TGA graph proves the architecture is safe." | TGA graph and architecture-flow relation are not proof or safety assurance. Use `E.18` and `C.30.TGA-FLOW-REL` for flow relation, `B.3` or evidence patterns for assurance, `C.30` only for the grounded architecture claim or thin conditional architecture-description bridge, and `C.30.AD` when the full architecture-description mechanism is live. |
| "The architecture score improved." | Recover whether the sentence means grounded architecture adequacy, selected-structure characteristic and scale score, pattern-quality coordinate, Q-bundle, benchmark result, gate threshold, or ordinary comparison. Apply `C.16.P` before any score-based use. |
| "Functional architecture improved maintainability." | Recover function or functionality use via `A.6.F` when hidden, then architecture structural view via `C.30.ASV` or quality or maintainability via `C.16.P`, `C.16.Q`, `C.25`, or exact quality pattern. |
| "The module layer supports the architecture." | Treat `layer` first as a source label and apply `C.30.STRAT`. Return to C.30.P only for the architecture or structure portion after recovery; return to `A.6.M` only if a module-interface relation is recovered, to `C.30.LCA` only if a control-layer relation is recovered, to `C.2.P` if this is a publication label or view label, to `A.6.P` if a basedness, source-use, evidence, or reliance relation is live, or to ordinary source-label disposition. |

