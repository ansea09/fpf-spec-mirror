---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Unified Normalization Mechanism (UNM)"
section_id: "A.19.UNM:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "A.19.UNM — Unified Normalization Mechanism (UNM)"
  - "A.19.UNM:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 27718
line_end: 27743
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:8 - Common Anti‑Patterns and How to Avoid Them

1) **Hidden normalization inside scoring or selection**
   Avoid by using `CN_Spec.comparability.mode` and explicit UNM use.

2) **“NCV ⇒ indicator” shortcut**
   Avoid by treating indicatorization as UINDM policy, not a byproduct of normalization.

3) **“We normalized” without declaring invariants**
   Avoid by naming `NormalizationInvariant[*]` and exposing `≡_UNM`.

4) **Cross-context reuse without transport declaration**
   Avoid by Bridge-only transport and auditing Bridge/CL/ReferencePlane pins.

5) **Choosing a representative implicitly**
   Avoid by either keeping quotient objects abstract or declaring `NormalizationFix`.

6) **Using “map/mapping/Map” language as if it were harmless**
   Avoid by using “normalization / re‑parameterization under invariants” and by keeping `Map` for its specialized FPF meaning.

7) **Treating UNM outputs as globally comparable across contexts or planes**
   Avoid by Bridge-only transport declarations + audited ReferencePlane/CL pins; otherwise stay context-local and fail‑closed.

8) **Re‑authoring editioned transport/calibration anchors downstream**
   Avoid by treating `UNM.TransportRegistryΦ` (and similar anchors) as single-writer editioned anchors: downstream is ref‑only.

