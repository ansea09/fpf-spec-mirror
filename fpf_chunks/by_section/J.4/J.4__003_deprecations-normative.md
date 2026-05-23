---
chunk_kind: "child"
pattern_id: "J.4"
pattern_title: "First Practical Entry Neighborhood Index"
section_id: "J.4:section-002"
section_title: "Deprecations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/J.4/J.4__003_deprecations-normative.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "J.4 — First Practical Entry Neighborhood Index"
  - "J.4:section-002 — Deprecations (normative)"
line_start: 75261
line_end: 75272
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

