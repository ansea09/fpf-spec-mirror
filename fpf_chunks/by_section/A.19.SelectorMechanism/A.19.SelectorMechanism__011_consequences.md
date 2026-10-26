---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__011_consequences.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:9 — Consequences"
line_start: 39186
line_end: 39202
dependencies:
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.CPM"
  - "A.19.ULSAM"
  - "A.19.USCM"
  - "A.6.1"
  - "A.6.5"
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

### A.19.SelectorMechanism:9 - Consequences

**Benefits**

* Preserves incomparable candidates when the criteria require them.
* Makes thresholds, weights and scalarization choices inspectable; correct selection still depends on applying the admitted criteria to the justified inputs.
* Supports replay through actual application bindings and the direct relations that the receiving use consumes.
* Supports evolvability: new method families and selection styles can be wired without changing the kernel signature.

**Costs and trade-offs**

* Selected-set results can require explicit downstream handling when a single decision is needed.
* Strict evidence discipline increases early `degrade` or `abstain` until criteria and evidence policies are explicit.
* Teams must make the selection criteria recoverable; existing descriptions may already suffice.

---

