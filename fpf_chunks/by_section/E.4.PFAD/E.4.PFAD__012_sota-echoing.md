---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__012_sota-echoing.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:11 — SoTA-Echoing"
line_start: 69296
line_end: 69304
dependencies:
  - "C.32.ADR"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Architecture decisions need context, decision, status, consequences, and supersession memory, but the record must not replace the decision relation. | Nygard, `Documenting Architecture Decisions`, 2011 lineage source still current for compact ADR section functions, `https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions`; MADR, maintained template practice, current projection-format source, `https://adr.github.io/madr/`. | `Solution` requires `PrincipleFrameworkArchitectureDecision@Context` before `C.32.ADR` projection; filled decision slice includes rejected alternatives, consequences, and supersession condition. | Adopt section-function memory; adapt by making ADR-like text a projection of a prior FPF relation. |
| Architecture decision records need concern, rationale, and description-boundary discipline. | `ISO/IEC/IEEE 42010:2022`, official current standard ref for architecture-description concepts and architecture-versus-description boundary, `https://www.iso.org/standard/74393.html`. | `Problem frame` says first output is relation, not ADR or realized framework; `Relations` keeps `C.32.PAD` and `C.32.ADR` as owners. | Adopt rationale recovery; adapt to framework selected structures, source-return, and receiving owners. |
| A framework-decision specialization must remain justified by recurring local obligations and near misses. | Riehle, Harutyunyan, Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, arXiv:2107.06065, 2021 current validation-practice source. | `Demotion condition`, `Conformance Checklist`, and `Common Anti-Patterns` require PFAD to collapse when framework-specific slots are absent. | Adopt validation pressure; reject a child pattern that only repeats generic decision slots. |
| Compatibility, deprecation, and supersession need impact thinking beyond a label or status field. | `Semantic Versioning 2.0.0`, current-standard compatibility-boundary practice, `https://semver.org/spec/v2.0.0.html`; Chen et al., `Breaking Changes in Software Ecosystems: A Systematic Literature Review`, arXiv:2605.24397, 2026 current SLR, `https://arxiv.org/abs/2605.24397`. | `refreshOrSupersessionConditions`, `dependencyAndEditionRefs`, and `E.4.PFR` relation exits become required PFAD slots. | Adapt compatibility-impact discipline to framework editions; reject software package, build, and binary semantics. |

