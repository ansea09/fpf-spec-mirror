---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:7"
section_title: "Author Standard (at a glance)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__009_author-standard-at-a-glance.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:7 — Author Standard (at a glance)"
line_start: 47632
line_end: 47647
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:7 - Author Standard (at a glance)

Begin with what the recipient must learn from the relation account.

1. **State or choose the relation.** Work from the question to the relevant participants, their relation and its conditions. Say, for example, “Impeller ComponentOf Pump” for an assembly claim, or “Vehicle 12 belongs to Fleet North under its registration rule” for an enrolment claim. Establish the asserted relation under its defining rule. For a broader conclusion, explain how the required assertions combine. When the supported readable claim completes the commission and the profile has not been elected, publish it directly.

2. **When CT2R-LOG is elected, attach `tv:groundedBy`**:

   * Structural parthood → the applicable current construction trace and `validationMode=axiomatic`.
   * Collection belonging under the collection's own rule → one current `C.13 set` trace and `validationMode=axiomatic`.
   * Another permitted epistemic or constitutive claim → the evidence object, argument or qualifying C.13 account used, with its corresponding mode from :4.
3. **Declare the selected `tv:validationMode`** for every covered claim.


> The public graph retains its relation vocabulary. For each assertion covered by the profile, a reviewer can follow the grounding reference to its construction or evidence account.

