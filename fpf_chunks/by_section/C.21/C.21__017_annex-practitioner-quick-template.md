---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:14"
section_title: "Annex - Practitioner Quick Template"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__017_annex-practitioner-quick-template.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:14 — Annex - Practitioner Quick Template"
line_start: 50570
line_end: 50589
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

### C.21:14 - Annex - Practitioner Quick Template

```
C.21.DHC(Discipline: <id>; IntendedUse: <use>; ClaimScope: <scope>; EffectiveReferenceScheme: <scheme-id-and-edition>; ComparisonBasis: <declared-comparison-set>; Γ_time: <policy>)
  ReproducibilityRate:
    value: <0..1>   lane: LA   window: <…>   scope: <…>
  StandardisationLevel:
    value: {none|emerging|de_facto|de_jure}   compare_only: true
  AlignmentDensity:
    value: <ratio>   units: bridges_per_100_cells   cell_set: <exact F.17 refs>   relation_refs: <exact F.9 refs>   CL_min: 2   scope: <…>
  DisruptionBalance:
    value: <−1..1>   method: <CD-index class / edition>   target_band: [l,u]
  EvidenceGranularity:
    value: <ordinal|ratio per selected scale edition>   notes: <…>
  MetaDiversity:
    value: <entropy/HHI>   target_band: [l,u]
Guards: ORD_COMPARE_ONLY(StandardisationLevel), UNIT_CHECK(*), FRESHNESS(*), LANE_TAGS, SCOPE_COVERS, CROSS_LOCAL_RELATION(if distinct F.17 cells are related)
Publish: UTS twin labels; RSCR triggers on method edition change.
```

