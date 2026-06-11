---
chunk_kind: "child"
pattern_id: "I.2"
pattern_title: "Expanded Entry Disambiguation Cases"
section_id: "I.2:section-010"
section_title: "Deprecations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/I.2/I.2__011_deprecations-normative.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "I.2 — Expanded Entry Disambiguation Cases"
  - "I.2:section-010 — Deprecations (normative)"
line_start: 83688
line_end: 83699
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

