---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__003_intent.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:1 — Intent"
line_start: 49850
line_end: 49885
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
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:1 - Intent

Operationalise No-Free-Lunch discipline in selection by making each selector decision use a typed `TaskSignature@Context`, not a paragraph. A problem reaches C.22 when its problem-side episteme is stable enough to construct and assign that signature without selecting a method in advance. The signature is the smallest CHR-typed A.6.0 declaration sufficient to support eligibility, acceptance, and policy-governed selection without inadmissible arithmetic or silent coercions; the separate assignment relation states which problem-side episteme and receiving use rely on it.

#### C.22:1.1 - Term split used in this pattern

- `TaskSignature` assignment means relating one `TaskSignature@Context` value to one exact problem-side episteme and one receiving selection use through `TaskSignatureAssignmentRelation@Context`; it does not pre-bind a method.
- `ScopeSlice(G)` means the claim-bounding scope cut over `EntityOfConcernRef` and scope; it is not an evidence-path slice and not a baseline-set slice.
- `threshold` is not one undifferentiated family here:
  - articulation and closure thresholds stay with cue or prompt governing patterns such as `B.4.1` and `B.5.2.0`
  - acceptance-gate thresholds stay with `G.4`
  - the work-measure threshold target used in specialization claims is only the declared success mark for the current task family or work target

**Name and kind map for code-shaped heads.** The names below identify different structural positions; capitalization does not make them peer kinds.

| Head used in this pattern | Recoverable kind or position | Direct governance boundary |
| --- | --- | --- |
| `TaskSignature@Context` | Context-local species of `U.Signature` and this pattern's primary EntityOfConcern | C.22 governs its A.6.0 four-row specialization; E.17 governs its publications and carriers. |
| `ProblemSideRecordRef` and `ReceivingUseDescription` | Positions of `TaskSignatureAssignmentRelation@Context`, not content or identity positions of `TaskSignature@Context` | C.22.2 or the direct problem-side pattern governs the problem episteme; the receiving-use description does not prove that the use occurred. |
| `TaskKind` | TaskSignature position filled by one exact C.3 `U.Kind` value that types the current problem or work target | C.3 governs the kind value; the field does not mint `U.Task`. |
| `TaskFamilyRef` | Optional reference position for the comparison-relevant task family | C.22 and C.22.1 govern task-family anchoring; the reference is not the family or a selected method. |
| `ProblemProfile` | `C.2.1`-conformant `U.Episteme` that describes the stabilized problem and may reference the TaskSignature assignment | It is not the problem, TaskSignature, assignment relation, method, plan, or work occurrence. |
| `ScopeSlice(G)` | Local field position whose filler is the current claim-bounding scope relation over the project `EntityOfConcernRef` | A.2.6 governs the scope relation; the field is not an E.18 path slice or a new slice kind. |
| CHR field heads in `5.1` | TaskSignature positions filled by characteristics, scales, units, polarity values, scope values, evidence relations, and currentness conditions | C.16 and each direct subject pattern govern the fillers; C.22 only states why the positions are needed by selector-facing use. |
| QD and OEE extension heads in `5.1` | Optional TaskSignature positions filled by exact characteristic-space, archive, policy, telemetry, generator-family, validity-region, and transfer-rule values or references | C.18, C.19, G.5, G.11, and the named direct patterns keep authority over those fillers. `ArchiveConfig`, `TelemetryHooks`, and `GeneratorIntent` do not become root kinds here. |

#### C.22:1.2 - ProblemCard@Context relation

`ProblemCard@Context` is the `C.22.2` problem-side record shape for stabilizing one context-bound problem representation before downstream Principles-to-Work (P2W).

A `ProblemCard@Context` episteme can be used to prepare the `TaskKind`, scope, and characteristic bindings for a candidate `TaskSignature@Context`. Assignment is admitted only when one signature is adequate for the named receiving use. If several signatures remain plausible, keep them as candidates under the selection or problem-framing pattern rather than asserting one `TaskSignatureAssignmentRelation@Context`.

`TaskSignatureAssignmentRelation@Context` does not move problem-card claims into the TaskSignature. The signature keeps only its four-row task declaration. `ProblemCard@Context` remains the reviewable problem-side episteme that explains why this problem can proceed to characterization, comparison, search, refresh, retirement, or another governing pattern.

The corresponding claims are governed by their named governing patterns.

