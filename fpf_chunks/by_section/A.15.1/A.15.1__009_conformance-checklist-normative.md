---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:8"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__009_conformance-checklist-normative.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:8 — Conformance Checklist (normative)"
line_start: 20265
line_end: 20358
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actuals"
  - "event"
  - "execution"
  - "log"
  - "occurrence"
  - "run"
---

### A.15.1:8 - Conformance Checklist (normative)

**CC‑A15.1‑1 (Strict distinction).**
`U.Work` is a **dated run-time occurrence**. It is **not** a `U.Method` (semantic way), **not** a `U.MethodDescription` (description), **not** a `U.Role` or `U.RoleAssignment` (assignment), and **not** a `U.WorkPlan` (plan or schedule).

**CC‑A15.1‑2 (Required links).**
Every `U.Work` **MUST** reference:
(a) `enactsMethod -> U.Method` (the method enacted),
(b) `methodDescriptionRef -> U.MethodDescription` when the source episteme or editioned method description is live,
(c) `performedBy -> U.RoleAssignment` (the assigned performer in context), and
(d) `executedWithin -> U.System` or `executedWithin -> U.SubSystem` (the operational system or subsystem accountable for the occurrence).

**CC‑A15.1‑3 (Time window).**
Every `U.Work` **MUST** carry a closed interval `[t_start, t_end]` (or an explicitly marked open end for in-flight work) and, where relevant, location or asset.

**CC‑A15.1‑4 (Context reference and judgement).**
A `U.Work` **MUST** be judged inside a declared **`U.BoundedContext`** (the **judgement context**).

* By default, the judgement context is **the context of the referenced MethodDescription**.
* If `performedBy` references a `U.RoleAssignment` in a different context, there **MUST** exist an explicit **Bridge (`U.Alignment`)** or policy stating cross-context acceptance. Otherwise, the Work is **non-conformant** in that context.

**CC‑A15.1‑4b (State-plane reference).**
Each `U.Work` **MUST** declare a `StatePlaneRef` for its Δ‑judgement.

**CC-A15.1-5 (RoleAssignment interval coverage).**
The `performedBy` `U.RoleAssignment` timespan **MUST** cover the Work interval. If it does not, the Work is **nonconformant for that role-assignment relation** or must be re-judged in a context that allows retroactive assignments.

**CC‑A15.1‑6 (Parameter binding).**
Parameters declared by the **MethodDescription** **MUST** have concrete values bound **at Work creation or start** and recorded with the Work. Defaults in the method description do not satisfy this requirement.

**CC‑A15.1‑7 (Capability check).**
All capability thresholds stated by the Method or MethodDescription **MUST** be checked against the **holder** in `performedBy` for the performed-work interval or declared checkpoints. Violations must be flagged on the Work outcome.

**CC‑A15.1‑8 (Acceptance criteria).**
Success and failure classes and quality grades **MUST** be determined by the acceptance criteria declared or referenced by the **MethodDescription** or **CG-Spec** **in the judgment context**. The verdict is recorded on the Work.

**CC‑A15.1‑9 (Resource honesty).**
All consumptions and costs (energy, materials, machine-time, money, tool wear) **SHALL** be booked **only** to `U.Work` (not to Method, MethodDescription, Role, or Capability). Estimates may live in method descriptions or plans; performed values live in Work.

**CC‑A15.1‑10 (Mereology declared).**
If a Work has parts, the chosen **part relation(s)** must be declared (temporal‑part, episode‑part, operational‑part, concurrent‑part). Ambiguous mixtures are forbidden.

**CC‑A15.1‑11 (Γ\_time selection).**
For any roll‑up, the judgement context **MUST** declare which temporal coverage operator applies: **union** (utilization) or **convex hull** (lead time). Silent mixing is prohibited.

**CC‑A15.1‑12 (Γ\_work aggregation).**
Aggregation of resource ledgers across Work parts **MUST** specify an **overlap policy** (e.g., “attribute shared machine‑time to parent only”) to prevent double‑counting.

**CC‑A15.1‑13 (Identity & retries).**
A retry **MUST** be modeled as a **new Work** linked via `retryOf`. Interruptions that are treated as the **same run** must be modeled as **episodes** (`resumptionOf`) per a context‑declared **episode policy**.

**CC‑A15.1‑14 (Concurrency & ordering).**
Overlaps and precedences among Work **MUST** use interval relations (`overlaps`, `precedes`, `contains`, or `within`). Implicit "step order" claims are not admissible evidence.

**CC‑A15.1‑15 (Cross‑context evidence).**
If a Work is to be accepted in multiple contexts (e.g., regulatory + operational), either:
(a) re‑judge it in each context, or
(b) provide Bridges that map acceptance criteria, units, and roles; never assume cross-context identity by name.

**CC-A15.1-16 (Method-description source changes during work).**
If the MethodDescription version changes mid‑run, the Work **MUST** either:
(a) split into episodes bound to respective method-description source editions, or
(b) record an explicit **method-description override** event in the judgement context. Silent substitution is forbidden.

**CC‑A15.1‑17 (Distributed performers).**
If multiple `U.RoleAssignment`s jointly perform the same top-level Work (e.g., multi-agent orchestration), the Work **MUST** either:
(a) designate a **lead `U.RoleAssignment`** and list others as **concurrent parts**, or
(b) be modeled as a **parent Work** with child Works per `U.RoleAssignment`.

**CC‑A15.1‑18 (Logs ≠ Work by themselves).**
Logs and telemetry are **evidence** for a Work; they **do not constitute** a Work unless bound to method-description source when live, performer, time window, affected referent, and judgment context.

**CC‑A15.1‑19 (Affected referent).** Each `U.Work` **MUST** name at least one affected referent (e.g., `U.Asset`, product, batch, dataset, or document) via `affected -> {...}`.

**CC‑A15.1‑20 (State-change witness).** Each `U.Work` **MUST** carry either (a) explicit **pre-state** and **post-state** references on the declared state-plane or (b) a **Δ-predicate** that can be evaluated on evidence. Trivial “no-op” runs **MUST** be flagged as such.

**CC‑A15.1‑21 (Affected-referent declaration vs. record handling).** A run whose only effect is copying or reformatting records **does not** qualify as `U.Work` unless the judgment context declares those records to be the **product referent** (e.g., data-product manufacture).

**CC‑A15.1‑22 (Executed-within declaration).** Each `U.Work` **MUST** declare `executedWithin -> U.System` or `executedWithin -> U.SubSystem`; if different from the asset of change, keep `affected` explicit.

**CC‑A15.1‑23 (Compositionality of Δ).** For composite Work, the parent effect **MUST** be the declared composition of child effects under the same overlap policy as `Γ_work`.

**CC‑A15.1‑24 (No new claims on publication views).** MVPK views for `U.Work` **SHALL NOT** add properties or claims beyond the declared work-occurrence claim; numeric or comparable content **MUST** include unit, scale, reference-plane, and **EditionId** pins; the term **"signature"** is banned on work-publication views.

**CC‑A15.1‑25 (No Γ leakage).** Publication views **MUST** reference Γ operators and policies by id when showing aggregates; they **MUST NOT** encode aggregation semantics in prose or imply defaults. Γ lives in Part B; views carry **pinned references** only.

**CC‑A15.1‑26 (No input-output re-listing).** Publication views **MUST NOT** restate method-description input and output lists; publish **presence pins** and source references only (per MVPK §5.4).

**CC‑A15.1‑27 (Lawful orders; return sets).** Any across-run comparison presented on a `U.Work` publication view **MUST** use a declared **ComparatorSet** (map-then-compare), **return sets** when order is partial, and **forbid** hidden scalarization or ordinal means.

**CC‑A15.1‑28 (Comparator and transport pins).** Any numeric or comparable acceptance or KPI on a `U.Work` publication view **MUST** pin `ComparatorSet.edition`, `CG-Spec.edition`, and, where conversions occur, `TransportRegistry.edition` with **Φ** or **Φ^plane** policy-ids; Bridge ids are mandatory for cross-context or cross-plane reuse; penalties affect the reliability relation only.

**CC-A15.1-29 (Telemetry-reference pins, when applicable).** If a Work instance feeds **G.11** or QD and OEE portfolios, it **SHALL** cite `PathId` or `PathSliceId` and the current declared **policy-id** in its evidence; illumination remains **report-only telemetry** unless CAL explicitly promotes it.

