---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Clarify Architecture and Structure Wording (Precision Restoration)"
section_id: "C.30.P:6"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__009_worked-cases.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.30.P — Clarify Architecture and Structure Wording (Precision Restoration)"
  - "C.30.P:6 — Worked cases"
line_start: 71997
line_end: 72010
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.8"
  - "G.5"
keywords:
  - "architecture description"
  - "architecture wording"
  - "diagram"
  - "model"
  - "precision restoration"
  - "structural view"
  - "structure wording"
---

### C.30.P:6 - Worked cases

| Wording | Repair |
| --- | --- |
| "The architecture is the diagram." | Recover how the diagram is used: as a publication, carrier, source cue, architecture-description rendering, or structural view. It is not the architecture itself. Apply `C.2.P` only while the source-publication distinction remains hidden, then `C.30` or `C.30.ASV` only if the architecture claim or structural view is recovered. |
| "`ArchitectureOf@PlantOps` is defined over structures S1 and S2 under context C." | Direct `C.30`; no `C.30.P` unless another selected structure, architecture-description use, structural-view use, source-return relation, or named C.30 subcase remains hidden. |
| "This ADR changed the architecture." | Recover whether the ADR is a publication, decision record, document with named source-use relation, architecture-description update, work plan, or ordinary source. Use `C.2.P`, `C.11`, `A.15`, or `C.30` when the corresponding claim kind is being made. |
| "The flow graph proves the architecture is safe." | Keep the flow-graph expression, selected flow structure, architecture-use account, and any proof or safety-assurance claim separate. Use `E.18.2` for the mathematical expression, `E.18` for the selected flow structure, `C.30.TFS-REL` for its bounded architecture-use record, `B.3` for assurance and the defining pattern for any separate proof, safety, or evidence claim; use `C.30` only for the grounded architecture claim or thin conditional architecture-description bridge, and `C.30.AD` when the full architecture-description mechanism is being used. |
| "The architecture score improved." | Recover whether the sentence means grounded architecture adequacy, selected-structure characteristic and scale score, pattern-quality coordinate, Q-bundle, benchmark result, gate threshold, or ordinary comparison. Use `C.16.P` while that meaning remains unresolved; an already clear score goes directly to its applicable measurement or evaluation rule. |
| "Functional architecture improved maintainability." | Recover hidden function wording through `A.6.F`, structural-view use through `C.30.ASV`, and the maintainability claim through `C.16.P`, `C.16.Q`, `C.25`, or its domain rule as needed. If improvement is attributed causally to the changed arrangement, use `C.28` for that further claim. |
| "The module layer supports the architecture." | Use `C.30.STRAT` if the source meaning of `layer` remains unclear. Use C.30.P only for the architecture or structure portion after recovery; use `A.6.M` only if a module-interface relation is recovered, `C.30.LCA` only if a control-layer relation is recovered, `C.2.P` if a publication-label or view-label distinction remains hidden, or `A.6.P` if a basedness, source-use, evidence, or reliance relation is being made; otherwise retain an ordinary source-label disposition. |

**Worked repair.** A review says, “The new module layer improved maintainability.” The available results report 80 seconds for revision R1 and 50 seconds for R2 on regression fixture F; the word *layer* merely labels the changed source grouping. The sufficient rewrite is: “On fixture F, the reported regression-test runtime was 80 seconds for R1 and 50 seconds for R2.” It preserves the observed comparison without claiming a structural layer, general maintainability gain or causal effect from two measurements. If the receiving task only needs that runtime comparison and its measurement basis is adequate, stop. If it needs a maintainability conclusion, establish how the measured runtime bears on that characteristic under `C.25` and the domain method; if it needs a causal conclusion, recover the additional intervention and comparison basis under `C.28`. If the grouping itself must be changed, recover its actual constituents and relations before using `A.22` or `C.30`. The stronger question selects the missing work; it does not invalidate the narrower measured result.

