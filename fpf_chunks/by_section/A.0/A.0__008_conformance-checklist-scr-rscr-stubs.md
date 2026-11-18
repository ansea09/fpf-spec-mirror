---
chunk_kind: "child"
pattern_id: "A.0"
pattern_title: "Generative Search Onboarding Glossary (NQD & E/E‑LOG)"
section_id: "A.0:7"
section_title: "Conformance Checklist (SCR/RSCR stubs)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.0/A.0__008_conformance-checklist-scr-rscr-stubs.md"
commit_sha: "169e3e09c04a4174ce4c26682cf181a0d255b6f7"
heading_path:
  - "A.0 — Generative Search Onboarding Glossary (NQD & E/E‑LOG)"
  - "A.0:7 — Conformance Checklist (SCR/RSCR stubs)"
line_start: 2409
line_end: 2425
dependencies:
  - "A.19"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.5"
  - "B.5"
  - "B.5.2.1"
  - "C.17"
  - "C.17-C.19"
  - "C.19"
  - "E.10"
  - "E.2"
  - "E.7"
  - "E.8"
  - "F.17"
  - "G.12"
  - "G.5"
  - "G.9"
  - "G.9-G.12"
  - "U.EpistemeRef"
keywords:
  - "& queries. novelty"
  - "BLP"
  - "CL^plane"
  - "DeclaredSubstrateInterpretiveView"
  - "OutcomeSpaceRef"
  - "ParetoOnly default"
  - "ReferencePlane"
  - "SearchSpaceRef"
  - "TypedSetViews"
  - "comparability"
  - "declared set result"
  - "explore/exploit (E/E-LOG)"
  - "explore/exploit (E/E‑LOG)"
  - "illumination map (report‑only telemetry)"
  - "novelty"
  - "parity run"
  - "quality-diversity (NQD)"
  - "quality‑diversity (NQD)"
  - "scale-probe"
  - "typed portfolio publication"
---

### A.0:7 - Conformance Checklist (SCR/RSCR stubs)

| ID          | Requirement                                                                                                                                                                               | Purpose                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **CC‑A0‑1** | If a pattern/UTS row **describes a generator, selector, typed portfolio publication, or set-return publication surface**, it **MUST** surface the glossary values and policies used by its operation or independently required by the receiving use, with their applicable **units, scale, polarity, ReferencePlane and policy‑ids**. | Makes generative claims comparable and auditable (UTS as publication surface). |
| **CC‑A0‑2** | For QD/OEE, **pin** the editions and policy‑ids used by the operation or required by the receiving use, including `DescriptorMapRef.edition`, `DistanceDefRef.edition`, the `CharacteristicSpaceRef` with its separate `characteristicSpaceDescriptionRef: U.EpistemeRef` under A.19:5.1.1.1 and `TransferRulesRef.edition` where applicable. Log `PathSliceId` when required; follow **G.9**'s pin requirements for a parity use. | Enables admissible parity and refresh; edition-aware telemetry. |
| **CC‑A0‑3** | **No mixed‑scale roll‑ups**; ordinal data **SHALL NOT** be averaged; any roll‑up **MUST** live under a declared **CG‑frame**.                                                             | Prevents illegal scoring; keeps comparisons lawful.                             |
| **CC‑A0‑4** | Where the G‑kit requires parity, **publish an Illumination Map** (coverage per niche); **single‑number leaderboards are non‑conformant** on the Core surface when a ParityReport is required. | Declared-set-first / typed portfolio-publication posture; avoids single‑winner bias.                         |
| **CC‑A0‑5** | Keep **illumination/coverage** as **report‑only telemetry**; **dominance policy defaults to `ParetoOnly`**; any change is CAL‑authorised and cited by policy‑id.                                          | Separates fit from exploration; preserves auditability.                         |
| **CC‑A0‑6** | Apply **E.7/E.8**: include a **U.System** and a **U.Episteme** illustration when claiming generative behaviour; obey **E.10** register hygiene; use the subsection title **“Archetypal Grounding.”** | Locks didactic primacy; prevents jargon drift.                                  |
| **CC-A0-7** | **ReferencePlane declared** for every reported N/U/C/Diversity_P head. For a plane relation, retain its source/target planes and basis under **G.Core:4.2.3**; cite **CL^plane** for a used or required calibration and the **Φ_plane** policy and loss model for a used or required loss calculation. Numerical assurance penalties follow an applicable B.3 model. | Prevents plane/stance category errors while preserving applicable crossing and receiving-use grounds. |
| **CC‑A0‑8** | **Diversity_P ≠ Illumination.** Diversity_P measures the retained set; DeltaDiversity_P measures a candidate's marginal contribution to it. Either requires a declared `PromotionPolicy` before entering dominance. **Illumination** remains **report‑only telemetry** unless explicitly promoted by a CAL-authorized policy-id.                                         | Matches QD triad semantics and parity defaults.                                 |
| **CC‑A0‑9** | For a generator or selector scale-behaviour claim, declare the scale variables **S** and the settings or range the claim covers. Cite the **E/E-LOG scale policy-id** when the claim or its use depends on a policy, for example a knee threshold or selection by class. A prediction from a model states the assumptions of the derivation. Mark **S = N/A** when no scale-behaviour claim is made. | Identifies what varies and the grounds for the asserted response. |
| **CC‑A0‑10** | For an empirical scale-behaviour claim, identify the compared settings, response, conditions and uncertainty. Use an applicable probe or obtain the missing evidence when the claim is needed. Report the class supported under **C.18.1**. With only one setting, report the result there and leave the trend open. Use a UTS row when **F.17** calls for one. | Makes the grounds for the scale claim recoverable, including when classification remains open. |
| **CC‑A0‑11** | Apply **Iso‑Scale Parity** in parity runs when S is declared; where infeasible, state the **loss notes** and treat results as **non‑parity**. For a penalty calculated or required by the receiving use, cite its model and policy; numerical assurance penalties require an applicable B.3 model. | Keeps comparisons fair and auditable under scale constraints. |
| **CC‑A0‑12** | Record a **BLP-waiver** only when overriding a declared generality preference that would otherwise decide the use. Apply **C.19.1**'s governed grounds: admissibility override, parity-supported scale-probe overturn, or non-blocking complementary bias. Bounded specialization alone requires no waiver. | Makes a policy override transparent without imposing one on ordinary bounded tactics. |

