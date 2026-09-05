---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "SoS‑LOG Bundles & Maturity Ladders"
section_id: "G.8:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__001_intro.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "G.8 — SoS‑LOG Bundles & Maturity Ladders"
  - "G.8:intro — Intro"
line_start: 105013
line_end: 105022
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

## G.8 - SoS‑LOG Bundles & Maturity Ladders

**Tag.** Architectural pattern (packaging kit).
**Stage.** Design‑time packaging (authoring & publication) with a run‑time consumption facade for `G.5` (selector/registry).
**Primary hooks:** `G.Core` (Part‑G invariants), `C.23` (SoS‑LOG semantics), `C.22` (TaskSignature), `G.4` (Acceptance & EvidenceProfiles), `G.6` (EvidenceGraph & `PathId/PathSliceId`), `G.5` (registry/selector), `G.11` (refresh orchestration), `G.10` (shipping boundary), `F.9` (BridgeCard & CL), `F.17` (UTS), `E.17` (publication faces), `G.7` (bridge calibration & Φ/Ψ/Φ_plane), `F.8` (Policy pins: `PolicySpecRef`/`MintDecisionRef` resolvability), `A.10` (anchors), `E.10` (LEX twin registers), `E.5.2` (notational independence), `E.18/A.21` (GateCrossing visibility and gate checks).

**Non‑duplication note (Phase‑2 universalization).** This pattern introduces **kit-governed packaging surfaces** for SoS‑LOG bundles and maturity ladders. All **Part‑G‑wide invariants** (no shadow specs, Bridge‑only crossings + visibility, tri‑state guard domain, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, defaults with one governing definition, shipping boundary) are **pinned through `G.Core`** and are not restated here.

**Modularity note (policy‑id pins are reference‑only).** This kit may pin/cite policy ids (e.g., `Φ/Ψ/Φ_plane` policies, `FailureBehaviorPolicyId`, illumination‑promotion policy ids, and E/E‑LOG policy ids) **as references only**. Conformance relies on the policy‑pin resolvability discipline of `F.8:8.1` (i.e., policy ids are not “inlined”; and when newly minted, they are backed by resolvable `PolicySpecRef` + `MintDecisionRef`). `G.8` does not define policy semantics and MUST NOT silently mint policy ids.

