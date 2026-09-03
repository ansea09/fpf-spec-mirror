---
chunk_kind: "child"
pattern_id: "C.2.4"
pattern_title: "U.ArticulationExplicitness"
section_id: "C.2.4:17"
section_title: "Threshold Crossing and Split Handling"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.4/C.2.4__018_threshold-crossing-and-split-handling.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.2.4 — U.ArticulationExplicitness"
  - "C.2.4:17 — Threshold Crossing and Split Handling"
line_start: 44363
line_end: 44384
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.3.1"
  - "A.6.3.RT"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.P"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.5"
  - "C.2.LS"
  - "C.2.P.DR"
keywords:
  - "articulation explicitness"
  - "early repair readiness"
  - "explicitness"
  - "semantic shape"
  - "under-articulated cue"
---

### C.2.4:17 - Threshold Crossing and Split Handling

#### C.2.4:17.1 - Branch-aware high-articulation exits
At `AE3+`, use the local threshold of the direct branch rather than one universal destination:

- for an actual relation claim, use `A.6.P` to restore relation precision and then return the claim to its direct relation pattern;
- for a plan or intended activity, use `A.15`;
- for a Method, use `A.3.1`, while its MethodDescription remains an episteme under `C.2.1`;
- for an admitted dated Work occurrence, use `A.15.1`;
- for a representation claim, use `C.2.P.DR`, adding `A.6.3.RT` only when a representation transition is current;
- for an abductive prompt or explicit open question, use `B.5.2.0` or the direct question pattern;
- for a Characteristic or Scale claim, use `A.17` and `A.18`, with `C.16.P` when its scalar wording hides the construction;
- for an ordinary domain claim, keep the episteme publication under `C.2.1` and use the direct domain pattern that governs its subject.

If the branch or threshold is unresolved, keep the episteme in `B.4.1` or `A.16.1` and state what is still missing. `AE` reports recoverable articulation; it does not itself choose the branch or authorize the receiving use.

#### C.2.4:17.2 - High-articulation, low-closure cases
A note may reach `AE4+` while remaining low or mid in `CD`. In such cases state that articulation is sufficient for precise handling while closure still leaves rival routes or frames live.

#### C.2.4:17.3 - Split-publication rule
If one note contains a high-`AE` fragment and a low-`AE` remainder, split the publication rather than assigning one averaged level that hides the actual route structure.

