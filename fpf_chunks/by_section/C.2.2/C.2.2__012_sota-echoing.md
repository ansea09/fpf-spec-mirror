---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__012_sota-echoing.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:11 — SoTA-Echoing"
line_start: 43352
line_end: 43366
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.21"
  - "A.6.3.RT"
  - "B.1.3"
  - "B.3"
  - "B.3.3"
  - "B.3.4"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.29"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.2"
  - "G.6"
  - "G.7"
keywords:
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "direct relation"
  - "evidence-bound"
  - "no implicit averaging"
  - "pathwise justification (PathId)"
  - "warrant"
  - "weakest-link"
---

### C.2.2:11 - SoTA-Echoing

Normative.

**SoTA pack binding note.** If a G.2 SoTA Synthesis Pack has sources that bear on reliability under the exact changed claim scope, kind, reference plane, notation, source-local meaning, model use, or evidence basis in this case, cite the relevant ClaimSheet IDs and CorpusLedger entries. Cite a `BridgeMatrix` row only when the current path actually uses an F.9 cross-local semantic Bridge represented by that row. Otherwise record `SoTA-Pack: TBD/none` and treat this section as the seed; neither a generic Context nor a generic transport package is required.

| Practice claim                                                                                                      | Post‑2015 source anchor                                                                   | Alignment to this pattern                                                                                                                                                           | Adoption status                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Verification and validation should be distinguished and tied to evidence quality, not to rhetoric.                  | ASME V&V 40‑2018 (model credibility assessment).                                          | This pattern separates VA and LA lanes and binds `R_eff` to evidence and declared scope rather than to narrative confidence.                                                        | **Adopt**, with KD‑CAL’s conservative fold as an explicit default.                                                   |
| Trustworthiness depends on intended use, affected risks, operating conditions, and explicit limits.              | NIST AI Risk Management Framework 1.0 (2023).                                             | This pattern makes claim limits explicit through `G` and applies CL penalties only through the actual relation used by a reuse path.                                               | **Adapt**, because FPF treats declared relation loss as an epistemic penalty, not only as an organisational risk statement. |
| Safety arguments should make claims, evidence, and assumptions explicit and reviewable. | UL 4600 (2020) and related assurance-case practice in autonomous systems. | This pattern treats `R` as an auditable warrant signal whose inputs are explicit evidence items; any reuse names the exact relation traversed and its declared loss. | **Adopt**, while remaining notation-independent and avoiding tool mandates. |
| Empirical results should be accompanied by structured provenance and usage conditions to enable reuse and critique. | “Datasheets for Datasets” (Gebru et al., 2018) and “Model Cards” (Mitchell et al., 2019). | Scope discipline and lane reporting make empirical warrant reusable only when the exact evidence, claim, use, conditions, and any evidence-reuse or dataset relation are explicit; that relation's declared loss routes to `R_eff` only. | **Adopt**, with relation-specific congruence penalties as the reuse control mechanism. |
| Reproducibility requires packaging evidence and making it re-checkable by others. | ACM Artifact Review and Badging (updated practices post-2015) and The Turing Way (2019). | This pattern treats evidence as inspectable across TA/VA/LA lanes and lets reliability decay when evidence becomes stale or non-replayable. | **Adapt**, because FPF treats freshness and relation-specific reuse losses as first-class calculus inputs. |
| Strong inference benefits from “severe tests” rather than from accumulation of weak confirmations.                  | Mayo (2018) on severity in statistical inference.                                         | Weakest-link propagation and explicit scope declarations discourage superficial confirmation piling and encourage explicit, discriminating evidence.                                | **Adapt**, because KD‑CAL is agnostic to frequentist vs Bayesian inference but requires auditability.                |

