---
chunk_kind: "child"
pattern_id: "J.4"
pattern_title: "First Practical Entry Pattern-Comparison Index"
section_id: "J.4:section-008"
section_title: "Deprecations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/J.4/J.4__009_deprecations-normative.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "J.4 — First Practical Entry Pattern-Comparison Index"
  - "J.4:section-008 — Deprecations (normative)"
line_start: 82991
line_end: 83002
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

