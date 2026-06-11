---
chunk_kind: "child"
pattern_id: "B.2"
pattern_title: "Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes"
section_id: "B.2:6.5"
section_title: "Certification Interface Example (Informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2/B.2__008_certification-interface-example-informative.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "B.2 — Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes"
  - "B.2:6.5 — Certification Interface Example (Informative)"
line_start: 31102
line_end: 31112
dependencies:
  - "A.1"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.x"
  - "B.2.x"
  - "B.3"
  - "B.4"
keywords:
  - "MHT"
  - "emergence"
  - "meta-system"
  - "new whole"
  - "synergy"
  - "system of systems"
---

### B.2:6.5 - Certification Interface Example *(Informative)*

Conceptual signature (notation‑neutral):

```
certify(role, context, window, snapshot, options) → StateAssertion
```

**Sketch.** `snapshot` contains coordinates over the Role’s RCS (A.19). `options` may reference named **NormalizationMethod(s)**/**NormalizationMethodInstance(s)** and overlays used in evaluation. The resulting **StateAssertion** states the target state (by name), the checklist applied (by name), the verdict, the window, and (if used) the **declared** **Bridge** or **NormalizationMethodInstance** employed for translation.
**Intent.** This example aids implementers; **normative constraints** on comparability, normalization, and evidence live in **A.19** and **C.16**, not here.

