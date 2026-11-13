---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Selection Kernel"
section_id: "A.19.SelectorMechanism:5"
section_title: "Archetypal Grounding — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__007_archetypal-grounding-informative.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.SelectorMechanism — Selection Kernel"
  - "A.19.SelectorMechanism:5 — Archetypal Grounding — informative"
line_start: 40964
line_end: 41010
dependencies:
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.CPM"
  - "A.19.ULSAM"
  - "A.19.USCM"
  - "A.6.0"
  - "A.6.1"
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

### A.19.SelectorMechanism:5 - Archetypal Grounding — informative

#### A.19.SelectorMechanism:5.1 - Selection under partial comparisons

When comparisons are partial or set-valued, selection must not pretend there is a single best candidate by default. `SelectorMechanism` makes selection explicit, policy-bound, and replayable: it returns a set, including a singleton when the criteria determine one candidate.

#### A.19.SelectorMechanism:5.2 - Deployment options

**Scenario.** A platform team must pick a set of deployment options for a subsystem under multiple criteria: latency, cost, and regulatory risk. Comparisons are multi-criteria and do not induce a total order.

* `CandidateSetSlot = {OptionA, OptionB, OptionC}`.
* `CriteriaSlot` requires Pareto selection over the three unordered pairs `{A,B}`, `{A,C}`, and `{B,C}`, returns all non-dominated admissible candidates, and preserves the full selected set unless an explicit current criterion requires a singleton.
* The finite upstream comparison-application basis covers all three required pairs:

  * `Compare(OptionA, OptionB, ...)` has `GuardDecision = pass`: OptionB is strictly better than OptionA on latency, while OptionA is strictly better than OptionB on cost under the declared comparator. Its `ComparisonResultSlot` records those strict opposite wins, so neither dominates the other;
  * `Compare(OptionA, OptionC, ...)` has `GuardDecision = degrade` because OptionC lacks the required risk attestation. In this constructed case, the admitted comparator and partial-evidence policy define the empty token set as the lawful output for this restricted use; its output binding contributes no relation token about OptionC; and
  * `Compare(OptionB, OptionC, ...)` has the same `degrade` basis and likewise contributes no relation token about OptionC.

  The Selector's `ComparisonResultSlot` argument is the union of those justified member outputs, so its two tokens both trace to the `{A,B}` CPM application. No equality, worse-than, or `abstain` token is fabricated for OptionC.
* `MinimalEvidenceSlot?` is absent, so evidence is evaluated against `CGSpecSlot.MinimalEvidence`.
* The selection application binds the three CPM applications and their pair, eligibility, and output bindings; the required-pair coverage and token trace; the deployment-option claim scope and selected regulatory `U.ContextSlice` members; the same predicate basis or explicit `none`; the reference plane and evaluation interval; and a `degrade` policy that permits exclusion of OptionC.

**Outcome.**

* Under that bound `degrade` policy, `SelectEligibility` returns `degrade`, excludes OptionC without coercing unknown evidence, and `SelectionSlot` returns `{OptionA, OptionB}`.
* If either required comparison involving OptionC instead had `GuardDecision = abstain`, that basis member would have no output binding, `SelectEligibility` would return `abstain`, and no selected-set value would be created. Neither guard value is a member of `ComparisonResultSlot` or `SelectionSlot`.
* The selection or eligibility application, finite CPM application basis, policies and returned value or explicit absence preserve the branch taken. An A.10 provenance account is added for the bounded reliance at issue; any dated Work claim requires the independent grounds in §4.1.

#### A.19.SelectorMechanism:5.3 - Analysis-method families

**Scenario.** A methods group selects a declared set of analysis-method families for a task. Candidates are refs to those families. The group wants diversity in the selected set, but does not want diversity metrics to silently become dominance criteria.

* `CandidateSetSlot` = `{Family1, Family2, Family3, Family4}`
* The selection conditions declare which binary method-family comparisons are required. A finite basis identifies every relied-on CPM application, its pair, eligibility value, and own output binding; the Selector's `ComparisonResultSlot` argument is their justified-token union.
* `TaskSignatureSlot` is present and is the single policy-default slot or ref:

  * `PortfolioMode` and dominance regime,
  * budgeting and telemetry hooks (when used).
* `CriteriaSlot` declares that diversity signals are telemetry unless explicitly promoted by policy.

**Outcome.**

* `SelectionSlot` returns a selected set of those families; any archive‑style behavior is a specialization and policy choice, not a hidden kernel default.
* The `Select` application retains its `TaskSignatureRef.edition`, effective criteria and `SelectionSlot` bindings for later explanation. Add provenance and dated Work only under their independent grounds in §4.1.

---

