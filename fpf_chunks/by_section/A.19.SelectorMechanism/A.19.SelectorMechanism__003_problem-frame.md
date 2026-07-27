---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__003_problem-frame.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:1 — Problem frame"
line_start: 32728
line_end: 32742
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

### A.19.SelectorMechanism:1 - Problem frame

FPF’s Characterization (CHR) suite treats selection as a **distinct mechanism boundary** within the suite (authoritative membership: `A.19.CHR:4.2`).
Suite membership is a **set**; order has no semantics. Any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under suite obligations (`A.19.CHR:4.3`).

Within the suite‑closed protocol, `SelectorMechanism` appears as the `select` stage (after admissible comparison; optional stages remain explicitly optional per `suite_protocols`). The kernel’s role is concept‑level and governed by CN‑Spec and CG‑Spec:

* consume **admissible** comparison outcomes without collapsing them into a hidden scalar,
* apply **explicit** criteria and policy references, and
* return a **selected-set** result whose defaults are policy‑bound and auditable.

The kernel uses the CHR suite SlotKind lexicon (`A.19.CHR:4.2.1`) to prevent SlotKind drift across specializations and across SoTA wiring layers.

---

