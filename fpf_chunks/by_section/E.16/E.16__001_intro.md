---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__001_intro.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:intro — Intro"
line_start: 79242
line_end: 79249
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.24"
  - "C.9"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.17"
  - "F.4"
  - "F.6"
  - "F.8"
  - "G.10"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "autonomy budget"
  - "autonomy ledger"
  - "guarded enactment"
  - "override speech act"
  - "scout/probe/commit checkpoint"
---

## E.16 - RoC‑Autonomy Budget & Enforcement

**Intent.** Make an autonomy claim testable and enforceable through a published **AutonomyBudgetDecl**, guarded enactment, override SpeechActs with separation of duties, and a Work-anchored **AutonomyLedger**.
**Rule (summary).** If a claim calls a local system-role kind, Method, or Service autonomous, read it as a claim about Work a System may perform without continuous human direction. Authors **MUST**: (i) publish an `AutonomyBudgetDecl` that names the claim, working situation, scope, window, policy, budget, and override rule; (ii) say whether it is prospective or bound to actual enactment; (iii) gate Method steps with `requiresAutonomyBudget`; (iv) write an `AutonomyLedgerEntry` for admitted Work; (v) block on depletion until a `ResumeAutonomy` SpeechAct passes the guards, the declared separation-of-duties check, and the independent authority check; and (vi) surface the autonomy fields in UTS rows.

**Builds on:** A.2 / A.2.1 / A.2.5 / A.2.7 / A.15 / A.21; B.3; C.16; E.8; E.10; E.18; F.4; F.6; F.8; F.15; F.17.
**Coordinates with:** A.13 (Agential Role) and A.17/A.18/A.19/C.16/A.10 for current agency characterization, measurement, and evidence; planned C.9 (Agency Characteristic Profile) only as future consolidation; C.24 (Agent-Tools-CAL) where applicable; G.4, G.5, G.8, G.9, and G.10 (method authoring, selection, and shipping).

