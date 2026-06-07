---
chunk_kind: "child"
pattern_id: "J.4"
pattern_title: "First Practical Entry Neighborhood Index"
section_id: "J.4:section-006"
section_title: "Deprecations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/J.4/J.4__007_deprecations-normative.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "J.4 — First Practical Entry Neighborhood Index"
  - "J.4:section-006 — Deprecations (normative)"
line_start: 82684
line_end: 82695
dependencies:
keywords:
---

### Deprecations (normative)

The following terms **MUST NOT** name scope objects in normative text, guards, or conformance blocks:

* *applicability*, *envelope*, *generality*, *capability envelope*, *validity* (as a characteristic name).

Use instead:

* **`U.ClaimScope`** (*Claim scope*, nick **G**) for epistemes;
* **`U.WorkScope`** (*Work scope*) for capabilities;
* **`U.Scope`** only when explaining the abstract mechanism (not in guards).

