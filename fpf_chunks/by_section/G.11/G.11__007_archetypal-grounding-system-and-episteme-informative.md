---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
section_id: "G.11:5"
section_title: "Archetypal Grounding — System and Episteme (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__007_archetypal-grounding-system-and-episteme-informative.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "G.11 — Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
  - "G.11:5 — Archetypal Grounding — System and Episteme (informative)"
line_start: 131359
line_end: 131380
dependencies:
  - "A.10.1"
  - "A.6.RCD"
  - "B.3.4"
  - "C.11.DUA"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "C.32.P2S"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.12"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G11"
keywords:
  - "Bridge Sentinels"
  - "PathSlice"
  - "RSCR"
  - "deprecation"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
  - "use-qualified currentness"
---

### G.11:5 - Archetypal Grounding — System and Episteme (informative)

**`U.System` illustration — Safety-critical maintenance loop (pump and calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). The maintenance team uses `G.11` to produce a refresh plan scoped to the affected inspection slices and publishes a refresh report of the executed actions with pins to the updated standard edition and the evidence or source relations. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by subject pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review and benchmark pack (claims and parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Calibration evidence changes, potentially affecting a bounded-use claim or a justified loss consequence. The maintainers identify which receiving uses depend on the changed row, retain matching results that remain supported, and use the canonical triggers to plan any needed targeted parity rerun. Re-shipping follows only when the publication needs the resulting change; a CL revision alone grants or withdraws no use.

**Paired currentness case.** A pack's export-date label changes, but its relied-on claims, source editions, qualification conditions and receiving use remain unchanged and adequately supported by available information. Retain the result; no refresh plan, waiver or no-refresh notice is needed. In the paired case, a dependency changes so that the shipped benchmark comparison no longer supports use beyond its stated window. Restrict that comparison and retain the warning with the shipped result so a later receiver cannot infer continued comparability. Plan the targeted check or update when it is justified and obtainable; currentness reporting alone does not repair the comparison.

**Three bounded currentness cases.** These are constructed applications of the same rule.

* A pump shortlist still consumes the same two immutable method rows, eligibility conditions and source edition. An age alert supplies no changed premise or expired use condition, and the available support remains sufficient for the same triage use. Retain the shortlist; no plan or omission certificate is needed.
* A local selected-set result consumes `PumpReviewBudget-E1`. Its replacement `PumpReviewBudget-E2` changes the allowed review time from 30 to 20 minutes. The existing result explicitly cites that budget; no evidence graph is in use. Scope `PumpTriageSelection` names that exact result, changed budget and dependent eligibility comparison. If re-selection is chosen, plan only that comparison through G.5 under `PatternScopeId=PumpTriageSelection`, carrying both budget editions and the current task/row refs. Record performed refresh and any required targeted check in the resulting report before republication.
* A shipped QD archive expresses its affected dependencies in `PathSliceId=ArchiveCell-Q7`. A distance-definition change reopens the comparison using that definition. Retain the slice, old/new `DistanceDefRef.edition`, descriptor, insertion/emitter and policy pins, and the applicable G.9/G.10 evidence and shipping requirements. An OEE change to `TransferRulesRef.edition` similarly retains its affected graph slice, exact generator row edition and environment-validity scope. Nongraph support elsewhere does not relax these contracts.

**Shared calibration, different branch outcomes.** Continue G.6:5.5's constructed case. A correction to calibration qualification K establishes that its uncertainty statement applies only in the low-vibration condition. P1 and P2 both consume K, and selection S uses their acceptance results; P3 uses another calibration. The complete affected scope includes P1, P2 and S, while P3 retains its independent basis.

The inspection team checks the existing configuration records. The records show that M1 was obtained in the qualified condition, so the applicable measurement and acceptance rules preserve its supported result. M2 was obtained outside that condition; the old uncertainty statement cannot support V2 for the proposed use. Preserve the actual measurement history while returning its changed qualification to C.16 and the acceptance question to G.4. Reconsider S under G.5 because it consumed V2. A permissible shortlist restricted to the supported candidate can answer the immediate triage question; keeping P1 does not preserve the original two-candidate conclusion.

For a later decision that requires V2, the team compares using a qualified independent measurement already available, obtaining a new calibration or measurement, narrowing the planned use and deferring it. In this stipulated case, an available independent measurement covers the required conditions and its assessment fits the decision window; a full repeat campaign would arrive too late and adds no needed coverage. The team selects assessment of that measurement under the subject rules. If it supports V2, S can be reconsidered with both supported branches. If it does not, retain the warranted restricted result. Record a new observation or performed refresh only when it actually occurs; the plan and the available measurement remain distinct.

