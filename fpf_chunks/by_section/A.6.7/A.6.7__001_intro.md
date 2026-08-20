---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Description of a set of distinct mechanisms"
section_id: "A.6.7:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__001_intro.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.6.7 — MechSuiteDescription — Description of a set of distinct mechanisms"
  - "A.6.7:intro — Intro"
line_start: 19807
line_end: 19837
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.18"
  - "E.19"
  - "E.8"
  - "G.10"
  - "G.5"
  - "U.Mechanism.Intension"
keywords:
  - "CG-Spec"
  - "CN-Spec"
  - "P2W"
  - "crossing visibility"
  - "distinct mechanisms"
  - "mechanism suite"
  - "planned baseline"
  - "spec pins"
  - "suite obligations"
---

## A.6.7 - `MechSuiteDescription` — Description of a set of distinct mechanisms

> **Type:** Architectural pattern.
> **Status:** Stable.
> **Normativity:** Normative [A] (Core).

**One-line summary.** A `MechSuiteDescription` is a Kernel **Description** token that names a **set of distinct** `U.Mechanism.Intension` (different mechanisms, not realizations of one mechanism) and declares **suite-level obligations**, **required spec pins**, and **allowed usage protocols**, without conflating this with `MechFamilyDescription` or with publication `Pack`s.

**Plain-name.** mechanism suite description; mechanism suite passport.
**Placement.** Part A → cluster A.IV (A.6), immediately after A.6.5.

**Builds on.** E.8 (pattern template discipline), A.6.1 (`U.Mechanism.Intension` canonical form), A.6.5 (slot/ref discipline), E.10 (lexical + ontological rules; strict distinction; minimal specificity; kind suffixes), E.19 (conformance checks), E.18 (transformation-flow structure and P2W carry-through discipline; crossing visibility), A.21 (OperationalGate(profile) and gate-level decisions).

**Used by.** Any framework area that needs a stable universal kernel shared across multiple mechanisms (notably the universalization of Part G patterns, including but not limited to G.5), and any mechanism stack whose correctness is defined by **shared admissibility + transport + audit obligations** and declared mechanism intensions.

**Mint vs reuse.**

* **Mints:** `MechSuiteDescription` (KernelToken, Description) and the record names used by its canonical form: `MechSuiteId`, `SuiteObligation`, `SuiteObligations`, `SuiteSpecPins`, `SuiteProtocol`, `ProtocolStep`, `SuiteAuditObligations`.
* **Reuses (by reference):** `U.Mechanism.Intension` (members), `MechFamilyDescription` / `MechInstanceDescription` (optional citations), existing pinned references such as `CN‑Spec` / `CG‑Spec` (as pins), and E.18/P2W notions (as obligations/pins), without introducing new U-kinds.

**LEX.TokenClass.**
* `LEX.TokenClass(MechSuiteDescription) = KernelToken.`
* `LEX.TokenClass(MechSuiteId) = KernelToken.`
* `LEX.TokenClass(SuiteObligations) = KernelToken.`
* `LEX.TokenClass(SuiteSpecPins) = KernelToken.`
* `LEX.TokenClass(SuiteProtocol) = KernelToken.`
* `LEX.TokenClass(SuiteAuditObligations) = KernelToken.`

**EntityOfConcern / Description / specification-use.** Description (D); Tech name ends with `…Description`.
Lexical note: do **not** prefix this token with `U.`. The `U.*` namespace is for admitted U-kinds and governed kernel values; `MechSuiteDescription` is a description value for a suite of mechanism intensions, not a root kind.

