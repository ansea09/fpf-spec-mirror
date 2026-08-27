---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:5"
section_title: "Archetypal Grounding — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__007_archetypal-grounding-informative.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:5 — Archetypal Grounding — informative"
line_start: 33431
line_end: 33463
dependencies:
keywords:
  - "ComparatorSet"
  - "ComparatorSpecRef"
  - "comparator"
  - "comparison"
  - "partial order"
  - "set-valued comparison outcome"
  - "tri-state admissibility (pass"
---

### A.19.CPM:5 - Archetypal Grounding — informative

#### A.19.CPM:5.1 - Tell

Think of CPM as a declaration for a **replayable, relation-producing comparison operation**:

* Input: "two admitted profiles + an explicit comparator spec + declared admissibility and evidence declarations"
* Output: “a **set‑valued** relation outcome that preserves incomparability and uncertainty”

The key didactic boundary is: **CPM compares; it does not decide.**

#### A.19.CPM:5.2 - Show (U.System) — comparing two supplier options without faking a total order

A program manager compares Supplier‑A vs Supplier‑B for a safety‑critical component. The team tracks a profile of measures (cost, lead time, defect rate, assurance, sustainability), but not all measures are strictly comparable across regions (different reporting regimes, different units).

* The project has a declared `CN‑Spec` (admission and comparability declarations) and a declared `CG‑Spec` that lists admissible comparators in `ComparatorSet` and evidence rules in `MinimalEvidence`.
* The comparator is `ParetoDominanceComparatorSpecRef@edition`, declared in `CG-Spec.ComparatorSet`.
* The actual application binds the two supplier profiles; the claim scope `supplier options for the named component and procurement decision`; its selected regulatory and reporting `U.ContextSlice` members under A.2.6; `ComparisonPredicate = none` because Pareto dominance is supplied by the comparator; the stated procurement reference plane; and the explicit comparison interval.
* CPM runs `Compare(...)`; a changed component, scope member, comparator, plane, or interval is another comparison rather than an update to the same output.

  * If Supplier‑A is better in cost but worse in defect rate and incomparable on assurance due to missing evidence, CPM does **not** invent “A wins” or “A loses”.
  * `CompareEligibility` returns `degrade` or `abstain` under the evidence policy. On `abstain`, no comparison tokens are fabricated. When an explicit `degrade` policy permits a bounded partial comparison, `ComparisonResultSlot` contains only the justified relation tokens and preserves incomparability.
* The downstream `SelectorMechanism` can then return a selected set (e.g., keep both suppliers in the candidate set) rather than forcing a single winner by hidden tie‑break rules.

#### A.19.CPM:5.3 - Show (U.Episteme) — uncertainty‑aware comparison with set‑valued outcomes

A research lead compares two proposed methods for a system component. Both methods have performance estimates with uncertainty bounds (e.g., distributions or prediction intervals). The team uses a SoTA uncertainty quantification package (post‑2015 conformal families are a common example) to avoid overstating confidence.

* `USCM` produces score profiles that are interval‑valued (or otherwise uncertainty‑annotated) rather than point estimates.
* The chosen comparator is uncertainty‑aware and declared as a `ComparatorSpec` (edition‑pinned) in `CG‑Spec.ComparatorSet`.
* `CompareEligibility` returns its guard value separately. If comparison proceeds, CPM returns justified relation tokens such as `not worse` or `incomparable`; if it abstains, no `abstain` token is smuggled into `ComparisonResultSlot`.
* The dated comparison `U.Work`, actual `Compare` application with its effective comparator, evidence-policy, and `ComparisonResultSlot` bindings, and A.10 evidence-provenance path let later readers reproduce why the comparison abstained or degraded instead of mistaking missing evidence for equality.

