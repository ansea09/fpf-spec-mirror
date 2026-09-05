---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:5"
section_title: "Archetypal Grounding — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__007_archetypal-grounding-informative.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:5 — Archetypal Grounding — informative"
line_start: 34690
line_end: 34736
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

### A.19.SelectorMechanism:5 - Archetypal Grounding — informative

#### A.19.SelectorMechanism:5.1 - Tell

When comparisons are partial or set-valued, selection must not pretend there is a single best candidate by default. `SelectorMechanism` makes selection explicit, policy-bound, and replayable: it returns a set unless criteria explicitly demand otherwise.

#### A.19.SelectorMechanism:5.2 - Show, U.System example

**Scenario.** A platform team must pick a set of deployment options for a subsystem under multiple criteria: latency, cost, and regulatory risk. Comparisons are multi-criteria and do not induce a total order.

* `CandidateSetSlot = {OptionA, OptionB, OptionC}`.
* `CriteriaSlot` requires Pareto selection over the three unordered pairs `{A,B}`, `{A,C}`, and `{B,C}`, returns all non-dominated admissible candidates, and preserves the full selected set unless an explicit current criterion requires a singleton.
* The finite upstream comparison-application basis covers all three required pairs:

  * exact `Compare(OptionA, OptionB, ...)` has `GuardDecision = pass` and its own `ComparisonResultSlot` binds the justified tokens `OptionA ≼ OptionB` on latency and `OptionB ≼ OptionA` on cost;
  * exact `Compare(OptionA, OptionC, ...)` has `GuardDecision = degrade` because OptionC lacks the required risk attestation, and its output binding contributes no relation token about OptionC; and
  * exact `Compare(OptionB, OptionC, ...)` has the same explicit `degrade` basis and likewise contributes no relation token about OptionC.

  The Selector's `ComparisonResultSlot` argument is exactly the union of those justified member outputs, so its two tokens both trace to the `{A,B}` CPM application. No equality, worse-than, or `abstain` token is fabricated for OptionC.
* `MinimalEvidenceSlot?` is absent, so evidence is evaluated against `CGSpecSlot.MinimalEvidence`.
* The actual selection binds the three exact CPM applications and their pair, eligibility, and output bindings; the required-pair coverage and token trace; the deployment-option claim scope and selected regulatory `U.ContextSlice` members; the same predicate basis or explicit `none`; the reference plane and evaluation interval; and a `degrade` policy that permits exclusion of OptionC.

**Outcome.**

* Under that explicitly bound `degrade` policy, `SelectEligibility` returns `degrade`, excludes OptionC without coercing unknown evidence, and `SelectionSlot` returns `{OptionA, OptionB}`.
* If either required comparison involving OptionC instead had `GuardDecision = abstain`, that basis member would have no output binding, `SelectEligibility` would return `abstain`, and no selected-set value would be created. Neither guard value is a member of `ComparisonResultSlot` or `SelectionSlot`.
* The dated selection `U.Work`, actual `Select` application, finite CPM application basis, evidence-policy and `SelectionSlot` bindings, and A.10 evidence-provenance path preserve why the reduced-set branch proceeded and why the abstain branch did not.

#### A.19.SelectorMechanism:5.3 - Show, U.Episteme example

**Scenario.** A methods group selects a declared set of analysis methods for a task. Candidates are method family refs. The group wants diversity in the selected set, but does not want diversity metrics to silently become dominance criteria.

* `CandidateSetSlot` = `{Family1, Family2, Family3, Family4}`
* The selection conditions declare which binary method-family comparisons are required. A finite basis identifies every relied-on CPM application, its exact pair, eligibility value, and own output binding; the Selector's `ComparisonResultSlot` argument is their exact justified-token union.
* `TaskSignatureSlot` is present and is the single policy-default slot or ref:

  * `PortfolioMode` and dominance regime,
  * budgeting and telemetry hooks (when used).
* `CriteriaSlot` declares that diversity signals are telemetry unless explicitly promoted by policy.

**Outcome.**

* `SelectionSlot` returns a selected set; any archive‑style behavior is a specialization and policy choice, not a hidden kernel default.
* The dated selection `U.Work`, actual `Select` application with its `TaskSignatureRef.edition` and `SelectionSlot` bindings, and A.10 evidence-provenance path support later explanation without embedding tool tokens into the kernel.

---

