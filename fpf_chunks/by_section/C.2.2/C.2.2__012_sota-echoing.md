---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__012_sota-echoing.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:11 — SoTA-Echoing"
line_start: 42901
line_end: 42915
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

### C.2.2:11 - SoTA-Echoing

Normative.

**SoTA pack binding note.** If a SoTA Synthesis Pack exists for KD‑CAL reliability / cross‑context warrant transport in your Context (G.2), cite its ClaimSheet IDs / CorpusLedger entries / BridgeMatrix rows here. Otherwise, record `SoTA-Pack: TBD/none` and treat this section as the seed (do not fork it silently elsewhere).

| Practice claim                                                                                                      | Post‑2015 source anchor                                                                   | Alignment to this pattern                                                                                                                                                           | Adoption status                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Verification and validation should be distinguished and tied to evidence quality, not to rhetoric.                  | ASME V&V 40‑2018 (model credibility assessment).                                          | This pattern separates VA and LA lanes and binds `R_eff` to evidence and declared scope rather than to narrative confidence.                                                        | **Adopt**, with KD‑CAL’s conservative fold as an explicit default.                                                   |
| Trustworthiness is context- and risk-dependent and requires explicit documentation of limits.                       | NIST AI Risk Management Framework 1.0 (2023).                                             | This pattern makes limits first-class via `G` and makes reuse loss explicit via CL penalties rather than informal caveats.                                                          | **Adapt**, because FPF treats transport loss as an epistemic penalty, not as a purely organisational risk statement. |
| Safety arguments should make claims, evidence, and assumptions explicit and reviewable.                             | UL 4600 (2020) and related assurance-case practice in autonomous systems.                 | This pattern treats `R` as an auditable warrant signal whose inputs are explicit evidence items and whose reuse requires explicit transport justification.                          | **Adopt**, while remaining notation-independent and avoiding tool mandates.                                          |
| Empirical results should be accompanied by structured provenance and usage conditions to enable reuse and critique. | “Datasheets for Datasets” (Gebru et al., 2018) and “Model Cards” (Mitchell et al., 2019). | This pattern’s scope discipline and lane reporting make empirical warrant portable only when its conditions are explicit; cross‑Context reuse is Bridge-only (e.g., `Bridge#MatLab_to_PlantB`, `CL=2`, `Φ=Φ_v1`), and congruence loss routes to `R_eff` only. | **Adopt**, with congruence penalties as the reuse control mechanism.                                                 |
| Reproducibility requires packaging evidence and making it re-checkable by others.                                   | ACM Artifact Review and Badging (updated practices post‑2015) and The Turing Way (2019).  | This pattern treats evidence as something that can be inspected across TA/VA/LA lanes and allows reliability to decay when evidence becomes stale or non-replayable.                | **Adapt**, because FPF treats decay and transport penalties as first-class calculus elements.                        |
| Strong inference benefits from “severe tests” rather than from accumulation of weak confirmations.                  | Mayo (2018) on severity in statistical inference.                                         | Weakest-link propagation and explicit scope declarations discourage superficial confirmation piling and encourage explicit, discriminating evidence.                                | **Adapt**, because KD‑CAL is agnostic to frequentist vs Bayesian inference but requires auditability.                |

