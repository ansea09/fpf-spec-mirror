---
chunk_kind: "child"
pattern_id: "C.41.QC"
pattern_title: "Qualify Checklist Criteria and Checking Means"
section_id: "C.41.QC:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.41.QC/C.41.QC__006_archetypal-grounding.md"
commit_sha: "64ebce216e1be91beb67120d83f4308a42795eaf"
heading_path:
  - "C.41.QC — Qualify Checklist Criteria and Checking Means"
  - "C.41.QC:5 — Archetypal Grounding"
line_start: 89252
line_end: 89277
dependencies:
  - "A.10"
  - "C.41"
  - "C.41.SR"
  - "C.41.UA"
keywords:
---

### C.41.QC:5 - Archetypal Grounding

A team describes an importer as preserving item identifiers, reporting duplicate identifiers and retaining the previous catalogue when parsing fails. The description embodies assumptions about the team's use. A proposed generated check asks only whether an input file was accepted.

That check establishes none of the three described properties. A17 can become 1 during an otherwise successful import. A successful run also says nothing about duplicate reporting or the state after a parse failure.

The team constructs these qualification cases:

| Case | Distinction to establish | Observation capable of supporting it |
| --- | --- | --- |
| Valid catalogue with identifier A17 | Identifier preserved, rather than replaced or normalized unexpectedly. | Compare the input identifier with the stored identifier for the corresponding item. |
| Two records with the same identifier | The described duplicate report occurs for that input. | Inspect the returned report and its association with the duplicate records. |
| Malformed input with a known prior catalogue | Parse failure leaves the prior catalogue intact. | Observe the failure and compare the relevant catalogue state before and after it. |

These are three separate questions. A candidate checker that observes only an exit code cannot settle the third unless an independently established relation makes that code sufficient for the stated use. The team tests its proposed before/after comparison against a deliberately altered catalogue and an unchanged one. If it passes both, it has failed the intended discrimination; if it distinguishes them, that supports the comparison for those cases.

Complement that changed-catalogue challenge with a changed-question challenge. Use a constructed fixture whose before and after catalogues are both C. For these fixed facts, “Are the before and after catalogue contents identical?” has the expected answer **Yes**, while “Do the after contents differ from the before contents?” has the expected answer **No**. “Do both snapshots contain the same catalogue content?” preserves the first question and therefore its expected Yes. These answers follow from the fixture before any checker is run. A checker that returns the same verdict for the opposite conditions misses the question; one that changes the first answer merely because it is reworded is unstable on that case. Passing these contrasts supports only this bounded discrimination.

To examine grouped judging, give a model the same before and after snapshots C, plus a report headed “Import summary”. Before any output, content identity has expected **Yes**, and the presence of that heading has its separate expected **Yes**. Compare the identity verdict when asked alone and when asked alongside the heading question, with the same evidence supplied. The extra question changes neither snapshot nor the identity predicate. Repeat the contrast with a fixture whose after snapshot changes A17 to 1: identity is then **No** in both arrangements, while the heading answer stays Yes. If grouping changes either identity verdict, investigate or restrict that arrangement; do not average the two distinct questions into a pass. Combining repeated identity verdicts still has to answer to these fixture facts. Where grouped judging preserves the needed distinctions at lower cost, keep it. For actual stored data, an adequate direct comparison remains the cheaper starting choice.

A known malformed-input case with an unobserved post-state remains unresolved. Tool failure is not an importer failure or success. Local parser correctness does not settle the encompassing response and catalogue state; C.41.SR connects those contributions.

For the workshop display, “readable” may be judged from a desktop preview while participants will read the projected content from the back of a room. Qualification varies the viewing condition relevant to the exercise and asks a representative participant to interpret the actual content. A font-size threshold can be a useful local proxy only if its basis supports that use. Reconsider that proxy if glare or contrast makes text unreadable despite the chosen size.

Both examples are constructed probes. They illustrate how to challenge a claim, not measured checker performance.

