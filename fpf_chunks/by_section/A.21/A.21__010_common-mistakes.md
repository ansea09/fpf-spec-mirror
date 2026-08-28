---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:8"
section_title: "Common mistakes"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__010_common-mistakes.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:8 — Common mistakes"
line_start: 34600
line_end: 34611
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:8 - Common mistakes

| Mistake | Why it fails | Repair |
| --- | --- | --- |
| Green cue as pass | No result, profile application, or check set is recoverable. | Recover the A.21 result or leave the cue non-decisional. |
| Merge by check label | Different subjects, criteria, regulators, or cases disappear. | Merge only identical check-application identities. |
| Unknown as `abstain` | A missing required fact becomes neutral and may yield pass. | Preserve `unknown`; apply an explicit profile rule. |
| New slice weakens checks | Locality is mistaken for policy authority. | Cite another applicable policy fact and any required authority. |
| `degrade` with no action | The word sounds precise but gives no usable consequence. | State the permitted restricted action, condition, stop, and recheck. |
| Every gate is a LaunchGate or crossing | Optional branches become universal infrastructure. | Activate only the branch present in the decision subject and selected structure. |
| Every crossing has a Bridge | Structural and semantic relations are collapsed. | Use E.18 for the crossing and F.9 only for a separate semantic relation. |

