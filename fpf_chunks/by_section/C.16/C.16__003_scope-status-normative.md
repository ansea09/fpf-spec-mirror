---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:2"
section_title: "Scope & Status (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__003_scope-status-normative.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:2 — Scope & Status (Normative)"
line_start: 44392
line_end: 44399
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:2 - Scope & Status (Normative)

**Scope.** **C.16** specifies the **measurement substrate** for FPF patterns: the roles of `U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`; their **CSLC discipline** (by reference to A.17 and A.18); and **evidence linkage semantics** at the level of *conceptual conditions*. It defines **direct interpretability** and **direct comparability** (same template), and it equips other patterns to state—and audit—comparability claims beyond direct comparability by **citing** the governing FPF pattern, method description, Bridge, or specification record. It **exports** these constructs for all FPF patterns (KD‑CAL, Arch‑CAL, etc.) without prescribing domain formulae, procedures, or any CHR mechanism semantics.

**Status.** **Normative** C.16 **depends on** A.17 (canonical **Characteristic**) and A.18 (minimal **CSLC** in Kernel). Where C.16 cites external CG‑frames, the stance is through **Part F** rows and **Bridges** (with CL and loss notes), not by vocabulary import.

**Out of scope.** No computational recipes, no work-procedure prescriptions, no governance or process guidance. No definitions of normalization, indicatorization, scoring, comparison, or selection mechanisms, no comparability policy specifications, and no admission gate specifications. C.16 concerns **measurement-definition constructs** and their **validity conditions** for measurement claims, not records or tooling. (Implementation guidance, if any, belongs outside Part C.)

