---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Selection Kernel"
section_id: "A.19.SelectorMechanism:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__011_consequences.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.SelectorMechanism — Selection Kernel"
  - "A.19.SelectorMechanism:9 — Consequences"
line_start: 41064
line_end: 41080
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

### A.19.SelectorMechanism:9 - Consequences

**Benefits**

* Preserves incomparable candidates when the criteria require them.
* Makes thresholds, weights and scalarization choices inspectable; correct selection still depends on applying the admitted criteria to the justified inputs.
* Supports replay through application bindings and the relations that the receiving use consumes.
* Supports evolvability: new method families and selection styles can be wired without changing the kernel signature.

**Costs and trade-offs**

* Selected-set results can require downstream handling when a single decision is needed.
* Evidence discipline increases early `degrade` or `abstain` until criteria and evidence policies are explicit.
* Teams must make the selection criteria recoverable; existing descriptions may already suffice.

---

