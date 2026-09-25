---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:0"
section_title: "At a glance — didactic, informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__002_at-a-glance-didactic-informative.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:0 — At a glance — didactic, informative"
line_start: 36435
line_end: 36454
dependencies:
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.ULSAM"
  - "A.19.USCM"
  - "A.6.1"
  - "A.6.5"
  - "C.22"
  - "E.18"
  - "G.0"
  - "G.5"
keywords:
  - "ComparisonResultSlot"
  - "SelectEligibility"
  - "SelectorMechanism"
  - "explicit criteria"
  - "finite basis of binary CPM applications"
  - "pass/degrade/abstain"
  - "required comparison coverage"
  - "selected candidate set"
  - "selection kernel"
---

### A.19.SelectorMechanism:0 - At a glance — didactic, informative

* **What it is:** a universal **set-returning** selection kernel: it takes candidates, admissible comparison outcomes, and explicit criteria, and returns a **selected set**, not a forced single winner.
* **What it is not:** it is not a hidden scoring model, not a comparator, not a gate, and not a telemetry or publishing step.
* **Why it exists:** to prevent three recurring failure modes: **hidden thresholds**, **silent scalarization**, and **winner‑take‑all defaults** under partial orders and uncertain evidence.
* **Use this when:** the current project question is selection from admitted candidates under explicit criteria after comparison has already been made or cited.
* **What this buys:** the practitioner gets one selected-set value whose criteria, finite basis of exact upstream binary CPM applications, required comparison coverage, token provenance, scope, predicate basis, plane, window, and policy bindings are explicit. `degrade` and `abstain` remain eligibility values, not selected-set members or alternative result kinds.
* **First output:** read the by-value candidate set bound to `SelectionSlot`. Read the candidate universe, finite upstream CPM application basis, required pair coverage, derived comparison-token union, selection conditions, claim scope and context slices, reference plane, evaluation window, eligibility value, and evidence use from the actual `Select` application and direct neighboring relations; they are not fields inside the selected set.
* **How it evolves:** method semantics and SoTA algorithm families connect via `G.2` packs and wiring modules; the kernel signature stays stable and teachable.
* **Suite stage:** `select` (ordering lives only in `A.19.CHR:4.5` and `suite_protocols`; suite membership is a set in `A.19.CHR:4.2`).
* **Inputs (conceptual):** admitted candidates; a finite by-value basis of exact upstream binary CPM applications, each with its exact pair, realized `GuardDecision`, and own `ComparisonResultSlot` binding when produced; the exact union of justified relation or poset tokens from those bindings; explicit `CriteriaSlot`, `CNSpecSlot`, `CGSpecSlot`; one `U.ClaimScope` with selected A.2.6 `U.ContextSlice` members; the same A.19 predicate basis when one governs the comparisons or selection criteria; effective reference plane; explicit evaluation window; and optional TaskSignature and MinimalEvidence policy refs.
* **Output (conceptual):** the by-value `SelectionSlot` candidate set. A singleton is allowed only under explicit selection conditions or an admissible upstream total order. The output is not a decision log, guard value, result episteme, generic result relation, publication, or replay record.
* **Non-goals:** does **not** normalize (UNM), indicatorize (UINDM), score (USCM), fold (ULSAM), compare (CPM), define acceptance thresholds, publish, or emit telemetry; it is a selection step over already-admissible inputs.
* **Planned use:** an A.15.2 baseline selects editions and policies. A.15.3 and SlotFillingsPlanItem apply only to independently declared receiving positions under A.19.CHR:4.7.2. The actual Select application carries its effective arguments and SelectionSlot binding under §4.1. Dated selection Work and an A.10 provenance account retain their independent grounds.
* **Transformation-flow use:** an E.18 node cites this declaration. Planned refs use A.15.3 typed filling only for independently declared receiving positions; actual Select bindings remain governed by §4.1.
* **Failure mode:** tri‑state guard (`pass|degrade|abstain`); missing or unknown evidence never coerces to `pass`.
* **Mental model:** `SelectEligibility` gates the step; `Select` applies explicit criteria to set‑valued comparison outcomes; the result is a selected set whose “single winner” behavior must be explicit.

---

