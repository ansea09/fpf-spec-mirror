---
chunk_kind: "child"
pattern_id: "C.18"
pattern_title: "Open‑Ended Search Calculus (NQD‑CAL)"
section_id: "C.18:5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18/C.18__006_conformance-checklist.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "C.18 — Open‑Ended Search Calculus (NQD‑CAL)"
  - "C.18:5 — Conformance Checklist"
line_start: 42442
line_end: 42460
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

### C.18:5 - Conformance Checklist
- **C18‑1** Declare `DescriptorMap` (encoder, invariances, corpus edition) before generation.
- **C18‑1b** When used in F/G triads, DescriptorMap SHALL declare a domain‑family coordinate (grid/cells) and reference an F1‑Card::DistanceDefRef & δ_family.
- **C18‑1c**  When a domain‑family coordinate is declared, the Context SHALL compute and publish **AliasRisk** for each front / declared set-result emission, together with the dSig collision rule and the policy id. AliasRisk is computed against `U.DomainDiversitySignature (dSig)`; **the DescriptorMap SHALL publish**: (i) `collisionRuleId` (near‑duplicate threshold, e.g. “≥3 characteristics equal”),  (ii) `dSigSource` pointers used for coding the five characteristics. The collision rule and formula **MUST** be part of `DescriptorMap` provenance (see **Creativity‑CHR**, Heterogeneity Characterisation).
- **C18‑2** Record `EmitterPolicyRef` (policy id from C.19) and parameter set.
- **C18‑3** Compute `D = ΔDiversity_P(h | Pool)` under the same DescriptorMap & TimeWindow as the Pool (see C.17).
- **C18‑4** Exclude Illumination from dominance unless policy explicitly promotes it.
- **C18‑5** Keep `Use‑Value` separate from assurance scores; do not alter `F/G/R` semantics (see B.3, C.17 §Use‑Value).
- **C18‑6** Emit full provenance; thinning after front computation MUST be recorded.
- **C18‑7** Before computing any front, apply **ConstraintFit = pass** as a hard eligibility filter.

**Defaults.** Default-governance responsibility is split on purpose: `G.Core` and `G.5` govern `DefaultId.DominanceRegime` and selector-facing default routing, while `C.19` governs emitter, insertion, and pool-policy defaults. `C.18` consumes those defaults and records the active refs instead of restating them locally. Minimum provenance remains: `DescriptorMapRef.edition` and `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `TimeWindow`, `Seeds`, `DedupThreshold?`; also record `FamilyCoverage/MinInterFamilyDistance`.

**Didactic quickstart (Context).**
1) Pick 2–4 Quality coordinates and a simple DescriptorMap (2–4 dims).
2) Set defaults: `K=1`, `ε=0`, a conservative `EmitterPolicy`.
3) Run `Γ_nqd.generate` to fixed Budget; inspect the front; log coverage (IlluminationSummary).
4) Apply abductive plausibility filters; promote prime hypothesis to L0.

