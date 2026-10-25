---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:15"
section_title: "Conformance Use Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__017_conformance-use-checks.md"
commit_sha: "ea8c54542bf017f36659167f36e816fad4de88cb"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:15 — Conformance Use Checks"
line_start: 110071
line_end: 110084
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:15 - Conformance Use Checks

Choose tests from the current use, then apply the selected profile to those tests. The full CC-E18 table is available for combined or high-assurance uses; it is not an instruction to run every row for every selected structure.

1. **Ordinary selected-structure check:** verify the selected structure, independently grounded locus values, one internal `U.Transfer` relation kind, and only the current position, path, path slice, or valuation. The cooling-loop first-use slice can close here when it asserts no crossing, launch, publication, comparison or selection, cycle or refresh, or assurance branch; missing faces, `LaunchGate`, selector, `DecisionLog`, and SquareLaw are then not defects.
2. **Crossing or launch check, when current:** for a `GateCrossing`, apply its crossing and gate rows, including the exact positions and changed-binding account; add launch rows only for a current `LaunchGate` or work-entry claim. Do not infer a Work occurrence from either gate.
3. **Publication or assurance check, when current:** for a published face, apply the MVPK, pin, and no-new-claim rows. Inspect `DecisionLog`, evidence-lane, replay, or SquareLaw material only when the current decision, crossing, publication, or named downstream reliance needs it.
4. **Comparison, selection, cycle, or refresh check, when current:** apply comparator and set-return tests to a current comparison or selection; apply budget, sentinel, edition, and slice-local replay tests to a current cycle or refresh. Hold editions fixed only for a replay claim, and test an edition bump only for a current refresh use.
5. **Structural reinterpretation check, when current:** confirm one exact A.6.4 arrow r, an affirmative q, a separate current-case judgement of `satisfies`, unchanged `CtxState`, and `PathSliceId` locality. Apply A.20 only when q also raises a current internal constraint. Test an independent F.9 Bridge and its bounded-use claim only when cross-semantic correspondence is also claimed; keep optional `CL`, evidence, reliance, any application, and Work separate.

[20]: https://webstore.ansi.org/preview-pages/ISO/preview_ISO%2B23247-1-2021.pdf?srsltid=AfmBOooAUXpg38IpkTlUFtcCpaMVOjivkewJWDIUd1VemIJO91abNEkG "INTERNATIONAL STANDARD ISO 23247-1"

For an independently identified value at a locus, use its defining pattern for the subject claim. A locus binding does not fill slots in another pattern.

