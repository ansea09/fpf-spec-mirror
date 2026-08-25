---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__003_intent.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:1 — Intent"
line_start: 49608
line_end: 49643
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:1 - Intent

Operationalise No-Free-Lunch discipline in selection by making each selector decision use a typed `TaskSignature`, not a paragraph. A problem reaches C.22 when its problem-side episteme is stable enough to constitute and assign that declaration without selecting a method in advance. The signature is the smallest CHR-typed A.6.0 declaration sufficient for eligibility, acceptance, and policy-governed selection without inadmissible arithmetic or silent coercions.

#### C.22:1.1 - Term split used in this pattern

- `TaskSignature` assignment means one obtaining `TaskSignatureAssignmentRelation` among an exact problem-side episteme, exact TaskSignature, and exact receiving-use episteme; it does not pre-bind a method.
- `ScopeSlice(G)` means the exact A.2.6 claim-scope relation used by this declaration; it is not an evidence-path slice, baseline-set slice, container, or assignment participant.
- `threshold` is not one undifferentiated family here:
  - articulation and closure thresholds stay with cue or prompt subject patterns such as `B.4.1` and `B.5.2.0`;
  - acceptance-gate thresholds stay with `G.4`;
  - a work-measure threshold target used in a specialization claim is only the declared success mark for that task family or work target.

**Name and kind map for code-shaped heads.** The names below identify different structural positions; capitalization does not make them peer kinds.

| Head used in this pattern | Recoverable kind or position | Direct governance boundary |
| --- | --- | --- |
| `TaskSignature` | C.2.1 episteme and species of `U.Signature`; this pattern's primary EntityOfConcern | C.22 governs its A.6.0 direct fields, Vocabulary, Laws, and Applicability; C.2.1 governs constitution; E.17 governs publications and carriers. |
| `ProblemSideEpistemeRef` and `ReceivingUseEpistemeRef` | Participant designations in an assertion or description of `TaskSignatureAssignmentRelation`, not content or identity positions of TaskSignature | C.22.2 or the direct problem-side pattern defines or constrains the first episteme; the receiving-use episteme states the use but does not prove that an assignment obtains. |
| `TaskKind` | TaskSignature position filled by one exact C.3 `U.Kind` value that types the current task or work target | C.3 governs the kind value; the field does not mint `U.Task`. |
| `TaskFamilyRef` | Optional reference position for the comparison-relevant task family | C.22 and C.22.1 govern task-family anchoring; the reference is not the family or a selected method. |
| `ProblemProfile` | C.2.1-conformant `U.Episteme` that describes the stabilized problem and may reference the TaskSignature assignment | It is not the actual Problem, TaskSignature, assignment relation, method, plan, or Work occurrence. |
| `ScopeSlice(G)` | Local position whose filler is the current A.2.6 claim-scope relation over the exact `EntityOfConcernRef` | A.2.6 governs membership; the position is not an E.18 path slice or a new slice kind. |
| CHR field heads in `5.1` | TaskSignature positions filled by characteristics, scales, units, polarity values, scope values, evidence relations, and currentness conditions | C.16 and each subject-pattern locator identify the exact definitions and constraints for the fillers; C.22 states why the selector-facing use needs them. |
| QD and OEE extension heads in `5.1` | Optional TaskSignature positions filled by exact characteristic-space, archive, policy, telemetry, generator-family, validity-region, and transfer-rule values or references | C.18, C.19, G.5, G.11, and the named direct patterns keep authority over those fillers. `ArchiveConfig`, `TelemetryHooks`, and `GeneratorIntent` do not become root kinds here. |

#### C.22:1.2 - ProblemCard relation

`ProblemCard` is the C.22.2 C.2.1 episteme used to stabilize one problem-side representation before downstream Principles-to-Work.

A ProblemCard can prepare `TaskKind`, scope, and characteristic bindings for a candidate TaskSignature. Assignment obtains only when one signature is adequate for the named receiving use. If several signatures remain plausible, keep them as candidates under the selection or problem-framing pattern rather than asserting one assignment occurrence.

`TaskSignatureAssignmentRelation` moves no card claim into the TaskSignature. The signature keeps only its A.6.0 declaration content; the card remains the reviewable problem-side episteme that explains why this problem can proceed to characterization, comparison, search, refresh, retirement, or another subject pattern.

The corresponding claims remain with their named subject patterns.

