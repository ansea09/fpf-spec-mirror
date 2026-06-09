---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:5"
section_title: "Archetypal Grounding — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__007_archetypal-grounding-informative.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:5 — Archetypal Grounding — informative"
line_start: 27657
line_end: 27703
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

When comparisons are partial or set‑valued, selection must not pretend there is a single “best” by default. `SelectorMechanism` makes selection explicit, policy‑bound, and auditable: it returns a **set** unless criteria explicitly demand otherwise.

#### A.19.SelectorMechanism:5.2 - Show, U.System example

**Scenario.** A platform team must pick a set of deployment options for a subsystem under multiple criteria: latency, cost, and regulatory risk. Comparisons are multi‑criteria and do not induce a total order.

* `CandidateSetSlot` = `{OptionA, OptionB, OptionC}`
* `ComparisonResultSlot` includes tokens such as:

  * `OptionA ≼ OptionB` on latency,
  * `OptionB ≼ OptionA` on cost,
  * `OptionC` incomparable with both on risk evidence (missing attestations).
* `CriteriaSlot` contains explicit clauses:

  * “return all non‑dominated candidates under ParetoOnly,”
  * “candidates missing required evidence must not pass.”
* `MinimalEvidenceSlot?` is absent, so evidence is evaluated against `CGSpecSlot.MinimalEvidence`.

**Outcome.**

* `SelectEligibility` returns `degrade` (or `abstain`, depending on the declared failure behavior) **because** `OptionC` fails evidence gating; selection excludes `OptionC` under an explicit policy route rather than coercing unknowns.
* `SelectionSlot` returns `{OptionA, OptionB}` as a selected set, rather than forcing a single winner.
* `Audit` records `CGSpecRef.edition`, the effective evidence policy, and the stable identity of the selected set result.

#### A.19.SelectorMechanism:5.3 - Show, U.Episteme example

**Scenario.** A methods group selects a declared set of analysis methods for a task. Candidates are method family refs. The group wants diversity in the selected set, but does not want diversity metrics to silently become dominance criteria.

* `CandidateSetSlot` = `{Family1, Family2, Family3, Family4}`
* `ComparisonResultSlot` is produced by lawful comparison on declared indicators and evidence gates.
* `TaskSignatureSlot` is present and is the single routing slot/ref for policy defaults:

  * `PortfolioMode` and dominance regime,
  * budgeting/telemetry hooks (when used).
* `CriteriaSlot` declares that diversity signals are telemetry unless explicitly promoted by policy.

**Outcome.**

* `SelectionSlot` returns a selected set; any archive‑style behavior is a specialization and policy choice, not a hidden kernel default.
* `Audit` records `TaskSignatureRef.edition`, enabling reproducibility and post‑hoc explanation without embedding tool tokens into the kernel.

---

