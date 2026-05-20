---
chunk_kind: "child"
pattern_id: "A.6.A"
pattern_title: "U.ActionInvitationPrecisionRestoration - Affordance / Action-Invitation Precision Restoration (ACT-INV)"
section_id: "A.6.A:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.A/A.6.A__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.6.A — U.ActionInvitationPrecisionRestoration - Affordance / Action-Invitation Precision Restoration (ACT-INV)"
  - "A.6.A:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 14161
line_end: 14172
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.3"
  - "A.6.B"
  - "A.6.P"
  - "A.6.Q"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.17"
  - "E.18"
  - "F.9"
keywords:
  - "A.15 docking"
  - "action invitation"
  - "action-first language"
  - "affordance"
  - "language-state seam"
  - "post-threshold classification"
---

### A.6.A:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern                   | Symptom                                                                                     | Why it fails                                           | How to avoid / repair                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------- |
| **Object-property affordance** | “The object is actionable” with no enactor or site frame                                    | collapses relationality into monadic property language | publish site + enactor + action + coupling frame               |
| **Invitation-as-obligation**   | “This calls for rollback” is treated as if rollback is already required                     | hides A/D routing and accountability                   | publish `actionInvitation(...)`, then route duty/gate via A.6.B |
| **Invitation-as-work**         | “The system reacted” is used where only a cue or option exists                              | confuses offer with execution                          | keep invitation separate from A.15 / `U.Work`                   |
| **Capability-as-invitation**   | “The robot can do X” stands in for a situated affordance                                    | destroys local enactor/site conditions                 | separate capability description from action invitation          |
| **Latent cue as explanation**  | a model tendency is narrated as if it were already an explicit rationale                    | overstates articulation and evidence                   | keep as `CuePack` or `OptionSet` until further articulation     |
| **Premature automation**       | an under-supported cue is wired directly into gates or controllers with no explicit hook `authoritySourceRef` target or guard | creates unsafe action pathways                         | require `PolicyHook` + A.6.B routing + witnesses                |
| **ArticulationHint as F proxy**| `hook-explicit` is read as “more formal”                                                    | recreates a forbidden second formality characteristic          | keep F in C.2.3; reserve articulation/closure semantics for `A.16` |

