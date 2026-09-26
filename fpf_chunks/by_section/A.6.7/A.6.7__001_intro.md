---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
section_id: "A.6.7:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__001_intro.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.6.7 — MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
  - "A.6.7:intro — Intro"
line_start: 21471
line_end: 21506
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "G.10"
  - "G.5"
  - "U.Mechanism"
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

## A.6.7 - `MechSuiteDescription` — Shared Conditions for Joint Use of Distinct Mechanisms

> **Type:** Architectural pattern.
> **Status:** Stable.
> **Normativity:** Normative [A] (Core).

**Use this when.** Several distinct operation declarations must be used together under shared conditions. Select their exact contracts, cite the required specifications, and state the permitted operation order.

**First useful result.** Each protocol step resolves to one declaration edition and one operation in that declaration. Two implementations of the same declaration do not become two members.

**Not this pattern when.** Use A.6.1 for one operation declaration, A.3.1 for a way of doing, and A.15.2 for an ordinary plan or edition baseline. A suite is useful only when several declarations have joint conditions to express.

A `MechSuiteDescription` is a Kernel **Description** token that names a **set of distinct** `U.Mechanism` (different declaration contracts, not different realizations of one contract) and declares **suite-level obligations**, **required spec pins**, and any **allowed usage protocols**, without conflating this with `MechFamilyDescription` or with publication `Pack`s.

**Plain-name.** mechanism suite description; mechanism suite passport.

**Builds on.** A.6.1 (`U.Mechanism` canonical form), A.6.5 (SlotSpecs where a RelationSignature is current), E.10 (lexical + ontological rules; strict distinction; minimal specificity; kind suffixes), E.18 (transformation-flow structure and crossing visibility), E.18.1 (P2W carry-through), A.21 (gate-level decisions).

**Used by.** Mechanism stacks governed by **shared admissibility, transport and audit obligations** and selected operation declarations, including shared suites reused by Part G patterns such as G.5.

**Declared vocabulary and references.**

* **Declares:** `MechSuiteDescription` (KernelToken, Description) and the record names used by its canonical form: `MechSuiteId`, `SuiteObligation`, `SuiteObligations`, `SuiteSpecPins`, `SuiteProtocol`, `ProtocolStep`, `SuiteAuditObligations`.
* **Reuses (by reference):** `U.Mechanism` (members), `MechFamilyDescription` / `MechInstanceDescription` (optional citations), existing pinned references such as `CN‑Spec` / `CG‑Spec` (as pins), and E.18/P2W notions (as obligations/pins), without introducing new U-kinds.

**LEX.TokenClass.**
* `LEX.TokenClass(MechSuiteDescription) = KernelToken.`
* `LEX.TokenClass(MechSuiteId) = KernelToken.`
* `LEX.TokenClass(SuiteObligations) = KernelToken.`
* `LEX.TokenClass(SuiteSpecPins) = KernelToken.`
* `LEX.TokenClass(SuiteProtocol) = KernelToken.`
* `LEX.TokenClass(SuiteAuditObligations) = KernelToken.`

**EntityOfConcern.** A finite set of distinct mechanism declarations intended for joint use. The description's Tech name ends with `…Description`.
Lexical note: do **not** prefix this token with `U.`. The `U.*` namespace is for admitted U-kinds and governed kernel values; `MechSuiteDescription` is a description value for a suite of mechanism declarations, not a root kind.

