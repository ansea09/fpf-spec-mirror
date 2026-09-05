---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:15"
section_title: "Conformance Use Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__017_conformance-use-checks.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:15 — Conformance Use Checks"
line_start: 86158
line_end: 86173
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

Relation boundary: `E.18` defines selected transformation-flow structures whose loci may bind independently identified actual `U.Transformation` values and structure-positioned adjacent values whose definitions or constraints are identified independently. It does not define a second change ontology, a transformation-composition relation, a work sequence, a method, a mechanism, a mathematical graph expression, or a publication record. A flow arrow, adjacency, shared work, common affected referent, or placement in one selected structure establishes neither an actual transformation nor transformation composition. When a selected-structure use raises bounded-transformation, dynamics-episteme, temporal-aspect, temporal-claim adequacy, work planning, performed work, work-to-change, production, evidence, assurance, gate, decision, architecture, structural-view, mechanism, selector, comparison, refresh, publication, or wording-use claims, apply the pattern whose Solution answers that exact claim before relying on the structure.

When a selected structure locus, selected path, path slice, substructure, or flow valuation expresses or constrains one independently identified actual bounded transformation, apply `A.3.4` to the `U.Transformation` claim and E.18 to the selected structure, containing locus, pins, locus kind, crossing, publication, comparability, and refresh discipline. Cite the exact predicate and case facts when dated work is claimed to cause or realize it, and cite the separate local `A.15.PROD` claim when production-work participation, entity-identity inception, or production completion is current. E.18 locus kinds do not automatically fill slots in other patterns. For a claim about the independently identified value bound at a locus, apply `A.3.4` to the bounded-transformation claim, `A.6.0` to the signature declaration, `A.6.1` and `E.20` to the mechanism claim, the applicable A.15 pattern to planning or dated Work, and `A.20` or `A.21` to the current internal-step-validity or gate claim.

