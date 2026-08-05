---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__005_forces.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:3 — Forces"
line_start: 33150
line_end: 33171
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

### A.19.SelectorMechanism:3 - Forces

1. **Set‑valued reality vs single‑winner convenience.** Many admissible comparisons are partial orders. The kernel must preserve set‑valued semantics while still allowing single‑winner outcomes when explicitly requested by criteria.

2. **Policy primacy vs method freedom.** Criteria and defaults must be explicit and policy‑bound, while multiple method families and decision styles must remain add‑able without mutating the kernel.

3. **No hidden thresholds vs usability pressure.** Engineers often want “just pick one.” If the spec does not constrain this, hidden thresholds and tie‑breakers become de facto policy.

4. **Evidence discipline vs delivery pressure.** Under uncertainty, teams default to coercion (unknown → pass). The kernel must enforce tri‑state eligibility and fail‑closed discipline.

5. **Replayability vs conceptual minimalism.** The mechanism declaration stays small, while dated selection work, the actual `Select` application and its argument and `SelectionSlot` bindings, and the evidence-provenance path retain the effective editions, policies, candidates, and selected set needed for replay.

6. **Evolvability vs didactic usability.** The kernel must be stable enough to support SoTA wiring and specialisation chains, but also teachable: one place states the mechanism boundary, laws, eligibility behavior, and the neighboring replay basis for realized use.

7. **Planned slot filling and gate and guard separation.** Planned fillers and pins live in `SlotFillingsPlanItem` rows. Selection must not mutate into a gate pattern: no `GateDecision` or decision logs inside the mechanism boundary.

8. **No competing defaults.** If defaults exist for `PortfolioMode`, dominance regime, or archive policy, cite their declared sources rather than re-declaring them in the kernel.

9. **Scope continuity vs legitimate reselection.** Selection may narrow candidates or apply explicit policy, but it may not silently change the finite upstream comparison-application basis, its required pair coverage, any member's predicate basis, claim scope, selected context slices, reference plane, or evaluation window. A justified change is a new selection application and may require new binary comparisons.

---

