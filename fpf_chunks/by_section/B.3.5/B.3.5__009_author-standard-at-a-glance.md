---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:7"
section_title: "Author Standard (at a glance)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__009_author-standard-at-a-glance.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:7 — Author Standard (at a glance)"
line_start: 40176
line_end: 40192
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:7 - Author Standard (at a glance)

When you add or import a relation edge:

1. **Pick a Working-Model relation sentence** such as “Impeller ComponentOf Pump” or “Vehicle 12 belongs to Fleet North under its registration rule”; avoid raw `ut:PartOf` unless you are drafting meta-level axioms. If no current publication choice or requirement elects CT2R-LOG, publish that direct claim and stop.

2. **When CT2R-LOG is elected, attach `tv:groundedBy`**:

   * Structural parthood → the applicable current construction trace and `validationMode=axiomatic`.
   * Collection belonging under the collection's own rule → one current `C.13 set` trace and `validationMode=axiomatic`.
   * Another permitted epistemic or constitutive claim → the branch's logical argument or evidence object and allowed mode.
3. **Declare the selected `tv:validationMode`** for every covered claim.


> **What managers see:** nothing new in the graph picture.
> **What auditors get:** a reliable trail from every edge covered by the elected profile back to its inspectable construction or evidence account.

