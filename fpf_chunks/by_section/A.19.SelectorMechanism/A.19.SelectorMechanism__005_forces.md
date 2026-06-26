---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__005_forces.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:3 — Forces"
line_start: 29148
line_end: 29167
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

5. **Auditability vs conceptual minimalism.** FPF stays conceptual. Audit obligations must be minimal yet decisive: editions and effective policy references must be visible without introducing tool‑level governance.

6. **Evolvability vs didactic usability.** The kernel must be stable enough to support SoTA wiring and specialisation chains, but also teachable: one place to learn the boundary, laws, guard behavior, and audit minimum.

7. **Planned slot filling and gate and guard separation.** Planned fillers and pins live in `SlotFillingsPlanItem` rows. Selection must not mutate into a gate pattern: no `GateDecision` or decision logs inside the mechanism boundary.

8. **No competing defaults.** If defaults exist (for `PortfolioMode`, dominance regime, archive policies), they must be cited from their declared defaults sources, not replicated or re-declared inside the kernel (`A.19.CHR:4.3.5`).

---

