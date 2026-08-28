---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__013_sota-echoing.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:11 — SoTA-Echoing"
line_start: 33629
line_end: 33649
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

### A.19.CPM:11 - SoTA-Echoing

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is **not** a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable CPM mechanism boundary.

Concrete comparator-family SoTA packages are cited through their current Part G pack or claim sheet when one governs the use. CPM's kernel semantics remain unchanged.

| SoTA practice pointer (post‑2015)                                                                                                   | How it connects to CPM                                                                                                                                           | Adoption status in FPF                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Fair ranking and constrained ranking** (e.g., Zehlike et al., 2017; Biega et al., 2018)                                             | Reinforces the “no hidden tie‑breaks and thresholds” stance: fairness constraints belong in explicit comparator and acceptance policies, not as silent kernel constants. | Integrate via `ComparatorSpec` editions in `CG‑Spec.ComparatorSet` + policy pins; CPM remains unchanged.              |
| **Uncertainty-aware and set-valued inference** (e.g., Romano et al., 2019; Barber et al., 2021)                                       | Supports “comparison may abstain” and “set‑valued outcomes are honest”: uncertain profiles should not be coerced into point‑comparisons.                         | Model as comparator families (or supporting method families) packaged in `G.2`; wired into declared `ComparatorSpec`. |
| **Differentiable sorting and learned comparators** (e.g., Grover et al., 2019; Blondel et al., 2020) | When comparators are learned, explicit comparator specs, edition and policy bindings in the actual operation application, its `ComparisonResultSlot` binding, and A.10 evidence-provenance become even more important for replay and drift control. | Treated as method implementations behind `ComparatorSpec` (wiring-only in Part G); CPM kernel stays stable. |
| **Robust multi‑criteria decision support under partial orders** (modern robust outranking and preference-learning variants post‑2015) | Emphasizes preserving incomparability and explicitly encoding thresholds and preferences as declared artifacts.                                                      | Packaged as comparator families; admissibility and evidence remain gated by `CG‑Spec`.                                     |

#### A.19.CPM:11.1 - Currentness and smallest reopen rule

**Qualification basis and window.** The stable kernel claim is qualified by the current editions of A.6.1/A.6.5 operation and slot discipline, A.19/A.18 space and scale semantics, A.19.CN comparability, G.0 comparator and evidence admissibility, A.2.6 scope semantics, and the exact current G.2 comparator pack or claim sheet cited by an actual use. For that use, the effective qualification window is the intersection of those bound editions' currentness and any validity interval declared by the comparator pack or claim sheet; `post-2015` is an orientation label, not an indefinite freshness claim.

**Reopen the CPM kernel only when.** Reopen the smallest affected CPM rule when a direct governor changes binary `Compare` application identity or bindings, `ComparisonResultSlot` kind, comparator admission, scale or normalization admissibility, tri-state eligibility, comparison scope, or the separation of output, evidence, provenance, and result epistemes, or when qualified evidence contradicts one of those kernel commitments. A new algorithm family, learned model, fairness constraint, uncertainty method, threshold, or robustness technique that still satisfies those commitments changes its G.2 pack, `ComparatorSpec`, `CG-Spec`, or policy binding rather than CPM.

**Smallest affected locus.** A signature or result-kind change reopens only the corresponding direct-signature, SlotSpec, or `OperationAlgebra` passage in `A.19.CPM:4.1`; an admissibility or failure-semantics change reopens the matching `LawSet` or `AdmissibilityConditions` clause. Update only the nearest exercising case in `A.19.CPM:5.2` or `:5.3` and the corresponding `CC-A19CPM` row. Source-family churn that changes no kernel commitment updates the direct pack or claim sheet and, when its summary is stale, only the affected row in this SoTA map.

