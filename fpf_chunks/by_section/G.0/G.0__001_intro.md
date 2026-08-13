---
chunk_kind: "child"
pattern_id: "G.0"
pattern_title: "Frame Standard and Comparability Governance — CG‑Spec"
section_id: "G.0:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.0/G.0__001_intro.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "G.0 — Frame Standard and Comparability Governance — CG‑Spec"
  - "G.0:intro — Intro"
line_start: 99290
line_end: 99297
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.5"
  - "E.5.2"
  - "F.9"
  - "G.1"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "CG-Frame"
  - "CG-Spec"
  - "CL-routing"
  - "ComparatorSet"
  - "MinimalEvidence"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "ScaleComplianceProfile (SCP)"
  - "admissibility gate"
  - "edition pins"
  - "Γ-fold"
  - "Φ(CL)"
  - "Φ_plane"
---

## G.0 - Frame Standard and Comparability Governance — CG‑Spec

**Tag.** Architectural pattern (foundational Standard; constrains G.1–G.5)
**Stage.** *design-time* legality gate (establishes comparison legality & evidence minima; constrains run-time gates)
**Primary output.** `CG‑Spec` — a notation-independent legality gate for a `CG‑Frame`, published to UTS (with explicit edition pins for downstream reproducibility and RSCR).
**Primary hooks.** `USM.ScopeSlice(G)`, `entityOfConcern`, `SCP`, `MinimalEvidence`, `CNSpecRef`, `Γ‑fold`, `Φ(CL)` / `Φ_plane` policy pins, `UTS` publication (Name Cards + edition pins).
**Non-duplication note.** Universal Part‑G invariants are governed by `G.Core` and are satisfied here **only via delegation** (`CC‑G0‑CoreRef` → `CC‑GCORE‑*`). Single‑governing definition CN/CG spec-ref discipline is enforced via `CC‑GCORE‑CN‑CG‑1` (no shadow specs; no competing defaults).

