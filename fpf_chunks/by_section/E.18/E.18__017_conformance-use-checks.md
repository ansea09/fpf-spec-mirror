---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:15"
section_title: "Conformance Use Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__017_conformance-use-checks.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:15 — Conformance Use Checks"
line_start: 78891
line_end: 78903
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:15 - Conformance Use Checks

1. **Model lint:** run static checks for CC-E18-01...25 (transfer relation kind, gates on crossings, CV=>GF, guard aggregation assignment, UNM declaration locus, SquareLaw).
2. **Publication audit:** sample a commuting square and a sentinel‑bounded subflow; verify pins and DecisionLog behavior on *block* or *degrade*.
3. **Replay test:** hold editions fixed; re‑run selection on a PathSlice; observe identical return‑sets; apply a bump; see only affected `PathSlice`s refresh.
4. **StructuralReinterpretation probe:** construct a minimal reinterpretation step; confirm `CL^k` with `bridgeChannel=Kind` on UTS, a SquareLaw‑retargeting witness on UTS, `PathSliceId` pinned, **CV.ReinterpretationEquivalence=pass**, and absence of hidden scalarization.

[20]: https://webstore.ansi.org/preview-pages/ISO/preview_ISO%2B23247-1-2021.pdf?srsltid=AfmBOooAUXpg38IpkTlUFtcCpaMVOjivkewJWDIUd1VemIJO91abNEkG "INTERNATIONAL STANDARD ISO 23247-1"

Relation boundary: `E.18` governs selected transformation-flow structures for structures of atomic `U.Transformation` values and their structure-positioned slot-filler loci. It does not define a second change ontology, a work sequence, a method, a mechanism, a mathematical graph expression, or a publication record. When a selected-structure use raises bounded-transformation, dynamics-episteme, temporal-aspect, temporal-claim adequacy, work planning, performed work, evidence, assurance, gate, decision, architecture, structural-view, mechanism, selector, comparison, refresh, publication, or wording-use claims, name the governing pattern for that relation before relying on the structure.

When a selected structure locus, selected path, path slice, substructure, or flow valuation expresses, decomposes, or constrains one bounded transformation relation, use `A.3.4` for the atomic `U.Transformation` claim and use `E.18` for the selected structure, containing locus, pins, locus kind, crossing, publication, comparability, and refresh discipline. E.18 locus kinds do not automatically fill slots in other patterns: `Transformation` points to `A.3.4`, `Signature` points to `A.6.0`, `Mechanism` points to `A.6.1` and `E.20`, `WorkPlanning` and `Work` point to the A.15 work family, and `Check` points to `A.20` or `A.21` according to the current claim.

