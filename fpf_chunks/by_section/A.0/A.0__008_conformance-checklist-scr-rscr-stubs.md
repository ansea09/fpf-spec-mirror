---
chunk_kind: "child"
pattern_id: "A.0"
pattern_title: "Onboarding Glossary (NQD & E/E‑LOG)"
section_id: "A.0:7"
section_title: "Conformance Checklist (SCR/RSCR stubs)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.0/A.0__008_conformance-checklist-scr-rscr-stubs.md"
commit_sha: "cc1aef9b8e38dd50889e058fdc56725b9714fd42"
heading_path:
  - "A.0 — Onboarding Glossary (NQD & E/E‑LOG)"
  - "A.0:7 — Conformance Checklist (SCR/RSCR stubs)"
line_start: 1378
line_end: 1394
dependencies:
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
| **CC‑A0‑1** | If a pattern/UTS row **describes a generator, selector, typed portfolio publication, or set-return publication surface**, it **MUST** surface **N, U, C, Diversity_P, `ReferencePlane`, and E/E‑LOG `policy‑id`**; **units, scale, and polarity** **MUST** be declared. | Makes generative claims comparable and auditable (UTS as publication surface).  |
| **CC‑A0‑2** | When QD/OEE is in scope, **pin** editions: `DescriptorMapRef.edition`, `DistanceDefRef.edition` (and, where applicable, `CharacteristicSpaceRef.edition`, `TransferRulesRef.edition`); log `PathSliceId` and policy‑ids. | Enables admissible parity and refresh; edition-aware telemetry.                       |
| **CC‑A0‑3** | **No mixed‑scale roll‑ups**; ordinal data **SHALL NOT** be averaged; any roll‑up **MUST** live under a declared **CG‑frame**.                                                             | Prevents illegal scoring; keeps comparisons lawful.                             |
| **CC‑A0‑4** | Where the G‑kit requires parity, **publish an Illumination Map** (coverage per niche); **single‑number leaderboards are non‑conformant** on the Core surface when a ParityReport is required. | Declared-set-first / typed portfolio-publication posture; avoids single‑winner bias.                         |
| **CC‑A0‑5** | Keep **illumination/coverage** as **report‑only telemetry**; **dominance policy defaults to `ParetoOnly`**; any change is CAL‑authorised and cited by policy‑id.                                          | Separates fit from exploration; preserves auditability.                         |
| **CC‑A0‑6** | Apply **E.7/E.8**: include a **U.System** and a **U.Episteme** illustration when claiming generative behaviour; obey **E.10** register hygiene; use the exact subsection title **“Archetypal Grounding.”** | Locks didactic primacy; prevents jargon drift.                                  |
| **CC-A0-7** | **ReferencePlane declared** for every N/U/C/Diversity_P head and **CL^plane** penalties **route to R only**; **Φ_plane** policy-id published when planes differ.                            | Prevents plane/stance category errors; aligns with Bridge/**GateCrossing visibility** guards (Bridge+UTS+CL/Φ_plane). |
| **CC‑A0‑8** | **Diversity_P ≠ Illumination.** Diversity_P may enter dominance; **Illumination** remains **report‑only telemetry** unless explicitly promoted by CAL policy‑id.                                         | Matches QD triad semantics and parity defaults.                                 |
| **CC‑A0‑9** | For any generator/selector **scale-behaviour claim**, declare **S (Scale Variables)**, its **ScaleWindow**, and an **E/E-LOG scale policy-id**. Mark **S = N/A** only when no scale-behaviour claim is made. | Keeps a negative scale result within its declared comparison basis. |
| **CC‑A0‑10** | For scale-behaviour claims, execute a **scale-probe** (≥ 2 points along S within the declared ScaleWindow) and report a **Scale Elasticity class** (*rising/knee/flat/declining*) in the UTS row, under **C.18.1**. | Reports adverse response as declining rather than hiding it as flat or N/A. |
| **CC‑A0‑11** | Apply **Iso‑Scale Parity** in parity runs when S is declared; where infeasible, state the **loss notes** and treat results as **non‑parity** with an explicit penalty in **R**.             | Keeps comparisons fair and auditable under scale constraints.                    |
| **CC‑A0‑12** | Record a **BLP-waiver** only when overriding an actual declared generality preference that would otherwise decide the use. Apply **C.19.1**'s governed grounds: admissibility override, parity-supported scale-probe overturn, or non-blocking complementary bias. Bounded specialization alone requires no waiver. | Makes an actual policy override transparent without imposing one on ordinary bounded tactics. |

