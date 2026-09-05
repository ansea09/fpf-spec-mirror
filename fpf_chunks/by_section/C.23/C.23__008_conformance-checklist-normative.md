---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__008_conformance-checklist-normative.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:7 — Conformance Checklist (normative)"
line_start: 53311
line_end: 53330
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
  - "admit"
  - "degrade"
  - "evidence"
  - "maturity"
  - "selector"
---

### C.23:7 - Conformance Checklist (normative)

| ID           | Requirement                                                                                                                                                                                | Purpose                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **CC-C23.1** | For each `MethodFamily`, an editioned `MaturityCard` SHALL name the exact family and registry edition, evidence profile, claim scope, qualification window, intended use, rung justification, A.10 anchors, and freshness windows; cite a relation and loss note only when the admission claim actually relies on it. | Makes maturity auditable for the declared family and admission use. |
| **CC-C23.2** | The `AdmissibilityLedger` row for each evaluation of an executable `SoS-LOG` rule on S2 MUST cite the exact MethodFamilyId and registry edition, rule and policy editions, Eligibility and CG-Spec verdicts, EvidenceProfile minima, Acceptance verdict, claim scope, qualification window, Γ-fold contributors where used, decision result, and EvidenceGraph path. Relation and loss-policy ids appear only when the branch relies on them. | Keeps every decision premise reconstructable. |
| **CC‑C23.3** | Enumerations used by the rules (**Degrade(mode)**; Maturity rungs) **SHALL** be **closed** and **UTS‑registered** (twin labels). | |
| **CC‑C23.4** | **Unknowns** in live S2 fields **SHALL** map to `Degrade(mode)` (including `sandbox`) or `Abstain` with explicit **branch‑ids**; no `unknown→0/false` coercions.                                                          | Tri‑state discipline.                          |
| **CC-C23.5** | If a branch relies on an F.9 Bridge, kind relation, or plane relation, it MUST cite that exact obtaining relation, direction, what meaning is preserved and what is lost, receiving use, and applicable loss policy; supported penalties selected under R4 affect `R_eff` only. A changed family, evidence profile, claim scope, qualification window, or use is not by itself a crossing. | Keeps `F` and `G` invariant and relation claims truthful. |
| **CC‑C23.6** | **No acceptance thresholds** in CHR or Maturity; acceptance thresholds **live only** in **AcceptanceClauses** (G.4).                                                                                             | Separation of concerns.                       |
| **CC‑C23.7** | `MaturityCard` **SHALL NOT** be turned into a global scalar; treat as **poset**; any ordering **MUST** be lawful over CHR types.                                                           | Forbids cross‑scale scalarisation.            |
| **CC‑C23.8** | Publish to **UTS** with twin labels. Run **GateCrossing visibility checks** only for a cited crossing of a selected **E.18** transformation-flow structure. Require **CrossingBundle** attestation only when the named receiving use needs it; apply **E.18/F.9/F.17/E.17** under their respective current uses. Apply **LanePurity** and **Lexical SD** (**E.10**); use GateChecks/GateProfile (**A.21**) only when a named gate decision is current. | Publication & crossing visibility hygiene. |
| **CC‑C23.9** | All enumerations (e.g., `Degrade(mode)`, Maturity rungs) **SHALL** declare a **closed value set** and **Scale kind**, and be registered at UTS (LEX enum clarity).                          | Avoids lexical drift; lawful typing.          |
| **CC‑C23.10** | **RSCR tests** cover negative/refusal paths (illegal CHR ops; CG‑Spec gate fail; Bridge missing when relied on; **Φ table/policy‑id missing** when that penalty policy is used; **Lexical SD violations (E.10)**); ensure **branch coverage** (Admit/Degrade/Abstain, unknown). | |
| **CC‑C23.11** | If QD fields are in scope, **R0.QD** **MUST** pass: lawful **CharacteristicSpaceRef** (d≥2, characteristics typed, planes declared per characteristic), **ArchiveConfig** (topology/resolution/K, `InsertionPolicyRef`, **editioned** `DistanceDef`), **EmitterPolicyRef** present. | QD legality gate. |
| **CC‑C23.12** | **DominanceRegime** **SHALL** default to `ParetoOnly`; switching to `ParetoPlusIllumination` **MUST** be authorised by **CAL** and cited by id in SCR.                                    | Prevents implicit scalarisation.              |
| **CC‑C23.13** | If `PortfolioMode=Archive`, LOG **MUST** allow G.5 archive outputs after `Admit` (R6) and publish **IlluminationSummary** as a report-only telemetry summary unless CAL opts‑in to dominance participation.                         | Lawful archive semantics.                     |
| **CC‑C23.14** | If `GeneratorIntent` present, **R7** **MUST** verify **EnvironmentValidityRegion** and **TransferRulesRef**; G.5 outputs are declared **{environment, method}** sets; coverage/regret telemetry published. | OEE legality & telemetry. |
| **CC‑C23.15** | On illumination increases/archive changes, current editions and any actual **edition increments** (CharacteristicSpaceRef/DistanceDefRef/EmitterPolicyRef) and the applicable **policy‑id** **SHALL** be logged (R8).                   | Reproducibility & refresh.                    |

