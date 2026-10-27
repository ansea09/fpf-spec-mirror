---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism (ULSAM)"
section_id: "A.19.ULSAM:0"
section_title: "At a glance (didactic, informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__002_at-a-glance-didactic-informative.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism (ULSAM)"
  - "A.19.ULSAM:0 — At a glance (didactic, informative)"
line_start: 38278
line_end: 38302
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UINDM"
  - "A.19.ULSAM"
  - "A.19.USCM"
keywords:
  - "CG-Spec.SCP"
  - "CG-Spec.Γ_fold"
  - "MinimalEvidence"
  - "fold_Γ?"
  - "lawful aggregation"
  - "scale-lawful fold"
  - "tri-state guard (pass"
  - "ΓFoldRef"
---

### A.19.ULSAM:0 - At a glance (didactic, informative)

* **Suite stage:** `fold_Γ?` (ordering lives only in `A.19.CHR:suite_protocols`; `mechanisms[]` membership is a set, not an order).
* **Input surface:** an admitted `MeasureSetSlot`, `CNSpecSlot`, `CGSpecSlot`, and `GammaFoldSlot`, with the grouping or membership basis, fold and policy editions, claim scope and selected slices, qualification window, evidence basis, contributors, and intended result declared by those inputs; `MinimalEvidenceSlot?` may override the CG-Spec minimum.
* **Output surface:** `AggregatedMeasureSlot` (+ optional `ContributorSetSlot?` as an explanation surface).
* **Non‑goals:** no scoring, no comparison, no selection, no “method catalog”, no hidden defaults, no hidden thresholds.
* **P2W seam:** an A.15.2 baseline selects the fold, evidence policy and their editions. A.15.3 typed filling applies only to independently declared receiving positions under the CHR P2W hook. Actual fold arguments bind under §4.1; a planned value does not establish that binding.
* **Failure mode:** tri‑state guard `GuardDecision := {pass|degrade|abstain}`; unknown/insufficient evidence never coerces to “pass”.
* **Rule of thumb:** if you are about to “average/sum/roll up”, you probably need an explicit ULSAM `Fold_Γ` stage (or a justified decision to *not* fold).

**What this mechanism is.** `ULSAM` is the CHR mechanism that makes **aggregation explicit**: it performs an explicit **Γ‑fold** over a set of **admitted measures**, producing an **aggregated measure** (and optionally a contributor surface) under **declared admissibility**.

**Use this when** the receiving use needs an aggregate measure:
- You want to “roll up” multiple measures into one measure (e.g., an overall reliability/assurance coordinate, a single aggregated risk measure, an aggregate score coordinate).
- You need the fold to be **auditable** (what contributed; what was excluded by evidence/admissibility).
- You need the fold to be **scale-lawful** (no ordinal arithmetic; no illegal mixing of units).
- You need the fold to be **policy-bound and edition-stable** (replayability and pin traceability).

**Choosing the fold.** If the law for the intended result or a required property is unresolved, use A.9 or reuse a sufficient domain result. When the result selects a fold, its law and conditions supply the basis for the explicit fold reference; ULSAM still governs admission of the measures, scale lawfulness and the actual mechanism operation.

**Where it sits in CHR.**
- In the CHR suite protocol, ULSAM corresponds to the optional stage `fold_Γ?` (i.e., **explicitly optional** and never hidden inside `score/compare/select`).

**First useful move.** State what the aggregate must mean and which contributors it covers. Resolve the fold and its conditions, then check the actual inputs. If separate measures already answer the receiving question, stop without folding. Make the actual contributors recoverable; a separate ContributorSet result is optional.

