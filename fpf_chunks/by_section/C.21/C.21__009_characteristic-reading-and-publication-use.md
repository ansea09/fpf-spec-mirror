---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:7"
section_title: "Characteristic Reading and Publication Use"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__009_characteristic-reading-and-publication-use.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:7 — Characteristic Reading and Publication Use"
line_start: 50495
line_end: 50503
dependencies:
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.20"
  - "E.10"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.5"
  - "G.9"
  - "U.Discipline"
keywords:
  - "alignment"
  - "discipline"
  - "disruption"
  - "field health"
  - "reproducibility"
  - "standardisation"
---

### C.21:7 - Characteristic Reading and Publication Use

1. **Declare the reading.** Name the discipline, intended use, `ClaimScope`, comparison basis, freshness window, and exact characteristic, scale, method, metric, and distance editions.
2. **Collect evidence.** Bind sources via **G.6 EvidenceGraph**; tag lanes and freshness.
3. **Compute DHC slots.** Enforce **Legality Matrix** and Guard Macros.
4. **State a cross-local relation only if needed.** When the reading actually relates distinct F.17 cells, cite the exact F.9 relation, CL, admitted use, and loss notes; apply any assurance penalty to **R** only.
5. **Publish to UTS.** Name Cards (Tech/Plain), twin labels; **bind `DHCMethodSpecRef.edition`**, `DistanceDefRef.edition`, and, where templates are used, `DHCMethodRef.edition`; register RSCR triggers (method change, ScoringMethod/NormalizationMethod edits).
6. **Publication view.** Feed G.12 with time-series and guard-bands (disruption, diversity) when a dashboard or trend publication is live.

