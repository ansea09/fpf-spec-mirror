---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Choose and Check an Aggregation Law for the Intended Result"
section_id: "A.9:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__007_conformance-checklist.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "A.9 — Choose and Check an Aggregation Law for the Intended Result"
  - "A.9:6 — Conformance Checklist"
line_start: 27724
line_end: 27734
dependencies:
  - "A.19.CN"
  - "A.19.ULSAM"
  - "B.1"
  - "B.2"
  - "C.29"
keywords:
  - "aggregation law"
  - "bounds"
  - "cross-scale consistency"
  - "dependency model"
  - "intended result"
  - "ordered composition"
  - "singleton identity"
---

### A.9:6 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| **CC-A9-1** | Name the intended result, inputs and the subject conditions that justify the law or bound used to answer the question. Add Characteristic, Scale and any applicable units for the quantitative branch; recover measurement conditions when it uses measured values. | Recover what the result means without excluding non-quantitative composition. |
| **CC-A9-2** | Select only the property needed by the current action and supply its applicable argument or warranted test. Distinguish singleton identity from idempotence and repeated-source handling. | Avoid a compulsory universal algebra. |
| **CC-A9-3** | Claim order or partition independence only under the model and recombination/numerical conditions. | Preserve lawful sequential or parallel composition. |
| **CC-A9-4** | Use a weakest-part bound only for a result and dependency model that justify it; distinguish a bound from a calculated value. | Prevent both unsupported optimism and a false universal cap. |
| **CC-A9-5** | Return the conclusion warranted for the intended use. If a proven bound settles the threshold, give that decision. If the requested value or decision remains open, give the useful conclusion and the premise still needed. Reopen a conclusion when its supporting condition fails. | Answer a threshold decision even when the exact aggregate remains unknown. |
| **CC-A9-6** | A claimed Meta-Holon Transition satisfies B.2's existing-whole comparison and the candidate whole's identity rule. | Keep reidentification independent of a model failure. |

