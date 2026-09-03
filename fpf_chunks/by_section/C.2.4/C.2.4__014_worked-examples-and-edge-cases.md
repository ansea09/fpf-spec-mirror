---
chunk_kind: "child"
pattern_id: "C.2.4"
pattern_title: "U.ArticulationExplicitness"
section_id: "C.2.4:13"
section_title: "Worked Examples and Edge Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.4/C.2.4__014_worked-examples-and-edge-cases.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "C.2.4 — U.ArticulationExplicitness"
  - "C.2.4:13 — Worked Examples and Edge Cases"
line_start: 44302
line_end: 44315
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

### C.2.4:13 - Worked Examples and Edge Cases

#### C.2.4:13.1 - High formality, low articulation
A template may be syntactically precise and therefore high in `F`, yet still low in `AE` because the actual participants, field meanings, bearer, planned action, admitted Work occurrence, reliance move, evaluator, or ordinary domain meaning remains unclear. A local system-role kind, classification, or assignment is selected only after evidence supports that branch. Formal-looking language does not make its semantic route recoverable.

#### C.2.4:13.2 - Plain plan, high articulation
The note `At 14:00, Maintenance Team 2 will isolate Pump P-17, replace Seal S-4, and restore service only after Leak Test LT-9 passes` uses ordinary language and little formal notation. It can still reach `AE4`: the planned actor, affected entity, ordered actions, time, and completion condition are explicit enough for the planning branch. It routes to `A.15`; it is not yet an `A.15.1` Work occurrence and needs no relation repair merely to count as explicit.

#### C.2.4:13.3 - Relation-looking but wrongly routed
A row `Maintenance Team 2 | Pump P-17 | isolate | 14:00` looks slot-shaped. If it records intended action, however, it is a compact plan row rather than proof of a durable relation. Its layout does not raise `AE` until the planning meaning and conditions are recoverable, and it does not select `A.6.P`.

#### C.2.4:13.4 - Threshold edge case
A cue with a stable trigger and candidate anchors may still sit between `AE2` and `AE3` because its direct branch is unresolved. Keep it in `B.4.1` or `A.16.1`, state what is missing, and apply the threshold of the branch eventually selected rather than a universal relation threshold.

