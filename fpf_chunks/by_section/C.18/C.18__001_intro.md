---
chunk_kind: "child"
pattern_id: "C.18"
pattern_title: "Open‑Ended Search Calculus (NQD‑CAL)"
section_id: "C.18:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18/C.18__001_intro.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "C.18 — Open‑Ended Search Calculus (NQD‑CAL)"
  - "C.18:intro — Intro"
line_start: 42379
line_end: 42389
dependencies:
  - "A.1"
  - "A.15"
  - "A.17-A.19"
  - "B.5.2.1"
  - "C.16"
  - "C.17"
  - "C.19"
  - "C.2"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "CandidateSet"
  - "DescriptorMapRef"
  - "DistanceDefRef"
  - "EmitterPolicyRef"
  - "Front vs ExplorationArchive"
  - "IlluminationSummary report-only telemetry"
  - "InsertionPolicyRef"
  - "NQD-CAL"
  - "NQDArchive"
  - "provenance editions"
  - "Γ_nqd.generate"
  - "Γ_nqd.illuminate"
  - "Γ_nqd.selectFront"
  - "Γ_nqd.updateArchive"
---

## C.18 - Open‑Ended Search Calculus (NQD‑CAL)

**Status.** Calculus specification (**CAL**). Exports `Γ_nqd.*` operators for open‑ended, illumination‑style generation. **ΔKernel = 0** (no kernel primitives added). *Minting note:* this CAL **does not mint** new U‑types; it defines **CAL‑records** that MAY alias to registered U‑types where present via **E.10/UTS**.

**Depends on.** A‑kernel (A.1–A.15), **MM‑CHR** (C.16) for measurements, **KD‑CAL** for similarity/corpora, **Sys‑CAL** for carriers, **Decsn‑CAL** (objectives; advisory), **Compose‑CAL** (set aggregation; advisory).

**Coordinates with.** **B.5.2.1** (binding), **C.17 Creativity‑CHR** (characteristics & scales), **C.19 E/E‑LOG** (policies: emitter selection, explore/exploit).

**Exports (CAL; no U‑type minting here).**
 - Records: `NQD.DescriptorMap` (alias of `U.DescriptorMap` if minted), `NQD.NQDArchive` (alias of `U.NQDArchive`), `NQD.Niche`, `NQD.ArchiveCell`, `NQD.EmissionSeed?`, `U.EmitterPolicyRef`, `U.InsertionPolicyRef`, `U.IlluminationSummary`, and `NQD.CandidateSet` (alias of `Set<U.Hypothesis>`).

