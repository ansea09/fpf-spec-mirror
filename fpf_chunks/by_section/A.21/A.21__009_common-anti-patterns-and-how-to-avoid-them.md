---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "GateProfilization: OperationalGate(profile) (GateFit core)"
section_id: "A.21:7.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.21 — GateProfilization: OperationalGate(profile) (GateFit core)"
  - "A.21:7.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 29883
line_end: 29891
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.7"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "CV⇒GF"
  - "DecisionLog"
  - "EquivalenceWitness"
  - "GateChecks"
  - "GateDecision"
  - "GateFit"
  - "GateProfile"
  - "LaunchGate"
  - "OperationalGate"
  - "join-semilattice"
---

### A.21:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct move |
|---|---|---|
| Guard as GateCheck | A guard, status cue, or publication label is treated as a profile-bound gate check. | Declare the `GateCheckRef`, check criteria, fold policy, and governing neighboring truth condition. |
| Explanation as decision | A readable narrative is treated as the `GateDecision` or `DecisionLog`. | Keep `GateDecision`, `GateDecisionRationale`, optional explanation, and decision record distinct. |
| Gate pass as performed work | `GateDecision=pass` is read as work occurrence, release action, or work authorization. | Use A.21 only for the gate-decision relation and use A.15 or the release-governing pattern for work or authorization claims. |
| Profile drift by publication mode | `PublishMode=Lite` is read as a weaker `GateProfile`. | Keep publication-face reduction in E.17 and keep `GateProfile` fold policy explicit in A.21. |

