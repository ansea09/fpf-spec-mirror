---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__002_use-this-when.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:0 — Use this when"
line_start: 34918
line_end: 34940
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "A.6.1"
  - "A.6.4"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "E.17"
  - "E.18"
  - "E.20"
  - "F.9"
  - "G.11"
keywords:
---

### A.20:0 - Use this when

Use A.20 when one transformation, one operation application, or one A.6.4 claim that a retargeting is fit for a stated use is current in a transformation-flow structure and the question is whether that subject satisfies one named internal constraint for one stated case.

**First useful move.** Write one sentence:

> For subject S and case facts I, constraint C is applicable and required; test T returned outcome O under window W, with witness or reason R.

**Quick worked case.** `TemperatureConversion-7` must add 273.15 to a Celsius input and must not return a value below 0 K. For input 25 °C, the test returns 298.15 K, so both required conditions are `satisfied`; the witness records the formula edition, input, output, and test result for this evaluation window. The practitioner may reuse this result for that case and window, or pass it to a current gate or assurance use; changed input, formula edition, assumptions, or window requires another check. If the output were 297.15 K, the formula condition would be `violated`; if no output could be recovered, it would be `unknown`; if the test had not run, its evaluation state would be `notRun`.

Stop after that result unless a gate, assurance argument, publication, or another named task needs it. Path and crossing structure, refresh, gate decisions, evidence, assurance, Work, and semantic bridges keep their own patterns.
**What goes wrong if missed.** A class label or green status replaces the actual constraint and test. An unknown or unrun required check disappears inside `pass`. A failed local constraint makes unrelated gate-fit facts look inapplicable. A.20 then starts redefining paths, publications, refresh, gates, or retargeting instead of reporting its own result.

**What this buys.** A practitioner can see which constraint was tested, why it applied, what case was used, what the result means, and which later decision may consume it.

**Not this pattern when.**

- Use `A.21` for a gate decision or profile consequence.
- Use `E.18` for transformation-flow positions, paths, crossings, valuations, or `PathSlice` identity.
- Use `E.17` for publication forms and faces, `G.11` for refresh work, and `C.27` for temporal-claim adequacy.
- Use `A.6.4` for retargeting semantics and `F.9` only for a separately claimed semantic correspondence.
- A `Signature`, WorkPlan, dated Work, or gate check does not enter A.20 merely because it occupies an E.18 position; use the pattern that defines the actual claim.

