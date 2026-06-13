---
chunk_kind: "child"
pattern_id: "I.2"
pattern_title: "Expanded Entry Disambiguation Cases"
section_id: "I.2:section-010"
section_title: "Deprecations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/I.2/I.2__011_deprecations-normative.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "I.2 — Expanded Entry Disambiguation Cases"
  - "I.2:section-010 — Deprecations (normative)"
line_start: 84824
line_end: 84835
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

