---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:15"
section_title: "Conformance evidence (how to show you comply)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__016_conformance-evidence-how-to-show-you-comply.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:15 — Conformance evidence (how to show you comply)"
line_start: 59182
line_end: 59190
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:15 - Conformance evidence (how to show you comply)

1. **Model lint:** run static checks for CC‑TGA‑01…25 (edge kind, gates on crossings, CV⇒GF, guard aggregation assignment, UNM declaration locus, SquareLaw).
2. **Publication audit:** sample a commuting square and a sentinel‑bounded subflow; verify pins and DecisionLog behavior on *block/degrade*.
3. **Replay test:** hold editions fixed; re‑run selection on a PathSlice; observe identical return‑sets; apply a bump; see only affected `PathSlice`s refresh.
4. **StructuralReinterpretation probe:** construct a minimal reinterpretation step; confirm `CL^k` with `bridgeChannel=Kind` on UTS, a SquareLaw‑retargeting witness on UTS, `PathSliceId` pinned, **CV.ReinterpretationEquivalence=pass**, and absence of hidden scalarization.

[20]: https://webstore.ansi.org/preview-pages/ISO/preview_ISO%2B23247-1-2021.pdf?srsltid=AfmBOooAUXpg38IpkTlUFtcCpaMVOjivkewJWDIUd1VemIJO91abNEkG "INTERNATIONAL STANDARD ISO 23247-1"

