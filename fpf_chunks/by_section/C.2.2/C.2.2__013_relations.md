---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__013_relations.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:12 — Relations"
line_start: 35855
line_end: 35861
dependencies:
  - "A.2.6"
  - "A.21"
  - "B.1.3"
  - "B.3"
  - "B.3.3"
  - "B.3.4"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.25"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.6"
  - "G.7"
keywords:
  - "Bridge-only reuse"
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "evidence-bound"
  - "no implicit averaging"
  - "pathwise justification (PathId)"
  - "warrant"
  - "weakest-link"
---

### C.2.2:12 - Relations

**Builds on:** C.2 (KD‑CAL overview), A.2.6 (Claim scope and operators), C.2.3 (Formality F), B.3 (Trust & Assurance calculus), B.1.3 (Γ‑fold patterns), B.3.3 (assurance lanes), B.3.4 (refresh/decay), C.3 (Kind‑CAL and kind bridges), F.9 (Bridges & CL), G.6 (EvidenceGraph PathId discipline), G.7 (Bridge calibration / admissibility thresholds).
**Coordinates with:** C.16 (MM‑CHR evidence discipline), E.14 (working-model assertions), E.18/F.9/F.17/E.17/A.21 where crossing bundles and gate checks are live, C.25 (Q‑Bundle, for avoiding confusion between epistemic reliability and system reliability).
**Used by:** C.3.3 (cross-kind reuse discipline), guard macro bundles in C.3.A and C.21, and any acceptance/gating logic that consumes `R_eff` while preserving `F` and `G`.
**Clarifies:** The KD‑CAL meaning of reliability implicit in C.2:4.1 and the transport clauses referenced across B.3 and C.3.

