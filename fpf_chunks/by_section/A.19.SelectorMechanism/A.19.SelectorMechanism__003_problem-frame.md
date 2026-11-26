---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Selection Kernel"
section_id: "A.19.SelectorMechanism:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__003_problem-frame.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "A.19.SelectorMechanism — Selection Kernel"
  - "A.19.SelectorMechanism:1 — Problem frame"
line_start: 40877
line_end: 40891
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

### A.19.SelectorMechanism:1 - Problem frame

FPF’s Characterization (CHR) suite treats selection as a **mechanism boundary** within the suite (authoritative membership: `A.19.CHR:4.2`).
Suite membership is a **set**; order has no semantics. Any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under suite obligations (`A.19.CHR:4.3`).

Within the suite‑closed protocol, `SelectorMechanism` appears as the `select` stage (after admissible comparison; optional stages remain optional per `suite_protocols`). Under CN-Spec and CG-Spec, the declared `Select` operation:

* consumes **admissible** comparison outcomes without collapsing them into a hidden scalar,
* applies **explicit** criteria and policy references, and
* returns a **selected-set** result under policy-bound defaults, with the `Select` application and its argument and result bindings recoverable; dated Work and evidence-provenance grounds enter when the account asserts them or the receiving use consumes them.

The kernel uses the CHR suite SlotKind lexicon (`A.19.CHR:4.2.1`) to prevent SlotKind drift in specializations and SoTA wiring modules.

---

