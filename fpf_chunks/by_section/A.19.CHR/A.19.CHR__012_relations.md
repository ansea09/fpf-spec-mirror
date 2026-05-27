---
chunk_kind: "child"
pattern_id: "A.19.CHR"
pattern_title: "CHRMechanismSuite"
section_id: "A.19.CHR:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CHR/A.19.CHR__012_relations.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.19.CHR — CHRMechanismSuite"
  - "A.19.CHR:12 — Relations"
line_start: 25431
line_end: 25461
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "A.6.7"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.19"
  - "E.TGA"
  - "G.0"
  - "G.10"
  - "G.5"
keywords:
  - "Bridge-only transport"
  - "CG-Spec"
  - "CHR suite"
  - "CN-Spec"
  - "P2W seam"
  - "SlotFillingsPlanItem"
  - "characterization core"
  - "crossing visibility"
  - "legality gate"
  - "no hidden scalarization"
  - "no hidden thresholds"
  - "penalties→R_eff"
  - "planned baseline"
  - "set-return selection"
  - "suite obligations"
  - "tri-state guard decision"
---

### A.19.CHR:12 - Relations

#### A.19.CHR:12.1 - Builds on

* **A.6.7 `MechSuiteDescription`** (the base suite description kind and obligations surface)
* **A.15.3 `SlotFillingsPlanItem`** (planned baseline in WorkPlanning)
* **A.6.1 `U.Mechanism.Intension`** and **A.6.5 slot discipline** (SlotSpecs in signatures; SlotIndex as projection)
* **A.19 CN‑Spec** and **G.0 CG‑Spec** (governance card and legality gate)
* **E.TGA / E.18** (P2W, crossings, UTS and Path pins)
* **E.10** (lexical and ontological discipline) and **E.19** (conformance style)

#### A.19.CHR:12.2 - Coordinates with

* **G.5** (selector semantics, set-return defaults, archive semantics and report-only illumination discipline)
* **G.10** and **PTM** (publication and telemetry as external steps, not suite internals)
* **A.21 OperationalGate(profile)** and **USM.Guards** (gate-level decisions and reserved guard pins)
* **C.23 SoS‑LOG** (explicit degrade branches such as probe-only and sandbox)

#### A.19.CHR:12.3 - Constrains and informs

* Constrains Part G universalization: G patterns should reference this suite for the universal CHR node set and express method and generator specifics only as (a) explicit specializations (`⊑/⊑⁺`) or (b) separate provider mechanisms connected via `Uses`.
* Informs other kits and suites: any kit or suite that materially participates in selection should provide an analogous `…SlotFillingsPlanItem` planned baseline, so that the P2W seam remains uniform and auditable.

#### A.19.CHR:12.4 - Notes for Part‑G

**Tell.** This pattern is intended as a universal core anchor for the Part‑G:

* G patterns not mixing universal CHR legality mechanics with CG-frame specifics, discipline-specific method content, and packaging concerns in one construct.
* Instead, they cite `CHRMechanismSuiteDescription` (universal node set and obligations) and keep specifics in explicit specializations or separate `Uses` providers.
* P2W integration is performed uniformly via `CHRMechanismSuiteSlotFillingsPlanItem` planned baselines, preserving the rule that only WorkEnactment witnesses launch values.

