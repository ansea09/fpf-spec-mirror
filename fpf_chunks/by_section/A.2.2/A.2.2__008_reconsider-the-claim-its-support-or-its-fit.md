---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:7"
section_title: "Reconsider the Claim, Its Support or Its Fit"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__008_reconsider-the-claim-its-support-or-its-fit.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:7 — Reconsider the Claim, Its Support or Its Fit"
line_start: 4311
line_end: 4326
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "E.23.CDI"
keywords:
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "work conditions"
---

### A.2.2:7 - Reconsider the Claim, Its Support or Its Fit

Reopen the value whose governing conditions changed. A different holder changes the subject. Configuration, calibration, wear, staffing, training or environment may change actual ability; evidence and qualification affect warranted reliance; the receiving demand affects fit. Assignment state and authority can separately defeat Work admission while ability remains.

The following constructed cases keep those changes apart:

| Change | Result |
|---|---|
| A new test supports the same measured performance under the same conditions. | Support changes; no changed ability is inferred. |
| A holder has supported throughput 10 units/min; demand rises from 8 to 12 under the same conditions. | The earlier demand fits that bound and the later demand does not. The holder's ability claim is unchanged. |
| Recalibration or configuration changes what precision the holder can attain while its old report remains. | Actual ability may change; reassess the predicate and the report's applicability. Unchanged paperwork does not fix the truth. |
| A fault makes the named ability predicate false at t1; repair restores it at t2. | State loss and recovery for the same holder under those times and conditions. No capability-individual continuity decision is needed. |
| RobotArm_A is replaced by RobotArm_B. | The assertion has a different subject; support for A does not automatically establish B's ability. |

A qualification window expiring may require new support or narrower reliance. An input outside the declared WorkScope defeats this fit basis. A changed Method can change the required bounds without changing the holder. A development intervention may be performed while its target remains unmet; a later successful comparison alone does not establish which intervention caused improvement. Use E.23.CDI and E.23.CAE for those development and attribution questions.

