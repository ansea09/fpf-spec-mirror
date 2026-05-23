---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:7"
section_title: "Measurement & Publication Procedure (authoring harness)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__008_measurement-publication-procedure-authoring-harness.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:7 — Measurement & Publication Procedure (authoring harness)"
line_start: 41366
line_end: 41374
dependencies:
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.20"
  - "E.10"
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

### C.21:7 - Measurement & Publication Procedure (authoring harness)

1. **Declare Context & TargetSlice.** (USM) Name editions, Standards, env params, `Γ_time`.
2. **Collect evidence.** Bind sources via **G.6 EvidenceGraph**; tag lanes and freshness.
3. **Compute DHC slots.** Enforce **Legality Matrix** and Guard Macros.
4. **Bridge (if needed).** Map via **F.9**; attach **CL** and **loss notes**; apply **R** penalties.
5. **Publish to UTS.** Name Cards (Tech/Plain), twin labels; **bind `DHCMethodSpecRef.edition`**, `DistanceDefRef.edition`, and, where templates are used, `DHCMethodRef.edition`; register RSCR triggers (method change, ScoringMethod/NormalizationMethod edits).
6. **Dashboard.** Feed G.12 with time-series and guard-bands (disruption, diversity).

