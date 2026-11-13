---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
section_id: "G.8:14"
section_title: "Author’s quick checklist (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__015_author-s-quick-checklist-informative.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.8 — Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
  - "G.8:14 — Author’s quick checklist (informative)"
line_start: 139166
line_end: 139179
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.23"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.17"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "SoS-LOG"
  - "admissibility ledger"
  - "rule ids"
  - "tri-state {pass\\"
---

### G.8:14 - Author’s quick checklist (informative)

* [ ] List the IDs of the applicable C.23 rules in `SoSLogRuleId[]`.
* [ ] Any numeric gates/thresholds are `G.4` Acceptance artefacts cited by id (no thresholds embedded in LOG or rungs).
* [ ] Evidence is citable: at run time use `PathId/PathSliceId` when available; at packaging time provide resolvable `A10EvidenceGraphRef?[]` / `EvidenceGraphId?`.
* [ ] Every actual sense, kind or plane correspondence retains its relation and receiving-use grounds under G.Core:4.2.3. For F.9 reuse, `G.8:Ext.BridgeReuseWiring` keeps the Bridge, separate bounded-use claim and reliance basis citable. `CL/CL^k/CL^plane` and `Φ/Ψ/Φ_plane` ids and editions are pinned when the calibration or named assurance account requires them; policy ids resolve under `F.8:8.1`.
* [ ] `PortfolioMode` and dominance defaults are not restated: cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` (governing definitions live outside `G.8`, typically `G.5`).
* [ ] When the bundle binds a QD use, its required descriptor, distance, insertion and emitter definitions are edition/policy pinned (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies); the exact space and its separate description-episteme reference are pinned iff cell boundaries/de-dup/parity depend on the space definition; **Spaces ≠ Maps**. `PortfolioMode=Archive` alone does not activate these QD fields.
* [ ] If open-ended surfaces are declared, pin `GeneratorFamilyRowRef`, `TransferRulesRef.edition` and any validity/coupler policies. Handle unknown transfer under the declared C.23 branch: permitted `degrade` after its prerequisites pass, otherwise `abstain`; report unavailable basis and unperformed judgements under C.23:4.2.1.
* [ ] `MaturityRungs` is a closed, UTS‑registered set; the maturity ladder is ordinal/poset with a declared `ReferencePlane`; rung transitions cite evidence.
* [ ] RSCR triggers are emitted as canonical `RSCRTriggerKindId` values (no prose-only “reasons”).
* [ ] Notation independence (`E.5.2`) and twin‑register discipline (`E.10`) are respected for all published heads/ids.
* [ ] If authoring tools materially shaped rule/rung content, cite `AuthoringMethodDescriptionRefs?[]` (edition‑pinned) for cross‑stance traceability.

