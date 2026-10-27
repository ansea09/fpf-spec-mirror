---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__008_conformance-checklist-normative.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:7 — Conformance Checklist (normative)"
line_start: 63720
line_end: 63739
dependencies:
  - "A.10"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "E.10"
  - "E.18"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
keywords:
  - "MethodFamily"
  - "SoS-LOG"
  - "abstain"
  - "admission rules"
  - "admit"
  - "degrade"
  - "evidence"
  - "maturity"
  - "selector"
---

### C.23:7 - Conformance Checklist (normative)

| ID           | Requirement                                                                                                                                                                                | Purpose                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **CC-C23.1** | An established or reused maturity judgement SHALL be cited through an editioned `MaturityCard` naming the exact family and registry edition, evidence profile, claim scope, qualification window, intended use, rung justification, A.10 anchors, and freshness windows. An early stop with no applicable judgement SHALL report that state under §4.2.1 without inventing a card or rung. Cite a relation and loss note only when the admission claim actually relies on it. | Makes established maturity auditable and keeps an unperformed judgement distinct from L0. |
| **CC-C23.2** | Each `AdmissibilityLedger` row MUST identify the exact MethodFamilyId and registry edition, S2, rule edition, intended use, claim scope, qualification window, decisive branch, and decision result. It MUST retain the consulted policy editions, established or applicable reused Eligibility, CG-Spec, evidence-profile and Acceptance results, and Γ-fold contributors where used; required missing bases and unperformed judgements are reported under §4.2.1. The A.10 source basis and any G.6 path ids follow R5; relation and loss-policy ids appear only when relied on. | Keeps the premises of each actual branch reconstructable, including early refusal. |
| **CC‑C23.3** | Enumerations used by the rules (**Degrade(mode)**; Maturity rungs) **SHALL** be **closed** and **UTS‑registered** (twin labels). | |
| **CC‑C23.4** | **Unknowns** in live S2 fields **SHALL** map to `Degrade(mode)` (including `sandbox`) or `Abstain` with explicit **branch‑ids**; no `unknown→0/false` coercions.                                                          | Tri‑state discipline.                          |
| **CC-C23.5** | If a branch relies on an F.9 Bridge, kind relation, or plane relation, it MUST cite that exact obtaining relation, direction, what meaning is preserved and what is lost, receiving use, and applicable loss policy; supported penalties selected under R4 affect `R_eff` only. A changed family, evidence profile, claim scope, qualification window, or use is not by itself a crossing. | Keeps `F` and `G` invariant and relation claims truthful. |
| **CC‑C23.6** | **No acceptance thresholds** in CHR or Maturity; acceptance thresholds **live only** in **AcceptanceClauses** (G.4).                                                                                             | Separation of concerns.                       |
| **CC‑C23.7** | `MaturityCard` **SHALL NOT** be turned into a global scalar; treat as **poset**; any ordering **MUST** be lawful over CHR types.                                                           | Forbids cross‑scale scalarisation.            |
| **CC‑C23.8** | Publish to **UTS** with twin labels. Run **GateCrossing visibility checks** only for a cited crossing of a selected **E.18** transformation-flow structure. Require **CrossingBundle** attestation only when the named receiving use needs it; apply **E.18/F.9/F.17/E.17** under their respective current uses. Apply **LanePurity** and **Lexical SD** (**E.10**); use GateChecks/GateProfile (**A.21**) only when a named gate decision is current. | Publication & crossing visibility hygiene. |
| **CC‑C23.9** | All enumerations (e.g., `Degrade(mode)`, Maturity rungs) **SHALL** declare a **closed value set** and **Scale kind**, and be registered at UTS (LEX enum clarity).                          | Avoids lexical drift; lawful typing.          |
| **CC‑C23.10** | **RSCR tests** cover negative/refusal paths (illegal CHR ops; CG‑Spec gate fail; Bridge missing when relied on; **Φ table/policy‑id missing** when that penalty policy is used; **Lexical SD violations (E.10)**); ensure **branch coverage** (Admit/Degrade/Abstain, unknown). | |
| **CC‑C23.11** | For an active QD use, **R0.QD MUST** pass: lawful **CharacteristicSpaceRef** (d≥2, characteristics typed, planes declared), **ArchiveConfig** (topology, resolution, K, `InsertionPolicyRef`, editioned `DistanceDef`) and **EmitterPolicyRef**. Evidence retention or set-valued selection alone does not activate this gate. | QD requirements apply to the actual QD use. |
| **CC‑C23.12** | **DominanceRegime** **SHALL** default to `ParetoOnly`; switching to `ParetoPlusIllumination` **MUST** be authorised by **CAL** and cited by id in SCR.                                    | Prevents implicit scalarisation.              |
| **CC‑C23.13** | Resolve `PortfolioMode` through G.5 `CC-G5.23`. An archive remains a source; G.5 outcomes follow G.5:4.4b–4.4e after the applicable admission result. When illumination telemetry is used, it remains report-only unless CAL authorises its dominance contribution. | Separates retention, QD construction and selector outcome. |
| **CC‑C23.14** | If `GeneratorIntent` is present, **R7 MUST** verify **EnvironmentValidityRegion** and **TransferRulesRef**. G.5 declares its outcome over **{environment, method}** pairs under G.5:4.4b–4.4e; coverage and regret remain telemetry. | OEE legality and telemetry. |
| **CC‑C23.15** | For the active QD or generator branch, illumination increases or search-archive changes retain the current definitions, actual edition increments and applicable policy ids under R8. Ordinary evidence retention does not activate QD telemetry fields. | Reproducibility and refresh of the actual use. |

