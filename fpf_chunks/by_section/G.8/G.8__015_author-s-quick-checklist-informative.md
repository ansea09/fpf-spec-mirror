---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "SoS‑LOG Bundles & Maturity Ladders"
section_id: "G.8:14"
section_title: "Author’s quick checklist (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__015_author-s-quick-checklist-informative.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "G.8 — SoS‑LOG Bundles & Maturity Ladders"
  - "G.8:14 — Author’s quick checklist (informative)"
line_start: 72769
line_end: 72783
dependencies:
  - "A.10"
  - "A.21"
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

* [ ] `RuleId[]` are ids only; rule semantics are governed by `C.23` (no re-definition in this bundle).
* [ ] `SoSLogRuleId[]` are ids only; rule semantics are governed by `C.23` (no re-definition in this bundle).
* [ ] Any numeric gates/thresholds are `G.4` Acceptance artefacts cited by id (no thresholds embedded in LOG or rungs).
* [ ] Evidence is citable: at run time use `PathId/PathSliceId` when available; at packaging time provide resolvable `A10EvidenceGraphRef?[]` / `EvidenceGraphId?`.
* [ ] Any cross-Context or cross-plane reuse is explicit: `BridgeId/BridgeCardId`, `CL/CL^k/CL^plane`, and `Φ/Ψ/Φ_plane` policy ids are pinned (policy ids resolvable per `F.8:8.1`).
* [ ] `PortfolioMode` and dominance defaults are not restated: cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` (governing definitions live outside `G.8`, typically `G.5`).
* [ ] QD pins are edition/policy pinned (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies); `CharacteristicSpaceRef.edition` is pinned iff cell boundaries/de‑dup/parity depend on it; **Spaces ≠ Maps**.
* [ ] If open‑ended surfaces are declared, pin `GeneratorFamilyId`, `TransferRulesRef.edition`, and any validity/coupler policy ids; unknown transfer validity is recorded as `degrade`/branching (no “fourth status”).
* [ ] `MaturityRungs` is a closed, UTS‑registered set; the maturity ladder is ordinal/poset with a declared `ReferencePlane`; rung transitions cite evidence.
* [ ] RSCR triggers are emitted as canonical `RSCRTriggerKindId` values (no prose-only “reasons”).
* [ ] Notation independence (`E.5.2`) and twin‑register discipline (`E.10`) are respected for all published heads/ids.
* [ ] If authoring tools materially shaped rule/rung content, cite `AuthoringMethodDescriptionRefs?[]` (edition‑pinned) for cross‑stance traceability.

