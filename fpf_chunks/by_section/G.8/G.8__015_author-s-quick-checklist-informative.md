---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
section_id: "G.8:14"
section_title: "Author’s quick checklist (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__015_author-s-quick-checklist-informative.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "G.8 — Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
  - "G.8:14 — Author’s quick checklist (informative)"
line_start: 129481
line_end: 129494
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
  - "tri-state {pass"
---

### G.8:14 - Author’s quick checklist (informative)

* [ ] `SoSLogRuleId[]` are ids only; rule semantics are governed by `C.23` (no re-definition in this bundle).
* [ ] Any numeric gates/thresholds are `G.4` Acceptance artefacts cited by id (no thresholds embedded in LOG or rungs).
* [ ] Evidence is citable: at run time use `PathId/PathSliceId` when available; at packaging time provide resolvable `A10EvidenceGraphRef?[]` / `EvidenceGraphId?`.
* [ ] Every actual sense, kind or plane correspondence retains its relation and receiving-use grounds under G.Core:4.2.3. For F.9 reuse, `G.8:Ext.BridgeReuseWiring` keeps the Bridge, separate bounded-use claim and reliance basis citable. `CL/CL^k/CL^plane` and `Φ/Ψ/Φ_plane` ids and editions are pinned when the calibration or named assurance account requires them; policy ids resolve under `F.8:8.1`.
* [ ] `PortfolioMode` and dominance defaults are not restated: cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` (governing definitions live outside `G.8`, typically `G.5`).
* [ ] When the bundle binds an actual QD use, its required descriptor, distance, insertion and emitter definitions are edition/policy pinned (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies); `CharacteristicSpaceRef.edition` is pinned iff cell boundaries/de-dup/parity depend on it; **Spaces ≠ Maps**. `PortfolioMode=Archive` alone does not activate these QD fields.
* [ ] If open‑ended surfaces are declared, pin `GeneratorFamilyRowRef`, `TransferRulesRef.edition`, and any validity/coupler policy ids; unknown transfer validity is recorded as `degrade`/branching (no “fourth status”).
* [ ] `MaturityRungs` is a closed, UTS‑registered set; the maturity ladder is ordinal/poset with a declared `ReferencePlane`; rung transitions cite evidence.
* [ ] RSCR triggers are emitted as canonical `RSCRTriggerKindId` values (no prose-only “reasons”).
* [ ] Notation independence (`E.5.2`) and twin‑register discipline (`E.10`) are respected for all published heads/ids.
* [ ] If authoring tools materially shaped rule/rung content, cite `AuthoringMethodDescriptionRefs?[]` (edition‑pinned) for cross‑stance traceability.

