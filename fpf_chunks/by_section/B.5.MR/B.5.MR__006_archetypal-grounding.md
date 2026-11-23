---
chunk_kind: "child"
pattern_id: "B.5.MR"
pattern_title: "Compare Models by Refinement and Abstraction"
section_id: "B.5.MR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MR/B.5.MR__006_archetypal-grounding.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "B.5.MR — Compare Models by Refinement and Abstraction"
  - "B.5.MR:5 — Archetypal Grounding"
line_start: 51036
line_end: 51047
dependencies:
  - "B.1"
  - "B.5.FM"
  - "B.5.TC"
  - "C.2.1"
  - "C.37.MM"
keywords:
---

### B.5.MR:5 - Archetypal Grounding

A project commissions a temperature recorder for one installation. The earlier specification permits records at whole-minute intervals of one or two minutes. The new specification permits only one-minute intervals and preserves the units, clock and operating conditions. A one-minute record is still eligible. A two-minute record is excluded. For the inquiry about permitted sampling intervals, this is strict refinement. If the recipient asks only whether every hour contains a reading, both specifications give the same answer. Whether the installed recorder met its specification last night requires observations of that recorder.

Suppose a receiving comparison needs to know whether each recorder specification ensures at least one reading in every hour, without deciding between one-minute and two-minute intervals. Reuse the earlier specification as an abstraction of the one-minute specification. Every completion of the latter still satisfies the former, and both permit a completion. The abstract specification retains the hourly conclusion over all its permitted intervals. It no longer entails that the interval is one minute. For an inquiry that distinguishes the intervals this is strict abstraction. For the hourly inquiry the answers remain equivalent.

Now consider two recorders required to use the same interval, either one or two minutes. Describing each by its allowed intervals and allowing the settings to vary independently admits the former pairs (1,1) and (2,2), as well as (1,2) and (2,1). For the inquiry about permitted pairs this is a strict abstraction. Each recorder still supplies an hourly reading under either setting. If the recipient must also be sure the intervals match, retain the common setting while leaving its value open. Both comparisons concern the same two recorders. The difference lies in what the models permit.

A work method screens requests under a criterion and then refers unresolved ones for a second judgement. A local revision adds a deadline to the referral while preserving the screening rule. A referral after the deadline was admissible under the earlier timing rule and now falls outside the local prescription. A second revision silently accepts some requests previously requiring referral. Compare that changed decision with the original rule before relying on it. An excellent record of one compliant case cannot settle the claim for the newly admitted cases.

To compare the local method with methods at other sites for their screening and referral duties, return to the prescription without the local deadline. It is an abstraction if every performance permitted by the local prescription satisfies it and at least one such performance is possible. The referral duty remains; the local deadline no longer follows. Removing that deadline from the model does not withdraw an actual site's deadline or establish that its workers performed the referral. Those are different assertions needing their own grounds.

